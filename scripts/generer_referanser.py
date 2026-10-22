#!/usr/bin/env python3
"""Bygger referansefilene (gen-*.md) til skillene fra docs/ og kilde/.

Bruk:
    python scripts/generer_referanser.py

Filene skrives til plugin/skills/<skill>/references/ og committes ikke.
Hver fil starter med byggedato og commit, så skillene kan oppgi hvor gammel kunnskapen er.
Avslutter med kode 1 hvis et flytkort ikke heter edi_… eller intern_…, siden det da ikke
kommer med i referansene til triage-skillene.
"""
from __future__ import annotations

import csv
import io
import os
import re
import subprocess
from datetime import date
from pathlib import Path

ROT = Path(__file__).resolve().parent.parent
DOCS = ROT / "docs"
KILDE = ROT / "kilde"
SKILLS = ROT / "plugin" / "skills"

# Hvilke referanser hver skill får.
PLAN = {
    "edi-triage": ["flyter-edi", "runbooks", "partnere", "kalender", "kontakter", "eksempler", "kilde-indeks"],
    "intern-triage": [
        "flyter-intern", "systemer", "runbooks", "status", "kalender", "kontakter", "eksempler", "kilde-indeks",
    ],
    "flytkart": ["flyter", "partnere", "systemer", "status", "kilde-indeks"],
}

FLYT_PREFIKSER = ("edi_", "intern_")
MAKS_TEGN_PER_EKSEMPEL = 200_000
MAKS_TEGN_EKSEMPLER = 3_000_000
FILNAVN_RE = re.compile(r"^(PRD|TST)_(\d{4}-\d{2}-\d{2})_([^_]+)_(.+)$")
SIST_VERIFISERT_RE = re.compile(r"^\|\s*Sist verifisert\s*\|\s*([^|]*?)\s*\|", re.M | re.I)
UTEN_NAVNEKONVENSJON = {"eksempler", "partnere", "systemer"}
SPRAK = {".xml": "xml", ".json": "json"}


def bygginfo() -> tuple[str, str]:
    commit = os.environ.get("GITHUB_SHA", "")[:7]
    if not commit:
        try:
            commit = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"],
                cwd=ROT, capture_output=True, text=True, timeout=10,
            ).stdout.strip()
        except (OSError, subprocess.SubprocessError):
            commit = ""
    return date.today().isoformat(), commit or "ikke committet"


BYGGEDATO, COMMIT = bygginfo()


def rel(sti: Path) -> str:
    return sti.relative_to(ROT).as_posix()


def celle(tekst: str) -> str:
    return tekst.replace("|", "\\|").replace("\n", " ").strip()


def hode(tittel: str, kilde: str) -> str:
    return (
        "<!-- Generert av scripts/generer_referanser.py. Ikke rediger her – endre kildene i docs/ eller kilde/. -->\n"
        f"# {tittel}\n\n"
        f"Bygget {BYGGEDATO} fra commit {COMMIT}. Kilde: `{kilde}`.\n\n"
    )


def dokumenter(mappe: Path, prefiks: str = "") -> list[Path]:
    if not mappe.is_dir():
        return []
    return sorted(
        p for p in mappe.glob(f"{prefiks}*.md")
        if not p.name.startswith("_") and p.name.lower() != "readme.md"
    )


def tittel_fra(tekst: str, reserve: str) -> str:
    treff = re.search(r"^#\s+(.+)$", tekst, re.M)
    return treff.group(1).strip() if treff else reserve


def senk_overskrifter(tekst: str) -> str:
    """Kildefilene starter med én H1. I samlefilene flyttes alle overskrifter ett nivå ned."""
    ut, i_kodeblokk = [], False
    for linje in tekst.splitlines():
        if linje.lstrip().startswith("```"):
            i_kodeblokk = not i_kodeblokk
        if not i_kodeblokk and re.match(r"^#{1,5}\s", linje):
            linje = "#" + linje
        ut.append(linje)
    return "\n".join(ut)


def samle(mappe: Path, tittel: str, prefiks: str = "") -> str:
    """Samler dokumentene i en mappe. Med prefiks tas bare filer som starter med det."""
    filer = dokumenter(mappe, prefiks)
    ut = hode(tittel, rel(mappe) + "/" + (f"{prefiks}*.md" if prefiks else ""))
    if not filer:
        return ut + "_Ingen dokumenter ennå._\n"
    ut += "| Dokument | Fil | Sist verifisert |\n| --- | --- | --- |\n"
    tekster = []
    for fil in filer:
        tekst = fil.read_text(encoding="utf-8")
        treff = SIST_VERIFISERT_RE.search(tekst)
        verifisert = treff.group(1) if treff and treff.group(1) else "ikke oppgitt"
        ut += f"| {celle(tittel_fra(tekst, fil.stem))} | `{rel(fil)}` | {celle(verifisert)} |\n"
        tekster.append((fil, tekst))
    for fil, tekst in tekster:
        ut += f"\n---\n\n<!-- Kilde: {rel(fil)} -->\n\n{senk_overskrifter(tekst.strip())}\n"
    return ut


def enkeltfil(fil: Path, tittel: str) -> str:
    ut = hode(tittel, rel(fil))
    if not fil.is_file():
        return ut + "_Filen finnes ikke ennå._\n"
    return ut + senk_overskrifter(fil.read_text(encoding="utf-8").strip()) + "\n"


def navnefeil() -> list[str]:
    """Flytkort som ikke starter med edi_ eller intern_, og derfor ikke når triage-skillene."""
    return [
        f"{rel(p)}: flytkort må hete edi_… eller intern_… med små bokstaver (se docs/flyter/README.md)"
        for p in dokumenter(DOCS / "flyter")
        if not p.name.startswith(FLYT_PREFIKSER)
    ]


def uten_endelser(navn: str) -> str:
    return navn.split(".", 1)[0] if "." in navn else navn


def kildefiler() -> list[Path]:
    """Filer i kilde/ som git ikke ignorerer. Uten git: alle filer."""
    try:
        svar = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z", "--", "kilde"],
            cwd=ROT, capture_output=True, text=True, timeout=30, check=True,
        )
        filer = [ROT / s for s in svar.stdout.split("\0") if s]
    except (OSError, subprocess.SubprocessError):
        filer = [p for p in KILDE.rglob("*") if p.is_file()]
    return sorted(
        p for p in filer
        if p.is_file() and not p.name.startswith((".", "_")) and p.name.lower() != "readme.md"
    )


def kilde_indeks() -> str:
    ut = hode("Eksporter og andre kildefiler i repoet", "kilde/")
    rader = []
    for fil in kildefiler():
        omrade = fil.relative_to(KILDE).parts[0]
        treff = FILNAVN_RE.match(uten_endelser(fil.name))
        if treff:
            miljo, dato, type_, navn = treff.groups()
        elif omrade in UTEN_NAVNEKONVENSJON:
            miljo, dato, type_, navn = "–", "–", fil.parent.relative_to(KILDE).as_posix(), fil.name
        else:
            miljo, dato, type_, navn = "–", "–", "–", f"{fil.name} (følger ikke navnekonvensjonen)"
        kb = max(1, round(fil.stat().st_size / 1024))
        rader.append(f"| `{rel(fil)}` | {miljo} | {dato} | {celle(type_)} | {celle(navn)} | {kb} kB |")
    if not rader:
        return ut + "_Ingen eksporter ennå._\n"
    return (
        ut
        + "| Fil | Miljø | Dato | Type | Navn | Størrelse |\n| --- | --- | --- | --- | --- | --- |\n"
        + "\n".join(rader)
        + "\n"
    )


def status() -> str:
    mappe = KILDE / "ion" / "status"
    ut = hode("Status i ION (aktiv/inaktiv)", rel(mappe) + "/")
    filer = sorted(p for p in mappe.glob("*.csv") if not p.name.startswith("_")) if mappe.is_dir() else []
    if not filer:
        return ut + "_Ingen statuslister ennå._\n"
    for fil in filer:
        tekst = fil.read_text(encoding="utf-8-sig")
        forste_linje = tekst.splitlines()[0] if tekst.strip() else ""
        try:
            dialekt = csv.Sniffer().sniff(forste_linje, delimiters=";,\t")
        except csv.Error:
            dialekt = csv.excel
        rader = [r for r in csv.reader(io.StringIO(tekst), dialekt) if any(c.strip() for c in r)]
        ut += f"## {fil.stem}\n\n"
        if len(rader) < 2:
            ut += "_Tom liste._\n\n"
            continue
        kolonner = rader[0]
        ut += "| " + " | ".join(celle(c) for c in kolonner) + " |\n"
        ut += "|" + " --- |" * len(kolonner) + "\n"
        for rad in rader[1:]:
            rad = (rad + [""] * len(kolonner))[: len(kolonner)]
            ut += "| " + " | ".join(celle(c) for c in rad) + " |\n"
        ut += "\n"
    return ut


def eksempler() -> str:
    mappe = KILDE / "eksempler"
    ut = hode("Anonymiserte eksempler", rel(mappe) + "/")
    filer = [p for p in kildefiler() if p.parent == mappe and ".anon." in p.name]
    if not filer:
        return ut + "_Ingen eksempler ennå._\n"
    brukt = 0
    for fil in filer:
        try:
            tekst = fil.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            tekst = fil.read_text(encoding="latin-1")
        if brukt + min(len(tekst), MAKS_TEGN_PER_EKSEMPEL) > MAKS_TEGN_EKSEMPLER:
            ut += f"\n_Flere eksempler i `{rel(mappe)}/` er utelatt for å holde størrelsen nede._\n"
            break
        avkortet = len(tekst) > MAKS_TEGN_PER_EKSEMPEL
        tekst = tekst[:MAKS_TEGN_PER_EKSEMPEL]
        brukt += len(tekst)
        sprak = SPRAK.get(fil.suffix.lower(), "text")
        ut += f"\n## {fil.name}\n\n```{sprak}\n{tekst.rstrip()}\n```\n"
        if avkortet:
            ut += "\n_Avkortet._\n"
    return ut


BYGGERE = {
    "flyter": lambda: samle(DOCS / "flyter", "Flytkort – alle flyter"),
    "flyter-edi": lambda: samle(DOCS / "flyter", "Flytkort – EDI", "edi_"),
    "flyter-intern": lambda: samle(DOCS / "flyter", "Flytkort – interne flyter", "intern_"),
    "systemer": lambda: samle(DOCS / "systemer", "Systemkort – interne systemer"),
    "runbooks": lambda: samle(DOCS / "runbooks", "Runbooks"),
    "partnere": lambda: samle(DOCS / "partnere", "Partnere"),
    "kalender": lambda: enkeltfil(DOCS / "kalender.md", "Utløpskalender"),
    "kontakter": lambda: enkeltfil(DOCS / "kontakter.md", "Kontakter og eskalering"),
    "eksempler": eksempler,
    "kilde-indeks": kilde_indeks,
    "status": status,
}


def bygg() -> list[str]:
    """Bygger referansene. Returnerer feil som skal stoppe bygget."""
    feil = navnefeil()
    ferdige: dict[str, str] = {}
    for skill, referanser in PLAN.items():
        if not (SKILLS / skill / "SKILL.md").is_file():
            print(f"Hopper over {skill}: finnes ikke i plugin/skills")
            continue
        mappe = SKILLS / skill / "references"
        mappe.mkdir(parents=True, exist_ok=True)
        for gammel in mappe.glob("gen-*"):
            gammel.unlink()
        for navn in referanser:
            if navn not in ferdige:
                ferdige[navn] = BYGGERE[navn]()
            with open(mappe / f"gen-{navn}.md", "w", encoding="utf-8", newline="\n") as f:
                f.write(ferdige[navn])
        print(f"{skill}: {len(referanser)} referansefiler bygget")
    for melding in feil:
        print(f"FEIL {melding}")
    return feil


def main() -> int:
    return 1 if bygg() else 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Sjekker skills mot grensene i Copilot Cowork.

Bruk:
    python scripts/sjekk_grenser.py            # sjekker plugin/skills og overgang
    python scripts/sjekk_grenser.py <mappe>    # sjekker skills i en valgfri mappe

Avslutter med kode 1 hvis noe bryter grensene.
Grensene er hentet fra «Build plugins for Copilot Cowork» (Microsoft Learn).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROT = Path(__file__).resolve().parent.parent

MAKS_SKILLS_PER_PLUGIN = 20
MAKS_TILLEGGSFILER = 20
MAKS_FILSTORRELSE = 5 * 1024 * 1024
MAKS_TOTALT = 10 * 1024 * 1024
MAKS_SKILL_MD = 1024 * 1024
MAKS_BESKRIVELSE = 1024
MAKS_NAVN = 64
ANBEFALT_MAKS_TEGN = 20_000  # ca. 5 000 tokens i selve SKILL.md-teksten

NAVN_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TRYGT_FILNAVN_RE = re.compile(r"^[A-Za-z0-9._ !-]+$")
RESERVERTE_NAVN = (
    {"CON", "PRN", "AUX", "NUL"}
    | {f"COM{i}" for i in range(1, 10)}
    | {f"LPT{i}" for i in range(1, 10)}
)


def vis(sti: Path) -> str:
    try:
        return sti.relative_to(ROT).as_posix()
    except ValueError:
        return sti.as_posix()


def les_frontmatter(tekst: str) -> tuple[dict[str, str] | None, str]:
    """Returnerer (felter, brødtekst). felter er None hvis frontmatter mangler."""
    tekst = tekst.lstrip("﻿").replace("\r\n", "\n")
    treff = re.match(r"---[ \t]*\n(.*?)\n---[ \t]*(?:\n|$)", tekst, re.S)
    if not treff:
        return None, tekst
    linjer = treff.group(1).split("\n")
    brodtekst = tekst[treff.end():]
    felter: dict[str, str] = {}
    i = 0
    while i < len(linjer):
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", linjer[i])
        if not m:
            i += 1
            continue
        nokkel, verdi = m.group(1), m.group(2).strip()
        if verdi[:1] in ("|", ">"):
            brettet = verdi.startswith(">")
            deler = []
            i += 1
            while i < len(linjer) and (linjer[i][:1] in (" ", "\t") or not linjer[i].strip()):
                deler.append(linjer[i].strip())
                i += 1
            felter[nokkel] = (" " if brettet else "\n").join(deler).strip()
            continue
        if len(verdi) >= 2 and verdi[0] == verdi[-1] and verdi[0] in "\"'":
            verdi = verdi[1:-1]
        felter[nokkel] = verdi
        i += 1
    return felter, brodtekst


def sjekk_skill(mappe: Path) -> tuple[list[str], list[str], str | None]:
    feil: list[str] = []
    advarsler: list[str] = []
    skill_md = mappe / "SKILL.md"
    sted = vis(mappe)
    if not skill_md.is_file():
        return [f"{sted}: mangler SKILL.md"], advarsler, None

    if skill_md.stat().st_size > MAKS_SKILL_MD:
        feil.append(f"{sted}: SKILL.md er større enn 1 MB")

    felter, brodtekst = les_frontmatter(skill_md.read_text(encoding="utf-8"))
    navn = None
    if felter is None:
        feil.append(f"{sted}: SKILL.md mangler frontmatter mellom to linjer med ---")
    else:
        navn = felter.get("name") or None
        beskrivelse = felter.get("description", "")
        if not navn:
            feil.append(f"{sted}: mangler name i frontmatter")
        else:
            if navn != mappe.name:
                feil.append(f"{sted}: name «{navn}» er ulik mappenavnet «{mappe.name}»")
            if not NAVN_RE.match(navn):
                feil.append(f"{sted}: name «{navn}» må være kebab-case (små bokstaver, tall og bindestrek)")
            if len(navn) > MAKS_NAVN:
                feil.append(f"{sted}: name er lengre enn {MAKS_NAVN} tegn")
        if not beskrivelse:
            feil.append(f"{sted}: mangler description i frontmatter")
        elif len(beskrivelse) > MAKS_BESKRIVELSE:
            feil.append(f"{sted}: description har {len(beskrivelse)} tegn (maks {MAKS_BESKRIVELSE})")
        if len(brodtekst) > ANBEFALT_MAKS_TEGN:
            advarsler.append(
                f"{sted}: SKILL.md har {len(brodtekst)} tegn tekst – flytt detaljer til references/"
            )

    filer = [p for p in sorted(mappe.rglob("*")) if p.is_file() and p != skill_md]
    if len(filer) > MAKS_TILLEGGSFILER:
        feil.append(f"{sted}: {len(filer)} tilleggsfiler (maks {MAKS_TILLEGGSFILER})")
    totalt = 0
    for fil in filer:
        relativ = fil.relative_to(mappe)
        storrelse = fil.stat().st_size
        totalt += storrelse
        if storrelse > MAKS_FILSTORRELSE:
            feil.append(f"{sted}/{relativ.as_posix()}: større enn 5 MB")
        for del_ in relativ.parts:
            if del_.startswith("."):
                feil.append(f"{sted}/{relativ.as_posix()}: skjulte filer og mapper er ikke tillatt")
            elif not TRYGT_FILNAVN_RE.match(del_):
                feil.append(f"{sted}/{relativ.as_posix()}: ugyldige tegn i navnet «{del_}»")
            elif del_.split(".")[0].upper() in RESERVERTE_NAVN:
                feil.append(f"{sted}/{relativ.as_posix()}: «{del_}» er et reservert navn i Windows")
    if totalt > MAKS_TOTALT:
        feil.append(f"{sted}: tilleggsfilene er {totalt / 1024 / 1024:.1f} MB til sammen (maks 10 MB)")
    return feil, advarsler, navn


def sjekk(mapper: list[Path]) -> list[str]:
    alle_feil: list[str] = []
    for mappe in mapper:
        if not mappe.is_dir():
            continue
        undermapper = sorted(p for p in mappe.iterdir() if p.is_dir() and not p.name.startswith("."))
        if mappe.name == "skills" and len(undermapper) > MAKS_SKILLS_PER_PLUGIN:
            alle_feil.append(f"{vis(mappe)}: {len(undermapper)} skills (maks {MAKS_SKILLS_PER_PLUGIN} per plugin)")
        sett: dict[str, Path] = {}
        for skill in undermapper:
            feil, advarsler, navn = sjekk_skill(skill)
            for melding in advarsler:
                print(f"ADVARSEL {melding}")
            if navn and navn in sett:
                feil.append(f"{vis(skill)}: navnet «{navn}» er også brukt i {vis(sett[navn])}")
            elif navn:
                sett[navn] = skill
            alle_feil.extend(feil)
        print(f"Sjekket {len(undermapper)} skill(s) i {vis(mappe)}")
    for melding in alle_feil:
        print(f"FEIL {melding}")
    return alle_feil


def main(argv: list[str]) -> int:
    mapper = [Path(a).resolve() for a in argv] or [ROT / "plugin" / "skills", ROT / "overgang"]
    feil = sjekk(mapper)
    if feil:
        print(f"{len(feil)} feil.")
        return 1
    print("Alle skills er innenfor grensene.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

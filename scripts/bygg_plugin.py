#!/usr/bin/env python3
"""Bygger referanser, sjekker navn og grenser, og pakker pluginen som zip.

Bruk:
    python scripts/bygg_plugin.py              # lager dist/<navn>-<versjon>.zip
    python scripts/bygg_plugin.py --kun-sjekk  # bygger referanser og sjekker, uten zip
"""
from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import generer_referanser  # noqa: E402
import sjekk_grenser  # noqa: E402

ROT = Path(__file__).resolve().parent.parent
PLUGIN = ROT / "plugin"
DIST = ROT / "dist"
MED_I_PAKKEN = (".claude-plugin", "skills")


def pakk() -> Path:
    meta = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    navn, versjon = meta["name"], meta["version"]
    DIST.mkdir(exist_ok=True)
    zip_sti = DIST / f"{navn}-{versjon}.zip"
    filer = [
        p for p in sorted(PLUGIN.rglob("*"))
        if p.is_file() and p.relative_to(PLUGIN).parts[0] in MED_I_PAKKEN
    ]
    mcp = PLUGIN / ".mcp.json"
    if mcp.is_file():
        filer.append(mcp)
    with zipfile.ZipFile(zip_sti, "w", zipfile.ZIP_DEFLATED) as z:
        for fil in filer:
            z.write(fil, fil.relative_to(PLUGIN).as_posix())
    print(f"Pakket {len(filer)} filer i {zip_sti.relative_to(ROT).as_posix()}")
    return zip_sti


def main(argv: list[str]) -> int:
    feil = generer_referanser.bygg()
    feil += sjekk_grenser.sjekk([PLUGIN / "skills", ROT / "overgang"])
    if feil:
        print(f"Stopper: {len(feil)} feil.")
        return 1
    if "--kun-sjekk" in argv:
        print("Sjekk fullført.")
        return 0
    pakk()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

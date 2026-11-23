#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resum en Markdown de l'estat de l'arxivament i de la verificació (s'escriu a la branca wayback-dades)."""
from __future__ import annotations

import argparse
import collections
import csv
from datetime import datetime, timezone
from pathlib import Path


def llegeix(p: Path) -> list[dict]:
    if not p or not p.is_file():
        return []
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--resultats", type=Path, required=True)
    ap.add_argument("--verificacio", type=Path)
    ap.add_argument("--entrada", type=Path)
    ap.add_argument("--commit", default="")
    ap.add_argument("--run", default="")
    a = ap.parse_args()

    res = llegeix(a.resultats)
    ultim = {}
    for r in res:
        ultim[(r.get("url") or "").strip()] = r
    ent = {(r.get("url") or "").strip() for r in llegeix(a.entrada)}
    ver = llegeix(a.verificacio)

    print("# Estat de l'arxivament a Wayback i de la verificació de cites\n")
    print(f"- Generat: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}; execució `{a.run}`; codi de `main` `{a.commit[:7]}`.")
    print("- Fitxers: `resultats_arxiu.csv` (una fila per URL i intent; mana l'última), `verificacio_cites.csv` "
          "(una fila per ISIN-any, camp, URL i cita).\n")
    print("## Arxivament\n")
    c = collections.Counter((r.get("estat") or "") for r in ultim.values())
    amb = {u for u, r in ultim.items() if r.get("estat") in ("ja_existia", "capturada") and (r.get("url_wayback") or "").strip()}
    print("| | URL |")
    print("|---|---:|")
    print(f"| URL de les fonts amb cita (entrada d'aquesta execució) | {len(ent)} |")
    print(f"| … amb captura a Wayback | {len(ent & amb)} |")
    print(f"| … sense captura encara | {len(ent - amb)} |")
    for k, v in sorted(c.items()):
        print(f"| Estat `{k}` (totes les URL tractades) | {v} |")
    print("\n## Verificació de la cita a la captura\n")
    cv = collections.Counter((r.get("estat") or "") for r in ver)
    print("| Estat | Parells |")
    print("|---|---:|")
    for k, v in sorted(cv.items(), key=lambda x: -x[1]):
        print(f"| `{k}` | {v} |")
    print(f"| **Total** | {len(ver)} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

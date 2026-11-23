#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Llista les URL del registre que encara no tenen la cita verificada a una captura Wayback.

Serveix d'entrada per a la passada d'arxivament (script `wayback_arxiva.py`, que només
es pot executar on hi ha les claus) i per a la verificació de cites a la captura.

Una URL entra a la llista si alguna entrada del registre amb cita i `url_font` http(s)
(funcions `ceo`, `fundador`, `context` o `datacio`) no té `cita_verificada_a_captura=si`.
No fa cap petició de xarxa.

  python3 estat/llista_urls_arxiu.py      # escriu estat/urls_per_arxivar.csv
"""
from __future__ import annotations

import collections
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "docs" / "REGISTRE_CANVIS.csv"
OUT = ROOT / "estat" / "urls_per_arxivar.csv"
FUNCIONS = {"ceo", "fundador", "context", "datacio"}


def main() -> int:
    with REG.open(encoding="utf-8", newline="") as f:
        reg = list(csv.DictReader(f))
    info: dict[str, dict] = {}
    verificada: set[str] = set()
    for e in reg:
        url = (e.get("url_font") or "").strip()
        if not url.lower().startswith(("http://", "https://")) or not (e.get("cita_literal") or "").strip():
            continue
        if e.get("funcio_cita") not in FUNCIONS:
            continue
        if e.get("cita_verificada_a_captura") == "si":
            verificada.add(url)
        d = info.setdefault(url, {"n": 0, "origens": set(), "funcions": set(), "wayback": set(), "isin": set()})
        d["n"] += 1
        d["origens"].add(e.get("origen") or "")
        d["funcions"].add(e.get("funcio_cita") or "")
        d["isin"].add(e.get("isin") or "")
        wb = (e.get("url_wayback") or "").strip()
        if wb.startswith("https://web.archive.org/web/"):
            d["wayback"].add(wb)
    files = []
    for url, d in info.items():
        if url in verificada:
            continue
        files.append({
            "url": url,
            "n_entrades": d["n"],
            "funcions": ";".join(sorted(d["funcions"])),
            "origens": ";".join(sorted(d["origens"])),
            "n_isin": len(d["isin"]),
            "url_wayback_al_registre": sorted(d["wayback"])[0] if d["wayback"] else "",
        })
    files.sort(key=lambda x: x["url"])
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(files[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(files)
    per_origen = collections.Counter(o for x in files for o in x["origens"].split(";"))
    print(f"URL al registre: {len(info)}; amb cita verificada a la captura: {len(verificada)}; "
          f"per arxivar o verificar: {len(files)} (sense url_wayback al registre: "
          f"{sum(1 for x in files if not x['url_wayback_al_registre'])}).")
    for o, n in sorted(per_origen.items()):
        print(f"  {o}: {n}")
    print(f"Escrit {OUT.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

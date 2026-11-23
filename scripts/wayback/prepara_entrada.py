#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepara l'entrada de wayback_arxiva.py: totes les URL de les fonts amb cita literal.

Fonts de les URL:
  - docs/REGISTRE_CANVIS.csv: `url_font` de les entrades amb `cita_literal`;
  - dades/base_isin_any_v8r3.csv: `font_classificacio_url` (amb cita) i `d37_cita_contemp_url`.

Columnes de sortida (format de wayback_arxiva.py): url, any_objectiu, captura_indicada,
url_wayback_indicada. Una fila per URL i any. `captura_indicada=1` si el registre ja hi
indica una captura de web.archive.org (l'arxivador la dona per feta sense consultar la xarxa).

No fa cap petició de xarxa.

  python3 scripts/wayback/prepara_entrada.py --sortida treball/entrada.csv
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def anys(text: str) -> list[str]:
    out = set()
    for a, z in re.findall(r"(\d{4})(?:\s*[-–]\s*(\d{4}))?", text or ""):
        if z:
            out.update(str(y) for y in range(int(a), int(z) + 1))
        else:
            out.add(a)
    return sorted(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", type=Path, default=ROOT / "dades" / "base_isin_any_v8r3.csv")
    ap.add_argument("--registre", type=Path, default=ROOT / "docs" / "REGISTRE_CANVIS.csv")
    ap.add_argument("--sortida", type=Path, required=True)
    args = ap.parse_args()

    files: dict[tuple[str, str], dict] = {}

    def afegeix(url: str, any_: str, wb: str = "") -> None:
        url = (url or "").strip()
        if not url.lower().startswith(("http://", "https://")) or "web.archive.org" in url:
            return
        k = (url, any_)
        f = files.setdefault(k, {"url": url, "any_objectiu": any_, "captura_indicada": "0", "url_wayback_indicada": ""})
        wb = (wb or "").strip()
        if wb.startswith(("https://web.archive.org/web/", "http://web.archive.org/web/")) and f["captura_indicada"] == "0":
            f["captura_indicada"] = "1"
            f["url_wayback_indicada"] = wb

    with args.registre.open(encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            if not (r.get("cita_literal") or "").strip():
                continue
            for y in anys(r.get("anys") or "") or [""]:
                afegeix(r.get("url_font") or "", y, r.get("url_wayback") or "")
    with args.base.open(encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            if (r.get("font_classificacio_cita") or "").strip():
                afegeix(r.get("font_classificacio_url") or "", r.get("any") or "")
            afegeix(r.get("d37_cita_contemp_url") or "", r.get("any") or "")

    args.sortida.parent.mkdir(parents=True, exist_ok=True)
    with args.sortida.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["url", "any_objectiu", "captura_indicada", "url_wayback_indicada"],
                           lineterminator="\n")
        w.writeheader()
        for k in sorted(files):
            w.writerow(files[k])
    n_url = len({k[0] for k in files})
    print(f"Files: {len(files)}; URL úniques: {n_url}. Escrit {args.sortida}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

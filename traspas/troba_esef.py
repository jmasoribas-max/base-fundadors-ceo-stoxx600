#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Troba l'informe anual oficial (ESEF) de l'exercici de cada fila d'un lot.

Els emissors de mercats regulats de la UE (i del Regne Unit fins al 2021) dipositen des de
l'exercici 2020 l'informe financer anual en format ESEF als dipòsits oficials nacionals (OAM).
filings.xbrl.org (XBRL International) en recull les còpies amb les metadades de l'exercici.
El document és l'informe anual de l'emissor (font A; allotjament `plataforma`).

  1. ISIN -> LEI amb l'API pública de GLEIF (memòria a traspas/isin_lei.csv, que es desa al repositori
     com a traçabilitat).
  2. LEI -> dipòsits ESEF amb l'API de filings.xbrl.org.
  3. Per a cada fila (ISIN, any) tria el dipòsit l'exercici del qual inclou el 31/10 de l'any:
     data de tancament entre el 31/10/any i el 30/10/any+1. Si n'hi ha diverses versions
     d'idioma, primer l'anglesa.

Surt un CSV isin,any,url,nivell,font,exercici per a traspas/extreu_ceo_documents.py --docs.

  python3 traspas/troba_esef.py lots/lot15.csv --sortida DOCS.csv --cache DIR
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ISIN_LEI = ROOT / "traspas" / "isin_lei.csv"
UA = "Mozilla/5.0 (X11; Linux x86_64) recerca-academica"


def baixa_json(url: str) -> dict | None:
    for intent in range(3):
        p = subprocess.run(["curl", "-sS", "--max-time", "60", "-A", UA, url], capture_output=True, text=True)
        if p.returncode == 0 and p.stdout.strip().startswith("{"):
            try:
                return json.loads(p.stdout)
            except json.JSONDecodeError:
                pass
        time.sleep(2 * (intent + 1))
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("lot")
    ap.add_argument("--sortida", required=True)
    ap.add_argument("--cache", required=True, help="carpeta per a les respostes de l'API (fora del repositori)")
    args = ap.parse_args()
    cache = Path(args.cache)
    cache.mkdir(parents=True, exist_ok=True)

    with (ROOT / args.lot).open(encoding="utf-8", newline="") as f:
        lot = [(r["isin"], int(r["any"])) for r in csv.DictReader(f)]
    isins = sorted({i for i, _ in lot})

    lei = {}
    if ISIN_LEI.exists():
        with ISIN_LEI.open(encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                lei[r["isin"]] = r
    avui = dt.date.today().isoformat()
    nous = 0
    for isin in isins:
        if isin in lei:
            continue
        d = baixa_json(f"https://api.gleif.org/api/v1/lei-records?filter%5Bisin%5D={isin}")
        if d is None:
            continue
        recs = d.get("data") or []
        lei[isin] = {"isin": isin, "lei": recs[0]["id"] if recs else "",
                     "nom_gleif": recs[0]["attributes"]["entity"]["legalName"]["name"] if recs else "",
                     "data_consulta": avui, "font": "api.gleif.org (filter[isin])"}
        nous += 1
        time.sleep(0.3)
    with ISIN_LEI.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["isin", "lei", "nom_gleif", "data_consulta", "font"], lineterminator="\n")
        w.writeheader()
        for isin in sorted(lei):
            w.writerow(lei[isin])
    print(f"ISIN: {len(isins)}; amb LEI: {sum(1 for i in isins if lei.get(i, {}).get('lei'))} (consultes noves: {nous})")

    dip = {}
    for isin in isins:
        l = lei.get(isin, {}).get("lei")
        if not l:
            continue
        fc = cache / f"esef_{l}.json"
        if fc.exists():
            dip[isin] = json.loads(fc.read_text(encoding="utf-8"))
            continue
        d = baixa_json(f"https://filings.xbrl.org/api/filings?filter%5Bentity.identifier%5D={l}&page%5Bsize%5D=100")
        if d is None:
            continue
        fc.write_text(json.dumps(d), encoding="utf-8")
        dip[isin] = d
        time.sleep(0.3)

    files = []
    sense = 0
    for isin, a in lot:
        d = dip.get(isin)
        if not d:
            sense += 1
            continue
        ini, fi = dt.date(a, 10, 31), dt.date(a + 1, 10, 30)
        cands = []
        for x in d.get("data", []):
            at = x["attributes"]
            try:
                pe = dt.date.fromisoformat(at["period_end"])
            except (TypeError, ValueError):
                continue
            if ini <= pe <= fi and at.get("report_url"):
                ru = at["report_url"]
                cands.append(((("-en" not in ru.lower()) and ("_en" not in ru.lower())), at.get("error_count") or 0, ru, at["period_end"]))
        if not cands:
            sense += 1
            continue
        cands.sort()
        for _, _, ru, pe in cands[:2]:
            files.append({"isin": isin, "any": a, "url": "https://filings.xbrl.org" + ru, "nivell": "A",
                          "font": "esef_filings.xbrl.org", "exercici": pe})
    with open(args.sortida, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["isin", "any", "url", "nivell", "font", "exercici"])
        w.writeheader()
        w.writerows(files)
    print(f"Files del lot: {len(lot)}; amb informe ESEF de l'exercici: {len({(r['isin'], r['any']) for r in files})}; sense: {sense}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

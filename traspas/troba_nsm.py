#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Troba l'informe anual de l'exercici de les files d'emissors britànics al dipòsit oficial de l'FCA (NSM).

Per a cada fila (ISIN, any) d'un emissor del Regne Unit, Jersey, Guernsey o l'illa de Man:
  1. cerca a l'API pública del National Storage Mechanism (api.data.fca.org.uk) els documents
     «Annual Financial Report» de l'empresa publicats entre l'1/1 de l'any i el 31/12 de l'any
     següent;
  2. baixa cada informe (mateixa memòria cau que traspas/importa_lot.py) i en llegeix la data de
     tancament de l'exercici al text («for the year ended 30 April 2017», «52 weeks ended …»);
  3. tria l'informe l'exercici del qual inclou el 31/10 de l'any de la fila: data de tancament
     entre el 31/10/any i el 30/10/any+1.
Surt un CSV isin,any,url,nivell,font,exercici per a traspas/extreu_ceo_documents.py --docs.

  python3 traspas/troba_nsm.py lots/lot17.csv --sortida DOCS.csv --cache DIR
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import importlib.util
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("importa_lot", ROOT / "traspas" / "importa_lot.py")
IL = importlib.util.module_from_spec(spec)
spec.loader.exec_module(IL)

MESOS = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august",
                                      "september", "october", "november", "december"], start=1)}
FI_EXERCICI = re.compile(r"(?:year|period|52 weeks|53 weeks|financial year)\s+(?:ended|ending)\s*:?\s*(?:on\s+)?"
                         r"(\d{1,2})(?:st|nd|rd|th)?\s+(" + "|".join(MESOS) + r")\s*,?\s+(20[12]\d)", re.I)


def nom_cerca(nom_panell: str) -> str:
    n = re.split(r"\s+(Registered|Reg\.|Shares|Shs|Ord|Ordinary|Namens|Inhaber|Actions|Aktie|Accions|Acciones)\b", nom_panell)[0]
    n = re.sub(r"\s+\(New\)|\s+\(The\)", "", n)
    return n.strip()


def nsm(company: str, des: str, fins: str) -> list[dict]:
    """Tots els documents de l'empresa entre les dues dates (amb paginació de 200 en 200, fins a 2.000)."""
    out = []
    for inici in range(0, 2000, 200):
        cos = {"from": inici, "size": 200, "primarySearch": [{"name": "company", "value": company}], "latestFlag": "Y",
               "criteriaObj": {"criteria": [], "dateCriteria": [{"name": "submitted_date",
                                                                  "value": {"from": f"{des}T00:00:00Z", "to": f"{fins}T23:59:59Z"}}]}}
        hits, total = None, 0
        for intent in range(3):
            p = subprocess.run(["curl", "-sS", "--max-time", "90", "-X", "POST", "https://api.data.fca.org.uk/search?index=nsm-search",
                                "-H", "Content-Type: application/json", "-d", json.dumps(cos)], capture_output=True, text=True)
            try:
                d = json.loads(p.stdout)
                hits, total = [h["_source"] for h in d["hits"]["hits"]], d["hits"]["total"]["value"]
                break
            except Exception:  # noqa: BLE001
                time.sleep(3 * (intent + 1))
        if not hits:
            break
        out += hits
        if inici + 200 >= total:
            break
    return out


def fi_exercici(t: str) -> dt.date | None:
    c = collections.Counter()
    for d, m, y in FI_EXERCICI.findall(t[:3_000_000]):
        try:
            c[dt.date(int(y), MESOS[m.lower()], int(d))] += 1
        except ValueError:
            pass
    if not c:
        return None
    # la data més citada; si n'hi ha diverses (comparatives), la més recent entre les dues més citades
    top = [d for d, _ in c.most_common(2)]
    return max(top) if len(top) == 2 and c[top[1]] >= c[top[0]] * 0.6 else top[0]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("lot")
    ap.add_argument("--sortida", required=True)
    ap.add_argument("--cache", required=True)
    args = ap.parse_args()
    IL.CACHE = Path(args.cache)
    with IL.BASE.open(encoding="utf-8", newline="") as f:
        base = {(r["isin"], r["any"]): r for r in csv.DictReader(f)}
    with (ROOT / args.lot).open(encoding="utf-8", newline="") as f:
        lot = [(r["isin"], int(r["any"])) for r in csv.DictReader(f)]
    files, sense = [], 0
    docs_isin: dict[str, dict] = {}
    for isin, a in lot:
        if isin[:2] not in ("GB", "JE", "GG", "IM"):
            continue
        nom = nom_cerca(base[(isin, str(a))].get("nom_panell") or "")
        cands = []
        for s in nsm(nom, f"{a}-01-01", f"{a + 1}-12-31"):
            if "Annual Financial Report" not in (s.get("type") or "") and "Annual Report" not in (s.get("headline") or ""):
                continue
            if not s.get("download_link"):
                continue
            url = "https://data.fca.org.uk/artefacts/" + s["download_link"].lstrip("/")
            cands.append(url)
        trobat = False
        for url in dict.fromkeys(cands):
            if url not in docs_isin:
                t = IL.text_cache(url)
                docs_isin[url] = {"fi": fi_exercici(t) if len(t) > 50_000 else None}
            fi = docs_isin[url]["fi"]
            if fi and dt.date(a, 10, 31) <= fi <= dt.date(a + 1, 10, 30):
                files.append({"isin": isin, "any": a, "url": url, "nivell": "A", "font": "fca_nsm", "exercici": fi.isoformat()})
                trobat = True
                break
        sense += not trobat
        time.sleep(0.3)
    with open(args.sortida, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["isin", "any", "url", "nivell", "font", "exercici"])
        w.writeheader()
        w.writerows(files)
    print(f"Files britàniques: {len(files) + sense}; amb informe de l'exercici: {len(files)}; sense: {sense}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

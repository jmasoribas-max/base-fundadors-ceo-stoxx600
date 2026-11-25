#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Porta al registre els resultats de l'arxivament i de la verificació a Wayback.

Entrades (CSV de la branca `wayback-dades`, carpeta `wayback/`, o de `wayback/` a main):
  --arxiu         resultats de wayback_arxiva.py (url, estat, timestamp_captura, url_wayback, ...)
  --verificacio   resultats de verifica_cites.py (isin, any, camp, url, url_wayback, estat, detall, cita, ...)

Per a cada entrada del registre amb cita i URL (camps `cita_literal` i `url_font`):
  - si la verificació dona `cita_ok` (la cita normalitzada és al text de la captura `id_`):
    `url_wayback`, `wayback_v8r1_estat` (existent/nova), `wayback_v8r1_origen=github_actions`,
    `wayback_v8r1_metode`, `wayback_v8r1_timestamp`, `cita_verificada_a_captura=si`;
  - si dona `cita_parcial` o `cita_no_trobada`: `cita_verificada_a_captura=no` i una nota
    (la captura existeix però no s'hi ha trobat la cita literal; pot ser una captura d'una altra
    versió del document);
  - si la captura no s'ha pogut llegir: no es toca res (queda pendent).
Amb `--flexible` (resultats de verifica_flexible.py, Claude, 25/11/2026), per a les entrades que no són `si`:
  - `cita_ok_altra_captura`: la cita és, exacta, en una altra captura de la mateixa URL → `si`, amb la URL
    d'aquesta captura;
  - `cita_ok_flexible` o `cita_ok_flexible_altra_captura`: la cita hi és amb la comparació flexible (espais,
    guions de final de línia o talls «[…]») → `si_flexible`, amb una nota.
No sobreescriu un `si` que ja hi fos. No toca FounderCEO ni `dades/`. Per defecte és una prova
en sec; amb --escriu modifica docs/REGISTRE_CANVIS.csv (mateix format, CRLF).

  python3 scripts/wayback/porta_al_registre.py --arxiu A.csv [A2.csv] --verificacio V.csv [V2.csv]
  python3 scripts/wayback/porta_al_registre.py --arxiu ... --verificacio ... --escriu
"""
from __future__ import annotations

import argparse
import collections
import csv
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REG = ROOT / "docs" / "REGISTRE_CANVIS.csv"


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip()


def timestamp(url_wb: str) -> str:
    m = re.search(r"/web/(\d{8,14})", url_wb or "")
    return m.group(1) if m else ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arxiu", nargs="+", default=[])
    ap.add_argument("--verificacio", nargs="+", required=True)
    ap.add_argument("--flexible", nargs="*", default=[])
    ap.add_argument("--escriu", action="store_true")
    args = ap.parse_args()

    arxiu = {}
    for p in args.arxiu:
        with open(p, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                if r.get("url_wayback"):
                    arxiu[r["url"]] = r
    ver = collections.defaultdict(list)
    for p in args.verificacio:
        with open(p, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                if (r.get("camp") or "").startswith("registre.url_font"):
                    ver[(r["url"], norm(r.get("cita")))].append(r)

    flex = {}
    for p in args.flexible:
        with open(p, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                if (r.get("camp") or "").startswith("registre.url_font") and r.get("estat_flexible", "").startswith("cita_ok"):
                    k = (r["url"], norm(r.get("cita")))
                    # preferència: estricta en una altra captura > flexible a la vigent > flexible en una altra
                    ordre = {"cita_ok_altra_captura": 0, "cita_ok_flexible": 1, "cita_ok_flexible_altra_captura": 2}
                    if k not in flex or ordre[r["estat_flexible"]] < ordre[flex[k]["estat_flexible"]]:
                        flex[k] = r

    raw = REG.read_bytes().decode("utf-8")
    files = list(csv.reader(io.StringIO(raw, newline="")))
    cap = files[0]
    c = {k: i for i, k in enumerate(cap)}
    res = collections.Counter()
    for r in files[1:]:
        cita, url = norm(r[c["cita_literal"]]), r[c["url_font"]].strip()
        if not cita or not url.startswith("http"):
            continue
        vs = ver.get((url, cita))
        if not vs:
            res["sense_resultat"] += 1
            continue
        if r[c["cita_verificada_a_captura"]] == "si":
            res["ja_era_si"] += 1
            continue
        fx = flex.get((url, cita))
        if fx and "cita_ok" not in {v["estat"] for v in vs}:
            wbn = fx.get("url_wayback_nova") or fx.get("url_wayback") or ""
            estricta = fx["estat_flexible"] == "cita_ok_altra_captura"
            if r[c["cita_verificada_a_captura"]] == "si_flexible" and not estricta:
                res["ja_era_si_flexible"] += 1
                continue
            a = arxiu.get(url) or {}
            r[c["url_wayback"]] = wbn
            r[c["wayback_v8r1_estat"]] = "existent"
            r[c["wayback_v8r1_origen"]] = "github_actions"
            r[c["wayback_v8r1_metode"]] = ("coincidencia_exacta_normalitzada (altra captura)" if estricta
                                           else f"comparacio_flexible:{fx.get('detall') or ''}")
            r[c["wayback_v8r1_timestamp"]] = timestamp(wbn)
            r[c["cita_verificada_a_captura"]] = "si" if estricta else "si_flexible"
            nota = (f"[Wayback, GitHub Actions] cita trobada a una altra captura ({timestamp(wbn)})." if estricta else
                    f"[Wayback, GitHub Actions] cita trobada a la captura {timestamp(wbn)} amb comparació flexible ({fx.get('detall') or ''}).")
            if nota not in r[c["wayback_v8r1_nota"]]:
                r[c["wayback_v8r1_nota"]] = (r[c["wayback_v8r1_nota"]] + " " + nota).strip()
            res["si_altra_captura" if estricta else "si_flexible"] += 1
            continue
        estats = {v["estat"] for v in vs}
        v = next((x for x in vs if x["estat"] == "cita_ok"), vs[0])
        url_wb = v.get("url_wayback") or (arxiu.get(url) or {}).get("url_wayback", "")
        if "cita_ok" in estats:
            a = arxiu.get(url) or {}
            r[c["url_wayback"]] = url_wb
            r[c["wayback_v8r1_estat"]] = "nova" if a.get("estat") == "capturada" else "existent"
            r[c["wayback_v8r1_origen"]] = "github_actions"
            r[c["wayback_v8r1_metode"]] = v.get("detall") or "coincidencia_exacta_normalitzada"
            r[c["wayback_v8r1_timestamp"]] = a.get("timestamp_captura") or timestamp(url_wb)
            r[c["cita_verificada_a_captura"]] = "si"
            res["si"] += 1
        elif estats & {"cita_parcial", "cita_no_trobada"}:
            if not r[c["url_wayback"]]:
                r[c["url_wayback"]] = url_wb
            r[c["cita_verificada_a_captura"]] = "no"
            nota = f"[Wayback, GitHub Actions] captura {timestamp(url_wb) or '?'}: {v['estat']} ({v.get('detall') or ''})."
            if nota not in r[c["wayback_v8r1_nota"]]:
                r[c["wayback_v8r1_nota"]] = (r[c["wayback_v8r1_nota"]] + " " + nota).strip()
            res["no"] += 1
        else:
            res["captura_no_llegible"] += 1
    print(dict(res))
    if not args.escriu:
        print("Prova en sec: no s'ha escrit res.")
        return 0
    buf = io.StringIO()
    csv.writer(buf, lineterminator="\r\n").writerows(files)
    REG.write_bytes(buf.getvalue().encode("utf-8"))
    print("Escrit docs/REGISTRE_CANVIS.csv.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Marca per tornar a buscar les captures de Wayback que no són el document (Claude, 24/11/2026).

La verificació (`verifica_cites.py`) dona `captura_no_llegible` quan la captura `id_` no és
el document: Wayback la va desar amb una resposta d'error (`http_404`, `http_410`) o el
fitxer arxivat no s'obre (`pdftotext_error`, `binari_no_llegible`, `html_sense_text`).
Per a cada URL en aquesta situació:
  1. s'anota a l'historial (`--historial`) la captura dolenta i el motiu;
  2. es treu la URL dels resultats d'arxiu, perquè `wayback_arxiva.py --refes` la torni a
     buscar (una altra captura desada amb resposta 200 o, si no n'hi ha, una de nova);
  3. es treuen de la verificació els parells d'aquesta URL, perquè es tornin a verificar.
Cada URL es refà com a molt `--max-intents` vegades. Si després continua sense una captura
bona, queda pendent (la cita no es dona per verificada a la captura) i surt al resum.

Escriu `--sortida` (url, timestamps_exclosos) amb totes les URL de l'historial: els
timestamps dolents no es tornen a triar mai.
No fa cap consulta a la xarxa.

  python scripts/wayback/refes_captures.py --resultats treball/resultats_arxiu.csv \
      --verificacio treball/verificacio_cites.csv --historial treball/captures_refetes.csv \
      --sortida treball/refes.csv
"""
from __future__ import annotations

import argparse
import collections
import csv
import re
from datetime import datetime, timezone
from pathlib import Path

MOTIUS = ("http_404", "http_410", "pdftotext_error", "binari_no_llegible", "html_sense_text")
CAMPS_HIST = ["url", "url_wayback_dolenta", "timestamp_dolent", "motiu", "data", "intent"]


def timestamp(url_wb: str) -> str:
    m = re.search(r"/web/(\d{8,14})", url_wb or "")
    return m.group(1) if m else ""


def llegeix(path: Path) -> tuple[list[str], list[dict]]:
    if not path.is_file() or path.stat().st_size == 0:
        return [], []
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def escriu(path: Path, camps: list[str], files: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=camps, extrasaction="ignore")
        w.writeheader()
        w.writerows(files)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--resultats", required=True)
    ap.add_argument("--verificacio", required=True)
    ap.add_argument("--historial", required=True)
    ap.add_argument("--sortida", required=True)
    ap.add_argument("--max-intents", type=int, default=2)
    a = ap.parse_args()

    camps_r, resultats = llegeix(Path(a.resultats))
    camps_v, verificacio = llegeix(Path(a.verificacio))
    _, historial = llegeix(Path(a.historial))

    # Captura vigent de cada URL (l'última fila dels resultats).
    vigent = {}
    for r in resultats:
        vigent[(r.get("url") or "").strip()] = (r.get("url_wayback") or "").strip()

    intents = collections.Counter((h.get("url") or "").strip() for h in historial)
    dolentes = {}
    for v in verificacio:
        if v.get("estat") != "captura_no_llegible":
            continue
        motiu = next((m for m in MOTIUS if (v.get("detall") or "").startswith(m)), "")
        url = (v.get("url") or "").strip()
        wb = (v.get("url_wayback") or "").strip()
        # Només si la verificació és de la captura vigent (no d'una d'anterior).
        if motiu and url and wb and timestamp(vigent.get(url, "")) == timestamp(wb):
            dolentes.setdefault(url, (wb, motiu))

    ara = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    refer, exhaurides = set(), []
    for url, (wb, motiu) in sorted(dolentes.items()):
        if intents[url] >= a.max_intents:
            exhaurides.append(url)
            continue
        historial.append({"url": url, "url_wayback_dolenta": wb, "timestamp_dolent": timestamp(wb),
                          "motiu": motiu, "data": ara, "intent": intents[url] + 1})
        refer.add(url)

    if refer:
        resultats = [r for r in resultats if (r.get("url") or "").strip() not in refer]
        verificacio = [v for v in verificacio if (v.get("url") or "").strip() not in refer]
        escriu(Path(a.resultats), camps_r, resultats)
        if camps_v:
            escriu(Path(a.verificacio), camps_v, verificacio)
    escriu(Path(a.historial), CAMPS_HIST, historial)

    excl = collections.defaultdict(set)
    for h in historial:
        if h.get("timestamp_dolent"):
            excl[(h.get("url") or "").strip()].add(h["timestamp_dolent"])
    escriu(Path(a.sortida), ["url", "timestamps_exclosos"],
           [{"url": u, "timestamps_exclosos": " ".join(sorted(t))} for u, t in sorted(excl.items())])

    per_motiu = collections.Counter(dolentes[u][1] for u in refer)
    print(f"Captures que no són el document (captura vigent): {len(dolentes)} URL")
    print(f"  es tornen a buscar ara: {len(refer)} {dict(per_motiu)}")
    print(f"  intents exhaurits ({a.max_intents}), queden pendents: {len(exhaurides)}")
    print(f"  URL a l'historial: {len(excl)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

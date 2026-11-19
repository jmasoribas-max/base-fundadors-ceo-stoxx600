#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprova cites i enllaços del registre i de les fitxes d'empresa.

Per defecte només fa comprovacions locals (text present, forma d'URL,
Wayback que apunta a web.archive.org). No publica res.

  python3 scripts/comprova_enllacos_cites.py
  python3 scripts/comprova_enllacos_cites.py --live   # només si s'ha demanat explícitament
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "docs" / "REGISTRE_CANVIS.csv"
FITXES = ROOT / "empreses"
URL_RE = re.compile(r"^https?://", re.I)
WB_RE = re.compile(r"^https?://web\.archive\.org/web/", re.I)
PENDENTS_WB = {"", "pendent_verificacio_externa", "—", "-", "na", "n/a"}


def check_url_shape(url: str, wayback: bool = False) -> str | None:
    if not url:
        return "buit"
    if wayback:
        if not WB_RE.search(url):
            return "no sembla un URL de Wayback"
    elif not URL_RE.search(url):
        return "no sembla un URL http(s)"
    return None


def maybe_live(url: str, live: bool) -> str | None:
    if not live or not url:
        return None
    try:
        import urllib.request

        req = urllib.request.Request(
            url, method="HEAD", headers={"User-Agent": "v8r2-link-check/0.1"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            if getattr(resp, "status", 200) >= 400:
                return f"HTTP {resp.status}"
    except Exception as exc:  # noqa: BLE001
        return f"error: {exc}"
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--live",
        action="store_true",
        help="Comprova els URL en viu (HEAD). Desactivat per defecte.",
    )
    args = ap.parse_args()
    problems = []
    n = 0
    if not REG.exists():
        print(f"No trobo {REG}", file=sys.stderr)
        return 2
    with REG.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            n += 1
            cita = (row.get("cita_literal") or "").strip()
            url = (row.get("url_font") or "").strip()
            wb = (row.get("url_wayback") or "").strip()
            marca = row.get("marca_veritat") or ""
            ident = f"{row.get('tipus')}|{row.get('isin')}|{row.get('anys')}|{row.get('id_document_o_font')}"
            if not cita and marca != "[NV]":
                problems.append((ident, "cita buida sense marca [NV]"))
            if url:
                err = check_url_shape(url)
                if err:
                    problems.append((ident, f"url_font: {err}"))
                err = maybe_live(url, args.live)
                if err:
                    problems.append((ident, f"url_font live: {err}"))
            if wb and wb.lower() not in PENDENTS_WB:
                err = check_url_shape(wb, wayback=True)
                if err:
                    problems.append((ident, f"url_wayback: {err}"))
                err = maybe_live(wb, args.live)
                if err:
                    problems.append((ident, f"url_wayback live: {err}"))
    n_fit = 0
    if FITXES.exists():
        for p in sorted(FITXES.glob("*.md")):
            n_fit += 1
            text = p.read_text(encoding="utf-8")
            for m in re.finditer(r"https?://[^\s)>\"]+", text):
                url = m.group(0).rstrip(".,;")
                if "web.archive.org" in url:
                    err = check_url_shape(url, wayback=True)
                    if err:
                        problems.append((p.name, f"wayback a la fitxa: {err} :: {url[:120]}"))
                else:
                    err = check_url_shape(url)
                    if err:
                        problems.append((p.name, f"url a la fitxa: {err} :: {url[:120]}"))
    print(f"Files del registre comprovades: {n}")
    print(f"Fitxes comprovades: {n_fit}")
    print(f"Problemes: {len(problems)}")
    for ident, msg in problems:
        print(f"  - {ident}: {msg}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mostra de control de la verificació a Wayback (Claude, 24/11/2026).

Agafa una mostra aleatòria (llavor fixa) dels parells que `verifica_cites.py` dona com a
`cita_ok` i la torna a comprovar amb un codi independent: torna a baixar la captura `id_`,
n'extreu el text d'una altra manera (`pdftotext` en dos modes, o el text de l'HTML) i hi
busca la cita amb una normalització pròpia. Serveix per estimar si els `cita_ok` del flux
són fiables. No fa servir claus. verify=True (sense -k).

  python scripts/wayback/mostra_control.py --verificacio treball/verificacio_cites.csv \
      --n 60 --llavor 20261124 --sortida treball/mostra_control.csv
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import random
import re
import subprocess
import tempfile
import time
import unicodedata
from pathlib import Path

import requests

USER_AGENT = ("base-fundadors-ceo-stoxx600 mostra_control "
              "(recerca academica; github.com/jmasoribas-max/base-fundadors-ceo-stoxx600)")
MAX_BYTES = 150 * 1024 * 1024


def a_id(url_wb: str) -> str:
    m = re.match(r"(https?://web\.archive\.org/web/)(\d+)[a-z_]*/(.*)", url_wb or "")
    return f"https://web.archive.org/web/{m.group(2)}id_/{m.group(3)}" if m else ""


def norm(s: str) -> str:
    s = html.unescape(s or "")
    s = unicodedata.normalize("NFKC", s).replace("­", "")
    s = re.sub(r"[‘’‚‛′`´]", "'", s)
    s = re.sub(r"[“”„«»]", '"', s)
    s = re.sub(r"[‐-―−]", "-", s)
    s = re.sub(r"-\s*\n\s*", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def text_de(raw: bytes) -> str:
    if raw[:5].startswith(b"%PDF"):
        with tempfile.NamedTemporaryFile(suffix=".pdf") as t:
            t.write(raw)
            t.flush()
            parts = []
            for mode in ([], ["-raw"]):
                p = subprocess.run(["pdftotext", "-q", *mode, t.name, "-"], capture_output=True, timeout=600)
                parts.append(p.stdout.decode("utf-8", "ignore"))
            return "\n".join(parts)
    t = raw.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    return re.sub(r"<[^>]+>", " ", t)


def hi_es(cita: str, text: str) -> bool:
    nc, nt = norm(cita), norm(text)
    if not nc:
        return False
    if nc in nt or re.sub(r"\s+", "", nc) in re.sub(r"\s+", "", nt):
        return True
    # Cita amb el·lipsi: cada tros ha de ser-hi, en ordre.
    trossos = [t.strip() for t in re.split(r"\[?(?:\.\.\.|…)\]?", nc) if len(t.strip()) >= 12]
    if len(trossos) > 1:
        pos = 0
        for t in trossos:
            i = nt.find(t, pos)
            if i < 0:
                return False
            pos = i + len(t)
        return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verificacio", required=True)
    ap.add_argument("--n", type=int, default=60)
    ap.add_argument("--llavor", type=int, default=20261124)
    ap.add_argument("--sortida", required=True)
    a = ap.parse_args()

    with open(a.verificacio, newline="", encoding="utf-8") as f:
        ok = [r for r in csv.DictReader(f) if r.get("estat") == "cita_ok" and r.get("cita")]
    random.seed(a.llavor)
    mostra = random.sample(ok, min(a.n, len(ok)))
    s = requests.Session()
    s.headers["User-Agent"] = USER_AGENT
    cache = {}
    camps = ["isin", "any", "camp", "url", "url_wayback", "cita", "http", "content_type", "bytes", "sha256", "resultat"]
    with open(a.sortida, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=camps)
        w.writeheader()
        for r in mostra:
            wid = a_id(r.get("url_wayback", ""))
            if wid not in cache:
                info = {"http": "", "content_type": "", "bytes": 0, "sha256": "", "text": ""}
                for intent in range(4):
                    try:
                        resp = s.get(wid, timeout=(20, 300), stream=True)
                        info["http"] = str(resp.status_code)
                        if resp.status_code in (429, 500, 502, 503, 504):
                            time.sleep(10 * (intent + 1))
                            continue
                        raw = b""
                        for chunk in resp.iter_content(1 << 20):
                            raw += chunk
                            if len(raw) > MAX_BYTES:
                                break
                        info.update(content_type=resp.headers.get("content-type", ""), bytes=len(raw),
                                    sha256=hashlib.sha256(raw).hexdigest())
                        if resp.status_code == 200:
                            info["text"] = text_de(raw)
                        break
                    except (requests.RequestException, subprocess.SubprocessError) as e:
                        info["http"] = f"error:{e.__class__.__name__}"
                        time.sleep(10)
                cache[wid] = info
                time.sleep(2)
            info = cache[wid]
            if info["http"] != "200":
                res = "no_descarregada"
            elif len(norm(info["text"])) < 200:
                res = "sense_text"
            else:
                res = "ok" if hi_es(r["cita"], info["text"]) else "no_trobada"
            w.writerow({**{k: r.get(k, "") for k in ("isin", "any", "camp", "url", "url_wayback", "cita")},
                        **{k: info[k] for k in ("http", "content_type", "bytes", "sha256")}, "resultat": res})
            f.flush()
    with open(a.sortida, newline="", encoding="utf-8") as f:
        res = [r["resultat"] for r in csv.DictReader(f)]
    print(f"Mostra de control: {len(res)} parells cita_ok;",
          {k: res.count(k) for k in sorted(set(res))})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

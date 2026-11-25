#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Segona comprovació de les cites que `verifica_cites.py` no troba a la captura (Claude, 25/11/2026; la
comparació flexible, aprovada per Jordi el 25/11/2026).

Per als parells `cita_no_trobada` i `cita_parcial`:
  1. Torna a baixar la captura `id_` i hi busca la cita amb la comparació flexible (vegeu més avall).
  2. Si no hi és, busca a l'índex CDX d'Internet Archive altres captures de la mateixa URL desades amb
     resposta 200 (fins a `--max-captures`) i hi busca la cita, primer amb la comparació estricta de
     `verifica_cites.py` i després amb la flexible. Sovint la captura vigent és una altra versió de la pàgina
     o del document (la mostra del 25/11/2026: el 85 % de les cites «no trobades» són a l'original).
Resultats: `cita_ok_altra_captura` (estricta, en una altra captura: es porta al registre com a `si`, amb la
URL de la captura nova), `cita_ok_flexible` o `cita_ok_flexible_altra_captura` (es porten com a
`si_flexible`), `no_trobada` o `captura_no_llegible`.

Comparació flexible: les mateixes paraules i en el mateix ordre, però sense tenir en compte:
  - els espais i salts de línia (columnes i taules de l'extracció del PDF);
  - els guions de final de línia i els guionets (p. ex. «Coca- Cola», «manage-\\nment»);
  - els talls marcats a la cita amb «[…]», «[...]», «…» o «...»: cada tros (de 12 caràcters o més, sense
    espais) ha de ser al text, en ordre.
Cap altra diferència no s'accepta (cap lletra, número ni paraula de més o de menys). El resultat és
`si_flexible` al registre, separat del `si` de la comparació estricta.

Reprenible: llegeix els resultats anteriors (`--sortida`) i no torna a fer els parells ja fets amb la
mateixa captura. No fa servir claus. verify=True (sense -k).

  python scripts/wayback/verifica_flexible.py --verificacio treball/verificacio_cites.csv \
      --sortida treball/verificacio_flexible.csv --limit-urls 300
"""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
import tempfile
import time
import unicodedata
from pathlib import Path

import requests

USER_AGENT = ("base-fundadors-ceo-stoxx600 verifica_flexible "
              "(recerca academica; github.com/jmasoribas-max/base-fundadors-ceo-stoxx600)")
MAX_BYTES = 150 * 1024 * 1024
CAMPS = ["isin", "any", "camp", "url", "url_wayback", "cita", "estat_estricte", "estat_flexible", "detall",
         "url_wayback_nova"]
CDX = "https://web.archive.org/cdx/search/cdx"
RE_TALL = re.compile(r"\[\s*(?:…|\.\.\.)\s*\]|…|\.\.\.")


def a_id(url_wb: str) -> str:
    m = re.match(r"(https?://web\.archive\.org/web/)(\d+)[a-z_]*/(.*)", url_wb or "")
    return f"https://web.archive.org/web/{m.group(2)}id_/{m.group(3)}" if m else ""


def base_norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").replace("­", "")
    s = re.sub(r"[‘’‚‛′`´]", "'", s)
    s = re.sub(r"[“”„«»]", '"', s)
    s = re.sub(r"[‐-―−]", "-", s)
    return s.lower()


def compacta(s: str, sense_guions: bool) -> str:
    s = re.sub(r"\s+", "", base_norm(s))
    return s.replace("-", "") if sense_guions else s


def text_de(raw: bytes) -> str:
    if raw[:5].startswith(b"%PDF"):
        with tempfile.NamedTemporaryFile(suffix=".pdf") as t:
            t.write(raw)
            t.flush()
            parts = []
            for mode in ([], ["-raw"], ["-layout"]):
                p = subprocess.run(["pdftotext", "-q", *mode, t.name, "-"], capture_output=True, timeout=600)
                parts.append(p.stdout.decode("utf-8", "ignore"))
            return "\n\f\n".join(parts)
    t = raw.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    import html
    return html.unescape(re.sub(r"<[^>]+>", " ", t))


def flexible(cita: str, text: str) -> str:
    """Torna el detall de la regla que fa coincidir la cita, o '' si no hi és."""
    for sense_guions, etiqueta in ((False, "espais"), (True, "espais_i_guions")):
        tc = compacta(text, sense_guions)
        trossos = [compacta(x, sense_guions) for x in RE_TALL.split(cita)]
        trossos = [x for x in trossos if x]
        if len(trossos) == 1:
            if trossos[0] in tc:
                return etiqueta
        elif trossos and all(len(x) >= 12 for x in trossos):
            pos = 0
            for x in trossos:
                i = tc.find(x, pos)
                if i < 0:
                    break
                pos = i + len(x)
            else:
                return etiqueta + "_i_talls"
    return ""


def estricta(cita: str, text: str) -> bool:
    """La mateixa normalització que verifica_cites.py (coincidència exacta de la cadena normalitzada)."""
    import importlib.util
    global _VC
    if "_VC" not in globals():
        spec = importlib.util.spec_from_file_location("vc", Path(__file__).with_name("verifica_cites.py"))
        _VC = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_VC)
    c = _VC.normalitza(cita)
    return bool(c) and c in _VC.normalitza(text)


def baixa(s: requests.Session, url: str) -> tuple[str, str]:
    """(text, error) de la captura id_."""
    for intent in range(4):
        try:
            resp = s.get(url, timeout=(20, 300), stream=True)
            if resp.status_code in (429, 500, 502, 503, 504):
                time.sleep(15 * (intent + 1))
                continue
            if resp.status_code != 200:
                return "", f"http_{resp.status_code}"
            raw = b""
            for chunk in resp.iter_content(1 << 20):
                raw += chunk
                if len(raw) > MAX_BYTES:
                    break
            return text_de(raw), ""
        except (requests.RequestException, subprocess.SubprocessError) as e:
            err = f"error:{e.__class__.__name__}"
            time.sleep(10)
    return "", "error:reintents"


def altres_captures(s: requests.Session, url: str, excloure: str, maxim: int) -> list[str]:
    """Timestamps d'altres captures 200 de la URL (de la més antiga a la més nova), sense la vigent."""
    try:
        r = s.get(CDX, params={"url": url, "output": "json", "fl": "timestamp,statuscode",
                               "filter": "statuscode:200", "collapse": "digest", "limit": "50"}, timeout=(20, 60))
        files = r.json()[1:] if r.status_code == 200 else []
    except (requests.RequestException, ValueError):
        files = []
    ts = [f[0] for f in files if f and f[0] != excloure]
    return ts[:maxim]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verificacio", required=True)
    ap.add_argument("--sortida", required=True)
    ap.add_argument("--limit-urls", type=int, default=300)
    ap.add_argument("--max-captures", type=int, default=6, help="altres captures a provar per URL")
    a = ap.parse_args()

    with open(a.verificacio, newline="", encoding="utf-8") as f:
        cands = [r for r in csv.DictReader(f) if r.get("estat") in ("cita_no_trobada", "cita_parcial") and r.get("cita")]
    fets, previs = set(), []
    out_p = Path(a.sortida)
    if out_p.is_file() and out_p.stat().st_size:
        with out_p.open(newline="", encoding="utf-8") as f:
            previs = list(csv.DictReader(f))
        fets = {(r["url_wayback"], r["cita"]) for r in previs if r.get("estat_flexible") != "error_baixada"}
        previs = [r for r in previs if (r["url_wayback"], r["cita"]) in fets]
    pendents = [r for r in cands if (r.get("url_wayback", ""), r["cita"]) not in fets]
    per_url: dict[str, list[dict]] = {}
    for r in pendents:
        per_url.setdefault(r.get("url_wayback", ""), []).append(r)
    urls = list(per_url)[: max(0, a.limit_urls)]
    print(f"Parells candidats {len(cands)}; ja fets {len(fets)}; pendents {len(pendents)} a {len(per_url)} URL; "
          f"en aquesta execució {len(urls)} URL.")

    s = requests.Session()
    s.headers["User-Agent"] = USER_AGENT
    nous = []
    for wb in urls:
        txt, err = baixa(s, a_id(wb))
        time.sleep(2)
        llegible = bool(txt) and len(re.sub(r"\s+", "", txt)) >= 200
        alt_textos: list[tuple[str, str]] | None = None  # (url_wayback, text) d'altres captures, només si cal
        for r in per_url[wb]:
            est, det, nova = "", "", ""
            if llegible:
                d = flexible(r["cita"], txt)
                if d:
                    est, det = "cita_ok_flexible", d
            if not est:
                if alt_textos is None:
                    alt_textos = []
                    m = re.match(r"https?://web\.archive\.org/web/(\d+)", wb)
                    for ts in altres_captures(s, r.get("url", ""), m.group(1) if m else "", a.max_captures):
                        alt = f"https://web.archive.org/web/{ts}/{r.get('url', '')}"
                        t2, e2 = baixa(s, a_id(alt))
                        time.sleep(2)
                        if t2 and len(re.sub(r"\s+", "", t2)) >= 200:
                            alt_textos.append((alt, t2))
                for alt, t2 in alt_textos:
                    if estricta(r["cita"], t2):
                        est, det, nova = "cita_ok_altra_captura", "coincidencia_exacta_normalitzada", alt
                        break
                if not est:
                    for alt, t2 in alt_textos:
                        d = flexible(r["cita"], t2)
                        if d:
                            est, det, nova = "cita_ok_flexible_altra_captura", d, alt
                            break
            if not est:
                if not llegible and not alt_textos:
                    est, det = ("error_baixada" if err.startswith("error") else "captura_no_llegible"), err or "text_buit"
                else:
                    est, det = "no_trobada", f"captures provades: {1 + len(alt_textos or [])}"
            nous.append({"isin": r.get("isin", ""), "any": r.get("any", ""), "camp": r.get("camp", ""), "url": r.get("url", ""),
                         "url_wayback": wb, "cita": r["cita"], "estat_estricte": r.get("estat", ""),
                         "estat_flexible": est, "detall": det, "url_wayback_nova": nova})
    with out_p.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPS, extrasaction="ignore")
        w.writeheader()
        w.writerows(previs + nous)
    from collections import Counter
    print("Aquesta execució:", dict(Counter(r["estat_flexible"] for r in nous)))
    print("Total acumulat:", dict(Counter(r["estat_flexible"] for r in previs + nous)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

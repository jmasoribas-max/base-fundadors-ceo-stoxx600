#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica si la cita literal de cada parell (ISIN-any, URL, cita) de main
apareix a la captura Wayback d'aquesta nit.

Reprenable: cache de captures i CSV incremental.
No fa servir claus d'archive.org. verify=True (sense -k).
Pausa minima 2 s; backoff si 429.
"""
from __future__ import annotations

# Adaptació de Claude (23/11/2026) de l'script de DF verifica_cites.py
# (SHA-256 original 0f45779681bf30a3284efc7df3977fd012a5896298da8d0a6cdfc824d9db3d5a):
#  - els camins de la base, el registre, els resultats de Wayback i el log es passen com a opcions;
#  - els parells sense cita literal no es processen (no hi ha res a verificar);
#  - els parells amb una URL encara sense captura no s'escriuen: queden pendents per a una execució
#    posterior, quan la URL ja tingui captura.
# La lògica de descàrrega (captura id_), d'extracció de text i d'avaluació de la cita no canvia.
import argparse
import csv
import hashlib
import json
import random
import re
import subprocess
import sys
import time
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Iterable
from zoneinfo import ZoneInfo

import signal
import requests
from bs4 import BeautifulSoup

TZ = ZoneInfo("Europe/Madrid")
DIR = Path(__file__).resolve().parent
REPO = DIR.parent / "repo_main_lectura"
BASE_CSV = REPO / "dades" / "base_isin_any_v8r3.csv"
REG_CSV = REPO / "docs" / "REGISTRE_CANVIS.csv"
RESULTATS_WB = DIR / "wayback_resultats_20261122.csv"
CACHE = DIR / "cache"
OUT_CSV = DIR / "verificacio_cites_20261122.csv"
OUT_INFORME = DIR / "INFORME_VERIFICACIO_CITES.md"
LOG = DIR / "verifica_cites.log"

USER_AGENT = (
    "base-fundadors-ceo-stoxx600 verifica_cites "
    "(recerca academica; github.com/jmasoribas-max/base-fundadors-ceo-stoxx600)"
)
PAUSA_MIN = 2.0
MAX_REINTENTS = 5
MAX_BYTES = 80 * 1024 * 1024
TIMEOUT = (20, 120)
TEMPS_MAX_TOTAL = 300  # segons per descarrega, encara que el servidor no respongui


class TempsMaxExcedit(Exception):
    pass


def _alarma(signum, frame):
    raise TempsMaxExcedit()
PDFTOTEXT = "pdftotext"
SEED_EXEMPLES = 20261122
CAMPS_OUT = [
    "isin",
    "any",
    "camp",
    "url",
    "url_wayback",
    "estat",
    "detall",
    "cita",
    "origen",
    "founderceo",
    "nom_panell",
]
ESTATS = {
    "cita_ok",
    "cita_parcial",
    "cita_no_trobada",
    "captura_no_llegible",
    "sense_cita",
}

LIGATURES = {
    "ﬁ": "fi",
    "ﬂ": "fl",
    "ﬀ": "ff",
    "ﬃ": "ffi",
    "ﬄ": "ffl",
    "ﬅ": "st",
    "ﬆ": "st",
    "æ": "ae",
    "œ": "oe",
    "Æ": "ae",
    "Œ": "oe",
}
DASHES = {
    "\u2010": "-",
    "\u2011": "-",
    "\u2012": "-",
    "\u2013": "-",
    "\u2014": "-",
    "\u2015": "-",
    "\u2212": "-",
    "\ufe58": "-",
    "\ufe63": "-",
    "\uff0d": "-",
    "\u2043": "-",
    "\u2e3a": "-",
    "\u2e3b": "-",
}
QUOTES = {
    "‘": "'",
    "’": "'",
    "‚": "'",
    "‛": "'",
    "ʼ": "'",
    "ˈ": "'",
    "´": "'",
    "′": "'",
    "“": '"',
    "”": '"',
    "„": '"',
    "‟": '"',
    "«": '"',
    "»": '"',
    "‹": "'",
    "›": "'",
    "「": '"',
    "」": '"',
    "『": '"',
    "』": '"',
}


def _ara() -> str:
    return datetime.now(TZ).strftime("%Y-%m-%d %H:%M:%S %Z")


def log(msg: str) -> None:
    line = f"[{_ara()}] {msg}"
    print(line, flush=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def normalitza(s: str) -> str:
    if not s:
        return ""
    for a, b in LIGATURES.items():
        s = s.replace(a, b)
    # guionet de final de linia (paraula partida): elimina el guionet i el salt
    s = re.sub(r"[\u00ad\u2010\u2011\-]\s*[\r\n]+\s*", "", s)
    # soft hyphen residual
    s = s.replace("\u00ad", "")
    s = re.sub(r"[\r\n]+", " ", s)
    for a, b in DASHES.items():
        s = s.replace(a, b)
    for a, b in QUOTES.items():
        s = s.replace(a, b)
    s = unicodedata.normalize("NFKC", s)
    s = s.lower()
    s = re.sub(r"[\u00a0\u1680\u2000-\u200a\u202f\u205f\u3000\t\f\v]+", " ", s)
    s = re.sub(r" {2,}", " ", s).strip()
    return s


def tokens(s: str) -> list[str]:
    return re.findall(r"[0-9a-zàáâäãåèéêëìíîïòóôöõùúûüçñýÿøæœß]+", s)


def score_parcial(tok_cita: list[str], tok_text: list[str]) -> float:
    n = len(tok_cita)
    if n == 0 or not tok_text:
        return 0.0
    need = Counter(tok_cita)
    have = Counter(tok_text)
    possible = sum(min(need[t], have[t]) for t in need) / n
    if possible < 0.85 or n == 1:
        return possible
    if len(tok_text) <= n:
        return sum(min(need[t], Counter(tok_text)[t]) for t in need) / n
    w = Counter(tok_text[:n])
    best = sum(min(need[t], w[t]) for t in need) / n
    if best >= 1.0:
        return 1.0
    for i in range(n, len(tok_text)):
        out = tok_text[i - n]
        inn = tok_text[i]
        w[out] -= 1
        if w[out] <= 0:
            del w[out]
        w[inn] += 1
        sc = sum(min(need[t], w[t]) for t in need) / n
        if sc > best:
            best = sc
            if best >= 1.0:
                return 1.0
    return best


def extract_original(u: str) -> str:
    u = (u or "").strip()
    m = re.match(
        r"https?://web\.archive\.org/web/\d{4,14}[a-zA-Z0-9_]*/(https?://\S+)$",
        u,
        re.I,
    )
    if m:
        return m.group(1).rstrip(").,];")
    return u


def split_v75(s: str) -> list[str]:
    s = (s or "").strip()
    if not s:
        return []
    parts = re.split(r"\s*;\s*|\n+", s)
    out: list[str] = []
    for p in parts:
        p = p.strip().strip('"').strip()
        if not p:
            continue
        if p.count("http") > 1:
            out.extend(
                c.strip()
                for c in re.split(r",\s*(?=https?://)", p)
                if c.strip()
            )
        else:
            out.append(p)
    seen = set()
    uniq = []
    for x in out:
        u = extract_original(x)
        if u and u not in seen:
            seen.add(u)
            uniq.append(u)
    return uniq


def expand_anys(s: str) -> list[str]:
    years: list[str] = []
    for part in (s or "").split(","):
        part = part.strip()
        if re.fullmatch(r"\d{4}-\d{4}", part):
            a, b = int(part[:4]), int(part[5:9])
            if a <= b <= 2100:
                years.extend(str(y) for y in range(a, b + 1))
        elif re.fullmatch(r"\d{4}", part):
            years.append(part)
    seen = set()
    out = []
    for y in years:
        if y not in seen:
            seen.add(y)
            out.append(y)
    return out


def a_id_(wb: str) -> str:
    wb = (wb or "").strip()
    m = re.match(
        r"(https?://web\.archive\.org/web/)(\d{4,14})([a-zA-Z0-9_]*)(/(?:https?://|https?://).*)",
        wb,
        re.I,
    )
    # The last group is /https?://...
    m = re.match(
        r"(https?://web\.archive\.org/web/)(\d{4,14})([a-zA-Z0-9_]*)(/https?://.*)$",
        wb,
        re.I,
    )
    if not m:
        return wb
    return m.group(1) + m.group(2) + "id_" + m.group(4)


def sha1_key(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()


def carrega_resultats_wb(path: Path) -> dict[str, dict]:
    last: dict[str, dict] = {}
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            url = (row.get("url") or "").strip()
            if url:
                last[url] = row
    return last


def carrega_parells() -> tuple[list[dict], dict]:
    """Construeix els parells des de main (base + registre)."""
    with BASE_CSV.open(newline="", encoding="utf-8") as f:
        base = list(csv.DictReader(f))
    panel: dict[str, set[str]] = defaultdict(set)
    meta_fila = {}
    for r in base:
        isin, any_ = r["isin"], r["any"]
        panel[isin].add(any_)
        meta_fila[(isin, any_)] = {
            "founderceo": r.get("FounderCEO") or "",
            "nom_panell": r.get("nom_panell") or "",
        }

    bruts: list[dict] = []

    def afegeix(isin, any_, camp, url, cita, origen):
        url = (url or "").strip()
        if not url or not (cita or "").strip():
            return
        bruts.append(
            {
                "isin": isin,
                "any": any_,
                "camp": camp,
                "url": url,
                "cita": (cita or "").strip(),
                "origen": origen,
            }
        )

    for r in base:
        isin, any_ = r["isin"], r["any"]
        url = (r.get("font_classificacio_url") or "").strip()
        if url:
            afegeix(
                isin,
                any_,
                "font_classificacio_url",
                url,
                r.get("font_classificacio_cita") or "",
                "base",
            )
        url = (r.get("d37_cita_contemp_url") or "").strip()
        if url:
            # d37_cita_contemporania es un flag (si/no); la data de cita es d37_data_cita
            afegeix(
                isin,
                any_,
                "d37_cita_contemp_url",
                url,
                r.get("d37_data_cita") or r.get("d37_cita_contemp_data") or "",
                "base",
            )
        url = (r.get("url_font") or "").strip()
        if url:
            afegeix(isin, any_, "url_font", url, "", "base")
        for u in split_v75(r.get("v75_urls_arxivades") or ""):
            afegeix(isin, any_, "v75_urls_arxivades", u, "", "base")

    n_reg_sense_url = 0
    with REG_CSV.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            url = extract_original((r.get("url_font") or "").strip())
            if not url:
                n_reg_sense_url += 1
                continue
            cita = (r.get("cita_literal") or "").strip()
            isin = (r.get("isin") or "").strip()
            funcio = (r.get("funcio_cita") or "").strip() or "registre"
            camp = f"registre.url_font/{funcio}"
            for y in expand_anys(r.get("anys") or ""):
                if y in panel.get(isin, set()):
                    afegeix(isin, y, camp, url, cita, "registre")

    # unics per (isin, any, camp, url, cita)
    seen = set()
    parells = []
    for p in bruts:
        k = (p["isin"], p["any"], p["camp"], p["url"], p["cita"])
        if k in seen:
            continue
        seen.add(k)
        info = meta_fila.get((p["isin"], p["any"]), {})
        p["founderceo"] = info.get("founderceo", "")
        p["nom_panell"] = info.get("nom_panell", "")
        parells.append(p)

    extra = {"n_reg_sense_url": n_reg_sense_url, "n_bruts": len(bruts)}
    return parells, extra


def treu_errors_interns(path: Path) -> int:
    """Adaptació de Claude (23/11/2026): treu del fitxer de resultats els parells que van fallar per
    un error intern de l'script (p. ex. `excepció_interna:FeatureNotFound`, perquè faltava lxml al
    flux de GitHub), perquè es tornin a verificar. Els altres resultats es conserven tal com són."""
    if not path.is_file() or path.stat().st_size == 0:
        return 0
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        camps = reader.fieldnames or []
        files = list(reader)
    bons = [r for r in files if not (r.get("estat") == "captura_no_llegible"
                                     and (r.get("detall") or "").startswith("excepció_interna"))]
    if len(bons) == len(files):
        return 0
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=camps)
        w.writeheader()
        w.writerows(bons)
    return len(files) - len(bons)


def carrega_fets(path: Path) -> set[tuple[str, str, str, str, str]]:
    fets: set[tuple[str, str, str, str, str]] = set()
    if not path.is_file() or path.stat().st_size == 0:
        return fets
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return fets
        for row in reader:
            fets.add(
                (
                    row.get("isin") or "",
                    row.get("any") or "",
                    row.get("camp") or "",
                    row.get("url") or "",
                    row.get("cita") or "",
                )
            )
    return fets


def obre_sortida(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    nou = (not path.is_file()) or path.stat().st_size == 0
    f = path.open("a", newline="", encoding="utf-8")
    w = csv.DictWriter(f, fieldnames=CAMPS_OUT, extrasaction="ignore")
    if nou:
        w.writeheader()
        f.flush()
    return f, w


def escriu_files(writer, fh, files: Iterable[dict]) -> None:
    for row in files:
        writer.writerow({k: row.get(k, "") for k in CAMPS_OUT})
    fh.flush()


def html_a_text(raw: bytes, content_type: str = "") -> str:
    charset = "utf-8"
    m = re.search(r"charset=([A-Za-z0-9_.:-]+)", content_type or "", re.I)
    if m:
        charset = m.group(1).strip().strip('"')
    for enc in (charset, "utf-8", "cp1252", "latin-1"):
        try:
            s = raw.decode(enc)
            break
        except (LookupError, UnicodeDecodeError):
            s = None
    if s is None:
        s = raw.decode("utf-8", errors="replace")
    soup = BeautifulSoup(s, "lxml")
    for tag in soup(["script", "style", "noscript", "template"]):
        tag.decompose()
    return soup.get_text("\n", strip=True)


def pdf_a_text(pdf_path: Path) -> tuple[str, str]:
    """Retorna (text, error)."""
    out = pdf_path.with_suffix(".pdftotext.txt")
    try:
        proc = subprocess.run(
            [PDFTOTEXT, "-enc", "UTF-8", "-nopgbrk", str(pdf_path), str(out)],
            capture_output=True,
            timeout=180,
            check=False,
        )
    except FileNotFoundError:
        return "", "pdftotext_no_trobat"
    except subprocess.TimeoutExpired:
        return "", "pdftotext_timeout"
    if proc.returncode != 0 and not out.is_file():
        err = (proc.stderr or b"").decode("utf-8", errors="replace")[:200]
        return "", f"pdftotext_error:{err or proc.returncode}"
    if not out.is_file():
        return "", "pdftotext_sense_sortida"
    text = out.read_text(encoding="utf-8", errors="replace")
    # si gairebe buit, reintenta amb -raw
    if len(normalitza(text)) < 40:
        out2 = pdf_path.with_suffix(".pdftotext_raw.txt")
        try:
            subprocess.run(
                [PDFTOTEXT, "-raw", "-enc", "UTF-8", "-nopgbrk", str(pdf_path), str(out2)],
                capture_output=True,
                timeout=180,
                check=False,
            )
            if out2.is_file():
                alt = out2.read_text(encoding="utf-8", errors="replace")
                if len(normalitza(alt)) > len(normalitza(text)):
                    text = alt
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
    return text, ""


def zip_a_text(raw: bytes) -> str:
    import io
    import zipfile

    parts: list[str] = []
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as zf:
            for name in zf.namelist():
                low = name.lower()
                if low.endswith((".xml", ".txt", ".html", ".htm", ".rels")):
                    data = zf.read(name)
                    try:
                        s = data.decode("utf-8")
                    except UnicodeDecodeError:
                        s = data.decode("latin-1", errors="replace")
                    # treu tags xml de manera simple
                    s = re.sub(r"<[^>]+>", " ", s)
                    parts.append(s)
    except Exception as exc:  # noqa: BLE001
        return ""
    return "\n".join(parts)


def detecta_tipus(raw: bytes, content_type: str, url: str) -> str:
    if raw.startswith(b"%PDF") or b"%PDF-" in raw[:1024]:
        return "pdf"
    if raw.startswith(b"PK"):
        return "zip"
    ct = (content_type or "").lower()
    if "pdf" in ct:
        return "pdf"
    if "html" in ct or "xml" in ct or "xhtml" in ct:
        return "html"
    ul = (url or "").lower().split("?")[0]
    if ul.endswith(".pdf"):
        return "pdf"
    if any(ul.endswith(ext) for ext in (".docx", ".xlsx", ".pptx", ".odt", ".ods")):
        return "zip"
    # heuristica html
    head = raw[:4096].lstrip().lower()
    if head.startswith(b"<!doctype") or head.startswith(b"<html") or b"<html" in head:
        return "html"
    if raw.startswith(b"<?xml"):
        return "html"
    return "binari"


def pagina_error_wayback(text: str, http_codi: int) -> str | None:
    low = (text or "")[:4000].lower()
    if http_codi >= 400:
        return f"http_{http_codi}"
    senyals = [
        "the wayback machine has not archived that url",
        "this page is not available on the web",
        "page cannot be displayed due to robots",
        "excluded by the site owner",
        "calendarcaptures",
    ]
    for s in senyals:
        if s in low and len(normalitza(text)) < 2000:
            return f"pagina_error_wayback:{s}"
    return None


def descarrega(url_id: str, dest: Path) -> dict:
    dest.parent.mkdir(parents=True, exist_ok=True)
    headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    intent = 0
    espera = 30
    darrer_err = ""
    while intent < MAX_REINTENTS:
        intent += 1
        signal.signal(signal.SIGALRM, _alarma)
        signal.alarm(TEMPS_MAX_TOTAL)
        try:
            with requests.get(
                url_id,
                headers=headers,
                timeout=TIMEOUT,
                stream=True,
                allow_redirects=True,
                verify=True,
            ) as resp:
                codi = resp.status_code
                if codi == 429 or codi == 503:
                    retry = resp.headers.get("Retry-After")
                    try:
                        sleep_s = max(espera, int(retry)) if retry and str(retry).isdigit() else espera
                    except Exception:
                        sleep_s = espera
                    darrer_err = f"http_{codi}"
                    log(f"  backoff {sleep_s}s per HTTP {codi} (intent {intent})")
                    signal.alarm(0)
                    time.sleep(sleep_s)
                    espera = min(espera * 2, 300)
                    continue
                if codi >= 500:
                    darrer_err = f"http_{codi}"
                    log(f"  reintent {intent} HTTP {codi}")
                    signal.alarm(0)
                    time.sleep(espera)
                    espera = min(espera * 2, 300)
                    continue
                ctype = resp.headers.get("Content-Type") or ""
                clen = resp.headers.get("Content-Length")
                if clen and clen.isdigit() and int(clen) > MAX_BYTES:
                    return {
                        "ok": False,
                        "http_codi": codi,
                        "content_type": ctype,
                        "bytes": int(clen),
                        "error": f"mida_excedida_content_length:{clen}",
                    }
                sha = hashlib.sha256()
                n = 0
                tmp = dest.with_suffix(dest.suffix + ".part")
                with tmp.open("wb") as f:
                    for chunk in resp.iter_content(chunk_size=64 * 1024):
                        if not chunk:
                            continue
                        n += len(chunk)
                        if n > MAX_BYTES:
                            tmp.unlink(missing_ok=True)
                            return {
                                "ok": False,
                                "http_codi": codi,
                                "content_type": ctype,
                                "bytes": n,
                                "error": f"mida_excedida:{n}",
                            }
                        sha.update(chunk)
                        f.write(chunk)
                tmp.replace(dest)
                return {
                    "ok": True,
                    "http_codi": codi,
                    "content_type": ctype,
                    "bytes": n,
                    "sha256": sha.hexdigest(),
                    "error": "" if codi < 400 else f"http_{codi}",
                }
        except TempsMaxExcedit:
            dest.with_suffix(dest.suffix + ".part").unlink(missing_ok=True)
            log(f"  temps maxim {TEMPS_MAX_TOTAL}s excedit, se salta")
            return {"ok": False, "http_codi": "", "content_type": "", "bytes": 0, "error": f"temps_max_{TEMPS_MAX_TOTAL}s"}
        except requests.exceptions.SSLError as exc:
            signal.alarm(0)
            return {"ok": False, "http_codi": "", "content_type": "", "bytes": 0, "error": f"ssl:{exc.__class__.__name__}"}
        except requests.RequestException as exc:
            signal.alarm(0)
            darrer_err = f"xarxa:{exc.__class__.__name__}"
            log(f"  error xarxa {darrer_err} intent {intent}")
            time.sleep(espera)
            espera = min(espera * 2, 300)
        finally:
            signal.alarm(0)
    return {
        "ok": False,
        "http_codi": "",
        "content_type": "",
        "bytes": 0,
        "error": darrer_err or "error_descarrega",
    }


def extreu_de_cache_o_baixa(url: str, url_wb: str, cache_dir: Path, sessio_pausa: list) -> dict:
    """Retorna meta amb 'text' (o error). sessio_pausa[0] es l'instant de l'ultima descarrega."""
    url_id = a_id_(url_wb) if url_wb else ""
    key = sha1_key(url_id or url)
    raw_path = cache_dir / "raw" / key
    text_path = cache_dir / "text" / f"{key}.txt"
    meta_path = cache_dir / "meta" / f"{key}.json"

    if meta_path.is_file() and text_path.is_file():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if meta.get("complet"):
            meta["text"] = text_path.read_text(encoding="utf-8", errors="replace")
            return meta

    if not url_id:
        meta = {
            "complet": True,
            "url": url,
            "url_wayback_id": "",
            "error": "sense_url_wayback",
            "http_codi": "",
            "tipus": "",
            "bytes": 0,
            "text_chars": 0,
        }
        _desa_meta(meta_path, text_path, meta, "")
        meta["text"] = ""
        return meta

    # pausa entre descarregues
    ara = time.time()
    delta = ara - sessio_pausa[0]
    if sessio_pausa[0] > 0 and delta < PAUSA_MIN:
        time.sleep(PAUSA_MIN - delta)

    log(f"  descarregant {url_id[:140]}")
    info = descarrega(url_id, raw_path)
    sessio_pausa[0] = time.time()

    if not info.get("ok"):
        meta = {
            "complet": True,
            "url": url,
            "url_wayback_id": url_id,
            "http_codi": info.get("http_codi") or "",
            "content_type": info.get("content_type") or "",
            "bytes": info.get("bytes") or 0,
            "error": info.get("error") or "descarrega_fallida",
            "tipus": "",
            "text_chars": 0,
            "fetched_at": _ara(),
        }
        _desa_meta(meta_path, text_path, meta, "")
        meta["text"] = ""
        return meta

    raw = raw_path.read_bytes() if raw_path.is_file() else b""
    tipus = detecta_tipus(raw, info.get("content_type") or "", url)
    error = ""
    text = ""
    if info.get("http_codi", 200) >= 400 and tipus != "pdf":
        # encara intentem extreure, pot ser una pagina d'error
        pass
    if tipus == "pdf":
        text, error = pdf_a_text(raw_path)
        if not error and len(normalitza(text)) < 40:
            error = f"pdf_escanejat_o_sense_text:chars={len(text)}:bytes={len(raw)}"
    elif tipus == "html":
        text = html_a_text(raw, info.get("content_type") or "")
        err_wb = pagina_error_wayback(text, int(info.get("http_codi") or 0) or 0)
        if err_wb:
            error = err_wb
        elif len(normalitza(text)) < 20:
            error = f"html_sense_text:chars={len(text)}:bytes={len(raw)}"
    elif tipus == "zip":
        text = zip_a_text(raw)
        if len(normalitza(text)) < 40:
            error = f"zip_sense_text_extractible:bytes={len(raw)}"
    else:
        # prova html per si de cas, si no binari
        if b"<" in raw[:2048]:
            text = html_a_text(raw, info.get("content_type") or "")
            if len(normalitza(text)) >= 20:
                tipus = "html"
            else:
                error = f"binari_no_llegible:content_type={info.get('content_type')}:bytes={len(raw)}"
                text = ""
        else:
            error = f"binari_no_llegible:content_type={info.get('content_type')}:bytes={len(raw)}"

    if not error and info.get("http_codi", 200) >= 400:
        error = f"http_{info.get('http_codi')}"

    meta = {
        "complet": True,
        "url": url,
        "url_wayback_id": url_id,
        "http_codi": info.get("http_codi") or "",
        "content_type": info.get("content_type") or "",
        "bytes": len(raw),
        "sha256": info.get("sha256") or "",
        "tipus": tipus,
        "error": error,
        "text_chars": len(text),
        "fetched_at": _ara(),
    }
    _desa_meta(meta_path, text_path, meta, text)
    meta["text"] = text
    return meta


def _desa_meta(meta_path: Path, text_path: Path, meta: dict, text: str) -> None:
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    text_path.parent.mkdir(parents=True, exist_ok=True)
    net = {k: v for k, v in meta.items() if k != "text"}
    meta_path.write_text(json.dumps(net, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    text_path.write_text(text or "", encoding="utf-8")


def avalua_cita(cita: str, text: str, meta: dict, url_wb: str) -> tuple[str, str]:
    if not (cita or "").strip():
        return "sense_cita", "sense cita literal al camp"
    if not url_wb:
        return "captura_no_llegible", "url_absent_als_resultats_wayback_20261122"
    err = meta.get("error") or ""
    if err:
        return "captura_no_llegible", err
    if not text:
        return "captura_no_llegible", "text_buit"
    cita_n = normalitza(cita)
    text_n = normalitza(text)
    if not cita_n:
        return "sense_cita", "cita només amb puntuació/espais després de normalitzar"
    if cita_n in text_n:
        return "cita_ok", "coincidencia_exacta_normalitzada"
    tok_c = tokens(cita_n)
    tok_t = tokens(text_n)
    sc = score_parcial(tok_c, tok_t)
    if tok_c and sc >= 0.85:
        n = len(tok_c)
        trobats = int(round(sc * n))
        return "cita_parcial", f"score={sc:.3f} tokens={trobats}/{n}"
    return (
        "cita_no_trobada",
        f"no_coincideix len_cita_norm={len(cita_n)} len_text_norm={len(text_n)} score={sc:.3f}",
    )


def genera_informe(out_csv: Path, dest: Path, extra: dict, wb_stats: dict) -> None:
    with out_csv.open(newline="", encoding="utf-8") as f:
        files = list(csv.DictReader(f))
    n = len(files)
    per_estat = Counter(r["estat"] for r in files)
    # per fila ISIN-any: estat pitjor
    ordre = {
        "captura_no_llegible": 4,
        "cita_no_trobada": 3,
        "cita_parcial": 2,
        "cita_ok": 1,
        "sense_cita": 0,
    }
    files_ia: dict[tuple[str, str], dict] = {}
    for r in files:
        k = (r["isin"], r["any"])
        info = files_ia.setdefault(
            k,
            {
                "founderceo": r.get("founderceo") or "",
                "nom_panell": r.get("nom_panell") or "",
                "estats": Counter(),
                "pitjor": "sense_cita",
                "problemes": [],
            },
        )
        st = r["estat"]
        info["estats"][st] += 1
        if ordre.get(st, -1) > ordre.get(info["pitjor"], -1):
            info["pitjor"] = st
        if st not in {"cita_ok", "sense_cita"}:
            info["problemes"].append(r)

    per_fila = Counter(v["pitjor"] for v in files_ia.values())

    def grup(fc: str) -> str:
        if fc == "1":
            return "F"
        if fc == "0":
            return "P"
        if fc == "NA_sense_ceo":
            return "NA"
        if fc == "no_determinat":
            return "ND"
        return fc or "?"

    # parells per grup x estat
    parells_grup_estat = Counter((grup(r.get("founderceo") or ""), r["estat"]) for r in files)
    files_grup_estat = Counter((grup(v["founderceo"]), v["pitjor"]) for v in files_ia.values())
    n_files_grup = Counter(grup(v["founderceo"]) for v in files_ia.values())
    n_parells_grup = Counter(grup(r.get("founderceo") or "") for r in files)

    f_problemes = []
    for (isin, any_), info in files_ia.items():
        if grup(info["founderceo"]) != "F":
            continue
        if info["pitjor"] in {"cita_ok", "sense_cita"}:
            continue
        f_problemes.append((isin, any_, info))
    f_problemes.sort(key=lambda x: (x[0], x[1]))

    no_trobades = [r for r in files if r["estat"] == "cita_no_trobada"]
    rng = random.Random(SEED_EXEMPLES)
    if len(no_trobades) <= 10:
        mostra = no_trobades
    else:
        mostra = rng.sample(no_trobades, 10)
    # estableix ordre per llegibilitat
    mostra = sorted(mostra, key=lambda r: (r["isin"], r["any"], r["camp"]))

    def fmt_n(x: int) -> str:
        return f"{x:,}".replace(",", ".")

    linies = []
    a = linies.append
    a("# Informe de verificació de cites a les captures Wayback")
    a("")
    a(f"Data de l'informe: {_ara()} (Europe/Madrid).")
    a("Tots els recomptes surten de `verificacio_cites_20261122.csv`. No s'ha inventat cap xifra.")
    a("")
    a("## Abast")
    a("")
    a(f"- Repositori `base-fundadors-ceo-stoxx600`, `main` = `6f871bb10c4575acfd7c74d8ed3c34c0a88d6e50`.")
    a("- Cites extretes del CSV de la base (`dades/base_isin_any_v8r3.csv`) i del registre (`docs/REGISTRE_CANVIS.csv`).")
    a("- Un parell = (ISIN, any, camp, URL, cita literal). Els anys del registre s'expandeixen (llistes i intervals) i només es queden els que són al panell.")
    a(f"- Parells únics escrits: {fmt_n(n)}.")
    a(f"- Files brutes abans de deduplicar: {fmt_n(extra.get('n_bruts', 0))}.")
    a(f"- Files del registre sense `url_font` (no entren als parells): {fmt_n(extra.get('n_reg_sense_url', 0))}.")
    a(
        f"- Resultats Wayback d'aquesta nit (`wayback_resultats_20261122.csv`, última línia per URL): "
        f"{fmt_n(wb_stats.get('n_url', 0))} URL "
        f"(ja_existia {fmt_n(wb_stats.get('ja_existia', 0))}, "
        f"capturada {fmt_n(wb_stats.get('capturada', 0))}, "
        f"error {fmt_n(wb_stats.get('error', 0))})."
    )
    a("")
    a("Camps de la base: `font_classificacio_url` + `font_classificacio_cita`; `d37_cita_contemp_url` + `d37_data_cita` (el camp `d37_cita_contemporania` és un flag, no una cita); `url_font` de sector (sense cita literal); `v75_urls_arxivades` (sense cita literal associada a la columna). Camps del registre: `registre.url_font/{funcio_cita}` amb `cita_literal`.")
    a("")
    a("## Mètode")
    a("")
    a("- S'ha fet servir la variant `id_` (contingut original) de cada `url_wayback` dels resultats. Sense claus d'archive.org, sense `-k`, sense archive.today ni bypass.")
    a("- Pausa mínima de 2 s entre descàrregues i backoff si Wayback respon 429.")
    a("- Text de PDF amb `pdftotext` (poppler, UTF-8; reintent `-raw` si el text és gairebé buit). HTML amb BeautifulSoup/lxml (s'eliminen script i style). Documents Office (zip) amb extracció simple de XML.")
    a("- Normalització: minúscules, ligadures, cometes tipogràfiques, guionets unificats, salts de línia amb guionet de partició de paraula, espais.")
    a("- `cita_ok` només si hi ha coincidència exacta de la cadena ja normalitzada. `cita_parcial` si el 85% o més dels tokens de la cita apareixen en una finestra de la mateixa longitud. La resta, `cita_no_trobada`.")
    a("- Si no hi ha cita literal: `sense_cita`. Si la URL no és als resultats d'aquesta nit o la captura no es pot llegir: `captura_no_llegible` (amb motiu a `detall`).")
    a("")
    a("## Recomptes per estat (parells)")
    a("")
    a("| Estat | Parells |")
    a("|---|---|")
    for est in ("cita_ok", "cita_parcial", "cita_no_trobada", "captura_no_llegible", "sense_cita"):
        a(f"| `{est}` | {fmt_n(per_estat.get(est, 0))} |")
    altres = [e for e in per_estat if e not in ESTATS]
    for e in altres:
        a(f"| `{e}` | {fmt_n(per_estat[e])} |")
    a(f"| **Total** | **{fmt_n(n)}** |")
    a("")
    a("### Parells per grup FounderCEO i estat")
    a("")
    a("| Grup | cita_ok | cita_parcial | cita_no_trobada | captura_no_llegible | sense_cita | Total |")
    a("|---|---|---|---|---|---|---|")
    for g in ("F", "P", "NA", "ND"):
        vals = [parells_grup_estat.get((g, e), 0) for e in ("cita_ok", "cita_parcial", "cita_no_trobada", "captura_no_llegible", "sense_cita")]
        a("| " + " | ".join([g] + [fmt_n(v) for v in vals] + [fmt_n(n_parells_grup.get(g, 0))]) + " |")
    a("")
    a("## Recomptes per fila ISIN-any")
    a("")
    a("Per a cada fila ISIN-any s'agafa l'estat més greu dels seus parells, en aquest ordre: `captura_no_llegible` > `cita_no_trobada` > `cita_parcial` > `cita_ok` > `sense_cita`.")
    a("")
    a("| Estat pitjor | Files ISIN-any |")
    a("|---|---|")
    for est in ("captura_no_llegible", "cita_no_trobada", "cita_parcial", "cita_ok", "sense_cita"):
        a(f"| `{est}` | {fmt_n(per_fila.get(est, 0))} |")
    a(f"| **Total** | **{fmt_n(len(files_ia))}** |")
    a("")
    a("### Files ISIN-any per grup FounderCEO i estat pitjor")
    a("")
    a("| Grup | Files | captura_no_llegible | cita_no_trobada | cita_parcial | cita_ok | sense_cita |")
    a("|---|---|---|---|---|---|---|")
    for g in ("F", "P", "NA", "ND"):
        vals = [files_grup_estat.get((g, e), 0) for e in ("captura_no_llegible", "cita_no_trobada", "cita_parcial", "cita_ok", "sense_cita")]
        a("| " + " | ".join([g, fmt_n(n_files_grup.get(g, 0))] + [fmt_n(v) for v in vals]) + " |")
    a("")
    a(f"## Files F amb problemes ({fmt_n(len(f_problemes))})")
    a("")
    a("S'hi llisten les files amb `FounderCEO=1` el pitjor estat de les quals no és `cita_ok` ni `sense_cita`.")
    a("")
    if not f_problemes:
        a("Cap fila F amb problemes en aquests parells.")
    else:
        for isin, any_, info in f_problemes:
            a(f"### {isin} {any_} — {info['nom_panell'] or '(sense nom)'}")
            a("")
            a(f"- Estat pitjor: `{info['pitjor']}`. Parells: " + ", ".join(f"{k}={v}" for k, v in info["estats"].most_common()) + ".")
            for r in info["problemes"]:
                cita = (r.get("cita") or "").replace("\n", " ")
                if len(cita) > 180:
                    cita = cita[:180] + "…"
                a(f"- `{r['camp']}` · `{r['estat']}` · {r.get('detall') or ''} · URL: {r['url']}")
                if cita:
                    a(f"  - Cita: «{cita}»")
            a("")
    a("## 10 exemples aleatoris de `cita_no_trobada` (llavor 20261122)")
    a("")
    if not no_trobades:
        a("No hi ha cap parell `cita_no_trobada`.")
    else:
        a(f"N'hi ha {fmt_n(len(no_trobades))} en total. Mostra per revisar a mà:")
        a("")
        for i, r in enumerate(mostra, 1):
            cita = (r.get("cita") or "").replace("\n", " ")
            a(f"### Exemple {i}")
            a("")
            a(f"- ISIN-any: `{r['isin']}` {r['any']} ({r.get('nom_panell') or ''}, FounderCEO={r.get('founderceo') or ''})")
            a(f"- Camp: `{r['camp']}`")
            a(f"- URL: {r['url']}")
            a(f"- URL Wayback: {r.get('url_wayback') or ''}")
            a(f"- Detall: {r.get('detall') or ''}")
            a(f"- Cita: «{cita}»")
            a("")
    a("## Limitacions (què no s'ha pogut verificar)")
    a("")
    n_abs = sum(1 for r in files if r["estat"] == "captura_no_llegible" and "url_absent" in (r.get("detall") or ""))
    n_ll = per_estat.get("captura_no_llegible", 0) - n_abs
    motius = Counter(
        (r.get("detall") or "").split(":")[0] for r in files if r["estat"] == "captura_no_llegible"
    )
    a(f"- Parells `captura_no_llegible`: {fmt_n(per_estat.get('captura_no_llegible', 0))} (dels quals {fmt_n(n_abs)} perquè la URL no era als resultats Wayback d'aquesta nit, i {fmt_n(n_ll)} perquè la captura no s'ha pogut llegir).")
    a("- Motius de `captura_no_llegible` (prefix de `detall`):")
    for motiu, c in motius.most_common():
        a(f"  - `{motiu or '(buit)'}`: {fmt_n(c)}")
    a(f"- {fmt_n(extra.get('n_reg_sense_url', 0))} files del registre no tenen `url_font` i no s'han convertit en parells.")
    a("- Les URL noves dels lots 6-8 que no eren a la llista d'aquesta nit no s'han descarregat (això queda per a una passada posterior de Wayback). No s'ha consultat cap altra còpia ni la web en viu.")
    a("- Un PDF escanejat (només imatge) queda com a `captura_no_llegible`, no com a `cita_no_trobada`.")
    a("- `cita_ok` no garanteix que la cita sigui la prova correcta per a aquella classificació; només que el text literal (ja normalitzat) apareix a la captura.")
    a("- Per a `d37_cita_contemp_url` s'ha pres `d37_data_cita` com a cita (com a `urls_main.csv`); `d37_cita_contemporania` és un flag i `d37_cita_contemp_data` pot ser una altra data.")
    a("- Les columnes `url_font` (sector, fulls STOXX) i `v75_urls_arxivades` no porten cita literal: queden `sense_cita` i no es comprova cap text.")
    a("- La coincidència parcial (≥85% de tokens) no es compta com a OK; cal revisar-la a mà.")
    a("")
    dest.write_text("\n".join(linies) + "\n", encoding="utf-8")


def main() -> int:
    global BASE_CSV, REG_CSV, LOG
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit-urls", type=int, default=0, help="Només processa N URL amb cita (prova).")
    ap.add_argument("--nomes-informe", action="store_true")
    ap.add_argument("--out", type=Path, default=OUT_CSV)
    ap.add_argument("--informe", type=Path, default=OUT_INFORME)
    ap.add_argument("--cache", type=Path, default=CACHE)
    ap.add_argument("--base", type=Path, default=BASE_CSV)
    ap.add_argument("--registre", type=Path, default=REG_CSV)
    ap.add_argument("--resultats-wb", type=Path, default=RESULTATS_WB)
    ap.add_argument("--log", type=Path, default=LOG)
    args = ap.parse_args()
    BASE_CSV, REG_CSV, LOG = args.base, args.registre, args.log

    wb = carrega_resultats_wb(args.resultats_wb)
    wb_stats = {
        "n_url": len(wb),
        "ja_existia": sum(1 for r in wb.values() if r.get("estat") == "ja_existia"),
        "capturada": sum(1 for r in wb.values() if r.get("estat") == "capturada"),
        "error": sum(1 for r in wb.values() if r.get("estat") not in {"ja_existia", "capturada"}),
    }

    parells, extra = carrega_parells()
    if args.nomes_informe:
        if not args.out.is_file():
            log(f"No trobo {args.out}")
            return 2
        genera_informe(args.out, args.informe, extra, wb_stats)
        log(f"Informe escrit a {args.informe}")
        return 0

    args.cache.mkdir(parents=True, exist_ok=True)
    tretes = treu_errors_interns(args.out)
    if tretes:
        log(f"Parells amb error intern retirats per tornar-los a verificar: {tretes}")
    fets = carrega_fets(args.out)
    pendents = [p for p in parells if (p["isin"], p["any"], p["camp"], p["url"], p["cita"]) not in fets]
    log(
        f"Parells únics {len(parells)}; ja fets {len(fets)}; pendents {len(pendents)}; "
        f"URL als resultats {wb_stats['n_url']}"
    )

    # Escriu primer els que no cal descarregar (sense cita, o URL absent)
    fh, writer = obre_sortida(args.out)
    sessio_pausa = [0.0]
    try:
        immediats = []
        per_url: dict[str, list[dict]] = defaultdict(list)
        for p in pendents:
            cita = (p["cita"] or "").strip()
            url = p["url"]
            row_wb = wb.get(url)
            if not cita:
                immediats.append(p)
            elif not row_wb or not (row_wb.get("url_wayback") or "").strip():
                continue  # encara sense captura: queda pendent per a una execució posterior
            else:
                per_url[url].append(p)

        if immediats:
            files_out = []
            for p in immediats:
                url_wb = (wb.get(p["url"], {}).get("url_wayback") or "") if p["url"] in wb else ""
                if not (p["cita"] or "").strip():
                    estat, detall = "sense_cita", "sense cita literal al camp"
                else:
                    estat, detall = "captura_no_llegible", "url_absent_als_resultats_wayback_20261122"
                files_out.append(
                    {
                        **p,
                        "url_wayback": a_id_(url_wb) if url_wb else "",
                        "estat": estat,
                        "detall": detall,
                    }
                )
            escriu_files(writer, fh, files_out)
            log(f"Escrits {len(files_out)} parells immediats (sense_cita o URL absent)")

        urls = list(per_url.keys())
        if args.limit_urls and args.limit_urls > 0:
            urls = urls[: args.limit_urls]
            log(f"PROVA: limit {args.limit_urls} URL ({sum(len(per_url[u]) for u in urls)} parells)")

        total_u = len(urls)
        for i, url in enumerate(urls, 1):
            row_wb = wb[url]
            url_wb = (row_wb.get("url_wayback") or "").strip()
            url_id = a_id_(url_wb)
            log(f"[{i}/{total_u}] {url[:120]} ({len(per_url[url])} parells)")
            try:
                meta = extreu_de_cache_o_baixa(url, url_wb, args.cache, sessio_pausa)
                text = meta.get("text") or ""
                files_out = []
                for p in per_url[url]:
                    estat, detall = avalua_cita(p["cita"], text, meta, url_wb)
                    files_out.append(
                        {
                            **p,
                            "url_wayback": url_id,
                            "estat": estat,
                            "detall": detall,
                        }
                    )
                escriu_files(writer, fh, files_out)
                log(
                    f"  -> {Counter(r['estat'] for r in files_out)} text_chars={meta.get('text_chars', len(text))} "
                    f"err={meta.get('error') or '-'}"
                )
                meta.pop("text", None)
                del text
            except Exception as exc:  # noqa: BLE001
                detall = f"excepció_interna:{type(exc).__name__}"
                log(f"  ERROR inesperat a {url[:120]}: {type(exc).__name__}: {exc}")
                files_out = [
                    {
                        **p,
                        "url_wayback": url_id,
                        "estat": "captura_no_llegible",
                        "detall": detall,
                    }
                    for p in per_url[url]
                ]
                escriu_files(writer, fh, files_out)
            finally:
                import gc
                gc.collect()
    finally:
        fh.close()

    # Si no estem en mode prova parcial, o si ja estan tots fets, genera informe
    fets2 = carrega_fets(args.out)
    if len(fets2) >= len(parells) and not args.limit_urls:
        genera_informe(args.out, args.informe, extra, wb_stats)
        log(f"Fet. Informe: {args.informe}")
    else:
        log(f"Progrés: {len(fets2)}/{len(parells)} parells al CSV. Informe pendent de completar el recorregut.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

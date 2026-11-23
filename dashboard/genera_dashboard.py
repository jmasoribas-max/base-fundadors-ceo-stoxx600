#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador del dashboard estàtic de la base Fundadors (STOXX Europe 600, 2016-2025).

Ús, des de l'arrel del repositori:

    python3 dashboard/genera_dashboard.py

Què fa:

- Comprova el SHA-256 de `dades/base_isin_any_v8r3.csv` i de
  `docs/REGISTRE_CANVIS.csv` contra `MANIFEST_SHA256.csv` del mateix commit.
  Si no coincideixen, s'atura i no escriu res.
- Llegeix només fitxers del repositori (csv, pathlib, hashlib). No fa cap
  petició de xarxa ni consulta Wayback ni les fonts originals.
- Reescriu només fitxers dins de `dashboard/`: `index.html`, `metodologia.html`,
  `empreses/{ISIN}.html` i `assets/` (CSS i JS).
- El resultat és determinista: amb les mateixes dades, els mateixos fitxers.

No llegeix l'`.xlsx`, ni `empreses/*.md`, ni `INDEX.md`, ni
`docs/REGISTRE_CANVIS.md`, ni cap fitxer de fora del repositori.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import re
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit

# ---------------------------------------------------------------------------
# Configuració
# ---------------------------------------------------------------------------

# Sector ICB: NO es mostra ni es fa servir als filtres fins que Jordi aclareixi
# la llicència (FTSE Russell / LSEG). Posar-ho a True només amb el seu OK.
MOSTRA_SECTOR = False

REPO_GITHUB = "https://github.com/jmasoribas-max/base-fundadors-ceo-stoxx600"
ANYS_PANELL = list(range(2016, 2026))

# Cites: fragments curts. Si una cita passa d'aquesta llargada, es mostra un
# fragment marcat amb […] i s'indica que el text complet és al registre.
LONGITUD_MAX_CITA = 600
# Notes més llargues que això es mostren plegades (es poden desplegar senceres).
LONGITUD_NOTA_PLEGADA = 700

ROOT = Path(__file__).resolve().parent.parent
SORTIDA = ROOT / "dashboard"
BASE = ROOT / "dades" / "base_isin_any_v8r3.csv"
REGISTRE = ROOT / "docs" / "REGISTRE_CANVIS.csv"
MANIFEST = ROOT / "MANIFEST_SHA256.csv"
# CSV opcional (no existeix ara): id_document_o_font,url_wayback[,timestamp]
# Només s'usa si existeix; no s'inventa mai.
WAYBACK_EXTRA = SORTIDA / "fonts_wayback_extra.csv"

# Criteris de la part pública ------------------------------------------------
# Termes que no es mostren mai (fitxers interns i columnes o notes de decisió).
# Si surten a la cita o a l'URL d'una prova, la prova sencera queda oculta; si
# només surten a les notes, s'oculta la nota. Per decisió de Jordi (23/11/2026),
# sí que es mostren les proves de LSEG (inclosa Refinitiv), les de fonts
# Bloomberg i les cites amb dates de naixement publicades per l'emissor.
RE_RESTRINGIT = re.compile(
    r"wrds|(?<![a-z0-9])article_?1(?![0-9])|no_per_a_ia|pes_pct|"
    r"founderceo_rob|sim_nota|sim_decisio|v75_decisio|ids_decisio|"
    r"model_verificacio|informe\s+intern",
    re.I,
)
# Noms de bots o models a les notes: la nota no es mostra (en cas de dubte, no).
RE_BOTS_I = re.compile(
    r"chat\s*-?gpt|\bgpt-?\d|\bcodex\b|(?<!cap\s)\bgemini\b(?!\s+computer)|"
    r"\bcopilot\b|\bopenai\b|\banthropic\b|_claude|claude_",
    re.I,
)
# Proves de sector ICB (PDF de components STOXX): només es mostren si MOSTRA_SECTOR.
RE_SECTOR_URL = re.compile(r"stoxx\.com/document/Indices/Factsheets_Components", re.I)
RE_SECTOR_NOTA = re.compile(r"\bICB\b|funcio_sector", re.I)
# «Claude» com a model; no «Jean-Claude», «Claude Bébéar», «Claude Moët»...
RE_BOTS_CLAUDE = re.compile(r"(?<![-\w])Claude(?!\s+[A-ZÀ-ÖØ-Þ])|(?<![-\w])claude(?![-\w])")

ETIQUETES = {
    "1": ("F", "Fundador-CEO"),
    "0": ("P", "Professional"),
    "no_determinat": ("ND", "No determinat"),
    "NA_sense_ceo": ("NA", "Sense CEO"),
}
ORDRE_ETIQ = ["F", "P", "ND", "NA"]
CERTIFICACIO = {
    "certificada": "Certificada",
    "certificada_ceo_pendent": "Certificada, CEO pendent",
    "no_certificada": "No certificada",
    "fora_mostra_auditoria": "Fora de la mostra d'auditoria",
}
FUNCIONS = {
    "ceo": "CEO",
    "fundador": "Fundador / classificació",
    "context": "Context",
    "datacio": "Datació",
    "revisio_font": "Revisió de font",
}
ESTAT_WAYBACK = {
    "existent": "captura existent",
    "pendent_verificacio_externa": "pendent de verificació externa",
    "ja_tenia_wayback_v8": "captura ja present a la v8",
    "nova": "captura nova",
    "existent_truncada": "captura existent però truncada",
    "verificada": "captura verificada",
}
# País d'emissió de l'ISIN, derivat del prefix (NO és la seu social ni un camp
# de la base).
PAISOS_ISIN = {
    "AT": "Àustria", "AU": "Austràlia", "BE": "Bèlgica", "BM": "Bermudes",
    "CA": "Canadà", "CH": "Suïssa", "CW": "Curaçao", "CY": "Xipre",
    "CZ": "Txèquia", "DE": "Alemanya", "DK": "Dinamarca", "ES": "Espanya",
    "FI": "Finlàndia", "FO": "Illes Fèroe", "FR": "França", "GB": "Regne Unit",
    "GG": "Guernsey", "GI": "Gibraltar", "GR": "Grècia", "HU": "Hongria",
    "IE": "Irlanda", "IL": "Israel", "IM": "Illa de Man", "IS": "Islàndia",
    "IT": "Itàlia", "JE": "Jersey", "KY": "Illes Caiman", "LI": "Liechtenstein",
    "LU": "Luxemburg", "MC": "Mònaco", "MT": "Malta", "NL": "Països Baixos",
    "NO": "Noruega", "PL": "Polònia", "PT": "Portugal", "SE": "Suècia",
    "US": "Estats Units", "VG": "Illes Verges Britàniques", "ZA": "Sud-àfrica",
}

# ---------------------------------------------------------------------------
# Utilitats
# ---------------------------------------------------------------------------


def esc(s: object) -> str:
    return html.escape("" if s is None else str(s), quote=True)


def fmt_int(n: int) -> str:
    s = f"{n:,}".replace(",", ".")
    return s


def fmt_pct(num: int, den: int, decimals: int = 1) -> str:
    if not den:
        return "—"
    pct = 100 * num / den
    if 0 < pct < 10 ** -decimals:
        decimals = 2
    return f"{pct:.{decimals}f}".replace(".", ",") + " %"


def norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip())


def norm_cerca(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("​", "")
    return re.sub(r"\s+", " ", s.lower()).strip()


def clau_ordre(s: str) -> str:
    return norm_cerca(s)


def comprimeix_anys(anys) -> str:
    anys = sorted(set(anys))
    if not anys:
        return "—"
    trams = []
    ini = prev = anys[0]
    for a in anys[1:]:
        if a == prev + 1:
            prev = a
            continue
        trams.append((ini, prev))
        ini = prev = a
    trams.append((ini, prev))
    return ", ".join(str(a) if a == b else f"{a}–{b}" for a, b in trams)


def expandeix_anys(text: str) -> tuple[list[int], bool]:
    """Expandeix `2016-2020`, `2016-2020,2022`, `2016–2025`, `2016, 2018`..."""
    anys: set[int] = set()
    ok = True
    for part in re.split(r"[,;]", text or ""):
        part = part.strip()
        if not part:
            continue
        m = re.fullmatch(r"(\d{4})\s*[-–—]\s*(\d{4})", part)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            if a <= b:
                anys.update(range(a, b + 1))
            else:
                ok = False
        elif re.fullmatch(r"\d{4}", part):
            anys.add(int(part))
        else:
            ok = False
    if not anys:
        ok = False
    return sorted(anys), ok


def url_segura(url: str) -> str | None:
    url = (url or "").strip()
    if re.match(r"^https?://", url, re.I) and not re.search(r"[\s\"'<>]", url):
        return url
    return None


def domini(url: str) -> str:
    try:
        host = urlsplit(url).hostname or ""
    except ValueError:
        return ""
    return host[4:] if host.startswith("www.") else host


def data_wayback(ts: str) -> str:
    ts = (ts or "").strip()
    if re.fullmatch(r"\d{8,14}", ts):
        return f"{ts[6:8]}/{ts[4:6]}/{ts[0:4]}"
    return ""


def ts_de_url_wayback(url: str) -> str:
    m = re.search(r"web\.archive\.org/web/(\d{8,14})", url or "")
    return m.group(1) if m else ""


def slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", s).strip("-") or "x"


def afegeix(llista: list, valor: str) -> None:
    valor = (valor or "").strip()
    if valor and valor not in llista:
        llista.append(valor)


def te_bot(s: str) -> bool:
    return bool(RE_BOTS_I.search(s or "") or RE_BOTS_CLAUDE.search(s or ""))


def te_restringit(s: str) -> bool:
    return bool(RE_RESTRINGIT.search(s or ""))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def git(*args: str) -> str | None:
    try:
        r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    except OSError:
        return None
    return r.stdout.strip() if r.returncode == 0 else None


def atura(msg: str) -> None:
    print(f"ATURAT: {msg}", file=sys.stderr)
    raise SystemExit(2)


# ---------------------------------------------------------------------------
# Integritat i procedència
# ---------------------------------------------------------------------------


def comprova_integritat(sha_esperat: str | None) -> dict[str, str]:
    if not MANIFEST.exists():
        atura("no trobo MANIFEST_SHA256.csv")
    with MANIFEST.open(encoding="utf-8", newline="") as f:
        manifest = {r["fitxer"]: r["sha256"] for r in csv.DictReader(f)}
    shas = {}
    for p in (BASE, REGISTRE):
        rel = p.relative_to(ROOT).as_posix()
        if not p.exists():
            atura(f"no trobo {rel}")
        h = sha256(p)
        if rel not in manifest:
            atura(f"{rel} no és a MANIFEST_SHA256.csv")
        if manifest[rel] != h:
            atura(f"el SHA-256 de {rel} ({h}) no coincideix amb el del manifest ({manifest[rel]})")
        shas[rel] = h
    rel_base = BASE.relative_to(ROOT).as_posix()
    if sha_esperat and shas[rel_base] != sha_esperat:
        atura(f"el SHA-256 de {rel_base} ({shas[rel_base]}) no és l'esperat ({sha_esperat})")
    return shas


def commit_referencia(commit_arg: str | None) -> tuple[str, str]:
    """Commit de main de què parteix l'arbre (merge-base), estable entre commits
    de la mateixa branca. Es pot forçar amb --commit."""
    sha = commit_arg
    if not sha:
        # La còpia local de `main` pot estar endarrerida respecte d'`origin/main`:
        # es pren el merge-base més recent dels dos.
        candidats = []
        for ref in ("main", "origin/main"):
            mb = git("merge-base", "HEAD", ref)
            if mb and mb not in candidats:
                candidats.append(mb)
        for mb in candidats:
            if all(o == mb or git("merge-base", "--is-ancestor", o, mb) is not None for o in candidats):
                sha = mb
                break
        if not sha and candidats:
            sha = candidats[0]
    if not sha:
        sha = git("rev-parse", "HEAD")
    if not sha:
        return "desconegut", ""
    data = git("show", "-s", "--format=%cs", sha) or ""
    return sha, data


# ---------------------------------------------------------------------------
# Lectura i model
# ---------------------------------------------------------------------------


def llegeix_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def llegeix_wayback_extra() -> dict[str, dict[str, str]]:
    if not WAYBACK_EXTRA.exists():
        return {}
    extra = {}
    for r in llegeix_csv(WAYBACK_EXTRA):
        ident = (r.get("id_document_o_font") or "").strip()
        url = (r.get("url_wayback") or "").strip()
        if ident and re.match(r"^https?://web\.archive\.org/web/", url, re.I):
            extra[ident] = {"url": url, "timestamp": (r.get("timestamp") or "").strip()}
    return extra


def carrega_model(stats: Counter) -> dict:
    base = llegeix_csv(BASE)
    registre = llegeix_csv(REGISTRE)
    wb_extra = llegeix_wayback_extra()
    stats["wayback_extra_files"] = len(wb_extra)

    files_per_isin: dict[str, list[dict]] = defaultdict(list)
    for r in base:
        if r["FounderCEO"] not in ETIQUETES:
            atura(f"FounderCEO desconegut a {r['isin']} {r['any']}: {r['FounderCEO']!r}")
        files_per_isin[r["isin"]].append(r)
    for files in files_per_isin.values():
        files.sort(key=lambda r: int(r["any"]))

    # --- Registre: agrupa per (isin, id, cita, url) i expandeix anys ---------
    grups: dict[tuple, dict] = {}
    for r in registre:
        isin = r["isin"].strip()
        ident = r["id_document_o_font"].strip()
        cita = norm_ws(r["cita_literal"])
        url = (r["url_font"] or "").strip()
        clau = (isin, ident, cita, url)
        anys, ok = expandeix_anys(r["anys"])
        if not ok:
            stats["registre_anys_no_interpretables"] += 1
        g = grups.get(clau)
        if g is None:
            g = grups[clau] = {
                "isin": isin, "id": ident, "cita": cita, "url": url,
                "anys": set(), "anys_text": [], "tipus": [], "funcio": [],
                "marca_prova": [], "veritat": [], "allotjament": [],
                "origen_cita": [], "notes": [], "marques": [], "wb": [],
                "wb_estat": [], "wb_ts": [], "capt": [], "n_files": 0,
            }
        g["anys"].update(anys)
        afegeix(g["anys_text"], r["anys"])
        afegeix(g["tipus"], r["tipus"])
        afegeix(g["funcio"], r["funcio_cita"])
        afegeix(g["marca_prova"], r["marca_prova"])
        afegeix(g["veritat"], r["marca_veritat"])
        afegeix(g["allotjament"], r["allotjament"])
        afegeix(g["origen_cita"], r["origen_cita"])
        afegeix(g["notes"], r["notes"])
        afegeix(g["marques"], r["marques_fundador"])
        afegeix(g["wb"], r["url_wayback"])
        afegeix(g["wb_estat"], r["wayback_v8r1_estat"])
        afegeix(g["wb_ts"], r["wayback_v8r1_timestamp"])
        afegeix(g["capt"], r["cita_verificada_a_captura"])
        g["n_files"] += 1
    stats["registre_files"] = len(registre)
    stats["registre_proves_agrupades"] = len(grups)

    proves_per_isin: dict[str, list[dict]] = defaultdict(list)
    for g in grups.values():
        if g["isin"] not in files_per_isin:
            stats["registre_isin_fora_base"] += 1
            continue
        prepara_prova(g, wb_extra, stats)
        proves_per_isin[g["isin"]].append(g)

    empreses = {}
    for isin in sorted(files_per_isin):
        empreses[isin] = construeix_empresa(isin, files_per_isin[isin], proves_per_isin.get(isin, []), stats)
    return {"empreses": empreses, "n_files": len(base)}


def prepara_prova(g: dict, wb_extra: dict, stats: Counter) -> None:
    # Grup de presentació (per funcio_cita; si és buida, pel tipus d'entrada).
    f = g["funcio"]
    if "ceo" in f:
        grup = "ceo"
    elif "fundador" in f:
        grup = "fundador"
    elif f:
        grup = "altres"
    elif set(g["tipus"]) & {"evidencia_ceo", "ceo"}:
        grup = "ceo"
    elif set(g["tipus"]) & {"evidencia_fundador", "etiqueta", "font_classificacio"}:
        grup = "fundador"
    else:
        grup = "altres"
    g["grup"] = grup
    g["origen"] = "registre"
    g["anys"] = sorted(g["anys"])
    g["es_v"] = "[V]" in g["veritat"]

    # Wayback: el del registre; si no n'hi ha cap d'URL vàlida, l'extra opcional.
    wbs = [u for u in g["wb"] if re.match(r"^https?://web\.archive\.org/web/", u, re.I)]
    g["wb_urls"] = wbs
    g["wb_pendent"] = any(u.lower() == "pendent_verificacio_externa" for u in g["wb"])
    g["wb_extra"] = None
    if not wbs and g["id"] in wb_extra:
        g["wb_extra"] = wb_extra[g["id"]]
        stats["proves_amb_wayback_extra"] += 1

    # Criteris de la part pública.
    camps_cita = [g["cita"], g["url"], *g["wb_urls"]]
    if g["wb_extra"]:
        camps_cita.append(g["wb_extra"]["url"])
    g["ocult"] = ""
    if any(te_restringit(c) for c in camps_cita):
        g["ocult"] = "restringit"
        stats["proves_ocultes_terme_restringit"] += 1
    elif not MOSTRA_SECTOR and (RE_SECTOR_URL.search(g["url"]) or any(RE_SECTOR_NOTA.search(n) for n in g["notes"])):
        g["ocult"] = "sector"
        stats["proves_ocultes_sector"] += 1
    notes = []
    for n in g["notes"]:
        if te_restringit(n):
            notes.append((n, "restringit"))
            stats["notes_ocultes_terme_restringit"] += 1
        elif te_bot(n):
            notes.append((n, "bot"))
            stats["notes_ocultes_nom_model"] += 1
        else:
            notes.append((n, ""))
    g["notes_pub"] = notes
    orig = []
    for o in g["origen_cita"]:
        if te_bot(o) or te_restringit(o):
            orig.append((o, "oculta"))
            stats["origen_cita_ocult"] += 1
        else:
            orig.append((o, ""))
    g["origen_pub"] = orig
    joined = " ".join(g["notes"])
    g["no_valida"] = "no_valida" in joined
    g["pendent_df"] = "pendent_DF" in joined


def construeix_empresa(isin: str, files: list[dict], proves: list[dict], stats: Counter) -> dict:
    anys_base = [int(r["any"]) for r in files]
    set_anys = set(anys_base)
    nom = files[-1]["nom_panell"].replace("​", "").strip()
    altres_noms = []
    for r in files:
        n = r["nom_panell"].replace("​", "").strip()
        if n != nom:
            afegeix(altres_noms, n)

    # Anys de cada prova que no són al panell de l'ISIN (es mostren igualment).
    for p in proves:
        p["anys_fora"] = [a for a in p["anys"] if a not in set_anys]
        if p["anys_fora"]:
            stats["proves_amb_anys_fora_panell"] += 1

    # Indicadors per any (funcio_cita estricta, com demana l'encàrrec).
    prova_ceo: dict[int, str] = {}
    prova_fund: dict[int, str] = {}
    cobert: set[int] = set()
    for p in proves:
        for a in p["anys"]:
            cobert.add(a)
            for funcio, dest in (("ceo", prova_ceo), ("fundador", prova_fund)):
                if funcio in p["funcio"]:
                    if p["es_v"]:
                        dest[a] = "V"
                    else:
                        dest.setdefault(a, "NV")

    # Cites que només són al CSV de la base.
    reg_index = defaultdict(list)
    for p in proves:
        reg_index[(p["cita"], p["url"])].append(p["id"])
    base_cites: dict[tuple, dict] = {}
    for r in files:
        a = int(r["any"])
        cita = norm_ws(r["font_classificacio_cita"])
        url = (r["font_classificacio_url"] or "").strip()
        if cita or url:
            k = ("font_classificacio", cita, url, "")
            d = base_cites.setdefault(k, {"tipus": "font_classificacio", "cita": cita, "url": url, "anys": [], "dada": ""})
            d["anys"].append(a)
        d37c = (r["d37_cita_contemporania"] or "").strip()
        d37u = (r["d37_cita_contemp_url"] or "").strip()
        es_indicador = d37c.lower() in {"si", "no", "si_cita_alternativa"}
        if d37u or (d37c and not es_indicador):
            k = ("d37", d37c, d37u, r["d37_cita_contemp_data"].strip())
            d = base_cites.setdefault(k, {"tipus": "d37", "cita": d37c, "url": d37u, "anys": [], "dada": r["d37_cita_contemp_data"].strip()})
            d["anys"].append(a)
    cites_base = []
    for d in base_cites.values():
        d["anys"] = sorted(set(d["anys"]))
        d["ids_registre"] = sorted(set(reg_index.get((d["cita"], d["url"]), []))) if d["tipus"] == "font_classificacio" else []
        d["ocult"] = te_restringit(d["cita"]) or te_restringit(d["url"])
        if d["ocult"]:
            stats["cites_base_ocultes_terme_restringit"] += 1
        cites_base.append(d)
    cites_base.sort(key=lambda d: (d["anys"][0] if d["anys"] else 0, d["tipus"], d["cita"]))
    base_fund_anys = {a for d in cites_base for a in d["anys"]}

    # Rastre secundari v75 (només si no hi ha cap cita estructurada).
    rastre = []
    if not proves and not cites_base:
        urls: dict[str, list[int]] = {}
        for r in files:
            for u in (r["v75_urls_arxivades"] or "").split(";"):
                u = u.strip()
                if u:
                    urls.setdefault(u, []).append(int(r["any"]))
        for u, anys in urls.items():
            if te_restringit(u):
                stats["v75_urls_ocultes_terme_restringit"] += 1
                continue
            rastre.append({"url": u, "anys": sorted(set(anys))})
        rastre.sort(key=lambda d: (d["anys"][0], d["url"]))

    anys_info = []
    recompte = Counter()
    certs = []
    ceos_noms = []
    for r in files:
        a = int(r["any"])
        lletra, nom_etiq = ETIQUETES[r["FounderCEO"]]
        recompte[lletra] += 1
        afegeix(certs, r["sim_estat_certificacio"])
        ceos = [c.strip() for c in (r["ceos"] or "").split("|") if c.strip()]
        for c in ceos:
            afegeix(ceos_noms, c)
        aplicat = (r["sim_ceo_aplicat"] or "").strip()
        anys_info.append({
            "any": a,
            "ceos": ceos,
            "ceos_text": (r["ceos"] or "").strip(),
            "lletra": lletra,
            "etiqueta": nom_etiq,
            "cert": r["sim_estat_certificacio"],
            "nivell": (r["sim_nivell"] or "").strip(),
            "aplicat": aplicat if aplicat and aplicat != (r["ceos"] or "").strip() else "",
            "prova_ceo": prova_ceo.get(a, ""),
            "prova_fund": prova_fund.get(a, ""),
            "base_fund": a in base_fund_anys,
            "cobert": a in cobert or a in base_fund_anys,
            "supersector": (r["supersector_fix"] or "").strip(),
            "estat_sector": r["estat_sector"],
        })

    proves.sort(key=lambda p: (p["anys"][0] if p["anys"] else 9999, p["id"], p["cita"]))
    usats = Counter()
    for p in proves:
        s = slug(p["id"])
        usats[s] += 1
        p["ancora"] = f"p-{s}" if usats[s] == 1 else f"p-{s}-{usats[s]}"

    pais_codi = isin[:2]
    if pais_codi not in PAISOS_ISIN:
        stats["prefix_isin_sense_nom"] += 1
    return {
        "isin": isin,
        "nom": nom,
        "altres_noms": altres_noms,
        "pais_codi": pais_codi,
        "pais": PAISOS_ISIN.get(pais_codi, f"prefix {pais_codi}"),
        "anys": anys_base,
        "files": anys_info,
        "recompte": recompte,
        "certs": certs,
        "ceos_noms": ceos_noms,
        "proves": proves,
        "cites_base": cites_base,
        "rastre": rastre,
        "supersector": next((x["supersector"] for x in anys_info if x["supersector"]), ""),
        "estats_sector": sorted({x["estat_sector"] for x in anys_info}),
    }


# ---------------------------------------------------------------------------
# HTML comú
# ---------------------------------------------------------------------------


class Context:
    def __init__(self, commit: str, data_commit: str, shas: dict[str, str]):
        self.commit = commit
        self.data_commit = data_commit
        self.sha_base = shas[BASE.relative_to(ROOT).as_posix()]
        self.sha_registre = shas[REGISTRE.relative_to(ROOT).as_posix()]


def curt(sha: str, n: int = 7) -> str:
    return sha[:n] if len(sha) > n else sha


def avis(ctx: Context) -> str:
    return (
        '<aside class="avis" role="note">'
        '<span class="avis-icona" aria-hidden="true">!</span>'
        '<p><strong>Base en revisió final.</strong> '
        f'Dades de <code>main</code> (commit <code title="{esc(ctx.commit)}">{esc(curt(ctx.commit))}</code>, '
        f'CSV <code title="{esc(ctx.sha_base)}">{esc(curt(ctx.sha_base, 12))}…</code>). '
        "Encara no és la v9 congelada. Algunes files tenen etiqueta però no tenen cita estructurada al registre.</p>"
        "</aside>"
    )


def pagina(ctx: Context, *, titol: str, descripcio: str, cos: str, prefix: str,
           actiu: str, scripts: tuple[str, ...] = ()) -> str:
    nav = []
    for clau, href, text in (("inici", "index.html", "Empreses"),
                             ("metodologia", "metodologia.html", "Metodologia i llegenda")):
        cur = ' aria-current="page"' if clau == actiu else ""
        nav.append(f'<a href="{prefix}{href}"{cur}>{text}</a>')
    js = "".join(f'<script src="{prefix}assets/{s}" defer></script>' for s in scripts)
    data = f" ({esc(ctx.data_commit)})" if ctx.data_commit else ""
    return f"""<!doctype html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{esc(titol)}</title>
<meta name="description" content="{esc(descripcio)}">
<link rel="stylesheet" href="{prefix}assets/style.css">
<script>document.documentElement.className+=' js';</script>
{js}
</head>
<body>
<a class="salta" href="#contingut">Salta al contingut</a>
<header class="barra">
<div class="barra-in">
<a class="marca" href="{prefix}index.html"><span class="marca-logo" aria-hidden="true"><i></i><i></i><i></i></span><span class="marca-text">Dashboard Fundadors<small>STOXX Europe 600 · 2016–2025</small></span></a>
<nav class="nav" aria-label="Navegació principal">{''.join(nav)}</nav>
</div>
</header>
<main id="contingut" class="pagina">
{cos}
</main>
<footer class="peu">
<div class="peu-in">
<p>Generat per <code>dashboard/genera_dashboard.py</code> a partir del repositori. Commit de referència de <code>main</code>: <code>{esc(ctx.commit)}</code>{data}.</p>
<p><code>dades/base_isin_any_v8r3.csv</code> SHA-256 <code>{esc(ctx.sha_base)}</code> · <code>docs/REGISTRE_CANVIS.csv</code> SHA-256 <code>{esc(ctx.sha_registre)}</code></p>
<p>Versió provisional, publicada a GitHub Pages mentre la base està en revisió final. La metodologia que mana és la del <a href="{REPO_GITHUB}" target="_blank" rel="noopener noreferrer">repositori</a>; aquest lloc no la substitueix.</p>
</div>
</footer>
</body>
</html>
"""


def cel_etiq(lletra: str, titol: str, petita: bool = False) -> str:
    cls = "cel cel-p" if petita else "cel"
    return f'<span class="{cls} e-{lletra}" title="{esc(titol)}">{lletra}</span>'


def cel_buida(titol: str, petita: bool = False) -> str:
    if petita:
        return f'<span class="cel cel-p cel-buida" title="{esc(titol)}"></span>'
    return f'<span class="cel cel-buida" title="{esc(titol)}"><span class="vh">{esc(titol)}</span></span>'


def badge_etiq(lletra: str) -> str:
    nom = {v[0]: v[1] for v in ETIQUETES.values()}[lletra]
    return f'<span class="etq e-{lletra}"><b>{lletra}</b> {esc(nom)}</span>'


def enllac_ext(url: str, text: str, cls: str = "") -> str:
    u = url_segura(url)
    c = f' class="{cls}"' if cls else ""
    if not u:
        return f"<span{c}>{esc(text)}</span>"
    return f'<a{c} href="{esc(u)}" target="_blank" rel="noopener noreferrer">{esc(text)}<span class="ext" aria-hidden="true">↗</span></a>'


# ---------------------------------------------------------------------------
# Pàgina d'inici
# ---------------------------------------------------------------------------


def calcula_resum(model: dict) -> dict:
    emp = model["empreses"]
    rec = Counter()
    per_any = defaultdict(Counter)
    files_ceo = files_fund = files_coberts = 0
    amb_registre = sense_cita = 0
    for e in emp.values():
        if e["proves"]:
            amb_registre += 1
        if not e["proves"] and not e["cites_base"]:
            sense_cita += 1
        for f in e["files"]:
            rec[f["lletra"]] += 1
            per_any[f["any"]][f["lletra"]] += 1
            per_any[f["any"]]["total"] += 1
            files_ceo += bool(f["prova_ceo"])
            files_fund += bool(f["prova_fund"])
            files_coberts += bool(f["cobert"])
    return {
        "n_isin": len(emp), "n_files": model["n_files"], "rec": rec, "per_any": per_any,
        "amb_registre": amb_registre, "sense_cita": sense_cita,
        "files_ceo": files_ceo, "files_fund": files_fund,
        "files_sense_cita": model["n_files"] - files_coberts,
    }


def grafic_f_per_any(resum: dict) -> str:
    per_any = resum["per_any"]
    anys = sorted(per_any)
    maxim = max((per_any[a]["F"] for a in anys), default=0)
    pas = 10 if maxim <= 60 else 20
    sostre = max(pas, -(-maxim // pas) * pas)
    ticks = list(range(0, sostre + 1, pas))
    eix = "".join(
        f'<span class="tick" style="bottom:{100 * t / sostre:.2f}%"><span>{t}</span></span>' for t in ticks
    )
    cols = []
    files_taula = []
    for a in anys:
        f, tot = per_any[a]["F"], per_any[a]["total"]
        alt = 100 * f / sostre if sostre else 0
        tip = f"{a}: {fmt_int(f)} files F de {fmt_int(tot)} ({fmt_pct(f, tot)})"
        cols.append(
            f'<div class="bcol" tabindex="0" aria-label="{esc(tip)}">'
            f'<div class="barea"><span class="bar" style="height:{alt:.2f}%"></span></div>'
            f'<span class="bany">{a}</span><span class="tip" role="tooltip">{esc(tip)}</span></div>'
        )
        files_taula.append(
            f"<tr><td>{a}</td><td class='num'>{fmt_int(f)}</td><td class='num'>{fmt_int(tot)}</td><td class='num'>{fmt_pct(f, tot)}</td></tr>"
        )
    return f"""<figure class="panell grafic">
<figcaption><h2 class="h-panell">Files F per any</h2><p class="nota">Files amb FounderCEO = 1 (fundador-CEO) cada any. Passa el cursor o el focus per sobre d'una barra per veure'n el detall.</p></figcaption>
<div class="barres" role="img" aria-label="Files F per any, de {anys[0] if anys else ''} a {anys[-1] if anys else ''}">
<div class="eix">{eix}</div>
<div class="bcols">{''.join(cols)}</div>
</div>
<details class="dades"><summary>Mostra les dades en una taula</summary>
<table class="taula-simple"><thead><tr><th>Any</th><th class="num">Files F</th><th class="num">Files al panell</th><th class="num">% F</th></tr></thead><tbody>{''.join(files_taula)}</tbody></table>
</details>
</figure>"""


def mesurador(etiqueta: str, valor: int, total: int, nota: str = "") -> str:
    pct = 100 * valor / total if total else 0
    nota_html = f'<span class="m-nota">{esc(nota)}</span>' if nota else ""
    return (
        '<div class="mesura">'
        f'<div class="m-cap"><span class="m-etq">{esc(etiqueta)}</span>'
        f'<span class="m-val"><b>{fmt_int(valor)}</b> de {fmt_int(total)} · {fmt_pct(valor, total)}</span></div>'
        f'<div class="m-pista" aria-hidden="true"><span style="width:{pct:.2f}%"></span></div>{nota_html}</div>'
    )


def pagina_inici(ctx: Context, model: dict, resum: dict) -> str:
    emp = model["empreses"]
    rec = resum["rec"]
    nf = resum["n_files"]
    tiles = [
        ('<span class="k-etq">Empreses (ISIN)</span>', fmt_int(resum["n_isin"]), "al panell 2016–2025", ""),
        ('<span class="k-etq">Files ISIN-any</span>', fmt_int(nf), "unitat d'anàlisi", ""),
    ]
    for lletra in ORDRE_ETIQ:
        nom = {v[0]: v[1] for v in ETIQUETES.values()}[lletra]
        tiles.append((
            f'<span class="k-etq"><span class="punt e-{lletra}" aria-hidden="true"></span>{lletra} · {esc(nom)}</span>',
            fmt_int(rec[lletra]), f"{fmt_pct(rec[lletra], nf)} de les files", f" k-{lletra}",
        ))
    tiles_html = "".join(
        f'<div class="kpi{cls}">{etq}<span class="k-val">{val}</span><span class="k-sub">{esc(sub)}</span></div>'
        for etq, val, sub, cls in tiles
    )
    cobertura = f"""<section class="panell cobertura" aria-labelledby="h-cob">
<h2 class="h-panell" id="h-cob">Cobertura de proves</h2>
<p class="nota">Calculada a partir de <code>docs/REGISTRE_CANVIS.csv</code> i dels camps de cita de la base.</p>
{mesurador("Empreses amb almenys una entrada al registre", resum["amb_registre"], resum["n_isin"])}
{mesurador("Files amb prova de CEO al registre", resum["files_ceo"], nf, "funcio_cita = ceo")}
{mesurador("Files amb prova de classificació al registre", resum["files_fund"], nf, "funcio_cita = fundador")}
{mesurador("Files sense cap cita estructurada", resum["files_sense_cita"], nf, "ni al registre ni als camps de cita de la base")}
<p class="nota">{fmt_int(resum["sense_cita"])} empreses no tenen cap cita estructurada en aquests fitxers d'origen; la seva fitxa ho indica.</p>
</section>"""

    # Opcions de filtre
    certs = Counter()
    paisos = Counter()
    sectors = Counter()
    for e in emp.values():
        for c in e["certs"]:
            certs[c] += 1
        paisos[(e["pais_codi"], e["pais"])] += 1
        if MOSTRA_SECTOR:
            sectors[e["supersector"] or "sense sector"] += 1
    opt_cert = "".join(
        f'<option value="{esc(c)}">{esc(CERTIFICACIO.get(c, c))} ({fmt_int(n)})</option>'
        for c, n in sorted(certs.items(), key=lambda x: list(CERTIFICACIO).index(x[0]) if x[0] in CERTIFICACIO else 99)
    )
    opt_pais = "".join(
        f'<option value="{esc(codi)}">{esc(nom)} · {esc(codi)} ({fmt_int(n)})</option>'
        for (codi, nom), n in sorted(paisos.items(), key=lambda x: clau_ordre(x[0][1]))
    )
    filtre_sector = ""
    if MOSTRA_SECTOR:
        opt_sec = "".join(f'<option value="{esc(s)}">{esc(s)} ({fmt_int(n)})</option>' for s, n in sorted(sectors.items()))
        filtre_sector = f'<label class="camp"><span>Supersector</span><select id="f-sector"><option value="">Tots</option>{opt_sec}</select></label>'

    files_html = []
    for e in sorted(emp.values(), key=lambda e: (clau_ordre(e["nom"]), e["isin"])):
        per_any = {f["any"]: f for f in e["files"]}
        cel = []
        for a in ANYS_PANELL:
            f = per_any.get(a)
            if f:
                ceo = f["ceos_text"].replace("|", " · ") or "sense CEO"
                cel.append(cel_etiq(f["lletra"], f"{a} · {f['lletra']} · {ceo}", petita=True))
            else:
                cel.append(cel_buida(f"{a}: no és al panell", petita=True))
        r = e["recompte"]
        darrer = e["files"][-1]
        ceo_darrer = darrer["ceos_text"].replace("|", " · ") or "sense CEO"
        if e["proves"]:
            proves = "registre"
        elif e["cites_base"]:
            proves = "base"
        else:
            proves = "cap"
        n_proves = len(e["proves"]) + len(e["cites_base"])
        cerca = norm_cerca(" ".join([e["nom"], *e["altres_noms"], e["isin"], *e["ceos_noms"]]))
        etiq = " ".join(l for l in ORDRE_ETIQ if r[l])
        sec_attr = f' data-sector="{esc(e["supersector"] or "sense sector")}"' if MOSTRA_SECTOR else ""
        sec_td = f'<td class="c-sec">{esc(e["supersector"] or "sense sector")}</td>' if MOSTRA_SECTOR else ""
        proves_txt = fmt_int(n_proves) if n_proves else '<span class="buit" title="Sense cita estructurada">—</span>'
        files_html.append(
            f'<tr data-cerca="{esc(cerca)}" data-etiq="{etiq}" data-cert="{esc(" ".join(e["certs"]))}" '
            f'data-pais="{esc(e["pais_codi"])}" data-proves="{proves}"{sec_attr} data-nom="{esc(clau_ordre(e["nom"]))}" '
            f'data-isin="{esc(e["isin"])}" data-nanys="{len(e["anys"])}" data-f="{r["F"]}" data-np="{n_proves}">'
            f'<td class="c-nom"><a href="empreses/{esc(e["isin"])}.html">{esc(e["nom"])}</a>'
            f'<span class="sub">CEO {darrer["any"]}: {esc(ceo_darrer)}</span></td>'
            f'<td class="c-isin"><code>{esc(e["isin"])}</code></td>'
            f'<td class="c-pais">{esc(e["pais"])}</td>{sec_td}'
            f'<td class="c-anys">{esc(comprimeix_anys(e["anys"]))}<span class="sub">{len(e["anys"])} anys</span></td>'
            f'<td class="c-serie"><span class="serie" aria-label="Sèrie FounderCEO 2016–2025">{"".join(cel)}</span></td>'
            f'<td class="num c-f">{r["F"] or ""}</td><td class="num c-p">{r["P"] or ""}</td>'
            f'<td class="num c-nd">{r["ND"] or ""}</td><td class="num c-na">{r["NA"] or ""}</td>'
            f'<td class="num c-proves">{proves_txt}</td></tr>'
        )
    th_sec = '<th scope="col" class="c-sec">Supersector</th>' if MOSTRA_SECTOR else ""
    llegenda = "".join(
        f'<span class="ll"><span class="cel cel-p e-{l}" aria-hidden="true">{l}</span>{esc(n)}</span>'
        for l, n in (("F", "fundador-CEO"), ("P", "professional"), ("ND", "no determinat"), ("NA", "sense CEO"))
    ) + '<span class="ll"><span class="cel cel-p cel-buida" aria-hidden="true"></span>no és al panell</span>'

    cos = f"""<section class="heroi">
<p class="eyebrow">STOXX Europe 600 · 2016–2025</p>
<h1>Dashboard Fundadors</h1>
<p class="entradeta">Qui era el CEO de cada empresa el 31 d'octubre de cada any, si era fundador de l'empresa, i amb quina cita i quina font es documenta.</p>
</section>
{avis(ctx)}
<section class="kpis" aria-label="Xifres principals">{tiles_html}</section>
<div class="dos-panells">
{grafic_f_per_any(resum)}
{cobertura}
</div>
<section class="cercador" id="empreses" aria-labelledby="h-emp">
<div class="cap-seccio"><h2 id="h-emp">Empreses</h2><p class="recompte" aria-live="polite">Es mostren <b id="n-visibles">{fmt_int(len(emp))}</b> de {fmt_int(len(emp))} empreses</p></div>
<form class="filtres" id="filtres" role="search" onsubmit="return false">
<label class="camp camp-cerca"><span>Cerca per nom, ISIN o CEO</span><input type="search" id="f-cerca" placeholder="p. ex. Nestlé, DE000A0D9PT0, Arora…" autocomplete="off"></label>
<label class="camp"><span>Etiqueta FounderCEO</span><select id="f-etiq"><option value="">Totes</option><option value="F">Amb algun any F</option><option value="P">Amb algun any P</option><option value="ND">Amb algun any ND</option><option value="NA">Amb algun any NA</option></select></label>
<label class="camp"><span>Certificació</span><select id="f-cert"><option value="">Totes</option>{opt_cert}</select></label>
<label class="camp"><span>País d'emissió de l'ISIN <small>(derivat)</small></span><select id="f-pais"><option value="">Tots</option>{opt_pais}</select></label>
{filtre_sector}
<label class="camp"><span>Proves</span><select id="f-proves"><option value="">Totes</option><option value="registre">Amb entrades al registre</option><option value="base">Només cites de la base</option><option value="cap">Sense cita estructurada</option></select></label>
<button type="button" class="boto-sec" id="f-reset">Esborra els filtres</button>
</form>
<p class="nota">El país d'emissió es deriva del prefix de l'ISIN (GB, FR, DE…). No és la seu social ni un camp de la base. Els filtres d'etiqueta i de certificació mostren les empreses amb almenys un any amb aquell valor.</p>
<div class="llegenda" aria-label="Llegenda de la sèrie">{llegenda}</div>
<div class="taula-wrap">
<table class="taula-emp" id="taula">
<thead><tr>
<th scope="col" class="c-nom"><button type="button" data-ordre="nom" aria-sort="ascending">Empresa</button></th>
<th scope="col" class="c-isin"><button type="button" data-ordre="isin">ISIN</button></th>
<th scope="col" class="c-pais">País ISIN</th>{th_sec}
<th scope="col" class="c-anys"><button type="button" data-ordre="nanys">Anys</button></th>
<th scope="col" class="c-serie">Sèrie 2016–2025</th>
<th scope="col" class="num c-f"><button type="button" data-ordre="f" title="Nombre d'anys F">F</button></th>
<th scope="col" class="num c-p" title="Nombre d'anys P">P</th>
<th scope="col" class="num c-nd" title="Nombre d'anys ND">ND</th>
<th scope="col" class="num c-na" title="Nombre d'anys NA">NA</th>
<th scope="col" class="num c-proves"><button type="button" data-ordre="np" title="Proves del registre i cites de la base">Proves</button></th>
</tr></thead>
<tbody>
{chr(10).join(files_html)}
</tbody>
</table>
</div>
<p class="sense-resultat" id="cap-resultat" hidden>Cap empresa no coincideix amb la cerca i els filtres.</p>
</section>"""
    return pagina(ctx, titol="Dashboard Fundadors · STOXX Europe 600, 2016-2025",
                  descripcio="Base Fundadors: CEO a 31/10 de cada any, etiqueta FounderCEO i proves amb cita i font.",
                  cos=cos, prefix="", actiu="inici", scripts=("cerca.js",))


# ---------------------------------------------------------------------------
# Fitxa d'empresa
# ---------------------------------------------------------------------------


def linia_temps(e: dict) -> str:
    per_any = {f["any"]: f for f in e["files"]}
    anys_cel = []
    cels = []
    for i, a in enumerate(ANYS_PANELL, start=1):
        anys_cel.append(f'<span class="tl-any" style="grid-column:{i}">{a}</span>')
        f = per_any.get(a)
        if f:
            ceo = f["ceos_text"].replace("|", " · ") or "sense CEO"
            titol = f"{a} · {f['etiqueta']} · {ceo}"
            cels.append(f'<span class="tl-cel" style="grid-column:{i}">{cel_etiq(f["lletra"], titol)}</span>')
        else:
            cels.append(f'<span class="tl-cel" style="grid-column:{i}">{cel_buida(f"{a}: no és al panell")}</span>')
    # Trams de CEO: anys consecutius del panell amb el mateix valor de `ceos`.
    trams = []
    for i, a in enumerate(ANYS_PANELL, start=1):
        f = per_any.get(a)
        if not f:
            continue
        clau = f["ceos_text"]
        if trams and trams[-1]["clau"] == clau and trams[-1]["fi"] == a - 1:
            trams[-1]["fi"] = a
            trams[-1]["span"] += 1
            trams[-1]["lletres"].append(f["lletra"])
        else:
            trams.append({"clau": clau, "ini": a, "fi": a, "col": i, "span": 1, "ceos": f["ceos"],
                          "lletres": [f["lletra"]]})
    noms = []
    llista = []
    for t in trams:
        nom = " · ".join(t["ceos"]) if t["ceos"] else "Sense CEO"
        rang = str(t["ini"]) if t["ini"] == t["fi"] else f"{t['ini']}–{t['fi']}"
        cls = "tl-ceo" + (" tl-ceo-buit" if not t["ceos"] else "")
        if len(set(t["lletres"])) == 1:
            cls += f" v-{t['lletres'][0]}"
        noms.append(
            f'<span class="{cls}" style="grid-column:{t["col"]} / span {t["span"]}" title="{esc(nom)} · {rang}">'
            f'<b>{esc(nom)}</b><small>{rang}</small></span>'
        )
        cels_t = "".join(
            cel_etiq(l, f"{a} · {l}", petita=True) for a, l in zip(range(t["ini"], t["fi"] + 1), t["lletres"])
        )
        llista.append(
            f'<li class="{cls.replace("tl-ceo", "tram")}"><span class="tram-anys">{rang}</span>'
            f'<b class="tram-nom">{esc(nom)}</b><span class="serie">{cels_t}</span></li>'
        )
    return (
        '<div class="tl-wrap"><div class="tl" role="group" aria-label="CEO i etiqueta per any">'
        f'<div class="tl-fila">{"".join(anys_cel)}</div>'
        f'<div class="tl-fila">{"".join(cels)}</div>'
        f'<div class="tl-fila tl-fila-ceo">{"".join(noms)}</div>'
        "</div></div>"
        f'<ol class="trams" aria-label="CEO per períodes">{"".join(llista)}</ol>'
    )


def cel_prova(estat: str, any_: int, base: bool = False) -> str:
    if estat == "V":
        return f'<a class="pv pv-v" href="#proves" data-filtre-any="{any_}" title="Hi ha almenys una prova [V] al registre per a {any_}"><span aria-hidden="true">✓</span> Sí</a>'
    if estat == "NV":
        return f'<a class="pv pv-nv" href="#proves" data-filtre-any="{any_}" title="Només hi ha proves [NV] al registre per a {any_}">Només [NV]</a>'
    if base:
        return f'<a class="pv pv-base" href="#proves" data-filtre-any="{any_}" title="Cita als camps de la base, no al registre">Base</a>'
    return '<span class="pv pv-no">No consta</span>'


def taula_anys(e: dict) -> str:
    files = []
    for f in e["files"]:
        if f["ceos"]:
            ceo = "<br>".join(esc(c) for c in f["ceos"])
            if len(f["ceos"]) > 1:
                ceo += f' <span class="mini">({len(f["ceos"])} CEO)</span>'
        else:
            ceo = '<span class="buit">Sense CEO</span>'
        if f["aplicat"]:
            ceo += (f'<span class="aplicat">CEO aplicat (columna de simulació): {esc(f["aplicat"])}. '
                    "No substitueix <code>ceos</code>.</span>")
        cert = CERTIFICACIO.get(f["cert"], f["cert"])
        nivell = esc(f["nivell"]) if f["nivell"] else '<span class="buit">—</span>'
        files.append(
            f'<tr><th scope="row">{f["any"]}</th><td class="t-ceo" data-l="CEO">{ceo}</td>'
            f'<td data-l="FounderCEO">{badge_etiq(f["lletra"])}</td>'
            f'<td data-l="Certificació"><span class="cert cert-{esc(f["cert"])}">{esc(cert)}</span></td>'
            f'<td data-l="Nivell">{nivell}</td>'
            f'<td data-l="Prova de CEO">{cel_prova(f["prova_ceo"], f["any"])}</td>'
            f'<td data-l="Prova de classificació">{cel_prova(f["prova_fund"], f["any"], f["base_fund"])}</td></tr>'
        )
    return f"""<div class="taula-wrap"><table class="taula-anys">
<caption class="vh">Resum per any</caption>
<thead><tr><th scope="col">Any</th><th scope="col">CEO a 31/10</th><th scope="col">FounderCEO</th><th scope="col">Certificació</th><th scope="col">Nivell</th><th scope="col">Prova de CEO</th><th scope="col">Prova de classificació</th></tr></thead>
<tbody>{''.join(files)}</tbody></table></div>"""


def html_cita(text: str, ident: str) -> str:
    if not text:
        return '<p class="sense-cita">Aquesta entrada no té cita literal.</p>'
    if len(text) <= LONGITUD_MAX_CITA:
        return f'<blockquote class="cita"><p>{esc(text)}</p></blockquote>'
    tall = text[:LONGITUD_MAX_CITA]
    m = list(re.finditer(r"[.;:!?](\s|$)", tall))
    if m and m[-1].end() > LONGITUD_MAX_CITA * 0.5:
        tall = tall[: m[-1].end()].rstrip()
    else:
        tall = tall.rsplit(" ", 1)[0]
    return (
        f'<blockquote class="cita"><p>{esc(tall)} […]</p></blockquote>'
        f'<p class="mini">Fragment: la cita completa té {fmt_int(len(text))} caràcters i és a '
        f"<code>docs/REGISTRE_CANVIS.csv</code> amb l'identificador <code>{esc(ident)}</code>.</p>"
    )


def meta(dt: str, dd: str) -> str:
    return f"<div><dt>{esc(dt)}</dt><dd>{dd}</dd></div>"


def llista_valors(valors: list[str], codi: bool = True) -> str:
    if not valors:
        return '<span class="buit">—</span>'
    if codi:
        return " ".join(f"<code>{esc(v)}</code>" for v in valors)
    return "; ".join(esc(v) for v in valors)


def anys_html(p: dict) -> str:
    txt = comprimeix_anys(p["anys"]) if p["anys"] else "; ".join(p.get("anys_text", [])) or "—"
    extra = ""
    if p.get("anys_fora"):
        extra = f' <span class="mini">(fora del panell d\'aquest ISIN: {esc(comprimeix_anys(p["anys_fora"]))})</span>'
    return f'<span class="p-anys" title="Anys que cobreix">{esc(txt)}</span>{extra}'


def html_prova(p: dict) -> str:
    anys_attr = " ".join(str(a) for a in p["anys"])
    funcions = [FUNCIONS.get(f, f) for f in p["funcio"]] or ["(buida)"]
    if p["ocult"]:
        return (
            f'<article class="prova prova-oculta" id="{p["ancora"]}" data-anys="{anys_attr}">'
            f'<header class="p-cap"><span class="b b-gris">No mostrada</span><code>{esc(p["id"])}</code>'
            f'<span class="mini">{esc(", ".join(funcions))}</span>{anys_html(p)}</header>'
            + ("<p>Prova de la classificació sectorial: el sector no es mostra en aquesta versió, pendent d'aclarir-ne la "
               "llicència. L'entrada consta al registre.</p></article>" if p["ocult"] == "sector" else
               "<p>La cita o l'URL contenen un terme de la llista restringida (columnes o documents "
               "interns). Criteri de la part pública; l'entrada consta al registre.</p></article>")
        )
    badges = []
    if "[V]" in p["veritat"]:
        badges.append('<span class="b b-v" title="marca_veritat = [V]">[V] Verificada</span>')
    if "[NV]" in p["veritat"]:
        badges.append('<span class="b b-nv" title="marca_veritat = [NV]">[NV] No verificada</span>')
    if p["no_valida"]:
        badges.append('<span class="b b-mal" title="La nota de l\'entrada diu no_valida">Font no vàlida</span>')
    if p["pendent_df"]:
        badges.append('<span class="b b-nv" title="La nota de l\'entrada diu pendent_DF">Pendent de DF</span>')
    curtes = [m for m in p["marca_prova"] if len(m) <= 14]
    llargues = [m for m in p["marca_prova"] if len(m) > 14]
    for m in curtes:
        badges.append(f'<span class="b b-marca" title="marca_prova">{esc(m)}</span>')
    for o, ocult in p["origen_pub"]:
        if not ocult and re.fullmatch(r"Nivell [ABC]", o):
            badges.append(f'<span class="b b-nivell" title="origen_cita">Font {esc(o[-1])}</span>')

    # Fonts
    url = url_segura(p["url"])
    fonts = []
    if url:
        fonts.append(f'<span class="domini">{esc(domini(url))}</span>')
        fonts.append(enllac_ext(url, "Font original", "boto"))
    elif p["url"]:
        fonts.append(f'<span class="domini">URL no vàlida: {esc(p["url"])}</span>')
    else:
        fonts.append('<span class="domini buit">Sense URL de la font</span>')
    if p["wb_urls"]:
        for u in p["wb_urls"]:
            d = data_wayback(ts_de_url_wayback(u))
            fonts.append(enllac_ext(u, "Còpia Wayback" + (f" · {d}" if d else ""), "boto boto-wb"))
    elif p["wb_extra"]:
        d = data_wayback(p["wb_extra"]["timestamp"] or ts_de_url_wayback(p["wb_extra"]["url"]))
        fonts.append(enllac_ext(p["wb_extra"]["url"], "Còpia Wayback (fitxer extra)" + (f" · {d}" if d else ""), "boto boto-wb"))
    elif p["wb_pendent"]:
        fonts.append('<span class="boto boto-off">Wayback: pendent de verificació externa</span>')
    else:
        fonts.append('<span class="boto boto-off">Wayback: no consta</span>')

    # Metadades
    m = []
    m.append(meta("Funció (funcio_cita)", llista_valors(p["funcio"]) if p["funcio"] else
                  f'<span class="buit">buida</span> · agrupada pel tipus {llista_valors(p["tipus"])}'))
    m.append(meta("Tipus d'entrada", llista_valors(p["tipus"])))
    if p["marca_prova"]:
        if llargues:
            items = "".join(f"<li><code>{esc(x)}</code></li>" for v in llargues for x in v.split(";") if x.strip())
            m.append(meta("Marca de prova", (llista_valors(curtes) + " " if curtes else "") + f'<ul class="llista-codi">{items}</ul>'))
        else:
            m.append(meta("Marca de prova", llista_valors(curtes)))
    m.append(meta("Marca de veritat", llista_valors(p["veritat"])))
    m.append(meta("Allotjament", llista_valors(p["allotjament"])))
    orig = []
    for o, ocult in p["origen_pub"]:
        orig.append('<span class="buit">valor no mostrat (criteri de la part pública)</span>' if ocult else f"<code>{esc(o)}</code>")
    m.append(meta("Origen de la cita", " ".join(orig) if orig else '<span class="buit">—</span>'))
    m.append(meta("Identificador", f'<code>{esc(p["id"])}</code>'))
    if p["marques"]:
        m.append(meta("Marques de fundador", llista_valors(p["marques"])))
    estat = [f'{esc(ESTAT_WAYBACK.get(s, s))} <code>{esc(s)}</code>' for s in p["wb_estat"]]
    ts = [data_wayback(t) or t for t in p["wb_ts"]]
    wb_txt = "; ".join(estat) if estat else '<span class="buit">no consta</span>'
    if ts:
        wb_txt += " · captura " + ", ".join(esc(t) for t in ts)
    m.append(meta("Estat Wayback", wb_txt))
    capt = {"si": "sí", "no": "no"}
    m.append(meta("Cita verificada a la captura",
                  ", ".join(esc(capt.get(c, c)) for c in p["capt"]) if p["capt"] else '<span class="buit">no consta</span>'))

    notes = []
    for n, motiu in p["notes_pub"]:
        if motiu:
            notes.append('<p class="nota-oculta">Nota no mostrada: conté noms de models o referències internes '
                         "(criteri de la part pública).</p>")
        elif len(n) > LONGITUD_NOTA_PLEGADA:
            notes.append(f'<details class="nota-llarga"><summary>{esc(n[:280].rsplit(" ", 1)[0])}… '
                         f'<span class="mini">(mostra la nota completa, {fmt_int(len(n))} caràcters)</span></summary>'
                         f"<p>{esc(n)}</p></details>")
        else:
            notes.append(f"<p>{esc(n)}</p>")
    notes_html = f'<div class="p-notes"><h4>Notes</h4>{"".join(notes)}</div>' if notes else ""

    cls = "prova"
    if "[V]" not in p["veritat"]:
        cls += " prova-nv"
    if p["no_valida"]:
        cls += " prova-mal"
    return f"""<article class="{cls}" id="{p["ancora"]}" data-anys="{anys_attr}">
<header class="p-cap">{''.join(badges)}{anys_html(p)}</header>
{html_cita(p["cita"], p["id"])}
<div class="p-fonts">{''.join(fonts)}</div>
<dl class="p-meta">{''.join(m)}</dl>
{notes_html}
</article>"""


def html_cita_base(d: dict, idx: int) -> str:
    anys_attr = " ".join(str(a) for a in d["anys"])
    rang = esc(comprimeix_anys(d["anys"]))
    origen = "base (font_classificacio)" if d["tipus"] == "font_classificacio" else "base (d37)"
    if d["ocult"]:
        return (f'<article class="prova prova-oculta" id="b-{idx}" data-anys="{anys_attr}"><header class="p-cap">'
                f'<span class="b b-gris">No mostrada</span><span class="p-anys">{rang}</span></header>'
                f"<p>Cita de la {esc(origen)} no mostrada (terme de la llista restringida).</p></article>")
    if d["tipus"] == "font_classificacio":
        cita = html_cita(d["cita"], f"font_classificacio_cita ({rang})")
    elif d["cita"] and d["cita"].lower() in {"si", "no", "si_cita_alternativa"}:
        cita = (f'<p class="sense-cita">El CSV no conté text literal d\'aquesta cita. Indicador '
                f'<code>d37_cita_contemporania</code> = <code>{esc(d["cita"])}</code>.</p>')
    else:
        cita = html_cita(d["cita"], f"d37_cita_contemporania ({rang})")
    url = url_segura(d["url"])
    fonts = []
    if url:
        fonts.append(f'<span class="domini">{esc(domini(url))}</span>')
        fonts.append(enllac_ext(url, "Font original", "boto"))
    else:
        fonts.append('<span class="domini buit">Sense URL de la font</span>')
    fonts.append('<span class="boto boto-off">Wayback: no consta en aquest camp de la base</span>')
    m = [meta("Origen", f"<code>{esc(origen)}</code>")]
    if d["tipus"] == "d37" and d["dada"]:
        m.append(meta("Data de la cita (d37_cita_contemp_data)", esc(d["dada"])))
    if d["tipus"] == "font_classificacio":
        if d["ids_registre"]:
            m.append(meta("Registre", "La mateixa cita i URL també consten al registre: " + llista_valors(d["ids_registre"])))
        else:
            m.append(meta("Registre", "No consta al registre amb el mateix text i URL."))
    return f"""<article class="prova prova-base" id="b-{idx}" data-anys="{anys_attr}">
<header class="p-cap"><span class="b b-base">Cita de la base</span><span class="p-anys" title="Anys en què el camp té aquest valor">{rang}</span></header>
{cita}
<div class="p-fonts">{''.join(fonts)}</div>
<dl class="p-meta">{''.join(m)}</dl>
</article>"""


def pagina_fitxa(ctx: Context, e: dict, anterior: dict | None, seguent: dict | None) -> str:
    r = e["recompte"]
    anys_txt = comprimeix_anys(e["anys"])
    chips = [
        f'<span class="chip"><span class="chip-k">ISIN</span><code>{esc(e["isin"])}</code></span>',
        f'<span class="chip" title="Derivat del prefix de l\'ISIN; no és la seu social ni un camp de la base">'
        f'<span class="chip-k">País d\'emissió de l\'ISIN</span>{esc(e["pais"])} <small>(derivat)</small></span>',
        f'<span class="chip"><span class="chip-k">Anys al panell</span>{esc(anys_txt)} · {len(e["anys"])}</span>',
    ]
    if MOSTRA_SECTOR:
        sec = e["supersector"] or "sense sector"
        estats = [s for s in e["estats_sector"] if s != "amb_sector"]
        extra = f' <small>({esc(", ".join(estats))})</small>' if estats else ""
        chips.append(f'<span class="chip"><span class="chip-k">Supersector</span>{esc(sec)}{extra}</span>')
    resum_etq = "".join(
        f'<span class="kp e-{l}-suau"><span class="cel cel-p e-{l}" aria-hidden="true">{l}</span><b>{r[l]}</b> {"any" if r[l] == 1 else "anys"}</span>'
        for l in ORDRE_ETIQ if r[l]
    )
    altres = ""
    if e["altres_noms"]:
        altres = f'<p class="altres-noms">Altres noms al panell: {"; ".join(esc(n) for n in e["altres_noms"])}</p>'

    # Proves agrupades
    grups = {"ceo": [], "fundador": [], "altres": []}
    for p in e["proves"]:
        grups[p["grup"]].append(html_prova(p))
    for i, d in enumerate(e["cites_base"], start=1):
        grups["fundador"].append(html_cita_base(d, i))
    titols = {
        "ceo": ("CEO", "Qui era el CEO a 31/10: nomenaments, informes anuals, intervals (ceo_interval)."),
        "fundador": ("Fundador o classificació", "Proves de l'etiqueta FounderCEO (D37, a–e…) i cites dels camps de classificació de la base."),
        "altres": ("Altres: context, datació i revisió", "Entrades de context, datació de mandats, revisió de fonts i dubtes metodològics."),
    }
    n_total = len(e["proves"]) + len(e["cites_base"])
    anys_amb = sorted({a for p in e["proves"] for a in p["anys"]} | {a for d in e["cites_base"] for a in d["anys"]})
    if n_total:
        chips_any = "".join(f'<button type="button" class="xip" data-filtre-any="{a}" aria-pressed="false">{a}</button>' for a in anys_amb)
        filtre = (f'<div class="filtre-anys" role="group" aria-label="Filtra les proves per any">'
                  f'<button type="button" class="xip" data-filtre-any="" aria-pressed="true">Tots els anys</button>{chips_any}</div>'
                  '<p class="recompte-proves" aria-live="polite" id="estat-filtre"></p>')
        seccions = []
        for clau in ("ceo", "fundador", "altres"):
            if not grups[clau]:
                continue
            t, desc = titols[clau]
            seccions.append(
                f'<section class="grup-proves" id="g-{clau}"><h3>{esc(t)} <span class="n">{len(grups[clau])}</span></h3>'
                f'<p class="nota">{esc(desc)}</p>{"".join(grups[clau])}</section>'
            )
        n_reg = len(e["proves"])
        n_base = len(e["cites_base"])
        intro = (f'<p class="nota">{fmt_int(n_reg)} {"entrada" if n_reg == 1 else "entrades"} de <code>docs/REGISTRE_CANVIS.csv</code>'
                 f'{" i " + fmt_int(n_base) + (" cita" if n_base == 1 else " cites") + " dels camps de la base" if n_base else ""}. '
                 "Cada prova es mostra una vegada, amb els anys que cobreix. Les proves [NV] es mostren marcades.</p>")
        proves_html = intro + filtre + "".join(seccions)
    else:
        proves_html = ('<div class="sense-proves"><p><strong>No hi ha cita estructurada en aquests fitxers d\'origen</strong> '
                       "(<code>docs/REGISTRE_CANVIS.csv</code> ni camps <code>font_classificacio_*</code> / <code>d37_*</code> de la base). "
                       "L'etiqueta FounderCEO i el CEO de la base es mostren igualment al resum.</p></div>")
        if e["rastre"]:
            items = "".join(
                f'<li>{enllac_ext(d["url"], d["url"], "url-llarga")} <span class="mini">({esc(comprimeix_anys(d["anys"]))})</span></li>'
                for d in e["rastre"]
            )
            proves_html += (
                '<details class="rastre"><summary>Rastre secundari: URL d\'arxiu heretades, sense cita literal estructurada '
                f'<span class="mini">({len(e["rastre"])})</span></summary>'
                "<p class=\"nota\">Columna <code>v75_urls_arxivades</code> de la base. No és una prova tancada: no hi ha cita literal "
                "estructurada i no s'ha verificat aquí.</p>"
                f'<ul class="llista-urls">{items}</ul></details>'
            )

    navegacio = ['<nav class="nav-fitxes" aria-label="Altres empreses">']
    if anterior:
        navegacio.append(f'<a class="ant" href="{esc(anterior["isin"])}.html"><small>← Anterior</small>{esc(anterior["nom"])}</a>')
    else:
        navegacio.append("<span></span>")
    if seguent:
        navegacio.append(f'<a class="seg" href="{esc(seguent["isin"])}.html"><small>Següent →</small>{esc(seguent["nom"])}</a>')
    navegacio.append("</nav>")

    llegenda_tl = "".join(
        f'<span class="ll"><span class="cel cel-p e-{l}" aria-hidden="true">{l}</span>{esc(n)}</span>'
        for l, n in (("F", "fundador-CEO"), ("P", "professional"), ("ND", "no determinat"), ("NA", "sense CEO"))
    ) + '<span class="ll"><span class="cel cel-p cel-buida" aria-hidden="true"></span>no és al panell</span>'

    cos = f"""<p class="molla"><a href="../index.html">← Totes les empreses</a></p>
{avis(ctx)}
<section class="fitxa-cap">
<p class="eyebrow">Fitxa d'empresa</p>
<h1>{esc(e["nom"])}</h1>
<div class="chips">{''.join(chips)}</div>
{altres}
<div class="kp-fila">{resum_etq}<span class="kp kp-proves"><b>{fmt_int(n_total)}</b> {"prova" if n_total == 1 else "proves"}</span></div>
<nav class="salts" aria-label="Seccions de la fitxa"><a href="#resum">Resum</a><a href="#proves">Proves</a></nav>
</section>
<section class="seccio" id="resum" aria-labelledby="h-resum">
<h2 id="h-resum">Resum</h2>
<h3 class="h-sub">CEO a 31 d'octubre de cada any</h3>
{linia_temps(e)}
<div class="llegenda">{llegenda_tl}</div>
{taula_anys(e)}
<p class="nota">CEO: columna <code>ceos</code> de la base. «Prova de CEO» i «Prova de classificació» indiquen si hi ha entrades al registre amb <code>funcio_cita</code> = <code>ceo</code> o <code>fundador</code> que cobreixen l'any; «Base» vol dir que la cita només és als camps de la base. Fes clic per veure les proves d'aquell any. Si <code>FounderCEO</code> = 1, el CEO d'aquell any està classificat com a fundador; això no és una llista dels fundadors de l'empresa.</p>
</section>
<section class="seccio" id="proves" aria-labelledby="h-proves">
<h2 id="h-proves">Proves</h2>
{proves_html}
</section>
{''.join(navegacio)}"""
    return pagina(ctx, titol=f"{e['nom']} · {e['isin']} · Dashboard Fundadors",
                  descripcio=f"Fitxa de {e['nom']} ({e['isin']}): CEO per any, FounderCEO i proves amb cita i font.",
                  cos=cos, prefix="../", actiu="", scripts=("fitxa.js",))


# ---------------------------------------------------------------------------
# Metodologia i llegenda
# ---------------------------------------------------------------------------


def pagina_metodologia(ctx: Context, resum: dict, stats: Counter) -> str:
    gh = f"{REPO_GITHUB}/blob/main"
    docs = [
        ("docs/METODOLOGIA.md", "Porta d'entrada a la metodologia vigent (v0.10.10), amb el text complet."),
        ("AGENTS.md", "Instruccions de treball i annex normatiu (regles 25 a 29, METODOLOGIA v0.10.10)."),
        ("docs/LIMITACIONS.md", "Limitacions declarades de la base."),
        ("docs/DICCIONARI_CAMPS.md", "Diccionari de camps de la base."),
    ]
    docs_html = "".join(
        f'<li>{enllac_ext(f"{gh}/{d}", d)} — {esc(t)}</li>' for d, t in docs
    )
    etiq = "".join(
        f'<div class="def">{badge_etiq(l)}<p>{t}</p></div>'
        for l, t in (
            ("F", "Valor <code>1</code>. El CEO de l'empresa a 31/10 d'aquell any és fundador o cofundador de l'empresa cotitzada o d'una entitat rellevant (per exemple, una predecessora documentada), segons les regles de la metodologia (D37, cita directa, fundador transformador)."),
            ("P", "Valor <code>0</code>. El CEO no és fundador. Cal una prova positiva amb cita (proves a–e); si no n'hi ha, no es posa 0."),
            ("ND", "Valor <code>no_determinat</code>. Hi ha un CEO identificat però cap prova concloent de sí ni de no, o les proves es contradiuen."),
            ("NA", "Valor <code>NA_sense_ceo</code>. Un cop aplicades les regles R1-R3, a 31/10 no hi ha cap CEO individual (R-SC)."),
        )
    )
    cert = "".join(
        f"<div class='def'><span class='cert cert-{c}'>{esc(CERTIFICACIO[c])}</span><p>{t}</p></div>"
        for c, t in (
            ("certificada", "L'etiqueta està certificada dins de l'auditoria. El nivell diu com: <b>N1</b> (les dues revisions independents de l'auditoria coincideixen amb la base, amb cita A/B i sense incidències E2, E4 ni E6), <b>N2</b> (una revisió coincideix amb la base i l'altra ho deixa indeterminat, sense incidència greu) o <b>doctorat</b> (certificada per decisió de Doctorat)."),
            ("certificada_ceo_pendent", "L'etiqueta és certificable, però la identitat del CEO encara no està verificada. Pot portar nivell N1 o N2."),
            ("no_certificada", "La fila és dins de l'àmbit de l'auditoria però no s'ha pogut certificar."),
            ("fora_mostra_auditoria", "La fila no formava part de la mostra de l'auditoria. Es revisa per lots; aquest estat no vol dir que l'etiqueta sigui dubtosa."),
        )
    )
    marques_ceo = [
        ("R1", "Títol de CEO o càrrec legal equivalent (Vorstandsvorsitzender, consejero delegado, PDG, directeur général…)."),
        ("R2", "CEO interí."),
        ("R2b", "Direcció col·legiada transitòria."),
        ("R3", "Persona descrita literalment com a primer executiu quan el càrrec de CEO és vacant (el president executiu, només per aquesta via)."),
        ("ceo_interval", "Interval: un document de nomenament amb data igual o anterior al 31/10 i un altre que anomena la persona CEO en una data igual o posterior. A les notes, «inici» o «final»."),
    ]
    marques_f = [
        ("D37", "Cita de l'emissor que anomena la persona fundadora o cofundadora de la cotitzada, del grup o d'una predecessora documentada."),
        ("a", "Llista tancada de fundadors en què el CEO no hi és."),
        ("b", "Edat: l'any de la fundació rellevant més recent, el CEO tenia menys de 18 anys."),
        ("c", "64 anys o més entre la fundació rellevant i l'inici del mandat, només si no hi ha dada d'edat."),
        ("d", "Incorporació tardana: el CEO entra 3 anys o més després de la fundació, amb cita de l'ocupador anterior."),
        ("e", "Origen no personal: l'entitat la va crear l'Estat o una altra empresa, sense persona fundadora."),
    ]
    def taula_marques(llista):
        return "".join(f"<div class='def'><code class='b b-marca'>{esc(k)}</code><p>{esc(t)}</p></div>" for k, t in llista)
    ocults = (
        f"<li>Proves del registre no mostrades perquè la cita o l'URL contenen un terme restringit: <b>{fmt_int(stats['proves_ocultes_terme_restringit'])}</b>.</li>"
        f"<li>Notes no mostrades per termes restringits o referències internes: <b>{fmt_int(stats['notes_ocultes_terme_restringit'])}</b>; per noms de models: <b>{fmt_int(stats['notes_ocultes_nom_model'])}</b>.</li>"
        f"<li>Proves de la classificació sectorial no mostrades (sector desactivat): <b>{fmt_int(stats['proves_ocultes_sector'])}</b>.</li>"
        f"<li>Valors d'«origen de la cita» no mostrats: <b>{fmt_int(stats['origen_cita_ocult'])}</b>.</li>"
        f"<li>URL del rastre secundari no mostrades: <b>{fmt_int(stats['v75_urls_ocultes_terme_restringit'])}</b>.</li>"
    )
    cos = f"""<p class="molla"><a href="index.html">← Totes les empreses</a></p>
<section class="heroi heroi-petit">
<p class="eyebrow">Metodologia i llegenda</p>
<h1>Com es llegeix aquest dashboard</h1>
<p class="entradeta">Explicació en llenguatge planer de les etiquetes que surten a les dades. La metodologia que mana és la del repositori; aquest resum no la substitueix.</p>
</section>
{avis(ctx)}
<div class="text-llarg">
<section class="seccio"><h2>La metodologia que mana</h2>
<p>La metodologia vigent és la del repositori: les instruccions de treball del repositori (<code>AGENTS.md</code>, que incorpora les regles 25 a 29 i cita la METODOLOGIA v0.10.10) i els documents als quals remeten. El text complet de la metodologia vigent (v0.10.10) és a <code>docs/METODOLOGIA_3_Articles_v0.10.10.md</code>. Si aquesta pàgina i aquests documents diuen coses diferents, manen els documents.</p>
<ul class="docs">{docs_html}</ul>
</section>
<section class="seccio"><h2>La unitat: empresa i any</h2>
<p>Cada fila de la base és un ISIN i un any (2016–2025). La base té {fmt_int(resum["n_files"])} files i {fmt_int(resum["n_isin"])} ISIN. Per a cada fila hi ha el CEO i l'etiqueta FounderCEO.</p>
<p><b>Data de referència del CEO: el 31 d'octubre de cada any.</b> El CEO de l'any t és qui ocupava el càrrec el 31/10/t. Aquesta data no es canvia.</p>
</section>
<section class="seccio"><h2>Etiqueta FounderCEO</h2>{etiq}
<p class="nota">Recompte actual: F {fmt_int(resum["rec"]["F"])}, P {fmt_int(resum["rec"]["P"])}, ND {fmt_int(resum["rec"]["ND"])}, NA {fmt_int(resum["rec"]["NA"])}.</p></section>
<section class="seccio"><h2>Estat de certificació i nivell</h2>{cert}</section>
<section class="seccio"><h2>Nivells de font</h2>
<div class="def"><span class="b b-nivell">Font A</span><p>Documents de la mateixa empresa o registres oficials: informe anual, fullet o document d'IPO, comunicat, pàgina oficial, document presentat a un regulador o a la borsa.</p></div>
<div class="def"><span class="b b-nivell">Font B</span><p>Tercers fiables: premsa econòmica de qualitat, obres de referència, llibres, articles acadèmics.</p></div>
<div class="def"><span class="b b-gris">Font C</span><p>Agregadors, blogs, enciclopèdies obertes, LinkedIn… Serveixen de pista, però una font C mai no verifica.</p></div>
<p class="nota">El nivell no té columna pròpia al registre. Quan consta, és al camp «origen de la cita» (<code>Nivell A</code>, <code>Nivell B</code>) o al text de les notes; el dashboard el mostra tal com és.</p>
</section>
<section class="seccio"><h2>Marques de prova</h2>
<h3>Per al CEO</h3>{taula_marques(marques_ceo)}
<h3>Per a l'etiqueta de fundador</h3>{taula_marques(marques_f)}
<p class="nota">Algunes entrades d'auditoria porten marques més llargues (per exemple <code>2016=informe_exercici:confirmada</code>); es mostren tal com són al registre.</p>
</section>
<section class="seccio"><h2>Estat d'una prova</h2>
<div class="def"><span class="b b-v">[V] Verificada</span><p>Qui va fer l'entrada va obrir el document sencer i hi va trobar la cita literalment. Fins que DF ho confirma per script, és provisional.</p></div>
<div class="def"><span class="b b-nv">[NV] No verificada</span><p>No s'ha pogut obrir el document sencer (bloqueig, descàrrega tallada…: a les notes, <code>pendent_DF</code>) o la cita no hi és (<code>no_valida</code>). Un error d'accés no vol dir que la font sigui dolenta.</p></div>
<div class="def"><span class="b b-mal">Font no vàlida</span><p>Distintiu que surt quan la nota de l'entrada diu <code>no_valida</code>: la cita no és al document, és d'un altre any o la font és C.</p></div>
<div class="def"><span class="b b-base">Cita de la base</span><p>Cita que només consta als camps <code>font_classificacio_cita</code> / <code>font_classificacio_url</code> o <code>d37_*</code> del CSV de la base. Només cobreix els anys en què el camp té valor.</p></div>
</section>
<section class="seccio"><h2>Fonts i còpies arxivades</h2>
<p><b>Font original</b>: l'URL del document on hi ha la cita. <b>Còpia Wayback</b>: la captura d'archive.org que consta al registre. Si no n'hi ha, es diu «no consta» (sense còpia arxivada, el document es considera no durable); si està pendent, «pendent de verificació externa». El dashboard no consulta ni completa cap captura.</p>
<p><b>Cita verificada a la captura</b>: <code>si</code> si DF ha comprovat la cita al document arxivat; <code>no</code> si no s'ha pogut comprovar.</p>
<p><b>Allotjament</b>: on és el document segons el registre (<code>emissor</code>, <code>regulador</code>, <code>grup</code>, <code>successor</code>, <code>plataforma</code>, <code>mitja</code>…). Es mostra tal com consta.</p>
</section>
<section class="seccio"><h2>Què no hi ha (i no s'inventa)</h2>
<ul>
<li><b>Fundadors de l'empresa.</b> La base no té cap camp amb els noms dels fundadors. Si una fila és F, el CEO d'aquell any està classificat com a fundador; no és una llista completa de fundadors.</li>
<li><b>Any de fundació.</b> No és un camp. Si apareix, és dins del text d'una cita o d'una nota.</li>
<li><b>País.</b> La base no té país. El filtre «país d'emissió de l'ISIN» es deriva del prefix de l'ISIN i no és la seu social.</li>
<li><b>Sector.</b> No es mostra en aquesta versió, pendent d'aclarir la llicència de la classificació.</li>
<li><b>Títol, data i pàgina del document.</b> No tenen columna pròpia; quan l'autor de l'entrada els va escriure, són a les notes.</li>
</ul>
</section>
<section class="seccio"><h2>Criteris de la part pública</h2>
<p>No es mostren les columnes de robustesa, les propostes brutes ni les notes de decisió de l'auditoria, ni referències a fitxers o informes interns. Quan una nota del registre conté noms de models o referències internes, es mostra un avís en lloc de la nota. Les cites es mostren tal com les publica l'emissor, incloses les dates de naixement que serveixen per a la prova b. Les cites llargues es retallen a un fragment, amb l'avís corresponent.</p>
<ul>{ocults}</ul>
</section>
<section class="seccio"><h2>Fitxers llegits</h2>
<div class="taula-wrap"><table class="taula-simple">
<thead><tr><th>Fitxer</th><th>SHA-256</th></tr></thead>
<tbody>
<tr><td><code>dades/base_isin_any_v8r3.csv</code></td><td><code class="sha">{esc(ctx.sha_base)}</code></td></tr>
<tr><td><code>docs/REGISTRE_CANVIS.csv</code></td><td><code class="sha">{esc(ctx.sha_registre)}</code></td></tr>
</tbody></table></div>
<p class="nota">Commit de referència de <code>main</code>: <code>{esc(ctx.commit)}</code>. Els SHA es comproven contra <code>MANIFEST_SHA256.csv</code> cada vegada que es genera el lloc.</p>
</section>
</div>"""
    return pagina(ctx, titol="Metodologia i llegenda · Dashboard Fundadors",
                  descripcio="Com es llegeixen les etiquetes F, P, ND, NA, la certificació i les proves del dashboard.",
                  cos=cos, prefix="", actiu="metodologia")


# ---------------------------------------------------------------------------
# Escriptura
# ---------------------------------------------------------------------------


def escriu(path: Path, text: str) -> None:
    path = path.resolve()
    path.relative_to(SORTIDA.resolve())  # només dins de dashboard/
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main() -> int:
    ap = argparse.ArgumentParser(description="Genera el dashboard estàtic a dashboard/.")
    ap.add_argument("--sha-esperat", help="SHA-256 que ha de tenir dades/base_isin_any_v8r3.csv (opcional).")
    ap.add_argument("--commit", help="Commit de referència a mostrar (per defecte, merge-base amb main).")
    args = ap.parse_args()

    shas = comprova_integritat(args.sha_esperat)
    commit, data_commit = commit_referencia(args.commit)
    ctx = Context(commit, data_commit, shas)
    stats: Counter = Counter()
    model = carrega_model(stats)
    resum = calcula_resum(model)

    escriu(SORTIDA / "assets" / "style.css", CSS)
    escriu(SORTIDA / "assets" / "cerca.js", JS_CERCA)
    escriu(SORTIDA / "assets" / "fitxa.js", JS_FITXA)
    escriu(SORTIDA / "index.html", pagina_inici(ctx, model, resum))
    escriu(SORTIDA / "metodologia.html", pagina_metodologia(ctx, resum, stats))

    ordenades = sorted(model["empreses"].values(), key=lambda e: (clau_ordre(e["nom"]), e["isin"]))
    dir_emp = SORTIDA / "empreses"
    for i, e in enumerate(ordenades):
        ant = ordenades[i - 1] if i > 0 else None
        seg = ordenades[i + 1] if i + 1 < len(ordenades) else None
        escriu(dir_emp / f"{e['isin']}.html", pagina_fitxa(ctx, e, ant, seg))
    actuals = {e["isin"] for e in ordenades}
    for f in sorted(dir_emp.glob("*.html")):
        if f.stem not in actuals:
            f.unlink()
            stats["fitxes_antigues_esborrades"] += 1

    rec = resum["rec"]
    print(f"Commit de referència: {commit} {data_commit}")
    for rel, h in shas.items():
        print(f"SHA-256 {rel}: {h} (coincideix amb el manifest)")
    print(f"ISIN: {resum['n_isin']} · files: {resum['n_files']} · F {rec['F']} · P {rec['P']} · ND {rec['ND']} · NA {rec['NA']}")
    print(f"Empreses amb almenys una entrada al registre: {resum['amb_registre']}")
    print(f"Empreses sense cita estructurada (avís a la fitxa): {resum['sense_cita']}")
    print(f"Files amb prova de CEO al registre: {resum['files_ceo']} · amb prova de classificació: {resum['files_fund']} · sense cap cita estructurada: {resum['files_sense_cita']}")
    for k in sorted(stats):
        print(f"{k}: {stats[k]}")
    print(f"Fitxes escrites: {len(ordenades)}")
    return 0


# ---------------------------------------------------------------------------
# Actius estàtics (CSS i JS), sense dependències externes
# ---------------------------------------------------------------------------

CSS = r"""/* Dashboard Fundadors. Generat per dashboard/genera_dashboard.py; no l'editis a mà. */
:root {
  color-scheme: light;
  --fons: #f5f4f0;
  --sup: #ffffff;
  --sup-2: #f0efea;
  --sup-3: #e7e5df;
  --tinta: #1a1a19;
  --tinta-2: #4b4a46;
  --tinta-3: #6e6d68;
  --linia: #e0ded7;
  --linia-forta: #c9c7bf;
  --enllac: #1c5cab;
  --enllac-hover: #104281;
  --focus: #2a78d6;
  --e-F: #eb6834;
  --e-P: #2a78d6;
  --e-ND: #1baf7a;
  --e-NA: #8a8983;
  --e-F-txt: #ffffff;
  --e-P-txt: #ffffff;
  --e-ND-txt: #0b2a1f;
  --e-NA-txt: #ffffff;
  --e-F-suau: #fdeee6;
  --e-P-suau: #e8f1fc;
  --e-ND-suau: #e3f6ee;
  --e-NA-suau: #efeeeb;
  --v: #12692c;
  --v-fons: #e5f3e8;
  --nv: #8a5300;
  --nv-fons: #fdf1d8;
  --mal: #b42318;
  --mal-fons: #fde8e6;
  --base: #5b4bc4;
  --base-fons: #eeecfb;
  --avis: #7a4b00;
  --avis-fons: #fff6e0;
  --avis-vora: #f1c75b;
  --cita-fons: #fbfaf7;
  --ombra: 0 1px 2px rgba(20, 20, 18, .05), 0 2px 8px rgba(20, 20, 18, .05);
  --radi: 12px;
  --radi-petit: 8px;
  --font: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  --font-cita: Charter, "Bitstream Charter", "Iowan Old Style", "Palatino Linotype", Georgia, Cambria, "Times New Roman", serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
}
@media (prefers-color-scheme: dark) {
  :root {
    color-scheme: dark;
    --fons: #121211;
    --sup: #1a1a19;
    --sup-2: #22221f;
    --sup-3: #2c2c29;
    --tinta: #f0efec;
    --tinta-2: #c9c8c0;
    --tinta-3: #9c9b93;
    --linia: #33332f;
    --linia-forta: #4a4a45;
    --enllac: #86b6ef;
    --enllac-hover: #b7d3f6;
    --focus: #6da7ec;
    --e-F: #d95926;
    --e-P: #3987e5;
    --e-ND: #199e70;
    --e-NA: #6f6e68;
    --e-ND-txt: #ffffff;
    --e-F-suau: #3a2116;
    --e-P-suau: #172a42;
    --e-ND-suau: #12302a;
    --e-NA-suau: #2a2a27;
    --v: #7fd99a;
    --v-fons: #143220;
    --nv: #f2c14e;
    --nv-fons: #382a0c;
    --mal: #ff9a8f;
    --mal-fons: #3f1814;
    --base: #b3a9f2;
    --base-fons: #262145;
    --avis: #f6d58a;
    --avis-fons: #2f2510;
    --avis-vora: #7a5b16;
    --cita-fons: #20201d;
    --ombra: 0 1px 2px rgba(0, 0, 0, .3), 0 2px 10px rgba(0, 0, 0, .25);
  }
}
*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: 76px; }
body { margin: 0; background: var(--fons); color: var(--tinta); font: 16px/1.55 var(--font); }
a { color: var(--enllac); text-underline-offset: 2px; }
a:hover { color: var(--enllac-hover); }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; border-radius: 4px; }
code { font-family: var(--font-mono); font-size: .86em; background: var(--sup-2); padding: .08em .35em; border-radius: 5px; overflow-wrap: anywhere; }
h1, h2, h3, h4 { line-height: 1.2; margin: 0 0 .5em; letter-spacing: -.01em; }
h1 { font-size: clamp(1.7rem, 1.2rem + 2.2vw, 2.6rem); letter-spacing: -.02em; }
h2 { font-size: 1.45rem; }
h3 { font-size: 1.12rem; }
p { margin: 0 0 .8em; }
small { font-size: .82em; }
.vh { position: absolute !important; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
.salta { position: absolute; left: -999px; top: 8px; background: var(--sup); padding: 8px 12px; border-radius: 8px; z-index: 50; }
.salta:focus { left: 8px; }
.nota { color: var(--tinta-3); font-size: .9rem; }
.mini { color: var(--tinta-3); font-size: .8rem; font-weight: 400; }
.buit { color: var(--tinta-3); }

/* Barra superior */
.barra { position: sticky; top: 0; z-index: 20; background: color-mix(in srgb, var(--sup) 88%, transparent); backdrop-filter: saturate(1.4) blur(10px); -webkit-backdrop-filter: saturate(1.4) blur(10px); border-bottom: 1px solid var(--linia); }
.barra-in { max-width: 1240px; margin: 0 auto; padding: 10px 16px; display: flex; align-items: center; justify-content: space-between; gap: 16px; flex-wrap: wrap; }
.marca { display: flex; align-items: center; gap: 10px; color: var(--tinta); text-decoration: none; font-weight: 700; }
.marca:hover { color: var(--tinta); }
.marca-text { display: flex; flex-direction: column; line-height: 1.15; }
.marca-text small { font-weight: 500; color: var(--tinta-3); font-size: .74rem; letter-spacing: .02em; }
.marca-logo { display: grid; grid-template-columns: repeat(3, 8px); gap: 3px; }
.marca-logo i { display: block; width: 8px; height: 22px; border-radius: 3px; background: var(--e-P); }
.marca-logo i:nth-child(2) { background: var(--e-F); height: 22px; }
.marca-logo i:nth-child(3) { background: var(--e-P); opacity: .55; }
.nav { display: flex; gap: 4px; flex-wrap: wrap; }
.nav a { padding: 7px 12px; border-radius: 999px; text-decoration: none; color: var(--tinta-2); font-weight: 550; font-size: .95rem; }
.nav a:hover { background: var(--sup-2); color: var(--tinta); }
.nav a[aria-current="page"] { background: var(--tinta); color: var(--sup); }

.pagina { max-width: 1240px; margin: 0 auto; padding: 24px 16px 48px; }
.molla { margin: 0 0 14px; font-size: .95rem; }
.molla a { text-decoration: none; font-weight: 550; }

/* Capçalera de pàgina */
.heroi { padding: 14px 0 18px; }
.heroi h1 { margin-bottom: .3em; }
.heroi-petit h1 { font-size: clamp(1.5rem, 1.1rem + 1.6vw, 2.1rem); }
.eyebrow { text-transform: uppercase; letter-spacing: .09em; font-size: .76rem; font-weight: 700; color: var(--tinta-3); margin-bottom: .5em; }
.entradeta { font-size: 1.12rem; color: var(--tinta-2); max-width: 62ch; }

/* Avís */
.avis { display: flex; gap: 12px; align-items: flex-start; background: var(--avis-fons); color: var(--avis); border: 1px solid var(--avis-vora); border-radius: var(--radi); padding: 12px 16px; margin: 0 0 22px; }
.avis p { margin: 0; font-size: .93rem; }
.avis code { background: transparent; padding: 0; }
.avis-icona { flex: none; width: 22px; height: 22px; border-radius: 50%; background: var(--avis-vora); color: #3d2600; display: grid; place-items: center; font-weight: 800; font-size: .85rem; margin-top: 1px; }

/* KPI */
.kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin-bottom: 18px; }
.kpi { background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 14px 16px; box-shadow: var(--ombra); display: flex; flex-direction: column; gap: 2px; min-width: 0; }
.k-etq { display: flex; align-items: center; gap: 7px; font-size: .84rem; font-weight: 600; color: var(--tinta-2); }
.k-val { font-size: 1.9rem; font-weight: 750; letter-spacing: -.02em; font-variant-numeric: tabular-nums; line-height: 1.15; }
.k-sub { font-size: .8rem; color: var(--tinta-3); }
.kpi.k-F { border-top: 4px solid var(--e-F); }
.kpi.k-P { border-top: 4px solid var(--e-P); }
.kpi.k-ND { border-top: 4px solid var(--e-ND); }
.kpi.k-NA { border-top: 4px solid var(--e-NA); }
.punt { width: 10px; height: 10px; border-radius: 3px; display: inline-block; background: var(--e-P); }
.punt.e-F { background: var(--e-F); } .punt.e-ND { background: var(--e-ND); } .punt.e-NA { background: var(--e-NA); }

/* Panells */
.dos-panells { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 420px), 1fr)); gap: 14px; margin-bottom: 30px; align-items: start; }
.panell { background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 18px 18px 14px; box-shadow: var(--ombra); margin: 0; min-width: 0; }
.h-panell { font-size: 1.05rem; margin-bottom: .25em; }
.grafic figcaption p { margin-bottom: 10px; }
.barres { position: relative; height: 190px; margin: 6px 0 4px 30px; }
.eix { position: absolute; inset: 0 0 24px 0; pointer-events: none; }
.tick { position: absolute; left: 0; right: 0; border-top: 1px solid var(--linia); }
.tick span { position: absolute; left: -30px; top: -.6em; width: 24px; text-align: right; font-size: .72rem; color: var(--tinta-3); font-variant-numeric: tabular-nums; }
.bcols { position: absolute; inset: 0; display: flex; gap: 6px; }
.bcol { position: relative; flex: 1; min-width: 0; display: flex; flex-direction: column; outline: none; }
.barea { flex: 1; display: flex; align-items: flex-end; justify-content: center; }
.bar { display: block; width: min(30px, 70%); background: var(--e-F); border-radius: 4px 4px 0 0; min-height: 2px; transition: filter .15s; }
.bany { height: 24px; display: flex; align-items: center; justify-content: center; font-size: .74rem; color: var(--tinta-3); font-variant-numeric: tabular-nums; }
.tip { position: absolute; bottom: calc(100% - 18px); left: 50%; transform: translateX(-50%); background: var(--tinta); color: var(--sup); font-size: .78rem; padding: 6px 9px; border-radius: 7px; white-space: nowrap; pointer-events: none; display: none; z-index: 5; }
.bcol:hover .tip, .bcol:focus .tip { display: block; }
.bcol:hover .bar, .bcol:focus .bar { filter: brightness(1.12); }
.bcol:first-child .tip { left: 0; transform: none; }
.bcol:last-child .tip { left: auto; right: 0; transform: none; }
details.dades { margin-top: 8px; font-size: .88rem; }
details.dades summary { cursor: pointer; color: var(--enllac); }
.mesura { margin: 14px 0; }
.m-cap { display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap; font-size: .9rem; margin-bottom: 6px; }
.m-etq { font-weight: 600; color: var(--tinta-2); }
.m-val { color: var(--tinta-3); font-variant-numeric: tabular-nums; }
.m-val b { color: var(--tinta); }
.m-pista { height: 10px; border-radius: 999px; background: var(--sup-3); overflow: hidden; }
.m-pista span { display: block; height: 100%; background: var(--e-P); border-radius: 999px; }
.m-nota { display: block; font-size: .76rem; color: var(--tinta-3); margin-top: 4px; font-family: var(--font-mono); }

/* Cercador i taula */
.cap-seccio { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; flex-wrap: wrap; }
.recompte { color: var(--tinta-2); margin: 0; }
.recompte b { font-variant-numeric: tabular-nums; color: var(--tinta); }
.filtres { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 10px 12px; align-items: end; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 14px; margin: 12px 0 10px; box-shadow: var(--ombra); }
.camp { display: flex; flex-direction: column; gap: 4px; font-size: .82rem; font-weight: 600; color: var(--tinta-2); min-width: 0; }
.camp small { font-weight: 400; color: var(--tinta-3); }
.camp-cerca { grid-column: 1 / -1; }
.camp input, .camp select { font: inherit; font-size: 1rem; font-weight: 400; color: var(--tinta); background: var(--fons); border: 1px solid var(--linia-forta); border-radius: var(--radi-petit); padding: 9px 11px; width: 100%; min-width: 0; }
.camp input[type="search"] { padding-left: 36px; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%238a8983' stroke-width='2' stroke-linecap='round'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cpath d='m20 20-3.5-3.5'/%3E%3C/svg%3E"); background-repeat: no-repeat; background-position: 11px center; }
.boto-sec { font: inherit; font-size: .92rem; font-weight: 600; border: 1px solid var(--linia-forta); background: var(--sup); color: var(--tinta-2); border-radius: var(--radi-petit); padding: 9px 12px; cursor: pointer; }
.boto-sec:hover { background: var(--sup-2); color: var(--tinta); }
.llegenda { display: flex; flex-wrap: wrap; gap: 6px 16px; font-size: .84rem; color: var(--tinta-2); margin: 10px 0 12px; }
.ll { display: inline-flex; align-items: center; gap: 6px; }
.taula-wrap { overflow-x: auto; -webkit-overflow-scrolling: touch; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); box-shadow: var(--ombra); }
table { border-collapse: collapse; width: 100%; }
th, td { text-align: left; vertical-align: top; padding: 10px 12px; border-bottom: 1px solid var(--linia); }
thead th { position: sticky; top: 0; background: var(--sup-2); font-size: .8rem; text-transform: uppercase; letter-spacing: .04em; color: var(--tinta-2); font-weight: 700; white-space: nowrap; z-index: 1; }
tbody tr:last-child > * { border-bottom: 0; }
.num { text-align: right; font-variant-numeric: tabular-nums; }
.taula-emp thead button { font: inherit; text-transform: inherit; letter-spacing: inherit; color: inherit; background: none; border: 0; padding: 0; cursor: pointer; display: inline-flex; align-items: center; gap: 4px; }
.taula-emp thead button::after { content: "↕"; opacity: .35; font-size: .9em; }
.taula-emp thead button[aria-sort="ascending"]::after { content: "↑"; opacity: 1; }
.taula-emp thead button[aria-sort="descending"]::after { content: "↓"; opacity: 1; }
.taula-emp tbody tr:hover { background: var(--sup-2); }
.taula-emp td { vertical-align: middle; }
.c-nom { min-width: 220px; }
.c-nom a { font-weight: 650; text-decoration: none; color: var(--tinta); }
.c-nom a:hover { color: var(--enllac); text-decoration: underline; }
.sub { display: block; font-size: .78rem; color: var(--tinta-3); margin-top: 2px; }
.c-isin code { background: transparent; padding: 0; font-size: .82rem; white-space: nowrap; }
td.c-pais, td.c-anys { white-space: nowrap; font-size: .9rem; }
.c-proves .buit { font-weight: 400; }
.sense-resultat { text-align: center; padding: 30px; color: var(--tinta-3); background: var(--sup); border: 1px dashed var(--linia-forta); border-radius: var(--radi); margin-top: 12px; }

/* Cel·les d'etiqueta */
.serie { display: inline-flex; gap: 2px; }
.cel { display: inline-grid; place-items: center; width: 100%; min-width: 34px; height: 34px; border-radius: 6px; font-weight: 750; font-size: .8rem; letter-spacing: .01em; background: var(--e-P); color: var(--e-P-txt); }
.cel-p { width: 19px; min-width: 19px; height: 22px; border-radius: 4px; font-size: .62rem; }
.cel.e-F { background: var(--e-F); color: var(--e-F-txt); }
.cel.e-P { background: var(--e-P); color: var(--e-P-txt); }
.cel.e-ND { background: var(--e-ND); color: var(--e-ND-txt); }
.cel.e-NA { background: var(--e-NA); color: var(--e-NA-txt); }
.cel-buida { background: repeating-linear-gradient(135deg, var(--sup-2) 0 4px, var(--sup-3) 4px 7px); color: var(--tinta-3); border: 1px solid var(--linia); }
.etq { display: inline-flex; align-items: center; gap: 6px; white-space: nowrap; font-size: .86rem; font-weight: 600; padding: 3px 9px 3px 3px; border-radius: 999px; background: var(--e-P-suau); color: var(--tinta); }
.etq b { display: inline-grid; place-items: center; min-width: 26px; height: 22px; padding: 0 4px; border-radius: 999px; font-size: .74rem; background: var(--e-P); color: var(--e-P-txt); }
.etq.e-F { background: var(--e-F-suau); } .etq.e-F b { background: var(--e-F); color: var(--e-F-txt); }
.etq.e-ND { background: var(--e-ND-suau); } .etq.e-ND b { background: var(--e-ND); color: var(--e-ND-txt); }
.etq.e-NA { background: var(--e-NA-suau); } .etq.e-NA b { background: var(--e-NA); color: var(--e-NA-txt); }

/* Fitxa */
.fitxa-cap { background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 22px 22px 16px; box-shadow: var(--ombra); margin-bottom: 26px; }
.fitxa-cap h1 { overflow-wrap: anywhere; }
.chips { display: flex; flex-wrap: wrap; gap: 8px; margin: 4px 0 12px; }
.chip { display: inline-flex; align-items: center; gap: 8px; background: var(--sup-2); border: 1px solid var(--linia); border-radius: 999px; padding: 5px 12px; font-size: .88rem; }
.chip code { background: transparent; padding: 0; font-size: .9rem; font-weight: 600; }
.chip-k { font-size: .72rem; text-transform: uppercase; letter-spacing: .05em; color: var(--tinta-3); font-weight: 700; }
.altres-noms { font-size: .86rem; color: var(--tinta-3); }
.kp-fila { display: flex; flex-wrap: wrap; gap: 8px; margin: 6px 0 12px; }
.kp { display: inline-flex; align-items: center; gap: 7px; font-size: .9rem; padding: 4px 12px 4px 5px; border-radius: 999px; background: var(--sup-2); }
.kp b { font-variant-numeric: tabular-nums; }
.e-F-suau { background: var(--e-F-suau); } .e-P-suau { background: var(--e-P-suau); } .e-ND-suau { background: var(--e-ND-suau); } .e-NA-suau { background: var(--e-NA-suau); }
.kp-proves { padding-left: 12px; border: 1px solid var(--linia); background: transparent; }
.salts { display: flex; gap: 6px; border-top: 1px solid var(--linia); padding-top: 12px; }
.salts a { text-decoration: none; font-weight: 600; font-size: .92rem; padding: 6px 12px; border-radius: 999px; background: var(--sup-2); color: var(--tinta-2); }
.salts a:hover { color: var(--tinta); background: var(--sup-3); }
.seccio { margin-bottom: 34px; }
.seccio > h2 { padding-bottom: 8px; border-bottom: 2px solid var(--tinta); display: inline-block; margin-bottom: 14px; }
.h-sub { color: var(--tinta-2); font-size: 1rem; text-transform: uppercase; letter-spacing: .05em; margin: 4px 0 10px; }

/* Línia de temps */
.tl-wrap { overflow-x: auto; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 14px; box-shadow: var(--ombra); }
.tl { min-width: 640px; display: flex; flex-direction: column; gap: 6px; }
.tl-fila { display: grid; grid-template-columns: repeat(10, minmax(0, 1fr)); gap: 4px; }
.tl-any { text-align: center; font-size: .78rem; font-weight: 650; color: var(--tinta-3); font-variant-numeric: tabular-nums; }
.tl-cel .cel { height: 36px; font-size: .86rem; }
.tl-fila-ceo { grid-auto-rows: minmax(52px, auto); }
.tl-ceo { background: var(--sup-2); border: 1px solid var(--linia); border-left: 4px solid var(--tinta-2); border-radius: 8px; padding: 6px 9px; display: flex; flex-direction: column; justify-content: center; min-width: 0; }
.tl-ceo b { font-size: .88rem; line-height: 1.25; overflow-wrap: anywhere; }
.tl-ceo small { color: var(--tinta-3); font-variant-numeric: tabular-nums; }
.tl-ceo-buit { font-style: italic; }
.trams { display: none; list-style: none; margin: 0; padding: 0; }
.tram { display: grid; grid-template-columns: auto 1fr; gap: 2px 10px; align-items: center; background: var(--sup); border: 1px solid var(--linia); border-left: 5px solid var(--tinta-2); border-radius: var(--radi-petit); padding: 10px 12px; margin-bottom: 8px; }
.tram-anys { font-weight: 750; font-variant-numeric: tabular-nums; font-size: .9rem; color: var(--tinta-2); }
.tram-nom { font-size: 1rem; overflow-wrap: anywhere; }
.tram .serie { grid-column: 1 / -1; margin-top: 4px; flex-wrap: wrap; }
.v-F { border-left-color: var(--e-F); background: var(--e-F-suau); }
.v-P { border-left-color: var(--e-P); background: var(--e-P-suau); }
.v-ND { border-left-color: var(--e-ND); background: var(--e-ND-suau); }
.v-NA { border-left-color: var(--e-NA); background: var(--e-NA-suau); }

/* Taula d'anys */
.taula-anys { margin-top: 14px; }
.taula-wrap + .nota, .llegenda + .taula-wrap { margin-top: 12px; }
.taula-anys th[scope="row"] { font-variant-numeric: tabular-nums; font-weight: 750; }
.taula-anys td, .taula-anys th { vertical-align: middle; }
.t-ceo { font-weight: 600; min-width: 180px; }
.aplicat { display: block; font-weight: 400; font-size: .8rem; color: var(--nv); background: var(--nv-fons); border-radius: 6px; padding: 4px 7px; margin-top: 5px; }
.cert { display: inline-block; font-size: .82rem; font-weight: 600; padding: 3px 9px; border-radius: 999px; white-space: nowrap; background: var(--sup-2); color: var(--tinta-2); border: 1px solid var(--linia); }
.cert-certificada { background: var(--v-fons); color: var(--v); border-color: transparent; }
.cert-certificada_ceo_pendent { background: var(--nv-fons); color: var(--nv); border-color: transparent; }
.cert-no_certificada { background: var(--mal-fons); color: var(--mal); border-color: transparent; }
.pv { display: inline-flex; align-items: center; gap: 4px; font-size: .84rem; font-weight: 650; padding: 3px 9px; border-radius: 999px; text-decoration: none; white-space: nowrap; }
.pv-v { background: var(--v-fons); color: var(--v); }
.pv-nv { background: var(--nv-fons); color: var(--nv); }
.pv-base { background: var(--base-fons); color: var(--base); }
.pv-no { color: var(--tinta-3); font-weight: 500; }
a.pv:hover { text-decoration: underline; }

/* Proves */
.filtre-anys { display: none; flex-wrap: wrap; gap: 6px; margin: 10px 0 6px; }
.js .filtre-anys { display: flex; }
.xip { font: inherit; font-size: .85rem; font-weight: 600; border: 1px solid var(--linia-forta); background: var(--sup); color: var(--tinta-2); border-radius: 999px; padding: 5px 12px; cursor: pointer; font-variant-numeric: tabular-nums; }
.xip:hover { background: var(--sup-2); }
.xip[aria-pressed="true"] { background: var(--tinta); color: var(--sup); border-color: var(--tinta); }
.recompte-proves { font-size: .88rem; color: var(--tinta-3); min-height: 1.3em; }
.grup-proves { margin: 22px 0 8px; }
.grup-proves > h3 { display: flex; align-items: center; gap: 8px; font-size: 1.15rem; }
.grup-proves > h3 .n { font-size: .78rem; background: var(--sup-3); color: var(--tinta-2); padding: 2px 9px; border-radius: 999px; font-variant-numeric: tabular-nums; }
.prova { background: var(--sup); border: 1px solid var(--linia); border-left: 5px solid var(--v); border-radius: var(--radi); padding: 16px 18px; margin: 12px 0; box-shadow: var(--ombra); }
.prova-nv { border-left-color: var(--nv); }
.prova-mal { border-left-color: var(--mal); }
.prova-base { border-left-color: var(--base); }
.prova-oculta { border-left-color: var(--tinta-3); background: var(--sup-2); box-shadow: none; }
.prova-oculta { padding: 10px 14px; }
.prova-oculta .p-cap { margin-bottom: 4px; }
.prova-oculta p { margin: 0; color: var(--tinta-3); font-size: .84rem; }
.prova:target { outline: 3px solid var(--focus); outline-offset: 2px; }
.p-cap { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin-bottom: 10px; }
.p-anys { margin-left: auto; font-size: .86rem; font-weight: 700; font-variant-numeric: tabular-nums; color: var(--tinta-2); background: var(--sup-2); padding: 3px 10px; border-radius: 999px; }
.b { display: inline-flex; align-items: center; font-size: .78rem; font-weight: 700; padding: 3px 9px; border-radius: 999px; white-space: nowrap; line-height: 1.3; font-family: var(--font); }
.b-v { background: var(--v-fons); color: var(--v); }
.b-nv { background: var(--nv-fons); color: var(--nv); }
.b-mal { background: var(--mal-fons); color: var(--mal); }
.b-base { background: var(--base-fons); color: var(--base); }
.b-gris { background: var(--sup-3); color: var(--tinta-2); }
.b-marca { background: transparent; border: 1px solid var(--linia-forta); color: var(--tinta-2); font-family: var(--font-mono); font-size: .76rem; }
.b-nivell { background: var(--e-P-suau); color: var(--tinta); }
.cita { margin: 0 0 12px; padding: 14px 18px 14px 44px; background: var(--cita-fons); border-radius: var(--radi-petit); position: relative; border: 1px solid var(--linia); }
.cita::before { content: "“"; position: absolute; left: 12px; top: 2px; font-family: var(--font-cita); font-size: 2.6rem; line-height: 1; color: var(--tinta-3); opacity: .6; }
.cita p { margin: 0; font-family: var(--font-cita); font-size: 1.14rem; line-height: 1.55; color: var(--tinta); overflow-wrap: anywhere; }
.sense-cita { font-style: italic; color: var(--tinta-3); background: var(--sup-2); border-radius: var(--radi-petit); padding: 10px 14px; }
.p-fonts { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-bottom: 12px; }
.domini { font-size: .86rem; font-weight: 650; color: var(--tinta-2); margin-right: 4px; overflow-wrap: anywhere; }
.boto { display: inline-flex; align-items: center; gap: 5px; font-size: .88rem; font-weight: 650; padding: 6px 12px; border-radius: var(--radi-petit); background: var(--enllac); color: #fff; text-decoration: none; }
.boto:hover { color: #fff; filter: brightness(1.1); }
@media (prefers-color-scheme: dark) { .boto, .boto:hover { color: #0d1b2e; } }
.boto-wb { background: transparent; color: var(--enllac); border: 1px solid var(--enllac); }
.boto-wb:hover { color: var(--enllac-hover); background: var(--sup-2); filter: none; }
@media (prefers-color-scheme: dark) { .boto-wb, .boto-wb:hover { color: var(--enllac); } }
.boto-off { background: var(--sup-2); color: var(--tinta-3); border: 1px dashed var(--linia-forta); font-weight: 550; }
.ext { font-size: .85em; }
.p-meta { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 8px 18px; margin: 0; padding: 12px 0 0; border-top: 1px solid var(--linia); }
.p-meta div { min-width: 0; }
.p-meta dt { font-size: .72rem; text-transform: uppercase; letter-spacing: .05em; color: var(--tinta-3); font-weight: 700; }
.p-meta dd { margin: 2px 0 0; font-size: .88rem; overflow-wrap: anywhere; }
.llista-codi { margin: 4px 0 0; padding-left: 18px; }
.p-notes { margin-top: 12px; padding-top: 10px; border-top: 1px solid var(--linia); }
.p-notes h4 { font-size: .72rem; text-transform: uppercase; letter-spacing: .05em; color: var(--tinta-3); margin-bottom: 4px; }
.p-notes p { font-size: .9rem; color: var(--tinta-2); margin-bottom: .5em; overflow-wrap: anywhere; }
.nota-oculta { font-style: italic; color: var(--tinta-3) !important; }
.nota-llarga summary { cursor: pointer; font-size: .9rem; color: var(--tinta-2); }
.sense-proves { background: var(--sup); border: 1px dashed var(--linia-forta); border-radius: var(--radi); padding: 18px; }
.sense-proves p { margin: 0; }
.rastre { margin-top: 14px; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 12px 16px; }
.rastre summary { cursor: pointer; font-weight: 600; }
.llista-urls { padding-left: 18px; font-size: .86rem; }
.url-llarga { overflow-wrap: anywhere; }
.nav-fitxes { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 30px; }
.nav-fitxes a { display: flex; flex-direction: column; gap: 2px; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 12px 16px; text-decoration: none; font-weight: 650; color: var(--tinta); box-shadow: var(--ombra); min-width: 0; overflow-wrap: anywhere; }
.nav-fitxes a small { color: var(--tinta-3); font-weight: 600; }
.nav-fitxes a:hover { border-color: var(--enllac); }
.nav-fitxes .seg { text-align: right; }

/* Metodologia */
.text-llarg { max-width: 860px; }
.text-llarg .seccio > h2 { font-size: 1.3rem; }
.def { display: grid; grid-template-columns: minmax(150px, max-content) 1fr; gap: 6px 16px; align-items: start; padding: 10px 0; border-bottom: 1px solid var(--linia); }
.def p { margin: 0; }
.def > :first-child { justify-self: start; }
.docs li { margin-bottom: 6px; }
.taula-simple th, .taula-simple td { padding: 8px 12px; font-size: .9rem; }
.sha { font-size: .78rem; }

/* Peu */
.peu { border-top: 1px solid var(--linia); background: var(--sup); }
.peu-in { max-width: 1240px; margin: 0 auto; padding: 18px 16px 26px; font-size: .8rem; color: var(--tinta-3); }
.peu-in p { margin: 0 0 6px; overflow-wrap: anywhere; }

@media (max-width: 760px) {
  .barra { position: static; }
  html { scroll-padding-top: 12px; }
  .c-pais, .c-p, .c-nd, .c-na, .c-isin { display: none; }
  .tl-wrap { display: none; }
  .trams { display: block; }
  .taula-anys thead { display: none; }
  .taula-anys, .taula-anys tbody { display: block; }
  .taula-anys tr { display: grid; grid-template-columns: 56px 1fr; gap: 6px 10px; padding: 12px; border-bottom: 1px solid var(--linia); }
  .taula-anys tbody tr:last-child { border-bottom: 0; }
  .taula-anys th[scope="row"] { grid-row: 1 / span 6; border: 0; padding: 0; font-size: 1.15rem; }
  .taula-anys td { border: 0; padding: 0; display: flex; flex-wrap: wrap; align-items: center; gap: 4px 8px; }
  .taula-anys td::before { content: attr(data-l); font-size: .68rem; text-transform: uppercase; letter-spacing: .04em; color: var(--tinta-3); font-weight: 700; min-width: 96px; }
  .taula-anys td.t-ceo { display: block; font-size: 1.02rem; }
  .taula-anys td.t-ceo::before { display: none; }
  .bcols { gap: 3px; }
  .bany { font-size: .62rem; }
  .tip { white-space: normal; width: 150px; }
  .c-nom { min-width: 160px; }
  th, td { padding: 9px 10px; }
  .def { grid-template-columns: 1fr; }
  .p-anys { margin-left: 0; }
  .fitxa-cap { padding: 16px; }
  .prova { padding: 14px; }
  .cita { padding: 12px 14px 12px 36px; }
  .cita p { font-size: 1.05rem; }
  .nav-fitxes { grid-template-columns: 1fr; }
  .nav-fitxes .seg { text-align: left; }
}
@media (max-width: 480px) {
  .c-anys { display: none; }
  .k-val { font-size: 1.55rem; }
}
@media print {
  .barra, .filtres, .filtre-anys, .nav-fitxes, .salts { display: none !important; }
  .prova { break-inside: avoid; box-shadow: none; }
}
"""

JS_CERCA = r"""/* Cercador i filtres de l'inici. Generat per dashboard/genera_dashboard.py. Sense dependències. */
(function () {
  'use strict';
  var taula = document.getElementById('taula');
  if (!taula) return;
  var tbody = taula.tBodies[0];
  var files = Array.prototype.slice.call(tbody.rows);
  var camps = {
    q: document.getElementById('f-cerca'),
    e: document.getElementById('f-etiq'),
    c: document.getElementById('f-cert'),
    p: document.getElementById('f-pais'),
    s: document.getElementById('f-sector'),
    v: document.getElementById('f-proves')
  };
  var nVis = document.getElementById('n-visibles');
  var cap = document.getElementById('cap-resultat');
  var ordre = { clau: 'nom', dir: 1 };

  function norm(s) {
    return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/\s+/g, ' ').trim();
  }
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.'); }
  function conte(llista, valor) { return (' ' + (llista || '') + ' ').indexOf(' ' + valor + ' ') >= 0; }

  function aplica() {
    var termes = norm(camps.q.value).split(' ').filter(Boolean);
    var e = camps.e.value, c = camps.c.value, p = camps.p.value, v = camps.v.value;
    var s = camps.s ? camps.s.value : '';
    var n = 0;
    for (var i = 0; i < files.length; i++) {
      var tr = files[i], d = tr.dataset, ok = true;
      for (var j = 0; j < termes.length && ok; j++) { if (d.cerca.indexOf(termes[j]) < 0) ok = false; }
      if (ok && e && !conte(d.etiq, e)) ok = false;
      if (ok && c && !conte(d.cert, c)) ok = false;
      if (ok && p && d.pais !== p) ok = false;
      if (ok && v && d.proves !== v) ok = false;
      if (ok && s && d.sector !== s) ok = false;
      tr.hidden = !ok;
      if (ok) n++;
    }
    nVis.textContent = fmt(n);
    cap.hidden = n > 0;
    desa();
  }

  function ordena(clau) {
    if (ordre.clau === clau) { ordre.dir = -ordre.dir; } else { ordre.clau = clau; ordre.dir = (clau === 'nom' || clau === 'isin') ? 1 : -1; }
    var num = !(clau === 'nom' || clau === 'isin');
    files.sort(function (a, b) {
      var x = a.dataset[clau], y = b.dataset[clau], r;
      if (num) { r = (+x) - (+y); } else { r = x < y ? -1 : x > y ? 1 : 0; }
      if (r === 0) { r = a.dataset.nom < b.dataset.nom ? -1 : a.dataset.nom > b.dataset.nom ? 1 : 0; return r; }
      return r * ordre.dir;
    });
    var frag = document.createDocumentFragment();
    files.forEach(function (tr) { frag.appendChild(tr); });
    tbody.appendChild(frag);
    taula.querySelectorAll('thead button[data-ordre]').forEach(function (b) {
      if (b.getAttribute('data-ordre') === ordre.clau) { b.setAttribute('aria-sort', ordre.dir > 0 ? 'ascending' : 'descending'); }
      else { b.removeAttribute('aria-sort'); }
    });
  }

  function desa() {
    var params = [];
    ['q', 'e', 'c', 'p', 's', 'v'].forEach(function (k) {
      if (camps[k] && camps[k].value) params.push(k + '=' + encodeURIComponent(camps[k].value));
    });
    var hash = params.length ? '#' + params.join('&') : '';
    if (location.hash !== hash) {
      try { history.replaceState(null, '', hash || location.pathname + location.search); } catch (err) { /* res */ }
    }
  }
  function llegeix() {
    var h = location.hash.replace(/^#/, '');
    if (!h || h.indexOf('=') < 0) return;
    h.split('&').forEach(function (parell) {
      var kv = parell.split('='), k = kv[0], val = decodeURIComponent(kv[1] || '');
      if (camps[k]) camps[k].value = val;
    });
  }

  camps.q.addEventListener('input', aplica);
  ['e', 'c', 'p', 's', 'v'].forEach(function (k) { if (camps[k]) camps[k].addEventListener('change', aplica); });
  document.getElementById('f-reset').addEventListener('click', function () {
    ['q', 'e', 'c', 'p', 's', 'v'].forEach(function (k) { if (camps[k]) camps[k].value = ''; });
    aplica();
    camps.q.focus();
  });
  taula.querySelectorAll('thead button[data-ordre]').forEach(function (b) {
    b.addEventListener('click', function () { ordena(b.getAttribute('data-ordre')); });
  });
  llegeix();
  aplica();
})();
"""

JS_FITXA = r"""/* Filtre de proves per any a la fitxa. Generat per dashboard/genera_dashboard.py. Sense dependències. */
(function () {
  'use strict';
  var cont = document.getElementById('proves');
  if (!cont) return;
  var proves = cont.querySelectorAll('.prova[data-anys]');
  var grups = cont.querySelectorAll('.grup-proves');
  var xips = cont.querySelectorAll('.xip[data-filtre-any]');
  var estat = document.getElementById('estat-filtre');
  if (!proves.length) return;

  function filtra(any) {
    var n = 0;
    proves.forEach(function (p) {
      var ok = !any || (' ' + p.getAttribute('data-anys') + ' ').indexOf(' ' + any + ' ') >= 0;
      p.hidden = !ok;
      if (ok) n++;
    });
    grups.forEach(function (g) {
      var vis = g.querySelectorAll('.prova:not([hidden])').length;
      g.hidden = vis === 0;
      var comptador = g.querySelector('h3 .n');
      if (comptador) comptador.textContent = vis;
    });
    xips.forEach(function (x) { x.setAttribute('aria-pressed', x.getAttribute('data-filtre-any') === any ? 'true' : 'false'); });
    if (estat) {
      estat.textContent = any ? ('Es mostren ' + n + (n === 1 ? ' prova' : ' proves') + ' que cobreixen el ' + any + '.') : '';
    }
  }

  document.addEventListener('click', function (ev) {
    var el = ev.target.closest ? ev.target.closest('[data-filtre-any]') : null;
    if (!el) return;
    var any = el.getAttribute('data-filtre-any') || '';
    if (el.tagName !== 'A') ev.preventDefault();
    filtra(any);
  });
})();
"""


if __name__ == "__main__":
    raise SystemExit(main())

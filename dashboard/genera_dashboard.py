#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador del dashboard estàtic de la base Fundadors (STOXX Europe 600, 2016-2025).

Ús, des de l'arrel del repositori:

    python3 dashboard/genera_dashboard.py

Què fa:

- Comprova el SHA-256 de `dades/base_isin_any_v8r3.csv`, `docs/REGISTRE_CANVIS.csv`,
  `estat/estat_files.csv`, `PENDENTS.md` i `estat/dubtes_tancats.csv` contra
  `MANIFEST_SHA256.csv` del mateix commit, i que `estat/RESUM_ESTAT.md` s'ha
  generat amb aquestes mateixes dades. Si no coincideixen, s'atura i no escriu res.
- Totes les xifres de progrés surten de `estat/estat_files.csv` (un sol
  comptador). Si l'embut no quadra amb l'estat de les files, s'atura.
- Llegeix només fitxers del repositori (csv, pathlib, hashlib). No fa cap
  petició de xarxa ni consulta Wayback ni les fonts originals.
- Reescriu només fitxers dins de `dashboard/`: `index.html` (Estat),
  `empreses.html`, `metodologia.html`, `empreses/{ISIN}.html` i `assets/`.
- El resultat és determinista: amb les mateixes dades, els mateixos fitxers.

No llegeix l'`.xlsx`, ni `empreses/*.md`, ni `INDEX.md`, ni
`docs/REGISTRE_CANVIS.md`, ni cap fitxer de fora del repositori. De
`PENDENTS.md` només en comprova els encapçalaments i les àncores: mai no en
mostra el text.
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

ROOT = Path(__file__).resolve().parent.parent
SORTIDA = ROOT / "dashboard"
BASE = ROOT / "dades" / "base_isin_any_v8r3.csv"
REGISTRE = ROOT / "docs" / "REGISTRE_CANVIS.csv"
MANIFEST = ROOT / "MANIFEST_SHA256.csv"
ESTAT_CSV = ROOT / "estat" / "estat_files.csv"
RESUM_ESTAT = ROOT / "estat" / "RESUM_ESTAT.md"
DUBTES_TANCATS = ROOT / "estat" / "dubtes_tancats.csv"
URLS_ARXIU = ROOT / "estat" / "urls_per_arxivar.csv"
PENDENTS = ROOT / "PENDENTS.md"
# CSV opcional (no existeix ara): id_document_o_font,url_wayback[,timestamp]
# Només s'usa si existeix; no s'inventa mai.
WAYBACK_EXTRA = SORTIDA / "fonts_wayback_extra.csv"

# Nom de la versió congelada. Buit mentre Jordi no el confirmi: el text diu
# només «la versió congelada», sense número.
VERSIO_CONGELADA = ""
GH_BLOB = f"{REPO_GITHUB}/blob/main"

# Estat exclusiu de cada fila (ordre de l'embut). Clau: (icona, nom, nom curt, definició).
ESTATS = {
    "acabada": ("✓", "Acabada", "Acab.",
                "Té cita de CEO i de fundador, coherent amb la base i sense dubtes, i la cita s'ha "
                "verificat per script a la còpia de Wayback."),
    "arxiu": ("◷", "Només falta l'arxiu", "Arxiu",
              "L'evidència és completa i coherent; falta verificar la cita a una còpia de Wayback."),
    "dubte": ("?", "Amb dubte o incoherència", "Dubte",
              "Té cita de CEO i de fundador, però hi ha un dubte obert a PENDENTS.md o no quadra amb la base."),
    "falta": ("–", "Falta evidència", "Falta",
              "Encara no hi ha cita vàlida de CEO o de fundador."),
}
ORDRE_ESTATS = ["acabada", "arxiu", "dubte", "falta"]
# Mancances (no excloents): nom planer i «què s'hi fa». {cua} = URL a la cua d'arxiu.
MANCANCES = {
    "falta_arxiu": ("Falta la cita verificada a la còpia de Wayback",
                    "Flux automàtic de Wayback a GitHub; {cua} URL a la cua."),
    "falta_fundador": ("Falta la prova de fundador",
                       "Fitxa de fundació per empresa (lot 18, en preparació)."),
    "dubte_obert": ("Dubte obert a PENDENTS.md",
                    "Cerca sense límit d'intents (A.4) i decisió de Jordi."),
    "falta_ceo": ("Falta la cita de CEO", "Cerca de la cita de CEO."),
    "incoherent": ("No quadra amb la base", "Revisió de la fila contra l'evidència."),
}
# Origen dels dubtes oberts: (nom planer, encapçalament de PENDENTS.md).
ORIGENS_DUBTE = {
    "regla29": ("Regla 29 (triatge de lots)", "Dubtes dels lots fora_mostra_auditoria (regla 29)"),
    "lot9": ("Lot 9", "Dubtes del lot ceo_pendent (lot 9)"),
    "lot10": ("Lot 10", "Dubtes del lot traspàs de cites (lot 10)"),
    "lot12": ("Lot 12", "Dubtes del lot 12 (cerca de CEO del grup F)"),
    "lot16": ("Lot 16", "Dubtes del lot 16 (cites de fundador del grup F)"),
    "lot17": ("Lot 17", "Dubtes del lot 17 (cerca de CEO)"),
    "ND_obert": ("ND obert", "1. Casos oberts"),
}
# Problemes de coherència (c4_coherencia), en paraules (estat/README.md).
PROBLEMES_C4 = {
    "ceos_diferent_de_sim_ceo_aplicat": "El CEO de la base no coincideix amb el CEO aplicat a l'auditoria.",
    "F_sense_regla_de_si": "Etiqueta F sense cap regla de «sí» registrada a la base.",
    "P_sense_prova_de_no": "Etiqueta P sense cap regla de prova de no fundador registrada a la base.",
    "P_amb_regla_de_si": "Etiqueta P amb una regla de «sí» registrada a la base.",
    "motiu_nd_residual": "Hi ha un motiu de ND en una fila que no és ND.",
    "NA_sense_motiu_na": "Fila NA sense motiu registrat.",
}
# Regles de la columna `regles`, en paraules. Els codis que no hi són es mostren
# tal com són, enllaçats al glossari del Mètode (no s'inventa cap descripció).
REGLES_TEXT = {
    "b": "b · edat a la fundació",
    "d": "d · incorporació posterior",
    "c_AAF64_reserva": "c · 64 anys o més (reserva)",
    "a": "a · llista de fundadors",
    "e": "e · origen no personal",
    "cita_fundador": "l'anomena fundador",
    "D37": "l'anomena fundador",
    "cap": "sense regla registrada",
}
# Àncora del glossari per a cada codi de regla.
REGLA_ANCORA = {"cita_fundador": "D37", "c_AAF64_reserva": "c"}

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
    for p in (BASE, REGISTRE, ESTAT_CSV, PENDENTS, DUBTES_TANCATS):
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


def comprova_resum_estat(shas: dict[str, str]) -> str:
    """Comprova que les quatre línies SHA-256 de la capçalera de RESUM_ESTAT.md
    corresponen als fitxers actuals (és a dir, que l'estat és d'aquestes dades).
    Retorna el text del resum per a les comprovacions de xifres."""
    if not RESUM_ESTAT.exists():
        atura("no trobo estat/RESUM_ESTAT.md: executa python3 estat/estat_files.py")
    text = RESUM_ESTAT.read_text(encoding="utf-8")
    trobats = dict(re.findall(r"^- `([^`]+)` SHA-256 `([0-9a-f]{64})`", text, re.M))
    for p in (BASE, REGISTRE, PENDENTS, DUBTES_TANCATS):
        rel = p.relative_to(ROOT).as_posix()
        if trobats.get(rel) != shas[rel]:
            atura(f"estat/RESUM_ESTAT.md no correspon a {rel} actual: executa python3 estat/estat_files.py")
    return text


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
    # Recomptes d'entrades del registre (cicle de qualitat): entrades, no files.
    reg = Counter()
    for r in registre:
        reg["entrades"] += 1
        reg[r["marca_veritat"].strip() or "(buida)"] += 1
        wb = (r["url_wayback"] or "").strip()
        if re.match(r"^https?://web\.archive\.org/web/", wb, re.I):
            reg["wb_url"] += 1
        elif wb.lower() == "pendent_verificacio_externa":
            reg["wb_pendent"] += 1
        if (r["cita_verificada_a_captura"] or "").strip() == "si":
            reg["capt_si"] += 1

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
    return {"empreses": empreses, "n_files": len(base), "registre": reg}


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
    # «Pendent d'arxiu»: pendent_arxiu (abans pendent_DF).
    g["pendent_arxiu"] = "pendent_DF" in joined or "pendent_arxiu" in joined
    g["capt_si"] = "si" in g["capt"]


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
            "base_fund": a in base_fund_anys,
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
# Estat de cada fila (estat/estat_files.csv): l'únic comptador de progrés
# ---------------------------------------------------------------------------


def estat_exclusiu(estat: str) -> str:
    """Estat exclusiu de la fila, en l'ordre de l'embut (§1.1 de l'especificació)."""
    toks = {t for t in (estat or "").split("+") if t}
    if toks & {"falta_ceo", "falta_fundador"}:
        return "falta"
    if toks & {"dubte_obert", "incoherent"}:
        return "dubte"
    if "falta_arxiu" in toks:
        if toks != {"falta_arxiu"}:
            atura(f"estat desconegut a estat_files.csv: {estat!r}")
        return "arxiu"
    if toks == {"acabada"}:
        return "acabada"
    atura(f"estat desconegut a estat_files.csv: {estat!r}")
    return ""


def carrega_estat(model: dict) -> None:
    """Uneix cada fila de la base amb la seva fila d'estat per (isin, any)."""
    files = llegeix_csv(ESTAT_CSV)
    estat = {}
    for r in files:
        k = (r["isin"].strip(), r["any"].strip())
        if k in estat:
            atura(f"clau duplicada a estat/estat_files.csv: {k}")
        estat[k] = r
    claus_base = {(e["isin"], str(f["any"])) for e in model["empreses"].values() for f in e["files"]}
    if len(estat) != model["n_files"] or set(estat) != claus_base:
        atura("estat/estat_files.csv no té les mateixes claus (isin, any) que la base: "
              "executa python3 estat/estat_files.py")
    for e in model["empreses"].values():
        for f in e["files"]:
            r = estat[(e["isin"], str(f["any"]))]
            f["est"] = r
            f["cat"] = estat_exclusiu(r["estat"])
            f["mancances"] = [t for t in r["estat"].split("+") if t in MANCANCES]
            f["dubtes"] = [t for t in r["dubtes_oberts"].split(";") if t]
            f["regles"] = [t for t in re.split(r"[;|]", r["regles"] or "") if t]
        e["st"] = Counter(f["cat"] for f in e["files"])
        e["mancances"] = sorted({m for f in e["files"] for m in f["mancances"]}, key=list(MANCANCES).index)


def compta_files_csv(path: Path) -> int | None:
    if not path.exists():
        return None
    return len(llegeix_csv(path))


def xifres_resum(text: str) -> dict:
    """Llegeix de RESUM_ESTAT.md l'embut, la fila Total i les mancances, per
    comprovar que l'Estat mostra exactament les mateixes xifres."""
    def num(s: str) -> int:
        return int(s.replace(".", ""))
    out: dict = {}
    m = re.search(r"^## Embut\n(.*?)\n## ", text, re.S | re.M)
    if m:
        out["embut"] = [num(x) for x in re.findall(r"^\|[^|\n]+\|\s*([\d.]+)", m.group(1), re.M)]
    m = re.search(r"^\| \*\*Total\*\* \|(.*)$", text, re.M)
    if m:
        out["total"] = [num(x) for x in re.findall(r"([\d.]+) \(", m.group(1))]
    m = re.search(r"^## Què falta, per condició\n(.*?)\n## ", text, re.S | re.M)
    if m:
        out["mancances"] = {k: num(v) for k, v in re.findall(r"^\| `(\w+)` \|.*\|\s*([\d.]+) \|$", m.group(1), re.M)}
    return out


def calcula_estat(model: dict, resum_text: str) -> dict:
    emp = model["empreses"]
    files = [f for e in emp.values() for f in e["files"]]
    tot = len(files)
    cat = Counter(f["cat"] for f in files)
    toks = [set(f["est"]["estat"].split("+")) for f in files]
    c1 = sum("falta_ceo" not in t for t in toks)
    c2 = sum("falta_fundador" not in t for t in toks)
    c4 = sum(not (t & {"incoherent", "dubte_obert"}) for t in toks)
    c3 = sum("falta_arxiu" not in t for t in toks)
    c12 = sum(not (t & {"falta_ceo", "falta_fundador"}) for t in toks)
    c124 = sum(not (t & {"falta_ceo", "falta_fundador", "incoherent", "dubte_obert"}) for t in toks)
    acab = cat["acabada"]
    # Assercions de §1.1: la barra de quatre estats ha de quadrar amb l'embut.
    if c12 != tot - cat["falta"]:
        atura(f"l'embut no quadra: C1∧C2 = {c12}, total − falta evidència = {tot - cat['falta']}")
    if c124 != c12 - cat["dubte"]:
        atura(f"l'embut no quadra: C1∧C2∧C4 = {c124}, C1∧C2 − dubte = {c12 - cat['dubte']}")
    if acab != c124 - cat["arxiu"] or sum(cat.values()) != tot:
        atura("l'embut no quadra amb els quatre estats")
    embut = [tot, c12, c124, acab]
    mancances = Counter(m for f in files for m in f["mancances"])

    # Les xifres han de ser les de estat/RESUM_ESTAT.md.
    ref = xifres_resum(resum_text)
    if ref.get("embut") != embut:
        atura(f"l'embut ({embut}) no coincideix amb estat/RESUM_ESTAT.md ({ref.get('embut')})")
    if ref.get("total") != [c1, c2, c12, c4, c3, acab]:
        atura(f"la fila Total no coincideix amb estat/RESUM_ESTAT.md ({ref.get('total')})")
    if ref.get("mancances") != {k: mancances[k] for k in ref.get("mancances", {})} or \
            set(ref.get("mancances", {})) != set(MANCANCES):
        atura(f"les mancances no coincideixen amb estat/RESUM_ESTAT.md ({ref.get('mancances')})")

    per_etiq = {}
    for l in ["F", "P", "NA", "ND"]:
        fl = [(f, t) for f, t in zip(files, toks) if f["lletra"] == l]
        per_etiq[l] = {
            "files": len(fl),
            "C1": sum("falta_ceo" not in t for _, t in fl),
            "C2": sum("falta_fundador" not in t for _, t in fl),
            "C4": sum(not (t & {"incoherent", "dubte_obert"}) for _, t in fl),
            "C3": sum("falta_arxiu" not in t for _, t in fl),
            "acabada": sum(f["cat"] == "acabada" for f, _ in fl),
        }
    per_any: dict[int, Counter] = defaultdict(Counter)
    etiq_any: dict[int, Counter] = defaultdict(Counter)
    for f in files:
        per_any[f["any"]][f["cat"]] += 1
        per_any[f["any"]]["total"] += 1
        etiq_any[f["any"]][f["lletra"]] += 1
        etiq_any[f["any"]]["total"] += 1
    dubtes = Counter(d for f in files for d in f["dubtes"])
    return {
        "n_isin": len(emp), "tot": tot, "cat": cat, "embut": embut,
        "c1": c1, "c2": c2, "c3": c3, "c4": c4,
        "per_etiq": per_etiq, "per_any": dict(sorted(per_any.items())),
        "etiq_any": dict(sorted(etiq_any.items())),
        "etiq": Counter(f["lletra"] for f in files),
        "mancances": mancances,
        "dubtes": dubtes,
        "files_amb_dubte": sum(bool(f["dubtes"]) for f in files),
        "dubtes_tancats": compta_files_csv(DUBTES_TANCATS) or 0,
        "urls_cua": compta_files_csv(URLS_ARXIU),
        "columna_antiga": sum(f["est"]["c2_fundador"] == "ok_columna_antiga" for f in files),
        "interval": sum("interval" in f["est"]["c1_tipus"] for f in files),
        "registre": model["registre"],
        "emp_totes_acabades": sum(e["st"]["acabada"] == len(e["files"]) for e in emp.values()),
    }


def pendents_info() -> dict:
    """Només els encapçalaments «## …» i les àncores <a id> de PENDENTS.md."""
    text = PENDENTS.read_text(encoding="utf-8")
    return {
        "titols": {l[3:].strip() for l in text.splitlines() if l.startswith("## ")},
        "ancores": set(re.findall(r'<a id="([^"]+)"', text)),
    }


def slug_github(titol: str) -> str:
    s = titol.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def url_pendents(pend: dict, origen: str | None = None, ancora: str | None = None) -> str:
    url = f"{GH_BLOB}/PENDENTS.md"
    if ancora and ancora in pend["ancores"]:
        return f"{url}#{ancora}"
    if origen in ORIGENS_DUBTE and ORIGENS_DUBTE[origen][1] in pend["titols"]:
        return f"{url}#{slug_github(ORIGENS_DUBTE[origen][1])}"
    return url


# ---------------------------------------------------------------------------
# HTML comú
# ---------------------------------------------------------------------------


class Context:
    def __init__(self, commit: str, data_commit: str, shas: dict[str, str]):
        self.commit = commit
        self.data_commit = data_commit
        self.shas = shas
        self.sha_base = shas[BASE.relative_to(ROOT).as_posix()]
        self.sha_registre = shas[REGISTRE.relative_to(ROOT).as_posix()]
        self.sha_estat = shas[ESTAT_CSV.relative_to(ROOT).as_posix()]
        self.pend = pendents_info()


def curt(sha: str, n: int = 7) -> str:
    return sha[:n] if len(sha) > n else sha


def data_ca(d: str) -> str:
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", d or "")
    return f"{m.group(3)}/{m.group(2)}/{m.group(1)}" if m else (d or "data desconeguda")


def nom_versio() -> str:
    return f"la versió congelada ({VERSIO_CONGELADA})" if VERSIO_CONGELADA else "la versió congelada"


def pagina(ctx: Context, *, titol: str, descripcio: str, cos: str, prefix: str,
           actiu: str, scripts: tuple[str, ...] = (), ample: bool = False, cap_extra: str = "",
           cls_body: str = "") -> str:
    nav = []
    for clau, href, text in (("estat", "index.html", "Estat"),
                             ("empreses", "empreses.html", "Empreses"),
                             ("metode", "metodologia.html", "Mètode")):
        cur = ' aria-current="page"' if clau == actiu else ""
        nav.append(f'<a href="{prefix}{href}"{cur}>{text}</a>')
    js = "".join(f'<script src="{prefix}assets/{s}" defer></script>' for s in scripts)
    data = data_ca(ctx.data_commit)
    body = f' class="{cls_body}"' if cls_body else ""
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
{cap_extra}{js}
</head>
<body{body}>
<a class="salta" href="#contingut">Salta al contingut</a>
<header class="barra">
<div class="barra-in">
<a class="marca" href="{prefix}index.html"><span class="marca-logo" aria-hidden="true"><i></i><i></i><i></i></span><span class="marca-text">Fundadors-CEO · STOXX Europe 600<small>Base de dades de doctorat · 2016–2025</small></span></a>
<nav class="nav" aria-label="Navegació principal">{''.join(nav)}</nav>
<a class="pindola" href="{prefix}index.html#versio">En revisió · dades del {esc(data)}</a>
</div>
</header>
<main id="contingut" class="pagina{' ample' if ample else ''}">
{cos}
</main>
<footer class="peu">
<p class="peu-in">Generat a partir del repositori · commit <code title="{esc(ctx.commit)}">{esc(curt(ctx.commit))}</code> · {esc(data)} · Detalls a <a href="{prefix}index.html#versio">Sobre aquestes dades</a></p>
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


NOM_ETIQ = {v[0]: v[1] for v in ETIQUETES.values()}
NOM_ETIQ_MIN = {"F": "fundador-CEO", "P": "professional", "ND": "no determinat", "NA": "sense CEO"}


def badge_etiq(lletra: str) -> str:
    return f'<span class="etq e-{lletra}"><b>{lletra}</b> <span class="etq-nom">{esc(NOM_ETIQ[lletra])}</span></span>'


def enllac_ext(url: str, text: str, cls: str = "") -> str:
    u = url_segura(url)
    c = f' class="{cls}"' if cls else ""
    if not u:
        return f"<span{c}>{esc(text)}</span>"
    return f'<a{c} href="{esc(u)}" target="_blank" rel="noopener noreferrer">{esc(text)}<span class="ext" aria-hidden="true">↗</span></a>'


def insignia_estat(cat: str, curt_: bool = False) -> str:
    icona, nom, nom_curt, defi = ESTATS[cat]
    return (f'<span class="st st-{cat}" title="{esc(defi)}"><span aria-hidden="true">{icona}</span> '
            f'{esc(nom_curt if curt_ else nom)}</span>')


def minibarra_estat(st: Counter, total: int, cls: str = "mb") -> str:
    """Minibarra de quatre segments (decorativa: el text del costat porta les xifres)."""
    segs = "".join(
        f'<i class="s-{k}" style="flex-grow:{st[k]}"></i>' for k in ORDRE_ESTATS if st[k]
    )
    return f'<span class="{cls}" aria-hidden="true">{segs}</span>'


def pct_txt(n: int, d: int) -> str:
    return fmt_pct(n, d)


def dades_taula(cap: str, files: list[list[str]], resum: str = "Mostra les dades en una taula") -> str:
    th = "".join(f'<th scope="col"{" class=num" if i else ""}>{c}</th>' for i, c in enumerate(cap))
    cos = "".join(
        "<tr>" + "".join((f'<th scope="row">{c}</th>' if i == 0 else f'<td class="num">{c}</td>') for i, c in enumerate(fila)) + "</tr>"
        for fila in files
    )
    return (f'<details class="dades"><summary>{esc(resum)}</summary>'
            f'<div class="taula-wrap"><table class="taula-simple"><thead><tr>{th}</tr></thead><tbody>{cos}</tbody></table></div></details>')


# ---------------------------------------------------------------------------
# Components de l'Estat
# ---------------------------------------------------------------------------


def barra_apilada(segs: list[tuple[str, int, str]], total: int, etiqueta: str, cls: str) -> str:
    """Barra al 100 % de segments (clau, n, nom). Els segments a 0 no es pinten.
    La xifra només va dins el segment si hi cap; si no, és a la llegenda."""
    parts = []
    for clau, n, nom in segs:
        if not n:
            continue
        pct = 100 * n / total if total else 0
        dins = f'<span class="sb-n">{fmt_pct(n, total, 0)}</span>' if pct >= 14 else ""
        parts.append(f'<span class="sb-s {cls}-{clau}" style="flex-grow:{n}" title="{esc(nom)}: {fmt_int(n)} ({fmt_pct(n, total)})">{dins}</span>')
    aria = etiqueta + ": " + "; ".join(f"{nom} {fmt_int(n)} ({fmt_pct(n, total)})" for _, n, nom in segs)
    return f'<div class="sb" role="img" aria-label="{esc(aria)}">{"".join(parts)}</div>'


def llegenda_estats(cat: Counter, total: int) -> str:
    items = []
    for k in ORDRE_ESTATS:
        icona, nom, _, defi = ESTATS[k]
        items.append(
            f'<li><span class="sw s-{k}" aria-hidden="true">{icona}</span>'
            f'<span class="ll-txt"><b>{esc(nom)}</b> <span class="ll-n">{fmt_int(cat[k])} · {fmt_pct(cat[k], total)}</span>'
            f'<span class="ll-def">{esc(defi)}</span></span></li>'
        )
    return f'<ul class="ll-estats">{"".join(items)}</ul>'


def embut(E: dict) -> str:
    tot, c12, c124, acab = E["embut"]
    passos = [
        ("Panell", tot, ""),
        ("Amb cita de CEO i de fundador (C1 i C2)", c12, "falta"),
        ("… i coherents, sense dubtes oberts (C4)", c124, "dubte"),
        ("… i amb la cita verificada a la còpia de Wayback (C3), és a dir, acabades", acab, "arxiu"),
    ]
    items = []
    salts = []
    prev = None
    for i, (nom, n, perd) in enumerate(passos):
        if prev is not None:
            caiguda = prev - n
            salts.append((caiguda, perd))
            items.append(
                f'<li class="eb-salt"><span class="sw s-{perd}" aria-hidden="true">{ESTATS[perd][0]}</span>'
                f'−{fmt_int(caiguda)} {esc(ESTATS[perd][1].lower())}</li>'
            )
        pct = 100 * n / tot if tot else 0
        val = fmt_int(n) + (f" ({fmt_pct(n, tot)})" if i else "")
        cls = " eb-final" if i == len(passos) - 1 else ""
        items.append(
            f'<li class="eb-pas{cls}"><span class="eb-nom">{esc(nom)}</span>'
            f'<span class="eb-fila"><span class="eb-barra" style="width:{pct:.2f}%"></span><span class="eb-val">{val}</span></span></li>'
        )
        prev = n
    gran = max(salts, key=lambda x: x[0]) if salts else (0, "")
    frase = ""
    if gran[0]:
        nom_pas = {"falta": "el de l'evidència", "dubte": "el dels dubtes", "arxiu": "el de l'arxiu"}[gran[1]]
        frase = (f'<p class="resposta">El pas on es queden més files és <b>{esc(nom_pas)}</b>: '
                 f'{fmt_int(gran[0])} files ({esc(ESTATS[gran[1]][1].lower())}).</p>')
    aria = "Embut: " + " → ".join(f"{nom} {fmt_int(n)}" for nom, n, _ in passos)
    taula = dades_taula(["Pas", "Files", "% del panell"],
                        [[esc(nom), fmt_int(n), fmt_pct(n, tot)] for nom, n, _ in passos])
    return (f'{frase}<ol class="embut" role="img" aria-label="{esc(aria)}">{"".join(items)}</ol>{taula}')


def taula_etiquetes(E: dict) -> str:
    cols = [("C1", "C1 CEO", "Té cita vàlida de CEO"), ("C2", "C2 fundador", "Té prova de fundador o de no fundador"),
            ("C4", "C4 coherent", "Coherent amb la base i sense dubtes oberts"),
            ("C3", "C3 arxiu", "Cita verificada a la còpia de Wayback"), ("acabada", "Acabades", "Compleix les quatre condicions")]
    th = "".join(f'<th scope="col" class="num"><span class="llarg">{esc(n)}</span><abbr class="curt" title="{esc(t)}">{esc("Acab." if k == "acabada" else n.split()[0])}</abbr></th>' for k, n, t in cols)
    files = []
    for l in ["F", "P", "NA", "ND"]:
        d = E["per_etiq"][l]
        n = d["files"]
        cel = []
        for k, _, _ in cols:
            v = d[k]
            pct = 100 * v / n if n else 0
            cel.append(f'<td class="num"><span class="tc-v"><span class="llarg">{fmt_pct(v, n)}</span><span class="curt">{fmt_pct(v, n, 0)}</span></span><span class="tc-n">{fmt_int(v)}</span>'
                       f'<span class="mm" aria-hidden="true"><i style="width:{pct:.1f}%"></i></span></td>')
        files.append(f'<tr><th scope="row">{badge_etiq(l)}</th><td class="num">{fmt_int(n)}</td>{"".join(cel)}</tr>')
    return (f'<div class="taula-wrap"><table class="taula-etiq"><caption class="vh">Condicions complertes per etiqueta FounderCEO</caption>'
            f'<thead><tr><th scope="col">Etiqueta</th><th scope="col" class="num">Files</th>{th}</tr></thead>'
            f'<tbody>{"".join(files)}</tbody></table></div>')


def grao(pct: float, n: int) -> int:
    if not n:
        return 0
    return min(5, int(pct // 20) + 1)


def mapa_calor(E: dict) -> str:
    th = "".join(
        f'<th scope="col" class="num"><span aria-hidden="true">{ESTATS[k][0]}</span> '
        f'<span class="llarg">{esc(ESTATS[k][1])}</span><abbr class="curt" title="{esc(ESTATS[k][1])}">{esc(ESTATS[k][2])}</abbr></th>'
        for k in ORDRE_ESTATS
    )
    files = []
    for a, c in E["per_any"].items():
        tot = c["total"]
        cel = []
        for k in ORDRE_ESTATS:
            n = c[k]
            pct = 100 * n / tot if tot else 0
            g = grao(pct, n)
            cel.append(f'<td class="num hm hm-{k} g{g}"><b>{fmt_int(n)}</b><small>{fmt_pct(n, tot, 0)}</small></td>')
        files.append(f'<tr><th scope="row">{a}</th>{"".join(cel)}<td class="num">{fmt_int(tot)}</td></tr>')
    escala = "".join(f'<li><span class="hm hm-acabada g{g}" aria-hidden="true"></span>{esc(t)}</li>'
                     for g, t in ((0, "0"), (1, "fins al 20 %"), (2, "20–40 %"), (3, "40–60 %"), (4, "60–80 %"), (5, "80–100 %")))
    return (f'<div class="taula-wrap"><table class="mapa"><caption class="vh">Files de cada any segons l\'estat (nombre i % de l\'any)</caption>'
            f'<thead><tr><th scope="col">Any</th>{th}<th scope="col" class="num">Total</th></tr></thead>'
            f'<tbody>{"".join(files)}</tbody></table></div>'
            f'<div class="hm-escala"><span>Intensitat: % de les files de l\'any, en el to de cada estat.</span><ul>{escala}</ul></div>')


def barres_simples(files: list[tuple[str, int, str]], maxim: int, etiqueta: str) -> str:
    """Barres horitzontals d'una sola sèrie: (nom en HTML, valor, detall en HTML)."""
    items = []
    for nom, n, detall in files:
        pct = 100 * n / maxim if maxim else 0
        items.append(
            f'<li><span class="bs-nom">{nom}</span>'
            f'<span class="bs-fila"><span class="bs-barra" style="width:{pct:.2f}%"></span><span class="bs-val">{fmt_int(n)}</span></span>'
            f'{detall}</li>'
        )
    return f'<ul class="bs" role="list" aria-label="{esc(etiqueta)}">{"".join(items)}</ul>'


def barres_mancances(E: dict) -> str:
    tot = E["tot"]
    cua = fmt_int(E["urls_cua"]) if E["urls_cua"] is not None else "les"
    files = []
    for k, (nom, que) in MANCANCES.items():
        n = E["mancances"][k]
        detall = (f'<span class="bs-det">{fmt_int(n)} files ({fmt_pct(n, tot)}) · <code class="codi-petit">{k}</code></span>'
                  f'<span class="bs-que"><b>Què s\'hi fa:</b> {esc(que.format(cua=cua))}</span>'
                  f'<a class="bs-link" href="empreses.html#m={k}">Mostra les empreses</a>')
        files.append((esc(nom), n, detall))
    return barres_simples(files, tot, "Files amb cada mancança, sobre el total de files")


def barres_dubtes(E: dict, pend: dict) -> str:
    if not E["dubtes"]:
        return '<p class="resposta">No hi ha dubtes oberts.</p>'
    ordre = [k for k in ORIGENS_DUBTE if E["dubtes"][k]] + sorted(k for k in E["dubtes"] if k not in ORIGENS_DUBTE)
    maxim = max(E["dubtes"].values())
    files = []
    for k in ordre:
        nom = ORIGENS_DUBTE.get(k, (k, ""))[0]
        sec = ORIGENS_DUBTE.get(k, ("", ""))[1]
        url = url_pendents(pend, k)
        link = (f'<a class="bs-link" href="{esc(url)}" target="_blank" rel="noopener noreferrer">'
                f'Secció «{esc(sec)}» a PENDENTS.md<span class="ext" aria-hidden="true">↗</span></a>') if sec else ""
        files.append((esc(nom), E["dubtes"][k], link))
    return barres_simples(files, maxim, "Files amb dubte obert, per origen")


def passos_qualitat(E: dict) -> str:
    R = E["registre"]
    passos = [
        ("Font A/B i cita literal", f'<b>{fmt_int(R["entrades"])}</b> entrades al registre'),
        ("Document obert sencer i cita trobada", f'<b>[V] {fmt_int(R["[V]"])}</b> · [NV] {fmt_int(R["[NV]"])}'),
        ("Còpia a Wayback",
         f'<b>{fmt_int(R["wb_url"])}</b> entrades amb URL Wayback'
         + (f' (i {fmt_int(R["wb_pendent"])} marcades «pendent de verificació externa»)' if R["wb_pendent"] else "")
         + f'; <b>{fmt_int(R["capt_si"])}</b> amb la cita verificada per script a la còpia (<code>id_</code>)'),
        ("Validadors automàtics a cada PR", '<span title="valida_pr.py, comprova_enllacos_cites.py, estat_files.py --comprova">Tres scripts: format del registre, enllaços de les cites i estat de les files</span>'),
        ("Revisió i fusió de Jordi", "i de Doctorat, si cal"),
    ]
    items = "".join(f'<li><span class="pq-n" aria-hidden="true">{i}</span><span class="pq-t"><b class="pq-nom">{esc(t)}</b><span>{x}</span></span></li>'
                    for i, (t, x) in enumerate(passos, start=1))
    return f'<ol class="passos">{items}</ol><p class="nota">Xifres d\'entrades del registre, no de files.</p>'


def grafic_f_per_any(E: dict) -> str:
    per_any = E["etiq_any"]
    anys = list(per_any)
    maxim = max((per_any[a]["F"] for a in anys), default=0)
    pas = 10 if maxim <= 60 else 20
    sostre = max(pas, -(-maxim // pas) * pas)
    eix = "".join(
        f'<span class="tick" style="bottom:{100 * t / sostre:.2f}%"><span>{t}</span></span>' for t in range(0, sostre + 1, pas)
    )
    cols = []
    for a in anys:
        f, tot = per_any[a]["F"], per_any[a]["total"]
        alt = 100 * f / sostre if sostre else 0
        tip = f"{a}: {fmt_int(f)} files F de {fmt_int(tot)} ({fmt_pct(f, tot)})"
        cols.append(
            f'<div class="bcol" tabindex="0" aria-label="{esc(tip)}">'
            f'<div class="barea"><span class="bar" style="height:{alt:.2f}%"><span class="bval">{fmt_int(f)}</span></span></div>'
            f'<span class="bany"><span><span class="a2">{str(a)[:2]}</span>{str(a)[2:]}</span><small>{fmt_pct(f, tot)}</small></span><span class="tip" role="tooltip">{esc(tip)}</span></div>'
        )
    taula = dades_taula(["Any", "Files F", "Files al panell", "% F"],
                        [[str(a), fmt_int(per_any[a]["F"]), fmt_int(per_any[a]["total"]), fmt_pct(per_any[a]["F"], per_any[a]["total"])] for a in anys])
    return (f'<figure class="grafic"><figcaption class="h3">Files F per any <span class="nota llarg">(sota cada any, el % de files F)</span></figcaption>'
            f'<div class="barres" role="img" aria-label="Files F per any, de {anys[0] if anys else ""} a {anys[-1] if anys else ""}">'
            f'<div class="eix">{eix}</div><div class="bcols">{"".join(cols)}</div></div>{taula}</figure>')


def linia_versio(ctx: Context) -> str:
    return (f'<p class="versio-linia"><span class="pv-icona" aria-hidden="true">!</span><span>Versió de treball, en revisió fins a {nom_versio()}. '
            f'Dades de <code>main</code> del {esc(data_ca(ctx.data_commit))} (commit <code title="{esc(ctx.commit)}">{esc(curt(ctx.commit))}</code>). '
            "Les xifres i les etiquetes poden canviar a cada lot que es fusiona.</span></p>")


def sobre_dades(ctx: Context) -> str:
    fitxers = [
        ("dades/base_isin_any_v8r3.csv", ctx.sha_base),
        ("docs/REGISTRE_CANVIS.csv", ctx.sha_registre),
        ("estat/estat_files.csv", ctx.sha_estat),
    ]
    dl = "".join(f'<div><dt><code>{esc(p)}</code></dt><dd><code class="sha">{esc(h)}</code></dd></div>' for p, h in fitxers)
    docs = [("estat/RESUM_ESTAT.md", "resum de l'estat per fila"), ("estat/README.md", "definició de les condicions C1-C4"),
            ("docs/PLA_FINALITZACIO_20261123.md", "pla de finalització"), ("estat/estat_files.csv", "estat de cada fila (CSV)")]
    links = "".join(f'<li>{enllac_ext(f"{GH_BLOB}/{d}", d)} · {esc(t)}</li>' for d, t in docs)
    return (f'<dl class="versio-dl"><div><dt>Commit de <code>main</code></dt><dd><code class="sha">{esc(ctx.commit)}</code></dd></div>'
            f'<div><dt>Data</dt><dd>{esc(data_ca(ctx.data_commit))}</dd></div>{dl}</dl>'
            '<p class="nota">SHA-256 comprovats contra <code>MANIFEST_SHA256.csv</code> en generar el lloc. El generador també comprova '
            "que <code>estat/RESUM_ESTAT.md</code> correspon a la base, al registre, a <code>PENDENTS.md</code> i a "
            "<code>estat/dubtes_tancats.csv</code> actuals, i s'atura si les xifres no quadren.</p>"
            f'<ul class="docs">{links}</ul>')


def seccio(id_: str, titol: str, resposta: str, cos: str, cls: str = "") -> str:
    return (f'<section class="bloc{(" " + cls) if cls else ""}" id="{id_}" aria-labelledby="h-{id_}">'
            f'<h2 id="h-{id_}">{esc(titol)}</h2>{resposta}{cos}</section>')


REDIRECCIO_HASH = ("<script>(function(){var h=location.hash;"
                   "if(/^#(?:.*&)?(?:q|e|c|p|s|v|t|m)=/.test(h)){location.replace('empreses.html'+h);}})();</script>\n")


def pagina_estat(ctx: Context, E: dict) -> str:
    tot = E["tot"]
    cat = E["cat"]
    acab = cat["acabada"]
    # 3. Quantes files estan acabades
    segs = [(k, cat[k], ESTATS[k][1]) for k in ORDRE_ESTATS]
    if acab:
        heroi = (f'<p class="heroi-xifra"><b>{fmt_int(acab)}</b> de {fmt_int(tot)} files acabades '
                 f'<span>({fmt_pct(acab, tot)})</span></p>')
    else:
        heroi = '<p class="heroi-xifra">Encara cap fila no compleix les quatre condicions.</p>'
    acabades = (heroi + barra_apilada(segs, tot, "Files segons l'estat", "s")
                + llegenda_estats(cat, tot)
                + '<p class="nota">Cada fila compta en un sol estat: el primer pas de l\'embut que no supera.</p>')
    # 4. Embut
    detall = (f'<p class="nota">C1 CEO {fmt_int(E["c1"])} ({fmt_pct(E["c1"], tot)}) · C2 fundador {fmt_int(E["c2"])} '
              f'({fmt_pct(E["c2"], tot)}), de les quals {fmt_int(E["columna_antiga"])} només amb la cita antiga de la base '
              "(sense còpia arxivada).</p>")
    # 5. Etiquetes
    F = E["per_etiq"]["F"]
    resp_etiq = (f'<p class="resposta">Per exemple, de les {fmt_int(F["files"])} files F, {fmt_pct(F["C2"], F["files"])} tenen prova de fundador '
                 f'però {fmt_pct(F["C3"], F["files"])} tenen la cita verificada a la còpia de Wayback; acabades: {fmt_int(F["acabada"])}.</p>')
    # 6. Mapa de calor
    anys = list(E["per_any"])
    millor = max(anys, key=lambda a: (E["per_any"][a]["acabada"] / E["per_any"][a]["total"], -a)) if anys else None
    resp_any = ""
    if millor is not None:
        c = E["per_any"][millor]
        resp_any = (f'<p class="resposta">L\'any amb més files acabades és el {millor}: {fmt_int(c["acabada"])} de {fmt_int(c["total"])} '
                    f'({fmt_pct(c["acabada"], c["total"])}).</p>')
    # 7. Mancances
    resp_m = (f'<p class="resposta">La mancança més freqüent és «{esc(MANCANCES[E["mancances"].most_common(1)[0][0]][0])}»: '
              f'{fmt_int(E["mancances"].most_common(1)[0][1])} files.</p>' if E["mancances"] else
              '<p class="resposta">No hi ha cap mancança.</p>')
    nota_m = '<p class="nota">Una fila pot tenir més d\'una mancança.</p>'
    # 8. Dubtes
    resp_d = (f'<p class="resposta">{fmt_int(E["files_amb_dubte"])} files tenen algun dubte obert. Dubtes tancats: <b>{fmt_int(E["dubtes_tancats"])}</b>.</p>'
              if E["dubtes"] else "")
    nota_d = ('<p class="nota">Una fila pot tenir dubtes de més d\'un origen. Aquí només es compten les files: el text dels dubtes '
              f'és a {enllac_ext(f"{GH_BLOB}/PENDENTS.md", "PENDENTS.md")}, a GitHub.</p>') if E["dubtes"] else ""
    # 10. Resultats provisionals
    et = E["etiq"]
    segs_e = [(l, et[l], f"{l} · {NOM_ETIQ[l]}") for l in ["F", "P", "NA", "ND"]]
    ll_e = "".join(f'<li><span class="sw e-{l}" aria-hidden="true">{l}</span><b>{esc(NOM_ETIQ[l])}</b> '
                   f'<span class="ll-n">{fmt_int(et[l])} · {fmt_pct(et[l], tot)}</span></li>' for l in ["F", "P", "NA", "ND"])
    resultats = (barra_apilada(segs_e, tot, "Files segons l'etiqueta FounderCEO", "e")
                 + f'<ul class="ll-etiq">{ll_e}</ul>' + grafic_f_per_any(E))

    cos = f"""<section class="cap-estat">
<h1>En quin punt és la base</h1>
<p class="entradeta">{fmt_int(tot)} files empresa-any ({fmt_int(E["n_isin"])} empreses, 2016–2025). Per a cada fila: qui era el CEO el 31 d'octubre i si era fundador, amb una cita literal, l'URL original i una còpia a Wayback Machine.</p>
{linia_versio(ctx)}
</section>
<form class="cerca-rapida" action="empreses.html" method="get" role="search">
<label for="q">Busca una empresa (nom, ISIN o CEO)</label>
<div class="cr-fila"><input type="search" id="q" name="q" autocomplete="off" placeholder="p. ex. Nestlé, DE000A0D9PT0, Arora…"><button type="submit" class="boto">Cerca</button></div>
</form>
{seccio("acabades", "Quantes files estan acabades?", "", acabades)}
{seccio("embut", "On es queden les files?", "", embut(E) + detall)}
{seccio("etiquetes", "Com està cada etiqueta?", resp_etiq, taula_etiquetes(E))}
{seccio("anys", "Com va cada any?", resp_any, mapa_calor(E))}
{seccio("mancances", "Què falta i què s'hi fa?", resp_m, nota_m + barres_mancances(E))}
{seccio("dubtes", "D'on venen els dubtes oberts?", resp_d, barres_dubtes(E, ctx.pend) + nota_d)}
{seccio("qualitat", "Com es controla la qualitat?", '<p class="resposta">Cada cita passa per cinc controls abans de comptar com a acabada.</p>', passos_qualitat(E))}
{seccio("resultats", "Resultats provisionals", '<p class="resposta etiqueta-prov">Provisional: pot canviar fins a ' + nom_versio() + '.</p>', resultats)}
{seccio("versio", "Sobre aquestes dades", linia_versio(ctx), sobre_dades(ctx), "versio")}"""
    return pagina(ctx, titol="Estat de la base · Fundadors-CEO STOXX Europe 600",
                  descripcio="En quin punt és la base Fundadors-CEO: files acabades, embut, mancances, dubtes i control de qualitat.",
                  cos=cos, prefix="", actiu="estat", cap_extra=REDIRECCIO_HASH, cls_body="p-estat")


# ---------------------------------------------------------------------------
# Empreses
# ---------------------------------------------------------------------------

LLETRA_ESTAT = {"acabada": "a", "arxiu": "r", "dubte": "d", "falta": "f"}


def text_estat_empresa(e: dict) -> str:
    n = len(e["files"])
    parts = [f'{fmt_int(e["st"]["acabada"])} de {fmt_int(n)} files acabades']
    for k, sing, plur in (("arxiu", "només falta l'arxiu", "només falten l'arxiu"),
                          ("dubte", "amb dubte", "amb dubte"),
                          ("falta", "falta evidència", "falta evidència")):
        v = e["st"][k]
        if v:
            parts.append(f"{fmt_int(v)} {sing if v == 1 else plur}")
    return " · ".join(parts)


def pagina_empreses(ctx: Context, model: dict, E: dict) -> str:
    emp = model["empreses"]
    paisos = Counter((e["pais_codi"], e["pais"]) for e in emp.values())
    opt_pais = "".join(
        f'<option value="{esc(codi)}">{esc(nom)} · {esc(codi)} ({fmt_int(n)})</option>'
        for (codi, nom), n in sorted(paisos.items(), key=lambda x: clau_ordre(x[0][1]))
    )
    etq_emp = Counter(l for e in emp.values() for l in ORDRE_ETIQ if e["recompte"][l])
    opt_etiq = "".join(f'<option value="{l}">Amb algun any {l} · {esc(NOM_ETIQ_MIN[l])} ({fmt_int(etq_emp[l])})</option>'
                       for l in ORDRE_ETIQ)
    st_emp = Counter(k for e in emp.values() for k in ORDRE_ESTATS if e["st"][k])
    opt_estat = "".join(f'<option value="{k}">Amb alguna fila: {esc(ESTATS[k][1].lower())} ({fmt_int(st_emp[k])})</option>'
                        for k in ORDRE_ESTATS)
    opt_estat += f'<option value="totes">Totes les files acabades ({fmt_int(E["emp_totes_acabades"])})</option>'
    noms_m = "".join(f'<option value="{k}">{esc(v[0])}</option>' for k, v in MANCANCES.items())

    files_html = []
    for e in sorted(emp.values(), key=lambda e: (clau_ordre(e["nom"]), e["isin"])):
        per_any = {f["any"]: f for f in e["files"]}
        cel = []
        for a in ANYS_PANELL:
            f = per_any.get(a)
            cel.append(f'<i class="{f["lletra"]} {LLETRA_ESTAT[f["cat"]]}">{f["lletra"]}</i>' if f else "<i></i>")
        r = e["recompte"]
        n = len(e["files"])
        st = e["st"]
        etiq_txt = ", ".join(f"{l} {r[l]} de {n} anys" for l in ORDRE_ETIQ if r[l])
        st_txt = ", ".join(f"{st[k]} {ESTATS[k][1].lower()}" for k in ORDRE_ESTATS if st[k])
        aria = f"{etiq_txt}; {st_txt}"
        darrer = e["files"][-1]
        ceo_darrer = darrer["ceos_text"].replace("|", " · ") or "sense CEO"
        cerca = norm_cerca(" ".join([e["nom"], *e["altres_noms"], e["isin"], *e["ceos_noms"]]))
        pa = round(100 * st["acabada"] / n) if n else 0
        files_html.append(
            f'<tr data-c="{esc(cerca)}" data-e="{" ".join(l for l in ORDRE_ETIQ if r[l])}" '
            f'data-st="{" ".join(str(st[k]) for k in ORDRE_ESTATS)}" data-m="{" ".join(e["mancances"])}" '
            f'data-p="{e["pais_codi"]}" data-n="{esc(clau_ordre(e["nom"]))}" data-f="{r["F"]}" data-pa="{pa}">'
            f'<td><a href="empreses/{e["isin"]}.html">{esc(e["nom"])}</a>'
            f'<span class="sub"><code>{e["isin"]}</code> · CEO {darrer["any"]}: {esc(ceo_darrer)}</span></td>'
            f'<td><span class="sr" role="img" aria-label="{esc(aria)}">{"".join(cel)}</span></td>'
            f'<td>{minibarra_estat(st, n)}<span class="sub">{st["acabada"]}/{n} acabades</span></td>'
            f'<td class="num">{r["F"] or ""}</td></tr>'
        )
    ll_etq = "".join(f'<span class="ll"><i class="sw e-{l}" aria-hidden="true">{l}</i>{esc(NOM_ETIQ_MIN[l])}</span>' for l in ORDRE_ETIQ)
    ll_st = "".join(f'<span class="ll"><i class="sw-ratlla s-{k}" aria-hidden="true"></i>'
                    f'<span aria-hidden="true">{ESTATS[k][0]}</span> {esc(ESTATS[k][1].lower())}</span>' for k in ORDRE_ESTATS)
    n_emp = len(emp)
    cos = f"""<section class="cap-pagina">
<h1>Empreses</h1>
<p class="entradeta">{fmt_int(n_emp)} empreses i {fmt_int(model["n_files"])} files. Cerca per nom, ISIN o CEO, o filtra per etiqueta i estat.</p>
</section>
<form class="filtres" id="filtres" role="search" onsubmit="return false">
<label class="camp camp-cerca"><span>Cerca per nom, ISIN o CEO</span><input type="search" id="f-q" placeholder="p. ex. Nestlé, DE000A0D9PT0, Arora…" autocomplete="off"></label>
<label class="camp"><span>Etiqueta</span><select id="f-e"><option value="">Totes</option>{opt_etiq}</select></label>
<label class="camp"><span>Estat</span><select id="f-t"><option value="">Tots</option>{opt_estat}</select></label>
<label class="camp"><span>País d'emissió de l'ISIN <small>(derivat)</small></span><select id="f-p"><option value="">Tots</option>{opt_pais}</select></label>
<label class="camp camp-m" id="camp-m" hidden><span>Mancança</span><select id="f-m"><option value="">Totes</option>{noms_m}</select></label>
<button type="button" class="boto-sec" id="f-reset">Esborra els filtres</button>
</form>
<p class="recompte" aria-live="polite">Es mostren <b id="n-visibles">{fmt_int(n_emp)}</b> de {fmt_int(n_emp)} empreses</p>
<div class="llegenda"><span class="ll-cap">Etiqueta:</span>{ll_etq}<span class="ll-cap">Estat (franja inferior):</span>{ll_st}<a class="ll-ajuda" href="metodologia.html#llegenda" aria-label="Què vol dir cada etiqueta i cada estat">?</a></div>
<div class="taula-wrap">
<table class="taula-emp" id="taula">
<caption class="vh">Empreses, sèrie FounderCEO 2016–2025 i estat de les files</caption>
<thead><tr>
<th scope="col"><button type="button" data-ordre="n" aria-sort="ascending">Empresa</button></th>
<th scope="col">Sèrie 2016–2025</th>
<th scope="col"><button type="button" data-ordre="pa">Estat</button></th>
<th scope="col" class="num"><button type="button" data-ordre="f">Anys F</button></th>
</tr></thead>
<tbody>
{chr(10).join(files_html)}
</tbody>
</table>
</div>
<div class="sense-resultat" id="cap-resultat" hidden><p>Cap empresa no coincideix amb la cerca i els filtres.</p><button type="button" class="boto-sec" id="f-reset-2">Esborra els filtres</button></div>
<p class="nota">El país d'emissió es deriva del prefix de l'ISIN (GB, FR, DE…): no és la seu social ni un camp de la base. Els filtres d'etiqueta i d'estat mostren les empreses amb almenys una fila amb aquell valor.</p>"""
    return pagina(ctx, titol="Empreses · Fundadors-CEO STOXX Europe 600",
                  descripcio="Cerca i filtra les 1.040 empreses de la base: sèrie FounderCEO 2016-2025 i estat de les files.",
                  cos=cos, prefix="", actiu="empreses", scripts=("cerca.js",), ample=True, cls_body="p-empreses")


# ---------------------------------------------------------------------------
# Fitxa d'empresa
# ---------------------------------------------------------------------------


def linia_temps(e: dict) -> str:
    per_any = {f["any"]: f for f in e["files"]}
    anys_cel, cels, estats = [], [], []
    for i, a in enumerate(ANYS_PANELL, start=1):
        f = per_any.get(a)
        if f:
            anys_cel.append(f'<a class="tl-any" style="grid-column:{i}" href="#any-{a}">{a}</a>')
            ceo = f["ceos_text"].replace("|", " · ") or "sense CEO"
            a_txt = str(a)
            cels.append(f'<span class="tl-cel" style="grid-column:{i}">{cel_etiq(f["lletra"], a_txt + " · " + f["etiqueta"] + " · " + ceo)}</span>')
            icona, nom, _, _ = ESTATS[f["cat"]]
            estats.append(f'<a class="tl-st st-{f["cat"]}" style="grid-column:{i}" href="#any-{a}" title="{a}: {esc(nom)}">'
                          f'<span aria-hidden="true">{icona}</span><span class="vh">{a}: {esc(nom)}</span></a>')
        else:
            anys_cel.append(f'<span class="tl-any" style="grid-column:{i}">{a}</span>')
            cels.append(f'<span class="tl-cel" style="grid-column:{i}">{cel_buida(f"{a}: no és al panell")}</span>')
            estats.append(f'<span class="tl-st tl-st-buit" style="grid-column:{i}"></span>')
    trams = []
    for i, a in enumerate(ANYS_PANELL, start=1):
        f = per_any.get(a)
        if not f:
            continue
        clau = f["ceos_text"]
        if trams and trams[-1]["clau"] == clau and trams[-1]["fi"] == a - 1:
            trams[-1]["fi"] = a
            trams[-1]["span"] += 1
            trams[-1]["files"].append(f)
        else:
            trams.append({"clau": clau, "ini": a, "fi": a, "col": i, "span": 1, "ceos": f["ceos"], "files": [f]})
    noms, llista = [], []
    for t in trams:
        nom = " · ".join(t["ceos"]) if t["ceos"] else "Sense CEO"
        rang = str(t["ini"]) if t["ini"] == t["fi"] else f"{t['ini']}–{t['fi']}"
        lletres = {f["lletra"] for f in t["files"]}
        cls = "tl-ceo" + (" tl-ceo-buit" if not t["ceos"] else "") + (f" v-{next(iter(lletres))}" if len(lletres) == 1 else "")
        noms.append(f'<span class="{cls}" style="grid-column:{t["col"]} / span {t["span"]}" title="{esc(nom)} · {rang}">'
                    f'<b>{esc(nom)}</b><small>{rang}</small></span>')
        cels_t = "".join(
            f'<a class="cel cel-p e-{f["lletra"]} b-{f["cat"]}" href="#any-{f["any"]}" title="{f["any"]} · {f["lletra"]} · {esc(ESTATS[f["cat"]][1])}">'
            f'{f["lletra"]}<span class="vh"> {f["any"]}: {esc(ESTATS[f["cat"]][1])}</span></a>' for f in t["files"])
        llista.append(f'<li class="{cls.replace("tl-ceo", "tram")}"><span class="tram-anys">{rang}</span>'
                      f'<b class="tram-nom">{esc(nom)}</b><span class="serie">{cels_t}</span></li>')
    return ('<div class="tl-wrap"><div class="tl" role="group" aria-label="CEO, etiqueta i estat per any">'
            f'<div class="tl-fila">{"".join(anys_cel)}</div>'
            f'<div class="tl-fila">{"".join(cels)}</div>'
            f'<div class="tl-fila tl-fila-st">{"".join(estats)}</div>'
            f'<div class="tl-fila tl-fila-ceo">{"".join(noms)}</div>'
            "</div></div>"
            f'<ol class="trams" aria-label="CEO per períodes">{"".join(llista)}</ol>')


def html_cita(text: str, ident: str, maxim: int = LONGITUD_MAX_CITA) -> str:
    if not text:
        return '<p class="sense-cita">Aquesta entrada no té cita literal.</p>'
    if len(text) <= maxim:
        return f'<blockquote class="cita"><p>{esc(text)}</p></blockquote>'
    tall = text[:maxim]
    m = list(re.finditer(r"[.;:!?](\s|$)", tall))
    if m and m[-1].end() > maxim * 0.5:
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


def insignies_prova(p: dict) -> list[str]:
    b = []
    if "[V]" in p["veritat"]:
        b.append('<span class="b b-v" title="marca_veritat = [V]: document obert sencer i cita trobada">[V]</span>')
    if "[NV]" in p["veritat"]:
        b.append('<span class="b b-nv" title="marca_veritat = [NV]: no verificada">[NV]</span>')
    if p["no_valida"]:
        b.append('<span class="b b-mal" title="La nota de l\'entrada diu no_valida">Font no vàlida</span>')
    elif p["capt_si"]:
        b.append('<span class="b b-v" title="cita_verificada_a_captura = si">Cita comprovada a la còpia</span>')
    elif p["pendent_arxiu"]:
        b.append('<span class="b b-nv" title="La nota diu pendent_arxiu (abans pendent_DF)">Pendent d\'arxiu</span>')
    for m in p["marca_prova"]:
        if len(m) <= 14:
            b.append(f'<span class="b b-marca" title="marca_prova">{esc(m)}</span>')
    for o, ocult in p["origen_pub"]:
        if not ocult and re.fullmatch(r"Nivell [ABC]", o):
            b.append(f'<span class="b b-nivell" title="origen_cita">Font {esc(o[-1])}</span>')
    return b


def wayback_prova(p: dict) -> tuple[str, str]:
    """(URL de la còpia, data) o ("", motiu)."""
    if p["wb_urls"]:
        u = p["wb_urls"][0]
        return u, data_wayback(ts_de_url_wayback(u))
    if p["wb_extra"]:
        return p["wb_extra"]["url"], data_wayback(p["wb_extra"]["timestamp"] or ts_de_url_wayback(p["wb_extra"]["url"]))
    if p["wb_pendent"]:
        return "", "pendent de verificació externa"
    return "", "encara no"


def botons_fonts(p: dict) -> str:
    url = url_segura(p["url"])
    fonts = []
    if url:
        fonts.append(enllac_ext(url, f"Font original · {domini(url)}", "boto"))
    elif p["url"]:
        fonts.append(f'<span class="domini">URL no vàlida: {esc(p["url"])}</span>')
    else:
        fonts.append('<span class="boto boto-off">Sense URL de la font</span>')
    for u in p["wb_urls"]:
        d = data_wayback(ts_de_url_wayback(u))
        fonts.append(enllac_ext(u, "Còpia Wayback" + (f" · {d}" if d else ""), "boto boto-wb"))
    if not p["wb_urls"]:
        wu, d = wayback_prova(p)
        if wu:
            fonts.append(enllac_ext(wu, "Còpia Wayback (fitxer extra)" + (f" · {d}" if d else ""), "boto boto-wb"))
        else:
            fonts.append(f'<span class="boto boto-off">Còpia Wayback: {esc(d)}</span>')
    return f'<div class="p-fonts">{"".join(fonts)}</div>'


def html_prova(p: dict) -> str:
    anys_attr = " ".join(str(a) for a in p["anys"])
    funcions = [FUNCIONS.get(f, f) for f in p["funcio"]] or ["(buida)"]
    if p["ocult"]:
        motiu = ("Prova de la classificació sectorial: el sector no es mostra en aquesta versió, pendent d'aclarir-ne la llicència."
                 if p["ocult"] == "sector" else
                 "La cita o l'URL contenen un terme de la llista restringida (columnes o documents interns).")
        return (f'<article class="prova prova-oculta" id="{p["ancora"]}" data-anys="{anys_attr}">'
                f'<header class="p-cap"><span class="b b-gris">Prova no mostrada</span><code>{esc(p["id"])}</code>'
                f'<span class="mini">{esc(", ".join(funcions))}</span>{anys_html(p)}</header>'
                f"<p>{motiu} Criteri de la part pública; l'entrada consta al registre.</p></article>")
    llargues = [m for m in p["marca_prova"] if len(m) > 14]
    curtes = [m for m in p["marca_prova"] if len(m) <= 14]
    m = [meta("Identificador", f'<code>{esc(p["id"])}</code>'),
         meta("Funció (funcio_cita)", llista_valors(p["funcio"]) if p["funcio"] else
              f'<span class="buit">buida</span> · agrupada pel tipus {llista_valors(p["tipus"])}'),
         meta("Tipus d'entrada", llista_valors(p["tipus"]))]
    if p["marca_prova"]:
        if llargues:
            items = "".join(f"<li><code>{esc(x)}</code></li>" for v in llargues for x in v.split(";") if x.strip())
            m.append(meta("Marca de prova", (llista_valors(curtes) + " " if curtes else "") + f'<ul class="llista-codi">{items}</ul>'))
        else:
            m.append(meta("Marca de prova", llista_valors(curtes)))
    m.append(meta("Marca de veritat", llista_valors(p["veritat"])))
    m.append(meta("Allotjament", llista_valors(p["allotjament"])))
    orig = ['<span class="buit">valor no mostrat (criteri de la part pública)</span>' if oc else f"<code>{esc(o)}</code>"
            for o, oc in p["origen_pub"]]
    m.append(meta("Origen de la cita", " ".join(orig) if orig else '<span class="buit">—</span>'))
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
                  ", ".join(esc(capt.get(c, c)) for c in p["capt"]) if p["capt"] else '<span class="buit">pendent</span>'))
    notes = []
    for n, motiu in p["notes_pub"]:
        if motiu:
            notes.append('<p class="nota-oculta">Nota no mostrada: conté noms de models o referències internes '
                         "(criteri de la part pública).</p>")
        else:
            notes.append(f"<p>{esc(n)}</p>")
    notes_html = f'<div class="p-notes"><h4>Notes</h4>{"".join(notes)}</div>' if notes else ""
    cls = "prova"
    if "[V]" not in p["veritat"]:
        cls += " prova-nv"
    if p["no_valida"]:
        cls += " prova-mal"
    return (f'<article class="{cls}" id="{p["ancora"]}" data-anys="{anys_attr}">'
            f'<header class="p-cap">{"".join(insignies_prova(p))}{anys_html(p)}</header>'
            f'{html_cita(p["cita"], p["id"])}{botons_fonts(p)}'
            f'<details class="tecnic"><summary>Detalls tècnics</summary><dl class="p-meta">{"".join(m)}</dl>{notes_html}</details>'
            "</article>")


def html_cita_base(d: dict, idx: int) -> str:
    anys_attr = " ".join(str(a) for a in d["anys"])
    rang = esc(comprimeix_anys(d["anys"]))
    origen = "base (font_classificacio)" if d["tipus"] == "font_classificacio" else "base (d37)"
    if d["ocult"]:
        return (f'<article class="prova prova-oculta" id="b-{idx}" data-anys="{anys_attr}"><header class="p-cap">'
                f'<span class="b b-gris">Prova no mostrada</span><span class="p-anys">{rang}</span></header>'
                f"<p>Cita de la {esc(origen)} no mostrada (terme de la llista restringida).</p></article>")
    if d["tipus"] == "font_classificacio":
        cita = html_cita(d["cita"], f"font_classificacio_cita ({rang})")
    elif d["cita"] and d["cita"].lower() in {"si", "no", "si_cita_alternativa"}:
        cita = (f'<p class="sense-cita">El CSV no conté text literal d\'aquesta cita. Indicador '
                f'<code>d37_cita_contemporania</code> = <code>{esc(d["cita"])}</code>.</p>')
    else:
        cita = html_cita(d["cita"], f"d37_cita_contemporania ({rang})")
    url = url_segura(d["url"])
    fonts = [enllac_ext(url, f"Font original · {domini(url)}", "boto") if url else '<span class="boto boto-off">Sense URL de la font</span>',
             '<span class="boto boto-off">Còpia Wayback: sense còpia arxivada</span>']
    m = [meta("Origen", f"<code>{esc(origen)}</code>")]
    if d["tipus"] == "d37" and d["dada"]:
        m.append(meta("Data de la cita (d37_cita_contemp_data)", esc(d["dada"])))
    if d["tipus"] == "font_classificacio":
        m.append(meta("Registre", ("La mateixa cita i URL també consten al registre: " + llista_valors(d["ids_registre"]))
                      if d["ids_registre"] else "No consta al registre amb el mateix text i URL."))
    return (f'<article class="prova prova-base" id="b-{idx}" data-anys="{anys_attr}">'
            f'<header class="p-cap"><span class="b b-gris">Cita de la base</span><span class="p-anys" title="Anys en què el camp té aquest valor">{rang}</span></header>'
            f'{cita}<div class="p-fonts">{"".join(fonts)}</div>'
            f'<details class="tecnic"><summary>Detalls tècnics</summary><dl class="p-meta">{"".join(m)}</dl></details></article>')


def regla_html(tok: str, prefix: str = "../") -> str:
    if tok in REGLES_TEXT:
        anc = REGLA_ANCORA.get(tok, tok)
        if tok == "cap":
            return f'<span class="regla regla-cap" title="cap: sense regla registrada">{esc(REGLES_TEXT[tok])}</span>'
        return f'<a class="regla" href="{prefix}metodologia.html#regla-{slug(anc)}">{esc(REGLES_TEXT[tok])}</a>'
    return f'<a class="regla" href="{prefix}metodologia.html#regla-{slug(tok)}"><code>{esc(tok)}</code></a>'


def primer_id(ids: str) -> list[str]:
    return [i for i in (ids or "").split(";") if i and not i.startswith("(+") and i != "(sense id)"]


SEP_CADENA = ' <span aria-hidden="true">→</span> '


def resum_prova_any(p: dict | None, ident: str, titol: str) -> str:
    """Bloc de «Per què?» per a una prova: marca, cita curta, font, còpia i comprovació."""
    if p is None:
        return (f'<div class="pq-bloc"><h4>{esc(titol)}</h4><p class="mini">Identificador <code>{esc(ident)}</code> '
                "(no trobat entre les proves d'aquesta empresa).</p></div>")
    if p["ocult"]:
        return (f'<div class="pq-bloc"><h4>{esc(titol)}</h4><p class="sense-cita">Prova no mostrada (criteri de la part pública) · '
                f'<code>{esc(p["id"])}</code></p></div>')
    wu, d = wayback_prova(p)
    comprovada = "sí" if p["capt_si"] else ("no" if "no" in p["capt"] else "pendent")
    cadena = [enllac_ext(p["url"], f"Font original · {domini(p['url'])}") if url_segura(p["url"]) else '<span class="buit">Sense URL de la font</span>',
              enllac_ext(wu, f"Còpia Wayback · {d}" if d else "Còpia Wayback") if wu else f'<span class="buit">Còpia Wayback: {esc(d)}</span>',
              f'<span class="{"ok" if comprovada == "sí" else "buit"}">Cita comprovada a la còpia: {comprovada}</span>']
    return (f'<div class="pq-bloc"><h4>{esc(titol)} <span class="pq-ins">{"".join(insignies_prova(p))}</span></h4>'
            f'{html_cita(p["cita"], p["id"], 320)}'
            f'<p class="pq-cadena">{SEP_CADENA.join(cadena)}</p>'
            f'<p class="mini"><a href="#{p["ancora"]}">Veure la prova</a> · <code>{esc(p["id"])}</code></p></div>')


def any_per_any(e: dict, index_proves: dict[str, dict], pend: dict) -> str:
    files = []
    for f in e["files"]:
        a = f["any"]
        est = f["est"]
        if f["ceos"]:
            ceo = " · ".join(esc(c) for c in f["ceos"])
        else:
            ceo = '<span class="buit">Sense CEO</span>'
        regles = f["regles"] or ["cap"]
        if len(regles) > 1 and "cap" in regles:
            regles = [t for t in regles if t != "cap"] + ["cap"]
        prova = " ".join(regla_html(t) for t in regles)
        # «Per què?»
        blocs = []
        es_na = f["lletra"] == "NA"
        t_ceo = "Documentació de la fila sense CEO (R-SC)" if es_na else "Cita de CEO"
        ids1 = primer_id(est["c1_ids"])
        if est["c1_ceo"] in ("ok", "rsc_documentat") and ids1:
            if est["c1_tipus"] == "interval":
                ext = [i for i in ids1 if index_proves.get(i) and any("interval" in m for m in index_proves[i]["marca_prova"])][:2] or ids1[:2]
                def extrem(i: str) -> str:
                    notes = " ".join(index_proves[i]["notes"]).lower() if index_proves.get(i) else ""
                    return "inici" if re.search(r"\binici\b", notes) else ("final" if re.search(r"\bfinal\b", notes) else "")
                ext.sort(key=lambda i: {"inici": 0, "": 1, "final": 2}[extrem(i)])
                for n_, i in enumerate(ext, start=1):
                    nom_ext = {"inici": "inici (nomenament)", "final": "final"}.get(extrem(i), f"extrem {n_}")
                    blocs.append(resum_prova_any(index_proves.get(i), i, f"Cita de CEO per interval · {nom_ext}"))
                blocs.append('<p class="mini">Limitació declarada: a les files amb <code>ceo_interval</code> no s\'ha verificat '
                             "l'absència de canvis de CEO entre els dos extrems.</p>")
            else:
                blocs.append(resum_prova_any(index_proves.get(ids1[0]), ids1[0], t_ceo))
        else:
            blocs.append(f'<p class="falta-txt">Falta: {"documentació de la fila sense CEO" if es_na else "cita de CEO"}.</p>')
        ids2 = primer_id(est["c2_ids"])
        t_f = "Documentació de la cerca" if f["lletra"] in ("NA", "ND") else "Prova de fundador"
        if est["c2_fundador"] == "ok_columna_antiga":
            d = next((d for d in e["cites_base"] if d["tipus"] == "font_classificacio" and a in d["anys"]), None)
            if d and not d["ocult"]:
                url = url_segura(d["url"])
                blocs.append(f'<div class="pq-bloc"><h4>{t_f} <span class="pq-ins"><span class="b b-gris">Cita de la base</span></span></h4>'
                             f'{html_cita(d["cita"], "font_classificacio_cita", 320)}'
                             f'<p class="pq-cadena">{enllac_ext(url, "Font original · " + domini(url)) if url else ""} '
                             '<span class="buit">· sense còpia arxivada</span></p></div>')
            else:
                blocs.append(f'<div class="pq-bloc"><h4>{t_f}</h4><p class="sense-cita">Prova no mostrada (criteri de la part pública) · '
                             "<code>font_classificacio_cita</code></p></div>")
        elif est["c2_fundador"] in ("ok_registre", "rsc_documentat", "cerca_documentada") and ids2:
            blocs.append(resum_prova_any(index_proves.get(ids2[0]), ids2[0], t_f))
        else:
            blocs.append('<p class="falta-txt">Falta: prova de fundador.</p>')
        if est["c4_coherencia"] != "ok":
            probs = [PROBLEMES_C4.get(x, x) for x in est["c4_coherencia"].split(";") if x]
            blocs.append(f'<p class="falta-txt">No quadra amb la base: {esc(" ".join(probs))}</p>')
        for dub in f["dubtes"]:
            nom = ORIGENS_DUBTE.get(dub, (dub, ""))[0]
            url = url_pendents(pend, dub, f"l10-{e['isin'].lower()}-{a}" if dub == "lot10" else None)
            blocs.append(f'<p class="falta-txt">Dubte obert ({esc(nom)}): {enllac_ext(url, "PENDENTS.md")}</p>')
        if "carrec_no_detectat_a_la_cita" in est["avisos"]:
            blocs.append('<p class="mini">Avís (no bloqueja): el càrrec no es detecta automàticament a la cita de CEO.</p>')
        n_proves = sum(a in p["anys"] for p in e["proves"]) + sum(a in d["anys"] for d in e["cites_base"])
        blocs.append(f'<p class="pq-totes"><a href="#proves" data-filtre-any="{a}">Totes les proves d\'aquest any ({n_proves})</a></p>')
        files.append(
            f'<details class="any" id="any-{a}"><summary>'
            f'<span class="a-any">{a}</span>'
            f'<span class="a-ceo"><span class="vh">CEO a 31/10: </span>{ceo}</span>'
            f'<span class="a-etq"><span class="vh">Etiqueta: </span>{badge_etiq(f["lletra"])}</span>'
            f'<span class="a-prova"><span class="vh">Prova: </span>{" · ".join(esc(REGLES_TEXT.get(t, t)) for t in regles)}</span>'
            f'<span class="a-st"><span class="vh">Estat: </span>{insignia_estat(f["cat"])}</span>'
            f'<span class="a-pq">Per què?</span></summary>'
            f'<div class="pq"><p class="pq-regla"><b>Prova:</b> {prova}</p>{"".join(blocs)}</div></details>'
        )
    cap = ('<div class="anys-cap" aria-hidden="true"><span>Any</span><span>CEO a 31/10</span><span>Etiqueta</span>'
           '<span>Prova</span><span>Estat</span><span></span></div>')
    return f'<div class="anys">{cap}{"".join(files)}</div>'


def caixa_dubte(e: dict, pend: dict) -> str:
    per_origen: dict[str, list[int]] = defaultdict(list)
    for f in e["files"]:
        for d in f["dubtes"]:
            per_origen[d].append(f["any"])
    if not per_origen:
        return ""
    items = []
    ordre = [k for k in ORIGENS_DUBTE if k in per_origen] + sorted(k for k in per_origen if k not in ORIGENS_DUBTE)
    for k in ordre:
        anys = per_origen[k]
        nom = ORIGENS_DUBTE.get(k, (k, ""))[0]
        amb_ancora = [a for a in anys if k == "lot10" and f"l10-{e['isin'].lower()}-{a}" in pend["ancores"]]
        if amb_ancora:
            enll = ", ".join(enllac_ext(url_pendents(pend, k, f"l10-{e['isin'].lower()}-{a}"), str(a)) if a in amb_ancora else str(a)
                             for a in anys)
            items.append(f"<li>Dubte obert ({esc(nom)}) per als anys {enll}. {enllac_ext(url_pendents(pend, k), 'Secció a PENDENTS.md')}</li>")
        else:
            items.append(f"<li>Dubte obert ({esc(nom)}) per als anys {esc(comprimeix_anys(anys))}. "
                         f"{enllac_ext(url_pendents(pend, k), 'Secció a PENDENTS.md')}</li>")
    return f'<aside class="caixa-dubte" role="note"><span class="cd-icona" aria-hidden="true">?</span><ul>{"".join(items)}</ul></aside>'


def historial_ia(e: dict) -> str:
    files = "".join(
        f'<tr><th scope="row">{f["any"]}</th><td>{esc(CERTIFICACIO.get(f["cert"], f["cert"]))}</td><td>{esc(f["nivell"]) or "—"}</td></tr>'
        for f in e["files"]
    )
    return ('<details class="historial"><summary>Historial de l\'auditoria IA <span class="mini">(històric: no és l\'estat de la fila)</span></summary>'
            '<p class="nota">Valors de <code>sim_estat_certificacio</code> i <code>sim_nivell</code> de la base. És l\'estat de l\'auditoria anterior; '
            'l\'estat actual de cada fila és el de la columna «Estat». <a href="../metodologia.html#historic">Què volen dir</a>.</p>'
            '<div class="taula-wrap"><table class="taula-simple"><caption class="vh">Historial de l\'auditoria IA per any</caption>'
            '<thead><tr><th scope="col">Any</th><th scope="col">Certificació</th><th scope="col">Nivell</th></tr></thead>'
            f"<tbody>{files}</tbody></table></div></details>")


def pagina_fitxa(ctx: Context, e: dict, anterior: dict | None, seguent: dict | None) -> str:
    n = len(e["files"])
    anys_txt = comprimeix_anys(e["anys"])
    altres = ""
    if e["altres_noms"]:
        altres = f'<p class="altres-noms">Altres noms al panell: {"; ".join(esc(x) for x in e["altres_noms"])}</p>'
    index_proves: dict[str, dict] = {}
    for p in e["proves"]:
        index_proves.setdefault(p["id"], p)

    grups = {"ceo": [], "fundador": [], "altres": []}
    for p in e["proves"]:
        grups[p["grup"]].append(html_prova(p))
    for i, d in enumerate(e["cites_base"], start=1):
        grups["fundador"].append(html_cita_base(d, i))
    titols = {
        "ceo": ("CEO", "Qui era el CEO a 31/10: nomenaments, informes anuals, intervals (ceo_interval)."),
        "fundador": ("Fundador", "Proves de l'etiqueta FounderCEO (D37, a–e…) i cites dels camps de classificació de la base."),
        "altres": ("Altres", "Context, datació de mandats, revisió de fonts i dubtes metodològics."),
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
                f'<details class="grup-proves" id="g-{clau}"><summary><span class="gp-t">{esc(t)}</span> <span class="n">{len(grups[clau])}</span></summary>'
                f'<p class="nota">{esc(desc)}</p>{"".join(grups[clau])}</details>'
            )
        intro = (f'<p class="nota">{fmt_int(len(e["proves"]))} entrades de <code>docs/REGISTRE_CANVIS.csv</code>'
                 f'{" i " + fmt_int(len(e["cites_base"])) + " cites dels camps de la base" if e["cites_base"] else ""}. '
                 "Cada prova es mostra una vegada, amb els anys que cobreix.</p>")
        proves_html = intro + filtre + "".join(seccions)
    else:
        proves_html = ('<div class="sense-proves"><p><strong>No hi ha cita estructurada en aquests fitxers d\'origen</strong> '
                       "(<code>docs/REGISTRE_CANVIS.csv</code> ni camps <code>font_classificacio_*</code> / <code>d37_*</code> de la base).</p></div>")
        if e["rastre"]:
            items = "".join(f'<li>{enllac_ext(d["url"], d["url"], "url-llarga")} <span class="mini">({esc(comprimeix_anys(d["anys"]))})</span></li>'
                            for d in e["rastre"])
            proves_html += ('<details class="rastre"><summary>Rastre secundari: URL d\'arxiu heretades, sense cita literal estructurada '
                            f'<span class="mini">({len(e["rastre"])})</span></summary>'
                            "<p class=\"nota\">Columna <code>v75_urls_arxivades</code> de la base. No és una prova tancada.</p>"
                            f'<ul class="llista-urls">{items}</ul></details>')

    nav = ['<nav class="nav-fitxes" aria-label="Altres empreses">']
    nav.append(f'<a class="ant" href="{esc(anterior["isin"])}.html"><small>← Anterior</small>{esc(anterior["nom"])}</a>' if anterior else "<span></span>")
    if seguent:
        nav.append(f'<a class="seg" href="{esc(seguent["isin"])}.html"><small>Següent →</small>{esc(seguent["nom"])}</a>')
    nav.append("</nav>")

    llegenda_tl = "".join(f'<span class="ll"><span class="cel cel-p e-{l}" aria-hidden="true">{l}</span>{esc(NOM_ETIQ_MIN[l])}</span>'
                          for l in ORDRE_ETIQ) + "".join(
        f'<span class="ll"><span class="sw s-{k}" aria-hidden="true">{ESTATS[k][0]}</span>{esc(ESTATS[k][1].lower())}</span>' for k in ORDRE_ESTATS)

    cos = f"""<p class="molla"><a href="../empreses.html">← Empreses</a></p>
<section class="fitxa-cap">
<h1>{esc(e["nom"])}</h1>
<p class="fitxa-linia"><code>{esc(e["isin"])}</code> · {esc(e["pais"])} <span class="mini">(prefix ISIN)</span> · {esc(anys_txt)} ({n} anys)</p>
{altres}
<p class="fitxa-estat">{minibarra_estat(e["st"], n, "mb mb-gran")}<span>{esc(text_estat_empresa(e))}</span></p>
</section>
{caixa_dubte(e, ctx.pend)}
<section class="seccio" id="resum" aria-labelledby="h-resum">
<h2 id="h-resum">CEO, etiqueta i estat per any</h2>
{linia_temps(e)}
<div class="llegenda">{llegenda_tl}</div>
</section>
<section class="seccio" id="anys" aria-labelledby="h-anys">
<h2 id="h-anys">Any per any</h2>
<p class="nota">CEO a 31/10 de la columna <code>ceos</code> de la base. Obre «Per què?» per veure la cita de CEO i la de fundador de l'any, amb la font original i la còpia arxivada.</p>
{any_per_any(e, index_proves, ctx.pend)}
</section>
<section class="seccio" id="proves" aria-labelledby="h-proves">
<h2 id="h-proves">Totes les proves</h2>
{proves_html}
</section>
{historial_ia(e)}
{''.join(nav)}"""
    return pagina(ctx, titol=f"{e['nom']} · {e['isin']} · Fundadors-CEO",
                  descripcio=f"Fitxa de {e['nom']} ({e['isin']}): CEO per any, FounderCEO, estat de les files i proves amb cita i font.",
                  cos=cos, prefix="../", actiu="empreses", scripts=("fitxa.js",), ample=True, cls_body="p-fitxa")


# ---------------------------------------------------------------------------
# Mètode
# ---------------------------------------------------------------------------

METODOLOGIA_COMPLETA = "docs/METODOLOGIA_3_Articles_v0.10.10.md"


def pagina_metodologia(ctx: Context, model: dict, E: dict, stats: Counter) -> str:
    met = enllac_ext(f"{GH_BLOB}/{METODOLOGIA_COMPLETA}", METODOLOGIA_COMPLETA)
    docs = [
        ("docs/METODOLOGIA.md", "Porta d'entrada a la metodologia vigent (v0.10.10)."),
        (METODOLOGIA_COMPLETA, "Text complet de la metodologia vigent."),
        ("AGENTS.md", "Instruccions de treball i annex normatiu (regles 25 a 29)."),
        ("estat/README.md", "Definició de les condicions C1-C4 i de l'estat de cada fila."),
    ]
    docs_html = "".join(f'<li>{enllac_ext(f"{GH_BLOB}/{d}", d)} · {esc(t)}</li>' for d, t in docs)

    def targeta(id_: str, cap: str, text: str) -> str:
        return f'<div class="def" id="{id_}"><div class="def-cap">{cap}</div><p>{text}</p></div>'

    et = E["etiq"]
    etiq = "".join(targeta(l, badge_etiq(l), t + f' <span class="mini">({fmt_int(et[l])} {"fila" if et[l] == 1 else "files"})</span>') for l, t in (
        ("F", "Valor <code>1</code>. El CEO a 31/10 d'aquell any és fundador o cofundador de l'empresa cotitzada o d'una entitat rellevant (per exemple, una predecessora documentada), segons les regles de la metodologia."),
        ("P", "Valor <code>0</code>. El CEO no és fundador. Cal una prova positiva amb cita (proves a–e); si no n'hi ha, no es posa 0."),
        ("ND", "Valor <code>no_determinat</code>. Hi ha un CEO identificat però cap prova concloent de sí ni de no, o les proves es contradiuen."),
        ("NA", "Valor <code>NA_sense_ceo</code>. Un cop aplicades les regles R1-R3, a 31/10 no hi ha cap CEO individual (R-SC)."),
    ))
    estats = "".join(targeta(k, insignia_estat(k), esc(ESTATS[k][3])) for k in ORDRE_ESTATS)
    precedencia = ("<ol class='prec'><li>Si a la fila li falta la cita de CEO o la de fundador → <b>Falta evidència</b>.</li>"
                   "<li>Si no, si té un dubte obert o no quadra amb la base → <b>Amb dubte o incoherència</b>.</li>"
                   "<li>Si no, si li falta la cita verificada a la còpia de Wayback → <b>Només falta l'arxiu</b>.</li>"
                   "<li>Si no → <b>Acabada</b>.</li></ol>")
    marques = "".join([
        targeta("V", '<span class="b b-v">[V]</span>', "Qui va fer l'entrada va obrir el document sencer i hi va trobar la cita literalment. "
                "És provisional fins que el flux automàtic de Wayback verifica la cita per script a la còpia arxivada."),
        targeta("NV", '<span class="b b-nv">[NV]</span>', "No s'ha pogut obrir el document sencer (bloqueig, descàrrega tallada…) o la cita no hi és. "
                "Un error d'accés no vol dir que la font sigui dolenta."),
        targeta("no-valida", '<span class="b b-mal">Font no vàlida</span>', "La nota de l'entrada diu <code>no_valida</code>: la cita no és al document, és d'un altre any o la font és C."),
        targeta("pendent-arxiu", '<span class="b b-nv">Pendent d\'arxiu</span>', "La nota diu <code>pendent_arxiu</code>, abans <code>pendent_DF</code>: el document no s'ha pogut obrir sencer i espera el flux d'arxiu."),
        targeta("comprovada", '<span class="b b-v">Cita comprovada a la còpia</span>', "<code>cita_verificada_a_captura = si</code>: la cita s'ha verificat per script a la captura de Wayback."),
        targeta("cita-base", '<span class="b b-gris">Cita de la base</span>', "Cita que només consta als camps <code>font_classificacio_*</code> o <code>d37_*</code> del CSV de la base, sense còpia arxivada."),
    ])
    fonts = "".join([
        targeta("font-original", '<span class="boto boto-mostra">Font original</span>', "L'URL del document on hi ha la cita."),
        targeta("copia-wayback", '<span class="boto boto-wb boto-mostra">Còpia Wayback</span>', "La captura d'archive.org que consta al registre. Si no n'hi ha, «encara no»; si està pendent, «pendent de verificació externa». El lloc no consulta ni completa cap captura."),
        targeta("cita-comprovada", "Cita comprovada a la còpia", "«sí» si la cita s'ha verificat per script a la captura; «no» si s'ha intentat i no s'ha pogut comprovar; «pendent» si encara no s'ha intentat."),
    ])
    condicions = "".join(f"<li><b>{c}</b> {t}</li>" for c, t in (
        ("C1 CEO.", "Hi ha una cita vàlida ([V], amb URL) amb funció CEO que anomena el CEO de la base."),
        ("C2 Fundador.", "Hi ha una cita vàlida amb funció fundador, o la cita antiga de la base amb URL."),
        ("C3 Arxiu.", "Almenys una cita de C1 i una de C2 s'han verificat per script a la còpia de Wayback."),
        ("C4 Coherència.", "L'etiqueta quadra amb la regla registrada a la base i la fila no té cap dubte obert a PENDENTS.md."),
    ))
    nivells = "".join([
        targeta("font-A", '<span class="b b-nivell">Font A</span>', "Documents de la mateixa empresa o registres oficials: informe anual, document de registre, comunicat, document presentat a un regulador."),
        targeta("font-B", '<span class="b b-nivell">Font B</span>', "Premsa econòmica de qualitat, llibres i articles acadèmics."),
        targeta("font-C", '<span class="b b-gris">Font C</span>', "Wikipedia, LinkedIn, Crunchbase, agregadors, biografies no corporatives, textos d'IA… Serveixen de pista, mai de prova."),
    ])
    pref = ("<p>Ordre de preferència: (1) informe anual o document de registre de l'emissor de l'exercici; (2) comunicat de l'emissor o canal "
            "regulat; (3) regulador o registre; (4) font B.</p>")
    sense = f"Codi de la base sense resum en aquest lloc: vegeu {met}."
    regles = [
        ("R1", "Per al CEO", "Títol de CEO o càrrec legal equivalent (Vorstandsvorsitzender, consejero delegado, PDG, directeur général…)."),
        ("R2", "Per al CEO", "CEO interí."),
        ("R2b", "Per al CEO", "Direcció col·legiada transitòria."),
        ("R3", "Per al CEO", "Persona descrita literalment com a primer executiu quan el càrrec de CEO és vacant (el president executiu, només per aquesta via)."),
        ("R-SC", "Per al CEO", "Sense CEO individual a 31/10 (NA), un cop aplicades R1-R3."),
        ("ceo_interval", "Per al CEO", "Interval: un document de nomenament amb data igual o anterior al 31/10 i un altre que anomena la persona CEO en una data igual o posterior."),
        ("D37", "De «sí»", "Cita de l'emissor que anomena la persona fundadora o cofundadora de la cotitzada, del grup o d'una predecessora documentada. A la columna <code>regles</code> també surt com a <code>cita_fundador</code>."),
        ("FT", "De «sí»", sense),
        ("D10", "De «sí»", sense),
        ("D10b_prelacio", "De «sí»", sense),
        ("a", "De «no»", "Llista tancada de fundadors en què el CEO no hi és."),
        ("b", "De «no»", "Edat: l'any de la fundació rellevant més recent, el CEO tenia menys de 18 anys."),
        ("c", "De «no»", "64 anys o més entre la fundació rellevant i l'inici del mandat, només si no hi ha dada d'edat. A la columna <code>regles</code>: <code>c_AAF64_reserva</code>."),
        ("d", "De «no»", "Incorporació tardana: el CEO entra 3 anys o més després de la fundació, amb cita de l'ocupador anterior."),
        ("e", "De «no»", "Origen no personal: l'entitat la va crear l'Estat o una altra empresa, sense persona fundadora."),
        ("d_per_part", "De «no»", sense),
        ("b_per_part", "De «no»", sense),
        ("holding_interposada", "Altres", sense),
    ]
    regles_html = "".join(
        f'<div class="def" id="regla-{slug(c)}"><div class="def-cap"><code class="b b-marca">{esc(c)}</code><span class="mini">{esc(g)}</span></div><p>{t}</p></div>'
        for c, g, t in regles
    )
    cert = "".join(
        f"<div class='def'><div class='def-cap'><span class='b b-gris'>{esc(CERTIFICACIO[c])}</span></div><p>{t}</p></div>"
        for c, t in (
            ("certificada", "L'etiqueta es va certificar dins de l'auditoria. Nivell <b>N1</b>: les dues revisions independents coincidien amb la base, amb cita A/B i sense incidències greus; <b>N2</b>: una revisió coincidia i l'altra ho deixava indeterminat; <b>doctorat</b>: per decisió de Doctorat."),
            ("certificada_ceo_pendent", "L'etiqueta era certificable, però la identitat del CEO no estava verificada."),
            ("no_certificada", "La fila era dins de l'àmbit de l'auditoria però no es va poder certificar."),
            ("fora_mostra_auditoria", "La fila no formava part de la mostra de l'auditoria i es revisa per lots."),
        )
    )
    ocults = (
        f"<li>Proves del registre no mostrades perquè la cita o l'URL contenen un terme restringit: <b>{fmt_int(stats['proves_ocultes_terme_restringit'])}</b>.</li>"
        f"<li>Notes no mostrades per termes restringits o referències internes: <b>{fmt_int(stats['notes_ocultes_terme_restringit'])}</b>; per noms de models: <b>{fmt_int(stats['notes_ocultes_nom_model'])}</b>.</li>"
        f"<li>Proves de la classificació sectorial no mostrades (sector desactivat): <b>{fmt_int(stats['proves_ocultes_sector'])}</b>.</li>"
        f"<li>Valors d'«origen de la cita» no mostrats: <b>{fmt_int(stats['origen_cita_ocult'])}</b>.</li>"
        f"<li>URL del rastre secundari no mostrades: <b>{fmt_int(stats['v75_urls_ocultes_terme_restringit'])}</b>.</li>"
    )
    cos = f"""<section class="cap-pagina">
<h1>Mètode</h1>
<p class="entradeta">Com es llegeix aquest lloc i com es decideix cada fila, en llenguatge planer. La metodologia que mana és la del repositori; aquest resum no la substitueix.</p>
</section>
<div class="text-llarg">
<section class="seccio" id="pregunta"><h2>La pregunta</h2>
<p>La unitat és l'empresa i l'any: cada ISIN de l'STOXX Europe 600 per a cada any del 2016 al 2025 ({fmt_int(model["n_files"])} files, {fmt_int(E["n_isin"])} empreses).</p>
<p>Per a cada fila, qui era el CEO el <b>31 d'octubre</b> d'aquell any. Aquesta data no es canvia.</p>
<p>I si aquell CEO era fundador de l'empresa (FounderCEO): F, P, ND o NA, sempre amb una cita literal d'una font A o B.</p>
</section>
<section class="seccio" id="llegenda"><h2>Llegenda</h2>
<h3>Etiquetes FounderCEO</h3>{etiq}
<h3>Estat de cada fila</h3>{estats}
<p>Cada fila té un sol estat, el primer pas de l'embut que no supera:</p>{precedencia}
<h3>Marques d'una prova</h3>{marques}
<h3>Fonts i còpies arxivades</h3>{fonts}
</section>
<section class="seccio" id="acabada-def"><h2>Quan una fila està acabada</h2>
<p>Quan compleix les quatre condicions i no té cap dubte obert:</p>
<ul class="condicions">{condicions}</ul>
<p class="nota">Definició completa: {enllac_ext(f"{GH_BLOB}/estat/README.md", "estat/README.md")}.</p>
</section>
<section class="seccio" id="fonts"><h2>Fonts A, B i C</h2>{nivells}{pref}</section>
<section class="seccio" id="marques"><h2>Marques de prova</h2>
<p class="nota">Codis de les columnes <code>marca_prova</code> del registre i <code>regles</code> de la base. Quan un codi no té resum aprovat en aquest lloc, remet a la metodologia.</p>
{regles_html}
</section>
<section class="seccio" id="historic"><h2>Estat antic de l'auditoria (històric)</h2>
<p>Abans de l'estat per fila, cada fila tenia un estat de certificació de l'auditoria amb IA (<code>sim_estat_certificacio</code>) i un nivell (<code>sim_nivell</code>). Es conserven a l'«Historial de l'auditoria IA» de cada fitxa, però <b>no són l'estat de la fila</b>: avui una fila està acabada només si compleix C1-C4 amb cites verificades per script.</p>
{cert}
</section>
<section class="seccio" id="criteris"><h2>Criteris de la part pública</h2>
<p>No es mostren les columnes de robustesa, les propostes brutes ni les notes de decisió de l'auditoria, ni referències a fitxers o informes interns. Quan una nota del registre conté noms de models o referències internes, es mostra un avís en lloc de la nota. Les cites es mostren tal com les publica l'emissor, incloses les dates de naixement que serveixen per a la prova b. Les cites llargues es retallen a un fragment, amb l'avís corresponent. Del fitxer de dubtes (<code>PENDENTS.md</code>) només es compten files: no se'n mostra el text.</p>
<ul>{ocults}</ul>
<h3>Què no hi ha (i no s'inventa)</h3>
<ul>
<li><b>Fundadors de l'empresa.</b> La base no té cap camp amb els noms dels fundadors. Si una fila és F, el CEO d'aquell any està classificat com a fundador; no és una llista completa de fundadors.</li>
<li><b>Any de fundació.</b> No és un camp. Si apareix, és dins del text d'una cita o d'una nota.</li>
<li><b>País.</b> El filtre «país d'emissió de l'ISIN» es deriva del prefix de l'ISIN i no és la seu social.</li>
<li><b>Sector.</b> No es mostra en aquesta versió, pendent d'aclarir la llicència de la classificació.</li>
</ul>
</section>
<section class="seccio" id="documents"><h2>Documents que manen</h2>
<ul class="docs">{docs_html}</ul>
<p>Si aquesta pàgina i aquests documents diuen coses diferents, manen els documents.</p>
</section>
</div>"""
    return pagina(ctx, titol="Mètode · Fundadors-CEO STOXX Europe 600",
                  descripcio="Com es llegeixen les etiquetes F, P, ND i NA, l'estat de cada fila, les fonts i les marques de prova.",
                  cos=cos, prefix="", actiu="metode", cls_body="p-metode")


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
    resum_text = comprova_resum_estat(shas)
    commit, data_commit = commit_referencia(args.commit)
    ctx = Context(commit, data_commit, shas)
    stats: Counter = Counter()
    model = carrega_model(stats)
    carrega_estat(model)
    E = calcula_estat(model, resum_text)

    escriu(SORTIDA / "assets" / "style.css", CSS)
    escriu(SORTIDA / "assets" / "cerca.js", JS_CERCA)
    escriu(SORTIDA / "assets" / "fitxa.js", JS_FITXA)
    escriu(SORTIDA / "index.html", pagina_estat(ctx, E))
    escriu(SORTIDA / "empreses.html", pagina_empreses(ctx, model, E))
    escriu(SORTIDA / "metodologia.html", pagina_metodologia(ctx, model, E, stats))

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

    tot = E["tot"]
    print(f"Commit de referència: {commit} {data_commit}")
    for rel, h in shas.items():
        print(f"SHA-256 {rel}: {h} (coincideix amb el manifest)")
    print("estat/RESUM_ESTAT.md correspon a les dades actuals")
    print(f"ISIN: {E['n_isin']} · files: {tot} · " + " · ".join(f"{l} {E['etiq'][l]}" for l in ORDRE_ETIQ))
    print("Estats: " + " · ".join(f"{ESTATS[k][1]} {E['cat'][k]}" for k in ORDRE_ESTATS))
    print("Embut: " + " → ".join(str(x) for x in E["embut"]))
    print("Mancances: " + " · ".join(f"{k} {E['mancances'][k]}" for k in MANCANCES))
    for k in sorted(stats):
        print(f"{k}: {stats[k]}")
    print(f"Fitxes escrites: {len(ordenades)}")
    return 0


# ---------------------------------------------------------------------------
# Actius estàtics (CSS i JS), sense dependències externes
# ---------------------------------------------------------------------------

CSS = r"""/* Fundadors-CEO. Generat per dashboard/genera_dashboard.py; no l'editis a mà. */
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
  /* Etiquetes FounderCEO (text blanc >= 4,5:1) */
  --e-F: #c2521f;
  --e-P: #1f66c1;
  --e-ND: #9b2f8f;
  --e-NA: #6e6d68;
  --e-txt: #ffffff;
  --e-F-suau: #fbe9e1;
  --e-P-suau: #e6effa;
  --e-ND-suau: #f5e6f3;
  --e-NA-suau: #efeeeb;
  /* Estats de la fila (escala ordinal, separada de les etiquetes) */
  --st-acabada: #1f7a3d;
  --st-acabada-txt: #ffffff;
  --st-arxiu: #cfe8d6;
  --st-arxiu-txt: #1a1a19;
  --st-dubte: #e9a93a;
  --st-dubte-txt: #1a1a19;
  --st-falta: #e7e5df;
  --st-falta-ratlla: #c9c6bd;
  --st-falta-txt: #1a1a19;
  /* Mapa de calor */
  --hm-acabada: #1f7a3d;
  --hm-arxiu: #3d8f63;
  --hm-dubte: #b7791f;
  --hm-falta: #6e6d68;
  /* Barres d'una sola sèrie */
  --barra: #4a5d73;
  /* Proves */
  --v: #12692c;
  --v-fons: #e5f3e8;
  --nv: #8a5300;
  --nv-fons: #fdf1d8;
  --mal: #b42318;
  --mal-fons: #fde8e6;
  --cita-fons: #fbfaf7;
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
    --e-ND: #a8399c;
    --e-F-suau: #3a2116;
    --e-P-suau: #172a42;
    --e-ND-suau: #33172f;
    --e-NA-suau: #2a2a27;
    --st-acabada: #5fcf8a;
    --st-acabada-txt: #121211;
    --st-arxiu: #2e6b47;
    --st-arxiu-txt: #f0efec;
    --st-dubte: #d9a93a;
    --st-dubte-txt: #121211;
    --st-falta: #3a3935;
    --st-falta-ratlla: #504f4a;
    --st-falta-txt: #f0efec;
    --barra: #8fa3ba;
    --v: #7fd99a;
    --v-fons: #143220;
    --nv: #f2c14e;
    --nv-fons: #382a0c;
    --mal: #ff9a8f;
    --mal-fons: #3f1814;
    --cita-fons: #20201d;
  }
}
*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: 80px; }
body { margin: 0; background: var(--fons); color: var(--tinta); font: 15px/1.55 var(--font); }
a { color: var(--enllac); text-underline-offset: 2px; }
a:hover { color: var(--enllac-hover); }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; border-radius: 4px; }
code { font-family: var(--font-mono); font-size: .86em; background: var(--sup-2); padding: .08em .35em; border-radius: 5px; overflow-wrap: anywhere; }
h1, h2, h3, h4 { line-height: 1.2; margin: 0 0 .5em; font-weight: 700; }
h1 { font-size: clamp(26px, 2.2vw + 16px, 32px); letter-spacing: -.01em; }
h2 { font-size: 22px; }
h3, .h3 { font-size: 17px; font-weight: 600; }
p { margin: 0 0 .8em; }
small { font-size: 13px; }
abbr[title] { text-decoration: none; }
.vh { position: absolute !important; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
.salta { position: absolute; left: -999px; top: 8px; background: var(--sup); padding: 8px 12px; border-radius: 8px; z-index: 50; }
.salta:focus { left: 8px; }
.nota { color: var(--tinta-3); font-size: 13px; max-width: 68ch; }
.mini { color: var(--tinta-3); font-size: 13px; font-weight: 400; }
.buit { color: var(--tinta-3); }
.ok { color: var(--v); font-weight: 600; }
.num, .tc-v, .tc-n, .ll-n, .bs-val, .eb-val, .tl-any, .a-any, .p-anys, td, th { font-variant-numeric: tabular-nums; }

/* Barra superior */
.barra { position: sticky; top: 0; z-index: 20; background: var(--sup); border-bottom: 1px solid var(--linia); }
.barra-in { max-width: 1240px; margin: 0 auto; padding: 8px 16px; display: flex; align-items: center; gap: 8px 24px; flex-wrap: wrap; }
.marca { display: flex; align-items: center; gap: 10px; color: var(--tinta); text-decoration: none; font-weight: 700; margin-right: auto; }
.marca:hover { color: var(--tinta); }
.marca-text { display: flex; flex-direction: column; line-height: 1.2; font-size: 15px; }
.marca-text small { font-weight: 400; color: var(--tinta-3); }
.marca-logo { display: grid; grid-template-columns: repeat(3, 7px); gap: 3px; }
.marca-logo i { display: block; width: 7px; height: 22px; border-radius: 3px; background: var(--e-P); }
.marca-logo i:nth-child(2) { background: var(--e-F); }
.marca-logo i:nth-child(3) { background: var(--st-acabada); }
.nav { display: flex; gap: 4px; }
.nav a { display: inline-flex; align-items: center; min-height: 40px; padding: 0 14px; border-radius: 999px; text-decoration: none; color: var(--tinta-2); font-weight: 600; }
.nav a:hover { background: var(--sup-2); color: var(--tinta); }
.nav a[aria-current="page"] { background: var(--tinta); color: var(--sup); }
.pindola { display: inline-flex; align-items: center; min-height: 32px; font-size: 13px; font-weight: 600; padding: 0 12px; border-radius: 999px; background: var(--nv-fons); color: var(--nv); text-decoration: none; white-space: nowrap; }
.pindola:hover { color: var(--nv); text-decoration: underline; }

.pagina { max-width: 1120px; margin: 0 auto; padding: 32px 16px 48px; }
.pagina.ample { max-width: 1240px; }
.molla { margin: 0 0 12px; }
.molla a { text-decoration: none; font-weight: 600; display: inline-flex; min-height: 40px; align-items: center; }
.entradeta { font-size: 17px; color: var(--tinta-2); max-width: 68ch; }
.cap-pagina { margin-bottom: 24px; }
.resposta { font-size: 17px; max-width: 68ch; }

/* Línia de versió */
.versio-linia { display: flex; gap: 12px; align-items: flex-start; font-size: 13px; color: var(--tinta-2); background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 12px 16px; max-width: 100%; }
.pv-icona { flex: none; width: 20px; height: 20px; border-radius: 50%; background: var(--nv-fons); color: var(--nv); display: grid; place-items: center; font-weight: 700; }
.versio-linia code { background: transparent; padding: 0; }

/* Cerca ràpida */
.cerca-rapida { margin: 24px 0 48px; max-width: 640px; }
.cerca-rapida label { display: block; font-weight: 600; margin-bottom: 8px; }
.cr-fila { display: flex; gap: 8px; }
.cr-fila input { flex: 1; min-width: 0; }
input[type="search"], select { font: inherit; color: var(--tinta); background: var(--sup); border: 1px solid var(--linia-forta); border-radius: var(--radi-petit); padding: 8px 12px; min-height: 42px; width: 100%; min-width: 0; }
.boto { display: inline-flex; align-items: center; gap: 6px; min-height: 40px; font: inherit; font-weight: 600; padding: 6px 14px; border: 0; border-radius: var(--radi-petit); background: var(--enllac); color: #fff; text-decoration: none; cursor: pointer; }
.boto:hover { color: #fff; background: var(--enllac-hover); }
@media (prefers-color-scheme: dark) { .boto, .boto:hover { color: #0d1b2e; } }
.boto-wb { background: transparent; color: var(--enllac); border: 1px solid var(--enllac); }
.boto-wb:hover { background: var(--sup-2); color: var(--enllac-hover); }
@media (prefers-color-scheme: dark) { .boto-wb, .boto-wb:hover { color: var(--enllac); } }
.boto-off { background: var(--sup-2); color: var(--tinta-3); border: 1px dashed var(--linia-forta); font-weight: 400; cursor: default; }
.boto-mostra { min-height: 0; padding: 4px 10px; font-size: 13px; }
.boto-sec { font: inherit; font-weight: 600; min-height: 42px; border: 1px solid var(--linia-forta); background: var(--sup); color: var(--tinta-2); border-radius: var(--radi-petit); padding: 6px 14px; cursor: pointer; }
.boto-sec:hover { background: var(--sup-2); color: var(--tinta); }
.ext { font-size: .85em; margin-left: 2px; }

/* Seccions de l'Estat */
.cap-estat { margin-bottom: 0; }
.bloc { margin: 0 0 48px; break-inside: avoid; }
.bloc > h2 { margin-bottom: 8px; }
.heroi-xifra { font-size: 22px; margin: 4px 0 16px; }
.heroi-xifra b { font-size: 40px; font-weight: 700; letter-spacing: -.01em; }
.heroi-xifra span { color: var(--tinta-2); }

/* Barra apilada al 100 % */
.sb { display: flex; gap: 2px; height: 32px; padding: 2px; background: var(--sup); border: 1px solid var(--linia-forta); border-radius: 8px; margin: 0 0 16px; }
.sb-s { min-width: 3px; flex-basis: 0; border-radius: 4px; display: flex; align-items: center; }
.sb-n { font-size: 13px; font-weight: 600; white-space: nowrap; padding-left: 8px; }
.s-acabada { background: var(--st-acabada); color: var(--st-acabada-txt); }
.s-arxiu { background: var(--st-arxiu); color: var(--st-arxiu-txt); }
.s-dubte { background: var(--st-dubte); color: var(--st-dubte-txt); }
.s-falta { background: repeating-linear-gradient(135deg, var(--st-falta) 0 5px, var(--st-falta-ratlla) 5px 7px); color: var(--st-falta-txt); }
.e-F { background: var(--e-F); color: var(--e-txt); }
.e-P { background: var(--e-P); color: var(--e-txt); }
.e-ND { background: var(--e-ND); color: var(--e-txt); }
.e-NA { background: var(--e-NA); color: var(--e-txt); }
.sw { display: inline-grid; place-items: center; flex: none; width: 24px; height: 24px; border-radius: 6px; font-size: 13px; font-weight: 700; font-style: normal; border: 1px solid var(--linia-forta); }
.ll-estats, .ll-etiq { list-style: none; margin: 0 0 12px; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); gap: 12px 24px; }
.ll-estats li, .ll-etiq li { display: flex; gap: 10px; align-items: flex-start; }
.ll-etiq li { align-items: center; }
.ll-txt { display: flex; flex-direction: column; }
.ll-n { color: var(--tinta-2); }
.ll-def { font-size: 13px; color: var(--tinta-3); }

/* Embut */
.embut { list-style: none; margin: 16px 0 8px; padding: 0; max-width: 860px; }
.eb-pas { margin: 0; }
.eb-nom { display: block; font-weight: 600; margin-bottom: 4px; }
.eb-fila { display: flex; align-items: center; gap: 10px; }
.eb-barra { display: block; height: 22px; min-width: 3px; background: var(--barra); border-radius: 0 4px 4px 0; }
.eb-final .eb-barra { background: var(--st-acabada); }
.eb-val { white-space: nowrap; font-weight: 600; }
.eb-salt { display: flex; align-items: center; gap: 8px; margin: 6px 0 10px 12px; padding-left: 12px; border-left: 2px solid var(--linia-forta); color: var(--tinta-2); font-size: 13px; }
.eb-salt .sw { width: 20px; height: 20px; font-size: 12px; }

/* Taula d'etiquetes */
.taula-wrap { overflow-x: auto; -webkit-overflow-scrolling: touch; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); }
table { border-collapse: collapse; width: 100%; }
th, td { text-align: left; vertical-align: top; padding: 8px 12px; border-bottom: 1px solid var(--linia); }
thead th { background: var(--sup-2); font-size: 13px; color: var(--tinta-2); font-weight: 600; white-space: nowrap; }
tbody tr:last-child > * { border-bottom: 0; }
.num { text-align: right; }
.taula-etiq td, .taula-etiq th { vertical-align: middle; }
.taula-etiq td { min-width: 92px; }
.tc-v { display: block; font-weight: 600; }
.tc-n { display: block; font-size: 13px; color: var(--tinta-3); }
.mm { display: block; height: 6px; background: var(--sup-3); border-radius: 3px; margin-top: 4px; overflow: hidden; }
.mm i { display: block; height: 100%; background: var(--barra); border-radius: 3px; }
.etq { display: inline-flex; align-items: center; gap: 6px; white-space: nowrap; font-size: 13px; font-weight: 600; padding: 2px 10px 2px 2px; border-radius: 999px; background: var(--e-P-suau); color: var(--tinta); }
.etq b { display: inline-grid; place-items: center; min-width: 26px; height: 22px; padding: 0 4px; border-radius: 999px; font-size: 12px; background: var(--e-P); color: var(--e-txt); }
.etq.e-F { background: var(--e-F-suau); color: var(--tinta); } .etq.e-F b { background: var(--e-F); }
.etq.e-P { color: var(--tinta); }
.etq.e-ND { background: var(--e-ND-suau); color: var(--tinta); } .etq.e-ND b { background: var(--e-ND); }
.etq.e-NA { background: var(--e-NA-suau); color: var(--tinta); } .etq.e-NA b { background: var(--e-NA); }

/* Mapa de calor */
.mapa { table-layout: fixed; }
.mapa th:first-child { width: 72px; }
.mapa th:last-child { width: 80px; }
.mapa td.hm { text-align: right; color: var(--tinta); padding-top: 6px; padding-bottom: 6px; }
.mapa td.hm b { display: block; font-weight: 600; }
.mapa td.hm small { color: var(--tinta-2); }
.hm.g0 { background: var(--sup); }
.hm-acabada.g1 { background: color-mix(in srgb, var(--hm-acabada) 10%, var(--sup)); }
.hm-acabada.g2 { background: color-mix(in srgb, var(--hm-acabada) 22%, var(--sup)); }
.hm-acabada.g3 { background: color-mix(in srgb, var(--hm-acabada) 34%, var(--sup)); }
.hm-acabada.g4 { background: color-mix(in srgb, var(--hm-acabada) 46%, var(--sup)); }
.hm-acabada.g5 { background: color-mix(in srgb, var(--hm-acabada) 60%, var(--sup)); }
.hm-arxiu.g1 { background: color-mix(in srgb, var(--hm-arxiu) 10%, var(--sup)); }
.hm-arxiu.g2 { background: color-mix(in srgb, var(--hm-arxiu) 22%, var(--sup)); }
.hm-arxiu.g3 { background: color-mix(in srgb, var(--hm-arxiu) 34%, var(--sup)); }
.hm-arxiu.g4 { background: color-mix(in srgb, var(--hm-arxiu) 46%, var(--sup)); }
.hm-arxiu.g5 { background: color-mix(in srgb, var(--hm-arxiu) 60%, var(--sup)); }
.hm-dubte.g1 { background: color-mix(in srgb, var(--hm-dubte) 10%, var(--sup)); }
.hm-dubte.g2 { background: color-mix(in srgb, var(--hm-dubte) 22%, var(--sup)); }
.hm-dubte.g3 { background: color-mix(in srgb, var(--hm-dubte) 34%, var(--sup)); }
.hm-dubte.g4 { background: color-mix(in srgb, var(--hm-dubte) 46%, var(--sup)); }
.hm-dubte.g5 { background: color-mix(in srgb, var(--hm-dubte) 60%, var(--sup)); }
.hm-falta.g1 { background: color-mix(in srgb, var(--hm-falta) 10%, var(--sup)); }
.hm-falta.g2 { background: color-mix(in srgb, var(--hm-falta) 22%, var(--sup)); }
.hm-falta.g3 { background: color-mix(in srgb, var(--hm-falta) 34%, var(--sup)); }
.hm-falta.g4 { background: color-mix(in srgb, var(--hm-falta) 46%, var(--sup)); }
.hm-falta.g5 { background: color-mix(in srgb, var(--hm-falta) 60%, var(--sup)); }
.curt { display: none; }
.hm-escala { display: flex; flex-wrap: wrap; gap: 8px 16px; align-items: center; font-size: 13px; color: var(--tinta-3); margin-top: 8px; }
.hm-escala ul { list-style: none; display: flex; flex-wrap: wrap; gap: 4px 12px; margin: 0; padding: 0; }
.hm-escala li { display: inline-flex; align-items: center; gap: 4px; }
.hm-escala .hm { display: inline-block; width: 18px; height: 14px; border: 1px solid var(--linia-forta); border-radius: 3px; }

/* Barres d'una sola sèrie (mancances, dubtes) */
.bs { list-style: none; margin: 16px 0 8px; padding: 0; max-width: 860px; }
.bs li { margin: 0 0 16px; }
.bs-nom { display: block; font-weight: 600; }
.bs-fila { display: flex; align-items: center; gap: 10px; margin: 4px 0; }
.bs-barra { display: block; height: 18px; min-width: 3px; background: var(--barra); border-radius: 0 4px 4px 0; }
.bs-val { font-weight: 600; white-space: nowrap; }
.bs-det, .bs-que { display: block; font-size: 13px; color: var(--tinta-2); }
.bs-link { display: inline-flex; align-items: center; min-height: 32px; font-size: 13px; font-weight: 600; }
.codi-petit { font-size: 12px; }

/* Passos de qualitat */
.passos { list-style: none; margin: 16px 0 8px; padding: 0; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 12px; }
.passos li { display: flex; flex-direction: column; gap: 8px; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 16px; min-width: 0; }
.pq-n { display: inline-grid; place-items: center; width: 28px; height: 28px; border-radius: 50%; background: var(--tinta); color: var(--sup); font-weight: 700; }
.pq-t { display: flex; flex-direction: column; gap: 4px; overflow-wrap: anywhere; }
.pq-nom { font-size: 15px; }
.pq-t > span { font-size: 13px; color: var(--tinta-2); }

/* Gràfic de files F per any */
.grafic { margin: 24px 0 0; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 16px; }
.grafic figcaption { margin-bottom: 12px; }
.barres { position: relative; height: 200px; margin: 8px 0 4px 30px; }
.eix { position: absolute; inset: 0 0 40px 0; pointer-events: none; }
.tick { position: absolute; left: 0; right: 0; border-top: 1px solid var(--linia); }
.tick span { position: absolute; left: -30px; top: -.6em; width: 24px; text-align: right; font-size: 12px; color: var(--tinta-3); }
.bcols { position: absolute; inset: 0; display: flex; gap: 6px; }
.bcol { position: relative; flex: 1; min-width: 0; display: flex; flex-direction: column; }
.barea { flex: 1; display: flex; align-items: flex-end; justify-content: center; }
.bar { position: relative; display: block; width: min(24px, 70%); background: var(--e-F); border-radius: 4px 4px 0 0; min-height: 2px; }
.bval { position: absolute; bottom: 100%; left: 50%; transform: translateX(-50%); font-size: 12px; color: var(--tinta-2); padding-bottom: 2px; }
.bany { height: 40px; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 12px; color: var(--tinta-2); line-height: 1.2; }
.bany small { font-size: 11px; color: var(--tinta-3); }
.tip { position: absolute; bottom: calc(100% - 30px); left: 50%; transform: translateX(-50%); background: var(--tinta); color: var(--sup); font-size: 13px; padding: 6px 9px; border-radius: 7px; white-space: nowrap; pointer-events: none; display: none; z-index: 5; }
.bcol:hover .tip, .bcol:focus .tip { display: block; }
.bcol:first-child .tip { left: 0; transform: none; }
.bcol:last-child .tip { left: auto; right: 0; transform: none; }
details.dades { margin-top: 8px; font-size: 13px; }
details.dades summary { cursor: pointer; color: var(--enllac); min-height: 32px; display: flex; align-items: center; }
.taula-simple th, .taula-simple td { padding: 6px 12px; font-size: 13px; }

/* Sobre aquestes dades */
.versio .versio-linia { margin-bottom: 16px; }
.versio-dl { display: grid; gap: 8px; margin: 0 0 12px; }
.versio-dl div { display: grid; grid-template-columns: minmax(180px, 280px) 1fr; gap: 4px 12px; }
.versio-dl dt { font-size: 13px; color: var(--tinta-2); }
.versio-dl dd { margin: 0; min-width: 0; }
.sha { font-size: 12px; }
.docs { padding-left: 20px; }
.docs li { margin-bottom: 4px; }

/* Empreses */
.filtres { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 12px; align-items: end; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 16px; margin: 0 0 12px; }
.camp { display: flex; flex-direction: column; gap: 4px; font-size: 13px; font-weight: 600; color: var(--tinta-2); min-width: 0; }
.camp small { font-weight: 400; color: var(--tinta-3); }
.camp-cerca { grid-column: 1 / -1; }
.camp-cerca input { font-size: 17px; }
.camp[hidden] { display: none; }
.recompte { color: var(--tinta-2); margin: 0 0 8px; }
.recompte b { color: var(--tinta); }
.llegenda { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 16px; font-size: 13px; color: var(--tinta-2); margin: 8px 0 12px; }
.ll { display: inline-flex; align-items: center; gap: 6px; }
.ll-cap { font-weight: 600; color: var(--tinta); }
.llegenda .sw { width: 20px; height: 20px; font-size: 11px; border: 0; }
.sw-ratlla { display: inline-block; width: 20px; height: 6px; border-radius: 2px; border: 1px solid var(--linia-forta); }
.ll-ajuda { display: inline-grid; place-items: center; width: 28px; height: 28px; border-radius: 50%; border: 1px solid var(--linia-forta); text-decoration: none; font-weight: 700; }
.taula-emp td { vertical-align: middle; }
.taula-emp thead button { font: inherit; color: inherit; background: none; border: 0; padding: 0; cursor: pointer; display: inline-flex; align-items: center; gap: 4px; min-height: 32px; }
.taula-emp thead button::after { content: "↕"; opacity: .4; }
.taula-emp thead button[aria-sort="ascending"]::after { content: "↑"; opacity: 1; }
.taula-emp thead button[aria-sort="descending"]::after { content: "↓"; opacity: 1; }
.taula-emp tbody tr:hover { background: var(--sup-2); }
.taula-emp td:first-child a { font-weight: 600; text-decoration: none; color: var(--tinta); }
.taula-emp td:first-child a:hover { color: var(--enllac); text-decoration: underline; }
.sub { display: block; font-size: 13px; color: var(--tinta-3); margin-top: 2px; }
.sub code { background: transparent; padding: 0; font-size: 12px; }
.sr { display: inline-flex; gap: 2px; }
.sr i { display: inline-grid; place-items: center; width: 20px; height: 24px; border-radius: 4px; font: 700 11px/1 var(--font); font-style: normal; background: repeating-linear-gradient(135deg, var(--sup-2) 0 4px, var(--sup-3) 4px 6px); border: 1px solid var(--linia); color: var(--e-txt); padding-bottom: 3px; }
.sr i.F { background: var(--e-F); border: 0; } .sr i.P { background: var(--e-P); border: 0; }
.sr i.ND { background: var(--e-ND); border: 0; } .sr i.NA { background: var(--e-NA); border: 0; }
.sr i.a { box-shadow: inset 0 -4px 0 var(--st-acabada); }
.sr i.r { box-shadow: inset 0 -4px 0 var(--st-arxiu); }
.sr i.d { box-shadow: inset 0 -4px 0 var(--st-dubte); }
.sr i.f { box-shadow: inset 0 -4px 0 var(--st-falta); }
.sw-ratlla.s-falta { background: var(--st-falta); }
.mb { display: flex; gap: 2px; width: 120px; height: 10px; padding: 1px; border: 1px solid var(--linia-forta); border-radius: 4px; background: var(--sup); }
.mb i { flex-basis: 0; min-width: 2px; border-radius: 2px; }
.mb .s-falta { background: var(--st-falta); }
.mb-gran { width: 200px; height: 14px; }
.sense-resultat { text-align: center; padding: 24px; color: var(--tinta-2); background: var(--sup); border: 1px dashed var(--linia-forta); border-radius: var(--radi); margin-top: 12px; }

/* Fitxa */
.fitxa-cap { margin-bottom: 24px; }
.fitxa-cap h1 { overflow-wrap: anywhere; margin-bottom: 4px; }
.fitxa-linia { color: var(--tinta-2); }
.fitxa-linia code { background: transparent; padding: 0; font-size: 15px; font-weight: 600; color: var(--tinta); }
.altres-noms { font-size: 13px; color: var(--tinta-3); }
.fitxa-estat { display: flex; align-items: center; flex-wrap: wrap; gap: 8px 12px; font-size: 17px; }
.caixa-dubte { display: flex; gap: 12px; align-items: flex-start; background: var(--nv-fons); color: var(--tinta); border: 1px solid var(--st-dubte); border-radius: var(--radi); padding: 12px 16px; margin: 0 0 32px; }
.caixa-dubte ul { margin: 0; padding: 0; list-style: none; }
.cd-icona { flex: none; width: 24px; height: 24px; border-radius: 50%; background: var(--st-dubte); color: var(--st-dubte-txt); display: grid; place-items: center; font-weight: 700; }
.seccio { margin-bottom: 48px; }
.seccio > h2 { margin-bottom: 12px; }
.tl-wrap { overflow-x: auto; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 16px; }
.tl { min-width: 640px; display: flex; flex-direction: column; gap: 6px; }
.tl-fila { display: grid; grid-template-columns: repeat(10, minmax(0, 1fr)); gap: 4px; }
.tl-any { text-align: center; font-size: 13px; font-weight: 600; color: var(--tinta-3); text-decoration: none; }
a.tl-any { color: var(--enllac); }
.cel { display: inline-grid; place-items: center; width: 100%; min-width: 34px; height: 34px; border-radius: 6px; font-weight: 700; font-size: 13px; text-decoration: none; }
.cel-p { width: 22px; min-width: 22px; height: 24px; border-radius: 4px; font-size: 11px; }
.cel-buida { background: repeating-linear-gradient(135deg, var(--sup-2) 0 4px, var(--sup-3) 4px 7px); color: var(--tinta-3); border: 1px solid var(--linia); }
.tl-st { display: grid; place-items: center; height: 26px; border-radius: 6px; font-weight: 700; text-decoration: none; }
.tl-st-buit { background: transparent; }
.tl-fila-ceo { grid-auto-rows: minmax(52px, auto); }
.tl-ceo { background: var(--sup-2); border: 1px solid var(--linia); border-left: 4px solid var(--tinta-2); border-radius: 8px; padding: 6px 9px; display: flex; flex-direction: column; justify-content: center; min-width: 0; }
.tl-ceo b { font-size: 13px; line-height: 1.25; overflow-wrap: anywhere; }
.tl-ceo small { color: var(--tinta-3); }
.tl-ceo-buit { font-style: italic; }
.trams { display: none; list-style: none; margin: 0; padding: 0; }
.tram { display: grid; grid-template-columns: auto 1fr; gap: 4px 10px; align-items: center; background: var(--sup); border: 1px solid var(--linia); border-left: 5px solid var(--tinta-2); border-radius: var(--radi-petit); padding: 10px 12px; margin-bottom: 8px; }
.tram-anys { font-weight: 700; color: var(--tinta-2); }
.tram-nom { overflow-wrap: anywhere; }
.tram .serie { grid-column: 1 / -1; display: flex; flex-wrap: wrap; gap: 4px; }
.tram .cel-p { width: 40px; height: 40px; font-size: 13px; box-shadow: inset 0 -5px 0 var(--sup-3); }
.tram .b-acabada { box-shadow: inset 0 -5px 0 var(--st-acabada); }
.tram .b-arxiu { box-shadow: inset 0 -5px 0 var(--st-arxiu); }
.tram .b-dubte { box-shadow: inset 0 -5px 0 var(--st-dubte); }
.tram .b-falta { box-shadow: inset 0 -5px 0 var(--st-falta); }
.v-F { border-left-color: var(--e-F); } .v-P { border-left-color: var(--e-P); }
.v-ND { border-left-color: var(--e-ND); } .v-NA { border-left-color: var(--e-NA); }

/* Insígnia d'estat */
.st { display: inline-flex; align-items: center; gap: 6px; white-space: nowrap; font-size: 13px; font-weight: 600; padding: 2px 10px; border-radius: 999px; }
.st-acabada { background: var(--st-acabada); color: var(--st-acabada-txt); }
.st-arxiu { background: var(--st-arxiu); color: var(--st-arxiu-txt); }
.st-dubte { background: var(--st-dubte); color: var(--st-dubte-txt); }
.st-falta { background: repeating-linear-gradient(135deg, var(--st-falta) 0 5px, var(--st-falta-ratlla) 5px 7px); color: var(--st-falta-txt); }
.st-falta, .s-falta { border: 1px solid var(--linia-forta); }

/* Any per any */
.anys { background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); overflow: hidden; }
.anys-cap, .any > summary { display: grid; grid-template-columns: 56px minmax(0, 1.5fr) 140px minmax(0, 1.3fr) 200px 92px; gap: 8px 12px; align-items: center; padding: 8px 16px; }
.anys-cap { background: var(--sup-2); font-size: 13px; font-weight: 600; color: var(--tinta-2); }
.any { border-top: 1px solid var(--linia); }
.any > summary { cursor: pointer; list-style: none; min-height: 48px; }
.any > summary::-webkit-details-marker { display: none; }
.any > summary:hover { background: var(--sup-2); }
.a-any { font-weight: 700; }
.a-ceo { font-weight: 600; overflow-wrap: anywhere; }
.a-prova { font-size: 13px; color: var(--tinta-2); overflow-wrap: anywhere; }
.a-pq { justify-self: end; font-size: 13px; font-weight: 600; color: var(--enllac); border: 1px solid var(--linia-forta); border-radius: 999px; padding: 4px 12px; white-space: nowrap; }
.a-pq::after { content: " ▾"; }
.any[open] .a-pq::after { content: " ▴"; }
.any[open] > summary { background: var(--sup-2); }
.pq { padding: 12px 16px 16px; border-top: 1px dashed var(--linia); display: grid; gap: 12px; }
.pq-regla { margin: 0; }
.regla { margin-right: 6px; }
.pq-bloc { border-left: 3px solid var(--linia-forta); padding-left: 12px; }
.pq-bloc h4 { font-size: 15px; display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin-bottom: 6px; }
.pq-ins { display: inline-flex; flex-wrap: wrap; gap: 4px; }
.pq-cadena { font-size: 13px; display: flex; flex-wrap: wrap; gap: 4px 8px; align-items: center; margin: 0 0 4px; }
.pq-cadena a { display: inline-flex; align-items: center; min-height: 32px; }
.pq-totes { margin: 0; font-weight: 600; }
.falta-txt { margin: 0; font-weight: 600; color: var(--mal); }

/* Proves */
.filtre-anys { display: none; flex-wrap: wrap; gap: 6px; margin: 10px 0 6px; }
.js .filtre-anys { display: flex; }
.xip { font: inherit; font-size: 13px; font-weight: 600; min-height: 36px; border: 1px solid var(--linia-forta); background: var(--sup); color: var(--tinta-2); border-radius: 999px; padding: 4px 12px; cursor: pointer; }
.xip:hover { background: var(--sup-2); }
.xip[aria-pressed="true"] { background: var(--tinta); color: var(--sup); border-color: var(--tinta); }
.recompte-proves { font-size: 13px; color: var(--tinta-3); min-height: 1.3em; }
.grup-proves { background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 0 16px; margin: 0 0 12px; }
.grup-proves > summary { cursor: pointer; min-height: 48px; display: flex; align-items: center; gap: 8px; font-weight: 700; font-size: 17px; }
.grup-proves > summary .n { font-size: 13px; background: var(--sup-3); color: var(--tinta-2); padding: 2px 9px; border-radius: 999px; }
.grup-proves[open] { padding-bottom: 8px; }
.prova { background: var(--sup); border: 1px solid var(--linia); border-left: 4px solid var(--v); border-radius: var(--radi); padding: 16px; margin: 12px 0; }
.prova-nv { border-left-color: var(--nv); }
.prova-mal { border-left-color: var(--mal); }
.prova-base { border-left-color: var(--linia-forta); }
.prova-oculta { border-left-color: var(--tinta-3); background: var(--sup-2); padding: 10px 14px; }
.prova-oculta p { margin: 0; color: var(--tinta-3); font-size: 13px; }
.prova:target { outline: 3px solid var(--focus); outline-offset: 2px; }
.p-cap { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin-bottom: 10px; }
.p-anys { margin-left: auto; font-size: 13px; font-weight: 700; color: var(--tinta-2); background: var(--sup-2); padding: 2px 10px; border-radius: 999px; }
.b { display: inline-flex; align-items: center; font-size: 12px; font-weight: 700; padding: 2px 9px; border-radius: 999px; white-space: nowrap; line-height: 1.4; font-family: var(--font); }
.b-v { background: var(--v-fons); color: var(--v); }
.b-nv { background: var(--nv-fons); color: var(--nv); }
.b-mal { background: var(--mal-fons); color: var(--mal); }
.b-gris { background: var(--sup-3); color: var(--tinta-2); }
.b-marca { background: transparent; border: 1px solid var(--linia-forta); color: var(--tinta-2); font-family: var(--font-mono); font-weight: 400; }
.b-nivell { background: var(--e-P-suau); color: var(--tinta); }
.cita { margin: 0 0 12px; padding: 12px 16px 12px 40px; background: var(--cita-fons); border-radius: var(--radi-petit); position: relative; border: 1px solid var(--linia); }
.cita::before { content: "“"; position: absolute; left: 12px; top: 2px; font-family: var(--font-cita); font-size: 2.4rem; line-height: 1; color: var(--tinta-3); }
.cita p { margin: 0; font-family: var(--font-cita); font-size: 17px; line-height: 1.5; overflow-wrap: anywhere; max-width: 68ch; }
.sense-cita { font-style: italic; color: var(--tinta-3); background: var(--sup-2); border-radius: var(--radi-petit); padding: 8px 12px; }
.p-fonts { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-bottom: 8px; }
.domini { font-size: 13px; color: var(--tinta-2); overflow-wrap: anywhere; }
details.tecnic > summary { cursor: pointer; font-size: 13px; color: var(--enllac); min-height: 32px; display: flex; align-items: center; }
.p-meta { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 8px 16px; margin: 8px 0 0; padding: 12px 0 0; border-top: 1px solid var(--linia); }
.p-meta div { min-width: 0; }
.p-meta dt { font-size: 12px; color: var(--tinta-3); font-weight: 600; }
.p-meta dd { margin: 2px 0 0; font-size: 13px; overflow-wrap: anywhere; }
.llista-codi { margin: 4px 0 0; padding-left: 18px; }
.p-notes { margin-top: 12px; padding-top: 8px; border-top: 1px solid var(--linia); }
.p-notes h4 { font-size: 12px; color: var(--tinta-3); margin-bottom: 4px; }
.p-notes p { font-size: 13px; color: var(--tinta-2); margin-bottom: .5em; overflow-wrap: anywhere; }
.nota-oculta { font-style: italic; color: var(--tinta-3) !important; }
.sense-proves { background: var(--sup); border: 1px dashed var(--linia-forta); border-radius: var(--radi); padding: 16px; }
.sense-proves p { margin: 0; }
.rastre { margin-top: 12px; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 12px 16px; }
.rastre summary { cursor: pointer; font-weight: 600; }
.llista-urls { padding-left: 18px; font-size: 13px; }
.url-llarga { overflow-wrap: anywhere; }
.historial { background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 0 16px; margin-bottom: 32px; }
.historial > summary { cursor: pointer; min-height: 48px; display: flex; align-items: center; flex-wrap: wrap; gap: 6px; font-weight: 600; }
.historial[open] { padding-bottom: 16px; }
.nav-fitxes { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.nav-fitxes a { display: flex; flex-direction: column; gap: 2px; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 12px 16px; text-decoration: none; font-weight: 600; color: var(--tinta); min-width: 0; overflow-wrap: anywhere; }
.nav-fitxes a small { color: var(--tinta-3); }
.nav-fitxes a:hover { border-color: var(--enllac); }
.nav-fitxes .seg { text-align: right; }

/* Mètode */
.text-llarg { max-width: 860px; }
.text-llarg p, .text-llarg li { max-width: 68ch; }
.def { display: grid; grid-template-columns: minmax(170px, max-content) 1fr; gap: 6px 16px; align-items: start; padding: 12px 0; border-bottom: 1px solid var(--linia); }
.def p { margin: 0; }
.def-cap { display: flex; flex-direction: column; align-items: flex-start; gap: 4px; }
.def:target { background: var(--nv-fons); }
.prec { padding-left: 20px; }
.text-llarg h3 { margin-top: 24px; }
.condicions { padding-left: 20px; }

/* Peu */
.peu { border-top: 1px solid var(--linia); background: var(--sup); }
.peu-in { max-width: 1240px; margin: 0 auto; padding: 16px; font-size: 13px; color: var(--tinta-3); overflow-wrap: anywhere; }
.peu-in code { background: transparent; padding: 0; }

@media (max-width: 900px) {
  .passos { grid-template-columns: 1fr; }
  .passos li { flex-direction: row; align-items: flex-start; }
  .pq-n { flex: none; }
}
@media (max-width: 760px) {
  .barra { position: static; }
  html { scroll-padding-top: 12px; }
  .barra-in { gap: 4px 8px; }
  .marca { width: 100%; }
  .nav a { padding: 0 12px; }
  .pindola { margin-left: auto; }
  .pagina { padding-top: 20px; }
  .cerca-rapida { margin: 16px 0 40px; }
  .llarg { display: none; }
  .curt { display: inline; }
  .mapa th, .mapa td { padding: 6px 6px; }
  .mapa td.hm { min-width: 0; }
  .taula-etiq th, .taula-etiq td { padding: 6px 4px; }
  .taula-etiq td { min-width: 0; }
  .taula-etiq .etq-nom, .taula-etiq .tc-n { display: none; }
  .taula-etiq .etq { padding-right: 2px; }
  .taula-etiq .tc-v { font-size: 13px; white-space: nowrap; }
  .mapa th:first-child { width: 48px; }
  .mapa th:last-child { width: 44px; }
  .mapa { font-size: 13px; }
  .a2, .bany small { display: none; }
  .tl-wrap { display: none; }
  .trams { display: block; }
  .anys-cap { display: none; }
  .any > summary { grid-template-columns: 56px 1fr; grid-template-areas: "any ceo" "any etq" "any prova" "any st" "any pq"; gap: 6px 10px; padding: 12px; align-items: start; }
  .a-any { grid-area: any; font-size: 17px; }
  .a-ceo { grid-area: ceo; } .a-etq { grid-area: etq; } .a-prova { grid-area: prova; } .a-st { grid-area: st; }
  .a-pq { grid-area: pq; justify-self: start; min-height: 40px; display: inline-flex; align-items: center; }
  .pq { padding: 12px; }
  .taula-emp, .taula-emp tbody, .taula-emp thead { display: block; }
  .taula-emp thead tr { display: flex; flex-wrap: wrap; gap: 4px 12px; padding: 4px 12px; background: var(--sup-2); }
  .taula-emp thead th { padding: 0; border: 0; background: transparent; }
  .taula-emp thead th:nth-child(2) { display: none; }
  .taula-emp tbody tr { display: grid; grid-template-columns: 1fr; gap: 6px; padding: 12px; border-bottom: 1px solid var(--linia); }
  .taula-emp tbody tr[hidden] { display: none; }
  .taula-emp td { padding: 0; border: 0; }
  .taula-emp td:nth-child(3) { display: flex; align-items: center; gap: 8px; }
  .taula-emp td:nth-child(3) .sub { margin: 0; }
  .taula-emp td:nth-child(4) { display: none; }
  .sr { display: grid; grid-template-columns: repeat(10, minmax(0, 1fr)); gap: 2px; width: 100%; }
  .sr i { width: auto; height: 26px; }
  .def { grid-template-columns: 1fr; }
  .versio-dl div { grid-template-columns: 1fr; }
  .p-anys { margin-left: 0; }
  .prova { padding: 12px; }
  .cita { padding: 10px 12px 10px 32px; }
  .nav-fitxes { grid-template-columns: 1fr; }
  .nav-fitxes .seg { text-align: left; }
  .heroi-xifra b { font-size: 36px; }
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { transition: none !important; animation: none !important; scroll-behavior: auto !important; }
}
@media print {
  @page { size: A4; margin: 10mm 12mm; }
  html { font-size: 8.5pt; }
  body { background: #fff; font-size: 8.5pt; line-height: 1.35; }
  * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .barra, .cerca-rapida, .filtres, .filtre-anys, .nav-fitxes, .salta, .peu, details.dades, .bs-link, .hm-escala ul { display: none !important; }
  .pagina { max-width: none; padding: 0; }
  a { color: inherit; text-decoration: none; }
  .ext { display: none; }
  h1 { font-size: 16pt; margin-bottom: 2pt; }
  h2 { font-size: 11pt; margin-bottom: 2pt; }
  .entradeta, .resposta { font-size: 9pt; margin-bottom: 3pt; max-width: none; }
  .nota, .mini, small, .ll-def, .bs-det, .bs-que, .tc-n { font-size: 7pt; }
  .versio-linia { padding: 4pt 6pt; font-size: 7.5pt; margin: 4pt 0; }
  .bloc { margin: 0 0 9pt; break-inside: avoid; }
  .bloc, .passos li, .embut, .taula-wrap, .prova { break-inside: avoid; }
  .heroi-xifra { font-size: 11pt; margin: 0 0 4pt; }
  .heroi-xifra b { font-size: 20pt; }
  .sb { height: 18pt; margin-bottom: 4pt; }
  .sb-n { font-size: 7pt; }
  .ll-estats, .ll-etiq { grid-template-columns: repeat(4, 1fr); gap: 4pt 10pt; margin-bottom: 3pt; }
  .sw { width: 13pt; height: 13pt; font-size: 7pt; }
  .embut { margin: 4pt 0; columns: 2; column-gap: 18pt; }
  .eb-pas, .eb-salt { break-inside: avoid; }
  .eb-barra { height: 8pt; }
  .eb-salt { margin: 2pt 0 3pt 6pt; font-size: 7pt; }
  .eb-salt .sw { width: 11pt; height: 11pt; }
  th, td { padding: 1.5pt 5pt; }
  .taula-etiq td { min-width: 0; }
  .tc-v, .tc-n { display: inline; margin-right: 3pt; }
  .mm { height: 3pt; margin-top: 1pt; }
  .etq b { height: 13pt; min-width: 16pt; }
  .mapa td.hm b, .mapa td.hm small { display: inline; margin-left: 3pt; }
  .mapa td.hm { padding: 1pt 5pt; }
  .bs { display: grid; grid-template-columns: repeat(2, 1fr); gap: 4pt 18pt; margin: 4pt 0; max-width: none; }
  #dubtes .bs { grid-template-columns: repeat(4, 1fr); }
  .bs li { margin: 0; break-inside: avoid; }
  .bs-barra { height: 7pt; }
  .bs-fila { margin: 1pt 0; }
  .passos { grid-template-columns: repeat(5, 1fr); gap: 4pt; margin: 4pt 0; }
  .passos li { flex-direction: column; padding: 4pt 6pt; gap: 2pt; }
  .pq-n { width: 13pt; height: 13pt; font-size: 7pt; }
  .pq-nom { font-size: 8pt; }
  .pq-t > span { font-size: 7pt; }
  .grafic { margin-top: 4pt; padding: 4pt 6pt; }
  .barres { height: 80pt; }
  .eix { bottom: 22pt; }
  .bany { height: 22pt; font-size: 7pt; }
  .bval { font-size: 7pt; }
  .versio-dl { gap: 1pt; }
  .versio-dl div { grid-template-columns: 150pt 1fr; }
  .sha { font-size: 6.5pt; }
  .docs li { margin: 0; }
  .s-dubte, .st-dubte { background: repeating-radial-gradient(circle at 2px 2px, #8a6a20 0 1px, var(--st-dubte) 1px 4px); }
  .versio .versio-linia { display: none; }
  .bloc.versio { break-inside: auto; }
  .mapa .llarg { display: none; }
  .mapa .curt { display: inline; }
  .grafic .barres { height: 58pt; }
  .versio .docs { display: none; }
  .versio-dl div { grid-template-columns: 120pt 1fr; }
  .bloc > h2 { margin-top: 0; }
  .bloc { margin-bottom: 6pt; break-inside: auto; }
  .bloc > h2 { break-after: avoid; }
  .versio-dl div { display: block; }
  .versio-dl dt, .versio-dl dd { display: inline; margin-right: 6pt; }
  .versio > .nota { margin: 2pt 0; }
  .grafic figcaption { margin-bottom: 2pt; font-size: 8pt; }
  .passos .pq-t > span { line-height: 1.2; }
  .bs-det { display: inline; }
  .ll-def { line-height: 1.2; }
  .passos li { padding: 3pt 5pt; }
}
"""

JS_CERCA = r"""/* Cercador i filtres d'Empreses. Generat per dashboard/genera_dashboard.py. Sense dependències. */
(function () {
  'use strict';
  var taula = document.getElementById('taula');
  if (!taula) return;
  var tbody = taula.tBodies[0];
  var files = Array.prototype.slice.call(tbody.rows);
  var camps = {
    q: document.getElementById('f-q'),
    e: document.getElementById('f-e'),
    t: document.getElementById('f-t'),
    p: document.getElementById('f-p'),
    m: document.getElementById('f-m')
  };
  var campM = document.getElementById('camp-m');
  var nVis = document.getElementById('n-visibles');
  var cap = document.getElementById('cap-resultat');
  var ordre = { clau: 'n', dir: 1 };
  var IDX = { acabada: 0, arxiu: 1, dubte: 2, falta: 3 };

  function norm(s) {
    return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/\s+/g, ' ').trim();
  }
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.'); }
  function conte(llista, valor) { return (' ' + (llista || '') + ' ').indexOf(' ' + valor + ' ') >= 0; }
  function st(tr) { return (tr.dataset.st || '0 0 0 0').split(' ').map(Number); }

  function aplica() {
    var termes = norm(camps.q.value).split(' ').filter(Boolean);
    var e = camps.e.value, t = camps.t.value, p = camps.p.value, m = camps.m.value;
    campM.hidden = !m;
    var n = 0;
    for (var i = 0; i < files.length; i++) {
      var tr = files[i], d = tr.dataset, ok = true;
      for (var j = 0; j < termes.length && ok; j++) { if (d.c.indexOf(termes[j]) < 0) ok = false; }
      if (ok && e && !conte(d.e, e)) ok = false;
      if (ok && p && d.p !== p) ok = false;
      if (ok && m && !conte(d.m, m)) ok = false;
      if (ok && t) {
        var s = st(tr);
        if (t === 'totes') { ok = s[0] === s[0] + s[1] + s[2] + s[3]; }
        else if (t in IDX) { ok = s[IDX[t]] > 0; }
      }
      tr.hidden = !ok;
      if (ok) n++;
    }
    nVis.textContent = fmt(n);
    cap.hidden = n > 0;
    desa();
  }

  function ordena(clau) {
    if (ordre.clau === clau) { ordre.dir = -ordre.dir; } else { ordre.clau = clau; ordre.dir = clau === 'n' ? 1 : -1; }
    var num = clau !== 'n';
    files.sort(function (a, b) {
      var x = a.dataset[clau], y = b.dataset[clau], r;
      if (num) { r = (+x) - (+y); } else { r = x < y ? -1 : x > y ? 1 : 0; }
      if (r === 0) { return a.dataset.n < b.dataset.n ? -1 : a.dataset.n > b.dataset.n ? 1 : 0; }
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
    ['q', 'e', 't', 'p', 'm'].forEach(function (k) {
      if (camps[k] && camps[k].value) params.push(k + '=' + encodeURIComponent(camps[k].value));
    });
    var hash = params.length ? '#' + params.join('&') : '';
    if (location.hash !== hash || location.search) {
      try { history.replaceState(null, '', location.pathname + hash); } catch (err) { /* res */ }
    }
  }
  function llegeix(text) {
    var h = (text || '').replace(/^[#?]/, '');
    if (!h || h.indexOf('=') < 0) return false;
    var trobat = false;
    h.split('&').forEach(function (parell) {
      var kv = parell.split('='), k = kv[0], val = '';
      try { val = decodeURIComponent((kv[1] || '').replace(/\+/g, ' ')); } catch (err) { val = ''; }
      if (camps[k]) { camps[k].value = val; trobat = true; }
    });
    return trobat;
  }
  function esborra() {
    ['q', 'e', 't', 'p', 'm'].forEach(function (k) { if (camps[k]) camps[k].value = ''; });
    aplica();
    camps.q.focus();
  }

  camps.q.addEventListener('input', aplica);
  ['e', 't', 'p', 'm'].forEach(function (k) { camps[k].addEventListener('change', aplica); });
  document.getElementById('f-reset').addEventListener('click', esborra);
  document.getElementById('f-reset-2').addEventListener('click', esborra);
  taula.querySelectorAll('thead button[data-ordre]').forEach(function (b) {
    b.addEventListener('click', function () { ordena(b.getAttribute('data-ordre')); });
  });
  var deQ = llegeix(location.search);
  llegeix(location.hash);
  window.addEventListener('hashchange', function () {
    ['q', 'e', 't', 'p', 'm'].forEach(function (k) { camps[k].value = ''; });
    llegeix(location.hash); aplica();
  });
  aplica();
  if (deQ && camps.q.value) { camps.q.focus(); }
})();
"""

JS_FITXA = r"""/* Fitxa d'empresa: filtre de proves per any i obertura dels plegables segons el hash.
   Generat per dashboard/genera_dashboard.py. Sense dependències. */
(function () {
  'use strict';
  var cont = document.getElementById('proves');
  var proves = cont ? cont.querySelectorAll('.prova[data-anys]') : [];
  var grups = cont ? cont.querySelectorAll('.grup-proves') : [];
  var xips = cont ? cont.querySelectorAll('.xip[data-filtre-any]') : [];
  var estat = document.getElementById('estat-filtre');

  function filtra(any) {
    var n = 0;
    Array.prototype.forEach.call(proves, function (p) {
      var ok = !any || (' ' + p.getAttribute('data-anys') + ' ').indexOf(' ' + any + ' ') >= 0;
      p.hidden = !ok;
      if (ok) n++;
    });
    Array.prototype.forEach.call(grups, function (g) {
      var vis = g.querySelectorAll('.prova:not([hidden])').length;
      g.hidden = vis === 0;
      if (any && vis) g.open = true;
      var comptador = g.querySelector('summary .n');
      if (comptador) comptador.textContent = vis;
    });
    Array.prototype.forEach.call(xips, function (x) { x.setAttribute('aria-pressed', x.getAttribute('data-filtre-any') === any ? 'true' : 'false'); });
    if (estat) {
      estat.textContent = any ? ('Es mostren ' + n + (n === 1 ? ' prova' : ' proves') + ' que cobreixen el ' + any + '.') : '';
    }
  }

  function obre() {
    var id = decodeURIComponent(location.hash.replace(/^#/, ''));
    if (!id) return;
    var el = document.getElementById(id);
    if (!el) return;
    if (el.tagName === 'DETAILS') { el.open = true; }
    var pare = el.parentElement;
    while (pare) {
      if (pare.tagName === 'DETAILS') { pare.open = true; }
      if (pare.hidden && pare.classList.contains('grup-proves')) { filtra(''); }
      pare = pare.parentElement;
    }
    if (el.hidden) { filtra(''); }
    el.scrollIntoView();
  }

  document.addEventListener('click', function (ev) {
    var el = ev.target.closest ? ev.target.closest('[data-filtre-any]') : null;
    if (!el || !proves.length) return;
    var any = el.getAttribute('data-filtre-any') || '';
    if (el.tagName !== 'A') ev.preventDefault();
    filtra(any);
  });
  window.addEventListener('hashchange', obre);
  obre();
})();
"""


if __name__ == "__main__":
    raise SystemExit(main())

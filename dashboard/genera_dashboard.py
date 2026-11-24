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
import json
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
# Funcions de cita que entren a la cua d'arxiu (estat/llista_urls_arxiu.py).
FUNCIONS_CUA = {"ceo", "fundador", "context", "datacio"}
PENDENTS = ROOT / "PENDENTS.md"
# CSV opcional (no existeix ara): id_document_o_font,url_wayback[,timestamp]
# Només s'usa si existeix; no s'inventa mai.
WAYBACK_EXTRA = SORTIDA / "fonts_wayback_extra.csv"

# Nom de la versió congelada. Buit mentre Jordi no el confirmi: el text diu
# només «la versió congelada», sense número.
VERSIO_CONGELADA = ""
GH_BLOB = f"{REPO_GITHUB}/blob/main"
METODOLOGIA_COMPLETA = "docs/METODOLOGIA_3_Articles_v0.10.10.md"

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
    "dubte_obert": ("Dubte obert",
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
# Frase curta de cada prova (la mateixa que el Mètode). Una sola font per als dos llocs.
REGLES_FRASE = {
    "R1": "Títol de CEO o càrrec legal equivalent (Vorstandsvorsitzender, consejero delegado, PDG, directeur général…).",
    "R2": "CEO interí.",
    "R2b": "Direcció col·legiada transitòria.",
    "R3": "Persona descrita literalment com a primer executiu quan el càrrec de CEO és vacant (el president executiu, només per aquesta via).",
    "R-SC": "Sense CEO individual a 31/10 (NA), un cop aplicades R1-R3.",
    "ceo_interval": "Interval: un document de nomenament amb data igual o anterior al 31/10 i un altre que anomena la persona CEO en una data igual o posterior.",
    "D37": "Cita de l'emissor que anomena la persona fundadora o cofundadora de la cotitzada, del grup o d'una predecessora documentada.",
    "a": "Llista tancada de fundadors en què el CEO no hi és.",
    "b": "Edat: l'any de la fundació rellevant més recent, el CEO tenia menys de 18 anys.",
    "c": "64 anys o més entre la fundació rellevant i l'inici del mandat, només si no hi ha dada d'edat.",
    "d": "Incorporació tardana: el CEO entra 3 anys o més després de la fundació, amb cita de l'ocupador anterior.",
    "e": "Origen no personal: l'entitat la va crear l'Estat o una altra empresa, sense persona fundadora.",
}
# Codis sense resum aprovat en aquest lloc: on són a la metodologia vigent. El
# número de línia es busca en generar el lloc (patró de la línia); si el patró
# no hi és, l'enllaç va al fitxer sencer. No s'hi afegeix cap descripció pròpia.
REGLES_REF = {
    "FT": (r"^6\. \*\*Raiders o refundadors", "secció 2.3, regla 6 (raiders o refundadors)"),
    "D10": (r"^\*\*Pas B: estatus de fundador", "secció 2.1, pas B (predecessores D1/D10 del PROTOCOL)"),
    "D10b_prelacio": (r"^4\. \*\*Spin-off:", "secció 2.3, regla 4 (spin-off; prelació D10b)"),
    "d_per_part": (r"^21\. \*\*Proves de l'estatus de fundador", "secció 2.3, regla 21 (proves a-e)"),
    "b_per_part": (r"^21\. \*\*Proves de l'estatus de fundador", "secció 2.3, regla 21 (proves a-e)"),
    "holding_interposada": (r"^- \*\*D36 ", "alineació del 15/11/2026, D36 (holding interposada)"),
}

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


# Nom de visualització: la columna `nom_panell` és la descripció del valor
# («Nestlé S.A. Namens-Aktien SF -,10»). Es treu el sufix de classe d'acció i el
# nominal. El nom original es manté al `title` i a la cerca; dades/ no es toca.
RE_SUFIX_VALOR = re.compile(
    r"(?:\s+|(?<=[a-z]\.)|(?<=PLC)|(?<=Group))"
    r"(?:vink\.|z\.\s?Umtausch|Reg(?:ist(?:ered|\.)|\.|(?!\w))|Bearer|Namens\w*|Namen-\w*|Nam\.|Nam-|Navne-?\w*|Namn-?\w*|"
    r"Inhaber-?\w*|Inh\.|Indehaver\w*|Ihændehaver\w*|Actions?(?!\w)|Act\.|Azioni|Acciones|Acç\w*|Acções\w*|Ações|Aand\.|Aandelen|"
    r"Aktier|Aktien(?!\w)|Akt\.|Aksjer|Shares\w*|Shs|Sh\.|Stamm\w*|Vorzug\w*|Port\.|Nom\.|Ordinary|Ord\.|Units?(?!\w)|Uts|"
    r"Depositary|Anrechte|o\.N\.|Cert\.v\.|Parts\s+Sociales|Stapled)"
    r".*$", re.I)


def nom_visible(nom: str) -> str:
    s = RE_SUFIX_VALOR.sub("", nom).strip()
    s = re.sub(r"[\s,;:/(\-]+$", "", s)
    m = re.match(r"^(.*?),\s*(The|L')$", s)
    if m:
        s = ("The " if m.group(2) == "The" else m.group(2)) + m.group(1)
    return s or nom


_LINIES_METODOLOGIA: list[str] | None = None


def ref_metodologia(codi: str) -> tuple[str, str] | None:
    """(URL a la línia de la metodologia vigent, text de la referència) per als
    codis sense resum aprovat. Si no troba la línia, l'URL és el fitxer sencer."""
    global _LINIES_METODOLOGIA
    if codi not in REGLES_REF:
        return None
    patro, text = REGLES_REF[codi]
    if _LINIES_METODOLOGIA is None:
        p = ROOT / METODOLOGIA_COMPLETA
        _LINIES_METODOLOGIA = p.read_text(encoding="utf-8").splitlines() if p.exists() else []
    url = f"{GH_BLOB}/{METODOLOGIA_COMPLETA}"
    for i, linia in enumerate(_LINIES_METODOLOGIA, start=1):
        if re.search(patro, linia):
            return f"{url}?plain=1#L{i}", text
    return url, text


def carrega_anomena():
    """La mateixa regla que estat/estat_files.py per decidir si una cita anomena
    el CEO (s'importa el mòdul, sense escriure bytecode a estat/)."""
    import importlib.util
    prev = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec = importlib.util.spec_from_file_location("estat_files_dashboard", ROOT / "estat" / "estat_files.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        sys.dont_write_bytecode = prev
    return lambda cita, nom: mod.anomena(mod.norm(cita), nom)


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
    # URL a la cua d'arxiu, calculades del registre actual amb la mateixa regla
    # que estat/llista_urls_arxiu.py (així no depèn que el CSV estigui al dia).
    urls_info: set[str] = set()
    urls_verif: set[str] = set()
    for r in registre:
        url = (r.get("url_font") or "").strip()
        if not url.lower().startswith(("http://", "https://")) or not (r.get("cita_literal") or "").strip():
            continue
        if r.get("funcio_cita") not in FUNCIONS_CUA:
            continue
        if r.get("cita_verificada_a_captura") == "si":
            urls_verif.add(url)
        urls_info.add(url)
    reg["urls_cua"] = len(urls_info - urls_verif)

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
    nom_base = files[-1]["nom_panell"].replace("​", "").strip()
    nom = nom_visible(nom_base)
    altres_noms = []       # noms originals de la base (per a la cerca)
    altres_visibles = []   # els mateixos, nets, si són diferents del nom que es mostra
    for r in files:
        n = r["nom_panell"].replace("​", "").strip()
        if n != nom_base:
            afegeix(altres_noms, n)
            if nom_visible(n) != nom:
                afegeix(altres_visibles, nom_visible(n))

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
        "nom_base": nom_base,
        "altres_noms": altres_noms,
        "altres_visibles": altres_visibles,
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
    # Repartiment de cada mancança entre els quatre estats exclusius (conciliació).
    manc_cat = {k: Counter(f["cat"] for f in files if k in f["mancances"]) for k in MANCANCES}
    dubte_cat = Counter(f["cat"] for f in files if f["dubtes"])
    return {
        "n_isin": len(emp), "tot": tot, "cat": cat, "embut": embut,
        "c1": c1, "c2": c2, "c3": c3, "c4": c4,
        "per_etiq": per_etiq, "per_any": dict(sorted(per_any.items())),
        "etiq_any": dict(sorted(etiq_any.items())),
        "etiq": Counter(f["lletra"] for f in files),
        "mancances": mancances,
        "manc_cat": manc_cat,
        "dubte_cat": dubte_cat,
        "dubtes": dubtes,
        "files_amb_dubte": sum(bool(f["dubtes"]) for f in files),
        "dubtes_tancats": compta_files_csv(DUBTES_TANCATS) or 0,
        "urls_cua": model["registre"]["urls_cua"],
        "urls_cua_fitxer": compta_files_csv(URLS_ARXIU),
        "columna_antiga": sum(f["est"]["c2_fundador"] == "ok_columna_antiga" for f in files),
        "interval": sum("interval" in f["est"]["c1_tipus"] for f in files),
        "registre": model["registre"],
        "emp_totes_acabades": sum(e["st"]["acabada"] == len(e["files"]) for e in emp.values()),
        "emp_estat": Counter(k for e in emp.values() for k in ORDRE_ESTATS if e["st"][k]),
        "emp_etiq": Counter(l for e in emp.values() for l in ORDRE_ETIQ if e["recompte"][l]),
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
        self.anomena = carrega_anomena()


def curt(sha: str, n: int = 7) -> str:
    return sha[:n] if len(sha) > n else sha


def data_ca(d: str) -> str:
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", d or "")
    return f"{m.group(3)}/{m.group(2)}/{m.group(1)}" if m else (d or "data desconeguda")


def nom_versio() -> str:
    return f"la versió congelada ({VERSIO_CONGELADA})" if VERSIO_CONGELADA else "la versió congelada"


# Icones de la navegació (decoratives; al mòbil, a les pestanyes inferiors).
ICONES_NAV = {
    "estat": '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M3 16h14M5 13V9m4 4V5m4 8v-6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "empreses": '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M4 4h12M4 8h12M4 12h12M4 16h8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "metode": '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M5 3h8l3 3v11H5zM8 9h5M8 12h5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
}
ICONA_LUPA = ('<svg class="cb-lupa" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="8.5" cy="8.5" r="5.5" fill="none" '
              'stroke="currentColor" stroke-width="1.8"/><path d="m13 13 4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>')
# Tema: l'opció desada (clar o fosc) s'aplica abans de pintar; si no n'hi ha, mana prefers-color-scheme.
SCRIPT_TEMA = ("<script>(function(d){d.className+=' js';try{var t=localStorage.getItem('fc-tema');"
               "if(t==='dark'||t==='light'){d.setAttribute('data-theme',t);}}catch(e){}})(document.documentElement);</script>")


def combobox(id_: str, prefix: str, etiqueta: str, placeholder: str, *, local: bool = False,
             cls: str = "", boto: bool = False, etiqueta_visible: bool = False, valor_nom: str = "q") -> str:
    """Cercador amb suggeriments (patró combobox de l'ARIA APG). Sense JS, és un
    formulari normal que porta a empreses.html?q=…; amb `local`, filtra la llista
    de la mateixa pàgina i el Retorn no navega."""
    lab_cls = "cb-et" if etiqueta_visible else "vh"
    accio = "" if local else f' action="{prefix}empreses.html" method="get"'
    nom = "" if local else f' name="{valor_nom}"'
    submit = '<button type="submit" class="boto cb-boto">Cerca</button>' if boto else ""
    kbd = '' if local or boto else '<kbd class="cb-kbd" aria-hidden="true">/</kbd>'
    extra = ' data-local onsubmit="return false"' if local else ""
    return (f'<form class="cb {cls}" role="search"{accio} data-combobox{extra} data-prefix="{prefix}">'
            f'<label class="{lab_cls}" for="{id_}">{esc(etiqueta)}</label>'
            f'<div class="cb-camp">{ICONA_LUPA}<input type="search" id="{id_}"{nom} autocomplete="off" spellcheck="false" '
            f'placeholder="{esc(placeholder)}" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="{id_}-llista">'
            f'{kbd}{submit}</div>'
            f'<ul class="cb-llista" id="{id_}-llista" role="listbox" aria-label="Suggeriments" hidden></ul>'
            f'<span class="vh cb-viu" aria-live="polite"></span></form>')


def pagina(ctx: Context, *, titol: str, descripcio: str, cos: str, prefix: str,
           actiu: str, scripts: tuple[str, ...] = (), ample: bool = False, cap_extra: str = "",
           cls_body: str = "") -> str:
    nav = []
    for clau, href, text in (("estat", "index.html", "Estat"),
                             ("empreses", "empreses.html", "Empreses"),
                             ("metode", "metodologia.html", "Mètode")):
        cur = ' aria-current="page"' if clau == actiu else ""
        nav.append(f'<a href="{prefix}{href}"{cur}>{ICONES_NAV[clau]}<span>{text}</span></a>')
    js = "".join(f'<script src="{prefix}assets/{s}" defer></script>' for s in ("comu.js", *scripts))
    data = data_ca(ctx.data_commit)
    body = f' class="{cls_body}"' if cls_body else ""
    cerca = combobox("cerca-cap", prefix, "Busca una empresa, un ISIN o un CEO", "Busca empresa, ISIN o CEO", cls="cb-cap")
    return f"""<!doctype html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{esc(titol)}</title>
<meta name="description" content="{esc(descripcio)}">
{SCRIPT_TEMA}
<link rel="stylesheet" href="{prefix}assets/style.css">
{cap_extra}{js}
</head>
<body{body}>
<a class="salta" href="#contingut">Salta al contingut</a>
<header class="barra">
<div class="barra-in">
<a class="marca" href="{prefix}index.html"><b>Fundadors-CEO · STOXX Europe 600</b><small>Base de dades de doctorat · 2016–2025</small></a>
{cerca}
<a class="pindola" href="{prefix}index.html#versio">En revisió · dades del {esc(data)}</a>
<button type="button" class="tema" aria-pressed="false" title="Canvia entre el mode clar i el mode fosc"><span class="tema-i" aria-hidden="true"></span><span class="vh">Mode fosc</span></button>
<nav class="nav" aria-label="Navegació principal">{''.join(nav)}</nav>
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
DEF_ND = "Hi ha un CEO identificat però cap prova concloent de sí ni de no, o les proves es contradiuen."
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


def dades_taula(cap: list[str], files: list[list[str]], caption: str, resum: str = "Mostra les dades en una taula") -> str:
    th = "".join(f'<th scope="col"{" class=num" if i else ""}>{c}</th>' for i, c in enumerate(cap))
    cos = "".join(
        "<tr>" + "".join((f'<th scope="row">{c}</th>' if i == 0 else f'<td class="num">{c}</td>') for i, c in enumerate(fila)) + "</tr>"
        for fila in files
    )
    return (f'<details class="dades"><summary>{esc(resum)}</summary>'
            f'<div class="taula-wrap"><table class="taula-simple"><caption class="vh">{esc(caption)}</caption>'
            f'<thead><tr>{th}</tr></thead><tbody>{cos}</tbody></table></div></details>')


# ---------------------------------------------------------------------------
# Components de l'Estat
# ---------------------------------------------------------------------------


def barra_apilada(segs: list[tuple[str, int, str]], total: int, etiqueta: str, cls: str) -> str:
    """Barra al 100 % de segments (clau, n, nom). Els segments a 0 no es pinten.
    Les xifres són a la llegenda (amb la mateixa precisió), no dins dels segments."""
    parts = []
    for clau, n, nom in segs:
        if not n:
            continue
        parts.append(f'<span class="sb-s {cls}-{clau}" style="flex-grow:{n}" title="{esc(nom)}: {fmt_int(n)} ({fmt_pct(n, total)})"></span>')
    aria = etiqueta + ": " + "; ".join(f"{nom} {fmt_int(n)} ({fmt_pct(n, total)})" for _, n, nom in segs)
    return f'<div class="sb" role="img" aria-label="{esc(aria)}">{"".join(parts)}</div>'


def llegenda_estats(cat: Counter, total: int) -> str:
    items = []
    for k in ORDRE_ESTATS:
        icona, nom, _, defi = ESTATS[k]
        items.append(
            f'<li><span class="ll-cap"><span class="sw s-{k}" aria-hidden="true">{icona}</span><b>{esc(nom)}</b></span>'
            f'<span class="ll-n"><span class="ll-xifra">{fmt_int(cat[k])}</span> <span class="ll-pc">{fmt_pct(cat[k], total)}</span></span>'
            f'<span class="ll-def">{esc(defi)}</span></li>'
        )
    return f'<ul class="ll-estats">{"".join(items)}</ul>'


def embut(E: dict) -> str:
    tot, c12, c124, acab = E["embut"]
    passos = [
        ("Panell", tot, ""),
        ("Amb cita de CEO i de fundador", c12, "falta"),
        ("… i coherents, sense dubtes oberts", c124, "dubte"),
        ("… i amb la cita verificada a la còpia de Wayback, és a dir, acabades", acab, "arxiu"),
    ]
    codis = ["", "C1 i C2", "C4", "C3"]
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
        tit = f' title="Condicions {codis[i]}"' if codis[i] else ""
        items.append(
            f'<li class="eb-pas{cls}"><span class="eb-nom"{tit}>{esc(nom)}</span>'
            f'<span class="eb-fila"><span class="eb-barra" aria-hidden="true" style="width:{pct:.2f}%"></span><span class="eb-val">{val}</span></span></li>'
        )
        prev = n
    gran = max(salts, key=lambda x: x[0]) if salts else (0, "")
    frase = ""
    if gran[0]:
        nom_pas = {"falta": "el de l'evidència", "dubte": "el dels dubtes", "arxiu": "el de l'arxiu"}[gran[1]]
        frase = (f'<p class="resposta">El pas on es queden més files és <b>{esc(nom_pas)}</b>: '
                 f'{fmt_int(gran[0])} files ({esc(ESTATS[gran[1]][1].lower())}).</p>')
    taula = dades_taula(["Pas", "Files", "% del panell"],
                        [[esc(nom), fmt_int(n), fmt_pct(n, tot)] for nom, n, _ in passos],
                        "Files que superen cada pas de l'embut")
    return f'{frase}<ol class="embut">{"".join(items)}</ol>{taula}'


def taula_etiquetes(E: dict) -> str:
    # (clau, nom planer, nom curt per al mòbil, codi i definició per al title)
    cols = [("C1", "Cita de CEO", "Cita CEO", "C1: té cita vàlida de CEO"),
            ("C2", "Prova de fundador", "Prova fund.", "C2: té prova de fundador o de no fundador"),
            ("C4", "Sense dubtes", "Sense dubtes", "C4: coherent amb la base i sense dubtes oberts"),
            ("C3", "Verificada a Wayback", "Wayback", "C3: cita verificada a la còpia de Wayback"),
            ("acabada", "Acabades", "Acab.", "Compleix les quatre condicions")]
    th = "".join(f'<th scope="col" class="num" title="{esc(t)}"><span class="llarg">{esc(n)}</span><span class="curt">{esc(c)}</span></th>'
                 for k, n, c, t in cols)
    files = []
    for l in ["F", "P", "NA", "ND"]:
        d = E["per_etiq"][l]
        n = d["files"]
        cel = []
        for k, _, _, _ in cols:
            v = d[k]
            pct = 100 * v / n if n else 0
            cel.append(f'<td class="num"><span class="tc-v"><span class="llarg">{fmt_pct(v, n)}</span><span class="curt">{fmt_pct(v, n, 0)}</span></span><span class="tc-n">{fmt_int(v)}</span>'
                       f'<span class="mm" aria-hidden="true"><i style="width:{pct:.1f}%"></i></span></td>')
        files.append(f'<tr><th scope="row">{badge_etiq(l)}<span class="tc-files">{fmt_int(n)} {"fila" if n == 1 else "files"}</span></th>'
                     f'<td class="num col-files">{fmt_int(n)}</td>{"".join(cel)}</tr>')
    return (f'<div class="taula-wrap"><table class="taula-etiq"><caption class="vh">Condicions complertes per etiqueta FounderCEO</caption>'
            f'<thead><tr><th scope="col">Etiqueta</th><th scope="col" class="num col-files">Files</th>{th}</tr></thead>'
            f'<tbody>{"".join(files)}</tbody></table></div>'
            '<p class="nota-clara">Cada columna es compta per separat; l\'última és la combinació de totes.</p>')


def taula_anys(E: dict) -> str:
    """Taula any × estat: el número i el % de l'any, amb una barra de longitud en
    el color de l'estat (sense intensitat de fons: el text queda sempre sobre la
    superfície i la comparació es fa per longitud)."""
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
            cel.append(f'<td class="num ta"><b>{fmt_int(n)}</b> <small>{fmt_pct(n, tot, 0)}</small>'
                       f'<span class="mm mk-{k}" aria-hidden="true"><i style="width:{pct:.1f}%"></i></span></td>')
        files.append(f'<tr><th scope="row">{a}</th>{"".join(cel)}<td class="num">{fmt_int(tot)}</td></tr>')
    return (f'<div class="taula-wrap"><table class="taula-anys"><caption class="vh">Files de cada any segons l\'estat (nombre i % de l\'any)</caption>'
            f'<thead><tr><th scope="col">Any</th>{th}<th scope="col" class="num">Total</th></tr></thead>'
            f'<tbody>{"".join(files)}</tbody></table></div>'
            '<p class="nota">Sota cada xifra, una barra amb el % de les files de l\'any, en el color de l\'estat.</p>')


def resposta_anys(E: dict) -> str:
    per_any = E["per_any"]
    if not per_any:
        return ""
    maxim = max(c["acabada"] for c in per_any.values())
    if not maxim:
        return '<p class="resposta">Encara cap any no té cap fila acabada.</p>'
    millors = [a for a, c in per_any.items() if c["acabada"] == maxim]
    if len(millors) == 1:
        a = millors[0]
        c = per_any[a]
        return (f'<p class="resposta">L\'any amb més files acabades és el {a}: {fmt_int(c["acabada"])} de {fmt_int(c["total"])} '
                f'({fmt_pct(c["acabada"], c["total"])}).</p>')
    noms = ", ".join(f"el {a}" for a in millors[:-1]) + f" i el {millors[-1]}"
    totals = {per_any[a]["total"] for a in millors}
    if len(totals) == 1:
        t = totals.pop()
        detall = f"{fmt_int(maxim)} de {fmt_int(t)} cadascun ({fmt_pct(maxim, t)})"
    else:
        detall = f"{fmt_int(maxim)} cadascun (" + "; ".join(f"{a}: {fmt_pct(maxim, per_any[a]['total'])}" for a in millors) + ")"
    return f'<p class="resposta">Els anys amb més files acabades són {noms}: {detall}.</p>'


def barres_simples(files: list[tuple[str, int, str]], maxim: int, etiqueta: str) -> str:
    """Barres horitzontals d'una sola sèrie: (nom en HTML, valor, detall en HTML)."""
    items = []
    for nom, n, detall in files:
        pct = 100 * n / maxim if maxim else 0
        items.append(
            f'<li><span class="bs-nom">{nom}</span>'
            f'<span class="bs-fila"><span class="bs-barra" aria-hidden="true" style="width:{pct:.2f}%"></span><span class="bs-val">{fmt_int(n)}</span></span>'
            f'{detall}</li>'
        )
    return f'<ul class="bs" aria-label="{esc(etiqueta)}">{"".join(items)}</ul>'


def conciliacio(n: int, per_cat: Counter) -> str:
    """«5.733 = 4.472 només falta l'arxiu + 1.261 falta evidència»: reparteix les
    files d'una mancança entre els quatre estats exclusius de la barra principal."""
    parts = [f"{fmt_int(per_cat[k])} {ESTATS[k][1].lower()}" for k in ORDRE_ESTATS if per_cat[k]]
    if sum(per_cat.values()) != n:
        atura("la conciliació de les mancances no quadra amb els quatre estats")
    if len(parts) < 2:
        return f"Les {fmt_int(n)} files són a l'estat «{ESTATS[next(k for k in ORDRE_ESTATS if per_cat[k])][1]}»." if parts else ""
    return f"Per estat de la fila: {fmt_int(n)} = " + " + ".join(parts) + "."


def barres_mancances(E: dict) -> str:
    tot = E["tot"]
    cua = fmt_int(E["urls_cua"])
    files = []
    for k, (nom, que) in MANCANCES.items():
        n = E["mancances"][k]
        conc = conciliacio(n, E["manc_cat"][k]) if n else ""
        detall = (f'<span class="bs-det">{fmt_int(n)} files ({fmt_pct(n, tot)}). {esc(conc)}</span>'
                  f'<span class="bs-que"><b>Què s\'hi fa:</b> {esc(que.format(cua=cua))}</span>'
                  f'<a class="bs-link" href="empreses.html#m={k}">Mostra les empreses</a>')
        files.append((f'<span title="{esc(k)}">{esc(nom)}</span>', n, detall))
    return barres_simples(files, tot, "Files amb cada mancança, sobre el total de files")


def barres_dubtes(E: dict, pend: dict) -> str:
    if not E["dubtes"]:
        return '<p class="resposta">No hi ha dubtes oberts.</p>'
    # De més a menys files; «ND obert» al final.
    ordre = sorted((k for k in E["dubtes"] if k != "ND_obert"), key=lambda k: (-E["dubtes"][k], k))
    if E["dubtes"]["ND_obert"]:
        ordre.append("ND_obert")
    maxim = max(E["dubtes"].values())
    files = []
    for k in ordre:
        nom = ORIGENS_DUBTE.get(k, (k, ""))[0]
        sec = ORIGENS_DUBTE.get(k, ("", ""))[1]
        url = url_pendents(pend, k)
        link = (f'<a class="bs-link" href="{esc(url)}" target="_blank" rel="noopener noreferrer" title="Secció «{esc(sec)}»">'
                f'Veure la secció al fitxer de dubtes<span class="ext" aria-hidden="true">↗</span></a>') if sec else ""
        files.append((f'<span title="{esc(k)}">{esc(nom)}</span>', E["dubtes"][k], link))
    return barres_simples(files, maxim, "Files amb dubte obert, per origen")


def passos_qualitat(E: dict) -> str:
    R = E["registre"]
    passos = [
        ("Font A/B i cita literal", f'<b>{fmt_int(R["entrades"])}</b> entrades al registre'),
        ("Document obert sencer i cita trobada",
         f'<b>{fmt_int(R["[V]"])}</b> amb la cita trobada al document obert <span title="marca_veritat = [V]">([V])</span> · '
         f'{fmt_int(R["[NV]"])} encara no comprovades <span title="marca_veritat = [NV]">([NV])</span>'),
        ("Còpia a Wayback",
         f'<b>{fmt_int(R["wb_url"])}</b> entrades amb URL Wayback'
         + (f' (i {fmt_int(R["wb_pendent"])} marcades «pendent de verificació externa»)' if R["wb_pendent"] else "")
         + f'; <b>{fmt_int(R["capt_si"])}</b> amb la cita verificada per script a la còpia arxivada'
         + f'; {fmt_int(R["urls_cua"])} URL a la cua d\'arxiu'),
        ("Validadors automàtics a cada PR", '<span title="valida_pr.py, comprova_enllacos_cites.py, estat_files.py --comprova">Tres scripts: format del registre, enllaços de les cites i estat de les files</span>'),
        ("Revisió i fusió de Jordi", "i de Doctorat, si cal"),
    ]
    items = "".join(f'<li><span class="pq-n" aria-hidden="true">{i}</span><span class="pq-t"><b class="pq-nom">{esc(t)}</b><span>{x}</span></span></li>'
                    for i, (t, x) in enumerate(passos, start=1))
    return f'<ol class="passos">{items}</ol><p class="nota-clara">Xifres d\'entrades del registre, no de files.</p>'


def grafic_f_per_any(E: dict) -> str:
    per_any = E["etiq_any"]
    anys = list(per_any)
    maxim = max((per_any[a]["F"] for a in anys), default=0)
    pas = 10 if maxim <= 60 else 20
    sostre = max(pas, -(-maxim // pas) * pas)
    eix = "".join(
        f'<span class="tick{"" if t in (0, sostre) or 2 * t == sostre else " tick-menor"}" style="bottom:{100 * t / sostre:.2f}%"><span>{t}</span></span>'
        for t in range(0, sostre + 1, pas)
    )
    cols = []
    tips = []
    for a in anys:
        f, tot = per_any[a]["F"], per_any[a]["total"]
        alt = 100 * f / sostre if sostre else 0
        tip = f"{a}: {fmt_int(f)} files F de {fmt_int(tot)} ({fmt_pct(f, tot)})"
        tips.append(f"{a} {fmt_int(f)} ({fmt_pct(f, tot)})")
        cols.append(
            f'<div class="bcol" tabindex="0" role="img" aria-label="{esc(tip)}">'
            f'<div class="barea" aria-hidden="true"><span class="bar" style="height:{alt:.2f}%"><span class="bval">{fmt_int(f)}</span></span></div>'
            f'<span class="bany" aria-hidden="true"><span><span class="a2">{str(a)[:2]}</span>{str(a)[2:]}</span><small>{fmt_pct(f, tot)}</small></span><span class="tip" aria-hidden="true">{esc(tip)}</span></div>'
        )
    taula = dades_taula(["Any", "Files F", "Files al panell", "% F"],
                        [[str(a), fmt_int(per_any[a]["F"]), fmt_int(per_any[a]["total"]), fmt_pct(per_any[a]["F"], per_any[a]["total"])] for a in anys],
                        "Files F per any")
    aria = "Files F per any: " + "; ".join(tips)
    return (f'<figure class="grafic"><figcaption class="h3">Files F per any <span class="nota llarg">(sota cada any, el % de files F)</span></figcaption>'
            f'<div class="barres" role="group" aria-label="{esc(aria)}">'
            f'<div class="eix" aria-hidden="true">{eix}</div><div class="bcols">{"".join(cols)}</div></div>{taula}</figure>')


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


def seccio(id_: str, titol: str, resposta: str, cos: str, cls: str = "", n: int | None = None) -> str:
    num = f'<span class="bloc-n" aria-hidden="true">{n}</span>' if n else ""
    return (f'<section class="bloc{(" " + cls) if cls else ""}" id="{id_}" aria-labelledby="h-{id_}">'
            f'<header class="bloc-cap">{num}<h2 id="h-{id_}">{esc(titol)}</h2></header>'
            f'<div class="bloc-cos">{resposta}{cos}</div></section>')


def dreceres(E: dict) -> str:
    """Targetes clicables amb el recompte de files i el d'empreses del filtre
    que obren (Empreses filtra per empresa: «amb alguna fila així»)."""
    cat, ee, et = E["cat"], E["emp_estat"], E["emp_etiq"]
    targetes = [(k, f"#t={k}", ESTATS[k][0], ESTATS[k][1], cat[k], ee[k], "amb alguna fila així") for k in ORDRE_ESTATS]
    targetes.append(("F", "#e=F", "F", "Fundadors-CEO (F)", E["etiq"]["F"], et["F"], "amb algun any F"))
    items = []
    for k, hash_, icona, nom, files, emps, que in targetes:
        sw = f'<span class="sw e-F" aria-hidden="true">F</span>' if k == "F" else f'<span class="sw s-{k}" aria-hidden="true">{icona}</span>'
        items.append(
            f'<li><a class="drec" href="empreses.html{hash_}">'
            f'<span class="drec-cap">{sw}<span class="drec-nom">{esc(nom)}</span></span>'
            f'<span class="drec-n"><b>{fmt_int(files)}</b> {"fila" if files == 1 else "files"}</span>'
            f'<span class="drec-emp"><b>{fmt_int(emps)}</b> {"empresa" if emps == 1 else "empreses"} {esc(que)} <span aria-hidden="true">→</span></span></a></li>')
    return ('<h3 class="vh">Dreceres a Empreses</h3>'
            f'<ul class="dreceres">{"".join(items)}</ul>'
            '<p class="nota">Cada targeta compta files; l\'enllaç obre Empreses amb el filtre aplicat, que compta empreses.</p>')


REDIRECCIO_HASH = ("<script>(function(){var h=location.hash;"
                   "if(/^#(?:.*&)?(?:q|e|c|p|s|v|t|m)=/.test(h)){location.replace('empreses.html'+h);}})();</script>\n")


ISIN_EXEMPLES = ("FR0000121014", "CH0038863350")


def pagina_estat(ctx: Context, E: dict) -> str:
    tot = E["tot"]
    cat = E["cat"]
    acab = cat["acabada"]
    # 3. Quantes files estan acabades
    segs = [(k, cat[k], ESTATS[k][1]) for k in ORDRE_ESTATS]
    if acab:
        heroi = (f'<p class="heroi-xifra"><b>{fmt_int(acab)}</b> <span>de {fmt_int(tot)} files acabades '
                 f'({fmt_pct(acab, tot)})</span></p>')
    else:
        heroi = '<p class="heroi-xifra">Encara cap fila no compleix les quatre condicions.</p>'
    acabades = (heroi + dreceres(E) + barra_apilada(segs, tot, "Files segons l'estat", "s")
                + llegenda_estats(cat, tot)
                + '<p class="nota">Cada fila compta en un sol estat: el primer pas de l\'embut que no supera.</p>')
    # 4. Embut
    detall = (f'<p class="nota-clara">Comptades per separat: <span title="C1">cita de CEO</span> {fmt_int(E["c1"])} ({fmt_pct(E["c1"], tot)}) · '
              f'<span title="C2">prova de fundador</span> {fmt_int(E["c2"])} '
              f'({fmt_pct(E["c2"], tot)}), de les quals {fmt_int(E["columna_antiga"])} només amb la cita antiga de la base '
              "(sense còpia arxivada).</p>")
    # 5. Etiquetes
    F = E["per_etiq"]["F"]
    resp_etiq = (f'<p class="resposta">Per exemple, de les {fmt_int(F["files"])} files F, {fmt_pct(F["C2"], F["files"])} tenen prova de fundador '
                 f'però {fmt_pct(F["C3"], F["files"])} tenen la cita verificada a la còpia de Wayback; acabades: {fmt_int(F["acabada"])}.</p>')
    # 6. Any per any
    resp_any = resposta_anys(E)
    # 7. Mancances
    resp_m = (f'<p class="resposta">La mancança més freqüent és «{esc(MANCANCES[E["mancances"].most_common(1)[0][0]][0])}»: '
              f'{fmt_int(E["mancances"].most_common(1)[0][1])} files.</p>' if E["mancances"] else
              '<p class="resposta">No hi ha cap mancança.</p>')
    nota_m = ('<p class="nota-clara">Una fila pot tenir més d\'una mancança. Sota cada barra, les files es reparteixen '
              "segons el seu estat a la barra de dalt («Quantes files estan acabades?»), on cada fila compta una sola vegada.</p>")
    # 8. Dubtes
    resp_d = ""
    if E["dubtes"]:
        resp_d = (f'<p class="resposta">{fmt_int(E["files_amb_dubte"])} files tenen algun dubte obert. '
                  f'Dubtes tancats: <b>{fmt_int(E["dubtes_tancats"])}</b>.</p>'
                  f'<p class="nota-clara">{esc(conciliacio(E["files_amb_dubte"], E["dubte_cat"]))} '
                  "A la barra de dalt, les files que també tenen falta d'evidència compten a «Falta evidència».</p>")
    nota_d = ('<p class="nota-clara">Una fila pot tenir dubtes de més d\'un origen. Aquí només es compten les files: el text dels dubtes '
              f'és al fitxer de dubtes de la base ({enllac_ext(f"{GH_BLOB}/PENDENTS.md", "PENDENTS.md")}, a GitHub).</p>') if E["dubtes"] else ""
    # 10. Resultats provisionals
    et = E["etiq"]
    segs_e = [(l, et[l], f"{l} · {NOM_ETIQ[l]}") for l in ["F", "P", "NA", "ND"]]
    ll_e = "".join(f'<li><span class="sw e-{l}" aria-hidden="true">{l}</span><b>{esc(NOM_ETIQ[l])}</b> '
                   f'<span class="ll-n">{fmt_int(et[l])} · {fmt_pct(et[l], tot)}</span></li>' for l in ["F", "P", "NA", "ND"])
    resultats = (barra_apilada(segs_e, tot, "Files segons l'etiqueta FounderCEO", "e")
                 + f'<ul class="ll-etiq">{ll_e}</ul>' + grafic_f_per_any(E))

    cerca = combobox("q", "", "Troba l'evidència d'una empresa", "LVMH, Nestlé, Arnault…", cls="cb-gran", boto=True, etiqueta_visible=True)
    exemples = ('<p class="exemples">Exemples: <a href="empreses/FR0000121014.html">LVMH</a> '
                '<a href="empreses/CH0038863350.html">Nestlé</a> <a href="empreses.html?q=Arnault">Arnault</a></p>')
    cos = f"""<section class="obertura">
<div class="ob-text">
<h1>En quin punt és la base</h1>
<p class="entradeta">{fmt_int(tot)} files empresa-any ({fmt_int(E["n_isin"])} empreses, 2016–2025). Per a cada fila: qui era el CEO el 31 d'octubre i si era fundador, amb una cita literal, l'URL original i una còpia a Wayback Machine.</p>
{linia_versio(ctx)}
</div>
<div class="cerca-rapida">
{cerca}
<p class="cr-ajuda">Busca per nom, ISIN o CEO. Des de la fitxa, la cita i la còpia arxivada són a un clic.</p>
{exemples}
</div>
</section>
{seccio("acabades", "Quantes files estan acabades?", "", acabades, n=1)}
{seccio("embut", "On es queden les files?", "", embut(E) + detall, n=2)}
{seccio("etiquetes", "Com està cada etiqueta?", resp_etiq, taula_etiquetes(E), n=3)}
{seccio("anys", "Com va cada any?", resp_any, taula_anys(E), n=4)}
{seccio("mancances", "Què falta i què s'hi fa?", resp_m, nota_m + barres_mancances(E), n=5)}
{seccio("dubtes", "D'on venen els dubtes oberts?", resp_d, barres_dubtes(E, ctx.pend) + nota_d, n=6)}
{seccio("qualitat", "Com es controla la qualitat?", '<p class="resposta">Cada cita passa per cinc controls abans de comptar com a acabada.</p>', passos_qualitat(E), n=7)}
{seccio("resultats", "Resultats provisionals", '<p class="resposta etiqueta-prov">Provisional: pot canviar fins a ' + nom_versio() + '.</p>', resultats, n=8)}
{seccio("versio", "Sobre aquestes dades", linia_versio(ctx), sobre_dades(ctx), "versio", n=9)}"""
    return pagina(ctx, titol="Estat de la base · Fundadors-CEO STOXX Europe 600",
                  descripcio="En quin punt és la base Fundadors-CEO: files acabades, embut, mancances, dubtes i control de qualitat.",
                  cos=cos, prefix="", actiu="estat", cap_extra=REDIRECCIO_HASH, cls_body="p-estat")


# ---------------------------------------------------------------------------
# Empreses
# ---------------------------------------------------------------------------

LLETRA_ESTAT = {"acabada": "a", "arxiu": "r", "dubte": "d", "falta": "f"}


# Nom de cada estat amb concordança de nombre (singular, plural).
ESTAT_NOMBRE = {
    "acabada": ("acabada", "acabades"),
    "arxiu": ("només falta l'arxiu", "només falten l'arxiu"),
    "dubte": ("amb dubte", "amb dubte"),
    "falta": ("falta evidència", "falta evidència"),
}


def estat_n(k: str, v: int) -> str:
    sing, plur = ESTAT_NOMBRE[k]
    return f"{fmt_int(v)} {sing if v == 1 else plur}"


def text_estat_empresa(e: dict) -> str:
    n = len(e["files"])
    parts = [f'{fmt_int(e["st"]["acabada"])} de {fmt_int(n)} {"fila acabada" if n == 1 and e["st"]["acabada"] == 1 else "files acabades"}']
    for k in ("arxiu", "dubte", "falta"):
        v = e["st"][k]
        if v:
            parts.append(estat_n(k, v))
    return " · ".join(parts)


def aria_serie(e: dict) -> str:
    """Un sol aria-label per a la sèrie: etiquetes, recompte per estat (amb les
    acabades encara que siguin 0) i l'estat per trams d'anys."""
    r, st, n = e["recompte"], e["st"], len(e["files"])
    etiq = ", ".join(f"{l} {r[l]} de {n} {'any' if n == 1 else 'anys'}" for l in ORDRE_ETIQ if r[l])
    estats = ", ".join([estat_n("acabada", st["acabada"])] + [estat_n(k, st[k]) for k in ("arxiu", "dubte", "falta") if st[k]])
    trams: list[list] = []
    for f in e["files"]:
        clau = (f["lletra"], f["cat"])
        if trams and trams[-1][2] == clau and trams[-1][1] == f["any"] - 1:
            trams[-1][1] = f["any"]
        else:
            trams.append([f["any"], f["any"], clau])
    una = len({f["lletra"] for f in e["files"]}) == 1  # amb una sola etiqueta, no cal repetir-la
    per_anys = "; ".join(f"{a if a == b else f'{a}–{b}'}{'' if una else ' ' + c[0] + ','} {ESTATS[c[1]][1].lower()}"
                         for a, b, c in trams)
    return f"{etiq}; {estats}. Per anys: {per_anys}"


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
            # Casella sense classe = l'empresa no era a l'índex aquell any (pesa menys).
            cel.append(f'<i class="{f["lletra"]} {LLETRA_ESTAT[f["cat"]]}">{f["lletra"]}</i>' if f else '<i></i>')
        r = e["recompte"]
        n = len(e["files"])
        st = e["st"]
        darrer = e["files"][-1]
        ceo_darrer = darrer["ceos_text"].replace("|", " · ") or "sense CEO"
        noms_c = [e["nom_base"], *e["altres_noms"]]
        if norm_cerca(e["nom"]) not in norm_cerca(" ".join(noms_c)):
            noms_c.insert(0, e["nom"])
        cerca = norm_cerca(" ".join([*noms_c, e["isin"], *e["ceos_noms"]]))
        st_curt = f'{st["acabada"]}/{n} acabades' + "".join(f' · {estat_n(k, st[k])}' for k in ("dubte", "falta") if st[k])
        files_html.append(
            f'<tr data-c="{esc(cerca)}" data-e="{" ".join(l for l in ORDRE_ETIQ if r[l])}" '
            f'data-st="{" ".join(str(st[k]) for k in ORDRE_ESTATS)}" data-m="{" ".join(e["mancances"])}" '
            f'data-p="{e["pais_codi"]}" data-f="{r["F"]}">'
            f'<td><a class="emp-nom" href="empreses/{e["isin"]}.html" title="{esc(e["nom_base"])}">{esc(e["nom"])}</a>'
            f'<span class="sub"><code>{e["isin"]}</code> · CEO {darrer["any"]}: {esc(ceo_darrer)}</span></td>'
            f'<td><span class="sr" role="img" aria-label="{esc(aria_serie(e))}">{"".join(cel)}</span></td>'
            f'<td>{minibarra_estat(st, n)}<span class="sub">{esc(st_curt)}</span></td>'
            f'<td class="num">{r["F"]}</td></tr>'
        )
    ll_etq = "".join(f'<span class="ll"><i class="sw e-{l}" aria-hidden="true">{l}</i>{esc(NOM_ETIQ_MIN[l])}</span>' for l in ORDRE_ETIQ)
    ll_st = "".join(f'<span class="ll"><i class="sw-ratlla s-{k}" aria-hidden="true"></i>'
                    f'<span aria-hidden="true">{ESTATS[k][0]}</span> {esc(ESTATS[k][1].lower())}</span>' for k in ORDRE_ESTATS)
    ll_st += '<span class="ll"><i class="sw-fora" aria-hidden="true"></i>casella buida: l\'empresa no era a l\'índex aquell any</span>'
    n_emp = len(emp)
    cos = f"""<section class="cap-pagina">
<h1>Empreses</h1>
<p class="entradeta">{fmt_int(n_emp)} empreses i {fmt_int(model["n_files"])} files. Cerca per nom, ISIN o CEO, o filtra per etiqueta i estat.</p>
</section>
{combobox("f-q", "", "Cerca per nom, ISIN o CEO", "Nom, ISIN o CEO…", local=True, cls="cb-llista-emp", etiqueta_visible=True)}
<form class="filtres" id="filtres" aria-label="Filtres" onsubmit="return false">
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
<th scope="col" aria-sort="ascending"><button type="button" data-ordre="n">Empresa<span class="ord" aria-hidden="true"></span></button></th>
<th scope="col" class="col-serie"><span class="vh">Sèrie 2016–2025</span><span class="serie-anys" aria-hidden="true">{"".join(f"<span>{str(a)[2:]}</span>" for a in ANYS_PANELL)}</span></th>
<th scope="col"><button type="button" data-ordre="pa">Estat<span class="ord" aria-hidden="true"></span></button></th>
<th scope="col" class="num"><button type="button" data-ordre="f">Anys F<span class="ord" aria-hidden="true"></span></button></th>
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


def franja_anys(e: dict, obert: int) -> str:
    """Franja de deu targetes 2016-2025 (any, etiqueta, icona d'estat i línia de
    color d'estat). Els anys fora de l'índex són targetes buides i no clicables.
    El JS hi afegeix el patró «roving tabindex» (fletxes ←/→)."""
    per_any = {f["any"]: f for f in e["files"]}
    items = []
    for a in ANYS_PANELL:
        f = per_any.get(a)
        if not f:
            items.append(f'<li><span class="rl rl-buit"><span class="rl-a">{a}</span>'
                         f'<span class="vh">: l\'empresa no era a l\'índex</span></span></li>')
            continue
        icona, nom_st = ESTATS[f["cat"]][0], ESTATS[f["cat"]][1]
        cur = ' aria-current="true"' if a == obert else ""
        items.append(
            f'<li><a class="rl b-{f["cat"]}" href="#any-{a}"{cur}><span class="rl-a">{a}</span>'
            f'<span class="rl-e e-{f["lletra"]}" aria-hidden="true">{f["lletra"]}</span>'
            f'<span class="rl-s" aria-hidden="true">{icona}</span>'
            f'<span class="vh">: {esc(NOM_ETIQ[f["lletra"]])}, {esc(nom_st.lower())}</span></a></li>')
    return f'<nav class="franja" aria-label="Anys de l\'empresa"><ol class="rail">{"".join(items)}</ol></nav>'


def trams_ceo(e: dict) -> str:
    """Qui era el CEO per períodes (trams d'anys consecutius amb el mateix `ceos`)."""
    trams: list[dict] = []
    for f in e["files"]:
        if trams and trams[-1]["clau"] == f["ceos_text"] and trams[-1]["fi"] == f["any"] - 1:
            trams[-1]["fi"] = f["any"]
        else:
            trams.append({"clau": f["ceos_text"], "ini": f["any"], "fi": f["any"], "ceos": f["ceos"]})
    items = []
    for t in trams:
        nom = " · ".join(t["ceos"]) if t["ceos"] else "Sense CEO"
        rang = str(t["ini"]) if t["ini"] == t["fi"] else f"{t['ini']}–{t['fi']}"
        items.append(f'<li><span class="tc-anys">{rang}</span> <b{"" if t["ceos"] else " class=buit"}>{esc(nom)}</b></li>')
    return f'<div class="trams-ceo"><h3 class="tc-cap">CEO a 31/10 per períodes</h3><ol>{"".join(items)}</ol></div>'


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
    notes_html = f'<div class="p-notes"><h3 class="pn-h">Notes</h3>{"".join(notes)}</div>' if notes else ""
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
    if tok == "cap":
        return f'<span class="regla regla-cap" title="cap: sense regla registrada">{esc(REGLES_TEXT[tok])}</span>'
    if tok in REGLES_TEXT:
        anc = REGLA_ANCORA.get(tok, tok)
        return f'<a class="regla" href="{prefix}metodologia.html#regla-{slug(anc)}">{esc(REGLES_TEXT[tok])}</a>'
    ref = ref_metodologia(tok)
    tit = f' title="Metodologia vigent, {esc(ref[1])}"' if ref else ""
    return f'<a class="regla" href="{prefix}metodologia.html#regla-{slug(tok)}"{tit}><code>{esc(tok)}</code></a>'


# Frase de cada codi de la columna `regles` (la del Mètode).
FRASE_REGLA = {"a": "a", "b": "b", "c_AAF64_reserva": "c", "d": "d", "e": "e", "D37": "D37", "cita_fundador": "D37",
               "R-SC": "R-SC", "R2b": "R2b", "R3": "R3"}


def regla_detall(tok: str) -> str:
    """La regla enllaçada i, al costat, la frase curta del Mètode o la
    referència a la secció de la metodologia (codis sense resum aprovat)."""
    if tok in FRASE_REGLA:
        extra = f'<span class="regla-frase">{esc(REGLES_FRASE[FRASE_REGLA[tok]])}</span>'
    elif ref_metodologia(tok):
        url, text = ref_metodologia(tok)
        extra = (f'<span class="regla-frase">Sense resum aprovat en aquest lloc: vegeu la metodologia, '
                 f'{enllac_ext(url, text)}.</span>')
    else:
        extra = ""
    return f'<span class="regla-item">{regla_html(tok)}{extra}</span>'


def regles_visibles(regles: list[str]) -> list[str]:
    """«cap» només es mostra si és l'únic codi (si no, es contradiu amb l'altre)."""
    toks = [t for t in regles if t != "cap"]
    return toks or ["cap"]


def primer_id(ids: str) -> list[str]:
    return [i for i in (ids or "").split(";") if i and not i.startswith("(+") and i != "(sense id)"]


TITOL_COMPROVADA = {
    "sí": "La cita s'ha verificat per script a la captura de Wayback.",
    "no": "S'ha intentat verificar la cita a la captura i no s'ha pogut comprovar.",
    "pendent": "Encara no s'ha intentat verificar la cita a la captura.",
}
RE_NIVELL = re.compile(r"\bNivell ([ABC])\b")


def nivell_font(p: dict) -> str:
    """Nivell A/B/C que declara la mateixa entrada (origen de la cita o nota pública)."""
    for o, ocult in p["origen_pub"]:
        m = None if ocult else re.fullmatch(r"Nivell ([ABC])", o)
        if m:
            return m.group(1)
    for n, motiu in p["notes_pub"]:
        m = None if motiu else RE_NIVELL.search(n)
        if m:
            return m.group(1)
    return ""


def descripcio_document(p: dict) -> str:
    """El document i la pàgina, segons la primera nota pública de l'entrada (sense
    inventar res: si la nota no diu «Document:», es mostra com a nota)."""
    for n, motiu in p["notes_pub"]:
        if motiu:
            continue
        t = norm_ws(n)
        t = re.sub(r"^(?:Nivell [ABC]\.\s*)?(?:Funció: \w+\.\s*)?", "", t)
        m = re.search(r"Document:\s*(.+?)(?:\.\s+Prova:|$)", t)
        doc = bool(m)
        if m:
            t = m.group(1)
        if not t:
            continue
        if len(t) > 230:
            t = t[:230].rsplit(" ", 1)[0].rstrip(",;:") + "…"
        return (esc(t) if doc else f'<span class="doc-et">Nota:</span> {esc(t)}')
    return ""


def comprovada_txt(p: dict) -> str:
    return "sí" if p["capt_si"] else ("no" if "no" in p["capt"] else "pendent")


def ev_prova(p: dict | None, ident: str) -> tuple[str, str]:
    """(insígnies, cos) d'una prova a la columna d'evidència: cita en serif, document,
    «Font original», «Còpia arxivada» i si la cita s'ha comprovat a la còpia."""
    if p is None:
        return "", (f'<p class="mini">Identificador <code>{esc(ident)}</code> '
                    "(no trobat entre les proves d'aquesta empresa).</p>")
    if p["ocult"]:
        return "", (f'<p class="sense-cita">Prova no mostrada (criteri de la part pública) · '
                    f'<code>{esc(p["id"])}</code></p>')
    ins = []
    if p["es_v"]:
        ins.append('<span class="b b-v" title="marca_veritat = [V]: document obert sencer i cita trobada">[V] cita trobada al document</span>')
    elif "[NV]" in p["veritat"]:
        ins.append('<span class="b b-nv" title="marca_veritat = [NV]">[NV] no comprovada al document</span>')
    if p["no_valida"]:
        ins.append('<span class="b b-mal" title="La nota de l\'entrada diu no_valida">Font no vàlida</span>')
    niv = nivell_font(p)
    allot = ", ".join(p["allotjament"])
    if niv or allot:
        ins.append(f'<span class="b b-gris" title="Nivell de la font i allotjament del document">'
                   f'{"Font " + niv if niv else "Font"}{" · " + esc(allot) if allot else ""}</span>')
    for m in p["marca_prova"]:
        if len(m) <= 14:
            ins.append(f'<span class="b b-marca" title="marca_prova">{esc(m)}</span>')
    url = url_segura(p["url"])
    if url:
        font = (f'<a class="boto" href="{esc(url)}" target="_blank" rel="noopener noreferrer">'
                f'<span class="bt"><span aria-hidden="true">↗</span> Font original</span> <small>{esc(domini(url))}</small></a>')
    elif p["url"]:
        font = f'<span class="domini">URL no vàlida: {esc(p["url"])}</span>'
    else:
        font = '<span class="boto boto-off">Sense URL de la font</span>'
    wu, d = wayback_prova(p)
    if wu:
        extra = " (fitxer extra)" if not p["wb_urls"] else ""
        copia = (f'<a class="boto boto-wb" href="{esc(wu)}" target="_blank" rel="noopener noreferrer">'
                 f'<span class="bt"><span aria-hidden="true">⟲</span> Còpia arxivada{extra}</span>{" <small>" + esc(d) + "</small>" if d else ""}</a>')
    else:
        copia = f'<span class="boto boto-off">Còpia arxivada: {"pendent" if p["wb_pendent"] else "encara no"}</span>'
    comp = comprovada_txt(p)
    doc = descripcio_document(p)
    cos = (f'<div class="ev-cita">{html_cita(p["cita"], p["id"], 420)}</div>'
           + (f'<p class="doc">{doc}</p>' if doc else "")
           + f'<div class="botons">{font}{copia}</div>'
           f'<p class="verif"><span title="{esc(TITOL_COMPROVADA[comp])}">Cita comprovada a la còpia: '
           f'<b class="vf vf-{"si" if comp == "sí" else comp}">{comp}</b></span>'
           f'<span>ID <code>{esc(p["id"])}</code></span>'
           f'<a href="#{p["ancora"]}">Veure la prova</a>'
           + ('<button type="button" class="copia" data-copia-cita>Copia la cita</button>' if p["cita"] else "")
           + '</p>')
    return "".join(ins), cos


def columna(titol: str, ins: str, cos: str, sub: str = "", cls: str = "") -> str:
    return (f'<div class="ev{(" " + cls) if cls else ""}"><div class="ev-cap"><h4 class="ev-t">{titol}</h4>{ins}</div>'
            f'{sub}{cos}</div>')


def prova_valida(p: dict) -> bool:
    """La definició de cita vàlida d'estat/estat_files.py, sobre la prova agrupada."""
    return (p["es_v"] and bool(p["cita"]) and p["url"].lower().startswith(("http://", "https://"))
            and not p["no_valida"])


def es_extrem(p: dict) -> bool:
    """Extrem d'interval: el mateix criteri que `c1_tipus` (marca_prova amb «interval»)."""
    return any("interval" in m for m in p["marca_prova"])


def tipus_extrem(p: dict) -> str:
    """«inici» o «final» si la nota ho diu al principi (format de la regla 28)."""
    for n in p["notes"]:
        t = n.strip().lower()
        if t.startswith("inici"):
            return "inici"
        if t.startswith("final"):
            return "final"
    return ""


def candidats(e: dict, ids_txt: str, a: int, funcions: set[str], noms: list[str], anomena) -> list[dict]:
    """Proves que sostenen la condició a l'any `a`, en l'ordre de `c1_ids`/`c2_ids`.
    Si la llista està truncada («(+n)»), s'hi afegeixen les proves de la fitxa que
    compleixen la mateixa regla que estat/estat_files.py."""
    ids = primer_id(ids_txt)
    out = []
    for i in ids:
        out.extend(p for p in e["proves"] if p["id"] == i and a in p["anys"] and prova_valida(p) and set(p["funcio"]) & funcions)
    if "(+" in (ids_txt or ""):
        for p in e["proves"]:
            if p["id"] in ids or a not in p["anys"] or not prova_valida(p) or not set(p["funcio"]) & funcions:
                continue
            if noms and not any(anomena(p["cita"], n) for n in noms):
                continue
            out.append(p)
    return out


def tria(cands: list[dict]) -> dict | None:
    """La primera prova amb la cita verificada a la còpia; si no n'hi ha, la primera."""
    return next((p for p in cands if p["capt_si"]), cands[0] if cands else None)


def tria_extrems(exts: list[dict]) -> list[tuple[str, dict]]:
    """Un extrem d'inici i un de final; si no es distingeixen, «extrem 1» i «extrem 2»."""
    inici = tria([p for p in exts if tipus_extrem(p) == "inici"])
    final = tria([p for p in exts if tipus_extrem(p) == "final"])
    if inici and final:
        return [("inici (nomenament)", inici), ("final", final)]
    ordenats = sorted(exts, key=lambda p: not p["capt_si"])[:2]
    return [(f"extrem {n}", p) for n, p in enumerate(ordenats, start=1)]


def linia_vertical(e: dict, index_proves: dict[str, dict], pend: dict, anomena, obert: int) -> str:
    """Un bloc per any: capçalera (CEO, etiqueta, prova, estat) i un plegable
    «Evidència de l'any» amb dues columnes: qui era el CEO i per què és (o no és)
    fundador. La prova que es mostra és la que fa complir la condició (la primera
    amb la cita comprovada a la còpia), amb la mateixa regla que estat_files.py."""
    blocs_any = []
    for f in e["files"]:
        a = f["any"]
        est = f["est"]
        l = f["lletra"]
        if f["ceos"]:
            ceo = " · ".join(esc(c) for c in f["ceos"])
        else:
            ceo = '<span class="buit">Sense CEO</span>'
        regles = regles_visibles(f["regles"])
        es_na, es_nd = l == "NA", l == "ND"
        sense_etiq = es_na or es_nd
        # Funcions i noms que fan servir les condicions C1 i C2 (estat/estat_files.py).
        if sense_etiq and not (es_nd and f["ceos"]):
            f1, noms1 = {"ceo", "fundador", "context"}, []
        else:
            f1, noms1 = {"ceo"}, f["ceos"]
        f2 = {"ceo", "fundador", "context"} if sense_etiq else {"fundador"}

        # --- Columna 1: qui era el CEO ---------------------------------------
        t1 = "Documentació de la fila sense CEO (R-SC)" if es_na else "Qui era el CEO"
        nom1 = "Sense CEO" if es_na else "CEO"
        mostrades1: list[dict] = []
        ids1 = primer_id(est["c1_ids"])
        estat1 = "falta"
        if est["c1_ceo"] in ("ok", "rsc_documentat") and ids1:
            cands = candidats(e, est["c1_ids"], a, f1, noms1, anomena)
            docs = [p for p in cands if not es_extrem(p)]
            exts = [p for p in cands if es_extrem(p)]
            doc = tria(docs)
            if doc and (doc["capt_si"] or not any(p["capt_si"] for p in exts)):
                mostrades1 = [doc]
                ins, cos = ev_prova(doc, doc["id"])
                col1 = columna(t1, ins, cos)
            elif exts:
                parts = []
                for nom_ext, p in tria_extrems(exts):
                    mostrades1.append(p)
                    ins, cos = ev_prova(p, p["id"])
                    parts.append(f'<div class="ev-ext"><div class="ev-cap"><span class="ev-ext-t">Extrem de l\'interval: {esc(nom_ext)}</span>{ins}</div>{cos}</div>')
                parts.append('<p class="mini ev-limit">Limitació declarada (regla 28): a les files amb '
                             '<abbr title="marca ceo_interval">CEO per interval</abbr> no s\'ha verificat '
                             "l'absència de canvis de CEO entre els dos extrems.</p>")
                col1 = columna(f"{t1} (per interval)", "", "".join(parts))
            else:
                ins, cos = ev_prova(index_proves.get(ids1[0]), ids1[0])
                col1 = columna(t1, ins, cos)
            estat1 = "v" if mostrades1 else "ok"
        else:
            col1 = columna(t1, "", f'<p class="falta-txt">Falta: {"documentació de la fila sense CEO" if es_na else "cita de CEO"}.</p>',
                           cls="ev-falta")

        # --- Columna 2: per què és (o no és) fundador -------------------------
        t2 = {"F": "Per què és fundador (F)", "P": "Per què no és fundador",
              "NA": "Per què no hi ha CEO", "ND": "Què falta"}[l]
        nom2 = {"F": "Fundador", "P": "Prova", "NA": "Cerca", "ND": "Cerca"}[l]
        sub = '<p class="ev-sub">' + "".join(regla_detall(t) for t in regles) + "</p>"
        if es_nd:
            sub += f'<p class="ev-sub-nd">{esc(DEF_ND)}</p>'
        if sense_etiq:
            sub += '<p class="ev-sub-t">Documentació de la cerca:</p>'
        mostrada2 = None
        ids2 = primer_id(est["c2_ids"])
        estat2 = "falta"
        if est["c2_fundador"] == "ok_columna_antiga":
            estat2 = "base"
            d = next((d for d in e["cites_base"] if d["tipus"] == "font_classificacio" and a in d["anys"]), None)
            if d and not d["ocult"]:
                url = url_segura(d["url"])
                font = (f'<a class="boto" href="{esc(url)}" target="_blank" rel="noopener noreferrer"><span class="bt"><span aria-hidden="true">↗</span> '
                        f'Font original</span> <small>{esc(domini(url))}</small></a>') if url else '<span class="boto boto-off">Sense URL de la font</span>'
                cos = (f'<div class="ev-cita">{html_cita(d["cita"], "font_classificacio_cita", 420)}</div>'
                       f'<div class="botons">{font}<span class="boto boto-off">Còpia arxivada: sense còpia arxivada</span></div>')
                col2 = columna(t2, '<span class="b b-gris">Cita de la base</span>', cos, sub)
            else:
                col2 = columna(t2, "", '<p class="sense-cita">Prova no mostrada (criteri de la part pública) · '
                               "<code>font_classificacio_cita</code></p>", sub)
        elif est["c2_fundador"] in ("ok_registre", "rsc_documentat", "cerca_documentada") and ids2:
            mostrada2 = tria(candidats(e, est["c2_ids"], a, f2, [], anomena))
            if mostrada2 is not None and any(mostrada2 is p for p in mostrades1):
                col2 = columna(t2, "", f'<p class="mini">La mateixa prova de la columna «{esc(t1)}».</p>', sub)
            elif mostrada2 is not None:
                ins, cos = ev_prova(mostrada2, mostrada2["id"])
                col2 = columna(t2, ins, cos, sub)
            else:
                ins, cos = ev_prova(index_proves.get(ids2[0]), ids2[0])
                col2 = columna(t2, ins, cos, sub)
            estat2 = "v" if mostrada2 is not None else "ok"
        else:
            col2 = columna(t2, "", f'<p class="falta-txt">Falta: {"documentació de la cerca" if sense_etiq else "prova de fundador"}.</p>',
                           sub, cls="ev-falta")
        # Una fila acabada ha de mostrar, a les dues cites, «comprovada a la còpia: sí».
        if f["cat"] == "acabada":
            if not any(p["capt_si"] for p in mostrades1) or mostrada2 is None or not mostrada2["capt_si"]:
                atura(f"{e['isin']} {a}: fila acabada sense cita comprovada a la còpia a l'evidència de l'any")

        # --- Avisos de la fila ------------------------------------------------
        avisos = []
        if est["c4_coherencia"] != "ok":
            probs = [PROBLEMES_C4.get(x, x) for x in est["c4_coherencia"].split(";") if x]
            avisos.append(f'<p class="falta-txt">No quadra amb la base: {esc(" ".join(probs))}</p>')
        for dub in f["dubtes"]:
            nom = ORIGENS_DUBTE.get(dub, (dub, ""))[0]
            url = url_pendents(pend, dub, f"l10-{e['isin'].lower()}-{a}" if dub == "lot10" else None)
            avisos.append(f'<p class="falta-txt">Dubte obert ({esc(nom)}): {enllac_ext(url, "veure al fitxer de dubtes")}</p>')
        if "carrec_no_detectat_a_la_cita" in est["avisos"]:
            avisos.append('<p class="mini">Avís (no bloqueja): el càrrec no es detecta automàticament a la cita de CEO.</p>')
        n_proves = sum(a in p["anys"] for p in e["proves"]) + sum(a in d["anys"] for d in e["cites_base"])

        # --- Resum del plegable: insígnies, data de la còpia i inici de la cita
        def ins_resum(nom: str, estat: str) -> str:
            if estat == "v":
                return f'<span class="b b-v">{esc(nom)} [V]</span>'
            if estat == "ok":
                return f'<span class="b b-gris">{esc(nom)}</span>'
            if estat == "base":
                return f'<span class="b b-gris">{esc(nom)}: cita de la base</span>'
            return f'<span class="b b-mal">{esc(nom)}: falta</span>'
        visibles = [p for p in [*mostrades1, mostrada2] if p is not None and not p["ocult"]]
        data_copia = next((wayback_prova(p)[1] for p in visibles if wayback_prova(p)[0]), "")
        copia_txt = f'<span class="b b-gris">còpia {esc(data_copia)}</span>' if data_copia else '<span class="b b-gris">sense còpia arxivada</span>'
        previ = ""
        p_previ = next((p for p in mostrades1 if not p["ocult"] and p["cita"]), None)
        if p_previ:
            t = p_previ["cita"]
            t = t if len(t) <= 90 else t[:90].rsplit(" ", 1)[0] + "…"
            previ = f'<span class="previ" aria-hidden="true">«{esc(t)}»</span>'
        resum = (f'<summary><span class="fletxa" aria-hidden="true"></span><span class="ev-titol">Evidència de {a}</span>'
                 f'{ins_resum(nom1, estat1)}{ins_resum(nom2, estat2)}{copia_txt}{previ}</summary>')
        prova_curta = " · ".join(regla_html(t) for t in regles)
        defecte = ' open data-defecte' if a == obert else ""
        blocs_any.append(
            f'<li class="tl-any l-{l}" id="any-{a}">'
            f'<div class="tl-marca"><h3 class="tl-a">{a}</h3><span class="tl-punt s-{f["cat"]}" aria-hidden="true">{ESTATS[f["cat"]][0]}</span></div>'
            f'<div class="tl-cos">'
            f'<div class="tl-fila"><p class="tl-ceo"><small>CEO a 31/10/{a}</small><b>{ceo}</b></p>'
            f'<span class="tl-etq"><span class="vh">Etiqueta: </span>{badge_etiq(l)}</span>'
            f'<span class="tl-prova">Prova: {prova_curta}</span>'
            f'<span class="tl-st"><span class="vh">Estat: </span>{insignia_estat(f["cat"])}</span></div>'
            f'<details class="tl-evid"{defecte}>{resum}'
            f'<div class="evid">{col1}{col2}</div>'
            + (f'<div class="ev-avisos">{"".join(avisos)}</div>' if avisos else "")
            + f'<div class="tl-peu"><a href="#proves" data-filtre-any="{a}">Totes les proves d\'aquest any ({n_proves}) <span aria-hidden="true">→</span></a>'
            f'<span class="tl-peu-st">Estat: {esc(ESTATS[f["cat"]][3])}</span></div>'
            "</details></div></li>")
    return f'<ol class="tl">{"".join(blocs_any)}</ol>'


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
            items.append(f"<li>Dubte obert ({esc(nom)}) per als anys {enll}. {enllac_ext(url_pendents(pend, k), 'Secció al fitxer de dubtes')}</li>")
        else:
            items.append(f"<li>Dubte obert ({esc(nom)}) per als anys {esc(comprimeix_anys(anys))}. "
                         f"{enllac_ext(url_pendents(pend, k), 'Secció al fitxer de dubtes')}</li>")
    return f'<aside class="caixa-dubte" role="note"><span class="cd-icona" aria-hidden="true">?</span><ul>{"".join(items)}</ul></aside>'


def historial_ia(e: dict) -> str:
    files = "".join(
        f'<tr><th scope="row">{f["any"]}</th><td>{esc(CERTIFICACIO.get(f["cert"], f["cert"]))}</td><td>{esc(f["nivell"]) or "—"}</td></tr>'
        for f in e["files"]
    )
    return ('<details class="historial"><summary>Historial de l\'auditoria IA <span class="mini">(històric: no és l\'estat de la fila)</span></summary>'
            '<p class="nota">Valors de l\'<span title="sim_estat_certificacio">estat de certificació</span> i del <span title="sim_nivell">nivell</span> de la base. És l\'estat de l\'auditoria anterior; '
            'l\'estat actual de cada fila és el de la columna «Estat». <a href="../metodologia.html#historic">Què volen dir</a>.</p>'
            '<div class="taula-wrap"><table class="taula-simple"><caption class="vh">Historial de l\'auditoria IA per any</caption>'
            '<thead><tr><th scope="col">Any</th><th scope="col">Certificació</th><th scope="col">Nivell</th></tr></thead>'
            f"<tbody>{files}</tbody></table></div></details>")


def pagina_fitxa(ctx: Context, e: dict, anterior: dict | None, seguent: dict | None) -> str:
    n = len(e["files"])
    anys_txt = comprimeix_anys(e["anys"])
    nom_base = (f'<p class="altres-noms">Nom del valor a la base: {esc(e["nom_base"])}</p>'
                if e["nom_base"] != e["nom"] else "")
    altres = ""
    if e["altres_visibles"]:
        altres = f'<p class="altres-noms">Altres noms al panell: {"; ".join(esc(x) for x in e["altres_visibles"])}</p>'
    index_proves: dict[str, dict] = {}
    for p in e["proves"]:
        index_proves.setdefault(p["id"], p)

    grups = {"ceo": [], "fundador": [], "altres": []}
    for p in e["proves"]:
        grups[p["grup"]].append(html_prova(p))
    for i, d in enumerate(e["cites_base"], start=1):
        grups["fundador"].append(html_cita_base(d, i))
    titols = {
        "ceo": ("CEO", "Qui era el CEO a 31/10: nomenaments, informes anuals i intervals de CEO."),
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
        intro = (f'<p class="nota">{fmt_int(len(e["proves"]))} entrades del <span title="docs/REGISTRE_CANVIS.csv">registre de canvis</span>'
                 f'{" i " + fmt_int(len(e["cites_base"])) + " cites dels camps de la base" if e["cites_base"] else ""}. '
                 "Cada prova es mostra una vegada, amb els anys que cobreix.</p>")
        proves_html = intro + filtre + "".join(seccions)
    else:
        proves_html = ('<div class="sense-proves"><p><strong>No hi ha cap cita estructurada</strong> ni al '
                       '<span title="docs/REGISTRE_CANVIS.csv">registre de canvis</span> ni als '
                       '<span title="font_classificacio_* i d37_*">camps de cita de la base</span>.</p></div>')
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

    # Etiqueta dominant: la més freqüent (en empat, l'ordre F, P, ND, NA) i el CEO d'aquells anys.
    dom = max(ORDRE_ETIQ, key=lambda x: (e["recompte"][x], -ORDRE_ETIQ.index(x)))
    ceos_dom = {f["ceos_text"] for f in e["files"] if f["lletra"] == dom}
    noms_dom = sorted({c for f in e["files"] if f["lletra"] == dom for c in f["ceos"]}, key=clau_ordre)
    if dom == "NA" or not noms_dom:
        qui = ""
    elif len(ceos_dom) == 1:
        qui = " · " + esc(" · ".join(next(f["ceos"] for f in e["files"] if f["lletra"] == dom)))
    else:
        qui = f" · {len(noms_dom)} CEO diferents"
    obert = e["files"][-1]["any"]  # per defecte, l'últim any amb dades
    llegenda = ("".join(f'<span class="ll"><span class="sw e-{l}" aria-hidden="true">{l}</span>{esc(NOM_ETIQ_MIN[l])}</span>' for l in ORDRE_ETIQ)
                + '<span class="ll-sep" aria-hidden="true"></span>'
                + "".join(f'<span class="ll"><span class="sw s-{k}" aria-hidden="true">{ESTATS[k][0]}</span>{esc(ESTATS[k][1].lower())}</span>' for k in ORDRE_ESTATS)
                + '<span class="ll-sep" aria-hidden="true"></span>'
                + '<span class="ll"><span class="b b-v">[V]</span>cita trobada al document</span>'
                + '<span class="ll"><span class="sw sw-buida" aria-hidden="true"></span>targeta buida: l\'empresa no era a l\'índex</span>'
                + '<a class="ll-mes" href="../metodologia.html#llegenda">Llegenda completa</a>')

    cos = f"""<p class="molla"><a href="../empreses.html">← Empreses</a></p>
<section class="fitxa-cap">
<div class="fc-nom">
<h1>{esc(e["nom"])}</h1>
<p class="fitxa-linia"><span class="isin"><code>{esc(e["isin"])}</code><button type="button" class="copia copia-isin" data-copia="{esc(e["isin"])}">Copia l'ISIN</button></span> <span>{esc(e["pais"])} <span class="mini">(prefix ISIN)</span></span> <span>{esc(anys_txt)} ({n} {"any" if n == 1 else "anys"})</span></p>
{nom_base}{altres}
</div>
<div class="fc-resum">
<p class="fc-etq">{badge_etiq(dom)} <span>{e["recompte"][dom]} de {n} {"any" if n == 1 else "anys"}{qui}</span></p>
<p class="fitxa-estat">{minibarra_estat(e["st"], n, "mb mb-gran")}<span>{esc(text_estat_empresa(e))}</span></p>
</div>
</section>
{caixa_dubte(e, ctx.pend)}
<section class="seccio seccio-anys" id="anys" aria-labelledby="h-anys">
<h2 id="h-anys">Any per any</h2>
<p class="nota">Tria un any per veure qui era el CEO el 31 d'octubre i per què és (o no és) fundador, amb la cita, la font original i la còpia arxivada.</p>
<div class="com-llegir"><span class="cl-cap">Com es llegeix:</span>{llegenda}</div>
<div class="rail-envol">{franja_anys(e, obert)}</div>
{trams_ceo(e)}
{linia_vertical(e, index_proves, ctx.pend, ctx.anomena, obert)}
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


def pagina_metodologia(ctx: Context, model: dict, E: dict, stats: Counter) -> str:
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
        ("ND", "Valor <code>no_determinat</code>. " + esc(DEF_ND)),
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
        targeta("no-valida", '<span class="b b-mal">Font no vàlida</span>', "La nota de l'entrada la marca com a <span title=\"no_valida\">no vàlida</span>: la cita no és al document, és d'un altre any o la font és C."),
        targeta("pendent-arxiu", '<span class="b b-nv">Pendent d\'arxiu</span>', "La nota diu <code>pendent_arxiu</code>, abans <code>pendent_DF</code>: el document no s'ha pogut obrir sencer i espera el flux d'arxiu."),
        targeta("comprovada", '<span class="b b-v">Cita comprovada a la còpia</span>', "<span title=\"cita_verificada_a_captura = si\">La cita s'ha verificat per script a la captura de Wayback</span>."),
        targeta("cita-base", '<span class="b b-gris">Cita de la base</span>', "Cita que només consta als <span title=\"font_classificacio_* o d37_*\">camps de cita</span> del CSV de la base, sense còpia arxivada."),
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
    def sense(codi: str) -> str:
        url, text = ref_metodologia(codi)
        return f"Codi de la base sense resum aprovat en aquest lloc. Vegeu la metodologia vigent, {enllac_ext(url, text)}."
    F = REGLES_FRASE
    regles = [
        ("R1", "Per al CEO", esc(F["R1"])),
        ("R2", "Per al CEO", esc(F["R2"])),
        ("R2b", "Per al CEO", esc(F["R2b"])),
        ("R3", "Per al CEO", esc(F["R3"])),
        ("R-SC", "Per al CEO", esc(F["R-SC"])),
        ("ceo_interval", "Per al CEO", esc(F["ceo_interval"])),
        ("D37", "Porta a F", esc(F["D37"]) + " A la columna <code>regles</code> també surt com a <code>cita_fundador</code>."),
        ("FT", "Porta a F", sense("FT")),
        ("D10", "Porta a F", sense("D10")),
        ("D10b_prelacio", "Porta a F", sense("D10b_prelacio")),
        ("a", "Porta a P", esc(F["a"])),
        ("b", "Porta a P", esc(F["b"])),
        ("c", "Porta a P", esc(F["c"]) + " A la columna <code>regles</code>: <code>c_AAF64_reserva</code>."),
        ("d", "Porta a P", esc(F["d"])),
        ("e", "Porta a P", esc(F["e"])),
        ("d_per_part", "Porta a P", sense("d_per_part")),
        ("b_per_part", "Porta a P", sense("b_per_part")),
        ("holding_interposada", "Altres", sense("holding_interposada")),
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


CODI_ETIQ = {"F": "F", "P": "P", "ND": "D", "NA": "N"}


def index_cerca(model: dict) -> str:
    """Índex compacte del cercador amb suggeriments, compartit per totes les pàgines
    (un fitxer JS, perquè funcioni també amb file://). Per empresa: ISIN, nom
    visible, altres noms de la base (normalitzats), CEO de la base, CEO de
    l'últim any i la sèrie de 10 anys (etiqueta F/P/D/N i estat a/r/d/f; «--» = fora
    de l'índex). Només dades que ja són a empreses.html."""
    files = []
    for e in sorted(model["empreses"].values(), key=lambda e: (clau_ordre(e["nom"]), e["isin"])):
        per_any = {f["any"]: f for f in e["files"]}
        serie = "".join(CODI_ETIQ[per_any[a]["lletra"]] + LLETRA_ESTAT[per_any[a]["cat"]] if a in per_any else "--"
                        for a in ANYS_PANELL)
        noms = norm_cerca(" ".join([e["nom_base"], *e["altres_noms"]]))
        files.append([e["isin"], e["nom"], noms, "|".join(e["ceos_noms"]), e["files"][-1]["ceos_text"], serie])
    dades = json.dumps(files, ensure_ascii=False, separators=(",", ":"))
    for camp in dades.split('","'):
        if te_restringit(camp):
            atura("l'índex de cerca conté un terme de la llista restringida")
    return ("/* Índex del cercador. Generat per dashboard/genera_dashboard.py; no l'editis a mà. */\n"
            f"window.CERCA_IDX={dades};\n")


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
    escriu(SORTIDA / "assets" / "comu.js", JS_COMU)
    escriu(SORTIDA / "assets" / "index_cerca.js", index_cerca(model))
    for isin in ISIN_EXEMPLES:
        if isin not in model["empreses"]:
            atura(f"l'exemple del cercador {isin} no és a la base")
    escriu(SORTIDA / "index.html", pagina_estat(ctx, E))
    # L'apòstrof no cal escapar-lo (els atributs van entre cometes dobles): la pàgina pesa menys.
    escriu(SORTIDA / "empreses.html", pagina_empreses(ctx, model, E).replace("&#x27;", "'"))
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
    if E["urls_cua_fitxer"] is not None and E["urls_cua_fitxer"] != E["urls_cua"]:
        print(f"AVÍS: estat/urls_per_arxivar.csv té {E['urls_cua_fitxer']} URL, però el registre actual en dona "
              f"{E['urls_cua']} (es mostra aquesta). Cal regenerar-lo amb python3 estat/llista_urls_arxiu.py en un PR de dades.")
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

CSS = r"""/* Fundadors-CEO. Generat per dashboard/genera_dashboard.py; no l'editis a mà.
   Estil editorial (paper càlid, tinta, xifres i cites en serif), fitxa amb franja
   d'anys i línia del temps, cercador amb suggeriments i mode clar/fosc. */
:root {
  color-scheme: light;
  --fons: #f7f4ec;
  --sup: #fffdf8;
  --sup-2: #f1ede2;
  --sup-3: #e7e1d3;
  --tinta: #1d1b16;
  --tinta-2: #4a463d;
  --tinta-3: #635e52;
  --linia: #e2dccd;
  --linia-forta: #c4bba7;
  --vora-camp: #8a826f;
  --enllac: #1f4f8f;
  --enllac-hover: #123766;
  --focus: #2456a6;
  /* Etiquetes FounderCEO (text blanc >= 4,5:1) */
  --e-F: #c2521f;
  --e-P: #1f66c1;
  --e-ND: #9b2f8f;
  --e-NA: #6e6d68;
  --e-txt: #ffffff;
  --e-F-suau: #f8e4d9;
  --e-P-suau: #e2eaf5;
  --e-ND-suau: #f3e2ef;
  --e-NA-suau: #ebe8e1;
  /* Insígnies d'estat amb text (to suau) */
  --st-acabada: #1f7a3d;
  --st-acabada-txt: #ffffff;
  --st-arxiu: #cfe8d6;
  --st-arxiu-txt: #1d1b16;
  --st-dubte: #e9a93a;
  --st-dubte-txt: #1d1b16;
  --st-falta: #e7e1d3;
  --st-falta-ratlla: #c9c0ac;
  --st-falta-txt: #1d1b16;
  /* Marques d'estat (barres, franges, minibarres, punts). Validades amb
     validate_palette.js --pairs all sobre #fffdf8 i #f7f4ec. */
  --mk-acabada: #1f7a3d;
  --mk-acabada-txt: #ffffff;
  --mk-arxiu: #86c9a0;
  --mk-arxiu-txt: #1d1b16;
  --mk-dubte: #e9a93a;
  --mk-dubte-txt: #1d1b16;
  --mk-falta: #8a8882;
  --mk-falta-ratlla: #a9a7a0;
  --mk-falta-txt: #1d1b16;
  --barra: #4a463d;
  /* Proves */
  --v: #12692c;
  --v-fons: #e3f1e5;
  --nv: #8a5300;
  --nv-fons: #fbefd5;
  --mal: #b42318;
  --mal-fons: #fbe6e2;
  --cita-fons: #faf7f0;
  --ombra: 0 12px 32px rgba(29, 27, 22, .14);
  --radi: 6px;
  --radi-petit: 4px;
  --serif: "Iowan Old Style", "Palatino Linotype", Palatino, "Book Antiqua", Charter, "Bitstream Charter", Cambria, Georgia, serif;
  --font: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  --font-cita: var(--serif);
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, "DejaVu Sans Mono", "Liberation Mono", monospace;
}
/* Mode fosc: el del sistema (si no s'ha triat res) o el triat amb el botó. Només a la pantalla. */
@media screen and (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    color-scheme: dark;
    --fons: #151411; --sup: #1c1a17; --sup-2: #25231f; --sup-3: #2f2c27;
    --tinta: #efebe1; --tinta-2: #cbc5b8; --tinta-3: #a7a194;
    --linia: #34312b; --linia-forta: #4d4940; --vora-camp: #8a8476;
    --enllac: #93b8ec; --enllac-hover: #bfd5f5; --focus: #7aa7ec;
    --e-ND: #a8399c;
    --e-F-suau: #3b2419; --e-P-suau: #1b2a3e; --e-ND-suau: #35192f; --e-NA-suau: #2a2824;
    --st-acabada: #5fcf8a; --st-acabada-txt: #121211;
    --st-arxiu: #2e6b47; --st-arxiu-txt: #f0efec;
    --st-dubte: #d9a93a; --st-dubte-txt: #121211;
    --st-falta: #3a3730; --st-falta-ratlla: #57524a; --st-falta-txt: #efebe1;
    --mk-acabada: #9be3b5; --mk-acabada-txt: #121211;
    --mk-arxiu: #3b9a6b; --mk-arxiu-txt: #121211;
    --mk-dubte: #d9a93a; --mk-dubte-txt: #121211;
    --mk-falta: #5a5954; --mk-falta-ratlla: #6e6d67; --mk-falta-txt: #efebe1;
    --barra: #b9b2a3;
    --v: #7fd99a; --v-fons: #143220; --nv: #f2c14e; --nv-fons: #382a0c; --mal: #ff9a8f; --mal-fons: #3f1814;
    --cita-fons: #211f1b; --ombra: 0 12px 32px rgba(0, 0, 0, .5);
  }
}
@media screen {
  :root[data-theme="dark"] {
    color-scheme: dark;
    --fons: #151411; --sup: #1c1a17; --sup-2: #25231f; --sup-3: #2f2c27;
    --tinta: #efebe1; --tinta-2: #cbc5b8; --tinta-3: #a7a194;
    --linia: #34312b; --linia-forta: #4d4940; --vora-camp: #8a8476;
    --enllac: #93b8ec; --enllac-hover: #bfd5f5; --focus: #7aa7ec;
    --e-ND: #a8399c;
    --e-F-suau: #3b2419; --e-P-suau: #1b2a3e; --e-ND-suau: #35192f; --e-NA-suau: #2a2824;
    --st-acabada: #5fcf8a; --st-acabada-txt: #121211;
    --st-arxiu: #2e6b47; --st-arxiu-txt: #f0efec;
    --st-dubte: #d9a93a; --st-dubte-txt: #121211;
    --st-falta: #3a3730; --st-falta-ratlla: #57524a; --st-falta-txt: #efebe1;
    --mk-acabada: #9be3b5; --mk-acabada-txt: #121211;
    --mk-arxiu: #3b9a6b; --mk-arxiu-txt: #121211;
    --mk-dubte: #d9a93a; --mk-dubte-txt: #121211;
    --mk-falta: #5a5954; --mk-falta-ratlla: #6e6d67; --mk-falta-txt: #efebe1;
    --barra: #b9b2a3;
    --v: #7fd99a; --v-fons: #143220; --nv: #f2c14e; --nv-fons: #382a0c; --mal: #ff9a8f; --mal-fons: #3f1814;
    --cita-fons: #211f1b; --ombra: 0 12px 32px rgba(0, 0, 0, .5);
  }
}

*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: 16px; }
body { margin: 0; background: var(--fons); color: var(--tinta); font: 400 16px/1.55 var(--font); font-variant-numeric: tabular-nums; }
a { color: var(--enllac); text-decoration-thickness: 1px; text-underline-offset: 3px; }
a:hover { color: var(--enllac-hover); }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; border-radius: 3px; }
code { font-family: var(--font-mono); font-size: .86em; background: var(--sup-2); padding: .08em .35em; border-radius: 3px; overflow-wrap: anywhere; }
h1, h2, h3, h4 { line-height: 1.2; margin: 0 0 .5em; font-weight: 600; }
h1 { font: 600 clamp(32px, 4.4vw, 48px)/1.06 var(--serif); letter-spacing: -.015em; }
h2 { font: 600 26px/1.15 var(--serif); letter-spacing: -.01em; }
h3, .h3 { font-size: 17px; font-weight: 600; }
p { margin: 0 0 .8em; }
small { font-size: 13px; }
abbr[title] { text-decoration: none; }
.vh { position: absolute !important; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
.salta { position: absolute; left: 16px; top: -80px; background: var(--tinta); color: var(--fons); padding: 8px 12px; z-index: 60; border-radius: 3px; }
.salta:focus { top: 8px; color: var(--fons); }
.nota { color: var(--tinta-3); font-size: 13px; max-width: 72ch; }
.mini { color: var(--tinta-3); font-size: 13px; font-weight: 400; }
.nota-clara { color: var(--tinta-2); font-size: 15px; max-width: 72ch; }
.buit { color: var(--tinta-3); }
.ok { color: var(--v); font-weight: 600; }
.num { text-align: right; }

/* ---------- Capçalera ---------- */
.barra { background: var(--sup); border-bottom: 1px solid var(--linia); position: relative; z-index: 25; }
.barra-in { max-width: 1240px; margin: 0 auto; padding: 14px 24px 0; display: grid; grid-template-columns: auto minmax(0, 1fr) auto auto; grid-template-areas: "marca cerca pindola tema" "nav nav nav nav"; gap: 8px 20px; align-items: center; }
.marca { grid-area: marca; display: flex; flex-direction: column; text-decoration: none; color: var(--tinta); padding-bottom: 4px; }
.marca:hover { color: var(--tinta); }
.marca b { font: 600 22px/1.15 var(--serif); letter-spacing: -.01em; }
.marca small { font-size: 13px; color: var(--tinta-3); margin-top: 2px; }
.cb-cap { grid-area: cerca; justify-self: end; width: min(100%, 400px); }
.pindola { grid-area: pindola; display: inline-flex; align-items: center; gap: 7px; font-size: 13px; padding: 4px 11px; border: 1px solid var(--linia-forta); border-radius: 999px; color: var(--tinta-2); text-decoration: none; white-space: nowrap; min-height: 32px; }
.pindola::before { content: ""; width: 7px; height: 7px; border-radius: 50%; background: var(--mk-dubte); flex: none; }
.pindola:hover { color: var(--tinta); border-color: var(--tinta-3); }
.tema { grid-area: tema; display: none; place-items: center; width: 40px; height: 40px; border-radius: 50%; border: 1px solid var(--linia-forta); background: var(--sup); color: var(--tinta-2); cursor: pointer; padding: 0; }
.js .tema { display: inline-grid; }
.tema:hover { color: var(--tinta); border-color: var(--tinta-3); }
.tema svg { width: 19px; height: 19px; display: block; }
.nav { grid-area: nav; display: flex; gap: 28px; border-top: 1px solid var(--linia); margin-top: 6px; }
.nav a { display: inline-flex; align-items: center; gap: 8px; padding: 11px 0 9px; min-height: 44px; font-size: 15px; font-weight: 600; text-decoration: none; color: var(--tinta-3); border-bottom: 3px solid transparent; }
.nav a:hover { color: var(--tinta); }
.nav a[aria-current="page"] { color: var(--tinta); border-bottom-color: var(--tinta); }
.nav svg { display: none; width: 20px; height: 20px; }

/* ---------- Cercador amb suggeriments ---------- */
.cb { position: relative; }
.cb-camp { position: relative; display: flex; align-items: center; gap: 8px; }
.cb-lupa { position: absolute; left: 12px; top: 50%; width: 18px; height: 18px; margin-top: -9px; color: var(--tinta-3); pointer-events: none; }
.cb input { flex: 1; min-width: 0; width: 100%; height: 42px; padding: 0 40px 0 38px; font: 400 16px var(--font); color: var(--tinta); background: var(--fons); border: 1px solid var(--vora-camp); border-radius: 999px; }
.cb input::placeholder { color: var(--tinta-3); opacity: 1; }
.cb input::-webkit-search-cancel-button { cursor: pointer; }
.cb-kbd { position: absolute; right: 12px; top: 50%; transform: translateY(-50%); font: 12px var(--font-mono); border: 1px solid var(--linia-forta); border-radius: 4px; padding: 1px 6px; color: var(--tinta-3); background: var(--sup); pointer-events: none; }
.cb input:focus ~ .cb-kbd, .cb input:not(:placeholder-shown) ~ .cb-kbd { display: none; }
.cb-et { display: block; font: 600 17px/1.3 var(--serif); margin-bottom: 8px; }
.cb-pop { position: absolute; left: 0; right: 0; top: calc(100% + 6px); z-index: 40; background: var(--sup); border: 1px solid var(--linia-forta); border-radius: var(--radi); box-shadow: var(--ombra); padding: 6px; min-width: min(560px, calc(100vw - 32px)); }
.cb-cap .cb-pop { left: auto; right: 0; }
.cb-pop[hidden] { display: none; }
.cb-llista { list-style: none; margin: 0; padding: 0; max-height: min(430px, 60vh); overflow: auto; }
.cb-llista[hidden] { display: none; }
.sug { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 2px 16px; align-items: center; padding: 9px 10px; border-radius: var(--radi-petit); cursor: pointer; }
.sug[aria-selected="true"], .sug:hover { background: var(--sup-2); box-shadow: inset 3px 0 0 var(--tinta); }
.sug-nom { font: 600 17px/1.3 var(--serif); overflow-wrap: anywhere; }
.sug-sub { grid-column: 1; font-size: 13px; color: var(--tinta-3); overflow-wrap: anywhere; }
.sug-sub code { background: transparent; padding: 0; color: var(--tinta-2); }
.sug .sr { grid-row: 1 / span 2; grid-column: 2; }
.sug mark, .cb mark { background: color-mix(in srgb, var(--mk-dubte) 45%, transparent); color: inherit; border-radius: 2px; padding: 0 1px; }
.cb-peu { margin: 4px 0 0; padding: 8px 10px 4px; border-top: 1px solid var(--linia); font-size: 14px; display: flex; flex-direction: column; gap: 6px; }
.cb-peu[hidden] { display: none; }
.cb-peu a { font-weight: 600; display: inline-flex; align-items: center; gap: .3em; min-height: 32px; }
.cb-buit { color: var(--tinta-2); }

/* ---------- Estructura ---------- */
.pagina { max-width: 1120px; margin: 0 auto; padding: 0 24px 64px; }
.pagina.ample { max-width: 1240px; }
.molla { padding-top: 24px; margin: 0; font-size: 14px; }
.molla a { font-weight: 600; text-decoration: none; display: inline-flex; min-height: 40px; align-items: center; }
.entradeta { font: 400 19px/1.5 var(--serif); color: var(--tinta-2); max-width: 36em; }
.cap-pagina { padding: 40px 0 20px; }
.resposta { font: 400 20px/1.45 var(--serif); margin: 0 0 20px; max-width: 36em; }
.resposta b { font-weight: 600; }

/* Línia de versió */
.versio-linia { display: flex; gap: 10px; align-items: flex-start; font-size: 13px; color: var(--tinta-3); margin: 16px 0 0; max-width: 64em; }
.pv-icona { flex: none; width: 18px; height: 18px; border-radius: 50%; border: 1px solid var(--mk-dubte); color: var(--tinta-2); display: grid; place-items: center; font-weight: 700; font-size: 11px; margin-top: 1px; }
.versio-linia code { background: transparent; padding: 0; }

/* ---------- Estat: obertura ---------- */
.obertura { padding: 52px 0 40px; display: grid; grid-template-columns: minmax(0, 1fr) 380px; gap: 48px; align-items: end; border-bottom: 1px solid var(--linia-forta); }
.obertura h1 { margin-bottom: 16px; }
.obertura .entradeta { margin: 0; }
.cerca-rapida { background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 20px; }
.cb-gran input { border-radius: 3px; height: 46px; padding-right: 12px; }
.cb-boto { min-height: 46px; }
.cr-ajuda { margin: 10px 0 0; font-size: 13px; color: var(--tinta-3); }
.exemples { margin: 8px 0 0; font-size: 13px; color: var(--tinta-3); display: flex; flex-wrap: wrap; gap: 0 12px; align-items: center; }
.exemples a { color: var(--tinta-2); display: inline-flex; align-items: center; min-height: 32px; }

/* ---------- Estat: seccions (pregunta a l'esquerra) ---------- */
.bloc { display: grid; grid-template-columns: 200px minmax(0, 1fr); gap: 32px; padding: 48px 0; border-bottom: 1px solid var(--linia); }
.bloc:last-child { border-bottom: 0; }
.bloc-cap h2 { margin: 0; }
.bloc-n { display: block; font: italic 400 15px/1 var(--serif); color: var(--tinta-3); margin-bottom: 10px; }
.bloc-cos { min-width: 0; }
.heroi-xifra { display: flex; align-items: baseline; flex-wrap: wrap; gap: 4px 16px; margin: 0 0 24px; }
.heroi-xifra b { font: 500 112px/.9 var(--serif); letter-spacing: -.03em; }
.heroi-xifra span { font: 400 22px/1.3 var(--serif); color: var(--tinta-2); }

/* Dreceres amb recompte */
.dreceres { list-style: none; margin: 0 0 8px; padding: 0; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 10px; }
.drec { display: flex; flex-direction: column; gap: 6px; height: 100%; padding: 14px 14px 12px; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); text-decoration: none; color: var(--tinta); }
.drec:hover { border-color: var(--tinta-3); color: var(--tinta); }
.drec:hover .drec-emp { text-decoration: underline; }
.drec-cap { display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 600; line-height: 1.25; }
.drec-n { font-size: 14px; color: var(--tinta-2); }
.drec-n b { font: 500 30px/1 var(--serif); color: var(--tinta); letter-spacing: -.01em; margin-right: 2px; }
.drec-emp { margin-top: auto; font-size: 13px; color: var(--enllac); line-height: 1.35; }
.drec-emp b { font-weight: 700; }
.dreceres + .nota { margin: 0 0 24px; }

/* Barra apilada al 100 % */
.sb { display: flex; gap: 2px; height: 24px; padding: 2px; background: var(--sup); border: 1px solid var(--linia-forta); border-radius: 3px; margin: 0 0 4px; }
.sb-s { min-width: 3px; flex-basis: 0; border-radius: 1px; }
.s-acabada { background: var(--mk-acabada); color: var(--mk-acabada-txt); }
.s-arxiu { background: var(--mk-arxiu); color: var(--mk-arxiu-txt); }
.s-dubte { background: var(--mk-dubte); color: var(--mk-dubte-txt); }
.s-falta { background: repeating-linear-gradient(135deg, var(--mk-falta) 0 5px, var(--mk-falta-ratlla) 5px 7px); color: var(--mk-falta-txt); }
.e-F { background: var(--e-F); color: var(--e-txt); }
.e-P { background: var(--e-P); color: var(--e-txt); }
.e-ND { background: var(--e-ND); color: var(--e-txt); }
.e-NA { background: var(--e-NA); color: var(--e-txt); }
.sw { display: inline-grid; place-items: center; flex: none; width: 22px; height: 22px; border-radius: 3px; font: 700 12px/1 var(--font); font-style: normal; }
.sw.s-falta, .st-falta { border: 1px solid var(--linia-forta); }
.sw.s-falta { background: repeating-linear-gradient(135deg, var(--st-falta) 0 5px, var(--st-falta-ratlla) 5px 7px); color: var(--st-falta-txt); }
.sw-buida { background: transparent; border: 1px dashed var(--linia-forta); }
.ll-estats { list-style: none; margin: 20px 0 0; padding: 0; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); border-top: 1px solid var(--linia); }
.ll-estats li { display: flex; flex-direction: column; padding: 16px 20px 0 0; min-width: 0; }
.ll-estats li + li { padding-left: 20px; border-left: 1px solid var(--linia); }
.ll-cap { display: flex; align-items: flex-start; gap: 8px; font-size: 14px; line-height: 1.3; }
.ll-xifra { font: 500 40px/1.1 var(--serif); letter-spacing: -.01em; }
.ll-n { margin: 8px 0 2px; }
.ll-pc { font-size: 14px; color: var(--tinta-2); }
.ll-def { font-size: 13px; color: var(--tinta-3); margin-top: 6px; line-height: 1.45; }
.ll-etiq { list-style: none; margin: 12px 0; padding: 0; display: flex; flex-wrap: wrap; gap: 8px 24px; }
.ll-etiq li { display: inline-flex; align-items: center; gap: 8px; }
.ll-etiq .ll-n { margin: 0; color: var(--tinta-2); }

/* Embut */
.embut { list-style: none; margin: 8px 0; padding: 0; max-width: 860px; }
.eb-pas { margin: 0; }
.eb-nom { display: block; font-size: 14px; color: var(--tinta-2); margin-bottom: 4px; }
.eb-fila { display: flex; align-items: center; gap: 14px; }
.eb-barra { display: block; height: 26px; min-width: 3px; background: var(--barra); border-radius: 2px; }
.eb-final .eb-barra { background: var(--mk-acabada); }
.eb-val { white-space: nowrap; font: 500 21px/1 var(--serif); }
.eb-salt { display: flex; align-items: center; gap: 8px; margin: 6px 0 10px 8px; padding: 6px 0 6px 16px; border-left: 1px dashed var(--linia-forta); color: var(--tinta-3); font-size: 13px; }
.eb-salt .sw { width: 18px; height: 18px; font-size: 11px; }

/* Taules */
.taula-wrap { overflow-x: auto; -webkit-overflow-scrolling: touch; }
table { border-collapse: collapse; width: 100%; font-size: 15px; }
th, td { text-align: left; vertical-align: top; padding: 10px 12px; border-bottom: 1px solid var(--linia); }
th:first-child, td:first-child { padding-left: 0; }
thead th { font-size: 12px; color: var(--tinta-3); font-weight: 600; white-space: nowrap; border-bottom: 1px solid var(--tinta); vertical-align: bottom; }
tbody tr:last-child > * { border-bottom: 0; }
.taula-etiq td, .taula-etiq th { vertical-align: middle; }
.taula-etiq td { min-width: 92px; }
.tc-v { display: block; font: 500 18px/1.2 var(--serif); }
.tc-n { display: block; font-size: 13px; color: var(--tinta-3); }
.tc-files { display: none; }
.mm { display: block; height: 4px; background: var(--sup-3); margin-top: 6px; overflow: hidden; }
.mm i { display: block; height: 100%; background: var(--barra); }
.etq { display: inline-flex; align-items: center; gap: 6px; white-space: nowrap; font-size: 13px; font-weight: 600; padding: 3px 11px 3px 3px; border-radius: 999px; background: var(--e-P-suau); color: var(--tinta); }
.etq b { display: inline-grid; place-items: center; min-width: 22px; height: 22px; padding: 0 4px; border-radius: 999px; font-size: 11px; background: var(--e-P); color: var(--e-txt); }
.etq.e-F { background: var(--e-F-suau); color: var(--tinta); } .etq.e-F b { background: var(--e-F); }
.etq.e-P { color: var(--tinta); }
.etq.e-ND { background: var(--e-ND-suau); color: var(--tinta); } .etq.e-ND b { background: var(--e-ND); }
.etq.e-NA { background: var(--e-NA-suau); color: var(--tinta); } .etq.e-NA b { background: var(--e-NA); }
.taula-anys { table-layout: fixed; }
.taula-anys th:first-child { width: 64px; }
.taula-anys th:last-child { width: 72px; }
.taula-anys tbody th { font: 600 16px var(--serif); }
.taula-anys td.ta { text-align: right; }
.taula-anys td.ta b { font-weight: 600; }
.taula-anys td.ta small { color: var(--tinta-2); }
.mm.mk-acabada i { background: var(--mk-acabada); }
.mm.mk-arxiu i { background: var(--mk-arxiu); }
.mm.mk-dubte i { background: var(--mk-dubte); }
.mm.mk-falta i { background: var(--mk-falta); }
.curt { display: none; }

/* Barres d'una sola sèrie (mancances, dubtes) */
.bs { list-style: none; margin: 8px 0; padding: 0; max-width: 860px; }
.bs li { margin: 0; padding: 16px 0; border-top: 1px solid var(--linia); }
.bs li:first-child { border-top: 0; padding-top: 4px; }
.bs-nom { display: block; font-weight: 600; }
.bs-fila { display: flex; align-items: center; gap: 12px; margin: 6px 0; }
.bs-barra { display: block; height: 10px; min-width: 3px; background: var(--barra); border-radius: 1px; }
.bs-val { font: 500 22px/1 var(--serif); white-space: nowrap; }
.bs-det, .bs-que { display: block; font-size: 13px; color: var(--tinta-2); }
.bs-link { display: inline-flex; align-items: center; min-height: 32px; font-size: 14px; font-weight: 600; }
/* Dubtes: una línia per origen (nom, barra i enllaç). */
#dubtes .bs li { display: grid; grid-template-columns: 190px minmax(0, 1fr) auto; gap: 0 16px; align-items: center; padding: 6px 0; }
#dubtes .bs li:first-child { padding-top: 0; }
#dubtes .bs-fila { margin: 0; }

/* Passos de qualitat */
.passos { list-style: none; margin: 8px 0; padding: 0; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); border-top: 1px solid var(--tinta); }
.passos li { display: flex; flex-direction: column; gap: 8px; padding: 16px 16px 0 0; min-width: 0; }
.passos li + li { padding-left: 16px; border-left: 1px solid var(--linia); }
.pq-n { font: italic 400 30px/1 var(--serif); color: var(--tinta-3); }
.pq-t { display: flex; flex-direction: column; gap: 6px; overflow-wrap: anywhere; }
.pq-nom { font-size: 15px; }
.pq-t > span { font-size: 13px; color: var(--tinta-2); }
.pq-t > span b { font: 500 20px/1.2 var(--serif); color: var(--tinta); }

/* Gràfic de files F per any */
.grafic { margin: 28px 0 0; }
.grafic figcaption { margin-bottom: 12px; font-family: var(--serif); }
.barres { position: relative; height: 200px; margin: 8px 0 4px 30px; }
.eix { position: absolute; inset: 0 0 40px 0; pointer-events: none; }
.tick { position: absolute; left: 0; right: 0; border-top: 1px solid var(--linia); }
.tick span { position: absolute; left: -30px; top: -.6em; width: 24px; text-align: right; font-size: 12px; color: var(--tinta-3); }
.bcols { position: absolute; inset: 0; display: flex; gap: 6px; }
.bcol { position: relative; flex: 1; min-width: 0; display: flex; flex-direction: column; }
.barea { flex: 1; display: flex; align-items: flex-end; justify-content: center; }
.bar { position: relative; display: block; width: min(32px, 70%); background: var(--e-F); border-radius: 2px 2px 0 0; min-height: 2px; }
.bval { position: absolute; bottom: 100%; left: 50%; transform: translateX(-50%); font: 500 13px var(--serif); color: var(--tinta-2); padding-bottom: 2px; }
.bany { height: 40px; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 12px; color: var(--tinta-2); line-height: 1.2; border-top: 1px solid var(--tinta); }
.bany small { font-size: 11px; color: var(--tinta-3); }
.tip { position: absolute; bottom: calc(100% - 30px); left: 50%; transform: translateX(-50%); background: var(--tinta); color: var(--fons); font-size: 13px; padding: 6px 9px; border-radius: 4px; white-space: nowrap; pointer-events: none; display: none; z-index: 5; }
.bcol:hover .tip, .bcol:focus .tip { display: block; }
.bcol:first-child .tip { left: 0; transform: none; }
.bcol:last-child .tip { left: auto; right: 0; transform: none; }
details.dades { margin-top: 12px; font-size: 14px; }
details.dades summary { cursor: pointer; color: var(--tinta-2); font-weight: 600; min-height: 32px; display: flex; align-items: center; }
.taula-simple th, .taula-simple td { padding: 6px 12px; font-size: 13px; }
.etiqueta-prov { display: inline-block; font: 600 13px var(--font); border: 1px solid var(--mk-dubte); padding: 2px 10px; border-radius: 2px; }

/* Sobre aquestes dades */
.versio .versio-linia { margin: 0 0 16px; }
.versio-dl { display: grid; gap: 8px; margin: 0 0 12px; font-size: 14px; }
.versio-dl div { display: grid; grid-template-columns: minmax(180px, 280px) 1fr; gap: 4px 16px; }
.versio-dl dt { color: var(--tinta-3); }
.versio-dl dd { margin: 0; min-width: 0; }
.sha { font-size: 12px; }
.docs { padding-left: 20px; }
.docs li { margin-bottom: 4px; }
.docs a, .text-llarg a, .versio-linia, .entradeta { overflow-wrap: anywhere; }

/* ---------- Botons ---------- */
.boto { display: inline-flex; flex-wrap: wrap; align-items: center; gap: 2px 8px; min-height: 40px; max-width: 100%; white-space: normal; overflow-wrap: anywhere; font: 600 14px/1.25 var(--font); padding: 6px 14px; border: 1px solid var(--tinta); border-radius: 3px; background: var(--tinta); color: var(--fons); text-decoration: none; cursor: pointer; }
.boto:hover { color: var(--fons); background: var(--tinta-2); border-color: var(--tinta-2); }
.boto small { font-weight: 400; font-size: 12px; opacity: .8; overflow-wrap: anywhere; }
.bt { white-space: nowrap; }
.boto-wb { background: transparent; color: var(--tinta); border-color: var(--tinta); }
.boto-wb:hover { background: var(--sup-2); color: var(--tinta); border-color: var(--tinta); }
.boto-off { background: transparent; color: var(--tinta-3); border: 1px dashed var(--linia-forta); font-weight: 500; cursor: default; }
.boto-off:hover { background: transparent; color: var(--tinta-3); border-color: var(--linia-forta); }
.boto-mostra { min-height: 0; padding: 3px 10px; font-size: 13px; }
.boto-sec { font: 600 14px var(--font); min-height: 40px; border: 1px solid var(--vora-camp); background: transparent; color: var(--tinta); border-radius: 3px; padding: 6px 14px; cursor: pointer; }
.boto-sec:hover { background: var(--sup-2); }
.ext { font-size: .85em; margin-left: 2px; }
.copia { display: none; align-items: center; gap: 6px; min-height: 32px; padding: 0 10px; font: 500 13px var(--font); color: var(--tinta-2); background: transparent; border: 1px solid var(--linia-forta); border-radius: 3px; cursor: pointer; }
.js .copia { display: inline-flex; }
.copia:hover { color: var(--tinta); border-color: var(--tinta-3); }

/* ---------- Empreses ---------- */
.p-empreses .cap-pagina { padding-bottom: 8px; }
.cb-llista-emp { margin: 8px 0 20px; }
.cb-llista-emp .cb-et { font: 600 12px var(--font); color: var(--tinta-3); margin-bottom: 8px; }
.cb-llista-emp .cb-lupa { left: 4px; width: 22px; height: 22px; margin-top: -11px; color: var(--tinta-2); }
.cb-llista-emp input { height: 60px; padding: 0 4px 0 38px; font: 400 26px var(--serif); background: transparent; border: 0; border-bottom: 2px solid var(--tinta); border-radius: 0; }
.cb-llista-emp input:focus-visible { outline-offset: 2px; }
.filtres { display: flex; flex-wrap: wrap; gap: 14px 24px; align-items: flex-end; padding-bottom: 8px; margin: 0 0 4px; }
.filtres select { max-width: 320px; }
.camp { display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; color: var(--tinta-3); min-width: 0; max-width: 100%; }
.camp small { font-weight: 400; }
.camp[hidden] { display: none; }
select { font: 400 14px var(--font); color: var(--tinta); background: var(--sup); border: 1px solid var(--vora-camp); border-radius: 3px; padding: 0 10px; min-height: 40px; max-width: 100%; }
.filtres .boto-sec { border: 0; text-decoration: underline; text-underline-offset: 3px; padding: 0 4px; color: var(--tinta-2); }
.recompte { padding: 18px 0 6px; margin: 12px 0 0; border-top: 1px solid var(--tinta); font: 400 18px var(--serif); color: var(--tinta-2); }
.recompte b { color: var(--tinta); font-weight: 600; }
.llegenda { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 16px; font-size: 12px; color: var(--tinta-3); margin: 6px 0 12px; }
.ll { display: inline-flex; align-items: center; gap: 6px; }
.llegenda .ll-cap { font-weight: 600; color: var(--tinta-2); }
.llegenda .sw { width: 16px; height: 16px; font-size: 9px; }
.ll-ajuda { display: inline-grid; place-items: center; width: 28px; height: 28px; border-radius: 50%; border: 1px solid var(--linia-forta); text-decoration: none; font-weight: 700; }
.taula-emp { border-top: 0; }
.taula-emp td { vertical-align: middle; padding-top: 16px; padding-bottom: 16px; }
.taula-emp thead th { border-bottom: 1px solid var(--linia-forta); }
.taula-emp thead button { font: inherit; color: inherit; background: none; border: 0; padding: 0; cursor: pointer; display: inline-flex; align-items: center; gap: 4px; min-height: 32px; }
.taula-emp thead .ord::after { content: "↕"; opacity: .45; }
.taula-emp thead th[aria-sort="ascending"] .ord::after { content: "↑"; opacity: 1; }
.taula-emp thead th[aria-sort="descending"] .ord::after { content: "↓"; opacity: 1; }
.taula-emp tbody tr:hover { background: color-mix(in srgb, var(--sup-2) 70%, transparent); }
.taula-emp td:first-child a { font: 600 19px/1.25 var(--serif); text-decoration: none; color: var(--tinta); }
.taula-emp td:first-child a:hover { text-decoration: underline; }
.col-serie { width: 360px; }
.serie-anys { display: grid; grid-template-columns: repeat(10, 30px); gap: 4px; text-align: center; }
.sub { display: block; font-size: 13px; color: var(--tinta-3); margin-top: 3px; }
.sub code { background: transparent; padding: 0; font-size: 12px; }
.sr { display: inline-grid; grid-template-columns: repeat(10, 30px); gap: 4px; padding-bottom: 7px; }
.sr i { position: relative; display: grid; place-items: center; height: 34px; border-radius: 3px; font: 700 12px/1 var(--font); font-style: normal; color: var(--e-txt); background: transparent; border: 1px dashed var(--linia-forta); }
.sr i.F { background: var(--e-F); border: 0; } .sr i.P { background: var(--e-P); border: 0; }
.sr i.ND { background: var(--e-ND); border: 0; font-size: 10px; } .sr i.NA { background: var(--e-NA); border: 0; font-size: 10px; }
/* Línia d'estat de 4 px sota la casella, separada per 3 px. */
.sr i::after { content: ""; position: absolute; left: 0; right: 0; bottom: -7px; height: 4px; border-radius: 1px; }
.sr i.a::after { background: var(--mk-acabada); }
.sr i.r::after { background: var(--mk-arxiu); }
.sr i.d::after { background: var(--mk-dubte); }
.sr i.f::after { background: repeating-linear-gradient(135deg, var(--mk-falta) 0 3px, var(--mk-falta-ratlla) 3px 5px); }
.sug .sr { grid-template-columns: repeat(10, 22px); gap: 3px; }
.sug .sr i { height: 24px; font-size: 10px; }
.sug .sr i.ND, .sug .sr i.NA { font-size: 8px; }
.sw-ratlla { display: inline-block; width: 18px; height: 4px; border-radius: 1px; }
.sw-ratlla.s-falta { background: var(--mk-falta); border: 0; }
.sw-fora { display: inline-block; width: 14px; height: 18px; border-radius: 3px; border: 1px dashed var(--linia-forta); }
.mb { display: flex; gap: 1px; width: 140px; height: 8px; border-radius: 1px; overflow: hidden; background: var(--sup-3); }
.mb i { flex-basis: 0; min-width: 2px; }
.mb .s-falta { background: var(--mk-falta); border: 0; }
.mb-gran { width: 240px; height: 10px; }
.sense-resultat { text-align: center; padding: 40px 16px; font: 400 20px var(--serif); color: var(--tinta-2); }
.sense-resultat p { margin-bottom: 12px; }

/* ---------- Insígnies ---------- */
.st { display: inline-flex; align-items: center; gap: 6px; white-space: nowrap; font-size: 13px; font-weight: 600; padding: 3px 11px; border-radius: 999px; }
.st-acabada { background: var(--st-acabada); color: var(--st-acabada-txt); }
.st-arxiu { background: var(--st-arxiu); color: var(--st-arxiu-txt); }
.st-dubte { background: var(--st-dubte); color: var(--st-dubte-txt); }
.st-falta { background: repeating-linear-gradient(135deg, var(--st-falta) 0 5px, var(--st-falta-ratlla) 5px 7px); color: var(--st-falta-txt); }
.b { display: inline-flex; align-items: center; font: 700 12px/1.4 var(--font); padding: 2px 9px; border-radius: 3px; white-space: nowrap; }
.b-v { background: var(--v-fons); color: var(--v); }
.b-nv { background: var(--nv-fons); color: var(--nv); }
.b-mal { background: var(--mal-fons); color: var(--mal); }
.b-gris { background: var(--sup-3); color: var(--tinta-2); }
.b-marca { background: transparent; border: 1px solid var(--linia-forta); color: var(--tinta-2); font-family: var(--font-mono); font-weight: 400; }
.b-nivell { background: var(--e-P-suau); color: var(--tinta); }

/* ---------- Fitxa ---------- */
.fitxa-cap { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 16px 40px; align-items: end; padding: 16px 0 28px; border-bottom: 1px solid var(--linia-forta); }
.fitxa-cap h1 { font-size: clamp(30px, 4vw, 44px); margin-bottom: 10px; overflow-wrap: anywhere; }
.fitxa-linia { display: flex; flex-wrap: wrap; gap: 6px 18px; align-items: center; color: var(--tinta-2); font-size: 14px; margin-bottom: 6px; }
.isin { display: inline-flex; align-items: center; gap: 8px; }
.isin code { font-size: 14px; font-weight: 600; color: var(--tinta); background: var(--sup); border: 1px solid var(--linia); padding: 3px 8px; }
.altres-noms { font-size: 13px; color: var(--tinta-3); margin: 0 0 4px; }
.fc-resum { display: flex; flex-direction: column; align-items: flex-end; gap: 10px; text-align: right; }
.fc-etq { display: flex; flex-wrap: wrap; align-items: center; justify-content: flex-end; gap: 6px 10px; margin: 0; font-size: 14px; color: var(--tinta-2); }
.fitxa-estat { display: flex; flex-direction: column; align-items: flex-end; gap: 6px; margin: 0; font-size: 14px; color: var(--tinta-2); }
.caixa-dubte { display: flex; gap: 12px; align-items: flex-start; background: var(--nv-fons); color: var(--tinta); border: 1px solid var(--mk-dubte); border-radius: var(--radi); padding: 12px 16px; margin: 24px 0 0; }
.caixa-dubte ul { margin: 0; padding: 0; list-style: none; }
.cd-icona { flex: none; width: 24px; height: 24px; border-radius: 50%; background: var(--st-dubte); color: var(--st-dubte-txt); display: grid; place-items: center; font-weight: 700; }
.seccio { padding: 36px 0 0; }
.seccio > h2 { margin-bottom: 6px; }
.seccio > .nota { margin-bottom: 14px; }
.com-llegir { display: flex; flex-wrap: wrap; gap: 8px 16px; align-items: center; font-size: 13px; color: var(--tinta-2); padding: 10px 14px; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); }
.cl-cap { font-weight: 700; color: var(--tinta); }
.com-llegir .sw { width: 20px; height: 20px; font-size: 10px; }
.ll-sep { width: 1px; height: 18px; background: var(--linia-forta); }
.ll-mes { font-weight: 600; display: inline-flex; align-items: center; min-height: 32px; }

/* Franja d'anys */
.rail-envol { position: sticky; top: 0; z-index: 15; background: var(--fons); padding: 12px 0; margin-top: 8px; }
.rail { display: grid; grid-template-columns: repeat(10, minmax(0, 1fr)); gap: 6px; list-style: none; margin: 0; padding: 0; }
.rl { position: relative; display: flex; flex-direction: column; align-items: center; gap: 5px; height: 100%; padding: 9px 4px 11px; border-radius: var(--radi); background: var(--sup); border: 1px solid var(--linia); text-decoration: none; color: var(--tinta); overflow: hidden; }
a.rl:hover { border-color: var(--tinta-3); color: var(--tinta); }
.rl::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 4px; }
.rl.b-acabada::after { background: var(--mk-acabada); }
.rl.b-arxiu::after { background: var(--mk-arxiu); }
.rl.b-dubte::after { background: var(--mk-dubte); }
.rl.b-falta::after { background: repeating-linear-gradient(135deg, var(--mk-falta) 0 3px, var(--mk-falta-ratlla) 3px 5px); }
.rl-a { font: 600 16px/1 var(--serif); }
.rl-e { display: inline-grid; place-items: center; min-width: 24px; height: 24px; padding: 0 3px; border-radius: 3px; font: 700 12px/1 var(--font); }
.rl-s { font-size: 12px; font-weight: 700; color: var(--tinta-3); line-height: 1; }
.rl[aria-current="true"] { border: 2px solid var(--tinta); padding: 8px 3px 10px; }
.rl-buit { background: transparent; border-style: dashed; border-color: var(--linia-forta); color: var(--tinta-3); justify-content: flex-start; }
.trams-ceo { display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 14px; font-size: 14px; color: var(--tinta-2); margin: 2px 0 8px; }
.tc-cap { font: 600 13px var(--font); color: var(--tinta-3); margin: 0; }
.trams-ceo ol { display: flex; flex-wrap: wrap; gap: 4px 18px; list-style: none; margin: 0; padding: 0; }
.tc-anys { color: var(--tinta-3); }
.trams-ceo b { color: var(--tinta); }

/* Línia del temps vertical */
.tl { list-style: none; margin: 20px 0 0; padding: 0; position: relative; }
.tl::before { content: ""; position: absolute; left: 47px; top: 10px; bottom: 10px; width: 2px; background: var(--linia-forta); }
.tl-any { display: grid; grid-template-columns: 96px minmax(0, 1fr); gap: 0 20px; margin-bottom: 18px; scroll-margin-top: 112px; }
.tl-marca { display: flex; flex-direction: column; align-items: center; gap: 8px; padding-top: 14px; position: relative; z-index: 1; }
.tl-a { font: 600 24px/1 var(--serif); margin: 0; background: var(--fons); padding: 2px 4px; }
.tl-punt { display: grid; place-items: center; width: 30px; height: 30px; border-radius: 50%; font-size: 13px; font-weight: 700; box-shadow: 0 0 0 3px var(--fons); }
.tl-cos { background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); min-width: 0; }
.tl-any:target .tl-cos { border-color: var(--tinta); box-shadow: 0 0 0 1px var(--tinta); }
.tl-fila { display: flex; flex-wrap: wrap; align-items: center; gap: 10px 16px; padding: 14px 20px; }
.tl-ceo { flex: 1 1 240px; min-width: 0; margin: 0; }
.tl-ceo small { display: block; font-size: 12px; color: var(--tinta-3); }
.tl-ceo b { font: 600 22px/1.2 var(--serif); overflow-wrap: anywhere; }
.tl-prova { font-size: 13px; color: var(--tinta-2); }
.tl-prova a { font-weight: 600; }
.tl-evid > summary { list-style: none; display: flex; align-items: center; flex-wrap: wrap; gap: 8px 10px; padding: 10px 20px; min-height: 48px; border-top: 1px solid var(--linia); background: var(--sup-2); cursor: pointer; font-size: 14px; }
.tl-evid > summary::-webkit-details-marker { display: none; }
.tl-evid > summary:hover .ev-titol { text-decoration: underline; }
.fletxa { width: 0; height: 0; border-style: solid; border-width: 5px 0 5px 8px; border-color: transparent transparent transparent var(--enllac); transition: transform .15s; }
.tl-evid[open] > summary .fletxa { transform: rotate(90deg); }
.ev-titol { font-weight: 700; color: var(--enllac); margin-right: 4px; }
.previ { margin-left: auto; font: italic 400 14px var(--serif); color: var(--tinta-3); max-width: 46ch; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.evid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); border-top: 1px solid var(--linia); }
.ev { padding: 20px 22px; min-width: 0; }
.ev + .ev { border-left: 1px solid var(--linia); }
.ev-cap { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 8px; margin-bottom: 10px; }
.ev-t { font: 700 14px/1.3 var(--font); margin: 0 6px 0 0; color: var(--tinta); }
.ev-sub { font-size: 13px; color: var(--tinta-2); margin: -2px 0 12px; }
.ev-sub-nd { font-size: 13px; color: var(--tinta-2); margin: 0 0 10px; }
.ev-sub-t { font-size: 13px; font-weight: 600; color: var(--tinta-2); margin: 0 0 8px; }
.regla-item { display: block; }
.regla-item + .regla-item { margin-top: 4px; }
.regla { font-weight: 600; margin-right: 6px; }
.regla-frase { display: block; font-size: 13px; color: var(--tinta-2); max-width: 68ch; }
.ev-cita .cita { margin: 0; padding: 14px 18px 14px 34px; background: var(--cita-fons); border: 0; border-left: 3px solid var(--tinta); border-radius: 0 var(--radi-petit) var(--radi-petit) 0; }
.ev + .ev .cita { border-left-color: var(--tinta-3); }
.l-F .ev + .ev .cita { border-left-color: var(--e-F); }
.l-P .ev + .ev .cita { border-left-color: var(--e-P); }
.ev-cita .cita::before { left: 10px; top: 8px; }
.ev-cita .cita p { font-size: 19px; line-height: 1.5; }
.doc { font-size: 13px; color: var(--tinta-2); margin: 12px 0 0; line-height: 1.5; overflow-wrap: anywhere; }
.doc-et { font-weight: 600; }
.botons { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }
.verif { display: flex; flex-wrap: wrap; gap: 4px 14px; align-items: center; margin: 12px 0 0; font-size: 13px; color: var(--tinta-2); }
.verif code { font-size: 11px; color: var(--tinta-3); background: transparent; padding: 0; }
.verif a { display: inline-flex; align-items: center; min-height: 32px; }
.vf { display: inline-block; padding: 0 8px; border-radius: 3px; font-weight: 700; }
.vf-si { background: var(--v-fons); color: var(--v); }
.vf-no { background: var(--sup-3); color: var(--tinta-2); }
.vf-pendent { background: var(--nv-fons); color: var(--nv); }
.ev-ext + .ev-ext { margin-top: 18px; padding-top: 16px; border-top: 1px dashed var(--linia-forta); }
.ev-ext-t { font-size: 13px; font-weight: 600; color: var(--tinta-2); margin-right: 4px; }
.ev-limit { margin: 14px 0 0; }
.ev-falta { background: color-mix(in srgb, var(--mal-fons) 45%, transparent); }
.ev-avisos { padding: 12px 22px; border-top: 1px solid var(--linia); display: grid; gap: 6px; }
.ev-avisos p { margin: 0; }
.falta-txt { margin: 0; font-weight: 600; color: var(--mal); }
.tl-peu { display: flex; flex-wrap: wrap; gap: 8px 20px; justify-content: space-between; align-items: center; padding: 12px 22px; border-top: 1px solid var(--linia); font-size: 14px; }
.tl-peu a { font-weight: 600; display: inline-flex; align-items: center; gap: .3em; min-height: 32px; }
.tl-peu-st { color: var(--tinta-3); font-size: 13px; max-width: 70ch; }

/* Cites i proves */
.cita { margin: 0 0 12px; padding: 12px 16px 12px 40px; background: var(--cita-fons); border-radius: var(--radi-petit); position: relative; border: 1px solid var(--linia); }
.cita::before { content: "“"; position: absolute; left: 12px; top: 4px; font-family: var(--serif); font-size: 2.2rem; line-height: 1; color: var(--tinta-3); }
.cita p { margin: 0; font-family: var(--serif); font-size: 17px; line-height: 1.5; overflow-wrap: anywhere; max-width: 70ch; }
.sense-cita { font-style: italic; color: var(--tinta-3); background: var(--sup-2); border-radius: var(--radi-petit); padding: 8px 12px; }
.filtre-anys { display: none; flex-wrap: wrap; gap: 6px; margin: 10px 0 6px; }
.js .filtre-anys { display: flex; }
.xip { display: inline-flex; align-items: center; font: 500 13px var(--font); min-height: 36px; border: 1px solid var(--linia-forta); background: var(--sup); color: var(--tinta); border-radius: 999px; padding: 0 12px; cursor: pointer; }
.xip:hover { border-color: var(--tinta-3); }
.xip[aria-pressed="true"] { background: var(--tinta); color: var(--fons); border-color: var(--tinta); }
.recompte-proves { font-size: 13px; color: var(--tinta-3); min-height: 1.3em; }
.grup-proves { border-top: 1px solid var(--linia); margin: 0; }
.grup-proves:last-of-type { border-bottom: 1px solid var(--linia); }
.grup-proves > summary { cursor: pointer; min-height: 52px; display: flex; align-items: center; gap: 8px; font: 600 19px var(--serif); }
.grup-proves > summary .n { font: 600 12px var(--font); background: var(--sup-3); color: var(--tinta-2); padding: 2px 9px; border-radius: 999px; }
.grup-proves[open] { padding-bottom: 12px; }
.prova { background: var(--sup); border: 1px solid var(--linia); border-left: 3px solid var(--v); border-radius: var(--radi); padding: 16px 18px; margin: 12px 0; scroll-margin-top: 16px; }
.prova-nv { border-left-color: var(--nv); }
.prova-mal { border-left-color: var(--mal); }
.prova-base { border-left-color: var(--linia-forta); }
.prova-oculta { border-left-color: var(--tinta-3); background: var(--sup-2); padding: 10px 14px; }
.prova-oculta p { margin: 0; color: var(--tinta-3); font-size: 13px; }
.prova:target { outline: 3px solid var(--focus); outline-offset: 2px; }
.p-cap { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin-bottom: 10px; }
.p-anys { margin-left: auto; font-size: 13px; font-weight: 700; color: var(--tinta-2); background: var(--sup-2); padding: 2px 10px; border-radius: 999px; }
.p-fonts { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-bottom: 8px; }
.domini { font-size: 13px; color: var(--tinta-2); overflow-wrap: anywhere; }
details.tecnic > summary { cursor: pointer; font-size: 13px; color: var(--enllac); min-height: 32px; display: flex; align-items: center; }
.p-meta { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 8px 16px; margin: 8px 0 0; padding: 12px 0 0; border-top: 1px solid var(--linia); }
.p-meta div { min-width: 0; }
.p-meta dt { font-size: 12px; color: var(--tinta-3); font-weight: 600; }
.p-meta dd { margin: 2px 0 0; font-size: 13px; overflow-wrap: anywhere; }
.llista-codi { margin: 4px 0 0; padding-left: 18px; }
.p-notes { margin-top: 12px; padding-top: 8px; border-top: 1px solid var(--linia); }
.p-notes .pn-h { font-size: 12px; font-weight: 700; color: var(--tinta-3); margin-bottom: 4px; }
.p-notes p { font-size: 13px; color: var(--tinta-2); margin-bottom: .5em; overflow-wrap: anywhere; }
.nota-oculta { font-style: italic; color: var(--tinta-3) !important; }
.sense-proves { background: var(--sup); border: 1px dashed var(--linia-forta); border-radius: var(--radi); padding: 16px; }
.sense-proves p { margin: 0; }
.rastre { margin-top: 12px; background: var(--sup); border: 1px solid var(--linia); border-radius: var(--radi); padding: 12px 16px; }
.rastre summary { cursor: pointer; font-weight: 600; }
.llista-urls { padding-left: 18px; font-size: 13px; }
.url-llarga { overflow-wrap: anywhere; }
.historial { border-top: 1px solid var(--linia); margin: 32px 0 0; font-size: 14px; }
.historial > summary { cursor: pointer; min-height: 52px; display: flex; align-items: center; flex-wrap: wrap; gap: 6px; font-weight: 600; color: var(--tinta-2); }
.historial[open] { padding-bottom: 16px; }
.nav-fitxes { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 24px; padding-top: 24px; border-top: 1px solid var(--linia); }
.nav-fitxes a { display: flex; flex-direction: column; gap: 2px; padding: 12px 16px; text-decoration: none; font: 600 17px var(--serif); color: var(--tinta); min-width: 0; overflow-wrap: anywhere; border: 1px solid var(--linia); border-radius: var(--radi); background: var(--sup); }
.nav-fitxes a small { font: 400 13px var(--font); color: var(--tinta-3); }
.nav-fitxes a:hover { border-color: var(--tinta-3); }
.nav-fitxes .seg { text-align: right; }

/* ---------- Mètode ---------- */
.text-llarg { max-width: 860px; }
.text-llarg p, .text-llarg li { max-width: 70ch; }
.text-llarg .seccio { padding: 32px 0; border-top: 1px solid var(--linia); }
.text-llarg h3 { margin-top: 24px; font: 600 19px var(--serif); }
.def { display: grid; grid-template-columns: minmax(170px, max-content) 1fr; gap: 6px 16px; align-items: start; padding: 12px 0; border-bottom: 1px solid var(--linia); }
.def p { margin: 0; }
.def-cap { display: flex; flex-direction: column; align-items: flex-start; gap: 4px; }
.def:target { background: var(--nv-fons); }
.prec, .condicions { padding-left: 20px; }

/* Peu */
.peu { border-top: 1px solid var(--linia); }
.peu-in { max-width: 1240px; margin: 0 auto; padding: 20px 24px 40px; font-size: 13px; color: var(--tinta-3); overflow-wrap: anywhere; }
.peu-in code { background: transparent; padding: 0; }

/* ---------- Responsiu ---------- */
@media (max-width: 1100px) {
  .dreceres { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}
@media (max-width: 1000px) {
  .obertura { grid-template-columns: minmax(0, 1fr); gap: 24px; }
  .bloc { grid-template-columns: minmax(0, 1fr); gap: 12px; }
  .passos { grid-template-columns: repeat(2, minmax(0, 1fr)); row-gap: 16px; }
  .passos li + li { border-left: 0; padding-left: 0; }
  .passos li:nth-child(even) { padding-left: 16px; border-left: 1px solid var(--linia); }
  .col-serie { width: auto; }
  .evid { grid-template-columns: minmax(0, 1fr); }
  .ev + .ev { border-left: 0; border-top: 1px solid var(--linia); }
  .previ { display: none; }
}
@media (max-width: 760px) {
  body { padding-bottom: 76px; }
  .barra-in { grid-template-columns: minmax(0, 1fr) auto; grid-template-areas: "marca tema" "pindola pindola" "cerca cerca"; padding: 12px 16px; gap: 8px 12px; }
  .marca b { font-size: 19px; }
  .marca small { font-size: 12px; }
  .pindola { justify-self: start; font-size: 12px; min-height: 28px; padding: 2px 9px; }
  .cb-cap { width: 100%; justify-self: stretch; }
  .cb-kbd { display: none; }
  .cb-pop, .cb-cap .cb-pop { left: 0; right: 0; min-width: 0; }
  .sug { grid-template-columns: minmax(0, 1fr); }
  .sug .sr { grid-row: auto; grid-column: 1; grid-template-columns: repeat(10, minmax(0, 1fr)); width: 100%; }
  /* Pestanyes inferiors fixes */
  .nav { position: fixed; left: 0; right: 0; bottom: 0; z-index: 30; margin: 0; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0; border-top: 1px solid var(--linia-forta); background: var(--sup); padding: 0 8px env(safe-area-inset-bottom); box-shadow: 0 -4px 16px rgba(0, 0, 0, .06); }
  .nav a { flex-direction: column; justify-content: center; gap: 2px; min-height: 60px; padding: 6px 4px; font-size: 12px; border-bottom: 0; border-top: 3px solid transparent; }
  .nav a[aria-current="page"] { border-top-color: var(--tinta); border-bottom: 0; }
  .nav svg { display: block; }
  .pagina { padding: 0 16px 40px; }
  h1 { font-size: 32px; }
  .obertura { padding: 28px 0 28px; }
  .entradeta { font-size: 17px; }
  .bloc { padding: 32px 0; }
  .heroi-xifra b { font-size: 76px; }
  .heroi-xifra span { font-size: 18px; }
  .dreceres { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; }
  .drec { padding: 12px; }
  .drec-n b { font-size: 26px; }
  .ll-estats { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .ll-estats li { padding: 14px 12px 14px 0; border-bottom: 1px solid var(--linia); }
  .ll-estats li + li { padding-left: 0; border-left: 0; }
  .ll-estats li:nth-child(even) { padding-left: 12px; border-left: 1px solid var(--linia); }
  .ll-xifra { font-size: 32px; }
  .passos { grid-template-columns: minmax(0, 1fr); }
  .passos li:nth-child(even) { padding-left: 0; border-left: 0; }
  .passos li { flex-direction: row; align-items: flex-start; gap: 12px; padding: 14px 0 0; }
  .passos li + li { border-top: 1px solid var(--linia); }
  .pq-n { flex: none; width: 28px; }
  .llarg { display: none; }
  .curt { display: inline; }
  .taula-anys th, .taula-anys td { padding: 6px 5px; }
  .taula-anys { font-size: 13px; }
  .taula-anys th:first-child { width: 46px; }
  .taula-anys th:last-child { width: 46px; }
  .taula-anys td.ta small { display: block; }
  .taula-etiq th, .taula-etiq td { padding: 6px 4px; }
  .taula-etiq td { min-width: 0; }
  .taula-etiq .tc-n, .taula-etiq .col-files { display: none; }
  .taula-etiq { table-layout: fixed; }
  .taula-etiq thead th { white-space: normal; }
  .taula-etiq th:first-child { width: 86px; }
  .taula-etiq .etq { display: flex; flex-direction: column; align-items: flex-start; gap: 2px; background: transparent; padding: 0; font-size: 12px; white-space: normal; }
  .taula-etiq .tc-files { display: block; font-size: 12px; font-weight: 400; color: var(--tinta-3); }
  .taula-etiq .tc-v { font-size: 15px; white-space: nowrap; }
  .a2, .bany small { display: none; }
  .versio-dl div { grid-template-columns: minmax(0, 1fr); }
  #dubtes .bs li { grid-template-columns: minmax(0, 1fr); padding: 10px 0; }
  /* Empreses */
  .cb-llista-emp input { font-size: 21px; height: 54px; }
  .filtres { gap: 12px; }
  .filtres .camp { flex: 1 1 100%; }
  .filtres select { width: 100%; }
  .taula-emp, .taula-emp tbody, .taula-emp thead { display: block; }
  .taula-emp thead tr { display: flex; flex-wrap: wrap; gap: 4px 16px; padding: 4px 0; }
  .taula-emp thead th { padding: 0; border: 0; }
  .taula-emp thead th.col-serie { display: none; }
  .taula-emp tbody tr { display: grid; grid-template-columns: minmax(0, 1fr); gap: 8px; padding: 16px 0; border-bottom: 1px solid var(--linia); position: relative; }
  .taula-emp tbody tr[hidden] { display: none; }
  .taula-emp td { padding: 0; border: 0; }
  /* Tota la targeta és l'enllaç a la fitxa (objectiu tàctil gran). */
  .taula-emp td:first-child a.emp-nom::after { content: ""; position: absolute; inset: 0; }
  .taula-emp td:first-child a.emp-nom { display: inline-flex; align-items: center; min-height: 40px; }
  .taula-emp td:nth-child(3) { display: flex; align-items: center; gap: 10px; }
  .taula-emp td:nth-child(3) .sub { margin: 0; }
  .taula-emp td:nth-child(4) { display: none; }
  .sr { display: grid; grid-template-columns: repeat(10, minmax(0, 1fr)); gap: 3px; width: 100%; }
  .sr i { height: 34px; }
  /* Fitxa */
  .fitxa-cap { grid-template-columns: minmax(0, 1fr); }
  .fc-resum, .fc-etq, .fitxa-estat { align-items: flex-start; justify-content: flex-start; text-align: left; }
  .mb-gran { width: 100%; max-width: 320px; }
  .rail-envol { position: static; }
  .rail { grid-template-columns: repeat(5, minmax(0, 1fr)); }
  .rl { min-height: 76px; }
  .tl::before { left: 21px; }
  .tl-any { grid-template-columns: 44px minmax(0, 1fr); gap: 0 10px; scroll-margin-top: 12px; }
  .tl-a { font-size: 15px; }
  .tl-punt { width: 26px; height: 26px; font-size: 12px; }
  .tl-fila { padding: 12px 14px; gap: 8px 10px; }
  .tl-ceo { flex-basis: 100%; }
  .tl-ceo b { font-size: 19px; }
  .tl-evid > summary { padding: 10px 14px; }
  .ev { padding: 16px 14px; }
  .ev-cita .cita { padding: 12px 12px 12px 28px; }
  .ev-cita .cita::before { left: 6px; }
  .ev-cita .cita p { font-size: 17px; }
  .ev-avisos, .tl-peu { padding: 12px 14px; }
  .botons .boto { width: 100%; justify-content: flex-start; }
  .def { grid-template-columns: minmax(0, 1fr); }
  .p-anys { margin-left: 0; }
  .prova { padding: 12px; }
  .cita { padding: 10px 12px 10px 32px; }
  .nav-fitxes { grid-template-columns: minmax(0, 1fr); }
  .nav-fitxes .seg { text-align: left; }
  /* Objectius tàctils de 40 px com a mínim. */
  .bs-link, .verif a, .tl-peu a, a.regla, .regla-frase a, .caixa-dubte a, .falta-txt a, .exemples a, .ll-mes, .cb-peu a,
  .taula-emp thead button, .xip, .pindola, .docs a, .salta, .tl-prova a, .copia, .molla a { min-height: 40px; display: inline-flex; align-items: center; gap: .3em; }
  a.regla { min-width: 40px; }
  details.dades > summary, details.tecnic > summary { min-height: 40px; }
  .ll-ajuda { width: 40px; height: 40px; }
}
@media (max-width: 360px) {
  .heroi-xifra b { font-size: 64px; }
  .dreceres { grid-template-columns: minmax(0, 1fr); }
  .rl-a { font-size: 14px; }
}
@media (forced-colors: active) {
  .sb-s, .mb i, .eb-barra, .bs-barra, .bar, .mm i, .sw, .sw-ratlla, .sr i, .sr i::after, .rl::after, .rl-e, .tl-punt, .etq b, .cel { forced-color-adjust: none; }
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { transition: none !important; animation: none !important; scroll-behavior: auto !important; }
}
@media print {
  @page { size: A4; margin: 10mm 12mm; }
  html { font-size: 8.5pt; }
  body { background: #fff; font-size: 8.5pt; line-height: 1.35; }
  * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .barra, .cerca-rapida, .filtres, .filtre-anys, .nav-fitxes, .salta, .peu, details.dades, .bs-link { display: none !important; }
  .pagina { max-width: none; padding: 0; }
  a { color: inherit; text-decoration: none; }
  .ext { display: none; }
  h1 { font-size: 16pt; margin-bottom: 2pt; }
  h2 { font-size: 11pt; margin-bottom: 2pt; }
  .entradeta, .resposta { font-size: 9pt; margin-bottom: 3pt; max-width: none; }
  .nota, .nota-clara, .mini, small, .ll-def, .bs-det, .bs-que, .tc-n { font-size: 7pt; }
  .nota-clara { margin-bottom: 3pt; }
  .taula-etiq, .taula-anys { font-size: 7.5pt; }
  .taula-etiq th, .taula-etiq td { padding: 1pt 3pt; }
  .taula-etiq thead th, .taula-anys thead th { font-size: 7pt; }
  .taula-anys td.ta b, .taula-anys td.ta small { display: inline; }
  .taula-anys .mm { margin-top: 0; }
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
  .taula-anys td.ta { padding: 1pt 5pt; }
  .taula-anys .mm { height: 2.5pt; }
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
  .taula-anys .llarg { display: none; }
  .taula-anys .curt { display: inline; }
  .tick-menor span { display: none; }
  .sb .e-F, .ll-etiq .sw.e-F { background: repeating-linear-gradient(45deg, var(--e-F) 0 3px, #f3c8b4 3px 5px); }
  .grafic .barres { height: 56pt; }
  .versio > .nota, #anys .nota { display: none; }
  .passos li { padding: 2pt 4pt; }
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
  /* Marc editorial: una sola columna, sense elements interactius. */
  body { padding-bottom: 0; }
  .tema, .nav, .cb, .cerca-rapida, .dreceres, .dreceres + .nota, .exemples, .copia { display: none !important; }
  .obertura { display: block; padding: 0 0 4pt; border: 0; }
  .obertura .entradeta { font-size: 9pt; }
  .bloc { display: block; padding: 0; border: 0; }
  .bloc-n { display: none; }
  .bloc-cap h2 { margin-bottom: 2pt; }
  .heroi-xifra { margin: 0 0 4pt; gap: 0 6pt; }
  .heroi-xifra b { font-size: 22pt; line-height: 1; }
  .heroi-xifra span { font-size: 10pt; }
  .ll-estats { margin-top: 3pt; border-top: 0; }
  .ll-estats li, .ll-estats li + li { padding: 0 6pt 0 0; border: 0; }
  .ll-cap { font-size: 8pt; }
  .ll-n { margin: 1pt 0 0; }
  .ll-xifra { font-size: 11pt; }
  .ll-pc { font-size: 7.5pt; }
  .resposta { font-family: var(--font); }
  .eb-val, .bs-val { font-size: 9pt; }
  .eb-nom { font-size: 8pt; margin-bottom: 1pt; }
  .eb-salt { padding: 1pt 0 1pt 6pt; }
  .bs li { padding: 0; border: 0; }
  .tc-v { font-size: 8pt; }
  .pq-n { font-size: 10pt; }
  .pq-t > span b { font-size: 8pt; }
  .passos li, .passos li + li { padding: 2pt 4pt; border-left: 0; }
  .grafic { margin-top: 4pt; }
  .bany { border-top-width: .5pt; }
  .taula-anys tbody th { font-size: 7.5pt; }
  .versio-linia { margin: 2pt 0; }
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
    return (s || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/\s+/g, ' ').trim();
  }
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.'); }
  function conte(llista, valor) { return (' ' + (llista || '') + ' ').indexOf(' ' + valor + ' ') >= 0; }
  function st(tr) { return (tr.dataset.st || '0 0 0 0').split(' ').map(Number); }
  // Claus d'ordre: el nom normalitzat i el % de files acabades (no van a l'HTML).
  files.forEach(function (tr) {
    var a = tr.querySelector('.emp-nom'), s = st(tr), n = s[0] + s[1] + s[2] + s[3];
    tr._ordre = { n: norm(a ? a.textContent : ''), pa: n ? Math.round(100 * s[0] / n) : 0 };
  });
  function clauOrdre(tr, clau) { return clau === 'f' ? +tr.dataset.f : tr._ordre[clau]; }

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
      var x = clauOrdre(a, clau), y = clauOrdre(b, clau), r;
      if (num) { r = x - y; } else { r = x < y ? -1 : x > y ? 1 : 0; }
      if (r === 0) { return a._ordre.n < b._ordre.n ? -1 : a._ordre.n > b._ordre.n ? 1 : 0; }
      return r * ordre.dir;
    });
    var frag = document.createDocumentFragment();
    files.forEach(function (tr) { frag.appendChild(tr); });
    tbody.appendChild(frag);
    taula.querySelectorAll('thead button[data-ordre]').forEach(function (b) {
      var th = b.parentElement;
      if (b.getAttribute('data-ordre') === ordre.clau) { th.setAttribute('aria-sort', ordre.dir > 0 ? 'ascending' : 'descending'); }
      else { th.removeAttribute('aria-sort'); }
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

JS_FITXA = r"""/* Fitxa d'empresa: franja d'anys (fletxes ←/→), obertura de l'any i de les proves
   segons el hash i filtre de proves per any. Generat per dashboard/genera_dashboard.py. Sense dependències. */
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

  /* Franja d'anys: una sola parada de tabulació i fletxes per passar d'any. */
  var rail = document.querySelector('.rail');
  var anys = rail ? Array.prototype.slice.call(rail.querySelectorAll('a.rl')) : [];
  function marcaAny(any) {
    var actual = null;
    anys.forEach(function (a) {
      var on = a.getAttribute('href') === '#any-' + any;
      if (on) { a.setAttribute('aria-current', 'true'); actual = a; } else { a.removeAttribute('aria-current'); }
    });
    anys.forEach(function (a) { a.tabIndex = a === (actual || anys[anys.length - 1]) ? 0 : -1; });
  }
  if (anys.length) {
    var cur = rail.querySelector('a.rl[aria-current]');
    anys.forEach(function (a) { a.tabIndex = a === (cur || anys[anys.length - 1]) ? 0 : -1; });
    rail.addEventListener('keydown', function (ev) {
      var i = anys.indexOf(document.activeElement);
      if (i < 0) return;
      var j = ev.key === 'ArrowRight' || ev.key === 'ArrowDown' ? i + 1 : ev.key === 'ArrowLeft' || ev.key === 'ArrowUp' ? i - 1 :
        ev.key === 'Home' ? 0 : ev.key === 'End' ? anys.length - 1 : null;
      if (j === null) return;
      ev.preventDefault();
      j = Math.max(0, Math.min(anys.length - 1, j));
      anys.forEach(function (a, k) { a.tabIndex = k === j ? 0 : -1; });
      anys[j].focus();
    });
  }

  var inici = true;
  function obre() {
    var id = '';
    try { id = decodeURIComponent(location.hash.replace(/^#/, '')); } catch (e) { id = ''; }
    var el = id ? document.getElementById(id) : null;
    if (!el) { inici = false; return; }
    if (/^any-\d{4}$/.test(id)) {
      var plegable = el.querySelector('details.tl-evid');
      if (plegable) plegable.open = true;
      // En obrir la pàgina amb un any, es tanca l'any obert per defecte (l'últim).
      if (inici) {
        var def = document.querySelector('details.tl-evid[data-defecte]');
        if (def && def !== plegable) def.open = false;
      }
      marcaAny(id.slice(4));
    } else {
      if (el.tagName === 'DETAILS') { el.open = true; }
      var pare = el.parentElement;
      while (pare) {
        if (pare.tagName === 'DETAILS') { pare.open = true; }
        if (pare.hidden && pare.classList.contains('grup-proves')) { filtra(''); }
        pare = pare.parentElement;
      }
      if (el.hidden) { filtra(''); }
    }
    inici = false;
    el.scrollIntoView();
  }

  document.addEventListener('click', function (ev) {
    var el = ev.target.closest ? ev.target.closest('[data-filtre-any]') : null;
    if (!el || !proves.length) return;
    var any = el.getAttribute('data-filtre-any') || '';
    if (el.tagName !== 'A') ev.preventDefault();
    filtra(any);
  });
  // Un enllaç al mateix hash no dispara «hashchange»: es torna a obrir a mà.
  document.addEventListener('click', function (ev) {
    var a = ev.target.closest ? ev.target.closest('a[href^="#any-"], a[href^="#p-"]') : null;
    if (a && a.hash && a.hash === location.hash) { obre(); }
  });
  window.addEventListener('hashchange', obre);
  obre();
})();
"""

JS_COMU = r"""/* Comú a totes les pàgines: mode clar/fosc, cercador amb suggeriments (combobox)
   i botons de copiar. Generat per dashboard/genera_dashboard.py. Sense dependències. */
(function () {
  'use strict';
  var doc = document.documentElement;

  /* ---------- Mode clar / fosc ---------- */
  var SOL = '<svg viewBox="0 0 20 20" focusable="false"><circle cx="10" cy="10" r="3.6" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M10 2v2.2M10 15.8V18M2 10h2.2M15.8 10H18M4.3 4.3l1.6 1.6M14.1 14.1l1.6 1.6M4.3 15.7l1.6-1.6M14.1 5.9l1.6-1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>';
  var LLUNA = '<svg viewBox="0 0 20 20" focusable="false"><path d="M15.5 12.6A6.5 6.5 0 0 1 7.4 4.5a6.5 6.5 0 1 0 8.1 8.1z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>';
  var botoTema = document.querySelector('.tema');
  var mq = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  function esFosc() {
    var t = doc.getAttribute('data-theme');
    return t ? t === 'dark' : !!(mq && mq.matches);
  }
  function pintaTema() {
    if (!botoTema) return;
    var f = esFosc();
    botoTema.setAttribute('aria-pressed', f ? 'true' : 'false');
    botoTema.title = f ? 'Passa al mode clar' : 'Passa al mode fosc';
    botoTema.querySelector('.tema-i').innerHTML = f ? SOL : LLUNA;
  }
  if (botoTema) {
    botoTema.addEventListener('click', function () {
      var nou = esFosc() ? 'light' : 'dark';
      doc.setAttribute('data-theme', nou);
      try { localStorage.setItem('fc-tema', nou); } catch (e) { /* sense emmagatzematge: només aquesta pàgina */ }
      pintaTema();
    });
    if (mq) {
      if (mq.addEventListener) mq.addEventListener('change', pintaTema);
      else if (mq.addListener) mq.addListener(pintaTema);
    }
    pintaTema();
  }

  /* ---------- Cercador amb suggeriments ---------- */
  function norm(s) {
    return (s || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/\s+/g, ' ').trim();
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  }
  var NOM_ETQ = { F: 'F', P: 'P', D: 'ND', N: 'NA' };
  var IDX = null, carregant = false, esperen = [];
  function prepara(llista) {
    return llista.map(function (r) {
      var ceos = r[3] ? r[3].split('|') : [];
      var darrer = 0;
      for (var i = 0; i < 10; i++) { if (r[5].substr(2 * i, 2) !== '--') darrer = 2016 + i; }
      return { isin: r[0], nom: r[1], nomN: norm(r[1]), ceos: ceos, ultim: (r[4] || '').split('|').join(' · '), serie: r[5], darrer: darrer,
               tot: norm(r[1]) + ' ' + r[2] + ' ' + r[0].toLowerCase() + ' ' + norm(ceos.join(' ')) };
    });
  }
  function ambIndex(prefix, fet) {
    if (IDX) { fet(); return; }
    if (window.CERCA_IDX) { IDX = prepara(window.CERCA_IDX); fet(); return; }
    esperen.push(fet);
    if (carregant) return;
    carregant = true;
    var s = document.createElement('script');
    s.src = prefix + 'assets/index_cerca.js';
    s.onload = function () { IDX = prepara(window.CERCA_IDX || []); var f = esperen; esperen = []; f.forEach(function (x) { x(); }); };
    s.onerror = function () { carregant = false; esperen = []; };
    document.head.appendChild(s);
  }
  function busca(q) {
    var qn = norm(q), termes = qn.split(' ').filter(Boolean);
    if (!termes.length || !IDX) return [];
    var r = [];
    IDX.forEach(function (e) {
      for (var j = 0; j < termes.length; j++) { if (e.tot.indexOf(termes[j]) < 0) return; }
      var p = e.nomN.indexOf(qn) === 0 ? 0 : (' ' + e.nomN).indexOf(' ' + qn) >= 0 ? 1 : e.nomN.indexOf(qn) >= 0 ? 2 :
        e.isin.toLowerCase().indexOf(qn) === 0 ? 3 : 4;
      r.push([p, e]);
    });
    r.sort(function (a, b) { return a[0] - b[0] || (a[1].nomN < b[1].nomN ? -1 : a[1].nomN > b[1].nomN ? 1 : 0); });
    return r.slice(0, 7).map(function (x) { return x[1]; });
  }
  function resalta(text, termes) {
    var n = norm(text), marques = [];
    if (n.length !== text.length) return esc(text);
    termes.forEach(function (t) { var i = n.indexOf(t); if (i >= 0) marques.push([i, i + t.length]); });
    marques.sort(function (a, b) { return a[0] - b[0]; });
    var out = '', pos = 0;
    marques.forEach(function (m) {
      if (m[0] < pos) return;
      out += esc(text.slice(pos, m[0])) + '<mark>' + esc(text.slice(m[0], m[1])) + '</mark>';
      pos = m[1];
    });
    return out + esc(text.slice(pos));
  }
  function serie(e) {
    var h = '<span class="sr" aria-hidden="true">';
    for (var i = 0; i < 10; i++) {
      var c = e.serie.substr(2 * i, 2);
      h += c === '--' ? '<i></i>' : '<i class="' + NOM_ETQ[c[0]] + ' ' + c[1] + '">' + NOM_ETQ[c[0]] + '</i>';
    }
    return h + '</span>';
  }

  Array.prototype.forEach.call(document.querySelectorAll('[data-combobox]'), function (form, nForm) {
    var input = form.querySelector('input');
    var llista = form.querySelector('[role="listbox"]');
    var viu = form.querySelector('.cb-viu');
    var local = form.hasAttribute('data-local');
    var prefix = form.getAttribute('data-prefix') || '';
    var pop = document.createElement('div');
    pop.className = 'cb-pop';
    pop.hidden = true;
    llista.parentNode.insertBefore(pop, llista);
    pop.appendChild(llista);
    llista.hidden = false;
    var peu = document.createElement('p');
    peu.className = 'cb-peu';
    pop.appendChild(peu);
    var opcions = [], actiu = -1;

    function tanca() {
      pop.hidden = true;
      input.setAttribute('aria-expanded', 'false');
      input.removeAttribute('aria-activedescendant');
      actiu = -1;
    }
    function mou(i) {
      opcions.forEach(function (o, k) { o.setAttribute('aria-selected', k === i ? 'true' : 'false'); });
      actiu = i;
      if (i >= 0) {
        input.setAttribute('aria-activedescendant', opcions[i].id);
        if (opcions[i].scrollIntoView) opcions[i].scrollIntoView({ block: 'nearest' });
      } else {
        input.removeAttribute('aria-activedescendant');
      }
    }
    function pinta() {
      var q = input.value.trim();
      if (!q) { tanca(); if (viu) viu.textContent = ''; return; }
      ambIndex(prefix, function () {
        if (input.value.trim() !== q) return;
        var termes = norm(q).split(' ').filter(Boolean);
        var r = busca(q), h = '';
        r.forEach(function (e, k) {
          var ceosQ = e.ceos.filter(function (c) { var n = norm(c); return termes.some(function (t) { return t.length > 1 && n.indexOf(t) >= 0; }); });
          var sub = '<code>' + resalta(e.isin, termes) + '</code> · ' +
            (ceosQ.length ? 'CEO: ' + ceosQ.map(function (c) { return resalta(c, termes); }).join(', ')
              : 'CEO ' + e.darrer + ': ' + esc(e.ultim || 'sense CEO'));
          h += '<li role="option" class="sug" id="' + llista.id + '-o' + k + '" aria-selected="false" data-href="' + prefix + 'empreses/' + e.isin + '.html">' +
            '<span class="sug-nom">' + resalta(e.nom, termes) + '</span>' + serie(e) + '<span class="sug-sub">' + sub + '</span></li>';
        });
        llista.innerHTML = h;
        llista.hidden = !r.length;
        peu.innerHTML = (r.length ? '' : '<span class="cb-buit">Cap empresa no coincideix. Prova amb part del nom, l\'ISIN o el cognom del CEO.</span>') +
          (local ? '' : '<a href="' + prefix + 'empreses.html?q=' + encodeURIComponent(q) + '">Veure tots els resultats a Empreses <span aria-hidden="true">→</span></a>');
        peu.hidden = !peu.innerHTML;
        opcions = Array.prototype.slice.call(llista.querySelectorAll('.sug'));
        opcions.forEach(function (o, k) {
          o.addEventListener('mousedown', function (ev) { ev.preventDefault(); location.href = o.getAttribute('data-href'); });
          o.addEventListener('mousemove', function () { if (actiu !== k) mou(k); });
        });
        actiu = -1;
        input.removeAttribute('aria-activedescendant');
        pop.hidden = false;
        input.setAttribute('aria-expanded', 'true');
        if (viu) viu.textContent = r.length ? (r.length === 1 ? '1 suggeriment' : r.length + ' suggeriments') + '. Fes servir les fletxes per triar-ne un.' : 'Cap suggeriment.';
      });
    }
    input.addEventListener('input', pinta);
    input.addEventListener('focus', function () { ambIndex(prefix, function () {}); if (input.value.trim() && input.getAttribute('aria-expanded') !== 'true' && !local) pinta(); });
    input.addEventListener('blur', function () { setTimeout(tanca, 150); });
    input.addEventListener('keydown', function (ev) {
      if (ev.key === 'ArrowDown' || ev.key === 'ArrowUp') {
        ev.preventDefault();
        if (pop.hidden) { pinta(); return; }
        if (!opcions.length) return;
        if (ev.key === 'ArrowDown') mou(actiu + 1 >= opcions.length ? 0 : actiu + 1);
        else mou(actiu <= 0 ? opcions.length - 1 : actiu - 1);
      } else if (ev.key === 'Escape') {
        if (!pop.hidden) { ev.preventDefault(); tanca(); }
      } else if (ev.key === 'Enter') {
        if (!pop.hidden && actiu >= 0) { ev.preventDefault(); location.href = opcions[actiu].getAttribute('data-href'); }
        else if (local) { ev.preventDefault(); tanca(); }
      } else if (ev.key === 'Tab') {
        tanca();
      }
    });
  });

  /* Drecera «/»: porta al cercador (a Empreses, al de la llista). */
  document.addEventListener('keydown', function (ev) {
    if (ev.key !== '/' || ev.ctrlKey || ev.metaKey || ev.altKey) return;
    var a = document.activeElement;
    if (a && (/^(input|textarea|select)$/i.test(a.tagName) || a.isContentEditable)) return;
    var camps = Array.prototype.slice.call(document.querySelectorAll('[data-combobox][data-local] input'))
      .concat(Array.prototype.slice.call(document.querySelectorAll('[data-combobox]:not([data-local]) input')));
    for (var i = 0; i < camps.length; i++) {
      if (camps[i].offsetParent !== null) { ev.preventDefault(); camps[i].focus(); return; }
    }
  });

  /* ---------- Botons de copiar ---------- */
  var viuCopia = document.createElement('div');
  viuCopia.className = 'vh';
  viuCopia.setAttribute('aria-live', 'polite');
  document.body.appendChild(viuCopia);
  function copiaAntic(text) {
    var t = document.createElement('textarea');
    t.value = text;
    t.setAttribute('readonly', '');
    t.style.position = 'fixed';
    t.style.opacity = '0';
    document.body.appendChild(t);
    t.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    document.body.removeChild(t);
    return ok;
  }
  function copia(text, boto, que) {
    var original = boto.getAttribute('data-original') || boto.textContent;
    boto.setAttribute('data-original', original);
    function fet(ok) {
      boto.textContent = ok ? 'Copiat ✓' : 'No s\'ha pogut copiar';
      viuCopia.textContent = ok ? que + ' copiat al porta-retalls.' : 'No s\'ha pogut copiar.';
      setTimeout(function () { boto.textContent = original; }, 1600);
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(function () { fet(true); }, function () { fet(copiaAntic(text)); });
    } else {
      fet(copiaAntic(text));
    }
  }
  document.addEventListener('click', function (ev) {
    var b = ev.target.closest ? ev.target.closest('[data-copia], [data-copia-cita]') : null;
    if (!b) return;
    if (b.hasAttribute('data-copia')) { copia(b.getAttribute('data-copia'), b, 'Text'); return; }
    var bloc = b.closest('.ev-ext') || b.closest('.ev');
    var p = bloc ? bloc.querySelector('.cita p') : null;
    if (p) copia(p.textContent.replace(/\s*\[…\]$/, ''), b, 'Cita');
  });
})();
"""


if __name__ == "__main__":
    raise SystemExit(main())

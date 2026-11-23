#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Importa al registre les cites candidates (traspas/candidates_evidencia.csv) per a les files d'un lot.

Per a cada fila del lot que avui no compleix C1 (CEO) o C2 (fundador) segons
estat/estat_files.csv, tria la millor cita candidata i en fa una entrada del registre
amb el format de CLAUDE.md §6. Una mateixa cita (ISIN, funció, URL, text) que serveix
per a diversos anys és una sola entrada.

Criteris de selecció:
  CEO       la cita anomena el CEO de la fila i conté un títol de primer executiu.
  Fundador  F: la cita anomena el CEO i conté un mot de fundació (founder, fundador, gründer…).
            P: cites del tipus que demana la regla de `regles` (a: llista de fundadors;
            b: any de fundació i naixement; d: ocupador anterior i any de fundació; e: origen),
            o la cita de classificació de r3e del model que dona la mateixa etiqueta.
  Prioritat: ja verificada per script de DF; després document de l'exercici (CEO); no
            agregador; nivell A.
  Si cap candidata no està verificada i s'usa --verifica, Claude baixa el document original
  i hi busca la cita literal. Si la troba: [V]; si no s'obre: [NV] amb pendent_DF.

Per defecte és una prova en sec (només recomptes). Amb --escriu afegeix les entrades al
registre i les cites a les fitxes.

  python3 traspas/importa_lot.py lots/lot11.csv --lot 11
  python3 traspas/importa_lot.py lots/lot11.csv --lot 11 --verifica --escriu
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import html
import importlib.util
import re
import subprocess
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "dades" / "base_isin_any_v8r3.csv"
REG = ROOT / "docs" / "REGISTRE_CANVIS.csv"
CANDS = ROOT / "traspas" / "candidates_evidencia.csv"
ESTAT = ROOT / "estat" / "estat_files.csv"
FITXES = ROOT / "empreses"

spec = importlib.util.spec_from_file_location("estat_files", ROOT / "estat" / "estat_files.py")
EF = importlib.util.module_from_spec(spec)
spec.loader.exec_module(EF)

VER = {"web_verificada": "DF (script verifica_evidencies_web_r4.py, 18/11/2026: cita literal al document baixat)",
       "r3e_verificada": "DF (script certifica_r3e_r4.py, 17-18/11/2026: cita literal al text del document del paquet r3e)",
       "v75_cita_a_captura": "DF (script de la v7.5, 16-17/11/2026: cita literal a la captura Wayback)"}
AGREGADORS = ("annualreports.com", "companiesmarketcap.com", "marketscreener.com", "zonebourse.com")
REGULADORS = ("sec.gov", "cnmv.es", "amf-france.org", "londonstockexchange.com", "company-information.service.gov.uk",
              "fca.org.uk", "consob.it", "bundesanzeiger.de", "unternehmensregister.de", "euronext.com", "nasdaq.com",
              "six-group.com", "ser-ag.com", "oslobors.no", "newsweb.no", "finanstilsynet", "knf.gov.pl", "gpw.pl",
              "borsaitaliana.it", "fi.se", "dfsa.dk", "cbi.ie", "afm.nl", "fsma.be", "cmvm.pt", "bolsamadrid.es")
PLATAFORMES = ("cision.com", "globenewswire.com", "eqs.com", "eqs-news.com", "businesswire.com", "prnewswire.com",
               "mfn.se", "investegate.co.uk", "mynewsdesk.com", "filings.xbrl.org", "financialreports.eu",
               "investis.com", "q4cdn.com", "rns-pdf", "emarketstorage", "1info.it", "lsegissuerservices.com")
FUNDACIO = re.compile(r"found|fundad|fundat|fundador|grunder|grundare|grundlag|grundet|grunnla|gegrund|grunde"
                      r"|fondat|fondateur|fondatrice|fondee|fonde par|oprichter|opgericht|perustaja|perusti"
                      r"|zalozyciel|zalozyl|stiftet|stifter|set up|established|started the|launched the"
                      r"|created the company|creat(ed|or) of")
# P6: expressions que no compten com a fundador
EXCLOU_P6 = re.compile(r"founding (ceo|chief executive|shareholder|member|members|partner|chairman|director|team member)"
                       r"|ceo fundador|consejero delegado fundador|founder[- ]led|fondateur[- ]dirigeant")
ABREV = re.compile(r"(?:\b(?:mr|mrs|ms|dr|prof|st|inc|ltd|plc|co|corp|no|nr|jr|sr|n\.v|s\.a|s\.p\.a|ag|se|vs|e\.g|i\.e))\.$", re.I)
NECESSITA = {"a": [{"llista_fundadors"}], "b": [{"any_fundacio", "naixement_ceo"}],
             "b_per_part": [{"any_fundacio", "naixement_ceo"}], "d": [{"ocupador_anterior", "any_fundacio"}],
             "d_per_part": [{"ocupador_anterior", "any_fundacio"}], "e": [{"origen_entitat"}],
             "c_AAF64_reserva": [{"any_fundacio"}]}
CACHE = None


def domini(url: str) -> str:
    return urlparse(url).netloc.lower()


def es_agregador(url: str) -> bool:
    return any(a in domini(url) for a in AGREGADORS)


def allotjament(url: str, nivell: str) -> str:
    d = domini(url) + urlparse(url).path.lower()
    if any(a in d for a in AGREGADORS) or any(p in d for p in PLATAFORMES):
        return "plataforma"
    if any(r in d for r in REGULADORS):
        return "regulador"
    return "emissor" if nivell != "B" else "mitja"


def any_doc(c: dict) -> int | None:
    m = re.match(r"(\d{4})", c.get("data_document") or "")
    return int(m.group(1)) if m else None


def norm_text(s: str) -> str:
    s = html.unescape(s)
    s = unicodedata.normalize("NFKC", s).replace("­", "")
    s = re.sub(r"[‘’‚‛′`´]", "'", s)
    s = re.sub(r"[“”„«»]", '"', s)
    s = re.sub(r"[‐-―−]", "-", s)
    s = re.sub(r"-\s*\n\s*", "", s)
    return re.sub(r"\s+", " ", s).lower()


def verifica(url: str, cita: str) -> tuple[str, str]:
    """Baixa el document original i hi busca la cita. Retorna (estat, detall)."""
    CACHE.mkdir(parents=True, exist_ok=True)
    fn = CACHE / hashlib.sha256(url.encode()).hexdigest()
    txt = fn.with_suffix(".txt")
    if not txt.exists():
        try:
            p = subprocess.run(["curl", "-sSL", "--max-time", "60", "--max-filesize", "80000000",
                                "-A", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
                                "-o", str(fn), "-w", "%{http_code}", url], capture_output=True, text=True, timeout=90)
            code = p.stdout.strip()
        except Exception as ex:  # noqa: BLE001
            return "no_accessible", f"error {str(ex)[:60]}"
        if code != "200" or not fn.exists() or fn.stat().st_size == 0:
            txt.write_text(f"#ERROR HTTP {code}", encoding="utf-8")
        else:
            raw = fn.read_bytes()
            if raw[:4] == b"%PDF":
                t = subprocess.run(["pdftotext", "-q", str(fn), "-"], capture_output=True, timeout=180).stdout.decode("utf-8", "ignore")
            else:
                h = raw.decode("utf-8", "ignore")
                h = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", h)
                t = re.sub(r"<[^>]+>", " ", h)
            txt.write_text(t, encoding="utf-8")
    t = txt.read_text(encoding="utf-8")
    if t.startswith("#ERROR"):
        return "no_accessible", t[1:40]
    if fn.exists() and fn.read_bytes()[:2] == b"PK":
        # informe ESEF o paquet zip: text de tots els fitxers HTML/XHTML
        import io
        import zipfile
        try:
            z = zipfile.ZipFile(io.BytesIO(fn.read_bytes()))
            parts = []
            for nom in z.namelist():
                if nom.lower().endswith((".xhtml", ".html", ".htm")) and z.getinfo(nom).file_size < 200_000_000:
                    h = z.read(nom).decode("utf-8", "ignore")
                    h = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", h)
                    parts.append(re.sub(r"<[^>]+>", " ", h))
            if parts:
                t = "\n".join(parts)
        except Exception:  # noqa: BLE001
            pass
    if len(t) < 1500:
        return "no_accessible", f"text de {len(t)} caràcters (bloqueig o pàgina amb JavaScript)"
    nc = norm_text(cita)
    if nc and nc[:250] in norm_text(t):
        return "trobada", f"{len(t)} caràcters de text"
    textos = [t]
    if fn.exists() and fn.read_bytes()[:4] == b"%PDF":
        raw = fn.with_suffix(".raw.txt")
        if not raw.exists():
            try:
                raw.write_text(subprocess.run(["pdftotext", "-q", "-raw", str(fn), "-"], capture_output=True,
                                              timeout=180).stdout.decode("utf-8", "ignore"), encoding="utf-8")
            except Exception:  # noqa: BLE001
                raw.write_text("", encoding="utf-8")
        tr = raw.read_text(encoding="utf-8")
        textos.append(tr)
        if nc and nc[:250] in norm_text(tr):
            return "trobada", f"{len(tr)} caràcters de text (pdftotext -raw, PDF a columnes)"
    sense = re.sub(r"\s+", "", nc[:250])
    if sense and any(sense in re.sub(r"\s+", "", norm_text(x)) for x in textos):
        return "trobada", "coincidència literal ignorant els espais (text extret amb espais trencats)"
    return "no_trobada", f"{len(t)} caràcters de text"


def frases(text: str) -> list[str]:
    t = re.sub(r"\s+", " ", text).strip()
    trossos, ini = [], 0
    for m in re.finditer(r"[.!?;:](?=\s+[A-ZÀ-ÖØ-Ý0-9«\"(])|\s{0}\n", t):
        fi = m.end()
        if ABREV.search(t[max(0, fi - 8):fi]):
            continue
        trossos.append(t[ini:fi].strip())
        ini = fi
    trossos.append(t[ini:].strip())
    return [x for x in trossos if x]


def norm_mapa(text: str) -> tuple[str, list[int]]:
    """Normalitza com EF.norm però caràcter a caràcter, i retorna el mapa de posicions a l'original."""
    out, mapa = [], []
    for i, ch in enumerate(text):
        n = unicodedata.normalize("NFKD", ch.translate(EF.TRANSLIT))
        n = "".join(c for c in n if not unicodedata.combining(c)).lower()
        if ch.isspace():
            n = " "
        for c in n:
            out.append(c)
            mapa.append(i)
    return "".join(out), mapa


def finestra(f: str, noms: list[str], patro: re.Pattern, exclou: re.Pattern | None) -> str:
    """Dins la frase f, comença al nom més proper abans del mot clau i talla poc després."""
    nf, mapa = norm_mapa(f)
    excl = [m.span() for m in exclou.finditer(nf)] if exclou is not None else []
    mk = next((m for m in patro.finditer(nf) if not any(a <= m.start() < b for a, b in excl)), None)
    if mk is None:
        return f
    toks = set()
    for nm in noms:
        toks.update(t for t in EF.tokens_nom(nm) if t)
    ini = 0
    millor = -1
    for t in toks:
        for m in re.finditer(r"(?<![\w])" + re.escape(t) + r"(?![\w])", nf[:mk.start()]):
            if mk.start() - m.start() <= 260 and m.start() > millor:
                millor = m.start()
    if millor >= 0:
        ini = millor
        # inclou el nom de pila o el tractament que va just abans
        abans = nf[max(0, ini - 25):ini]
        mm = re.search(r"((?:mr|mrs|ms|dr|sir|m|mme)\.?\s+)?((?:[a-z][\w'-]*\.?\s+){0,2})$", abans)
        if mm and mm.group(0).strip():
            cand = abans[mm.start():]
            if any(w.strip(".") in toks or w.strip(".") in {EF.norm(x.split()[0]) for x in noms} for w in cand.split()):
                ini -= len(cand)
    fi = len(nf)
    punt = nf.find(". ", mk.end())
    if 0 <= punt <= mk.end() + 220:
        fi = punt + 1
    elif fi > mk.end() + 120:
        tall = nf.rfind(" ", mk.end(), mk.end() + 120)
        fi = tall if tall > mk.end() else mk.end() + 120
    o_ini = mapa[ini] if ini < len(mapa) else 0
    o_fi = mapa[fi - 1] + 1 if fi - 1 < len(mapa) else len(f)
    return f[o_ini:o_fi].strip(" ,;:")


def retalla(cita: str, noms: list[str], patro: re.Pattern, exclou: re.Pattern | None = None) -> str:
    """Retorna el tros de la cita que anomena la persona i conté el patró; '' si no n'hi ha."""
    fs = frases(cita)
    def ok_pat(x):
        n = EF.norm(x)
        if exclou is not None:
            n = exclou.sub(" ", n)
        return bool(patro.search(n))
    def ok_nom(x):
        n = EF.norm(x)
        return any(EF.anomena(n, nm) for nm in noms)
    cands = [f for f in fs] + [fs[i] + " " + fs[i + 1] for i in range(len(fs) - 1)]
    for f in cands:
        if ok_pat(f) and ok_nom(f) and len(f) <= 1200:
            w = finestra(f, noms, patro, exclou)
            if ok_pat(w) and ok_nom(w) and len(w) <= 450:
                return w
            if len(f) <= 450:
                return f
    return ""


SORTIDA = re.compile(r"step(ped|s)? down|will step|resign|demission|retir|former|outgoing|left the|held the position"
                     r"|until \d|succeeded by|to be succeeded|will leave|leaves the|departure|depart|abandon|cesa|cese|dimission"
                     r"|tritt zuruck|ausgeschieden|scheidet")
TITOLS = {"mr", "mrs", "ms", "dr", "sir", "dame", "prof", "herr", "frau", "don", "dona", "d", "m", "mme", "lord",
          "chief", "ceo", "executive", "director", "chairman", "founder", "co-founder", "president", "the", "and", "our", "by"}
GENERICS = {"actions", "aktien", "namens", "inhaber", "registered", "shares", "share", "group", "holding", "holdings",
            "port", "nom", "bearer", "ordinary", "class", "akt", "reg", "stammaktien", "vorzugsaktien", "acciones",
            "azioni", "aandelen", "navne", "aktier", "namn", "osake", "company", "limited", "international",
            "europe", "european", "plc", "the", "and"}
AUTOREF = re.compile(r"\bour\b|\bwe\b|the company|the group|its founder|the business|the bank|the firm|du groupe"
                     r"|de la societe|de l'entreprise|des unternehmens|der gruppe|selskapet|bolaget|yhtio|la compania"
                     r"|la empresa|del grupo|della societa|del gruppo|het bedrijf|de onderneming")


def persona_conflictiva(cita: str, noms: list[str]) -> bool:
    """Cert si el cognom del CEO surt precedit d'un altre nom de pila (p. ex. Aditya Mittal per Lakshmi Mittal)."""
    for nom in noms:
        parts = [p.strip(".,") for p in nom.split()]
        if len(parts) < 2:
            continue
        pila = EF.norm(parts[0])
        for cog in [p for p in parts[1:] if len(p) >= 3 and EF.norm(p) not in EF.PARTICULES]:
            for m in re.finditer(r"([A-ZÀ-ÖØ-Ý][\w'\-]+)\.?\s+(?:[A-Z]\.\s*)*" + re.escape(cog), cita):
                prev = EF.norm(m.group(1))
                if prev in TITOLS or prev == pila or prev == pila[:1] or EF.norm(cog) == prev:
                    continue
                if prev in [EF.norm(x) for x in parts]:
                    continue
                return True
    return False


def esmenta_empresa(cita: str, nom_panell: str) -> bool:
    n = EF.norm(cita)
    if AUTOREF.search(n):
        return True
    toks = [EF.norm(t).strip(".,()&'") for t in re.split(r"[\s/]+", nom_panell)]
    toks = [t for t in toks if len(t) >= 4 and t not in GENERICS and not re.match(r"^[\d,.-]+$", t)]
    return any(t in n for t in toks[:3])


def puntua_ceo(c: dict, any_fila: int) -> tuple:
    y = any_doc(c)
    exercici = y in (any_fila, any_fila + 1) if y else False
    return (c["verificacio_previa"] in VER, exercici, not es_agregador(c["url"]), c["nivell_font"] == "A",
            c["font_traspas"].startswith("r4_claude"))


def puntua_fund(c: dict) -> tuple:
    return (c["verificacio_previa"] in VER, not es_agregador(c["url"]), c["nivell_font"] == "A",
            c["font_traspas"] == "fonts_v75r2")


def blocs(anys: list[int]) -> str:
    anys = sorted(set(anys))
    out, ini, prev = [], anys[0], anys[0]
    for a in anys[1:] + [None]:
        if a is not None and a == prev + 1:
            prev = a
            continue
        out.append(str(ini) if ini == prev else f"{ini}-{prev}")
        if a is not None:
            ini = prev = a
    return ",".join(out)


def main() -> int:
    global CACHE
    ap = argparse.ArgumentParser()
    ap.add_argument("lot")
    ap.add_argument("--lot", dest="n", required=True)
    ap.add_argument("--verifica", action="store_true", help="baixa i verifica les candidates no verificades")
    ap.add_argument("--escriu", action="store_true")
    ap.add_argument("--cache", default="", help="carpeta per a les baixades (fora del repositori)")
    args = ap.parse_args()
    CACHE = Path(args.cache) if args.cache else ROOT / ".cache" / "baixades"

    with BASE.open(encoding="utf-8", newline="") as f:
        base = {(r["isin"], r["any"]): r for r in csv.DictReader(f)}
    with ESTAT.open(encoding="utf-8", newline="") as f:
        estat = {(r["isin"], r["any"]): r for r in csv.DictReader(f)}
    with (ROOT / args.lot).open(encoding="utf-8", newline="") as f:
        lot = [(r["isin"], r["any"]) for r in csv.DictReader(f)]
    per = collections.defaultdict(list)
    with CANDS.open(encoding="utf-8", newline="") as f:
        for c in csv.DictReader(f):
            per[(c["isin"], c["any"])].append(c)

    tries: dict[tuple, dict] = {}   # (isin, funcio, url, cita) -> {c, anys, estat, detall}
    res = collections.Counter()
    pendents = []

    def tria(k, funcio, cands, puntua):
        cands = sorted(cands, key=puntua, reverse=True)
        for c in cands:
            if c["verificacio_previa"] in VER:
                return c, "[V]", VER[c["verificacio_previa"]], ""
        if not args.verifica:
            return (cands[0], "?", "", "") if cands else (None, "", "", "")
        primera_nv = None
        for c in cands[:4]:
            est, det = verifica(c["url"], c["cita_literal"])
            if est == "trobada":
                return c, "[V]", "Claude (script traspas/importa_lot.py, 23/11/2026: cita literal al document original baixat)", det
            if est == "no_accessible" and primera_nv is None:
                primera_nv = (c, det)
        if primera_nv:
            c, det = primera_nv
            return c, "[NV]", "Claude (script traspas/importa_lot.py, 23/11/2026)", f"pendent_DF: {det}"
        return None, "", "", ""

    for k in lot:
        r, e = base[k], estat[k]
        any_fila = int(k[1])
        cs = per.get(k, [])
        if "falta_ceo" in e["estat"].split("+") and r["FounderCEO"] in ("0", "1"):
            noms = [n.strip() for n in (r.get("ceos") or "").split("|") if n.strip()]
            cands = []
            for c in cs:
                if c["funcio"] != "ceo" or c["anomena_ceo"] != "si":
                    continue
                y = any_doc(c)
                if y not in (any_fila, any_fila + 1):
                    continue  # CLAUDE.md §3: document del mateix exercici (si no, interval de la regla 28)
                curta = retalla(c["cita_literal"], noms, EF.CARRECS)
                if not curta or SORTIDA.search(EF.norm(curta)) or persona_conflictiva(curta, noms):
                    continue
                cands.append(dict(c, cita_original=c["cita_literal"], cita_literal=curta))
            c, marca, model, det = tria(k, "ceo", cands, lambda c: puntua_ceo(c, any_fila))
            if c and marca in ("[V]", "[NV]"):
                t = tries.setdefault((k[0], "ceo", c["url"], c["cita_literal"]), {"c": c, "anys": [], "marca": marca, "model": model, "det": det})
                t["anys"].append(any_fila)
                res[f"ceo_{marca}"] += 1
            else:
                res["ceo_sense_candidata"] += 1
                pendents.append((k, "ceo"))
        if "falta_fundador" in e["estat"].split("+") and r["FounderCEO"] in ("0", "1"):
            if r["FounderCEO"] == "1":
                noms = [n.strip() for n in (r.get("ceos") or "").split("|") if n.strip()]
                cands = []
                for c in cs:
                    if c["funcio"] != "fundador" or c["anomena_ceo"] != "si":
                        continue
                    if c["font_traspas"].startswith("r3e") and c["model_etiqueta"] != "1":
                        continue
                    curta = retalla(c["cita_literal"], noms, FUNDACIO, EXCLOU_P6)
                    if not curta or persona_conflictiva(curta, noms) or not esmenta_empresa(curta, r.get("nom_panell") or ""):
                        continue
                    cands.append(dict(c, cita_original=c["cita_literal"], cita_literal=curta))
                c, marca, model, det = tria(k, "fundador", cands, puntua_fund)
                triades = [(c, marca, model, det)] if c and marca in ("[V]", "[NV]") else []
            else:
                toks = {t for t in (r.get("regles") or "").replace("|", ";").split(";") if t}
                triades = []
                r3 = [c for c in cs if c["font_traspas"].startswith("r3e") and c["model_etiqueta"] == "0" and c["model_regla"] in toks]
                v75 = [c for c in cs if c["font_traspas"] == "fonts_v75r2" and c["funcio"] == "fundador"]
                for grup in (r3, v75):
                    c, marca, model, det = tria(k, "fundador", grup, puntua_fund)
                    if c and marca in ("[V]", "[NV]"):
                        triades = [(c, marca, model, det)]
                        break
                if not triades:
                    for t in toks:
                        for conj in NECESSITA.get(t, []):
                            parcial = []
                            for tp in sorted(conj):
                                grup = [c for c in cs if c["font_traspas"].startswith("r4") and c["tipus_prova"] == tp]
                                c, marca, model, det = tria(k, "fundador", grup, puntua_fund)
                                if c and marca in ("[V]", "[NV]"):
                                    parcial.append((c, marca, model, det))
                            if len(parcial) == len(conj):
                                triades = parcial
                                break
                        if triades:
                            break
            if triades:
                for c, marca, model, det in triades:
                    t = tries.setdefault((k[0], "fundador", c["url"], c["cita_literal"]), {"c": c, "anys": [], "marca": marca, "model": model, "det": det})
                    t["anys"].append(any_fila)
                res["fundador_" + ("[V]" if all(x[1] == "[V]" for x in triades) else "[NV]")] += 1
            else:
                res["fundador_sense_candidata"] += 1
                pendents.append((k, "fundador"))

    print(f"Lot {args.n}: {len(lot)} files.")
    for kk, v in sorted(res.items()):
        print(f"  {kk}: {v}")
    print(f"Entrades noves (agrupades per cita): {len(tries)}; agregadors: "
          f"{sum(es_agregador(t['c']['url']) for t in tries.values())}")
    if not args.escriu:
        print("Prova en sec: no s'ha escrit res.")
        return 0

    # Entrades del registre
    with REG.open(encoding="utf-8", newline="") as f:
        rcap = next(csv.reader(f))
    crlf = b"\r\n" in REG.read_bytes()[:4000]
    comptador = collections.Counter()
    noves = []
    per_isin = collections.defaultdict(list)
    for (isin, funcio, url, cita), t in sorted(tries.items(), key=lambda x: (x[0][0], x[0][1], min(x[1]["anys"]), x[0][2])):
        c = t["c"]
        lletra = "C" if funcio == "ceo" else "F"
        comptador[(isin, lletra)] += 1
        ident = f"L{args.n}-{isin}-{lletra}{comptador[(isin, lletra)]:02d}"
        k0 = (isin, str(min(t["anys"])))
        r = base[k0]
        if funcio == "ceo":
            marques = r.get("marques") or ""
            marca_prova = "R2" if "interi" in marques else ("R3" if "ceo_president_exec" in marques or "de_facto" in marques else "R1")
            nc = EF.norm(cita)
            if marca_prova == "R1" and re.search(r"executive chair", nc) and not re.search(
                    r"\bceo\b|chief executive|directeur general|director general|consejero delegado|amministratore delegato|vorstand", nc):
                marca_prova = "R3"
            y = any_doc(c)
            exer = "document de l'exercici" if y and any(y in (a, a + 1) for a in t["anys"]) else \
                (f"document de {y}: no és de l'exercici; cal un document de l'exercici o un interval (regla 28)" if y else "data del document no indicada")
        else:
            toks = [x for x in (r.get("regles") or "").replace("|", ";").split(";") if x and x != "cap"]
            pref = EF.REGLES_SI if r.get("FounderCEO") == "1" else EF.REGLES_NO
            toks = [x for x in toks if x in pref] or toks
            marca_prova = toks[0] if toks else ""
            exer = f"prova: {c['tipus_prova']}"
        notes = [f"Traspàs de l'auditoria IA i de l'inventari antic ({c['font_traspas']}, {c['id_origen']}).",
                 f"Nivell {c['nivell_font'] or '?'}.", exer + "."]
        if c.get("data_document"):
            notes.append(f"Data del document: {c['data_document']}.")
        if c.get("url_arxivada"):
            notes.append(f"Captura coneguda: {c['url_arxivada']}.")
        if es_agregador(url):
            notes.append("agregador=true: còpia de l'informe de l'emissor en un agregador; cal substituir-la per la còpia de l'emissor si existeix.")
        if t["det"]:
            notes.append(t["det"] + ".")
        fila = {kk: "" for kk in rcap}
        fila.update({
            "tipus": "evidencia_ceo" if funcio == "ceo" else "evidencia_fundador",
            "grup_id": f"L{args.n}-{isin}", "isin": isin, "nom": r.get("nom_panell", ""),
            "anys": blocs(t["anys"]), "n_files": str(len(set(t["anys"]))),
            "origen": f"proposta_claude_lot{args.n}", "estat_certificacio": r.get("sim_estat_certificacio", ""),
            "cita_literal": cita, "url_font": url, "id_document_o_font": ident,
            "origen_cita": c["font_traspas"], "model_verificacio": t["model"], "marca_veritat": t["marca"],
            "notes": " ".join(notes), "allotjament": allotjament(url, c["nivell_font"]),
            "funcio_cita": funcio, "marca_prova": marca_prova,
        })
        noves.append(fila)
        per_isin[isin].append(fila)
    with REG.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rcap, lineterminator="\r\n" if crlf else "\n")
        w.writerows(noves)
    for isin, fs in per_isin.items():
        p = FITXES / f"{isin}.md"
        text = p.read_text(encoding="utf-8").rstrip("\n")
        L = [f"\n## Lot {args.n} · Traspàs de l'auditoria IA i de l'inventari antic\n"]
        for fl in fs:
            L.append(f"- **{fl['id_document_o_font']}** · {fl['anys']} · {fl['marca_veritat']} · `{fl['tipus']}` "
                     f"(`{fl['marca_prova']}`). «{fl['cita_literal']}» [Font original]({fl['url_font']}).")
        p.write_text(text + "\n" + "\n".join(L) + "\n", encoding="utf-8")
    pend = ROOT / "lots" / f"lot{args.n}_pendents.csv"
    with pend.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["isin", "any", "falta"])
        w.writerows([(k[0], k[1], fn) for k, fn in sorted(pendents)])
    print(f"Escrit: {len(noves)} entrades al registre, {len(per_isin)} fitxes, {pend.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extreu cites de CEO dels documents de l'exercici que ja coneixem (auditoria, inventari i registre).

Per a cada fila del lot que avui no compleix C1 (estat/estat_files.csv) i té FounderCEO 0 o 1:

  1. Documents candidats de l'ISIN: les URL de traspas/candidates_evidencia.csv (de qualsevol
     funció) i les `url_font` del registre, de nivell A o B i sense agregadors.
  2. Claude baixa cada document (mateixa memòria cau que traspas/importa_lot.py) i n'extreu el text.
  3. Exercici del document: l'any que més hi surt (2010-2027) ha de ser l'any de la fila. Si el
     document té molts anys partits («2019/20», «2019-20»), és d'un exercici no natural i no es fa
     servir (la fila es deixa per a la cerca manual).
  4. Hi busca un fragment curt que anomeni el CEO de la fila (cognom) i hi tingui a prop un títol
     de primer executiu (EF.CARRECS). Es descarten els fragments:
       - amb mots de sortida o de càrrec anterior (former, previously, until, resign…);
       - amb un títol adjunt (deputy, vice, stellvertretender, délégué, adjoint);
       - on el càrrec és «of/at/de/der» una altra entitat que no és l'empresa;
       - on davant el cognom hi ha un altre nom de pila (una altra persona amb el mateix cognom).
  5. El fragment és un tros literal del text del document; es comprova amb la mateixa funció
     verifica() de l'importador i entra com a [V].

Una mateixa cita (ISIN, URL, text) que serveix per a diversos anys és una sola entrada.
Per defecte és una prova en sec que escriu una mostra a --mostra (CSV) per revisar-la a mà.

  python3 traspas/extreu_ceo_documents.py lots/lot15.csv --lot 15 --cache DIR --mostra m.csv
  python3 traspas/extreu_ceo_documents.py lots/lot15.csv --lot 15 --cache DIR --escriu
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("importa_lot", ROOT / "traspas" / "importa_lot.py")
IL = importlib.util.module_from_spec(spec)
spec.loader.exec_module(IL)
EF = IL.EF

ANTERIOR = re.compile(r"previous|previously|prior to|before joining|formerly|former|until |from \d{4} (to|until)"
                      r"|between \d{4} and|\d{4}\s*-\s*\d{4}|zuvor|vorher|bis \d|anteriormente|auparavant|precedemment"
                      r"|ex-|ehemalig|tidigare|tidligere|aiemmin|in precedenza|voorheen|eerder")
ADJUNT = re.compile(r"deputy|vice[- ]|stellvertret|delegue|adjoint|adjunt|deputy chief|assistant|\bcoo\b|\bcfo\b(?! and)")
ALTRA = re.compile(r"(?:chief executive(?: officer)?|ceo|managing director|directeur general|director general"
                   r"|consejero delegado|amministratore delegato|vorstandsvorsitzender|administrador-delegado|presidente executivo"
                   r"|verkstallande direktor|vd)\s+(?:of|at|de|du|der|des|di|del|da|do|della|bei|chez|i|i\.)\s+"
                   r"((?:[\w&'.-]+\s+){0,3}[\w&'.-]+)")


def text_de(url: str) -> str:
    t = IL.text_cache(url)
    # els informes ESEF (XHTML) poden fer centenars de MB: un cop desat el text, no cal guardar l'original
    fn = IL.CACHE / hashlib.sha256(url.encode()).hexdigest()
    if fn.exists() and fn.stat().st_size > 5_000_000 and fn.read_bytes()[:4] not in (b"%PDF",) and fn.read_bytes()[:2] != b"PK":
        fn.unlink()
    return t


def exercici(t: str) -> tuple[int | None, bool]:
    return IL.any_dominant(t)


def tokens_empresa(nom_panell: str) -> list[str]:
    toks = [EF.norm(x).strip(".,()&'") for x in re.split(r"[\s/]+", nom_panell)]
    return [x for x in toks if len(x) >= 3 and x not in IL.GENERICS and not re.match(r"^[\d,.-]+$", x)][:3]


FUTUR = re.compile(r"will (be|become|take|assume|succeed|join|step|hand|remain)|\bfuture\b|designate|incoming|with effect from"
                   r"|effective (from|as of|on)|to become|shall (be|become)|as from|to succeed|will succeed|sera nomme"
                   r"|deviendra|prendra|succedera|wird .{0,40}(ubernehmen|nachfolgen)|sucedera|asumira")
ALTRES_ROLS = re.compile(r"\b(cfo|coo|cto|chair|chairman|member|director|officer|vorstand|e\.h|mitglied|secretary)\b")
TRACT = {"mr", "mrs", "ms", "dr", "prof", "herr", "frau", "m", "mme", "sir", "dame", "dott", "ing", "mag", "dipl"}


CURTS_OK = {"of", "de", "du", "da", "do", "di", "la", "le", "el", "et", "en", "i", "y", "e", "a", "&", "and", "och", "og", "og",
            "the", "to", "in", "on", "at", "by", "as", "is", "vd", "ceo", "co", "ag", "se", "sa", "nv", "bv", "plc", "mr", "ms", "dr",
            "m.", "-", "–", "•", "|", "(", ")", "der", "des", "den", "het", "van", "von", "zu", "af", "al", "il", "lo", "su"}


def trencament(w: str) -> float:
    """Proporció de «paraules» d'una o dues lletres que no són paraules curtes normals (text amb lletres separades)."""
    toks = re.findall(r"[^\s]+", w)
    if not toks:
        return 0.0
    curts = [t for t in toks if len(t.strip(".,;:()«»\"'")) <= 2 and t.lower().strip(".,;:()") not in CURTS_OK
             and not t.strip(".,;:()").isdigit()]
    return len(curts) / len(toks)


def nom_ok(nw: str, nom: str) -> bool:
    """Nom de pila + cognom, o tots els mots del cognom; un sol cognom curt no n'hi ha prou si n'hi ha més."""
    toks = [t for t in EF.tokens_nom(nom) if t]
    pila = EF.norm(nom.split()[0]) if nom.split() else ""
    hi = [t for t in toks if re.search(r"(?<![\w])" + re.escape(t) + r"(?![\w])", nw)]
    if not hi:
        return False
    if pila and re.search(r"(?<![\w])" + re.escape(pila) + r"(?![\w])", nw):
        return True
    return len(hi) == len(toks)


TITOLS_MOTS = {"Chief", "Executive", "Officer", "Group", "Managing", "Director", "President", "Board", "Chairman", "Chair",
               "The", "Company", "Vorstand", "Vorsitzender", "Directeur", "Général", "General", "Consejero", "Delegado",
               "Amministratore", "Delegato", "CEO", "Our", "Annual", "Report", "Executive,", "Officer,"}


def altra_persona(entre: str, nom: str) -> bool:
    propis = {x.strip(".,()").lower() for x in re.split(r"[\s-]+", nom) if x}
    for m in re.finditer(r"\b([A-ZÀ-Þ][a-zà-ÿ'’-]+|[A-ZÀ-Þ]{2,})\s+([A-ZÀ-Þ][a-zà-ÿ'’-]+|[A-ZÀ-Þ]{2,})\b", entre):
        a, b = m.group(1), m.group(2)
        if a in TITOLS_MOTS or b in TITOLS_MOTS:
            continue
        if a.lower() in propis or b.lower() in propis:
            continue
        return True
    return False


def fragments(t: str, nom: str, nom_panell: str) -> list[tuple[tuple, str]]:
    """Fragments curts (nom + títol, ampliats a la frase si és curta), amb puntuació (més alta, millor)."""
    tt = re.sub(r"\s+", " ", t)
    nf, mapa = IL.norm_mapa(tt)
    toks = [x for x in EF.tokens_nom(nom) if x]
    paraules_nom = set(EF.norm(nom).replace("-", " ").split()) | set(EF.norm(nom).split())
    emp = tokens_empresa(nom_panell)
    vistos, out = set(), []
    for tok in toks:
        for m in re.finditer(r"(?<![\w])" + re.escape(tok) + r"(?![\w])", nf):
            s, e = m.start(), m.end()
            # amplia el nom amb les paraules del nom complet i el tractament que hi ha just abans o després
            for _ in range(4):  # cap a l'esquerra: nom de pila, partícules, tractament
                mm = re.search(r"([\w'-]+)\.?\s$", nf[max(0, s - 30):s])
                if not mm or not (mm.group(1) in paraules_nom or mm.group(1) in TRACT):
                    break
                s = max(0, s - 30) + mm.start()
            for _ in range(3):  # cap a la dreta: la resta del cognom
                mm = re.match(r"\s([\w'-]+)", nf[e:e + 30])
                if not mm or mm.group(1) not in paraules_nom:
                    break
                e += mm.end()
            zona_a, zona_b = max(0, s - 90), min(len(nf), e + 90)
            ks = [k for k in EF.CARRECS.finditer(nf, zona_a, zona_b)]
            if not ks:
                continue
            k = min(ks, key=lambda k: (k.start() - e) if k.start() >= e else (s - k.end()) + 10)
            gap = (k.start() - e) if k.start() >= e else (s - k.end())
            if gap > 80:
                continue
            a, b = min(s, k.start()), max(e, k.end())
            # amplia a la frase si en queda poc per l'esquerra o per la dreta
            ini = max(nf.rfind(". ", 0, a), nf.rfind("; ", 0, a))
            if ini >= 0 and a - ini <= 60:
                a = ini + 2
            while a > 0 and nf[a - 1].isalnum():
                a -= 1
            while b < len(nf) and nf[b].isalnum():
                b += 1
            if nf[b:b + 1] == ")":
                b += 1
            fi = nf.find(". ", b)
            if 0 <= fi and fi - b <= 60 and not ALTRES_ROLS.search(nf[b:fi]):
                b = fi + 1
            w = tt[mapa[a]:mapa[b - 1] + 1].strip(" ,;:-–•*")
            if not w or w in vistos or len(w) > 320 or len(w) < 8:
                continue
            vistos.add(w)
            nw = EF.norm(w)
            if not EF.anomena(nw, nom) or not nom_ok(nw, nom) or not EF.CARRECS.search(nw):
                continue
            # el cognom ha de sortir com a nom propi (majúscula), no com a paraula comuna («does», «young»…)
            cognoms = [x for x in re.split(r"[\s-]+", nom)[1:] if len(x) >= 3 and EF.norm(x) not in EF.PARTICULES]
            if cognoms and not any(re.search(r"(?<![\w])(" + re.escape(x) + "|" + re.escape(x.upper()) + r")(?![\w])", w)
                                   for x in cognoms):
                continue
            if re.search(r"\b\d{1,3}[,.]\d{3}\b|\d\s?%", w):
                continue  # taules (accions, percentatges)
            # entre el nom i el títol no hi pot haver el nom d'una altra persona
            if k.start() >= e:
                entre = tt[mapa[min(e, len(mapa) - 1)]:mapa[min(k.start(), len(mapa) - 1)]]
            else:
                entre = tt[mapa[min(k.end(), len(mapa) - 1)]:mapa[min(s, len(mapa) - 1)]]
            if altra_persona(entre, nom):
                continue
            if IL.SORTIDA.search(nw) or ANTERIOR.search(nw) or FUTUR.search(nw) or IL.persona_conflictiva(w, [nom]):
                continue
            if any(ADJUNT.search(nw[max(0, kk.start() - 25):kk.end() + 25]) for kk in EF.CARRECS.finditer(nw)):
                continue
            altra = False
            for kk in ALTRA.finditer(nw):
                desti = kk.group(1)
                if not (IL.AUTOREF.search(desti) or any(x in desti for x in emp)):
                    altra = True
            if altra:
                continue
            w = re.sub(r"\s+\d{1,2}\.?$", "", w)
            pila = EF.norm(nom.split()[0]) if nom.split() else ""
            trencat = trencament(w)
            if trencat > 0.3:
                continue  # text amb les lletres separades: massa risc de llegir malament el càrrec
            out.append(((bool(pila) and pila in nw, -round(trencat, 1), -gap, -len(w)), w))
    out.sort(reverse=True)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("lot")
    ap.add_argument("--lot", dest="n", required=True)
    ap.add_argument("--cache", required=True)
    ap.add_argument("--escriu", action="store_true")
    ap.add_argument("--mostra", default="", help="CSV amb totes les cites proposades, per revisar-les")
    ap.add_argument("--max-docs", type=int, default=12, help="màxim de documents per fila")
    ap.add_argument("--totes", action="store_true", help="també les files que ja compleixen C1 (p. ex. per substituir "
                    "una cita d'un altre exercici per una de l'exercici; lot 27)")
    ap.add_argument("--docs", default="", help="CSV isin,any,url,nivell,font,exercici amb els documents de cada fila "
                    "(p. ex. informes ESEF de l'exercici trobats per traspas/troba_esef.py); si s'indica, només es fan servir aquests")
    args = ap.parse_args()
    IL.CACHE = Path(args.cache)

    with IL.BASE.open(encoding="utf-8", newline="") as f:
        base = {(r["isin"], r["any"]): r for r in csv.DictReader(f)}
    with IL.ESTAT.open(encoding="utf-8", newline="") as f:
        estat = {(r["isin"], r["any"]): r for r in csv.DictReader(f)}
    with (ROOT / args.lot).open(encoding="utf-8", newline="") as f:
        lot = [(r["isin"], r["any"]) for r in csv.DictReader(f)]
    isins = {k[0] for k in lot}

    docs = collections.defaultdict(dict)  # isin -> url -> info
    with IL.CANDS.open(encoding="utf-8", newline="") as f:
        for c in csv.DictReader(f):
            if c["isin"] in isins and c["url"].startswith("http") and c["nivell_font"] in ("A", "B") and not IL.es_agregador(c["url"]):
                d = docs[c["isin"]].setdefault(c["url"], {"nivell": c["nivell_font"], "font": c["font_traspas"], "dates": set()})
                y = IL.any_doc(c)
                if y:
                    d["dates"].add(y)
    with IL.REG.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            u = r.get("url_font") or ""
            if r["isin"] in isins and u.startswith("http") and not IL.es_agregador(u) and r.get("allotjament") != "mitja":
                docs[r["isin"]].setdefault(u, {"nivell": "A", "font": "registre", "dates": set()})

    docs_fila = collections.defaultdict(list)
    if args.docs:
        with open(args.docs, encoding="utf-8", newline="") as f:
            for d in csv.DictReader(f):
                docs_fila[(d["isin"], d["any"])].append((d["url"], {"nivell": d["nivell"], "font": d["font"],
                                                                    "dates": set(), "exercici": d["exercici"]}))
    tries: dict[tuple, dict] = {}
    res = collections.Counter()
    pendents = []
    mostra = []
    for k in lot:
        r, e = base[k], estat[k]
        if (not args.totes and "falta_ceo" not in e["estat"].split("+")) or r["FounderCEO"] not in ("0", "1"):
            res["fila_ja_coberta_o_fora"] += 1
            continue
        any_fila = int(k[1])
        noms = [n.strip() for n in (r.get("ceos") or "").split("|") if n.strip()]
        if not noms:
            res["sense_ceo_a_la_base"] += 1
            pendents.append((k, "sense_ceo"))
            continue
        # primer els documents datats a l'any de la fila o el següent; després la resta
        cands = sorted(docs.get(k[0], {}).items(),
                       key=lambda x: (not (x[1]["dates"] & {any_fila, any_fila + 1}), bool(x[1]["dates"]) and not (x[1]["dates"] & {any_fila - 1, any_fila, any_fila + 1, any_fila + 2})))
        if args.docs:
            cands = docs_fila.get(k, [])
        trobats = {}
        provats = 0
        for url, info in cands:
            if len(trobats) == len(noms) or provats >= args.max_docs:
                break
            if info["dates"] and not (info["dates"] & {any_fila - 1, any_fila, any_fila + 1, any_fila + 2}):
                continue
            provats += 1
            t = text_de(url)
            if len(t) < 1500:
                continue
            if not info.get("exercici"):
                # sense metadades de l'exercici: només informes llargs i any dominant = any de la fila
                fy, partit = exercici(t)
                if len(t) < 150_000 or fy != any_fila or partit:
                    continue
            for nom in noms:
                if nom in trobats:
                    continue
                fr = fragments(t, nom, r.get("nom_panell") or "")
                for _, w in fr[:3]:
                    est, det = IL.verifica(url, w)
                    if est == "trobada":
                        trobats[nom] = (url, info, w, det)
                        break
        if len(trobats) == len(noms):
            for nom, (url, info, w, det) in trobats.items():
                t_ = tries.setdefault((k[0], url, w), {"anys": [], "info": info, "det": det, "noms": set()})
                t_["anys"].append(any_fila)
                t_["noms"].add(nom)
                mostra.append({"isin": k[0], "any": k[1], "ceo": nom, "url": url, "cita": w})
            res["fila_coberta"] += 1
        else:
            res["fila_sense_cita"] += 1
            pendents.append((k, "ceo"))

    print(f"Lot {args.n}: {len(lot)} files.")
    for kk, v in sorted(res.items()):
        print(f"  {kk}: {v}")
    print(f"Entrades noves (agrupades per cita): {len(tries)}")
    if args.mostra:
        with open(args.mostra, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["isin", "any", "ceo", "url", "cita"])
            w.writeheader()
            w.writerows(mostra)
    with (ROOT / "lots" / f"lot{args.n}_pendents.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["isin", "any", "falta"])
        for (isin, a), q in sorted(pendents):
            w.writerow([isin, a, q])
    if not args.escriu:
        print("Prova en sec: no s'ha escrit res al registre ni a les fitxes.")
        return 0

    with IL.REG.open(encoding="utf-8", newline="") as f:
        rcap = next(csv.reader(f))
    crlf = b"\r\n" in IL.REG.read_bytes()[:4000]
    comptador = collections.Counter()
    noves, per_isin = [], collections.defaultdict(list)
    for (isin, url, cita), t_ in sorted(tries.items(), key=lambda x: (x[0][0], min(x[1]["anys"]), x[0][1])):
        comptador[isin] += 1
        ident = f"L{args.n}-{isin}-C{comptador[isin]:02d}"
        r = base[(isin, str(min(t_["anys"])))]
        marques = r.get("marques") or ""
        marca_prova = "R2" if "interi" in marques else ("R3" if "ceo_president_exec" in marques or "de_facto" in marques else "R1")
        nc = EF.norm(cita)
        if marca_prova == "R1" and re.search(r"executive chair", nc) and not re.search(
                r"\bceo\b|chief executive|directeur general|director general|consejero delegado|amministratore delegato|vorstand", nc):
            marca_prova = "R3"
        ex = t_["info"].get("exercici")
        origen_doc = ((f"informe anual de l'exercici tancat el {ex} (ESEF, metadades del dipòsit oficial)"
                       if t_["info"].get("font") == "esef_filings.xbrl.org" else
                       f"informe anual de l'exercici tancat el {ex} (FCA NSM; data de tancament llegida a l'informe)") if ex else
                      f"any dominant del document; el document ja era a l'auditoria o al registre ({t_['info']['font']})")
        notes = (f"Frase extreta per script del document original de l'exercici {', '.join(str(a) for a in sorted(set(t_['anys'])))} "
                 f"({origen_doc}). "
                 f"Nivell {t_['info']['nivell']}. Cita literal comprovada al document baixat: {t_['det']}.")
        fila = {kk: "" for kk in rcap}
        fila.update({
            "tipus": "evidencia_ceo", "grup_id": f"L{args.n}-{isin}", "isin": isin, "nom": r.get("nom_panell", ""),
            "anys": IL.blocs(t_["anys"]), "n_files": str(len(set(t_["anys"]))),
            "origen": f"proposta_claude_lot{args.n}", "estat_certificacio": r.get("sim_estat_certificacio", ""),
            "cita_literal": cita, "url_font": url, "id_document_o_font": ident,
            "origen_cita": "extret_per_claude", "model_verificacio":
                "Claude (script traspas/extreu_ceo_documents.py, 23/11/2026: frase literal del document original baixat)",
            "marca_veritat": "[V]", "notes": notes, "allotjament": IL.allotjament(url, t_["info"]["nivell"]),
            "funcio_cita": "ceo", "marca_prova": marca_prova,
        })
        noves.append(fila)
        per_isin[isin].append(fila)
    with IL.REG.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rcap, lineterminator="\r\n" if crlf else "\n")
        w.writerows(noves)
    for isin, fs in per_isin.items():
        p = IL.FITXES / f"{isin}.md"
        text = p.read_text(encoding="utf-8").rstrip("\n")
        L = [f"\n## Lot {args.n} · Cites de CEO extretes dels documents de l'exercici\n"]
        for fl in fs:
            L.append(f"- **{fl['id_document_o_font']}** · {fl['anys']} · {fl['marca_veritat']} · `evidencia_ceo` "
                     f"(`{fl['marca_prova']}`). «{fl['cita_literal']}» [Font original]({fl['url_font']}).")
        p.write_text(text + "\n" + "\n".join(L) + "\n", encoding="utf-8")
    print(f"Escrit: {len(noves)} entrades i {len(per_isin)} fitxes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

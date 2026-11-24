#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica i importa al registre la fitxa de fundació de cada empresa (files P).

Decisió de Jordi del 24/11/2026 (CLAUDE.md): un 0 necessita la prova completa, per parts. Si hi ha
evidència de qui va fundar l'empresa (llista de fundadors) i el CEO no hi és, la prova a és completa.
Si l'empresa la va crear l'Estat o una altra empresa, ho és la prova e. L'any de fundació és la part
d'empresa de les proves b, c i d.

Entrades (de la cerca):
  - cites: isin, part, entitat, fundadors, any_fundacio, url, data_document, tipus_document, pagina,
    cita_literal, nivell, notes; `part` és llista_fundadors | origen_entitat | any_fundacio | cadena;
  - resum per empresa: isin, entitat_rellevant, tipus_origen, fundadors, any_fundacio, singular,
    ceo_entre_fundadors, dubte, notes.

Per a cada cita:
  1. comprovació de contingut segons la part:
     - llista: anomena algun dels fundadors, té un mot de fundació i no anomena cap CEO P de l'empresa;
     - origen: diu que la va crear l'Estat, una llei o una altra empresa;
     - any: té un any i un verb de fundació;
  2. Claude torna a baixar el document i hi busca la cita literal (o, si la re-descàrrega falla, al
     fitxer baixat per la cerca);
  3. l'entrada s'aplica a tots els anys de l'ISIN amb FounderCEO=0 on cap CEO no és entre els fundadors.
Marques: `llista_exhaustiva=implicita;a_fundador_unic` (P8) si l'atribució és en singular; `fundacio_no_nova`
si la cerca hi aplica la P1. Les empreses amb un CEO entre els fundadors, sense fitxa o amb dubte de
criteri van a `lots/lot{N}_dubtes.csv`. Cap canvi de FounderCEO ni de `regles`.

  python3 traspas/importa_fitxa_fundacio.py --lot 18 --cites C.csv --resum R.csv --descarregues DIR [--escriu]
"""
from __future__ import annotations

import argparse
import collections
import csv
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("importa_cerca", ROOT / "traspas" / "importa_cerca.py")
IC = importlib.util.module_from_spec(spec)
spec.loader.exec_module(IC)
IL, EF = IC.IL, IC.EF

ORIGEN = re.compile(IL.CONTINGUT["origen_entitat"].pattern
                    + r"|(state|government|crown|ministry|parliament|law|act of|decree|royal charter|municipal|city of|federal"
                    r"|bank of|banks|companies|savings banks|cooperative|co-operative|staat|etat|estado|stato|statens|valtion"
                    r"|regering|bund\b|land\b|cantons?|kanton)")
PARTS = {"llista_fundadors": "a", "origen_entitat": "e"}
# Verbs i expressions de fundació per a cites d'empresa (més amples que les de les biografies de CEO)
FUND = re.compile(IL.FUND_VERB + r"|founder|foundation|formed|form(ed)? the company|started|began|set up|launched|costituit"
                  r"|per iniziativa di|on the initiative of|a l'initiative de|grunnlagt|grundlagd|grundades|grundet|perustettiin"
                  r"|perustett|perustam|zalozon|powstal|oprichter|opgericht|fundou|criad[ao]|nata|nato|creat|formation|opens|opened"
                  r"|open(ed|s)? (his|her|a|the) (business|company|shop|firm)|begins|gründung|grundung|naci[oó]|nacque|nasce")
ORIGEN_E = re.compile(ORIGEN.pattern + r"|statlig|statens|staatlich|statale|estatal|publique|public sector|side business"
                      r"|division of|unit of|business unit|part of the|subsidiary|subsiduary|spun|spin|carved|demerged|joint venture"
                      r"|gemeinschaftsunternehm|coentreprise|empresa conjunta|caisse des depots|beteiligten sich|a partir de")


def files_p(base: list[dict]) -> dict[str, list[dict]]:
    out = collections.defaultdict(list)
    for r in base:
        if r["FounderCEO"] == "0":
            out[r["isin"]].append(r)
    return out


def noms_ceo(rs: list[dict]) -> list[str]:
    return sorted({n.strip() for r in rs for n in (r.get("ceos") or "").split("|") if n.strip()})


def comprova(part: str, cita: str, fundadors: list[str], ceos: list[str]) -> str:
    """'' si la cita aporta la part; si no, el motiu."""
    n = EF.norm(cita)
    if part == "llista_fundadors":
        if not any(EF.anomena(n, f) for f in fundadors):
            return "la cita no anomena cap dels fundadors indicats"
        if not (IL.FUNDACIO.search(IL.EXCLOU_P6.sub(" ", n)) or FUND.search(n)):
            return "sense mot de fundació"
        for c in ceos:
            pila = EF.norm(c.split()[0]) if c.split() else ""
            if EF.norm(c) in n or (EF.anomena(n, c) and pila and re.search(r"(?<![\w])" + re.escape(pila) + r"(?![\w])", n)):
                return "la cita anomena un CEO de l'empresa"
        return ""
    if part == "origen_entitat":
        if re.search(r"\bmerg|joined forces|fusion|fusio|combination", n) and not re.search(r"state|statlig|government|staat|etat|estado", n):
            return "fusió: és un cas de D1 (regla 26), no de prova e"
        return "" if ORIGEN_E.search(n) and (IL.FUNDACIO.search(n) or FUND.search(n)) else "la cita no diu qui la va crear"
    if part == "any_fundacio":
        return "" if (IL.CONTINGUT["any_fundacio"].search(n) or (FUND.search(n) and re.search(IL.ANY_HIST, n))) else "sense any i verb de fundació"
    if part == "cadena":
        return ""
    return f"part desconeguda: {part}"


LLISTA_OBERTA = re.compile(r"one of the (co-?)?founders|among (others|the founders)|\bco-?founders?\b|co-?fondateur"
                           r"|cofundador|mitgr[uü]nder|un des fondateurs|uno de los fundadores|tra i fondatori|en av grundarna",
                           re.I)


def any_de_la_cita(r: dict, entitat: str) -> str:
    """Any de fundació que la mateixa cita dona (camp any_fundacio de la cerca), si el text de la cita el conté."""
    m = re.search(r"\b(1[5-9]\d\d|20[0-2]\d)\b", r.get("any_fundacio") or "")
    if m and m.group(1) in (r.get("cita_literal") or ""):
        return f" [part any_fundacio={m.group(1)}; entitat={entitat}]"
    return ""


def etiqueta(r: dict, rm: dict) -> str:
    """Etiqueta estructurada [part …] per a estat/estat_files.py (valors de la fitxa verificada)."""
    entitat = "incert" if (rm.get("dubte") or "").strip() else "emissor"
    part = r["part"]
    if part == "llista_fundadors":
        noms = " + ".join(n.strip() for n in re.split(r"[|;]", r.get("fundadors") or rm.get("fundadors") or "") if n.strip())
        if not noms:
            return ""
        tancada = "no" if LLISTA_OBERTA.search(r.get("cita_literal") or "") else "si"
        return f"[part llista_fundadors={noms}; entitat={entitat}; tancada={tancada}]" + any_de_la_cita(r, entitat)
    if part == "origen_entitat":
        return f"[part origen_entitat={rm.get('tipus_origen') or 'corporatiu'}; entitat={entitat}]" + any_de_la_cita(r, entitat)
    if part == "any_fundacio":
        for y in re.findall(r"\b(1[5-9]\d\d|20[0-2]\d)\b", (r.get("any_fundacio") or "") + " " + (rm.get("any_fundacio") or "")):
            if y in (r.get("cita_literal") or ""):
                return f"[part any_fundacio={y}; entitat={entitat}]"
        return ""
    return ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lot", required=True)
    ap.add_argument("--cites", nargs="+", required=True)
    ap.add_argument("--resum", nargs="+", required=True)
    ap.add_argument("--descarregues", default="")
    ap.add_argument("--cache", default=str(ROOT / ".cache" / "baixades"))
    ap.add_argument("--escriu", action="store_true")
    args = ap.parse_args()
    IL.CACHE = Path(args.cache)
    desc = Path(args.descarregues) if args.descarregues else None

    with IL.BASE.open(encoding="utf-8", newline="") as f:
        base = list(csv.DictReader(f))
    P = files_p(base)
    resum = {}
    for p in args.resum:
        with open(p, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                resum[r["isin"].strip()] = r
    cites = collections.defaultdict(list)
    for p in args.cites:
        with open(p, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                r["_fitxer"] = Path(p).stem
                cites[r["isin"].strip()].append(r)

    acceptades, rebutjades, dubtes = [], [], []
    ver = {}
    for isin, rs in sorted(cites.items()):
        if isin not in P:
            rebutjades.append((isin, "", "sense files P"))
            continue
        rm = resum.get(isin, {})
        ceos = noms_ceo(P[isin])
        if (rm.get("ceo_entre_fundadors") or "").strip().lower() == "si":
            dubtes.append({"isin": isin, "motiu": "un CEO és entre els fundadors (contradiu el 0)", "notes": rm.get("notes", "")})
            continue
        if (rm.get("dubte") or "").strip():
            dubtes.append({"isin": isin, "motiu": f"dubte de criteri: {rm['dubte']}", "notes": rm.get("notes", "")})
        for r in rs:
            part = (r.get("part") or "").strip()
            cita = re.sub(r"\s+", " ", r.get("cita_literal") or "").strip()
            url = (r.get("url") or "").strip()
            if not cita or not url.startswith("http"):
                rebutjades.append((isin, part, "sense cita o URL"))
                continue
            fundadors = [x.strip() for x in (r.get("fundadors") or rm.get("fundadors") or "").split("|") if x.strip()]
            motiu = comprova(part, cita, fundadors, ceos)
            if motiu:
                rebutjades.append((isin, part, motiu))
                continue
            clau = (url, cita)
            if clau not in ver:
                est, det = IL.verifica(url, cita)
                if est == "trobada":
                    ver[clau] = ("[V]", "Claude (re-descàrrega del document original i cerca literal)", "")
                elif IC.a_local(desc / r["_fitxer"].replace("_cites", "") if desc else None, url, cita):
                    ver[clau] = ("[V]", "Claude (cita literal comprovada al fitxer baixat per la cerca)",
                                 f"La re-descàrrega no l'ha pogut confirmar ({est}: {det}); la cita és al fitxer baixat de la mateixa URL durant la cerca.")
                elif est == "no_trobada":
                    ver[clau] = ("[NV]", "Claude", f"no_valida: la cita no s'ha trobat al document tornat a baixar ({det}) ni al fitxer de la cerca.")
                else:
                    ver[clau] = ("[NV]", "Claude", f"pendent_arxiu: re-descàrrega {est} ({det}).")
            acceptades.append({**r, "part": part, "cita_literal": cita, "url": url})

    perempresa = collections.defaultdict(set)
    for r in acceptades:
        if ver[(r["url"], r["cita_literal"])][0] == "[V]":
            perempresa[r["isin"]].add(r["part"])
    tanca = {i for i, ps in perempresa.items() if ps & {"llista_fundadors", "origen_entitat"}}
    print(f"Empreses: {len(cites)}; cites acceptades: {len(acceptades)} "
          f"{dict(collections.Counter(ver[(r['url'], r['cita_literal'])][0] for r in acceptades))}; "
          f"empreses amb prova a o e [V]: {len(tanca)}; files P cobertes per a/e: {sum(len(P[i]) for i in tanca)}; "
          f"amb any de fundació [V]: {sum(1 for ps in perempresa.values() if 'any_fundacio' in ps or 'llista_fundadors' in ps)}; "
          f"dubtes: {len(dubtes)}; rebutjades: {len(rebutjades)}")
    for x in rebutjades:
        print("  rebutjada", x)
    for d in dubtes:
        print("  dubte", d["isin"], d["motiu"][:120])
    if not args.escriu:
        print("Prova en sec: no s'ha escrit res.")
        return 0

    with IL.REG.open(encoding="utf-8", newline="") as f:
        rcap = next(csv.reader(f))
    crlf = b"\r\n" in IL.REG.read_bytes()[:4000]
    comptador = collections.Counter()
    noves, per_fitxa = [], collections.defaultdict(list)
    for r in sorted(acceptades, key=lambda r: (r["isin"], r["part"], r["url"])):
        isin = r["isin"]
        if isin in {d["isin"] for d in dubtes if "contradiu" in d["motiu"]}:
            continue
        rm = resum.get(isin, {})
        anys = sorted(int(b["any"]) for b in P[isin])
        b0 = P[isin][0]
        v = ver[(r["url"], r["cita_literal"])]
        if r["part"] in PARTS:
            marca = PARTS[r["part"]]
        else:
            regles = collections.Counter(t for b in P[isin] for t in (b.get("regles") or "").replace("|", ";").split(";")
                                         if t in ("b", "c_AAF64_reserva", "d"))
            marca = regles.most_common(1)[0][0] if regles else "b"
        marques = []
        if r["part"] == "llista_fundadors" and (rm.get("singular") or "").strip().lower() == "si":
            marques += ["llista_exhaustiva=implicita", "a_fundador_unic"]
        if re.search(r"\bP1\b|holding|redomicil|fundacio_no_nova", (rm.get("dubte") or "") + " " + (rm.get("notes") or ""), re.I):
            marques.append("fundacio_no_nova")
        comptador[isin] += 1
        ident = f"L{args.lot}-{isin}-F{comptador[isin]:02d}"
        notes = [f"Fitxa de fundació per empresa (decisió de Jordi del 24/11/2026). Part de la prova {marca}: {r['part']}.",
                 f"Entitat: {r.get('entitat') or rm.get('entitat_rellevant') or '?'}; origen: {rm.get('tipus_origen') or '?'}; "
                 f"fundadors: {r.get('fundadors') or rm.get('fundadors') or '-'}; any de fundació: {r.get('any_fundacio') or rm.get('any_fundacio') or '-'}.",
                 f"Document: {r.get('tipus_document') or '?'}, {r.get('data_document') or 'sense data'}, pàgina {r.get('pagina') or '?'}. Nivell {r.get('nivell') or '?'}.",
                 "S'aplica a tots els anys amb FounderCEO=0 de l'ISIN: cap dels CEO no surt entre els fundadors."]
        if rm.get("notes"):
            notes.append("Raonament de la cerca: " + re.sub(r"\s+", " ", rm["notes"])[:400])
        if v[2]:
            notes.append(v[2])
        etiq = etiqueta(r, rm)
        if etiq:
            notes.append(etiq)
        fila = {kk: "" for kk in rcap}
        fila.update({
            "tipus": "evidencia_fundador" if r["part"] != "cadena" else "evidencia_context",
            "grup_id": f"L{args.lot}-{isin}", "isin": isin, "nom": b0.get("nom_panell", ""),
            "anys": IL.blocs(anys), "n_files": str(len(anys)), "origen": f"proposta_claude_lot{args.lot}",
            "estat_certificacio": b0.get("sim_estat_certificacio", ""), "cita_literal": r["cita_literal"], "url_font": r["url"],
            "id_document_o_font": ident, "origen_cita": "cerca_nova", "model_verificacio": v[1], "marca_veritat": v[0],
            "notes": " ".join(notes), "allotjament": IL.allotjament(r["url"], (r.get("nivell") or "A").strip()),
            "funcio_cita": "fundador" if r["part"] != "cadena" else "context",
            "marca_prova": marca if r["part"] != "cadena" else "", "marques_fundador": ";".join(marques),
        })
        noves.append(fila)
        per_fitxa[isin].append(fila)
    with IL.REG.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rcap, lineterminator="\r\n" if crlf else "\n")
        w.writerows(noves)
    for isin, fs in per_fitxa.items():
        p = IL.FITXES / f"{isin}.md"
        text = p.read_text(encoding="utf-8").rstrip("\n")
        rm = resum.get(isin, {})
        L = [f"\n## Lot {args.lot} · Fitxa de fundació\n",
             f"Entitat rellevant: {rm.get('entitat_rellevant') or '?'} · origen: {rm.get('tipus_origen') or '?'} · "
             f"fundadors: {rm.get('fundadors') or '-'} · any: {rm.get('any_fundacio') or '-'}.\n"]
        for fl in fs:
            L.append(f"- **{fl['id_document_o_font']}** · {fl['marca_veritat']} · `{fl['marca_prova'] or 'context'}`. "
                     f"«{fl['cita_literal']}» [Font original]({fl['url_font']}).")
        p.write_text(text + "\n" + "\n".join(L) + "\n", encoding="utf-8")
    with (ROOT / "lots" / f"lot{args.lot}_dubtes.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["isin", "motiu", "notes"], extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        w.writerows(dubtes)
    print(f"Escrit: {len(noves)} entrades, {len(per_fitxa)} fitxes, lots/lot{args.lot}_dubtes.csv.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica i importa al registre entrades d'evidència d'origen divers (tancament de dubtes, cerques puntuals).

Entrada: un o més CSV amb, com a mínim, les columnes isin, anys, funcio_cita, marca_prova,
cita_literal i url (o url_font). Opcionals: part, persona, data_document, tipus_document,
pagina, nivell, allotjament, notes, id_origen i seccio.

Per a cada entrada:
  1. comprova que té cita i URL http(s), que la funció és ceo, fundador o context i que els anys
     són anys de l'ISIN a la base;
  2. per a una entrada de CEO, la cita ha d'anomenar un dels CEO de la base en algun dels anys;
  3. verificació de la cita:
     - si `id_origen` és una entrada [V] del registre amb la mateixa URL i la mateixa cita, l'entrada
       nova n'hereta la verificació (amb nota);
     - si no, Claude torna a baixar el document i hi busca la cita literal; si la re-descàrrega falla
       però la cita és al fitxer baixat per la cerca (`--descarregues`), també és [V] amb nota;
       si el document s'obre i la cita no hi és, [NV] `no_valida`; si no s'obre, [NV] `pendent_arxiu`.
Cap canvi de FounderCEO ni de `ceos`: els canvis de dades van a part, en un lot de correcció.

  python3 traspas/importa_entrades.py --lot 19 --origen tancaments ENTRADES.csv                 # en sec
  python3 traspas/importa_entrades.py --lot 19 --origen cerca_dubtes RESULTATS/*.csv --descarregues DIR --escriu
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

TIPUS = {"ceo": "evidencia_ceo", "fundador": "evidencia_fundador", "context": "evidencia_context", "revisio_font": "revisio_font"}
LLETRA = {"ceo": "C", "fundador": "F", "context": "X", "revisio_font": "R"}
MARQUES_CEO = {"R1", "R2", "R2b", "R3", "ceo_interval"}
MARQUES_FUND = {"a", "b", "c", "d", "e", "D37", "si_font_B", "cita_fundador"}


def anys_de(text: str) -> set[int]:
    out = set()
    for tros in re.split(r"[;,\s]+", text or ""):
        m = re.match(r"^(\d{4})(?:-(\d{4}))?$", tros)
        if m:
            a, b = int(m.group(1)), int(m.group(2) or m.group(1))
            out.update(range(a, b + 1))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("entrades", nargs="+")
    ap.add_argument("--lot", required=True)
    ap.add_argument("--origen", required=True, help="nom curt de l'origen (p. ex. tancaments, cerca_dubtes)")
    ap.add_argument("--data", default="24/11/2026")
    ap.add_argument("--escriu", action="store_true")
    ap.add_argument("--cache", default=str(ROOT / ".cache" / "baixades"))
    ap.add_argument("--descarregues", default="")
    args = ap.parse_args()
    IL.CACHE = Path(args.cache)
    desc_arrel = Path(args.descarregues) if args.descarregues else None

    with IL.BASE.open(encoding="utf-8", newline="") as f:
        base = list(csv.DictReader(f))
    per_isin = collections.defaultdict(dict)
    for r in base:
        per_isin[r["isin"]][int(r["any"])] = r
    with IL.REG.open(encoding="utf-8", newline="") as f:
        registre = list(csv.DictReader(f))
    per_id = {r["id_document_o_font"]: r for r in registre}
    ids_existents = set(per_id)

    acceptades, rebutjades = [], []
    for p in args.entrades:
        with open(p, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                r["_fitxer"] = Path(p).stem
                isin = (r.get("isin") or "").strip()
                funcio = (r.get("funcio_cita") or "").strip()
                cita = re.sub(r"\s+", " ", r.get("cita_literal") or "").strip()
                url = (r.get("url") or r.get("url_font") or "").strip()
                marca = (r.get("marca_prova") or "").strip()
                anys = sorted(anys_de(r.get("anys") or "") & set(per_isin.get(isin, {})))
                motiu = ""
                if funcio not in TIPUS:
                    motiu = f"funció desconeguda: {funcio!r}"
                elif not cita or not url.startswith("http"):
                    motiu = "sense cita o URL"
                elif IL.es_agregador(url):
                    motiu = "URL d'un agregador"
                elif not anys:
                    motiu = f"cap any de l'ISIN dins {r.get('anys')!r}"
                elif funcio in ("ceo", "revisio_font") and marca and marca not in MARQUES_CEO | MARQUES_FUND:
                    motiu = f"marca no admesa: {marca!r}"
                elif funcio == "ceo" and marca not in MARQUES_CEO:
                    motiu = f"marca de CEO no admesa: {marca!r}"
                elif funcio == "fundador" and marca not in MARQUES_FUND:
                    motiu = f"marca de fundador no admesa: {marca!r}"
                elif funcio == "ceo":
                    noms = {n for a in anys for n in (per_isin[isin][a]["ceos"] or "").split("|") if n}
                    if not any(EF.anomena(EF.norm(cita), n) for n in noms):
                        motiu = f"la cita no anomena cap CEO de la base ({'; '.join(sorted(noms))})"
                if motiu:
                    rebutjades.append((isin, r.get("anys"), funcio, motiu))
                    continue
                acceptades.append({**r, "isin": isin, "funcio_cita": funcio, "cita_literal": cita, "url": url,
                                   "marca_prova": marca, "_anys": anys})

    ver = {}
    for r in acceptades:
        clau = (r["url"], r["cita_literal"])
        if clau in ver:
            continue
        orig = per_id.get((r.get("id_origen") or "").strip())
        if orig and orig.get("marca_veritat") == "[V]" and (orig.get("url_font") or "").strip() == r["url"] \
                and re.sub(r"\s+", " ", orig.get("cita_literal") or "").strip() == r["cita_literal"] \
                and "no_valida" not in (orig.get("notes") or ""):
            ver[clau] = ("[V]", f"Claude (cita i URL idèntiques a l'entrada [V] {orig['id_document_o_font']}, {args.data})",
                         f"Hereta la verificació de {orig['id_document_o_font']}.")
            continue
        est, det = IL.verifica(r["url"], r["cita_literal"])
        if est == "trobada":
            ver[clau] = ("[V]", f"Claude (re-descàrrega del document original i cerca literal, {args.data})", "")
        elif IC.a_local(desc_arrel / r["_fitxer"].replace("_cites", "") if desc_arrel else None, r["url"], r["cita_literal"]):
            ver[clau] = ("[V]", f"Claude (cita literal comprovada al fitxer baixat per la cerca, {args.data})",
                         f"La re-descàrrega no l'ha pogut confirmar ({est}: {det}); la cita és al fitxer baixat de la mateixa URL durant la cerca.")
        elif est == "no_trobada":
            ver[clau] = ("[NV]", f"Claude ({args.data})",
                         f"no_valida: la cita no s'ha trobat literalment al document tornat a baixar ({det}) ni al fitxer de la cerca.")
        else:
            ver[clau] = ("[NV]", f"Claude ({args.data})", f"pendent_arxiu: re-descàrrega {est} ({det}).")

    c = collections.Counter(ver[(r["url"], r["cita_literal"])][0] for r in acceptades)
    print(f"Entrades acceptades: {len(acceptades)} {dict(c)}; rebutjades: {len(rebutjades)}")
    for x in rebutjades:
        print("  rebutjada", x)
    for r in acceptades:
        v = ver[(r["url"], r["cita_literal"])]
        if v[0] != "[V]":
            print("  ", v[0], r["isin"], r["funcio_cita"], r.get("anys"), v[2][:150])
    if not args.escriu:
        print("Prova en sec: no s'ha escrit res.")
        return 0

    with IL.REG.open(encoding="utf-8", newline="") as f:
        rcap = next(csv.reader(f))
    crlf = b"\r\n" in IL.REG.read_bytes()[:4000]
    noves, per_fitxa = [], collections.defaultdict(list)
    for r in sorted(acceptades, key=lambda r: (r["isin"], r["funcio_cita"], r["_anys"][0], r["url"])):
        isin, funcio = r["isin"], r["funcio_cita"]
        n = 1
        while f"L{args.lot}-{isin}-{LLETRA[funcio]}{n:02d}" in ids_existents:
            n += 1
        ident = f"L{args.lot}-{isin}-{LLETRA[funcio]}{n:02d}"
        ids_existents.add(ident)
        b0 = per_isin[isin][r["_anys"][0]]
        v = ver[(r["url"], r["cita_literal"])]
        nivell = (r.get("nivell") or "A").strip() or "A"
        notes = [f"Lot {args.lot} ({args.origen}, {args.data})."]
        if r.get("seccio"):
            notes.append(f"Dubte: {r['seccio']}.")
        if r.get("part"):
            notes.append(f"Part de la prova: {r['part']}.")
        if r.get("persona"):
            notes.append(f"Persona: {r['persona']}.")
        notes.append(f"Document: {r.get('tipus_document') or '?'}, {r.get('data_document') or 'sense data'}, "
                     f"pàgina {r.get('pagina') or '?'}. Nivell {nivell}.")
        if r.get("id_origen"):
            notes.append(f"Cita presa de {r['id_origen']}.")
        if r.get("notes"):
            notes.append("Nota: " + re.sub(r"\s+", " ", r["notes"])[:500])
        if v[2]:
            notes.append(v[2])
        marca = r["marca_prova"]
        marques = []
        if marca in ("si_font_B", "cita_fundador") or (funcio == "fundador" and nivell == "B" and marca == "D37"):
            marca, marques = "cita_fundador", ["si_font_B"]
        fila = {kk: "" for kk in rcap}
        fila.update({
            "tipus": TIPUS[funcio], "grup_id": f"L{args.lot}-{isin}", "isin": isin, "nom": b0.get("nom_panell", ""),
            "anys": IL.blocs(r["_anys"]), "n_files": str(len(r["_anys"])), "origen": f"proposta_claude_lot{args.lot}",
            "estat_certificacio": b0.get("sim_estat_certificacio", ""), "cita_literal": r["cita_literal"], "url_font": r["url"],
            "id_document_o_font": ident, "origen_cita": args.origen, "model_verificacio": v[1], "marca_veritat": v[0],
            "notes": " ".join(notes), "allotjament": (r.get("allotjament") or "").strip() or IL.allotjament(r["url"], nivell),
            "funcio_cita": funcio, "marca_prova": marca if funcio != "context" else "", "marques_fundador": ";".join(marques),
        })
        noves.append(fila)
        per_fitxa[isin].append(fila)
    with IL.REG.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rcap, lineterminator="\r\n" if crlf else "\n")
        w.writerows(noves)
    for isin, fs in per_fitxa.items():
        p = IL.FITXES / f"{isin}.md"
        text = p.read_text(encoding="utf-8").rstrip("\n")
        L = [f"\n## Lot {args.lot} · {args.origen}\n"]
        for fl in fs:
            L.append(f"- **{fl['id_document_o_font']}** · {fl['funcio_cita']} · {fl['anys']} · {fl['marca_veritat']} · "
                     f"`{fl['marca_prova'] or 'context'}`. «{fl['cita_literal']}» [Font original]({fl['url_font']}).")
        p.write_text(text + "\n" + "\n".join(L) + "\n", encoding="utf-8")
    print(f"Escrit: {len(noves)} entrades, {len(per_fitxa)} fitxes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

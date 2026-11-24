#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica i importa al registre els resultats d'una cerca nova de cites de fundador (files F).

Entrada: un o més CSV amb les columnes isin, anys, ceo, resultat, url, data_document,
tipus_document, pagina, cita_literal, nivell, entitat_fundada, notes. `resultat` és trobat,
contradiccio o no_trobat.

Per a cada cita trobada:
  1. ha d'anomenar el CEO i contenir un mot de fundació admès per la P6 (sense «founding CEO»,
     «founder-led», «founding shareholder», «founding member»…), sense un altre nom de pila davant
     el cognom;
  2. s'aplica a les files de l'ISIN, dins `anys`, on FounderCEO=1 i el CEO és la persona;
  3. Claude torna a baixar el document de la URL i hi busca la cita literal; si la re-descàrrega
     falla però la cita és al fitxer que va baixar la cerca (`--descarregues`), també és [V] amb nota.
Marca de prova: `D37` si la font és de nivell A; `cita_fundador` amb la marca `si_font_B` si és B.
Si l'entitat fundada no és la cotitzada (predecessora), l'entrada porta la nota i la fila va a dubtes:
la decisió (D1/D10, regla 26) és de Jordi. Les contradiccions i els no trobats també van a dubtes.
Cap canvi de FounderCEO ni de `ceos`.

  python3 traspas/importa_fundador.py --lot 16 RESULTATS/*.csv --descarregues DIR            # en sec
  python3 traspas/importa_fundador.py --lot 16 RESULTATS/*.csv --descarregues DIR --escriu
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


def anys_de(text: str) -> set[int]:
    out = set()
    for tros in re.split(r"[;,\s]+", text or ""):
        m = re.match(r"^(\d{4})(?:-(\d{4}))?$", tros)
        if m:
            a = int(m.group(1))
            b = int(m.group(2) or a)
            out.update(range(a, b + 1))
    return out


def es_cotitzada(entitat: str, nom_panell: str) -> bool:
    ne = EF.norm(entitat or "")
    if not ne:
        return True
    if re.search(r"name of the listed company|renamed", ne):
        return True  # la mateixa societat amb un altre nom
    if re.search(r"predecess|acquired|not the listed|via .{0,20}merger|merger of", ne):
        return False
    toks = [EF.norm(x).strip(".,()&'") for x in re.split(r"[\s/]+", nom_panell)]
    toks = [x for x in toks if len(x) >= 3 and x not in IL.GENERICS and not re.match(r"^[\d,.-]+$", x)][:2]
    return any(t in ne for t in toks)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("resultats", nargs="+")
    ap.add_argument("--lot", required=True)
    ap.add_argument("--escriu", action="store_true")
    ap.add_argument("--cache", default=str(ROOT / ".cache" / "baixades"))
    ap.add_argument("--descarregues", default="")
    args = ap.parse_args()
    IL.CACHE = Path(args.cache)
    desc_arrel = Path(args.descarregues) if args.descarregues else None

    with IL.BASE.open(encoding="utf-8", newline="") as f:
        base = list(csv.DictReader(f))
    per_isin = collections.defaultdict(list)
    for r in base:
        per_isin[r["isin"]].append(r)

    acceptades, dubtes, rebutjades = [], [], []
    for p in args.resultats:
        with open(p, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                r["_fitxer"] = Path(p).stem
                res = (r.get("resultat") or "").strip()
                isin = r["isin"].strip()
                if res != "trobat":
                    dubtes.append({**r, "motiu": res or "sense resultat"})
                    continue
                cita = re.sub(r"\s+", " ", r.get("cita_literal") or "").strip()
                url = (r.get("url") or "").strip()
                ceo = (r.get("ceo") or "").strip()
                nc = EF.norm(cita)
                if not cita or not url.startswith("http"):
                    rebutjades.append((isin, ceo, "sense cita o URL"))
                    continue
                if not EF.anomena(nc, ceo):
                    rebutjades.append((isin, ceo, "la cita no anomena el CEO"))
                    continue
                if not IL.FUNDACIO.search(IL.EXCLOU_P6.sub(" ", nc)):
                    rebutjades.append((isin, ceo, "sense mot de fundació admès per la P6"))
                    continue
                if IL.persona_conflictiva(cita, [ceo]):
                    rebutjades.append((isin, ceo, "el cognom va precedit d'un altre nom de pila"))
                    continue
                anys = anys_de(r.get("anys") or "")
                files = [b for b in per_isin.get(isin, []) if b["FounderCEO"] == "1" and int(b["any"]) in anys
                         and any(EF.norm(ceo) == EF.norm(n) or EF.anomena(EF.norm(n), ceo) for n in (b["ceos"] or "").split("|"))]
                if not files:
                    rebutjades.append((isin, ceo, f"cap fila F amb aquest CEO als anys {r.get('anys')}"))
                    continue
                predecessora = not es_cotitzada(r.get("entitat_fundada") or "", files[0]["nom_panell"])
                acceptades.append({**r, "cita_literal": cita, "url": url, "_files": files, "_predecessora": predecessora})
                if predecessora:
                    dubtes.append({**r, "motiu": f"entitat fundada: {r.get('entitat_fundada')} (no és la cotitzada; cal decidir si és predecessora, D1/D10 i regla 26)"})

    ver = {}
    for r in acceptades:
        clau = (r["url"], r["cita_literal"])
        if clau in ver:
            continue
        est, det = IL.verifica(r["url"], r["cita_literal"])
        if est == "trobada":
            ver[clau] = ("[V]", "Claude (re-descàrrega del document original i cerca literal, 23/11/2026)", "")
        elif IC.a_local(desc_arrel / r["_fitxer"].replace("fund_", "") if desc_arrel else None, r["url"], r["cita_literal"]):
            ver[clau] = ("[V]", "Claude (cita literal comprovada al fitxer baixat per la cerca, 23/11/2026)",
                         f"La re-descàrrega de Claude no ha pogut confirmar-la ({est}: {det}); la cita és al fitxer baixat de la mateixa URL durant la cerca.")
        else:
            ver[clau] = ("[NV]", "Claude (23/11/2026)", f"pendent_arxiu: re-descàrrega {est} ({det}).")

    c = collections.Counter(ver[(r["url"], r["cita_literal"])][0] for r in acceptades)
    files_v = {(b["isin"], b["any"]) for r in acceptades if ver[(r["url"], r["cita_literal"])][0] == "[V]" for b in r["_files"]}
    print(f"Cites acceptades: {len(acceptades)} {dict(c)}; files F cobertes amb [V]: {len(files_v)}; "
          f"dubtes: {len(dubtes)}; rebutjades: {len(rebutjades)}")
    for x in rebutjades:
        print("  rebutjada", x)
    for d in dubtes:
        print("  dubte", d["isin"], d.get("ceo"), d["motiu"][:140])
    if not args.escriu:
        print("Prova en sec: no s'ha escrit res.")
        return 0

    with IL.REG.open(encoding="utf-8", newline="") as f:
        rcap = next(csv.reader(f))
    crlf = b"\r\n" in IL.REG.read_bytes()[:4000]
    comptador = collections.Counter()
    noves, per_fitxa = [], collections.defaultdict(list)
    for r in sorted(acceptades, key=lambda r: (r["isin"], r["ceo"], r["url"])):
        isin = r["isin"]
        comptador[isin] += 1
        ident = f"L{args.lot}-{isin}-F{comptador[isin]:02d}"
        anys = sorted({int(b["any"]) for b in r["_files"]})
        b0 = r["_files"][0]
        v = ver[(r["url"], r["cita_literal"])]
        nivell = (r.get("nivell") or "A").strip()
        notes = [f"Cerca nova de la cita de fundador ({r['_fitxer']}, 23/11/2026).",
                 f"Document: {r.get('tipus_document') or '?'}, {r.get('data_document') or 'sense data'}, pàgina {r.get('pagina') or '?'}.",
                 f"Nivell {nivell}. Entitat fundada segons la cita: {r.get('entitat_fundada') or '?'}."]
        if r["_predecessora"]:
            notes.append("L'entitat fundada no és la cotitzada: cal decidir si és predecessora (D1/D10, regla 26); la fila queda en dubte.")
        if r.get("notes"):
            notes.append("Nota de la cerca: " + re.sub(r"\s+", " ", r["notes"])[:300])
        if v[2]:
            notes.append(v[2])
        fila = {kk: "" for kk in rcap}
        fila.update({
            "tipus": "evidencia_fundador", "grup_id": f"L{args.lot}-{isin}", "isin": isin, "nom": b0.get("nom_panell", ""),
            "anys": IL.blocs(anys), "n_files": str(len(anys)), "origen": f"proposta_claude_lot{args.lot}",
            "estat_certificacio": b0.get("sim_estat_certificacio", ""), "cita_literal": r["cita_literal"], "url_font": r["url"],
            "id_document_o_font": ident, "origen_cita": "cerca_nova", "model_verificacio": v[1], "marca_veritat": v[0],
            "notes": " ".join(notes), "allotjament": IL.allotjament(r["url"], nivell), "funcio_cita": "fundador",
            "marca_prova": "D37" if nivell == "A" else "cita_fundador",
            "marques_fundador": "" if nivell == "A" else "si_font_B",
        })
        noves.append(fila)
        per_fitxa[isin].append(fila)
    with IL.REG.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rcap, lineterminator="\r\n" if crlf else "\n")
        w.writerows(noves)
    for isin, fs in per_fitxa.items():
        p = IL.FITXES / f"{isin}.md"
        text = p.read_text(encoding="utf-8").rstrip("\n")
        L = [f"\n## Lot {args.lot} · Cerca nova de cites de fundador\n"]
        for fl in fs:
            L.append(f"- **{fl['id_document_o_font']}** · {fl['anys']} · {fl['marca_veritat']} · `{fl['marca_prova']}`. "
                     f"«{fl['cita_literal']}» [Font original]({fl['url_font']}).")
        p.write_text(text + "\n" + "\n".join(L) + "\n", encoding="utf-8")
    with (ROOT / "lots" / f"lot{args.lot}_dubtes.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["isin", "anys", "ceo", "motiu", "url", "cita_literal", "notes"], extrasaction="ignore",
                           lineterminator="\n")
        w.writeheader()
        w.writerows(dubtes)
    print(f"Escrit: {len(noves)} entrades, {len(per_fitxa)} fitxes, lots/lot{args.lot}_dubtes.csv.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

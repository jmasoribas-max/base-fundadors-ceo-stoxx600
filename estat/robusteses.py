#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Columnes de robustesa noves, calculades per script a partir de les marques de la base i de l'evidència
del registre (Claude, 25/11/2026). No toca `dades/`: escriu `estat/robusteses.csv` i `estat/ROBUSTESES.md`.
Les columnes es copiaran a la base en congelar-la (v1.0.0), amb el flux vigent.

Cada columna copia FounderCEO, llevat de les files que tenen el tret que tracta. Regles (CLAUDE.md, regles 25,
27 i 28 i decisions de Jordi del 24/11/2026):

- founderceo_rob_regla25_nd: les files la classificació de les quals depèn d'algun criteri de la regla 25,
  com a ND. Per a les files P amb la prova per parts, la dependència surt de `estat_files.py` (`c2_depen`):
  la fila en depèn si, per a algun CEO, totes les proves possibles en depenen. Per a la resta, de les marques
  de la base: fundacio_no_nova (P1/P2), e_matriu_personal (P3), si_font_B (P6), data_fundacio_conflicte (P7),
  llista_exhaustiva=implicita i a_fundador_unic (P8), i les files F de fundador d'escissió (P4; la columna
  existent `founderceo_rob_fundador_escissio_com_0` les posa a 0).
- founderceo_rob_r25_p1p2, _p3, _p4, _p6, _p7, _p8: el mateix, criteri per criteri.
- founderceo_rob_sense_interval (regla 28): les files amb el CEO acreditat només per interval, com a ND.
- founderceo_rob_conflicte_fonts (regla 27): el valor alternatiu de la font en conflicte (0 ↔ 1). Inclou
  Steinhoff 2016-2017, que la regla 25 marca com a conflicte_fonts (robustesa a 1).
- founderceo_rob_dues_fonts (Q6): les files F amb menys de dues fonts diferents (documents) amb una cita de
  fundador vàlida que anomena el CEO (de qualsevol any de l'ISIN), com a ND. Reprodueix el criteri de
  Villalonga i Amit (2006). Les files P no canvien.
- founderceo_rob_sense_gestio_externa (Q12): les empreses amb la marca gestio_externa, fora (`exclosa`).
- founderceo_rob_sense_titol_funcional (Q14): sense la persona amb el títol funcional de co-CEO. Si era l'únic
  CEO de la fila, NA_sense_ceo; a CD Projekt 2018-2021 l'1 és per Iwiński, el co-CEO funcional, i passa a 0
  (anàlisi de criteris, Q14: «4 files passen d'1 a 0»). La resta de files amb la marca són 0 i no canvien.
- founderceo_rob_c_com_nd: recalcul de la columna existent amb la dependència de la prova c de `c2_depen`.
- founderceo_rob_llista_predecessora_nd (PROPOSTA, pendent de Jordi): les files P tancades només amb la
  llista de fundadors d'una predecessora, com a ND (la llista pot no cobrir totes les parts d'una fusió).

  python3 estat/robusteses.py
"""
from __future__ import annotations

import collections
import csv
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("estat_files", ROOT / "estat" / "estat_files.py")
EF = importlib.util.module_from_spec(spec)
spec.loader.exec_module(EF)

ND = "no_determinat"
SORTIDA = ROOT / "estat" / "robusteses.csv"
INFORME = ROOT / "estat" / "ROBUSTESES.md"
# Decisions documentades sense marca a la base (regla 25, darrer paràgraf; v0.10.8)
CONFLICTE_DECIDIT = {("NL0011375019", "2016"): "1", ("NL0011375019", "2017"): "1"}
# Q14: files on l'1 es deu al co-CEO amb títol funcional (docs/ANALISI_CRITERIS_v2_20261124.md)
TITOL_FUNCIONAL_FUNDADOR = {("PLOPTTC00011", y) for y in ("2018", "2019", "2020", "2021")}

COLS = ["founderceo_rob_regla25_nd", "founderceo_rob_r25_p1p2", "founderceo_rob_r25_p3", "founderceo_rob_r25_p4",
        "founderceo_rob_r25_p6", "founderceo_rob_r25_p7", "founderceo_rob_r25_p8", "founderceo_rob_sense_interval",
        "founderceo_rob_conflicte_fonts", "founderceo_rob_dues_fonts", "founderceo_rob_sense_gestio_externa",
        "founderceo_rob_sense_titol_funcional", "founderceo_rob_c_com_nd", "founderceo_rob_llista_predecessora_nd"]


def main() -> int:
    files, _ = EF.calcula()
    estat = {(f["isin"], f["any"]): f for f in files}
    with EF.BASE.open(encoding="utf-8", newline="") as fh:
        base = list(csv.DictReader(fh))
    with EF.REG.open(encoding="utf-8", newline="") as fh:
        reg = [e for e in csv.DictReader(fh) if EF.valida(e)]
    per_id = {e.get("id_document_o_font"): e for e in reg}
    gestio_externa = {r["isin"] for r in base if "gestio_externa" in (r.get("marques") or "").split(";")}
    fund_isin = collections.defaultdict(list)
    for e in reg:
        if (e.get("funcio_cita") or "") == "fundador":
            fund_isin[(e.get("isin") or "").strip()].append(e)

    out = []
    for r in base:
        k = (r["isin"], r["any"])
        fc = r["FounderCEO"]
        m = set((r.get("marques") or "").split(";")) - {""}
        f = estat.get(k, {})
        dep = set((f.get("c2_depen") or "").split(";")) - {""}
        es_p_parts = fc == "0" and (f.get("c2_fundador") or "").startswith("ok_prova_")
        val = {}

        def nd_si(cond: bool) -> str:
            return ND if (cond and fc in ("0", "1")) else fc

        # Regla 25: per a les P amb prova per parts, la dependència de l'evidència; si no, les marques
        p1 = ("P1" in dep) if es_p_parts else ("fundacio_no_nova" in m)
        p3 = ("P3" in dep) if es_p_parts else ("e_matriu_personal" in m)
        p8 = ("P8" in dep) if es_p_parts else bool({"llista_exhaustiva=implicita", "a_fundador_unic"} & m)
        # P4: files F de fundador d'escissió (la columna existent les posa a 0)
        p4 = fc == "1" and r.get("founderceo_rob_fundador_escissio_com_0") == "0"
        p6 = "si_font_B" in m
        p7 = "data_fundacio_conflicte" in m
        r25 = (("regla25" in dep) if es_p_parts else (p1 or p3 or p8)) or p4 or p6 or p7
        val["founderceo_rob_regla25_nd"] = nd_si(r25)
        for col, c in (("p1p2", p1), ("p3", p3), ("p4", p4), ("p6", p6), ("p7", p7), ("p8", p8)):
            val[f"founderceo_rob_r25_{col}"] = nd_si(c)

        val["founderceo_rob_sense_interval"] = nd_si((f.get("c1_tipus") or "") == "interval")

        alt = {"0": "1", "1": "0"}.get(fc, fc)
        if k in CONFLICTE_DECIDIT:
            val["founderceo_rob_conflicte_fonts"] = CONFLICTE_DECIDIT[k]
        else:
            val["founderceo_rob_conflicte_fonts"] = alt if "conflicte_fonts" in m else fc

        if fc == "1":
            # Documents diferents amb una cita de fundador vàlida de l'ISIN que anomena algun CEO de la fila
            cognoms = [EF.norm(c.split()[-1]) for c in (r.get("ceos") or "").split("|") if c.strip()]
            docs = {(e.get("url_font") or "").strip() for e in fund_isin.get(r["isin"], [])
                    if any(cg and cg in EF.norm((e.get("cita_literal") or "") + " " + (e.get("notes") or "")) for cg in cognoms)}
            docs |= {(per_id[i].get("url_font") or "").strip() for i in (f.get("c2_ids") or "").split(";") if i in per_id}
            val["founderceo_rob_dues_fonts"] = fc if len(docs) >= 2 else ND
        else:
            val["founderceo_rob_dues_fonts"] = fc

        val["founderceo_rob_sense_gestio_externa"] = "exclosa" if r["isin"] in gestio_externa else fc

        if "co_ceo_titol_funcional" in m:
            if len([c for c in (r.get("ceos") or "").split("|") if c.strip()]) <= 1:
                val["founderceo_rob_sense_titol_funcional"] = "NA_sense_ceo"
            elif k in TITOL_FUNCIONAL_FUNDADOR:
                val["founderceo_rob_sense_titol_funcional"] = "0"
            else:
                val["founderceo_rob_sense_titol_funcional"] = fc
        else:
            val["founderceo_rob_sense_titol_funcional"] = fc

        val["founderceo_rob_c_com_nd"] = nd_si(("c" in dep) if es_p_parts else (r.get("founderceo_rob_c_com_nd") == ND))
        val["founderceo_rob_llista_predecessora_nd"] = nd_si(es_p_parts and "llista_predecessora" in dep)

        out.append({"isin": r["isin"], "any": r["any"], "FounderCEO": fc,
                    "a_mostra_principal": r.get("a_mostra_principal", ""), **val})

    with SORTIDA.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["isin", "any", "FounderCEO", "a_mostra_principal"] + COLS, lineterminator="\r\n")
        w.writeheader()
        w.writerows(out)

    # Informe: per a cada columna, F i P dins la mostra principal i quantes files canvien
    mostra = [o for o in out if o["a_mostra_principal"] == "1"]
    f0 = sum(o["FounderCEO"] == "1" for o in mostra)
    L = ["# Robusteses calculades per script", "",
         "Generat per `estat/robusteses.py` a partir de la base, del registre i de `estat/estat_files.py`. "
         "No toca `dades/`: les columnes es copiaran a la base en congelar-la. "
         "Les regles de cada columna són a la capçalera de l'script.", "",
         f"Mostra principal (`a_mostra_principal`=1): {len(mostra):,} files, {f0} F ({100 * f0 / len(mostra):.2f} %).".replace(",", "."), "",
         "| Columna | Files que canvien (tota la base) | F a la mostra | P a la mostra | ND a la mostra | Altres a la mostra | % F (F / (F + P)) |",
         "|---|---:|---:|---:|---:|---:|---:|"]
    for c in COLS:
        canvien = sum(o[c] != o["FounderCEO"] for o in out)
        cnt = collections.Counter(o[c] for o in mostra)
        F, P = cnt.get("1", 0), cnt.get("0", 0)
        altres = len(mostra) - F - P - cnt.get(ND, 0)
        pct = f"{100 * F / (F + P):.2f} %" if F + P else "—"
        L.append(f"| `{c}` | {canvien} | {F} | {P} | {cnt.get(ND, 0)} | {altres} | {pct} |")
    L += ["", "`founderceo_rob_llista_predecessora_nd` és una **proposta**: no s'aplicarà sense la decisió de Jordi."]
    INFORME.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"Escrit {SORTIDA.relative_to(ROOT)} ({len(out)} files) i {INFORME.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

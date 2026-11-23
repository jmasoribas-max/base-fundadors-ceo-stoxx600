#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fase 1 del pla: evidències candidates a partir de les sortides de l'auditoria IA i de l'inventari antic.

Llegeix els fitxers de DF (branca `df/fitxers-per-claude`, carpeta `entrada_claude/`,
commit 34cff60) i genera, per a cada fila de la base, les cites candidates de CEO i de
fundador amb el seu estat de verificació previ. No modifica el registre ni la base.

Fonts:
  - r4 (ChatGPT i Claude): `ceo_31_10.evidencies[]` (CEO) i `dades[].evidencies[]`
    (any_fundacio, naixement_ceo, llista_fundadors, cita_fundador, ocupador_anterior,
    origen_entitat, cas_especific). Verificació: `MANIFEST_evidencies_web_r4.csv`
    (estat `verificada` = la cita es va trobar literalment al document baixat per DF).
  - r3e (ChatGPT i Claude): la cita de classificació de cada fila. Verificació:
    `CERTIFICACIO_parella_any_r3e.csv` ({model}_cita_verificada).
  - `fonts_v75r2.csv`: fonts amb cita literal; verificació `v75_cita_trobada=1`
    (cita trobada a la captura Wayback per script).

  python3 traspas/candidates_auditoria.py RUTA/entrada_claude
"""
from __future__ import annotations

import collections
import csv
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "dades" / "base_isin_any_v8r3.csv"
OUT = ROOT / "traspas" / "candidates_evidencia.csv"
RESUM = ROOT / "traspas" / "RESUM_CANDIDATES.md"

spec = importlib.util.spec_from_file_location("estat_files", ROOT / "estat" / "estat_files.py")
EF = importlib.util.module_from_spec(spec)
spec.loader.exec_module(EF)

FUNCIO_PREGUNTA = {
    "ceo_31_10": "ceo",
    "any_fundacio": "fundador", "naixement_ceo": "fundador", "llista_fundadors": "fundador",
    "cita_fundador": "fundador", "ocupador_anterior": "fundador", "origen_entitat": "fundador",
    "cas_especific": "fundador",
}
FUNCIO_FONT = {
    "fonts_ceo": "ceo", "proves_ceo": "ceo", "font_inici_mandat": "ceo",
    "prova_classificacio": "fundador", "prova_classificadora": "fundador", "proves": "fundador",
    "font_any_fundacio": "fundador", "font_naixement": "fundador", "primaria_empresa": "fundador",
    "casos_D1_D10": "fundador", "dictamen_D1": "fundador",
}
# proves que necessita cada regla (r4): conjunts alternatius
NECESSITA = {
    "a": [{"llista_fundadors"}],
    "b": [{"any_fundacio", "naixement_ceo"}],
    "b_per_part": [{"any_fundacio", "naixement_ceo"}],
    "d": [{"ocupador_anterior", "any_fundacio"}],
    "d_per_part": [{"ocupador_anterior", "any_fundacio"}],
    "e": [{"origen_entitat"}],
    "c_AAF64_reserva": [{"any_fundacio"}],
    "cita_fundador": [{"cita_fundador"}], "D37": [{"cita_fundador"}],
}
COLS = ["isin", "any", "funcio", "tipus_prova", "font_traspas", "id_origen", "cita_literal",
        "url", "url_arxivada", "data_document", "nivell_font", "verificacio_previa",
        "anomena_ceo", "model_ceo_coincideix", "model_etiqueta", "model_regla"]


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    E = Path(sys.argv[1])
    with BASE.open(encoding="utf-8", newline="") as f:
        base = {(r["isin"], r["any"]): r for r in csv.DictReader(f)}

    def noms(k):
        return [n.strip() for n in (base[k].get("ceos") or "").split("|") if n.strip()]

    def anomena(cita, k):
        c = EF.norm(cita)
        return any(EF.anomena(c, n) for n in noms(k))

    cands = []

    # r4
    for model in ("claude", "chatgpt"):
        man = {}
        with (E / f"r4_{model}" / "MANIFEST_evidencies_web_r4.csv").open(encoding="utf-8", newline="") as f:
            for m in csv.DictReader(f):
                man[(m["id_fila"], m["tipus_pregunta"], m["url"])] = m
        for line in (E / f"SORTIDA_{model}_COMPLETACIO.jsonl").open(encoding="utf-8"):
            r = json.loads(line)
            if r.get("tipus_registre") != "resposta":
                continue
            k = (r["isin"], str(r["any"]))
            if k not in base:
                continue
            ceo = r.get("ceo_31_10") or {}
            ceo_ok = any(EF.anomena(EF.norm(ceo.get("nom") or ""), n) for n in noms(k)) if ceo.get("nom") else False
            blocs = [("ceo_31_10", ceo.get("evidencies") or [])]
            blocs += [(d.get("tipus_pregunta"), d.get("evidencies") or []) for d in r.get("dades") or []]
            for tp, evs in blocs:
                for e in evs:
                    cita = (e.get("cita_literal") or "").strip()
                    url = (e.get("url") or "").strip()
                    if not cita or not url:
                        continue
                    if e.get("origen") == "web":
                        m = man.get((r["id_fila"], tp, url), {})
                        ver = "web_" + (m.get("estat") or "sense_manifest")
                        arx = e.get("url_arxivada") or (m.get("url_baixada") if (m.get("font_baixada") or "").startswith("wayback") else "")
                    else:
                        ver = "paquet_sense_verificar"
                        arx = e.get("url_arxivada") or ""
                    cands.append({
                        "isin": k[0], "any": k[1], "funcio": FUNCIO_PREGUNTA.get(tp, "context"),
                        "tipus_prova": tp, "font_traspas": f"r4_{model}", "id_origen": r["id_fila"],
                        "cita_literal": cita, "url": url, "url_arxivada": arx,
                        "data_document": e.get("data_document") or "", "nivell_font": e.get("nivell_font") or "",
                        "verificacio_previa": ver,
                        "anomena_ceo": "si" if anomena(cita, k) else "no",
                        "model_ceo_coincideix": "si" if ceo_ok else "no",
                        "model_etiqueta": r.get("founderceo_proposat") or "", "model_regla": r.get("regla_proposada") or "",
                    })

    # r3e
    cert = {}
    with (E / "CERTIFICACIO_parella_any_r3e.csv").open(encoding="utf-8", newline="") as f:
        for c in csv.DictReader(f):
            cert[(c["isin"], c["any"])] = c
    for model in ("claude", "chatgpt"):
        for line in (E / f"SORTIDA_{model}_COMPLET.jsonl").open(encoding="utf-8"):
            r = json.loads(line)
            if r.get("tipus_registre") != "classificacio":
                continue
            k = (r["isin"], str(r["any"]))
            cita = (r.get("cita_literal") or "").strip()
            url = (r.get("url_oficial") or "").strip()
            if k not in base or not cita or not url:
                continue
            c = cert.get(k, {})
            ver = "r3e_verificada" if c.get(f"{model}_cita_verificada") == "True" else "r3e_no_verificada"
            cands.append({
                "isin": k[0], "any": k[1], "funcio": "fundador", "tipus_prova": "classificacio_r3e",
                "font_traspas": f"r3e_{model}", "id_origen": r.get("id_cec") or "",
                "cita_literal": cita, "url": url, "url_arxivada": r.get("url_arxivada") or "",
                "data_document": "", "nivell_font": r.get("nivell_font") or "", "verificacio_previa": ver,
                "anomena_ceo": "si" if anomena(cita, k) else "no",
                "model_ceo_coincideix": "si" if any(EF.anomena(EF.norm(r.get("ceo_31_10") or ""), n) for n in noms(k)) else "no",
                "model_etiqueta": r.get("founderceo_proposat") or "", "model_regla": r.get("regla_proposada") or "",
            })

    # fonts_v75r2
    with (E / "fonts_v75r2.csv").open(encoding="utf-8", newline="") as f:
        for s in csv.DictReader(f):
            cita = (s.get("cita_literal") or "").strip()
            url = (s.get("url") or "").strip()
            funcio = FUNCIO_FONT.get(s.get("tipus_evidencia") or "")
            if not cita or not url.lower().startswith("http") or not funcio:
                continue
            claus = set()
            if s.get("isin") and s.get("any"):
                claus.add((s["isin"], s["any"]))
            for p in (s.get("isin_anys_enllacats") or "").split(";"):
                if "|" in p:
                    i, a = p.strip().split("|", 1)
                    claus.add((i, a))
            arx = s.get("v75_url_arxivada") or s.get("url_arxivada") or ""
            ver = "v75_cita_a_captura" if s.get("v75_cita_trobada") == "1" and s.get("v75_on_cita") == "captura_wayback" \
                else ("v75_cita_trobada_" + (s.get("v75_on_cita") or "") if s.get("v75_cita_trobada") == "1" else "v75_sense_verificar")
            for k in sorted(claus):
                if k not in base:
                    continue
                cands.append({
                    "isin": k[0], "any": k[1], "funcio": funcio, "tipus_prova": s.get("tipus_evidencia") or "",
                    "font_traspas": "fonts_v75r2", "id_origen": s.get("id_font") or "",
                    "cita_literal": cita, "url": url, "url_arxivada": arx, "data_document": s.get("data_document") or "",
                    "nivell_font": s.get("nivell") or "", "verificacio_previa": ver,
                    "anomena_ceo": "si" if anomena(cita, k) else "no", "model_ceo_coincideix": "",
                    "model_etiqueta": "", "model_regla": "",
                })

    cands.sort(key=lambda c: (c["isin"], c["any"], c["funcio"], c["font_traspas"], c["tipus_prova"], c["url"], c["cita_literal"]))
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, lineterminator="\n")
        w.writeheader()
        w.writerows(cands)

    # Cobertura sobre l'estat actual
    with (ROOT / "estat" / "estat_files.csv").open(encoding="utf-8", newline="") as f:
        estat = {(r["isin"], r["any"]): r for r in csv.DictReader(f)}
    per = collections.defaultdict(list)
    for c in cands:
        per[(c["isin"], c["any"])].append(c)
    VER = {"web_verificada", "r3e_verificada", "v75_cita_a_captura"}

    def ceo_ok(cs, verif):
        return any(c["funcio"] == "ceo" and c["anomena_ceo"] == "si" and (not verif or c["verificacio_previa"] in VER) for c in cs)

    def fun_ok(k, cs, verif):
        lab = base[k]["FounderCEO"]
        toks = {t for t in (base[k].get("regles") or "").replace("|", ";").split(";") if t}
        cs = [c for c in cs if c["funcio"] == "fundador" and (not verif or c["verificacio_previa"] in VER)]
        if not cs:
            return False
        # r3e o fonts antigues: la cita de classificació de la fila
        if any(c["font_traspas"].startswith("r3e") and c["model_etiqueta"] == lab for c in cs):
            return True
        if any(c["font_traspas"] == "fonts_v75r2" for c in cs):
            return True
        tipus = {c["tipus_prova"] for c in cs}
        for t in toks:
            for conj in NECESSITA.get(t, []):
                if conj <= tipus:
                    return True
        return False

    L = ["# Evidències candidates de l'auditoria IA i de l'inventari antic\n",
         "Generat per `traspas/candidates_auditoria.py` a partir dels fitxers de DF (`df/fitxers-per-claude`, "
         "commit `34cff60`). No modifica el registre. «Verificada» vol dir que la cita es va trobar literalment "
         "en un document baixat per script de DF (manifest r4, certificació r3e o captura Wayback de la v7.5).\n",
         f"Candidates: {EF.num(len(cands))} cites per a {EF.num(len(per))} files.\n",
         "## Candidates per font i verificació prèvia\n", "| Font | Funció | Verificació prèvia | Cites |", "|---|---|---|---:|"]
    for (ft, fu, v), n in sorted(collections.Counter((c["font_traspas"], c["funcio"], c["verificacio_previa"]) for c in cands).items()):
        L.append(f"| {ft} | {fu} | `{v}` | {EF.num(n)} |")
    L.append("")
    L.append("## Què aporten a les files incompletes\n")
    L.append("| Mancança actual | Files | Amb candidata | Amb candidata ja verificada |")
    L.append("|---|---:|---:|---:|")
    for etiqueta, falta, fn in (
        ("Sense cita de CEO (C1)", "falta_ceo", lambda k, cs, v: ceo_ok(cs, v)),
        ("Sense cita de fundador (C2)", "falta_fundador", lambda k, cs, v: fun_ok(k, cs, v)),
    ):
        ks = [k for k, e in estat.items() if falta in e["estat"].split("+")]
        a = sum(fn(k, per.get(k, []), False) for k in ks)
        b = sum(fn(k, per.get(k, []), True) for k in ks)
        L.append(f"| {etiqueta} | {EF.num(len(ks))} | {EF.num(a)} | {EF.num(b)} |")
    for lab, nom in (("1", "F"), ("0", "P")):
        for etiqueta, falta, fn in (("CEO", "falta_ceo", lambda k, cs, v: ceo_ok(cs, v)),
                                    ("fundador", "falta_fundador", lambda k, cs, v: fun_ok(k, cs, v))):
            ks = [k for k, e in estat.items() if falta in e["estat"].split("+") and e["FounderCEO"] == lab]
            L.append(f"| … {nom} sense {etiqueta} | {EF.num(len(ks))} | {EF.num(sum(fn(k, per.get(k, []), False) for k in ks))} | "
                     f"{EF.num(sum(fn(k, per.get(k, []), True) for k in ks))} |")
    L.append("")
    ks = [k for k, e in estat.items() if ("falta_ceo" in e["estat"] or "falta_fundador" in e["estat"])]
    both = sum((("falta_ceo" not in estat[k]["estat"]) or ceo_ok(per.get(k, []), True)) and
               (("falta_fundador" not in estat[k]["estat"]) or fun_ok(k, per.get(k, []), True)) for k in ks)
    L.append(f"Files que avui no tenen C1 o C2 i que quedarien amb totes dues amb candidates ja verificades: "
             f"**{EF.num(both)} de {EF.num(len(ks))}**.\n")
    RESUM.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())

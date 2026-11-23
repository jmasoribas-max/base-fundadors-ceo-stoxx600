#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Estat de cada fila (ISIN-any) de la base respecte de la definició de «fila acabada».

Definició (docs/PLA_FINALITZACIO_20261123.md, secció 1):

  C1 CEO          almenys una cita [V] del registre (funcio_cita=ceo) que anomena
                  cadascun dels CEO de la fila.
  C2 Fundador     F: cita [V] de fundador (funcio_cita=fundador) al registre, o la
                  cita antiga del CSV (font_classificacio_cita).
                  P: el mateix, amb la prova a-e indicada a `regles`.
                  NA / ND: alguna entrada [V] del registre que documenti la cerca.
  C3 Arxiu        alguna de les cites que compleixen C1 i alguna de les que
                  compleixen C2 té cita_verificada_a_captura=si (Wayback, per DF).
  C4 Coherència   el CSV és coherent (ceos = sim_ceo_aplicat; la regla de `regles`
                  correspon a l'etiqueta; motiu_nd només a ND; motiu_na a NA) i la
                  fila no té cap dubte obert a PENDENTS.md (seccions de dubtes dels
                  lots) que no consti tancat a estat/dubtes_tancats.csv.

Una cita és vàlida si té cita_literal i url_font http(s), marca_veritat=[V] i les
notes no contenen «no_valida».

Només llegeix fitxers locals. No fa cap petició de xarxa ni modifica dades/.

  python3 estat/estat_files.py              # escriu estat/estat_files.csv i estat/RESUM_ESTAT.md
  python3 estat/estat_files.py --comprova   # falla (exit 1) si els fitxers d'estat no estan al dia
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "dades" / "base_isin_any_v8r3.csv"
REG = ROOT / "docs" / "REGISTRE_CANVIS.csv"
PENDENTS = ROOT / "PENDENTS.md"
TANCATS = ROOT / "estat" / "dubtes_tancats.csv"
OUT_CSV = ROOT / "estat" / "estat_files.csv"
OUT_MD = ROOT / "estat" / "RESUM_ESTAT.md"

SECCIONS_DUBTES = (
    "Dubtes dels lots fora_mostra_auditoria (regla 29)",
    "Dubtes del lot ceo_pendent (lot 9)",
    "Dubtes del lot traspàs de cites (lot 10)",
    "Dubtes del lot 12 (cerca de CEO del grup F)",
    "Dubtes del lot 16 (cites de fundador del grup F)",
)
REGLES_SI = {"cita_fundador", "D37", "FT", "D10b_prelacio", "D10"}
REGLES_NO = {"a", "b", "c_AAF64_reserva", "d", "e", "d_per_part", "b_per_part"}
PARTICULES = {"de", "del", "della", "di", "da", "das", "dos", "do", "van", "von",
              "der", "den", "le", "la", "les", "du", "y", "i", "e", "af", "zu", "ter", "ten"}
CARRECS = re.compile(
    r"\bceos?\b|chief executive|managing director|vorstandsvorsitz|vorsitzende[rn]? des vorstand"
    r"|sprecher des vorstand|chair(man|woman|person)? of the (board of management|management board|executive board)"
    r"|consejer[oa] delegad[oa]|director general|directeur general|directrice generale|\bpdg\b"
    r"|president[- ]directeur|administrat(eur|rice) delegue|amministratore delegato"
    r"|verkstallande direktor|koncernchef|\bvd\b|toimitusjohtaja|administrerende direktor"
    r"|adm\. direktor|konsernsjef|prezes zarzadu|presidente (ejecutivo|executivo|esecutivo)"
    r"|executive chair|group chief|bestuursvoorzitter|voorzitter van de raad van bestuur"
    r"|directeur generaal|generaldirektor|chief executive officer|presidente e ceo"
    r"|\bgerant(e|s|es)?\b|\bgerance\b|president of the [\w .]{0,30}management board|president du directoire"
    r"|management board.{0,100}president of the board|presidente del consiglio di gestione"
)
TRANSLIT = str.maketrans({"ø": "o", "Ø": "o", "æ": "ae", "Æ": "ae", "ß": "ss", "ł": "l",
                          "Ł": "l", "đ": "d", "Đ": "d", "ı": "i", "œ": "oe", "Œ": "oe"})
MAX_IDS = 5
COLUMNES = [
    "isin", "any", "nom", "FounderCEO", "ceos", "regles", "estat_certificacio_antic",
    "c1_ceo", "c1_ids", "c1_tipus", "c2_fundador", "c2_ids", "c3_arxiu",
    "c4_coherencia", "dubtes_oberts", "avisos", "estat",
]


def norm(s: str) -> str:
    s = (s or "").translate(TRANSLIT)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s).lower()


def anys(text: str) -> set[str]:
    out: set[str] = set()
    for a, z in re.findall(r"(\d{4})(?:\s*[-–]\s*(\d{4}))?", text or ""):
        if z:
            out.update(str(y) for y in range(int(a), int(z) + 1))
        else:
            out.add(a)
    return out


def tokens_nom(nom: str) -> list[str]:
    parts = [p.strip(".,;:()") for p in nom.split()]
    if len(parts) > 1:
        parts = parts[1:]  # el nom de pila sol no identifica la persona
    toks = [norm(p) for p in parts if len(p.strip(".")) >= 3 and norm(p) not in PARTICULES]
    return toks or [norm(nom)]


def anomena(cita_norm: str, nom: str) -> bool:
    return any(t and t in cita_norm for t in tokens_nom(nom))


def valida(e: dict) -> bool:
    return (
        bool((e.get("cita_literal") or "").strip())
        and (e.get("url_font") or "").strip().lower().startswith(("http://", "https://"))
        and (e.get("marca_veritat") or "") == "[V]"
        and "no_valida" not in (e.get("notes") or "")
    )


def ids(entries: list[dict]) -> str:
    vals = sorted({(e.get("id_document_o_font") or "").strip() or "(sense id)" for e in entries})
    extra = f";(+{len(vals) - MAX_IDS})" if len(vals) > MAX_IDS else ""
    return ";".join(vals[:MAX_IDS]) + extra


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def dubtes_tancats() -> set[tuple[str, str]]:
    if not TANCATS.exists():
        return set()
    with TANCATS.open(encoding="utf-8", newline="") as f:
        return {((r.get("isin") or "").strip(), (r.get("any") or "").strip()) for r in csv.DictReader(f)}


def dubtes_pendents(tancats: set[tuple[str, str]]) -> dict[tuple[str, str], set[str]]:
    oberts: dict[tuple[str, str], set[str]] = collections.defaultdict(set)
    seccio = None
    for linia in PENDENTS.read_text(encoding="utf-8").splitlines():
        if linia.startswith("## "):
            titol = linia[3:].strip()
            seccio = titol if titol in SECCIONS_DUBTES else None
            continue
        if not seccio or not linia.startswith("| `"):
            continue
        cel = [c.strip() for c in linia.strip().strip("|").split("|")]
        if len(cel) < 2:
            continue
        isin = cel[0].strip("` ")
        ref = ("regla29" if "regla 29" in seccio else "lot9" if "lot 9" in seccio
               else "lot12" if "lot 12" in seccio else "lot16" if "lot 16" in seccio else "lot10")
        for y in anys(re.sub(r"<[^>]+>", "", cel[1])):
            oberts[(isin, y)].add(ref)
    for k in tancats:
        oberts.pop(k, None)
    return oberts


def calcula() -> tuple[list[dict], dict]:
    with BASE.open(encoding="utf-8", newline="") as f:
        base = list(csv.DictReader(f))
    with REG.open(encoding="utf-8", newline="") as f:
        reg = list(csv.DictReader(f))
    claus = {(r["isin"], r["any"]) for r in base}
    per_fila: dict[tuple[str, str], list[dict]] = collections.defaultdict(list)
    for e in reg:
        if not valida(e):
            continue
        e["_cita_norm"] = norm(e["cita_literal"])
        isin = (e.get("isin") or "").strip()
        for y in anys(e.get("anys", "")):
            if (isin, y) in claus:
                per_fila[(isin, y)].append(e)
    tancats = dubtes_tancats()
    oberts = dubtes_pendents(tancats)

    files = []
    for r in base:
        k = (r["isin"], r["any"])
        lab = r["FounderCEO"]
        es = per_fila.get(k, [])
        noms = [n.strip() for n in (r.get("ceos") or "").split("|") if n.strip()]
        ceo_es = [e for e in es if e.get("funcio_cita") == "ceo"]
        fun_es = [e for e in es if e.get("funcio_cita") == "fundador"]
        avisos = []
        out = {
            "isin": r["isin"], "any": r["any"], "nom": r.get("nom_panell", ""),
            "FounderCEO": lab, "ceos": r.get("ceos", ""), "regles": r.get("regles", ""),
            "estat_certificacio_antic": r.get("sim_estat_certificacio", ""),
        }
        c1_ok = c2_ok = c3_ok = False
        c1_suport: list[dict] = []
        c2_suport: list[dict] = []

        if lab in ("NA_sense_ceo", "no_determinat"):
            docs = [e for e in es if e.get("funcio_cita") in ("ceo", "fundador", "context")]
            etiqueta = "rsc_documentat" if lab == "NA_sense_ceo" else "cerca_documentada"
            falta = "falta_rsc" if lab == "NA_sense_ceo" else "falta_cerca"
            if lab == "no_determinat" and noms:
                c1_suport = [e for e in ceo_es if all(anomena(e["_cita_norm"], n) for n in noms)] or \
                    [e for e in ceo_es if any(anomena(e["_cita_norm"], n) for n in noms)]
                out["c1_ceo"] = "ok" if c1_suport else ("cita_sense_nom" if ceo_es else "falta")
                c1_ok = bool(c1_suport)
            else:
                c1_suport = docs
                out["c1_ceo"] = etiqueta if docs else falta
                c1_ok = bool(docs)
            c2_suport = docs
            out["c2_fundador"] = etiqueta if docs else falta
            c2_ok = bool(docs)
            out["c1_tipus"] = ""
        else:
            nomenats = {n: [e for e in ceo_es if anomena(e["_cita_norm"], n)] for n in noms}
            c1_suport = sorted({id(e): e for v in nomenats.values() for e in v}.values(),
                               key=lambda e: e.get("id_document_o_font") or "")
            if noms and all(nomenats.values()):
                out["c1_ceo"] = "ok"
                c1_ok = True
            elif any(nomenats.values()):
                out["c1_ceo"] = "co_ceo_parcial"
            elif ceo_es:
                out["c1_ceo"] = "cita_sense_nom"
                c1_suport = []
            else:
                out["c1_ceo"] = "falta"
            tipus = {"interval" if "interval" in (e.get("marca_prova") or "") else "document"
                     for e in c1_suport}
            out["c1_tipus"] = "+".join(sorted(tipus))
            if c1_suport and not any(CARRECS.search(e["_cita_norm"]) for e in c1_suport):
                avisos.append("carrec_no_detectat_a_la_cita")
            c2_suport = fun_es
            if fun_es:
                out["c2_fundador"] = "ok_registre"
                c2_ok = True
            elif (r.get("font_classificacio_cita") or "").strip() and \
                    (r.get("font_classificacio_url") or "").strip():
                out["c2_fundador"] = "ok_columna_antiga"
                c2_ok = True
            else:
                out["c2_fundador"] = "falta"
        out["c1_ids"] = ids(c1_suport) if c1_suport else ""
        out["c2_ids"] = ids(c2_suport) if c2_suport else ""

        # C3 arxiu
        a1 = any(e.get("cita_verificada_a_captura") == "si" for e in c1_suport)
        a2 = any(e.get("cita_verificada_a_captura") == "si" for e in c2_suport)
        if not (c1_ok and c2_ok):
            out["c3_arxiu"] = "sense_evidencia"
        elif a1 and a2:
            out["c3_arxiu"] = "ok"
            c3_ok = True
        elif out.get("c2_fundador") == "ok_columna_antiga" and a1:
            out["c3_arxiu"] = "falta_fundador_columna_antiga"
        else:
            out["c3_arxiu"] = "falta_" + ("ceo+fundador" if not a1 and not a2 else ("ceo" if not a1 else "fundador"))

        # C4 coherència
        probs = []
        toks = {t for t in re.split(r"[;|]", r.get("regles") or "") if t}
        if (r.get("ceos") or "") != (r.get("sim_ceo_aplicat") or ""):
            probs.append("ceos_diferent_de_sim_ceo_aplicat")
        if lab == "1" and not toks & REGLES_SI:
            probs.append("F_sense_regla_de_si")
        if lab == "0" and not toks & REGLES_NO:
            probs.append("P_sense_prova_de_no")
        if lab == "0" and toks & {"cita_fundador", "D37"}:
            probs.append("P_amb_regla_de_si")
        if (r.get("motiu_nd") or "").strip() and lab != "no_determinat":
            probs.append("motiu_nd_residual")
        if lab == "NA_sense_ceo" and not (r.get("motiu_na") or "").strip():
            probs.append("NA_sense_motiu_na")
        dub = set(oberts.get(k, set()))
        if lab == "no_determinat" and k not in tancats:
            dub.add("ND_obert")  # un ND només es dona per tancat si consta a dubtes_tancats.csv
        dub = sorted(dub)
        out["c4_coherencia"] = ";".join(probs) if probs else "ok"
        out["dubtes_oberts"] = ";".join(dub)
        out["avisos"] = ";".join(avisos)

        falta = []
        if not c1_ok:
            falta.append("falta_ceo")
        if not c2_ok:
            falta.append("falta_fundador")
        if probs:
            falta.append("incoherent")
        if dub:
            falta.append("dubte_obert")
        if not c3_ok:
            falta.append("falta_arxiu")
        out["estat"] = "acabada" if not falta else "+".join(falta)
        files.append(out)

    info = {
        "sha_base": sha256(BASE), "sha_registre": sha256(REG), "sha_pendents": sha256(PENDENTS),
        "sha_tancats": sha256(TANCATS) if TANCATS.exists() else "(no existeix)",
        "n_registre": len(reg),
    }
    return files, info


def csv_text(files: list[dict]) -> str:
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=COLUMNES, lineterminator="\n")
    w.writeheader()
    for f in sorted(files, key=lambda x: (x["isin"], x["any"])):
        w.writerow(f)
    return buf.getvalue()


def num(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def pct(n: int, d: int) -> str:
    if not d:
        return "0"
    return num(n) + " (" + f"{100 * n / d:.1f}".replace(".", ",") + " %)"


def md_text(files: list[dict], info: dict) -> str:
    L = []
    L.append("# Estat de la base per fila\n")
    L.append("Fitxer generat per `estat/estat_files.py`. No l'editis a mà. Definicions a "
             "[`estat/README.md`](README.md).\n")
    L.append("Entrades llegides:\n")
    L.append(f"- `dades/base_isin_any_v8r3.csv` SHA-256 `{info['sha_base']}`")
    L.append(f"- `docs/REGISTRE_CANVIS.csv` SHA-256 `{info['sha_registre']}` ({num(info['n_registre'])} entrades)")
    L.append(f"- `PENDENTS.md` SHA-256 `{info['sha_pendents']}`")
    L.append(f"- `estat/dubtes_tancats.csv` SHA-256 `{info['sha_tancats']}`\n")

    grups = [("F (`1`)", "1"), ("P (`0`)", "0"), ("NA", "NA_sense_ceo"), ("ND", "no_determinat")]
    L.append("## Resum per etiqueta\n")
    L.append("| Etiqueta | Files | C1 CEO | C2 fundador | C1 i C2 | C4 coherent i sense dubtes | C3 arxiu | **Acabades** |")
    L.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for nom, lab in grups + [("**Total**", None)]:
        S = [f for f in files if lab is None or f["FounderCEO"] == lab]
        n = len(S)
        c1 = sum("falta_ceo" not in f["estat"] for f in S)
        c2 = sum("falta_fundador" not in f["estat"] for f in S)
        c12 = sum("falta_ceo" not in f["estat"] and "falta_fundador" not in f["estat"] for f in S)
        c4 = sum("incoherent" not in f["estat"] and "dubte_obert" not in f["estat"] for f in S)
        c3 = sum(f["c3_arxiu"] == "ok" for f in S)
        ac = sum(f["estat"] == "acabada" for f in S)
        L.append(f"| {nom} | {num(n)} | {pct(c1, n)} | {pct(c2, n)} | {pct(c12, n)} | {pct(c4, n)} | {pct(c3, n)} | **{pct(ac, n)}** |")
    L.append("")

    S = files
    n = len(S)
    ev = [f for f in S if "falta_ceo" not in f["estat"] and "falta_fundador" not in f["estat"]]
    ev_coh = [f for f in ev if "incoherent" not in f["estat"] and "dubte_obert" not in f["estat"]]
    L.append("## Embut\n")
    L.append("| Pas | Files |")
    L.append("|---|---:|")
    L.append(f"| Panell | {num(n)} |")
    L.append(f"| Amb evidència de CEO i de fundador (C1 i C2) | {pct(len(ev), n)} |")
    L.append(f"| … i coherents, sense dubtes oberts (C4) | {pct(len(ev_coh), n)} |")
    L.append(f"| … i arxivades a Wayback amb la cita verificada (C3): **acabades** | {pct(sum(f['estat'] == 'acabada' for f in S), n)} |")
    L.append("")

    L.append("## Què falta, per condició\n")
    L.append("Una fila pot tenir més d'una mancança.\n")
    L.append("| Mancança | F | P | NA | ND | Total |")
    L.append("|---|---:|---:|---:|---:|---:|")
    for m in ("falta_ceo", "falta_fundador", "incoherent", "dubte_obert", "falta_arxiu"):
        cnt = [sum(m in f["estat"].split("+") for f in S if f["FounderCEO"] == lab) for _, lab in grups]
        L.append(f"| `{m}` | " + " | ".join(f"{num(c)}" for c in cnt) + f" | {num(sum(cnt))} |")
    L.append("")

    L.append("## Detall de C1 (CEO) i C2 (fundador)\n")
    L.append("| Valor de `c1_ceo` | Files |")
    L.append("|---|---:|")
    for k, v in sorted(collections.Counter(f["c1_ceo"] for f in S).items(), key=lambda x: -x[1]):
        L.append(f"| `{k}` | {num(v)} |")
    L.append("")
    L.append("| Valor de `c2_fundador` | Files |")
    L.append("|---|---:|")
    for k, v in sorted(collections.Counter(f["c2_fundador"] for f in S).items(), key=lambda x: -x[1]):
        L.append(f"| `{k}` | {num(v)} |")
    L.append("")
    L.append("| Valor de `c3_arxiu` | Files |")
    L.append("|---|---:|")
    for k, v in sorted(collections.Counter(f["c3_arxiu"] for f in S).items(), key=lambda x: -x[1]):
        L.append(f"| `{k}` | {num(v)} |")
    L.append("")

    L.append("## Segons l'estat de certificació antic (`sim_estat_certificacio`)\n")
    L.append("| Estat antic | Files | C1 i C2 | Acabades |")
    L.append("|---|---:|---:|---:|")
    for est in ("certificada", "certificada_ceo_pendent", "no_certificada", "fora_mostra_auditoria"):
        T = [f for f in S if f["estat_certificacio_antic"] == est]
        e12 = sum("falta_ceo" not in f["estat"] and "falta_fundador" not in f["estat"] for f in T)
        L.append(f"| `{est}` | {num(len(T))} | {pct(e12, len(T))} | {pct(sum(f['estat'] == 'acabada' for f in T), len(T))} |")
    L.append("")

    per = collections.defaultdict(list)
    for f in S:
        per[f["isin"]].append(f)
    F_isin = [i for i, v in per.items() if any(f["FounderCEO"] == "1" for f in v)]
    def totes(v, cond):
        return all(cond(f) for f in v)
    evid = lambda f: "falta_ceo" not in f["estat"] and "falta_fundador" not in f["estat"]  # noqa: E731
    L.append("## Per empresa (ISIN)\n")
    L.append("| | Totes les files amb C1 i C2 | Totes les files acabades | Total |")
    L.append("|---|---:|---:|---:|")
    L.append(f"| Empreses amb almenys un any F | {sum(totes(per[i], evid) for i in F_isin)} | "
             f"{sum(totes(per[i], lambda f: f['estat'] == 'acabada') for i in F_isin)} | {len(F_isin)} |")
    L.append(f"| Totes les empreses | {num(sum(totes(v, evid) for v in per.values()))} | "
             f"{num(sum(totes(v, lambda f: f['estat'] == 'acabada') for v in per.values()))} | {num(len(per))} |")
    L.append("")

    inc = [f for f in S if f["c4_coherencia"] != "ok"]
    L.append(f"## Incoherències del CSV ({len(inc)} files)\n")
    if inc:
        L.append("| ISIN | Any | FounderCEO | `ceos` | `regles` | Problema |")
        L.append("|---|---|---|---|---|---|")
        for f in sorted(inc, key=lambda x: (x["isin"], x["any"])):
            L.append(f"| `{f['isin']}` | {f['any']} | {f['FounderCEO']} | {f['ceos']} | `{f['regles']}` | {f['c4_coherencia']} |")
    L.append("")
    av = collections.Counter(a for f in S for a in f["avisos"].split(";") if a)
    if av:
        L.append("## Avisos (no bloquegen)\n")
        for k, v in sorted(av.items()):
            L.append(f"- `{k}`: {v} files")
        L.append("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description="Estat de cada fila de la base (sense xarxa).")
    ap.add_argument("--comprova", action="store_true",
                    help="no escriu res; falla si estat/estat_files.csv o estat/RESUM_ESTAT.md no estan al dia")
    args = ap.parse_args()
    files, info = calcula()
    t_csv, t_md = csv_text(files), md_text(files, info)
    if args.comprova:
        dif = [p.relative_to(ROOT).as_posix() for p, t in ((OUT_CSV, t_csv), (OUT_MD, t_md))
               if not p.exists() or p.read_text(encoding="utf-8") != t]
        if dif:
            print("Els fitxers d'estat no estan al dia: " + ", ".join(dif))
            print("Executa: python3 estat/estat_files.py")
            return 1
        print("OK: els fitxers d'estat estan al dia.")
        return 0
    OUT_CSV.write_text(t_csv, encoding="utf-8")
    OUT_MD.write_text(t_md, encoding="utf-8")
    acab = sum(f["estat"] == "acabada" for f in files)
    print(f"Files: {len(files)}; acabades: {acab}. Escrit {OUT_CSV.relative_to(ROOT)} i {OUT_MD.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

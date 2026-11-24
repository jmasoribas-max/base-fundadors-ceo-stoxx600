#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Estat de cada fila (ISIN-any) de la base respecte de la definició de «fila acabada».

Definició (docs/PLA_FINALITZACIO_20261123.md, secció 1):

  C1 CEO          almenys una cita [V] del registre (funcio_cita=ceo) que anomena
                  cadascun dels CEO de la fila.
  C2 Fundador     F: cita [V] de fundador (funcio_cita=fundador) al registre, o la
                  cita antiga del CSV (font_classificacio_cita).
                  P: una prova de no fundador COMPLETA, amb cada part documentada per una
                  cita [V] (decisió de Jordi del 24/11/2026, opció b):
                    a llista de fundadors (sense el CEO) · e origen estatal o corporatiu ·
                    c any de fundació 64 anys o més abans · b any de fundació + naixement
                    de cada CEO · d any de fundació + ocupador anterior de cada CEO.
                  La part d'una cita es pren de les notes («Part de la prova …: part») o,
                  si no hi és, del contingut de la cita.
                  NA / ND: alguna entrada [V] del registre que documenti la cerca.
  C3 Arxiu        alguna de les cites que compleixen C1 i alguna de les que
                  compleixen C2 té cita_verificada_a_captura=si (Wayback); a les P,
                  cada part de la prova ha de tenir una cita verificada a la captura.
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
    "Dubtes del lot 17 (cerca de CEO)",
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
    r"|chair(man|woman|person)? of [\w .'’-]{0,45}(board of management|management board|executive board)"
    r"|executive board.{0,160}\(chair(man|woman|person)?\)|executive board.{0,80}its chair(man|woman|person)?"
    r"|president of the (executive committee|ec|management committee)\b|voorzitter van het directiecomite"
    r"|president du comite de direction|maximo responsable ejecutivo"
    r"|spokes(man|woman|person) of the (executive|management) board|chair(man|woman|person)? of the board of executive directors"
)
TRANSLIT = str.maketrans({"ø": "o", "Ø": "o", "æ": "ae", "Æ": "ae", "ß": "ss", "ł": "l",
                          "Ł": "l", "đ": "d", "Đ": "d", "ı": "i", "œ": "oe", "Œ": "oe",
                          "’": "'", "‘": "'", "´": "'", "`": "'"})
MAX_IDS = 5
# Parts de cada prova de no fundador (decisió de Jordi del 24/11/2026, opció b).
PROVES_PARTS = {
    "a": ("llista_fundadors",),
    "e": ("origen_entitat",),
    "c": ("any_fundacio_64",),
    "b": ("any_fundacio", "naixement_ceo"),
    "d": ("any_fundacio", "ocupador_anterior"),
}
ORDRE_PROVES = ("a", "e", "c", "b", "d")
PARTS_PERSONA = {"naixement_ceo", "ocupador_anterior"}
RE_PART_EXPLICITA = re.compile(r"Part de la prova(?: [\w-]+)?: (llista_fundadors|origen_entitat|any_fundacio"
                               r"|naixement_ceo|ocupador_anterior)\b")
ANY_HIST = r"\b(1[5-9]\d\d|20[0-2]\d)\b"
FUND_VERB = (r"(founded|founding|established|incorporated|was created|were created|formed|set up|dates? back|inception"
             r"|gegrundet|grundung|fondee?|fondation|fundad[ao]|fundacion|fondata|fondato|costituit|constituid[ao]"
             r"|opgericht|oprichting|grundad|grundlagt|stiftet|perustettu|zalozon)")
CONTINGUT = {
    "any_fundacio": re.compile(FUND_VERB + r".{0,80}" + ANY_HIST + "|" + ANY_HIST + r".{0,80}" + FUND_VERB),
    "naixement_ceo": re.compile(r"(born|\bnee?\b|geboren|\bgeb\.|nacid|\bnato\b|\bnata\b|\bfodt|\bfodd|syntyn|urodz"
                                r"|year of birth|date of birth|\baged? \d{2}|\d{2} years old|\(\d{2}\)|\bage:? \d{2})"),
    "ocupador_anterior": re.compile(r"(joined|prior to|previously|before joining|before that|worked (at|for|as)"
                                    r"|career (at|with|in)|spent \d+ years|served as|held (the )?(position|role|post)s?"
                                    r"|was (the )?(ceo|cfo|coo|head|director|partner|president|managing|chief|vice|executive)"
                                    r"|from \d{4} (to|until)|vorher|zuvor|davor|war .{0,60} bei|tatig|auparavant"
                                    r"|precedemment|a rejoint|anteriormente|previamente|se incorporo|tidigare|tidligere"
                                    r"|aiemmin|in precedenza|eerder|daarvoor)"),
    "llista_fundadors": re.compile(r"(founded by|co-?founded|founders?\b|fondee? par|fondateurs?|gegrundet (von|durch)"
                                   r"|grunder|fundad[ao] por|fundadores|opgericht door|oprichters?|grundades av|grundare"
                                   r"|perustaja)"),
    "origen_entitat": re.compile(r"(spin-? ?off|spun off|demerg|carve-? ?out|privatis|privatiz|state-owned|sole shareholder"
                                 r"|created by|established by|formed by|set up by|subsidiary of|was part of|separation from"
                                 r"|ausglieder|abspaltung|scission|escision|scissione|nationalised|nationalized"
                                 r"|owned by the (state|government)|(state|government) (owned|holding))"),
}
COLUMNES = [
    "isin", "any", "nom", "FounderCEO", "ceos", "regles", "estat_certificacio_antic",
    "c1_ceo", "c1_ids", "c1_tipus", "c2_fundador", "c2_ids", "c2_parts", "c3_arxiu",
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


def parts_entrada(e: dict, noms: list[str], any_fila: int) -> set[tuple[str, str]]:
    """Parts d'una prova de no fundador que documenta una cita: {(part, persona)}.

    persona és el CEO per a les parts de persona (naixement, ocupador anterior) i '' per a les
    parts d'empresa. La part es pren de les notes si hi és explícita; si no, del contingut.
    """
    t = e["_cita_norm"]
    noms_cita = [n for n in noms if anomena(t, n)]
    m = RE_PART_EXPLICITA.search(e.get("notes") or "")
    candidates = [m.group(1)] if m else [p for p, rx in CONTINGUT.items() if rx.search(t)]
    out: set[tuple[str, str]] = set()
    for p in candidates:
        if p in PARTS_PERSONA:
            out.update((p, n) for n in noms_cita)
        elif p == "llista_fundadors":
            if not noms_cita:  # una llista de fundadors que anomena el CEO no prova que no ho sigui
                out.add((p, ""))
        else:
            out.add((p, ""))
        if p == "any_fundacio":
            anys_cita = [int(y) for y in re.findall(ANY_HIST, t)]
            if anys_cita and min(anys_cita) <= any_fila - 64:
                out.add(("any_fundacio_64", ""))
    return out


def prova_P(cands: list[dict], noms: list[str], any_fila: int) -> tuple[str, list[dict], str, bool]:
    """Avalua les proves de no fundador d'una fila P a partir de les cites candidates.

    Retorna (prova completa o '', cites que la sostenen, parts presents, si cada part té una
    cita verificada a la captura). Prefereix una prova amb totes les parts verificades.
    """
    per_part: dict[tuple[str, str], list[dict]] = collections.defaultdict(list)
    for e in cands:
        for pp in parts_entrada(e, noms, any_fila):
            per_part[pp].append(e)
    persones = noms or [""]
    millor = ("", [], False)
    for prova in ORDRE_PROVES:
        claus = [(p, n) for p in PROVES_PARTS[prova] for n in (persones if p in PARTS_PERSONA else [""])]
        if not all(per_part.get(k) for k in claus):
            continue
        verif = all(any(e.get("cita_verificada_a_captura") == "si" for e in per_part[k]) for k in claus)
        suport = []
        for k in claus:
            es = sorted(per_part[k], key=lambda e: (e.get("cita_verificada_a_captura") != "si",
                                                    e.get("id_document_o_font") or ""))
            suport.append(es[0])
        if not millor[0] or (verif and not millor[2]):
            millor = (prova, suport, verif)
        if verif:
            break
    presents = sorted({p + (f"({n})" if n else "") for p, n in per_part})
    return millor[0], millor[1], ";".join(presents), millor[2]


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
               else "lot12" if "lot 12" in seccio else "lot16" if "lot 16" in seccio
               else "lot17" if "lot 17" in seccio else "lot10")
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
            antiga = (r.get("font_classificacio_cita") or "").strip() and \
                (r.get("font_classificacio_url") or "").strip()
            out["_c2_antic"] = bool(fun_es) or bool(antiga)
            if lab == "0":
                # P: prova completa per parts (decisió de Jordi del 24/11/2026, opció b)
                any_fila = int(r["any"])
                prova, suport, presents, verif_p = prova_P(fun_es, noms, any_fila)
                out["c2_parts"] = presents
                if prova:
                    out["c2_fundador"] = f"ok_prova_{prova}"
                    c2_ok = True
                    c2_suport = suport
                else:
                    antic = {"_cita_norm": norm(r.get("font_classificacio_cita") or ""), "notes": "",
                             "id_document_o_font": "(columna antiga)"} if antiga else None
                    prova2, suport2, presents2, _ = prova_P(fun_es + ([antic] if antic else []), noms, any_fila)
                    if prova2:
                        out["c2_fundador"] = "ok_columna_antiga"
                        out["c2_parts"] = presents2
                        c2_ok = True
                        c2_suport = [e for e in suport2 if e is not antic]
                    else:
                        out["c2_fundador"] = "prova_incompleta" if presents else "falta"
                        c2_suport = fun_es
            else:
                verif_p = None
                c2_suport = fun_es
                if fun_es:
                    out["c2_fundador"] = "ok_registre"
                    c2_ok = True
                elif antiga:
                    out["c2_fundador"] = "ok_columna_antiga"
                    c2_ok = True
                else:
                    out["c2_fundador"] = "falta"
        out["c1_ids"] = ids(c1_suport) if c1_suport else ""
        out["c2_ids"] = ids(c2_suport) if c2_suport else ""
        out.setdefault("c2_parts", "")

        # C3 arxiu (a les P, cada part de la prova amb una cita verificada a la captura)
        a1 = any(e.get("cita_verificada_a_captura") == "si" for e in c1_suport)
        if lab == "0" and out.get("c2_fundador", "").startswith("ok_prova_"):
            a2 = bool(verif_p)
        else:
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
    w = csv.DictWriter(buf, fieldnames=COLUMNES, lineterminator="\n", extrasaction="ignore")
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
    P = [f for f in S if f["FounderCEO"] == "0"]
    L.append("### C2 de les files P: prova de no fundador completa per parts\n")
    L.append("Decisió de Jordi del 24/11/2026 (opció b): un 0 només compta com a documentat si la prova té "
             "totes les parts, cadascuna amb la seva cita A/B. Parts: a llista de fundadors; e origen estatal "
             "o corporatiu; c any de fundació 64 anys o més abans; b any de fundació i naixement del CEO; "
             "d any de fundació i ocupador anterior del CEO.\n")
    antic = sum(1 for f in P if f.get("_c2_antic"))
    nou = sum(1 for f in P if "falta_fundador" not in f["estat"])
    L.append("| | Files P |")
    L.append("|---|---:|")
    L.append(f"| Amb alguna cita de fundador (criteri anterior al 24/11) | {pct(antic, len(P))} |")
    L.append(f"| Amb una prova completa per parts (criteri vigent) | {pct(nou, len(P))} |")
    for k in ("a", "e", "c", "b", "d"):
        L.append(f"| … prova {k} | {num(sum(f['c2_fundador'] == 'ok_prova_' + k for f in P))} |")
    L.append(f"| … només amb la cita de la columna antiga | {num(sum(f['c2_fundador'] == 'ok_columna_antiga' for f in P))} |")
    L.append(f"| Amb alguna part però sense cap prova completa | {num(sum(f['c2_fundador'] == 'prova_incompleta' for f in P))} |")
    L.append(f"| Sense cap part documentada | {num(sum(f['c2_fundador'] == 'falta' for f in P))} |")
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

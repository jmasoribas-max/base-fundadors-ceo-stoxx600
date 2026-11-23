#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica i importa al registre els resultats d'una cerca nova de cites de CEO.

Entrada: un o més CSV amb les columnes isin, any, ceo_esperat, resultat, url,
data_document, tipus_document, pagina, cita_literal, nivell, notes (format de la cerca
del grup F, 23/11/2026). `resultat` és trobat, interval_inici, interval_final,
no_trobat o discrepancia.

Per a cada fila trobada o d'interval:
  1. la cita ha d'anomenar el CEO de la fila (base) i contenir un títol de primer executiu;
  2. per a `trobat`, el document ha de ser de l'exercici (any de la fila o el següent);
     per a `interval_final`, posterior al 31/10 de l'any; un interval necessita les dues files;
  3. Claude torna a baixar el document de la URL i hi busca la cita literal (verificació
     independent). Si la re-descàrrega falla però la cita és al fitxer que va baixar la
     cerca (`--descarregues`), també compta com a [V] amb nota; si no, [NV] `pendent_arxiu`.
Les discrepàncies i les files no trobades van a `lots/lot{N}_dubtes.csv` i
`lots/lot{N}_pendents.csv`. Cap canvi de FounderCEO ni de `ceos`.

  python3 traspas/importa_cerca.py --lot 12 RESULTATS/*.csv            # prova en sec
  python3 traspas/importa_cerca.py --lot 12 RESULTATS/*.csv --escriu
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
BASE = ROOT / "dades" / "base_isin_any_v8r3.csv"
REG = ROOT / "docs" / "REGISTRE_CANVIS.csv"
FITXES = ROOT / "empreses"

spec = importlib.util.spec_from_file_location("importa_lot", ROOT / "traspas" / "importa_lot.py")
IL = importlib.util.module_from_spec(spec)
spec.loader.exec_module(IL)
EF = IL.EF


def data_ok_final(data: str, any_fila: int) -> bool:
    m = re.match(r"(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", data or "")
    if not m:
        return False
    y = int(m.group(1))
    mes = int(m.group(2)) if m.group(2) else None
    dia = int(m.group(3)) if m.group(3) else None
    if y > any_fila:
        return True
    if y == any_fila and mes is not None:
        return mes > 10 or (mes == 10 and dia is not None and dia >= 31)
    return False


def a_local(desc: Path | None, url: str, cita: str) -> bool:
    """Busca la cita en els fitxers baixats per la cerca (qualsevol fitxer de la carpeta)."""
    if not desc or not desc.is_dir():
        return False
    nc = IL.norm_text(cita)[:250]
    import subprocess
    for p in desc.rglob("*"):
        if not p.is_file() or p.stat().st_size == 0 or p.stat().st_size > 120_000_000:
            continue
        cap = p.read_bytes()[:5]
        try:
            if cap.startswith(b"%PDF"):
                t = subprocess.run(["pdftotext", "-q", str(p), "-"], capture_output=True, timeout=180).stdout.decode("utf-8", "ignore")
                t += "\n" + subprocess.run(["pdftotext", "-q", "-raw", str(p), "-"], capture_output=True, timeout=180).stdout.decode("utf-8", "ignore")
            elif p.suffix.lower() in (".html", ".htm", ".txt", ".xhtml", "") or cap.startswith(b"<"):
                t = p.read_bytes().decode("utf-8", "ignore")
                t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
                t = re.sub(r"<[^>]+>", " ", t)
            else:
                continue
        except Exception:  # noqa: BLE001
            continue
        nt = IL.norm_text(t)
        if nc and (nc in nt or re.sub(r"\s+", "", nc) in re.sub(r"\s+", "", nt)):
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("resultats", nargs="+")
    ap.add_argument("--lot", required=True)
    ap.add_argument("--escriu", action="store_true")
    ap.add_argument("--cache", default=str(ROOT / ".cache" / "baixades"))
    ap.add_argument("--descarregues", default="", help="carpeta amb els fitxers baixats per la cerca (opcional)")
    args = ap.parse_args()
    IL.CACHE = Path(args.cache)
    desc_arrel = Path(args.descarregues) if args.descarregues else None

    with BASE.open(encoding="utf-8", newline="") as f:
        base = {(r["isin"], r["any"]): r for r in csv.DictReader(f)}
    files = []
    for p in args.resultats:
        with open(p, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                r["_fitxer"] = Path(p).stem
                files.append(r)

    acceptades, dubtes, pendents, rebutjades = [], [], [], []
    per_fila = collections.defaultdict(list)
    for r in files:
        per_fila[(r["isin"].strip(), r["any"].strip())].append(r)

    for k, rs in sorted(per_fila.items()):
        if k not in base:
            rebutjades.append((k, "fila fora del panell"))
            continue
        noms = [n.strip() for n in (base[k].get("ceos") or "").split("|") if n.strip()]
        any_fila = int(k[1])
        bones = []
        for r in rs:
            res = (r.get("resultat") or "").strip()
            if res == "discrepancia":
                dubtes.append({**r, "motiu": "la cerca indica un altre CEO a 31/10"})
                continue
            if res not in ("trobat", "interval_inici", "interval_final"):
                continue
            cita = re.sub(r"\s+", " ", r.get("cita_literal") or "").strip()
            url = (r.get("url") or "").strip()
            if not cita or not url.lower().startswith("http"):
                rebutjades.append((k, "sense cita o URL"))
                continue
            nc = EF.norm(cita)
            if not any(EF.anomena(nc, n) for n in noms) and res != "interval_inici":
                rebutjades.append((k, f"la cita no anomena {base[k]['ceos']}"))
                continue
            if res != "interval_inici" and not EF.CARRECS.search(nc):
                rebutjades.append((k, "la cita no conté un títol de primer executiu"))
                continue
            if res == "trobat":
                y = IL.any_doc({"data_document": r.get("data_document") or ""})
                if y not in (any_fila, any_fila + 1):
                    rebutjades.append((k, f"document de {y}: no és de l'exercici"))
                    continue
            if res == "interval_final" and not data_ok_final(r.get("data_document") or "", any_fila):
                rebutjades.append((k, "document final de l'interval no posterior al 31/10"))
                continue
            bones.append({**r, "cita_literal": cita, "url": url})
        trobats = [r for r in bones if r["resultat"] == "trobat"]
        ini = [r for r in bones if r["resultat"] == "interval_inici"]
        fin = [r for r in bones if r["resultat"] == "interval_final"]
        if trobats:
            acceptades += trobats
        elif ini and fin:
            acceptades += ini + fin
        elif not any(d["isin"] == k[0] and d["any"] == k[1] for d in dubtes):
            pendents.append({"isin": k[0], "any": k[1], "falta": "ceo",
                             "notes": "; ".join((r.get("notes") or "")[:200] for r in rs)})

    # verificació independent
    resultat_ver = {}
    for r in acceptades:
        clau = (r["url"], r["cita_literal"])
        if clau in resultat_ver:
            continue
        est, det = IL.verifica(r["url"], r["cita_literal"])
        if est == "trobada":
            resultat_ver[clau] = ("[V]", "Claude (re-descàrrega del document original i cerca literal, 23/11/2026)", "")
        else:
            desc = desc_arrel / r["_fitxer"] if desc_arrel else None
            if a_local(desc, r["url"], r["cita_literal"]):
                resultat_ver[clau] = ("[V]", "Claude (cita literal comprovada al fitxer baixat per la cerca, 23/11/2026)",
                                      f"La re-descàrrega de Claude no ha pogut confirmar-la ({est}: {det}); la cita és al fitxer baixat de la mateixa URL durant la cerca.")
            else:
                resultat_ver[clau] = ("[NV]", "Claude (23/11/2026)", f"pendent_arxiu: re-descàrrega {est} ({det}).")

    c = collections.Counter(resultat_ver[(r["url"], r["cita_literal"])][0] for r in acceptades)
    files_cobertes = {(r["isin"], r["any"]) for r in acceptades if resultat_ver[(r["url"], r["cita_literal"])][0] == "[V]"}
    print(f"Files als resultats: {len(per_fila)}; files amb cita acceptada [V]: {len(files_cobertes)}; "
          f"cites acceptades: {len(acceptades)} {dict(c)}; dubtes: {len(dubtes)}; pendents: {len(pendents)}; rebutjades: {len(rebutjades)}")
    for k, m in rebutjades[:40]:
        print(f"  rebutjada {k}: {m}")
    if not args.escriu:
        print("Prova en sec: no s'ha escrit res.")
        return 0

    with REG.open(encoding="utf-8", newline="") as f:
        rcap = next(csv.reader(f))
    crlf = b"\r\n" in REG.read_bytes()[:4000]
    grups = collections.OrderedDict()
    for r in sorted(acceptades, key=lambda r: (r["isin"], r["resultat"], r["url"], r["any"])):
        g = grups.setdefault((r["isin"], r["url"], r["cita_literal"], r["resultat"]), {"r": r, "anys": []})
        g["anys"].append(int(r["any"]))
    comptador = collections.Counter()
    noves, per_isin = [], collections.defaultdict(list)
    for (isin, url, cita, res), g in grups.items():
        r = g["r"]
        comptador[isin] += 1
        ident = f"L{args.lot}-{isin}-C{comptador[isin]:02d}"
        k0 = (isin, str(min(g["anys"])))
        b = base[k0]
        marques = b.get("marques") or ""
        if res.startswith("interval"):
            marca = "ceo_interval"
        else:
            marca = "R2" if "interi" in marques else ("R3" if "ceo_president_exec" in marques or "de_facto" in marques else "R1")
        v = resultat_ver[(url, cita)]
        notes = [f"Cerca nova de la cita de CEO ({r['_fitxer']}, 23/11/2026)."]
        if res == "interval_inici":
            notes.append("inici: nomenament (regla 28).")
        elif res == "interval_final":
            notes.append("final: document posterior al 31/10 (regla 28).")
        notes.append(f"Document: {r.get('tipus_document') or '?'}, {r.get('data_document') or 'sense data'}, pàgina {r.get('pagina') or '?'}.")
        notes.append(f"Nivell {r.get('nivell') or '?'}.")
        if r.get("notes"):
            notes.append("Nota de la cerca: " + re.sub(r"\s+", " ", r["notes"])[:300])
        if IL.es_agregador(url):
            notes.append("agregador=true: cal substituir-la per la còpia de l'emissor si existeix.")
        if v[2]:
            notes.append(v[2])
        fila = {kk: "" for kk in rcap}
        fila.update({
            "tipus": "evidencia_ceo", "grup_id": f"L{args.lot}-{isin}", "isin": isin, "nom": b.get("nom_panell", ""),
            "anys": IL.blocs(g["anys"]), "n_files": str(len(set(g["anys"]))),
            "origen": f"proposta_claude_lot{args.lot}", "estat_certificacio": b.get("sim_estat_certificacio", ""),
            "cita_literal": cita, "url_font": url, "id_document_o_font": ident, "origen_cita": "cerca_nova",
            "model_verificacio": v[1], "marca_veritat": v[0], "notes": " ".join(notes),
            "allotjament": IL.allotjament(url, r.get("nivell") or "A"), "funcio_cita": "ceo", "marca_prova": marca,
        })
        noves.append(fila)
        per_isin[isin].append(fila)
    with REG.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rcap, lineterminator="\r\n" if crlf else "\n")
        w.writerows(noves)
    for isin, fs in per_isin.items():
        p = FITXES / f"{isin}.md"
        text = p.read_text(encoding="utf-8").rstrip("\n")
        L = [f"\n## Lot {args.lot} · Cerca nova de cites de CEO\n"]
        for fl in fs:
            L.append(f"- **{fl['id_document_o_font']}** · {fl['anys']} · {fl['marca_veritat']} · `{fl['marca_prova']}`. "
                     f"«{fl['cita_literal']}» [Font original]({fl['url_font']}).")
        p.write_text(text + "\n" + "\n".join(L) + "\n", encoding="utf-8")
    for nom, dades, cols in ((f"lot{args.lot}_dubtes.csv", dubtes, ["isin", "any", "ceo_esperat", "motiu", "url", "data_document", "cita_literal", "notes"]),
                             (f"lot{args.lot}_pendents.csv", pendents, ["isin", "any", "falta", "notes"])):
        with (ROOT / "lots" / nom).open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
            w.writeheader()
            w.writerows(dades)
    print(f"Escrit: {len(noves)} entrades al registre, {len(per_isin)} fitxes, lots/lot{args.lot}_dubtes.csv i _pendents.csv.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

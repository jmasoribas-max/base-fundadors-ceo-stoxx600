#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica a la base un fitxer de canvis aprovat (p. ex. lots/correccio1_canvis.csv).

Format del fitxer de canvis (CSV): id_canvi, isin, any, nom, camp, valor_actual,
valor_proposat, motiu, font_decisio, aprovacio.

Per defecte NO escriu res: comprova que cada `valor_actual` coincideix amb el valor
d'ara al CSV i a l'xlsx de la base i mostra el resum. Amb --aplica:

  1. canvia les cel·les al CSV (mantenint el format: CRLF, cometes mínimes) i a l'xlsx;
  2. afegeix al registre una entrada `tipus=correccio_coherencia` per ISIN, camp i
     bloc de valors (amb `de`, `a`, anys i la referència als id_canvi);
  3. afegeix a cada fitxa `empreses/{ISIN}.md` una secció amb els canvis, sense esborrar res.

Després cal regenerar l'estat (estat/estat_files.py), el dashboard si escau i el manifest.
Només s'ha d'executar amb --aplica quan Jordi hagi aprovat el lot.

  python3 estat/aplica_canvis.py lots/correccio1_canvis.csv
  python3 estat/aplica_canvis.py lots/correccio1_canvis.csv --aplica --origen correccio1_claude
"""
from __future__ import annotations

import argparse
import collections
import csv
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "dades" / "base_isin_any_v8r3.csv"
XLSX = ROOT / "dades" / "base_isin_any_v8r3.xlsx"
REG = ROOT / "docs" / "REGISTRE_CANVIS.csv"
FITXES = ROOT / "empreses"


def llegeix_base() -> tuple[list[str], list[list[str]]]:
    raw = BASE.read_bytes().decode("utf-8")
    files = list(csv.reader(io.StringIO(raw, newline="")))
    return files[0], files[1:]


def escriu_base(cap: list[str], files: list[list[str]]) -> None:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\r\n")
    w.writerow(cap)
    w.writerows(files)
    BASE.write_bytes(buf.getvalue().encode("utf-8"))


def blocs(anys: list[int]) -> str:
    anys = sorted(anys)
    trossos, ini, prev = [], anys[0], anys[0]
    for a in anys[1:] + [None]:
        if a is not None and a == prev + 1:
            prev = a
            continue
        trossos.append(str(ini) if ini == prev else f"{ini}-{prev}")
        if a is not None:
            ini = prev = a
    return ",".join(trossos)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("canvis")
    ap.add_argument("--aplica", action="store_true")
    ap.add_argument("--origen", default="", help="valor de la columna origen del registre (obligatori amb --aplica)")
    args = ap.parse_args()
    path = (ROOT / args.canvis) if not Path(args.canvis).is_absolute() else Path(args.canvis)
    with path.open(encoding="utf-8", newline="") as f:
        canvis = list(csv.DictReader(f))

    cap, files = llegeix_base()
    col = {c: i for i, c in enumerate(cap)}
    idx = {(r[col["isin"]], r[col["any"]]): r for r in files}

    import openpyxl
    wb = openpyxl.load_workbook(XLSX)
    ws = wb[wb.sheetnames[0]]
    xcap = [c.value for c in ws[1]]
    xcol = {c: i + 1 for i, c in enumerate(xcap)}
    xrow = {}
    for i, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        xrow[(str(row[xcol["isin"] - 1]), str(row[xcol["any"] - 1]))] = i

    errors = []
    for c in canvis:
        k = (c["isin"], c["any"])
        if c["camp"] not in col or c["camp"] not in xcol:
            errors.append(f"{c['id_canvi']}: camp desconegut {c['camp']}")
            continue
        if k not in idx or k not in xrow:
            errors.append(f"{c['id_canvi']}: fila inexistent {k}")
            continue
        actual = idx[k][col[c["camp"]]]
        xactual = ws.cell(row=xrow[k], column=xcol[c["camp"]]).value
        xactual = "" if xactual is None else str(xactual)
        if actual != c["valor_actual"]:
            errors.append(f"{c['id_canvi']}: el CSV diu {actual!r}, el fitxer de canvis {c['valor_actual']!r}")
        if xactual != c["valor_actual"]:
            errors.append(f"{c['id_canvi']}: l'xlsx diu {xactual!r}, el fitxer de canvis {c['valor_actual']!r}")

    per_camp = collections.Counter(c["camp"] for c in canvis)
    print(f"Canvis: {len(canvis)} ({dict(per_camp)}); files afectades: {len({(c['isin'], c['any']) for c in canvis})}")
    if errors:
        print(f"Errors: {len(errors)}")
        for e in errors:
            print("  - " + e)
        return 1
    print("OK: tots els valor_actual coincideixen amb el CSV i l'xlsx.")
    if not args.aplica:
        print("Prova en sec: no s'ha escrit res (afegeix --aplica per aplicar-ho).")
        return 0
    if not args.origen:
        print("Cal --origen amb --aplica.")
        return 2

    for c in canvis:
        k = (c["isin"], c["any"])
        idx[k][col[c["camp"]]] = c["valor_proposat"]
        ws.cell(row=xrow[k], column=xcol[c["camp"]]).value = c["valor_proposat"]
    escriu_base(cap, files)
    wb.save(XLSX)

    with REG.open(encoding="utf-8", newline="") as f:
        rcap = next(csv.reader(f))
    grups = collections.defaultdict(list)
    for c in canvis:
        grups[(c["isin"], c["camp"], c["valor_actual"], c["valor_proposat"])].append(c)
    noves = []
    for (isin, camp, de, a), cs in sorted(grups.items()):
        anys = [int(c["any"]) for c in cs]
        fila = {k: "" for k in rcap}
        fila.update({
            "tipus": "correccio_coherencia",
            "grup_id": f"{args.origen}-{isin}-{camp}",
            "isin": isin,
            "nom": cs[0]["nom"],
            "anys": blocs(anys),
            "n_files": str(len(anys)),
            "de": f"{camp}={de}",
            "a": f"{camp}={a}",
            "decisio": cs[0]["aprovacio"],
            "origen": args.origen,
            "estat_certificacio": idx[(isin, cs[0]["any"])][col["sim_estat_certificacio"]],
            "id_document_o_font": ";".join(c["id_canvi"] for c in cs),
            "model_verificacio": "Claude (script estat/aplica_canvis.py)",
            "marca_veritat": "[V]",
            "notes": f"{cs[0]['motiu']} Font de la decisió: {cs[0]['font_decisio']}",
        })
        noves.append(fila)
    with REG.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rcap, lineterminator="\r\n" if b"\r\n" in REG.read_bytes()[:4000] else "\n")
        w.writerows(noves)

    per_isin = collections.defaultdict(list)
    for c in canvis:
        per_isin[c["isin"]].append(c)
    for isin, cs in per_isin.items():
        p = FITXES / f"{isin}.md"
        text = p.read_text(encoding="utf-8")
        linies = [f"\n## Correcció de coherència ({args.origen})\n",
                  "Canvis aplicats a `dades/base_isin_any_v8r3.csv` amb l'OK de Jordi. Detall a "
                  "`lots/` i a `docs/REGISTRE_CANVIS.csv`.\n"]
        for c in sorted(cs, key=lambda x: (x["camp"], x["any"])):
            linies.append(f"- **{c['id_canvi']}** · {c['any']} · `{c['camp']}`: «{c['valor_actual']}» → "
                          f"«{c['valor_proposat']}». {c['motiu']}")
        p.write_text(text.rstrip("\n") + "\n" + "\n".join(linies) + "\n", encoding="utf-8")
    print(f"Aplicat: CSV, xlsx, {len(noves)} entrades al registre i {len(per_isin)} fitxes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

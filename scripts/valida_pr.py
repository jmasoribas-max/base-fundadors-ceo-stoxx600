#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validador de PR i de l'arbre del repositori v8 r2.

Comprova el format de les fitxes, els valors permesos, les cites literals,
la coherència de l'índex amb la base i els enllaços interns.

En un PR (si git és disponible i hi ha `main` amb historial), comprova a més
que els canvis a dades/ portin canvis al registre i a les fitxes afectades,
i que no s'estigui treballant a main.

Per defecte no fa cap petició de xarxa (sense --live).
S'ha d'executar i ha de passar abans d'obrir el PR. No fusiona res.

  python3 scripts/valida_pr.py
"""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "dades" / "base_isin_any_v8r3.csv"
INDEX_CSV = ROOT / "index.csv"
INDEX_MD = ROOT / "INDEX.md"
FITXES = ROOT / "empreses"
REG_CSV = ROOT / "docs" / "REGISTRE_CANVIS.csv"
PENDENTS = ROOT / "PENDENTS.md"

FOUNDERCEO_OK = {"1", "0", "no_determinat", "NA_sense_ceo"}
ESTAT_SECTOR_OK = {
    "amb_sector",
    "revisar",
    "pendent_extensio_2024_2025",
    "revisar_pendent_extensio_2024_2025",
    "sense_sector",
}
ESTAT_CERT_OK = {
    "certificada",
    "certificada_ceo_pendent",
    "no_certificada",
    "fora_mostra_auditoria",
}
NIVELL_OK = {"N1", "N2", "doctorat", ""}
CAPSALERES_FITXA = [
    "## Sèrie anual",
    "## Cites (URL original i Wayback)",
    "## Canvis del registre",
    "## Pendències d'aquesta empresa",
]
MD_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
URL_RE = re.compile(r"^https?://", re.I)
WB_RE = re.compile(r"^https?://web\.archive\.org/web/", re.I)
ISIN_RE = re.compile(r"^[A-Z]{2}[A-Z0-9]{10}$")
PENDENTS_WB = {"", "pendent_verificacio_externa", "—", "-", "na", "n/a"}


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )


def current_branch() -> str | None:
    r = git("rev-parse", "--abbrev-ref", "HEAD")
    if r.returncode != 0:
        return None
    return r.stdout.strip() or None


def changed_vs_main() -> list[str]:
    if git("rev-parse", "--verify", "main").returncode != 0:
        return []
    r = git("diff", "--name-only", "main...HEAD")
    if r.returncode != 0:
        r = git("diff", "--name-only", "main")
    if r.returncode != 0:
        return []
    return [ln.strip() for ln in r.stdout.splitlines() if ln.strip()]


def add(problems: list[str], msg: str) -> None:
    problems.append(msg)


def main() -> int:
    argparse.ArgumentParser(
        description="Valida l'arbre o el PR (sense --live, no fusiona)."
    ).parse_args()
    problems: list[str] = []

    if not BASE.exists():
        add(problems, f"no trobo la base {BASE.relative_to(ROOT)}")
        print_report(problems)
        return 2

    with BASE.open(encoding="utf-8", newline="") as f:
        base_rows = list(csv.DictReader(f))
    if len(base_rows) != 6012:
        add(problems, f"la base té {len(base_rows)} files, n'esperava 6.012")
    isins = sorted({r["isin"] for r in base_rows})
    if len(isins) != 1040:
        add(problems, f"la base té {len(isins)} ISIN, n'esperava 1.040")

    for i, r in enumerate(base_rows, start=2):
        ident = f"dades/base_isin_any_v8r3.csv:{i} {r.get('isin')} {r.get('any')}"
        if r.get("FounderCEO") not in FOUNDERCEO_OK:
            add(problems, f"{ident}: FounderCEO no permès: {r.get('FounderCEO')!r}")
        if r.get("estat_sector") not in ESTAT_SECTOR_OK:
            add(problems, f"{ident}: estat_sector no permès: {r.get('estat_sector')!r}")
        if r.get("sim_estat_certificacio") not in ESTAT_CERT_OK:
            add(problems, f"{ident}: sim_estat_certificacio no permès: {r.get('sim_estat_certificacio')!r}")
        if r.get("sim_nivell", "") not in NIVELL_OK:
            add(problems, f"{ident}: sim_nivell no permès: {r.get('sim_nivell')!r}")
        if not ISIN_RE.match(r.get("isin") or ""):
            add(problems, f"{ident}: ISIN amb forma inesperada")

    # Fitxes
    if not FITXES.is_dir():
        add(problems, "falta el directori empreses/")
        fitxes = []
    else:
        fitxes = sorted(FITXES.glob("*.md"))
    noms_fitxa = {p.stem for p in fitxes}
    if len(fitxes) != 1040:
        add(problems, f"hi ha {len(fitxes)} fitxes, n'esperava 1.040")
    falta = [i for i in isins if i not in noms_fitxa]
    sobra = sorted(noms_fitxa - set(isins))
    if falta:
        add(problems, f"falten {len(falta)} fitxes, p. ex. {falta[:5]}")
    if sobra:
        add(problems, f"hi ha {len(sobra)} fitxes sense ISIN a la base, p. ex. {sobra[:5]}")

    for p in fitxes:
        text = p.read_text(encoding="utf-8")
        if f"`{p.stem}`" not in text and p.stem not in text:
            add(problems, f"empreses/{p.name}: no hi figura l'ISIN")
        for cap in CAPSALERES_FITXA:
            if cap not in text:
                add(problems, f"empreses/{p.name}: falta la capçalera {cap!r}")

    # index.csv
    if not INDEX_CSV.exists():
        add(problems, "falta index.csv")
        idx_rows = []
    else:
        with INDEX_CSV.open(encoding="utf-8", newline="") as f:
            idx_rows = list(csv.DictReader(f))
    idx_isins = [r.get("isin", "") for r in idx_rows]
    if len(idx_rows) != 1040:
        add(problems, f"index.csv té {len(idx_rows)} files, n'esperava 1.040")
    if set(idx_isins) != set(isins):
        add(problems, "index.csv no té el mateix conjunt d'ISIN que la base")
    for r in idx_rows:
        isin = r.get("isin", "")
        fitxa = r.get("fitxa", f"empreses/{isin}.md")
        path = (ROOT / fitxa).resolve()
        if not path.exists():
            add(problems, f"index.csv: no existeix la fitxa {fitxa}")

    # INDEX.md enllaços a fitxes
    if not INDEX_MD.exists():
        add(problems, "falta INDEX.md")
    else:
        text_idx = INDEX_MD.read_text(encoding="utf-8")
        linked = set(re.findall(r"empreses/([A-Z0-9]+)\.md", text_idx))
        if linked != set(isins):
            add(
                problems,
                f"INDEX.md enllaça {len(linked)} ISIN; la base en té {len(isins)}",
            )

    # Enllaços interns markdown (relatius, existents)
    md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    for p in md_files:
        text = p.read_text(encoding="utf-8")
        for m in MD_LINK.finditer(text):
            dest = m.group(1).strip()
            if dest.startswith(("http://", "https://", "mailto:", "#")):
                continue
            dest = dest.split("#", 1)[0].split("?", 1)[0]
            if not dest:
                continue
            target = (p.parent / dest).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                add(problems, f"{p.relative_to(ROOT)}: enllaç fora del repo: {dest}")
                continue
            if not target.exists():
                add(problems, f"{p.relative_to(ROOT)}: enllaç intern trencat: {dest}")

    # Cites literals al registre
    if REG_CSV.exists():
        with REG_CSV.open(encoding="utf-8", newline="") as f:
            for i, row in enumerate(csv.DictReader(f), start=2):
                cita = (row.get("cita_literal") or "").strip()
                url = (row.get("url_font") or "").strip()
                wb = (row.get("url_wayback") or "").strip()
                marca = row.get("marca_veritat") or ""
                ident = f"docs/REGISTRE_CANVIS.csv:{i} {row.get('isin')}"
                if url and not cita and marca != "[NV]":
                    add(problems, f"{ident}: URL sense cita literal")
                if url and not URL_RE.search(url):
                    add(problems, f"{ident}: url_font amb forma no vàlida")
                if wb and wb.lower() not in PENDENTS_WB and not WB_RE.search(wb):
                    add(problems, f"{ident}: url_wayback amb forma no vàlida")
    else:
        add(problems, "falta docs/REGISTRE_CANVIS.csv")

    if not PENDENTS.exists():
        add(problems, "falta PENDENTS.md")

    # Regles de branca / PR
    branch = current_branch()
    if branch == "main":
        changed = changed_vs_main()
        # Al commit inicial no hi ha diff contra main; només alertem si
        # l'arbre de treball té canvis locals a dades/ després del commit.
        dirty = git("status", "--porcelain")
        dirty_lines = [ln[3:].strip() for ln in dirty.stdout.splitlines()] if dirty.returncode == 0 else []
        dades_dirty = [p for p in dirty_lines if p.startswith("dades/")]
        if dades_dirty:
            add(
                problems,
                "s'està a main amb canvis a dades/: cal una branca i un PR; Claude no pot tocar main",
            )
    else:
        changed = changed_vs_main()
        if changed:
            dades_ch = [p for p in changed if p.startswith("dades/")]
            if dades_ch:
                if not any(p.startswith("docs/REGISTRE_CANVIS") for p in changed):
                    add(
                        problems,
                        "el PR modifica dades/ però no docs/REGISTRE_CANVIS (cal cita, URL i Wayback)",
                    )
                if not any(p.startswith("empreses/") for p in changed):
                    add(
                        problems,
                        "el PR modifica dades/ però no cap fitxa a empreses/",
                    )

    print_report(problems)
    return 1 if problems else 0


def print_report(problems: list[str]) -> None:
    print(f"Problemes: {len(problems)}")
    for msg in problems:
        print(f"  - {msg}")
    if not problems:
        print("OK: valida_pr ha passat (sense --live).")


if __name__ == "__main__":
    raise SystemExit(main())

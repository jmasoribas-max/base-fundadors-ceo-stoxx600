# Apply the independent verifier's corrections to founding records (lot 18, correction pass)

Context: PhD evidence database on founder-CEOs (STOXX Europe 600). The rules are in CLAUDE.md, which you already have. Read in particular:
- proofs a-e;
- the «Decisió de Jordi del 24/11/2026» sections (proof by parts; P8 single founder);
- P1-P4 of rule 25;
- rule 26 (strict D1).

For each company, a research agent built a "founding record" in `cerca_fund/resultats/<g>_cites.csv` (one row per quote) and `<g>_resum.csv` (one row per company). An independent verifier then marked the company **corregir**, with its reasons in `<g>_verif.csv`:
- `motiu`: why;
- `cites_dolentes`: the first 60 characters of the quotes to drop, separated by ||;
- `correccio`: what to change.

Your batch is a JSON list of [group, isin] pairs: `cerca_fund/correccions/lot{N}.json`. All paths are relative to the scratchpad `{S}`.

## For each company

1. Read its verif row, its quote rows and its summary row.
2. Apply ONLY the corrections that need **no new web search**:
   - drop the quotes listed in `cites_dolentes`, and any quote the `correccio` says to drop;
   - relabel a quote's `part` when the correction says so (e.g. `origen_entitat` → `cadena`, `llista_fundadors` → `any_fundacio`);
   - fix `fundadors`, `any_fundacio`, `singular`, `tipus_origen`, `entitat_rellevant` and `dubte` in the summary row as the correction says;
   - if the correction asks to ADD a quote that is in a file **already downloaded** (`cerca_fund/descarregues/<g>/`), you may add it. Copy it exactly from the file and check it with `python3 -I {S}/cerca_fund/cerca.py FILE REGEX`. Big PDFs were converted to text and are now `<name>.pdf.txt`; grep or cerca.py work on those too. Give the page if known.
3. Decide the company's status:
   - `ok`: all corrections applied, and the record is coherent with the rules;
   - `pendent`: some correction needs a new web search, a methodology decision by Jordi, or data you do not have. Say what is missing.

## Output (python csv module, UTF-8)

- `cerca_fund/correccions/lot{N}_cites.csv`: same columns as `<g>_cites.csv`, plus a final column `grup`. It contains the corrected quote rows of every company you mark `ok`.
- `cerca_fund/correccions/lot{N}_resum.csv`: same columns as `<g>_resum.csv`, plus `grup`. One corrected summary row per company marked `ok`.
- `cerca_fund/correccions/lot{N}_verif.csv`, with columns `isin,veredicte,motiu,cites_dolentes,correccio`:
  - `veredicte` = `ok` or `pendent`;
  - `motiu` = what you changed (for `ok`) or what is missing (for `pendent`);
  - `cites_dolentes` empty.

## Rules

- Do not modify the original research or verif files.
- Do not invent quotes, years or names.
- Do not download anything new.
- When done, reply with the counts: ok, pendent, quotes dropped, quotes relabelled, quotes added.

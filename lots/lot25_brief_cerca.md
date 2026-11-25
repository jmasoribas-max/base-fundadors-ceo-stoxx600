# Lot 25 (pas 3c): open cases, search without attempt limit (A.4)

**Context.** This is a PhD evidence database on founder-CEOs in the STOXX Europe 600. The rules are in CLAUDE.md, which you already have. Read in particular:
- proofs a-e;
- «Decisió de Jordi del 24/11/2026»: a 0 needs EVERY part of its proof, each with its own A/B quote;
- rule 25 P1-P9, especially **P3**;
- rule 26 (strict D1) and rule 21b;
- the evening decisions of 24/11.

This is research only: do not edit any git repository.

**Input:** `(carpeta de treball de Claude)/pas3c/entrada/v{N}.csv`, about 24 companies. In every row the CEOs are classified as NOT founders, but a script says the proof is still incomplete. The columns are:
- `ceos_anys`: each CEO and the panel years still open;
- `origen_corporatiu_sense_P3`: filled if a registered quote says another company created this one. Proof e then also needs the P3 check (see below);
- `parts_registrades`: proof parts already in the database, with their entry IDs, in the same tag format you will write;
- `parts_rebutjades_literalitat`: parts that do NOT count, because the value is not in the quote itself (see "Literal rule"). Find a quote that states the value literally;
- `anys_anul_lats`: registered founding years that were rejected (P1/D1);
- `pas3_*`: what the previous search (step 3) concluded and looked at. Do not repeat it; try other sources.

## How the script decides (so you know what is missing)

For each CEO, one complete proof:
- **a:** a closed founders list (`tancada=si`) of the company or a D1/D10 predecessor that does not include the CEO.
- **e:**
  - an origin from the State (State, law, decree, public body, municipalities). This closes the proof for every CEO.
  - Or an origin from another company PLUS the **P3 check**: the CEO cannot be a founder of that parent. Any one of these closes it:
    1. the parent was itself created by the State, tagged `[part origen_entitat=...; entitat=matriu]`;
    2. a closed founders list of the parent that does not include the CEO, tagged `[part llista_fundadors=...; entitat=matriu; tancada=si]`;
    3. proof b on the parent: the parent's founding year minus the CEO's birth year is under 18. Tag the year `[part any_fundacio=YYYY; entitat=matriu]`; the CEO's birth year must also be registered or found.

    For a joint venture or several parents, give the founding year of **each** parent. The script uses the most recent one.
- **b:** F − CEO birth year < 18, where F is the most recent valid founding year of the company or of its operating business (P7).
- **d:** CEO entry year − F ≥ 3, plus a named prior employer.
- **c** (reserve, only with no birth year): start of mandate − F ≥ 64.

## Literal rule (enforced by script)

A part counts only if the quote itself states the value:
- **founding year:** the 4-digit year must be in the quote, tied to a founding verb about that entity;
- **entry or start of mandate:** the year must be in the quote, or be the year of the document date;
- **birth:** either the birth year is in the quote, or an age is in the quote and the document date is known. Then the tag is `document year − age − 1`, the earliest possible year.

Each quote must be literal, 1-3 sentences, copied exactly, not translated.

## What to do, per company, in this order

1. If `origen_corporatiu_sense_P3` is filled, close **P3**. Usually this only needs one founding-year quote per parent, often the parent's own history page or annual report, plus the CEO's birth year if it is not yet registered.
2. Otherwise, or if P3 cannot be closed, use **b or d on the company itself**:
   - the founding year of the relevant entity, if it is missing or was rejected;
   - the CEO birth year;
   - or the prior employer plus the entry year.
3. Replace any part in `parts_rebutjades_literalitat` that the proof needs with a quote that states the value literally.
4. **Founder check.** If any source says a CEO founded the company or a D1/D10 predecessor, report it as `ceo_fundador`. Do not hide it.

## Sources

- **A:** issuer documents, regulators and registers. UK Companies House officer pages (month and year of birth) count as a register.
- **B:** quality press, books, academic articles.
- **Not allowed:** Wikipedia, LinkedIn, Crunchbase, Bloomberg or Reuters profile pages, and aggregators (marketscreener, zonebourse, annualreports.com, companiesmarketcap). These can only be hints.
- **Tools** (in `(carpeta de treball de Claude)/cerca_fund`):
  - `dl.sh URL OUTPATH` downloads with plain curl. Save to `(carpeta de treball de Claude)/pas3c/descarregues/v{N}/`.
  - `python3 -I cerca.py FILE REGEX` finds a quote.

  The final URL must download with plain curl, because it will be re-downloaded and the quote checked by script.
- No `curl -k`, no logins, no antibot circumvention, no spoofed headers (no browser user agent, no Referer). If a site blocks plain curl, use another source. Do not invent anything.

## Output 1: quotes

Write `(carpeta de treball de Claude)/pas3c/resultats/v{N}_cites.csv` with the python csv module, one row per quote. Columns:

`isin,anys,funcio_cita,marca_prova,part,persona,url,data_document,tipus_document,pagina,cita_literal,nivell,allotjament,notes`

- `anys`:
  - company and parent parts: all open years of the company;
  - person parts: that CEO's open years.
- `funcio_cita`: `fundador`.
- `marca_prova`: `a`, `e`, `b`, `c` or `d`.
- `data_document`: YYYY-MM-DD or YYYY. Always give it when you rely on an age.
- `nivell`: `A` or `B`.
- `allotjament`: `emissor`, `regulador`, `grup`, `successor`, `plataforma` or `mitja`.
- `notes`: MUST start with exactly one structured tag:
  - `[part any_fundacio=1923; entitat=emissor]`. `entitat` is `emissor`, `predecessora` or `matriu`.
  - `[part naixement_ceo=Firstname Lastname:1965]`
  - `[part llista_fundadors=Name One + Name Two; entitat=matriu; tancada=si]`
  - `[part origen_entitat=Creator; entitat=matriu]`
  - `[part ocupador_anterior=Firstname Lastname:Employer:YYYY]`. YYYY is the year they joined the company.
  - `[part entrada=Firstname Lastname:YYYY]`
  - `[part inici_mandat=Firstname Lastname:YYYY]`

  After the tag, say where the quote is and give your reasoning (P1/P3/D1 etc.). If a registered founding year is not a founding (P1/D1), write `ANUL·LAR any_fundacio=YYYY` and the reason in the resum notes.

## Output 2: one row per company

Write `(carpeta de treball de Claude)/pas3c/resultats/v{N}_resum.csv`. Columns:

`isin,resultat,que_s_ha_mirat,dubte,notes`

- `resultat`: `tancat` (every open year has a complete proof with your quotes plus the registered parts), `parcial` or `no_trobat`.
- `dubte`: empty or a short label: `D1`, `P1`, `P3`, `contradiccio` or `ceo_fundador`.

Rewrite both CSVs after each company. Before finishing, re-check every quote with `cerca.py` against the downloaded file. End with a 10-line report: counts per `resultat`, and any `dubte` cases.

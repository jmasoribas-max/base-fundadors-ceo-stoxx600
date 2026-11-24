# Pas 3: close the non-founder proof for professional CEOs (research)

**Context.** This is a PhD evidence database on founder-CEOs in the STOXX Europe 600. The rules are in CLAUDE.md, which you already have. Read in particular:
- proofs a-e;
- «Decisió de Jordi del 24/11/2026» (a 0 needs EVERY part of its proof, each with its own A/B quote);
- rule 25 (P1-P9);
- rule 26 (strict D1);
- the evening decisions of 24/11.

This is research only: do not edit any git repository.

**Input:** `(carpeta de treball de Claude)/pas3/entrada/t{N}.csv`, about 20 companies. In every row the CEOs are classified as NOT founders, but the proof is incomplete. The columns are:
- `ceos_anys`: CEOs and the panel years still open;
- `any_fundacio_registrat`: founding years already in the database, if any;
- `falta_any_fundacio`: `si` if no founding year is registered;
- `falta_naixement`: CEOs with no registered birth year;
- `fitxa_*` and `verificador`: what an earlier search found about the founding, and the doubts an independent checker raised. Read these: they tell you which entity counts and what was wrong.

## What to find, in this order, for each company

1. **Shortcut: proof a or e.**
   - **Proof a:** if you can quickly find an A/B quote that names ALL the founders of the relevant entity, and none of the CEOs is among them, that closes every year.
   - **Proof e:** a quote that the State or another company created it closes every year too, unless the creator was founded by natural persons (P3). In that case, also give the parent's founders.
   - If the earlier search failed at this, do not spend long on it.
2. **Founding year of the relevant entity** (only if `falta_any_fundacio=si`). The quote must give the year and a founding verb, about this company or its operating business.
   - New holdings, renamings, IPOs and redomiciliations do not count (P1).
   - For a merger, apply strict D1 (rule 26): if it is a real merger of equals, give the founding years of all parties. If it is an acquisition, give the year of the absorbing party, or of the party the CEO came from (J1).
   - Note your reasoning in `notes`.
3. **Birth year of each CEO in `falta_naixement`.**
   - Typical A sources:
     - directors' biographies in the annual report or corporate governance report ("born 1965", "aged 54");
     - the AGM notice;
     - the prospectus;
     - UK Companies House officer pages (month/year of birth), which count as a register (A).
   - B sources: quality financial press.
   - An age is fine only if the document date is known. Then give the earliest possible birth year: document year − age − 1.
4. **Proof d, only if the birth year cannot be found.** Give the CEO's prior employer and the year the CEO joined the company, at least 3 years after the founding, with a quote.

## Sources

- **A:** issuer documents, regulators and registers. **B:** quality press, books, academic articles.
- **Not allowed:** Wikipedia, LinkedIn, Crunchbase, Bloomberg or Reuters profile pages, and aggregators (marketscreener, zonebourse, annualreports.com, companiesmarketcap). These can only serve as hints.
- **Tools** (in `(carpeta de treball de Claude)/cerca_fund`):
  - `dl.sh URL OUTPATH` downloads to `(carpeta de treball de Claude)/pas3/descarregues/t{N}/`;
  - `python3 -I cerca.py FILE REGEX` checks a quote.
- Copy each quote EXACTLY: 1-3 sentences, no translation. The final URL must download with plain curl, because it will be re-downloaded and the quote checked by script.
- No `curl -k`, no logins, no antibot circumvention, no spoofed headers. Do not invent anything.

## Output 1: quotes

Write `(carpeta de treball de Claude)/pas3/resultats/t{N}_cites.csv` with the python csv module, one row per quote. Columns:

`isin,anys,funcio_cita,marca_prova,part,persona,url,data_document,tipus_document,pagina,cita_literal,nivell,allotjament,notes`

- `anys`: the panel years the quote supports.
  - Company parts (founding, founders list, origin): all open years of the company.
  - Person parts: that CEO's open years.
- `funcio_cita`: `fundador`.
- `marca_prova`: `a`, `e`, `b`, `c` or `d`.
- `part`: one of `llista_fundadors`, `origen_entitat`, `any_fundacio`, `naixement_ceo`, `ocupador_anterior`, `entrada`, `inici_mandat`.
- `nivell`: `A` or `B`. `allotjament`: `emissor`, `regulador`, `grup`, `successor`, `plataforma` or `mitja`.
- `notes`: MUST contain one structured tag, exactly in this format:
  - `[part any_fundacio=1923; entitat=emissor]`. `entitat` is `emissor` or `predecessora`.
  - `[part naixement_ceo=Firstname Lastname:1965]`
  - `[part llista_fundadors=Name One + Name Two; entitat=emissor; tancada=si]`. `tancada` is `si` only if the quote presents the whole set.
  - `[part origen_entitat=Creator; entitat=emissor]`
  - `[part ocupador_anterior=Firstname Lastname:Employer:YYYY]`. YYYY is the year they joined the company.
  - `[part inici_mandat=Firstname Lastname:YYYY]`

  After the tag, add where the quote is and your reasoning (P1/D1 etc.).

## Output 2: one row per company

Write `(carpeta de treball de Claude)/pas3/resultats/t{N}_resum.csv`. Columns:

`isin,resultat,que_s_ha_mirat,dubte,notes`

- `resultat`: `tancat` (every open year has a complete proof with your quotes plus what was registered), `parcial` or `no_trobat`.
- `dubte`: empty, or a short label: `D1`, `P1`, `P3`, `contradiccio`, or `ceo_fundador` if any source says a CEO founded the company (report it, do not hide it).

Rewrite both CSVs after each company. End with a 10-line report: counts per `resultat`, and any `dubte` cases.

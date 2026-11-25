# Lot 26: second source for founder-CEOs (research)

**Context.** This is a PhD evidence database on founder-CEOs in the STOXX Europe 600. The rules are in CLAUDE.md, which you already have. Read in particular:
- D37 (founder citation from the issuer);
- rule 25, P6, the founder expressions;
- the decisions of 24/11/2026: Q2, Q3 «founding CEO» alone does not count, and Q6;
- D1/D10, the predecessors.

This is research only. Do not edit any git repository.

**Why.** Each company below has a CEO classified as a FOUNDER (FounderCEO = 1) in the years `anys_F`, but the founder evidence comes from only ONE document. A robustness check that reproduces Villalonga and Amit (2006) needs at least TWO different documents (n_A + n_B ≥ 2). Your job is to find a **second, different document** that says the same CEO founded or co-founded the company, or a D1/D10 predecessor.

**Input:** `(carpeta de treball de Claude)/font2/entrada/f{N}.csv`, about 29 companies. The columns are:
- `ceos`: the CEO(s) in the F years;
- `regles` and `marques`: the current rule, e.g. D37 or FT;
- `fonts_fundador_registrades`: the document(s) already registered, given as ID, mark, URL and quote. Do NOT reuse that same document (same URL, or the same file under another URL).

## What counts

- **Accepted wording:** an A source (issuer, regulator, register) or a B source (quality financial press, books, academic articles) that literally calls the CEO founder or co-founder of the listed company or a predecessor:
  - P6 wording: founder, co-founder, fondateur, Gründer, oprichter, grundare, «founded/set up/established/started the company» with the person as subject;
  - Q2 wording: «one of the founding members», «founding partner», «part of the founding group».
- **Not accepted:**
  - «founder-led», «founding CEO» alone, «founding shareholder»;
  - founder of ANOTHER entity, such as a subsidiary, a fund, or a company the listed group later bought (Q1).
- **FT cases:** if `regles` is FT (a transformational founder: the person took control of an existing company), a second source must document the same thing. That means control or first individual shareholder, CEO or executive chair, and a documented transformation. Or a source calling the person founder.
- **Contrary evidence:** if you find a source that contradicts the founder status, for example «joined the company in 1995 after its founding», report it. Do not hide it.
- **Not allowed:** Wikipedia, LinkedIn, Crunchbase, Bloomberg or Reuters profile pages, and aggregators. They can be hints only.
- **Downloads:** plain curl only, via `(carpeta de treball de Claude)/cerca_fund/dl.sh URL OUTPATH` into `(carpeta de treball de Claude)/font2/descarregues/f{N}/`. No browser user agent, no Referer, no `-k`, no logins, no antibot circumvention. The final URL must download with plain curl, because the quote will be re-checked by script.
- **Check:** verify each quote with `python3 -I (carpeta de treball de Claude)/cerca_fund/cerca.py FILE REGEX`. If a PDF has columns, also try `pdftotext` without `-layout` and with `-raw`.
- **Quote format:** copy the quote exactly, 1-3 sentences, no translation.

## Output 1: quotes

Write `(carpeta de treball de Claude)/font2/resultats/f{N}_cites.csv` with the python csv module, one row per quote. Columns:

`isin,anys,funcio_cita,marca_prova,part,persona,url,data_document,tipus_document,pagina,cita_literal,nivell,allotjament,notes`

- `anys`: the F years of that CEO.
- `funcio_cita`: `fundador`. Use `context` for an FT transformation or control quote, or for contrary evidence.
- `marca_prova`:
  - `D37` for an issuer (A) source;
  - `cita_fundador` for a B source or a non-issuer A source;
  - empty for `context`.
- `part`: empty.
- `persona`: the CEO's name.
- `nivell`: `A` or `B`.
- `allotjament`: one of `emissor`, `regulador`, `grup`, `successor`, `plataforma`, `mitja`.
- `notes`: say which entity the quote refers to (the listed company or a predecessor) and why it is a second, independent document.

## Output 2: one row per company

Write `(carpeta de treball de Claude)/font2/resultats/f{N}_resum.csv`. Columns:

`isin,resultat,que_s_ha_mirat,dubte,notes`

- `resultat`:
  - `trobada`: a second document was found;
  - `no_trobada`;
  - `contradiccio`: a source contradicts the founder status.
- `dubte`: empty, or a short label.

Rewrite both CSVs after each company. Be efficient. Good routes are:
- the issuer's own other documents: other years' annual reports, IPO prospectus, AGM notices, press releases, history page;
- quality press profiles: FT, Les Echos, Handelsblatt, Expansión, Il Sole 24 Ore, Dagens Industri and similar.

End with a 10-line report: counts per `resultat`, and any contradictions.

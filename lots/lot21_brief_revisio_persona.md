# Review of proof parts taken from documents we already have (pass 2)

Context: PhD evidence database on founder-CEOs (STOXX Europe 600). CLAUDE.md holds the rules; read the proofs a-e and the «Decisió de Jordi del 24/11/2026».

To document that a CEO is NOT a founder, we need, for each part of the proof, an A/B quote:
- proof **b**: the company's founding year, and the CEO's birth year (the CEO was under 18 or not yet born at founding);
- proof **c** (reserve proof, used only when there is no age): the founding year, and the year the CEO's mandate started (64 or more years apart).

A script extracted candidate sentences from the issuers' own annual reports, which we already have. Your batch is `persona/lot{N}.json`, relative to `{S}`. It is a list of companies:
- `isin`, `empresa` and `ceos`;
- `tags_script`: parts the script tagged with strict patterns. Each has `persona`, `part`, `cita_literal`, `url`, `anys` and `notes`. The notes contain the tag `[part naixement_ceo=Name:YYYY]` or `[part inici_mandat=Name:YYYY]`;
- `candidats_fundacio`: up to 6 sentences that may give the company's founding year.

## Task 1: check every script tag

For each script tag, give a verdict:
- `ok`: the sentence itself states this person's birth year, or age, or the year they became CEO of this company, and the value in the tag is right;
- `corregir`: the sentence supports the part but the value is wrong. Give the right value. For an age, the tag already converts it as (year of the document − age − 1). Keep that convention: an age only gives the earliest plausible birth year;
- `rebutjar`: the sentence does not state it for this person. For example:
  - «Born» is part of the person's name;
  - an age range for a whole board;
  - the year belongs to another role (board member, joining the group) or to another person;
  - the document year for an age is unknown.

## Task 2: founding-year candidates

For each sentence in `candidats_fundacio`, decide whether it states the founding year of THIS company, or of its operating business or a named predecessor, as the issuer presents it. The relevant founding follows rule 25:
- a new holding, renaming, IPO or redomiciliation is not a founding (P1);
- for a merger, say so.

Answer `ok` with the year and `entitat_tipus` (emissor | predecessora | holding | altra), or `rebutjar` with the reason. Keep at most the 2 best `ok` sentences per company.

## Output

Write `persona/lot{N}_revisio.json` with this shape:

```
[{"isin": "...",
  "tags": [{"cita_inici": "<first 60 chars>", "persona": "...", "part": "...", "veredicte": "ok|corregir|rebutjar", "valor": "Name:YYYY", "motiu": "..."}],
  "fundacio": [{"cita_inici": "<first 60 chars>", "veredicte": "ok|rebutjar", "any": "YYYY", "entitat_tipus": "...", "motiu": "..."}]}]
```

## Rules

- Judge only from the sentence itself and the names given.
- Do not search the web.
- Do not invent anything.
- When done, reply with the counts per verdict.

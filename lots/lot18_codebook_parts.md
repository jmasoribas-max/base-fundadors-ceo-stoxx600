# Codebook: proof parts in founder-evidence quotes (PhD database, founder-CEOs, STOXX Europe 600)

Each entry is a literal quote from an A/B source, attached to a listed company (`empresa`, `isin`) and a range of years.
- In those years the company's CEO(s) are `ceos_anys_entrada`. Other CEOs of the same company in other years are listed in `altres_ceos_isin`.
- The database classifies these CEOs as NOT founders. To document that, each proof needs all of its parts, each backed by a quote:

| Proof | Parts needed |
|---|---|
| a | the founders are named, and the CEO is not one of them |
| e | the company was created by the State or by another company |
| b | founding year, and the CEO's birth year (the CEO was under 18 or not yet born) |
| d | founding year, and the CEO's prior employer plus the year they joined (3 or more years after the founding) |
| c | founding year, and the start of the CEO's mandate (64 or more years apart; reserve proof) |

Your job: read ONLY the quote text, plus the company name and CEO names given. List the parts the quote itself documents, with their values.
- Do not use outside knowledge.
- Do not infer what the quote does not say.
- If unsure, leave a part out.

## Parts (one object per part found; a quote can document several)

1. **`llista_fundadors`**
   - When to tag: the quote names the natural person(s) who founded the company.
     - Examples: "founded in 1865 by Henri Nestlé", "Ernest Solvay founded the company", "fondée par Marcel Dassault".
     - Also counts (decision of 24/11/2026): "founding member", "co-founding executive", "founding partner", "founding director", "part of the founding group".
   - Fields:
     - `valor`: the founder names, separated by " + ".
     - `tancada`:
       - `si` when the quote presents the founders as the whole set: a singular "founded by X", or "founded by X and Y";
       - `no` when the set is open: "one of the founders", "co-founder" with no other names, "among others".
     - `entitat`: the company that was founded, as the quote names it.
   - Not this part:
     - "son of the founder" or "founder-led" with no founder name;
     - a family with no person ("the Wallenberg family") — tag it with `valor` = the family name and `tancada` = `familia`.

2. **`origen_entitat`**
   - When to tag: the quote says the company (or its predecessor) was created by the State, by law, by a government, or by another company (spin-off, carve-out, subsidiary set up by X, created by a group of banks).
   - Fields:
     - `valor`: the creator.
     - `entitat`: the company that was created.
   - Not this part:
     - a merger of two companies;
     - an acquisition;
     - a person or a family creating it (that is `llista_fundadors`).

3. **`any_fundacio`**
   - When to tag: the quote gives the year the company (or a predecessor) was founded, established, incorporated or created.
   - Fields:
     - `valor`: the year (4 digits), the one tied to the founding verb.
     - `entitat`: the company the year refers to.
   - Not this part: a year of a merger, IPO, renaming, acquisition or listing. You may report it as `any_altre`, with a word in `nota` saying what happened.

4. **`naixement_ceo`**
   - When to tag: the quote states a person's birth year explicitly ("born in 1963", "né en 1963", "geboren 1963", "(born 1963)", "year of birth: 1963").
   - Fields: `valor` = "Name:YYYY".
   - If the quote gives an age and the date of that age is stated in the quote, give "Name:age NN in YYYY".
   - Not this part: a bare year next to a name with no birth wording, as in "Andreas Treichl (Chairman) 1952".

5. **`ocupador_anterior`**
   - When to tag: the quote says the person worked at ANOTHER named organisation before joining the company or its group ("prior to joining X, he was at Y", "joined X from Y", "previously CFO of Y").
   - Fields: `valor` = "Name:Employer:YYYY", where YYYY is the year the person joined the company, if the quote gives it; otherwise "Name:Employer:".
   - Not this part:
     - "joined the company in 2003" with no other employer (that is `entrada`);
     - roles inside the same company.

6. **`entrada`**
   - When to tag: the quote gives the year the person joined the company or group.
   - Fields: `valor` = "Name:YYYY".

7. **`inici_mandat`**
   - When to tag: the quote gives the year the person became CEO (or the equivalent title) of the company.
   - Fields: `valor` = "Name:YYYY".

For any part, `entitat_tipus` is one of:
- `emissor`: the listed company itself;
- `predecessora`: a former name of the listed company or of its operating business;
- `altra`: another company, such as a subsidiary, a parent, a different firm or a firm the person founded elsewhere;
- `incert`.

For persons, use the name as written in the quote. If the quote uses only a first name or "he", give the CEO name that it clearly refers to and add `nota: pronom`.

## Flags (per entry)

- `ceo_fundador`: `si` if the quote says that one of the CEOs (`ceos_anys_entrada` or `altres_ceos_isin`) founded or co-founded the listed company or a predecessor. Name the CEO in `nota_entrada`. This contradicts the "not founder" label, so be precise.
- `sense_parts`: `si` if the quote documents none of the parts above.

## Output

One object per entry: `{id, parts: [{part, valor, entitat, entitat_tipus, tancada?, nota?}], ceo_fundador, sense_parts, nota_entrada}`. Use exactly these part names. Be literal and conservative.

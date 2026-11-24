# Lot 16: grup F, cerca nova de cites de fundador

- **Fet per:** Claude, 23/11/2026. Cerca amb dos agents (22 empreses), i verificació i importació amb [`traspas/importa_fundador.py`](../traspas/importa_fundador.py).
- **Abast:** les 57 files F que, després del lot 11, no tenien cita de fundador. Només s'hi afegeixen proves; **cap canvi de FounderCEO ni de `ceos`**.
- **Normes de la cerca:** fonts A/B (ni agregadors, ni Wayback, ni biografies no corporatives). La cita ha d'anomenar el CEO i dir que va fundar la cotitzada o una predecessora, amb les expressions que admet la P6.

## Verificació independent (Claude)

1. **Contingut de la cita:**
   - ha d'anomenar el CEO i contenir un mot de fundació admès per la P6 («founding CEO», «founder-led», «founding shareholder» i «founding member» no compten);
   - el cognom no pot anar precedit d'un altre nom de pila.
2. **Document:** Claude el torna a baixar i hi busca la cita literal.
3. **Cites ampliades:** quatre cites anomenaven la persona només pel nom de pila («Martin», «Michael», «Nick»). S'han ampliat cap enrere, amb text contigu del mateix document, fins al nom complet de la capçalera de la biografia. Ho diu la nota de cada entrada.
4. **Marca de prova:**
   - `D37` si la font és de l'emissor (nivell A);
   - `cita_fundador` amb `si_font_B` si no ho és. És el cas d'Actelion: el prospecte de l'OPA de Johnson & Johnson, publicat per la Comissió d'OPA suïssa.
5. **Entitat predecessora:** si l'entitat fundada no és la cotitzada (Intercapital, Aberdeen Asset Management), l'entrada porta una nota i la fila queda en dubte (regla 26).

## Resultats

| Recompte | Valor |
|---|---:|
| Files del lot | 57 (22 empreses) |
| Files fetes (cita de CEO i de fundador) | 36 |
| … de les quals amb `ceo_interval` | 0 |
| Files amb cita de fundador nova `[V]` | 37 |
| Files en dubte enviades a `PENDENTS.md` | 27 (secció «Dubtes del lot 16») |
| Entrades noves `[V]` | 19 (18 `D37`, 1 `si_font_B`) |
| Entrades noves `[NV]` | 0 |
| Fonts antigues revisades | 0 |
| Canvis proposats a FounderCEO o `ceos` | 0 (les contradiccions van a dubtes) |
| Dubtes del lot 10 tancats | 17 files: Actelion 2016, Neoen 2024, Melrose 2016-2020 i 2023, Reply 2021-2025 i ArcelorMittal 2017-2020 ([`estat/dubtes_tancats.csv`](../estat/dubtes_tancats.csv)) |

**Grup F després del lot:** 329 de 349 files amb cita de fundador (abans 292).

## Dubtes per a Jordi (resum; detall a `PENDENTS.md`)

- **Predecessores (regla 26):**
  - ICAP i NEX (Spencer, Intercapital i la combinació del 1999);
  - Standard Life Aberdeen (Gilbert; la fusió del 2017 es comptabilitza com a adquisició, i probablement és un `dubte_D1`);
  - Petrofac (entrada el 1991 a través d'AMcorp).
- **P6:**
  - Rightmove: «co-founding executives», i a més la formen quatre agències;
  - Energean: «Prior to setting up Energean», més «founding shareholder» i la P1.
- **Contradiccions amb font A** (possible canvi 1 → 0):
  - Cellnex: escissió del 2015, en què Martínez havia entrat com a directiu (P4);
  - Merlin: MBO del 1999 (P1).
- **Sense cap font A/B:** alstria (possible prova e) i Sagax.
- **Co-CEO que no són fundadors**, on la fila ja és F pels altres co-CEO: Skeoch (Standard Life Aberdeen), Clarisse Gobin-Swiecznik (Rubis 2023-2025) i Tatiana Rizzante (Reply; l'emissor en diu «part of the founding group», expressió que la P6 no admet). Les fonts ho confirmen i no canvia l'etiqueta de la fila.

# Triatge dels dubtes oberts de `PENDENTS.md` (25/11/2026)

Hi havia 150 files-any amb un dubte obert en alguna secció de `PENDENTS.md`: regla 29 i lots 9, 10, 12, 16 i 17. Un agent n'ha revisat cada dubte contra l'evidència actual del registre (lots 18-26), els lots de correcció i les decisions de Jordi de CLAUDE.md, amb les entrades concretes que el resolen. El resultat, una fila per ISIN, any i secció, és a `triatge_dubtes_20261125.csv`. Les que queden obertes són a `triatge_dubtes_20261125_oberts.csv`.

| Secció | Es tanca | Queda obert |
|---|---:|---:|
| Regla 29 | 45 | 24 |
| Lot 9 | 5 | 0 |
| Lot 10 | 52 | 10 |
| Lot 12 | 17 | 6 |
| Lot 16 | 17 | 5 |
| Lot 17 | 3 | 4 |

- **Tancades a `estat/dubtes_tancats.csv`:** 106 files-any, les que tenien totes les seccions resoltes. Una fila-any només es tanca si es tanquen tots els seus dubtes, perquè el fitxer va per ISIN i any.
- **Comprovació:** s'ha revisat una mostra de 10 tancaments, i tots els ID citats existeixen al registre. CTS Eventim (FT, Q7) ja és a la base amb FT tipus c.
- **Efecte:** les files amb un dubte obert passen de 150 a 44, i les files acabades, de 279 a 287.

## Què queda obert (44 files-any)

**Decisions per a Jordi:**
1. **Tritax `GB00BG49KP99` 2019-2021.** Els informes signen Godfrey com a «CEO – Fund Management», que és un títol del gestor extern. Recomanació: llegir-lo així (Q12). El 2019-2020 es mantenen R-SC. El 2021 passa d'1 a NA_sense_ceo, llevat que l'AR 2021 l'anomeni CEO de la plc.
2. **EssilorLuxottica `FR0000121667` 2018-2020.** Del Vecchio és fundador de Luxottica, la part que s'hi va combinar. Abans de decidir cal mirar a l'AR 2018 o al document de l'OPA el repartiment del capital i quina part va ser l'adquirent comptable. Recomanació:
   - si és una D1 (cap part per sobre del 60 %), es manté l'1;
   - si va ser una adquisició, 0 amb `dubte_D1`;
   - si Luxottica va ser l'adquirent comptable (adquisició inversa), es manté l'1 amb `dubte_D1` (D37d).
3. **Siemens Gamesa `ES0143416115` 2017-2019.** Tacke venia de la part de Siemens. Primer cal buscar el seu naixement i l'any de fundació de Bonus Energy. Si no es troben, la recomanació és declarar la fila com a 0 sense prova completa (A.4), sense acceptar Siemens AG com a ocupador anterior (P9).

**Correccions ja decidides, pendents d'una cerca o d'una entrada al registre:**
- **Standard Life Aberdeen 2017-2018:** Q1, de 1 a 0 amb `dubte_D1`.
- **alstria 2019-2021:** registrar «one of the founding members» (Q2) si és de l'emissor.
- **Rubis 2021-2025:** Q11, els co-gérants que l'emissor no anomeni Gérant surten de `ceos`.
- **Telefónica 2017-2025:** regla única del president executiu, amb l'IAGC original en castellà.

**Només cerca o registre:**
- ACS 2016 i 2021: Q7 i cerca de la D37.
- Holmen 2020-2025: fundació de Holmens Bruk i d'Iggesund.
- UBI 2016-2019.
- Vifor 2017-2019: evidència R3.
- Mapfre 2025: R1 → R3.

**Seguiments de files tancades** (`que_falta` del CSV), sense efecte sobre l'etiqueta:
- **Marques per afegir:**
  - `dubte_D1`: ACS, UPM, RTL, Fluidra i AFRY;
  - `gestio_externa`: BB Biotech;
  - `co_ceo_titol_funcional`: Zalando.
- **Entrades que cal tornar a registrar amb la funció correcta:**
  - Ferrovial X01-X07, com a CEO R1;
  - Bridgepoint X01, com a fundador D37;
  - Hexagon X01;
  - BB Biotech;
  - Evraz D01.
- **Comprovacions de la D37a:** Tritax, Darktrace i Energean.

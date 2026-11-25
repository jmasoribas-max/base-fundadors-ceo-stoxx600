# Lot de correcció 4: fundador transformador (D37b) a Bridgepoint, Petrofac i Paysafe (25/11/2026)

- **Proposta:** Claude, 25/11/2026, a partir de l'evidència contrària trobada al lot 26 (`lot26_README.md`).
- **Aprovació:** Jordi, 25/11/2026: «hi estic d'acord». Les quatre empreses es mantenen a 1 per la D37, amb `fundador_transformador`=1 (D37b).
- **Canvis:** [`correccio4_canvis.csv`](correccio4_canvis.csv), 9 cel·les a 5 files. **Cap canvi de FounderCEO.**
- **Com s'ha aplicat:**
  - `python3 estat/aplica_canvis.py lots/correccio4_canvis.csv --aplica --origen correccio4_claude`. Abans, la prova en sec no va trobar cap discrepància.
  - L'script ha escrit el CSV i l'xlsx de la base, el registre i les fitxes.

| Empresa | Anys | Evidència (A) | Canvi |
|---|---|---|---|
| Bridgepoint `GB00BND88V85` | 2021-2022 | Fullet de l'OPV del 2021: «employed by the group since 6 October 1986»; «Founded in 1984» | `fundador_transformador` 0 → 1. Amb la fórmula v8r1 (si `fundador_transformador`=1, es pren `founderceo_rob_pre_d37`), `founderceo_rob_sense_fundador_transformador` i `sense_fundador_transformador` passen d'1 a 0 |
| Petrofac `GB00B0H2K534` | 2016 | AR 2016, p. 72: «Joined the Group in 1991 to establish Petrofac International» (negoci des del 1981) | `fundador_transformador` 0 → 1. La robustesa no canvia, perquè `founderceo_rob_pre_d37`=1 |
| Paysafe `GB0034264548` | 2016-2017 | Fullet regulat del 2015: la cotitzada va comprar el negoci d'Optimal Payments el 2011; Leonoff va fundar SureFire el 1998 | `fundador_transformador` 0 → 1. La robustesa no canvia (`founderceo_rob_pre_d37`=1). La Q1 queda resolta per la D37 i la Q5, que ja estaven aprovades |
| Investec `GB00B17BBQ50` | 2016-2017 | AR 2017, p. 118: «Stephen joined Investec in 1980» (fundació el 1974) | Cap: ja tenia `fundador_transformador`=1 |

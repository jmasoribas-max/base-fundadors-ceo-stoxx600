# Lot 28 · Dubtes oberts (cerca) i lot de correcció 5 (25/11/2026)

Cerca per als 44 files-any que el triatge del 25/11/2026 havia deixat amb un dubte obert (`triatge_dubtes_20261125_oberts.csv`), i aplicació dels criteris ja aprovats que la cerca permet tancar. El resultat per empresa és a `lot28_resum_cerca.csv`.

- **Evidència:** `traspas/importa_entrades.py --lot 28 --origen dubtes_oberts` ha escrit 73 entrades. Cada cita s'ha tornat a baixar i s'ha comprovat literalment. Una de les entrades anul·la el 2007 de la fitxa d'UBI (fusió D1, regla 21b).
- **Correcció:** `correccio5_canvis.csv` són 51 cel·les a 11 files, aplicades amb `estat/aplica_canvis.py`. Només s'hi apliquen criteris que Jordi ja havia aprovat (Q1, Q2, R3 i la regla única).
- **Dubtes tancats:** 34 files-any més a `estat/dubtes_tancats.csv`. **Queden 10 files amb un dubte obert**, que són decisions de Jordi.

| Empresa | Resultat | Canvi |
|---|---|---|
| Standard Life Aberdeen 2017 (`GB00BVFD7Q58`) i 2018 (`GB00BF8Q6K64`) | Els informes del 2017 i el 2018 diuen «merger accounted for as an acquisition of Aberdeen by Standard Life plc» (66,7 % / 33,3 %) | **Q1: FounderCEO 1 → 0** (prova d de Skeoch i Gilbert), `dubte_D1`, robustesa D1 àmplia = 1 |
| Vifor 2017-2019 | El càrrec de CEO era vacant (Schulze, 14/5/2020) i l'emissor presenta Jornod com a primer executiu | `regles` R-SC;b → R3;b |
| alstria 2019-2021 | Perfil de l'emissor a EQS News: «one of the founding members of alstria» (sense data; probablement del 2018) | `regles` cita_fundador → D37 (Q2) |
| Mapfre 2025 | IAGC 2025: «máximo responsable ejecutivo»; «La Sociedad no cuenta con consejeros delegados» | Cita R3; `founderceo_rob_sense_r3` 0 → NA_sense_ceo |
| Telefónica 2017-2025 | Els IAGC originals designen el president primer executiu cada any | Cap: es confirma `ceo_president_exec` |
| Siemens Gamesa 2017-2019 | Bonus Energy 1980 i Gamesa 1976; naixement de Tacke (1964 com a molt aviat, per l'edat a l'AR 2021 d'Oerlikon) | Cap: prova b contra les dues parts |
| Holmen 2020-2025 | Iggesunds Bruk 1685, Holmens Bruk 1854 | Cap: prova b contra totes les parts |
| UBI 2016-2019 | Fullet de Banca Lombarda del 2006: CAB 1883, Banca San Paolo 1888, Massiah nascut el 1959 | Cap: prova b; el 2007 queda anul·lat |
| Rubis 2021-2023 | Els documents de registre anomenen Gérant cada persona de `ceos` | Cap (Q11) |

## Decisions per a Jordi (10 files, no s'ha canviat res)

1. **EssilorLuxottica 2018-2020.**
   - **Fets:** el document de référence del 2018 diu «rapprochement». Després de l'OPA, Delfin té el 32 % i cap part no supera el 60 %. Luxottica és l'adquirent comptable («acquisition inversée», p. 200). L'emissor diu «Leonardo Del Vecchio est le fondateur du groupe Luxottica».
   - **Proposta:** mantenir l'1 i afegir `dubte_D1`. La Q1 no s'hi aplica, perquè Luxottica no és la part absorbida.
2. **ACS 2016 i 2021 (Florentino Pérez), Q7 FT.**
   - **Fets:**
     - Primer accionista de la cotitzada: 12,5 % el 2016 i 12,9 % el 2021.
     - Màxim executiu des del 1984.
     - L'emissor documenta la transformació («tras su adquisición se reconvierte y relanza. Es germen del Grupo ACS hoy»).
     - Cap document de l'emissor no l'anomena fundador.
     - Cap font no diu literalment que fos el primer accionista individual de Padrós el 1983.
   - **Proposta:** si acceptes l'FT, FounderCEO 0 → 1, `ft`=1, `tipus_ft`=c, `regles` cap;FT.
3. **Rubis 2024-2025 (Jacques Riou).** No se l'anomena Gérant: només signa com a «Président d'Agena, société co-Gérante», sota «La Gérance». Amb la Q11 literal, surt de `ceos`. L'1 es manté, perquè Gilles Gobin hi continua.
4. **Tritax 2021.** L'AR 2021 no anomena Godfrey CEO de la plc: diu «CEO – Fund Management» i que la societat no té executius. Amb la Q12, la fila passa a R-SC: FounderCEO 1 → NA_sense_ceo. El 2019 i el 2020 ja són R-SC.

## Efecte

- **Panell:** 350 F i 5.623 P. Abans eren 352 F i 5.621 P, i la diferència és Standard Life Aberdeen.
- **Files amb un dubte obert:** passen de 44 a 10.

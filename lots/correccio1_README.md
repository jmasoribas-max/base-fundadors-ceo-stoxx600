# Lot de correcció 1: coherència del CSV oficial

- **Proposta de:** Claude, 23/11/2026. **Estat:** preparat, **no aplicat**.
- **Aprovació:** Jordi va aprovar el 23/11/2026 la decisió 1 (copiar `sim_ceo_aplicat` a `ceos`) i la decisió 2 (corregir `regles` amb les decisions de Doctorat i revisar les P amb `cap`). El buidatge dels camps de motiu de ND és una proposta de Claude dins el mateix lot, pendent de l'OK de Jordi al PR.
- **Canvis:** [`correccio1_canvis.csv`](correccio1_canvis.csv), 171 cel·les a 59 files. Cap canvi de `FounderCEO`.
- **Com s'aplica:** `python3 estat/aplica_canvis.py lots/correccio1_canvis.csv` (prova en sec, comprova els valors actuals); amb `--aplica --origen correccio1_claude` escriu el CSV, l'xlsx, el registre i les fitxes. Qui l'aplica (Claude o DF) depèn de la decisió de Jordi sobre l'accés a `dades/`.

## Què canvia

| Camp | Cel·les | Què |
|---|---:|---|
| `ceos` | 7 | Enagás 2016-2021 → Marcelino Oreja Arburúa (consejero delegado, R1; decisió de Doctorat 8). Bellway 2017 → Ted Ayres (decisió de Doctorat 9). És el valor que ja tenia `sim_ceo_aplicat` |
| `regles` | 41 | La regla de la decisió de Doctorat (`sim_nota`) o de l'evidència del registre, en lloc de `cap`, `b` o `cita_fundador` |
| `motiu_nd`, `detall_motiu_nd`, `motiu_nd_article`, `tancament_nd` | 123 | Es buiden en 39 files que ja no són ND. El valor antic queda al fitxer de canvis, al registre i a l'historial |

Regles noves per empresa:

| Empresa | Anys | De | A | Font |
|---|---|---|---|---|
| Cellnex `ES0105066007` | 2016-2022 | `b` | `D37` | Doctorat, `previa:C0220` (F per D37) |
| AB InBev `BE0974293251` | 2021-2025 | `cap` | `b` | Doctorat, `previa:C0417` |
| Unicaja `ES0180907000` | 2025 | `cap` | `e` | Doctorat 6 |
| Mandatum `FI4000552526` | 2025 | `cap` | `e` | Doctorat, `previa:C0180` |
| Orpea `FR0000184798` | 2016-2021 | `cap` | `a` | Doctorat 2 (fundador únic) |
| SFR `FR0011594233` | 2016 | `cap` | `e` | Doctorat, `previa:C0302` |
| Dechra `GB0009633180` | 2018-2023 | `cap` | `a` | Doctorat, `previa:C0369` |
| Mediclinic `GB00B8HX8Z88` | 2016-2017 | `cap` | `a` | Doctorat 4 |
| Harbour `GB00BMBVGQ36` | 2022-2023 | `cita_fundador` | `e` | Doctorat, `previa:C0241` |
| Steinhoff `NL0011375019` | 2016-2017 | `cap` | `b` | Lot ND-1 |
| CD Projekt `PLOPTTC00011` | 2023 | `cap` | `a` | Doctorat 1 |
| Swedbank `SE0000242455` | 2016-2018 | `cap` | `e` | Doctorat 5 |
| Vantage Towers `DE000A3H3LL2` | 2022 | `cap` | `e` | Registre, lot 3 (fullet d'IPO: Vodafone va crear l'entitat) |
| Stora Enso `FI0009005961` | 2020-2022 | `cap` | `d` | Registre, lot 7 (incorporació el 2001 i el 2017, després de la fusió del 1998) |

## Què no entra en aquest lot

- **Knorr-Bremse 2019-2020 i Pandora 2018** (`regles=R-SC;R2b`, FounderCEO 0): direcció interina col·legiada (R2b). La metodologia diu que, en aquest cas, FounderCEO surt de les proves normals per a cada membre, i el registre no en té cap. Hi ha un dubte obert del lot 5. Van a la llista de dubtes per a Doctorat i a cerca (proves a-e per a cada membre); si no se'n troben, el 0 no té prova.
- **Les 48 P amb `cap;b` o `cap;a`**: ja contenen una prova de «no»; no són incoherents. Netejar el prefix `cap;` és cosmètic i es pot fer més endavant.

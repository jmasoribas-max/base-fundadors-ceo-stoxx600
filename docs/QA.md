# QA del repositori v8 r2

Data: 19/11/2026 09:49 (CET, Europe/Madrid). Scripts executats en local, **sense `--live`**. No s'ha creat cap remot ni s'ha fet cap push.

## QA de la base

# QA v8 r2

Data: 19/11/2026 09:42 (CET, Europe/Madrid). Font del sector: `auditoria_v75r2/sector_icb/sector_icb_v75r2.csv` SHA `ddc3d037d796c4053700ce374148f134b09e071579875befe89e664e816899af` [V].
Base d'origen: `base_isin_any_v8r1.csv` SHA `eded7aca54d653119df703cc5fe54d1838e8ccd75e7ee02e149d790ecfbe12d9` [V]. No s'han modificat la v8 ni la v8r1 (SHA v8 `3755089905305f3f13d23c73846e555afec2918a0642377c8b2ba3a62534e916` [V]).

- CSV: `base_isin_any_v8r2.csv` SHA `1eb35dd77b410eb486e5ce534c9a852357517090b9a7759d25f8de90ee31c68f` [V], 6768551 B, 6012 files, 156 columnes (146 heretades + 10 de sector).
- XLSX: `base_isin_any_v8r2.xlsx` SHA `f93c22748abc6632829bcea54bccbb5a286db4e395b0a498ab65ef9056a7cca0` [V] (el SHA de l'xlsx no és estrictament reproduïble per metadades zip).
- Còpia del sector: `sector_icb_v8r2.csv` SHA `ddc3d037d796c4053700ce374148f134b09e071579875befe89e664e816899af` [V] (idèntic a la font).

## Comptes principals (han de coincidir amb la v8r1 / v8 / v2)

- Panell: n=6012, ISIN=1040, anys 2016-2025.
- FounderCEO: F 343, P 5624, ND 14, NA 31.
- Mostra principal J14: n=5954, F=342.
- Certificació (files `sim_estat_certificacio=certificada` i nivell): N1 740, N2 1018, doctorat 15 (total 1.773); ceo_pendent 108; no_certificada 241; fora_mostra_auditoria 3890.
- Discrepàncies vs v8r1: 0.
- Columnes heretades idèntiques: True. `ceos` idèntic: True. `FounderCEO` idèntic: True.

## Sector (v8r2)

No s'ha estès el sector d'una font de 2023 (ni de cap `any_font` ≤ 2023) als anys 2024-2025. Aquesta extensió queda com a pendència de Doctorat.

| estat_sector | Files |
|---|---:|
| `amb_sector` | 4777 |
| `pendent_extensio_2024_2025` | 1095 |
| `sense_sector` | 98 |
| `revisar` | 9 |
| `revisar_pendent_extensio_2024_2025` | 33 |

- Empreses `revisar*` (via indirecta `nom_stoxx_via_llista_seleccio`): 25 (esperat 25).
- Empreses `sense_sector`: 72 (esperat 72), files 98 (esperat 98), amb el motiu original de la font.
- Files amb `supersector` buit: 1226 (98 sense_sector + 1.128 pendent d'extensió 2024-2025).
- Recomptes d'`estat_sector` com s'esperava: True.
- v8 i v8r1 intactes després de l'escriptura: True.

Resultat global: OK.


## QA de l'arbre del repositori

| Comprovació | Resultat |
|---|---|
| Fitxes `empreses/{ISIN}.md` | 1.040 / 1.040, un per ISIN de la base [V] |
| `index.csv` i `INDEX.md` coherents amb la base | OK (mateix conjunt de 1.040 ISIN; enllaços a les fitxes) [V] |
| Enllaços interns markdown | 0 trencats [V] |
| `python3 scripts/valida_pr.py` (sense `--live`) | exit 0, 0 problemes [V] |
| `python3 scripts/comprova_enllacos_cites.py` (sense `--live`) | exit 0; 46 files del registre i 1.040 fitxes; 0 problemes [V] |
| Valors permesos (FounderCEO, estat_sector, certificació, nivell) | OK [V] |
| Capçaleres obligatòries de les fitxes | OK [V] |

La branca `main` d'aquest arbre local és el commit inicial. A GitHub, `main` s'ha de protegir abans d'usar Claude Code (vegeu `docs/PROTECCIO_BRANCA_MAIN.md`). Claude no pot tocar `main`.

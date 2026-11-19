# QA del repositori v8 r3

Data: 19/11/2026 10:14 (CET, Europe/Madrid). Scripts executats en local, **sense `--live`**. No s'ha creat cap remot ni s'ha fet cap push.

## QA de la base

# QA v8 r3

Data: 19/11/2026 10:10 (CET, Europe/Madrid). Part de `base_isin_any_v8r2.csv` SHA `1eb35dd77b410eb486e5ce534c9a852357517090b9a7759d25f8de90ee31c68f` [V] sense modificar-la.
No s'han modificat la v8 ni la v8r1 ni la v8r2 (intactes: True).

- CSV: `base_isin_any_v8r3.csv` SHA `1b7df913b31300857cbc77332a9aa03626edc0013f3bbb1e8625aa456ee38d4c` [V], 6912713 B, 6012 files, 158 columnes.
- XLSX: `base_isin_any_v8r3.xlsx` SHA `4ad8dbf3086b99768a3d50d655d3fcb91606f02b9a9d7682bf2b161ca7b9f41b` [V].
- Sector (còpia, idèntica a la font): SHA `ddc3d037d796c4053700ce374148f134b09e071579875befe89e664e816899af` [V].

## Comptes principals (han de coincidir amb la v8r2 / v8r1 / v8)

- FounderCEO: F 343, P 5624, ND 14, NA 31.
- J14: n=5954, F=342.
- Certificació: N1 740, N2 1018, doctorat 15; ceo_pendent 108; no_certificada 241; fora_mostra_auditoria 3890.
- Discrepàncies vs v8r2: 0. FounderCEO idèntic: True. ceos idèntic: True.

## Sector (extensió juny 2023 → 2024-2025)

S'ha estès el supersector del PDF de juny 2023 a **1076 files** de **561 ISIN** (només els que ja tenien `any_font=2023`). `sector_estes_des_2023=1` i `any_font=2023`. Per excloure-les en una robustesa, filtra `sector_estes_des_2023!=1`. El sector fix per empresa és `supersector_fix` (5914 files amb valor).

| estat_sector | Files |
|---|---:|
| `amb_sector` | 5825 |
| `revisar` | 37 |
| `pendent_extensio_2024_2025` | 47 |
| `revisar_pendent_extensio_2024_2025` | 5 |
| `sense_sector` | 98 |

- Files 2024-2025 que no s'han estès (ISIN amb sector però sense font de juny 2023): 52 files, 33 ISIN.
- Empreses `sense_sector`: 72 (48 només 2024-2025 + 24 no casades), 98 files. Queden pendents per a Claude (font A).
- Supòsit, [NV]: no hi ha hagut cap reclassificació ICB entre 2023 i 2025 (vegeu LIMITACIONS).

Resultat global: OK.


## QA de l'arbre del repositori

Comprovacions estructurals (1.040 fitxes, índex, enllaços, valors, capçaleres i cites) aplicades sobre l'arbre. `scripts/valida_pr.py` avisa si s'edita `dades/` a `main` amb canvis sense commitejar: aquest avís és el comportament esperat mentre s'actualitza l'arbre oficial; un cop fet el commit local i l'arbre net, el validador ha de passar amb exit 0.

| Comprovació | Resultat |
|---|---|
| Fitxes `empreses/{ISIN}.md` | 1.040 / 1.040, un per ISIN de la base [V] |
| `index.csv` i `INDEX.md` coherents amb la base | OK (mateix conjunt de 1.040 ISIN) [V] |
| Enllaços interns markdown a fitxers existents | OK, tret del cas transitiu de `MANIFEST` si es regenera; es revalida després del manifest [V] |
| `python3 scripts/comprova_enllacos_cites.py` (sense `--live`) | exit 0; 46 files del registre i 1.040 fitxes; 0 problemes [V] |
| Valors permesos i capçaleres de fitxa | OK [V] |
| Files `fora_mostra_auditoria` | 3.890 [V] |
| Comptes principals vs v8r2 | 0 discrepàncies [V] |

La branca `main` d'aquest arbre local recull el commit d'instruccions aprovades i de la v8 r3. A GitHub, `main` s'ha de protegir abans d'usar Claude Code (vegeu `docs/PROTECCIO_BRANCA_MAIN.md`). Claude no pot tocar `main`.

## Revisió prèvia a la publicació (19/11/2026 10:18 CET, Europe/Madrid)

S'ha tornat a revisar l'arbre abans del push públic: cap secret ni clau, cap correu personal, cap ruta de PC local, cap PDF ni fitxer de text complet d'una font amb drets. Les cites del registre i de les fitxes són literals curtes amb URL. El camp més llarg de cita a la base (`font_classificacio_cita`) fa 437 caràcters. Les mencions a `IA_S3` als documents només afirmen que no s'ha fet servir cap clau.

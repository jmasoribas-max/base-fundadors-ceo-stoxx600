# Dashboard Fundadors — base v8 r3

Panell d'empreses del doctorat sobre Founder-CEO, unitat **ISIN-any**. Aquest repositori recull la base v8 r3, el sector ICB per ISIN (amb l'extensió del supersector de juny 2023 als anys 2024-2025 per als ISIN que ja el tenien), una fitxa per empresa i la documentació de treball.

Repositori **públic** (decisió de Jordi, 19/11/2026 10:18, CET, Europe/Madrid): tothom el pot veure; ningú de fora no el pot modificar. La branca `main` està protegida (PR obligatori, aprovació de Jordi i CODEOWNERS; cap push directe ni force push). Les instruccions de `CLAUDE.md` van ser aprovades per Jordi el 19/11/2026; l'extensió de sector, el mateix dia a les 10:06.

## Xifres principals [V]

- **6.012** files ISIN-any del panell (`fora_panel=0`).
- **1.040** ISIN.
- Anys **2016-2025**.
- FounderCEO (base actual, després del lot ND-1): **F 343**, **P 5.632**, **ND 6**, **NA 31** (F és el 5,74 % de F+P). A la v8 r3 d'origen: P 5.624 i ND 14 (F 5,75 %).
- Mostra principal J14 (panell, FounderCEO 0 o 1, no `dret_temporal`): **n=5.954**, **F=342** (v8 r3 d'origen; DF l'ha de recalcular després del lot ND-1).
- Certificació (àmbit de l'auditoria, 2.122 files; la resta del panell, **3.890**, és `fora_mostra_auditoria`):
  - certificades: **N1 740**, **N2 1.018**, **doctorat 15** (total **1.773**);
  - `ceo_pendent` **108**;
  - `no_certificada` **241**.

**Lot ND-1, fusionat a `main` el 19/11/2026 (PR #2, merge `edea674`):** 8 files passen de ND a P (B&M 2016-2021 i Steinhoff 2016-2017); a la base només ha canviat `FounderCEO`, i en queden 6 ND (Drillisch 2017, Sopra Steria 2025 i Aroundtown 2017-2020) amb la cerca documentada a la fitxa. **Pendent de DF** (no ho fa Claude): a les 8 files que han passat a P, `regles`, `motiu_nd`, `detall_motiu_nd`, `founderceo_rob_*` i `sim_*` encara tenen els valors de la v8 r3 (p. ex. `regles=cap`, `motiu_nd` ple i `founderceo_rob_na_com_0=no_determinat`); cal recalcular-les amb els scripts de DF, com les mostres (J14) i les robusteses, i regenerar l'`.xlsx`, que encara té les 14 ND de la v8 r3 [V]. La certificació d'aquestes files no ha canviat (`sim_estat_certificacio=no_certificada`). Detall a `docs/REGISTRE_CANVIS.md`, secció «Lot ND-1».

La v8 r3 d'origen no canvia cap d'aquestes xifres respecte a la v8 r2 / v8 r1 (després, el lot ND-1 ha canviat els recomptes de FounderCEO): només aplica l'extensió de sector aprovada i afegeix les columnes de robustesa `sector_estes_des_2023` i `supersector_fix`.

Valors de FounderCEO a la base: `1` (F), `0` (P), `no_determinat` (ND), `NA_sense_ceo` (NA).

## Protecció de `main` i flux de canvis

La branca `main` ha d'estar protegida i **Claude no la pot tocar mai** (ni push, ni commit, ni fusió, ni esmena directa). Tampoc no toca `scripts/`, `docs/METODOLOGIA.md`, `CLAUDE.md`, les regles ni `.github/`. Claude Code només treballa en branques, per lots d'empreses, i obre un pull request per lot.

El flux és:

1. Claude treballa en una branca, deixa a les fitxes i a `docs/REGISTRE_CANVIS` la cita literal, l'URL i el Wayback de cada canvi de dades, i passa `scripts/valida_pr.py`.
2. Obre un PR amb un resum. **No fusiona a `main`.**
3. **DF** valida.
4. **Doctorat** revisa la metodologia.
5. **Jordi** aprova.

Les instruccions per configurar la protecció de `main` a GitHub (PR obligatori, aprovació de Jordi, cap push directe i CODEOWNERS) són a [`docs/PROTECCIO_BRANCA_MAIN.md`](docs/PROTECCIO_BRANCA_MAIN.md). Les instruccions de treball per a Claude Code, aprovades per Jordi el 19/11/2026, són a [`CLAUDE.md`](CLAUDE.md).

## Com navegar-hi

| On | Què |
|---|---|
| [`INDEX.md`](INDEX.md) i [`index.csv`](index.csv) | Índex de les 1.040 empreses per nom i per ISIN, amb el sector i l'estat |
| [`empreses/`](empreses/) | Una fitxa `empreses/{ISIN}.md` per cada ISIN |
| [`dades/`](dades/) | Base `base_isin_any_v8r3.csv` / `.xlsx` i `sector_icb_v8r3.csv` |
| [`docs/DICCIONARI_CAMPS.md`](docs/DICCIONARI_CAMPS.md) | Diccionari de camps |
| [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md) | Resum de les regles R1-R3 i dels criteris N1/N2 (el que no està documentat es marca [NV]) |
| [`docs/REGISTRE_CANVIS.md`](docs/REGISTRE_CANVIS.md) | Registre de canvis i cites |
| [`docs/LIMITACIONS.md`](docs/LIMITACIONS.md) | Limitacions de la base |
| [`docs/QA.md`](docs/QA.md) | Control de qualitat |
| [`PENDENTS.md`](PENDENTS.md) | Feina pendent, amb l'ordre de treball |
| [`scripts/`](scripts/) | `comprova_enllacos_cites.py` i `valida_pr.py` (executar sense `--live` en local) |
| [`MANIFEST_SHA256.csv`](MANIFEST_SHA256.csv) | SHA-256 dels fitxers del repositori |

## Sector ICB (v8 r3)

Font: PDF públics de components amb supersector, 2015-juny 2023. SHA de la taula sectorial: `ddc3d037d796c4053700ce374148f134b09e071579875befe89e664e816899af` [V].

Decisió de Jordi (19/11/2026 10:06, CET, Europe/Madrid): s'estén el supersector del PDF de juny 2023 als anys 2024-2025, només per als ISIN que ja el tenien. Aquestes files porten `sector_estes_des_2023=1` i `any_font=2023` (1.076 files, 561 ISIN). Per excloure-les en una robustesa: `sector_estes_des_2023!=1`. El sector fix per empresa és `supersector_fix`.

Supòsit, [NV]: no hi ha hagut cap reclassificació ICB entre el 2023 i el 2025 (vegeu `docs/LIMITACIONS.md`).

A la base, per fila:

- `amb_sector` 5.825
- `revisar` 37
- `pendent_extensio_2024_2025` 47
- `revisar_pendent_extensio_2024_2025` 5
- `sense_sector` 98 (72 empreses: 48 només 2024-2025 i 24 no casades, pendents per a Claude amb una font A)

Les 25 empreses casades per via indirecta (`nom_stoxx_via_llista_seleccio`) queden marcades `revisar` o `revisar_pendent_extensio_2024_2025`. 33 ISIN tenen un sector d'una font anterior a juny 2023 i no s'han estès (52 files).

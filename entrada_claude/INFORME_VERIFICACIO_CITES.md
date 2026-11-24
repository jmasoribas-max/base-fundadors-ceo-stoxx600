# Informe de verificació de cites a les captures Wayback

Data de l'informe: 2026-11-24 07:34:34 CET (Europe/Madrid).
Tots els recomptes surten de `verificacio_cites_20261122.csv`. No s'ha inventat cap xifra.

## Abast

- Repositori `base-fundadors-ceo-stoxx600`, `main` = `6f871bb10c4575acfd7c74d8ed3c34c0a88d6e50`.
- Cites extretes del CSV de la base (`dades/base_isin_any_v8r3.csv`) i del registre (`docs/REGISTRE_CANVIS.csv`).
- Un parell = (ISIN, any, camp, URL, cita literal). Els anys del registre s'expandeixen (llistes i intervals) i només es queden els que són al panell.
- Parells únics escrits: 39.453.
- Files brutes abans de deduplicar: 39.489.
- Files del registre sense `url_font` (no entren als parells): 24.
- Resultats Wayback d'aquesta nit (`wayback_resultats_20261122.csv`, última línia per URL): 4.550 URL (ja_existia 3.850, capturada 700, error 0).

Camps de la base: `font_classificacio_url` + `font_classificacio_cita`; `d37_cita_contemp_url` + `d37_data_cita` (el camp `d37_cita_contemporania` és un flag, no una cita); `url_font` de sector (sense cita literal); `v75_urls_arxivades` (sense cita literal associada a la columna). Camps del registre: `registre.url_font/{funcio_cita}` amb `cita_literal`.

## Mètode

- S'ha fet servir la variant `id_` (contingut original) de cada `url_wayback` dels resultats. Sense claus d'archive.org, sense `-k`, sense archive.today ni bypass.
- Pausa mínima de 2 s entre descàrregues i backoff si Wayback respon 429.
- Text de PDF amb `pdftotext` (poppler, UTF-8; reintent `-raw` si el text és gairebé buit). HTML amb BeautifulSoup/lxml (s'eliminen script i style). Documents Office (zip) amb extracció simple de XML.
- Normalització: minúscules, ligadures, cometes tipogràfiques, guionets unificats, salts de línia amb guionet de partició de paraula, espais.
- `cita_ok` només si hi ha coincidència exacta de la cadena ja normalitzada. `cita_parcial` si el 85% o més dels tokens de la cita apareixen en una finestra de la mateixa longitud. La resta, `cita_no_trobada`.
- Si no hi ha cita literal: `sense_cita`. Si la URL no és als resultats d'aquesta nit o la captura no es pot llegir: `captura_no_llegible` (amb motiu a `detall`).

## Recomptes per estat (parells)

| Estat | Parells |
|---|---|
| `cita_ok` | 13.001 |
| `cita_parcial` | 295 |
| `cita_no_trobada` | 894 |
| `captura_no_llegible` | 12.512 |
| `sense_cita` | 12.751 |
| **Total** | **39.453** |

### Parells per grup FounderCEO i estat

| Grup | cita_ok | cita_parcial | cita_no_trobada | captura_no_llegible | sense_cita | Total |
|---|---|---|---|---|---|---|
| F | 1.157 | 11 | 13 | 152 | 753 | 2.086 |
| P | 11.318 | 277 | 874 | 12.322 | 11.952 | 36.743 |
| NA | 477 | 5 | 7 | 33 | 43 | 565 |
| ND | 49 | 2 | 0 | 5 | 3 | 59 |

## Recomptes per fila ISIN-any

Per a cada fila ISIN-any s'agafa l'estat més greu dels seus parells, en aquest ordre: `captura_no_llegible` > `cita_no_trobada` > `cita_parcial` > `cita_ok` > `sense_cita`.

| Estat pitjor | Files ISIN-any |
|---|---|
| `captura_no_llegible` | 3.559 |
| `cita_no_trobada` | 271 |
| `cita_parcial` | 88 |
| `cita_ok` | 767 |
| `sense_cita` | 1.326 |
| **Total** | **6.011** |

### Files ISIN-any per grup FounderCEO i estat pitjor

| Grup | Files | captura_no_llegible | cita_no_trobada | cita_parcial | cita_ok | sense_cita |
|---|---|---|---|---|---|---|
| F | 349 | 32 | 8 | 1 | 79 | 229 |
| P | 5.630 | 3.521 | 260 | 87 | 683 | 1.079 |
| NA | 31 | 5 | 3 | 0 | 5 | 18 |
| ND | 1 | 1 | 0 | 0 | 0 | 0 |

## Files F amb problemes (41)

S'hi llisten les files amb `FounderCEO=1` el pitjor estat de les quals no és `cita_ok` ni `sense_cita`.

### FR0000071946 2018 — Alten S.A. Actions au Porteur o.N.

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=9, sense_cita=2, cita_parcial=1, captura_no_llegible=1.
- `registre.url_font/ceo` · `cita_parcial` · score=0.912 tokens=31/34 · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf
  - Cita: «Simon AZOULAY Président-Directeur général Date de début de mandat : 22/09/1998 Date de fin de mandat : Assemblée à tenir en 2021 et appelée à statuer sur les comptes de l’exercice …»
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip
  - Cita: «Simon AZOULAY Président-Directeur général Date de début de mandat : 22/09/1998 Date de fin de mandat : Assemblée à tenir en 2025 et appelée à statuer sur les comptes de l’exercice …»

### FR0000071946 2019 — Alten S.A. Actions au Porteur EO 1,05

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=8, sense_cita=2, cita_parcial=1, captura_no_llegible=1.
- `registre.url_font/ceo` · `cita_parcial` · score=0.912 tokens=31/34 · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf
  - Cita: «Simon AZOULAY Président-Directeur général Date de début de mandat : 22/09/1998 Date de fin de mandat : Assemblée à tenir en 2021 et appelée à statuer sur les comptes de l’exercice …»
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip
  - Cita: «Simon AZOULAY Président-Directeur général Date de début de mandat : 22/09/1998 Date de fin de mandat : Assemblée à tenir en 2025 et appelée à statuer sur les comptes de l’exercice …»

### FR0000071946 2020 — Alten S.A. Actions au Porteur EO 1,05

- Estat pitjor: `cita_parcial`. Parells: cita_ok=4, sense_cita=2, cita_parcial=1.
- `registre.url_font/ceo` · `cita_parcial` · score=0.912 tokens=31/34 · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf
  - Cita: «Simon AZOULAY Président-Directeur général Date de début de mandat : 22/09/1998 Date de fin de mandat : Assemblée à tenir en 2021 et appelée à statuer sur les comptes de l’exercice …»

### FR0000071946 2021 — Alten S.A. Actions au Porteur EO 1,05

- Estat pitjor: `captura_no_llegible`. Parells: sense_cita=2, cita_no_trobada=2, cita_ok=1, captura_no_llegible=1.
- `registre.url_font/ceo` · `cita_no_trobada` · no_coincideix len_cita_norm=282 len_text_norm=8216 score=0.289 · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317442505_20220429.zip
  - Cita: «En 2002, le Conseil d’administration a décidé l’unicité des fonctions de Président du Conseil d’administration et de Directeur général. Cette décision n’a pas été modifiée depuis l…»
- `registre.url_font/datacio` · `cita_no_trobada` · no_coincideix len_cita_norm=120 len_text_norm=8216 score=0.500 · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317442505_20220429.zip
  - Cita: «nous avons effectué l’audit des comptes consolidés de la société ALTEN SA relatifs à l’exercice clos le 31 décembre 2021»
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip
  - Cita: «Simon AZOULAY Président-Directeur général Date de début de mandat : 22/09/1998 Date de fin de mandat : Assemblée à tenir en 2025 et appelée à statuer sur les comptes de l’exercice …»

### FR0000071946 2022 — Alten S.A. Actions au Porteur EO 1,05

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=3, sense_cita=2, captura_no_llegible=1.
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip
  - Cita: «Simon AZOULAY Président-Directeur général Date de début de mandat : 22/09/1998 Date de fin de mandat : Assemblée à tenir en 2025 et appelée à statuer sur les comptes de l’exercice …»

### FR0000071946 2023 — Alten S.A. Actions au Porteur EO 1,05

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=3, sense_cita=2, captura_no_llegible=1.
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip
  - Cita: «Simon AZOULAY Président-Directeur général Date de début de mandat : 22/09/1998 Date de fin de mandat : Assemblée à tenir en 2025 et appelée à statuer sur les comptes de l’exercice …»

### FR0000071946 2024 — Alten S.A. Actions au Porteur EO 1,05

- Estat pitjor: `captura_no_llegible`. Parells: captura_no_llegible=3, sense_cita=2, cita_ok=1.
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip
  - Cita: «Monsieur Simon AZOULAY exerce les fonctions de Président-Directeur général. Son mandat arrive à échéance lors de l’Assemblée générale annuelle 2025.»
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip
  - Cita: «Simon AZOULAY Président-Directeur général Date de début de mandat : 22/09/1998 Date de fin de mandat : Assemblée à tenir en 2025 et appelée à statuer sur les comptes de l’exercice …»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip
  - Cita: «Le Document d’enregistrement universel a été déposé le 25 avril 2025 auprès de l’AMF»

### FR0000121014 2016 — LVMH Moët Henn. L. Vuitton SE Actions Port.

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=49, sense_cita=5, captura_no_llegible=2.
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"annee_categorie_entreprise":"2024","date_creation":"1971-01-01","date_fermeture":null»
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"siren":"775670417","siren_conserve":null,"nom_complet":"LVMH MOET HENNESSY LOUIS VUITTON"»

### FR0000121014 2017 — LVMH Moët Henn. L. Vuitton SE Actions Port.

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=45, captura_no_llegible=6, sense_cita=5.
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://lvmh-com.cdn.prismic.io/lvmh-com/ZnL0L5m069VX147T_lvmh_ddr_va_2017-interactif.pdf
  - Cita: «Bernard Arnault has been Chairman and Chief Executive Officer of the Company since 1989.»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://lvmh-com.cdn.prismic.io/lvmh-com/ZnL0L5m069VX147T_lvmh_ddr_va_2017-interactif.pdf
  - Cita: «the Company is controlled by the Arnault Family Group, which controlled 46.84% of the share capital and 63.13% of the voting rights exercisable at Shareholders’ Meetings as of Dece…»
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://lvmh-com.cdn.prismic.io/lvmh-com/Zmh3UJm069VX1pT-_2017-financial-documents.pdf
  - Cita: «EXECUTIVE AND SUPERVISORY BODIES; STATUTORY AUDITORS AS OF DECEMBER 31, 2017 Board of Directors Executive Committee Performance Audit Committee Bernard Arnault Chairman and Chief E…»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://lvmh-com.cdn.prismic.io/lvmh-com/Zmh3UJm069VX1pT-_2017-financial-documents.pdf
  - Cita: «Consolidated revenue for fiscal year 2017 was 42,636 million euros, up 13% over the preceding fiscal year.»
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"annee_categorie_entreprise":"2024","date_creation":"1971-01-01","date_fermeture":null»
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"siren":"775670417","siren_conserve":null,"nom_complet":"LVMH MOET HENNESSY LOUIS VUITTON"»

### FR0000121014 2018 — LVMH Moët Henn. L. Vuitton SE Actions Port.

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=49, sense_cita=5, captura_no_llegible=2.
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"annee_categorie_entreprise":"2024","date_creation":"1971-01-01","date_fermeture":null»
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"siren":"775670417","siren_conserve":null,"nom_complet":"LVMH MOET HENNESSY LOUIS VUITTON"»

### FR0000121014 2019 — LVMH Moët Henn. L. Vuitton SE Actions Port.

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=49, sense_cita=5, captura_no_llegible=2.
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"annee_categorie_entreprise":"2024","date_creation":"1971-01-01","date_fermeture":null»
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"siren":"775670417","siren_conserve":null,"nom_complet":"LVMH MOET HENNESSY LOUIS VUITTON"»

### FR0000121014 2020 — LVMH Moët Henn. L. Vuitton SE Actions Port.

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=49, sense_cita=5, captura_no_llegible=2.
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"annee_categorie_entreprise":"2024","date_creation":"1971-01-01","date_fermeture":null»
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"siren":"775670417","siren_conserve":null,"nom_complet":"LVMH MOET HENNESSY LOUIS VUITTON"»

### FR0000121014 2021 — LVMH Moët Henn. L. Vuitton SE Actions

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=47, sense_cita=5, captura_no_llegible=4.
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://lvmh-com.cdn.prismic.io/lvmh-com/Zmcg25m069VX1m3P_financial-documents-december-31-2021.pdf
  - Cita: «EXECUTIVE AND SUPERVISORY BODIES; STATUTORY AUDITORS AS OF DECEMBER 31, 2021 Board of Directors Executive Committee Performance Audit Committee Bernard Arnault Chairman and Chief E…»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://lvmh-com.cdn.prismic.io/lvmh-com/Zmcg25m069VX1m3P_financial-documents-december-31-2021.pdf
  - Cita: «Revenue for the 2021 fiscal year was 64,215 million euros, up 44% from the previous fiscal year, which had been very hard hit by the impact of the Covid-19 pandemic.»
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"annee_categorie_entreprise":"2024","date_creation":"1971-01-01","date_fermeture":null»
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"siren":"775670417","siren_conserve":null,"nom_complet":"LVMH MOET HENNESSY LOUIS VUITTON"»

### FR0000121014 2022 — LVMH Moët Henn. L. Vuitton SE Actions Port.

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=47, sense_cita=5, captura_no_llegible=4.
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://lvmh-com.cdn.prismic.io/lvmh-com/ZmF-Fpm069VX1gVJ_deu-2022-va_vdef.pdf
  - Cita: «Bernard Arnault has been Chairman and Chief Executive Officer of the Company since 1989.»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://lvmh-com.cdn.prismic.io/lvmh-com/ZmF-Fpm069VX1gVJ_deu-2022-va_vdef.pdf
  - Cita: «The Company is controlled by the Arnault family group, which directly and indirectly held 48.18% of the share capital and 63.90% of the voting rights exercisable at Shareholders’ M…»
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"annee_categorie_entreprise":"2024","date_creation":"1971-01-01","date_fermeture":null»
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"siren":"775670417","siren_conserve":null,"nom_complet":"LVMH MOET HENNESSY LOUIS VUITTON"»

### FR0000121014 2023 — LVMH Moët Henn. L. Vuitton SE Actions Port.

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=49, sense_cita=5, captura_no_llegible=2.
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"annee_categorie_entreprise":"2024","date_creation":"1971-01-01","date_fermeture":null»
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"siren":"775670417","siren_conserve":null,"nom_complet":"LVMH MOET HENNESSY LOUIS VUITTON"»

### FR0000121014 2024 — LVMH Moët Henn. L. Vuitton SE Actions Port.

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=50, sense_cita=5, captura_no_llegible=2.
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"annee_categorie_entreprise":"2024","date_creation":"1971-01-01","date_fermeture":null»
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"siren":"775670417","siren_conserve":null,"nom_complet":"LVMH MOET HENNESSY LOUIS VUITTON"»

### FR0000121014 2025 — LVMH Moët Henn. L. Vuitton SE Actions Port.

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=51, sense_cita=5, captura_no_llegible=2.
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"annee_categorie_entreprise":"2024","date_creation":"1971-01-01","date_fermeture":null»
- `registre.url_font/fundador` · `captura_no_llegible` · binari_no_llegible:content_type=application/json:bytes=6368 · URL: https://recherche-entreprises.api.gouv.fr/search?q=775670417
  - Cita: «"siren":"775670417","siren_conserve":null,"nom_complet":"LVMH MOET HENNESSY LOUIS VUITTON"»

### GB0000031285 2016 — Aberdeen Asset Management PLC Registered

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=48, captura_no_llegible=39, cita_no_trobada=3, cita_parcial=2, sense_cita=1.
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-310720-122652-1
  - Cita: «The Chief Executive, Martin Gilbert, is responsible for the day to day management of the Group.»
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-310720-122652-1
  - Cita: «M J Gilbert Chief Executive 27 November 2016»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-310720-122652-1
  - Cita: «Roger Cornick, who had been Chairman since 2009, stepped down on 30 September 2016 and was replaced by Simon Troughton, who was previously Senior Independent Non-Executive Director…»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-310720-122652-1
  - Cita: «The financial statements on pages 92 to 152 were approved by the Board of Directors on 27 November 2016, and signed on its behalf by:»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-310720-122652-1
  - Cita: «Martin trained as a chartered accountant prior to moving into investment management with an Aberdeen firm of solicitors. He is a founding director and shareholder of the Group.»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-310720-122652-1
  - Cita: «Martin was appointed to the Board on 1 July 1983.»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-310720-122652-1
  - Cita: «Formed in 1983, we have around 2,700 employees, manage £312.1 billion of assets as at 30 September 2016, and are one of Europe's largest investment managers.»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-310720-122652-1
  - Cita: «The roles of the Chairman and Chief Executive are separate, clearly defined and have been approved by the Board.»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-310720-122652-1
  - Cita: «Simon was appointed to the Board on 29 July 2009 and was appointed Chairman on 1 October 2016.»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-310720-122652-1
  - Cita: «The scale of Aberdeen’s operations, locally and internationally, has changed dramatically since it was founded in 1983.»
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-300720-122606-1
  - Cita: «Martin Gilbert, Chief Executive of Aberdeen Asset Management, commented:»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-300720-122606-1
  - Cita: «Interim Results for six months to 31 March 2017»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-300720-122606-1
  - Cita: «Simon Troughton Chairman 28 April 2017»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-300720-122606-1
  - Cita: «Further information on the proposed merger will be sent to shareholders shortly, and completion is expected during the fourth quarter of the Group’s financial year, subject to rele…»
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/RNS/a19c5ee2-2581-483c-8e30-a201791a0849.html
  - Cita: «Martin Gilbert has a long history in asset and wealth management. He co-founded Aberdeen Asset Management PLC in 1983 and was chief executive officer from 1991 to 2017.»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/RNS/a19c5ee2-2581-483c-8e30-a201791a0849.html
  - Cita: «He co-founded Aberdeen Asset Management PLC in 1983 and was chief executive officer from 1991 to 2017.»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/RNS/a19c5ee2-2581-483c-8e30-a201791a0849.html
  - Cita: «RNS Number : 7517W River Global PLC 16 March 2026»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-310720-122690-1
  - Cita: «Martin trained as a chartered accountant prior to moving into investment management with an Aberdeen firm of solicitors. He is a founding director and shareholder of the Group.»
- `registre.url_font/fundador` · `captura_no_llegible` · pdftotext_error:Syntax Error: Couldn't find trailer dictionary
Syntax Error: Invalid XRef entry 3684
Syntax Error: Invalid XRef entry 3608
Syntax Error: Top-level pages object is wrong type (null)
Command Line Error: · URL: https://www.aberdeenplc.com/docs?documentId=GB-270720-122140-1
  - Cita: «Martin was appointed Director and Co-Chief Executive on 14 August 2017. He is co-founder (and former chief executive) of Aberdeen Asset Management PLC and has been a director since…»
- `registre.url_font/context` · `captura_no_llegible` · pdftotext_error:Syntax Error: Couldn't find trailer dictionary
Syntax Error: Invalid XRef entry 3684
Syntax Error: Invalid XRef entry 3608
Syntax Error: Top-level pages object is wrong type (null)
Command Line Error: · URL: https://www.aberdeenplc.com/docs?documentId=GB-270720-122140-1
  - Cita: «The merger of Standard Life plc and Aberdeen Asset Management PLC (Aberdeen) completed on 14 August 2017, with the merger accounted for as an acquisition of Aberdeen by Standard Li…»
- `registre.url_font/fundador` · `cita_parcial` · score=1.000 tokens=10/10 · URL: https://find-and-update.company-information.service.gov.uk/company/SC082015
  - Cita: «ABERDEEN FUND MANAGERS LIMITED 02 Mar 1983 - 23 Dec 1987»
- `registre.url_font/context` · `cita_parcial` · score=1.000 tokens=10/10 · URL: https://find-and-update.company-information.service.gov.uk/company/SC082015
  - Cita: «ABERDEEN ASSET MANAGEMENT PLC 01 May 1997 - 25 Nov 2022»
- `registre.url_font/datacio` · `cita_no_trobada` · no_coincideix len_cita_norm=43 len_text_norm=6606 score=0.571 · URL: https://ioandc.com/the-aberdeen-story-why-history-matters/
  - Cita: «Investor Strategy News Sunday 25th Sep 2016»
- `registre.url_font/datacio` · `cita_no_trobada` · no_coincideix len_cita_norm=90 len_text_norm=6606 score=0.538 · URL: https://ioandc.com/the-aberdeen-story-why-history-matters/
  - Cita: «The Aberdeen story: why history matters Analysis (pictured: Martin Gilbert) by Greg Bright»
- `registre.url_font/fundador` · `cita_no_trobada` · no_coincideix len_cita_norm=267 len_text_norm=4606 score=0.833 · URL: https://uk.finance.yahoo.com/news/1-martin-gilbert-step-down-064228989.html
  - Cita: «Gilbert oversaw the meteoric rise of Aberdeen Asset Management, the small company he co-founded in 1983 with just 50 million pounds in assets, to what became the country's biggest …»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://archive.news.stv.tv/north/1441232-boss-to-leave-standard-life-aberdeen-after-three-decades.html
  - Cita: «Mr Gilbert is co-founder of Aberdeen Asset Management, running the firm since 1983, and was instrumental in its merger with Standard Life in 2017.»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://archive.news.stv.tv/north/1441232-boss-to-leave-standard-life-aberdeen-after-three-decades.html
  - Cita: «He said: "It has been an incredible journey, almost unimaginable from the earliest days when we were just three people in one office in Aberdeen with £50m under management to today…»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://archive.news.stv.tv/north/1441232-boss-to-leave-standard-life-aberdeen-after-three-decades.html
  - Cita: «This story has been archived. It was originally published by STV News on 02 Oct 2019.»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-200720-121520-1
  - Cita: «Aberdeen was established in 1983 by a group of investors, including its current Chief Executive, Martin Gilbert.»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-200720-121520-1
  - Cita: «Since it was formed in 1983, Aberdeen's management and staff have, with the support of its shareholders and clients, transformed the firm into a leading global asset manager.»
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-200720-121520-1
  - Cita: «Commenting on the Merger, Martin Gilbert, CEO of Aberdeen said:»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-200720-121520-1
  - Cita: «6 March 2017 Recommended All-Share Merger of Standard Life plc and Aberdeen Asset Management PLC»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-200720-121520-1
  - Cita: «The Boards of Standard Life plc (“Standard Life”) and Aberdeen Asset Management PLC (“Aberdeen”) are pleased to announce that they have reached agreement on the terms of a recommen…»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-200720-121520-1
  - Cita: «“Aberdeen” Aberdeen Asset Management PLC, incorporated in Scotland with registered number SC082015.»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://www.aberdeenplc.com/docs?documentId=GB-200720-121520-1
  - Cita: «A copy of this Announcement is and will be available, subject to certain restrictions relating to persons resident in Restricted Jurisdictions, for inspection on Standard Life’s we…»
- `registre.url_font/fundador` · `captura_no_llegible` · pdftotext_error:Syntax Error: Invalid XRef entry 798
Internal Error: xref num 798 not found but needed, try to reconstruct
Syntax Error: Invalid XRef entry 759
Syntax Error: Top-level pages object is wrong type (null · URL: https://www.abrdn.com/docs?documentId=GB-310720-122735-1
  - Cita: «Martin trained as a chartered accountant prior to moving into investment management with an Aberdeen firm of solicitors. He is a founding director and shareholder of the Company.»
- `registre.url_font/datacio` · `captura_no_llegible` · pdftotext_error:Syntax Error: Invalid XRef entry 798
Internal Error: xref num 798 not found but needed, try to reconstruct
Syntax Error: Invalid XRef entry 759
Syntax Error: Top-level pages object is wrong type (null · URL: https://www.abrdn.com/docs?documentId=GB-310720-122735-1
  - Cita: «M J Gilbert Chief Executive 28 November 2014»
- `registre.url_font/datacio` · `captura_no_llegible` · pdftotext_error:Syntax Error: Invalid XRef entry 798
Internal Error: xref num 798 not found but needed, try to reconstruct
Syntax Error: Invalid XRef entry 759
Syntax Error: Top-level pages object is wrong type (null · URL: https://www.abrdn.com/docs?documentId=GB-310720-122735-1
  - Cita: «Aberdeen Asset Management PLC Annual Report and Accounts 2014»
- `registre.url_font/fundador` · `captura_no_llegible` · pdftotext_error:Syntax Error: Couldn't find trailer dictionary
Syntax Error: Invalid XRef entry 3302
Syntax Error: Invalid XRef entry 3238
Syntax Error: Top-level pages object is wrong type (null)
Command Line Error: · URL: https://www.aberdeenplc.com/docs?documentId=GB-300720-122474-1
  - Cita: «He is co-founder (and former chief executive) of Aberdeen Asset Management PLC, having been a director since 1983.»
- `registre.url_font/datacio` · `captura_no_llegible` · pdftotext_error:Syntax Error: Couldn't find trailer dictionary
Syntax Error: Invalid XRef entry 3302
Syntax Error: Invalid XRef entry 3238
Syntax Error: Top-level pages object is wrong type (null)
Command Line Error: · URL: https://www.aberdeenplc.com/docs?documentId=GB-300720-122474-1
  - Cita: «Kenneth A Gilmour Company Secretary, Standard Life Aberdeen plc (SC286832) 13 March 2019»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/company/SC082015/filing-history?page=36
  - Cita: «Company name changed\certificate issued on 13/04/83»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/company/SC082015/filing-history?page=36
  - Cita: «Accounts made up to 30 September 1984»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.investegate.co.uk/announcement/rns/aberdeen-group-plc--abdn/standard-life-and-aberdeen-agree-terms/5062726
  - Cita: «History of the Aberdeen Group Aberdeen was established in 1983 by a group of investors, including its current Chief Executive, Martin Gilbert.»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.investegate.co.uk/announcement/rns/aberdeen-group-plc--abdn/standard-life-and-aberdeen-agree-terms/5062726
  - Cita: «Standard Life and Aberdeen agree Terms Standard Life plc 06 March 2017»

### GB0002869419 2021 — Big Yellow Group PLC Registered Shares LS

- Estat pitjor: `cita_no_trobada`. Parells: sense_cita=1, cita_no_trobada=1.
- `font_classificacio_url` · `cita_no_trobada` · no_coincideix len_cita_norm=50 len_text_norm=82 score=0.000 · URL: https://corporate.bigyellow.co.uk/about-us/our-management
  - Cita: «following the retirement of co-founder Jim Gibson.»

### GB0002869419 2022 — Big Yellow Group PLC Registered Shares LS

- Estat pitjor: `cita_no_trobada`. Parells: sense_cita=1, cita_no_trobada=1.
- `font_classificacio_url` · `cita_no_trobada` · no_coincideix len_cita_norm=50 len_text_norm=82 score=0.000 · URL: https://corporate.bigyellow.co.uk/about-us/our-management
  - Cita: «following the retirement of co-founder Jim Gibson.»

### GB0002869419 2023 — Big Yellow Group PLC Registered Shares LS

- Estat pitjor: `cita_no_trobada`. Parells: sense_cita=1, cita_no_trobada=1.
- `font_classificacio_url` · `cita_no_trobada` · no_coincideix len_cita_norm=50 len_text_norm=82 score=0.000 · URL: https://corporate.bigyellow.co.uk/about-us/our-management
  - Cita: «following the retirement of co-founder Jim Gibson.»

### GB0002869419 2024 — Big Yellow Group PLC Registered Shares LS

- Estat pitjor: `cita_no_trobada`. Parells: sense_cita=1, cita_no_trobada=1.
- `font_classificacio_url` · `cita_no_trobada` · no_coincideix len_cita_norm=50 len_text_norm=82 score=0.000 · URL: https://corporate.bigyellow.co.uk/about-us/our-management
  - Cita: «following the retirement of co-founder Jim Gibson.»

### GB0002869419 2025 — Big Yellow Group PLC Registered Shares LS

- Estat pitjor: `cita_no_trobada`. Parells: sense_cita=1, cita_no_trobada=1.
- `font_classificacio_url` · `cita_no_trobada` · no_coincideix len_cita_norm=50 len_text_norm=82 score=0.000 · URL: https://corporate.bigyellow.co.uk/about-us/our-management
  - Cita: «following the retirement of co-founder Jim Gibson.»

### GB00B17BBQ50 2016 — Investec PLC Registered Shares LS -,00022)

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=4, sense_cita=1, captura_no_llegible=1.
- `registre.url_font/ceo` · `captura_no_llegible` · pdftotext_error:Syntax Error: Couldn't find trailer dictionary
Syntax Error: Invalid XRef entry 8324
Syntax Error: Invalid XRef entry 8274
Syntax Error: Top-level pages object is wrong type (null)
Command Line Error: · URL: https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2019/investec-dlc-vol-1-annual-report-2019.pdf
  - Cita: «S Koseff stepped down as group CEO on 1 October 2018.»

### GB00B17BBQ50 2017 — Investec PLC Registered Shares LS -,00022)

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=3, sense_cita=1, captura_no_llegible=1.
- `registre.url_font/ceo` · `captura_no_llegible` · pdftotext_error:Syntax Error: Couldn't find trailer dictionary
Syntax Error: Invalid XRef entry 8324
Syntax Error: Invalid XRef entry 8274
Syntax Error: Top-level pages object is wrong type (null)
Command Line Error: · URL: https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2019/investec-dlc-vol-1-annual-report-2019.pdf
  - Cita: «S Koseff stepped down as group CEO on 1 October 2018.»

### GB00BNC5T391 2021 — Deliveroo PLC Registered Shares

- Estat pitjor: `cita_no_trobada`. Parells: cita_ok=7, sense_cita=1, cita_no_trobada=1.
- `registre.url_font/ceo` · `cita_no_trobada` · no_coincideix len_cita_norm=108 len_text_norm=698593 score=0.722 · URL: https://data.fca.org.uk/artefacts/NSM/Portal/NI-000092427/NI-000092427.pdf
  - Cita: «Will Shu Chief Executive Officer Appointed as CEO: 1 February 2013 Appointed to Deliveroo plc: 19 March 2021»

### IT0005619678 2024 — Reply S.p.A. Anrechte

- Estat pitjor: `captura_no_llegible`. Parells: captura_no_llegible=3, cita_ok=3.
- `registre.url_font/fundador` · `captura_no_llegible` · url_absent_als_resultats_wayback_20261122 · URL: https://www.reply.com/contents/REP25_Bilancio_ENG_2024.pdf
  - Cita: «Mario Rizzante (Chairman, CEO and Founder of Reply S.p.A.):»
- `registre.url_font/fundador` · `captura_no_llegible` · url_absent_als_resultats_wayback_20261122 · URL: https://www.reply.com/contents/REP25_Bilancio_ENG_2024.pdf
  - Cita: «Tatiana Rizzante (CEO, Reply S.p.A.): Computer Engineering graduate and co-founder of Reply.»
- `registre.url_font/context` · `captura_no_llegible` · url_absent_als_resultats_wayback_20261122 · URL: https://dam-media.reply.com/contents/REP24_Avviso_di_offerta_in_opzione_e_prelazione_IT.pdf
  - Cita: «I Diritti di opzioni, ISIN n. IT0005619678, non sono negoziabili su alcun mercato o sistema multilaterale di negoziazione»

### JE00B8KF9B49 2016 — WPP PLC Registered Shares LS -,10

- Estat pitjor: `cita_no_trobada`. Parells: sense_cita=1, cita_ok=1, cita_no_trobada=1.
- `d37_cita_contemp_url` · `cita_no_trobada` · no_coincideix len_cita_norm=10 len_text_norm=6211 score=0.000 · URL: https://www.wpp.com/en/news/2015/06/wpp-and-aston-martin-to-create-bespoke-team-in-global-collaboration
  - Cita: «2017-06-14»

### JE00B8KF9B49 2017 — WPP PLC Registered Shares LS -,10

- Estat pitjor: `cita_no_trobada`. Parells: sense_cita=1, cita_ok=1, cita_no_trobada=1.
- `d37_cita_contemp_url` · `cita_no_trobada` · no_coincideix len_cita_norm=10 len_text_norm=6211 score=0.000 · URL: https://www.wpp.com/en/news/2015/06/wpp-and-aston-martin-to-create-bespoke-team-in-global-collaboration
  - Cita: «2017-06-14»

### LU1072616219 2016 — B & M Europ.Value Retail S.A. Actions

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=49, captura_no_llegible=8, sense_cita=1, cita_parcial=1.
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://bandmretail-ar2017.html.investis.com/publication/contents/pdfweb.pdf
  - Cita: «Simon Arora, as the CEO, together with Paul McDonald as the CFO, is responsible for the day-to-day management of the Group and implementation of strategy approved by the Board and …»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://bandmretail-ar2017.html.investis.com/publication/contents/pdfweb.pdf
  - Cita: «The 2015/16 year is for the 52 weeks ended 26 March 2016 and the 2016/17 year is for the 52 weeks ended 25 March 2017.»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://bandmretail-ar2017.html.investis.com/publication/contents/pdfweb.pdf
  - Cita: «the Board has successfully led the transition of the business from a founder family private business to a public listed company over the last 3 years, establishing effective and st…»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «Simon ARORA Filter appointments Filter appointments, selecting an input will reload the page. Current appointments Total number of appointments 11 Date of birth November 1969»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «B & M RETAIL LIMITED (01357507) Company status Active Correspondence address Finance Director, The Vault, Dakota Drive, Estuary Commerce Park, Speke, Liverpool, Merseyside, L24 8RJ…»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «B&M EUROPEAN VALUE RETAIL HOLDCO 3 LTD (08309890)»
- `registre.url_font/context` · `cita_parcial` · score=1.000 tokens=12/12 · URL: https://find-and-update.company-information.service.gov.uk/company/01357507
  - Cita: «B. & M. BARGAINS (W & R) LIMITED 31 Dec 1978 - 09 Jul 1997»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/DirectUpload/NI-000139695/NI-000139695.pdf
  - Cita: «The business was founded in 1978 with the first store opening in Blackpool»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/DirectUpload/NI-000139695/NI-000139695.pdf
  - Cita: «B&M was acquired by Simon and Bobby Arora in December 2004 from Phildrew Investments, at which time the Company traded from just 21 stores»

### LU1072616219 2017 — B & M Europ.Value Retail S.A. Actions

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=52, captura_no_llegible=6, sense_cita=1, cita_parcial=1.
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://bandmretail-ar2017.html.investis.com/publication/contents/pdfweb.pdf
  - Cita: «the Board has successfully led the transition of the business from a founder family private business to a public listed company over the last 3 years, establishing effective and st…»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «Simon ARORA Filter appointments Filter appointments, selecting an input will reload the page. Current appointments Total number of appointments 11 Date of birth November 1969»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «B & M RETAIL LIMITED (01357507) Company status Active Correspondence address Finance Director, The Vault, Dakota Drive, Estuary Commerce Park, Speke, Liverpool, Merseyside, L24 8RJ…»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «B&M EUROPEAN VALUE RETAIL HOLDCO 3 LTD (08309890)»
- `registre.url_font/context` · `cita_parcial` · score=1.000 tokens=12/12 · URL: https://find-and-update.company-information.service.gov.uk/company/01357507
  - Cita: «B. & M. BARGAINS (W & R) LIMITED 31 Dec 1978 - 09 Jul 1997»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/DirectUpload/NI-000139695/NI-000139695.pdf
  - Cita: «The business was founded in 1978 with the first store opening in Blackpool»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/DirectUpload/NI-000139695/NI-000139695.pdf
  - Cita: «B&M was acquired by Simon and Bobby Arora in December 2004 from Phildrew Investments, at which time the Company traded from just 21 stores»

### LU1072616219 2018 — B & M Europ.Value Retail S.A. Actions

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=49, captura_no_llegible=8, sense_cita=1, cita_parcial=1.
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://bandmretail-ar2017.html.investis.com/publication/contents/pdfweb.pdf
  - Cita: «the Board has successfully led the transition of the business from a founder family private business to a public listed company over the last 3 years, establishing effective and st…»
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://staticcontents.investis.com/html/b/bandmretail/annual-report-and-accounts-2019/publication/contents/pdfweb.pdf
  - Cita: «Simon Arora, as the Group CEO, is responsible for the day-to-day management of the Group and implementation of strategy approved by the Board and implementation of other Board deci…»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://staticcontents.investis.com/html/b/bandmretail/annual-report-and-accounts-2019/publication/contents/pdfweb.pdf
  - Cita: «The 2017/18 year is for the 53 weeks ended 31 March 2018 and the 2018/19 year is for the 52 weeks ended 30 March 2019.»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «Simon ARORA Filter appointments Filter appointments, selecting an input will reload the page. Current appointments Total number of appointments 11 Date of birth November 1969»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «B & M RETAIL LIMITED (01357507) Company status Active Correspondence address Finance Director, The Vault, Dakota Drive, Estuary Commerce Park, Speke, Liverpool, Merseyside, L24 8RJ…»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «B&M EUROPEAN VALUE RETAIL HOLDCO 3 LTD (08309890)»
- `registre.url_font/context` · `cita_parcial` · score=1.000 tokens=12/12 · URL: https://find-and-update.company-information.service.gov.uk/company/01357507
  - Cita: «B. & M. BARGAINS (W & R) LIMITED 31 Dec 1978 - 09 Jul 1997»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/DirectUpload/NI-000139695/NI-000139695.pdf
  - Cita: «The business was founded in 1978 with the first store opening in Blackpool»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/DirectUpload/NI-000139695/NI-000139695.pdf
  - Cita: «B&M was acquired by Simon and Bobby Arora in December 2004 from Phildrew Investments, at which time the Company traded from just 21 stores»

### LU1072616219 2019 — B & M Europ.Value Retail S.A. Actions

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=49, captura_no_llegible=8, sense_cita=1, cita_parcial=1.
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://bandmretail-ar2017.html.investis.com/publication/contents/pdfweb.pdf
  - Cita: «the Board has successfully led the transition of the business from a founder family private business to a public listed company over the last 3 years, establishing effective and st…»
- `registre.url_font/ceo` · `captura_no_llegible` · http_404 · URL: https://staticcontents.investis.com/html/b/bandmretail/annual-report-and-accounts-2020/publication/contents/pdfweb.pdf
  - Cita: «Simon Arora, as the Group CEO, is responsible for the day-to-day management of the Group and implementation of strategy approved by the Board and other Board decisions.»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://staticcontents.investis.com/html/b/bandmretail/annual-report-and-accounts-2020/publication/contents/pdfweb.pdf
  - Cita: «The 2018/19 year is for the 52 weeks ended 30 March 2019 and the 2019/20 year is for the 52 weeks ended 28 March 2020.»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «Simon ARORA Filter appointments Filter appointments, selecting an input will reload the page. Current appointments Total number of appointments 11 Date of birth November 1969»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «B & M RETAIL LIMITED (01357507) Company status Active Correspondence address Finance Director, The Vault, Dakota Drive, Estuary Commerce Park, Speke, Liverpool, Merseyside, L24 8RJ…»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «B&M EUROPEAN VALUE RETAIL HOLDCO 3 LTD (08309890)»
- `registre.url_font/context` · `cita_parcial` · score=1.000 tokens=12/12 · URL: https://find-and-update.company-information.service.gov.uk/company/01357507
  - Cita: «B. & M. BARGAINS (W & R) LIMITED 31 Dec 1978 - 09 Jul 1997»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/DirectUpload/NI-000139695/NI-000139695.pdf
  - Cita: «The business was founded in 1978 with the first store opening in Blackpool»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/DirectUpload/NI-000139695/NI-000139695.pdf
  - Cita: «B&M was acquired by Simon and Bobby Arora in December 2004 from Phildrew Investments, at which time the Company traded from just 21 stores»

### LU1072616219 2020 — B & M Europ.Value Retail S.A. Actions

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=51, captura_no_llegible=6, sense_cita=1, cita_parcial=1.
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://bandmretail-ar2017.html.investis.com/publication/contents/pdfweb.pdf
  - Cita: «the Board has successfully led the transition of the business from a founder family private business to a public listed company over the last 3 years, establishing effective and st…»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «Simon ARORA Filter appointments Filter appointments, selecting an input will reload the page. Current appointments Total number of appointments 11 Date of birth November 1969»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «B & M RETAIL LIMITED (01357507) Company status Active Correspondence address Finance Director, The Vault, Dakota Drive, Estuary Commerce Park, Speke, Liverpool, Merseyside, L24 8RJ…»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «B&M EUROPEAN VALUE RETAIL HOLDCO 3 LTD (08309890)»
- `registre.url_font/context` · `cita_parcial` · score=1.000 tokens=12/12 · URL: https://find-and-update.company-information.service.gov.uk/company/01357507
  - Cita: «B. & M. BARGAINS (W & R) LIMITED 31 Dec 1978 - 09 Jul 1997»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/DirectUpload/NI-000139695/NI-000139695.pdf
  - Cita: «The business was founded in 1978 with the first store opening in Blackpool»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/DirectUpload/NI-000139695/NI-000139695.pdf
  - Cita: «B&M was acquired by Simon and Bobby Arora in December 2004 from Phildrew Investments, at which time the Company traded from just 21 stores»

### LU1072616219 2021 — B & M Europ.Value Retail S.A. Actions

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=53, captura_no_llegible=6, sense_cita=1, cita_parcial=1.
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://bandmretail-ar2017.html.investis.com/publication/contents/pdfweb.pdf
  - Cita: «the Board has successfully led the transition of the business from a founder family private business to a public listed company over the last 3 years, establishing effective and st…»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «Simon ARORA Filter appointments Filter appointments, selecting an input will reload the page. Current appointments Total number of appointments 11 Date of birth November 1969»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «B & M RETAIL LIMITED (01357507) Company status Active Correspondence address Finance Director, The Vault, Dakota Drive, Estuary Commerce Park, Speke, Liverpool, Merseyside, L24 8RJ…»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://find-and-update.company-information.service.gov.uk/officers/0UHPDh6qiuM-U6VMTUbmiXkJkRU/appointments
  - Cita: «B&M EUROPEAN VALUE RETAIL HOLDCO 3 LTD (08309890)»
- `registre.url_font/context` · `cita_parcial` · score=1.000 tokens=12/12 · URL: https://find-and-update.company-information.service.gov.uk/company/01357507
  - Cita: «B. & M. BARGAINS (W & R) LIMITED 31 Dec 1978 - 09 Jul 1997»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/DirectUpload/NI-000139695/NI-000139695.pdf
  - Cita: «The business was founded in 1978 with the first store opening in Blackpool»
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://data.fca.org.uk/artefacts/NSM/DirectUpload/NI-000139695/NI-000139695.pdf
  - Cita: «B&M was acquired by Simon and Bobby Arora in December 2004 from Phildrew Investments, at which time the Company traded from just 21 stores»

### NL0012866412 2020 — BE Semiconductor Inds N.V. Aandelen op

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=26, captura_no_llegible=5, sense_cita=2.
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «A take-over has been one of the scenarios for Besi in recent years, as no plan of succession has ever been presented for CEO/Founder [Richard] Blickman»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «analysts for Degroof Petercam said in a note on Friday.»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «By Milana Vinn and Amy-Jo Crowley»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «NEW YORK/LONDON, March 13 (Reuters) - BE Semiconductor Industries BESI.AS has attracted takeover interest as its chip-packaging technology becomes increasingly strategic for semico…»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «"pubTime":"2026-03-13 21:51"»

### NL0012866412 2021 — BE Semiconductor Inds N.V. Aandelen op

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=26, captura_no_llegible=5, sense_cita=2.
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «A take-over has been one of the scenarios for Besi in recent years, as no plan of succession has ever been presented for CEO/Founder [Richard] Blickman»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «analysts for Degroof Petercam said in a note on Friday.»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «By Milana Vinn and Amy-Jo Crowley»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «NEW YORK/LONDON, March 13 (Reuters) - BE Semiconductor Industries BESI.AS has attracted takeover interest as its chip-packaging technology becomes increasingly strategic for semico…»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «"pubTime":"2026-03-13 21:51"»

### NL0012866412 2022 — BE Semiconductor Inds N.V. Aandelen op

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=26, captura_no_llegible=5, sense_cita=2.
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «A take-over has been one of the scenarios for Besi in recent years, as no plan of succession has ever been presented for CEO/Founder [Richard] Blickman»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «analysts for Degroof Petercam said in a note on Friday.»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «By Milana Vinn and Amy-Jo Crowley»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «NEW YORK/LONDON, March 13 (Reuters) - BE Semiconductor Industries BESI.AS has attracted takeover interest as its chip-packaging technology becomes increasingly strategic for semico…»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «"pubTime":"2026-03-13 21:51"»

### NL0012866412 2023 — BE Semiconductor Inds N.V. Aandelen op

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=26, captura_no_llegible=5, sense_cita=2.
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «A take-over has been one of the scenarios for Besi in recent years, as no plan of succession has ever been presented for CEO/Founder [Richard] Blickman»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «analysts for Degroof Petercam said in a note on Friday.»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «By Milana Vinn and Amy-Jo Crowley»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «NEW YORK/LONDON, March 13 (Reuters) - BE Semiconductor Industries BESI.AS has attracted takeover interest as its chip-packaging technology becomes increasingly strategic for semico…»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «"pubTime":"2026-03-13 21:51"»

### NL0012866412 2024 — BE Semiconductor Inds N.V. Aandelen op

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=26, captura_no_llegible=5, sense_cita=2.
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «A take-over has been one of the scenarios for Besi in recent years, as no plan of succession has ever been presented for CEO/Founder [Richard] Blickman»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «analysts for Degroof Petercam said in a note on Friday.»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «By Milana Vinn and Amy-Jo Crowley»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «NEW YORK/LONDON, March 13 (Reuters) - BE Semiconductor Industries BESI.AS has attracted takeover interest as its chip-packaging technology becomes increasingly strategic for semico…»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «"pubTime":"2026-03-13 21:51"»

### NL0012866412 2025 — BE Semiconductor Inds N.V. Aandelen op

- Estat pitjor: `captura_no_llegible`. Parells: cita_ok=27, captura_no_llegible=5, sense_cita=2.
- `registre.url_font/fundador` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «A take-over has been one of the scenarios for Besi in recent years, as no plan of succession has ever been presented for CEO/Founder [Richard] Blickman»
- `registre.url_font/context` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «analysts for Degroof Petercam said in a note on Friday.»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «By Milana Vinn and Amy-Jo Crowley»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «NEW YORK/LONDON, March 13 (Reuters) - BE Semiconductor Industries BESI.AS has attracted takeover interest as its chip-packaging technology becomes increasingly strategic for semico…»
- `registre.url_font/datacio` · `captura_no_llegible` · http_404 · URL: https://www.itiger.com/news/2619711899
  - Cita: «"pubTime":"2026-03-13 21:51"»

## 10 exemples aleatoris de `cita_no_trobada` (llavor 20261122)

N'hi ha 894 en total. Mostra per revisar a mà:

### Exemple 1

- ISIN-any: `AT0000BAWAG2` 2025 (BAWAG Group AG Inhaber-Aktien o.N., FounderCEO=0)
- Camp: `registre.url_font/datacio`
- URL: https://www.bawaggroup.com/resource/blob/36212/73684de813a32b65d5ba7a03a63bbeb8/cv-anas-abuzaakouk-data-data.pdf
- URL Wayback: https://web.archive.org/web/20260211100215id_/https://www.bawaggroup.com/resource/blob/36212/73684de813a32b65d5ba7a03a63bbeb8/cv-anas-abuzaakouk-data-data.pdf
- Detall: no_coincideix len_cita_norm=39 len_text_norm=1314 score=0.600
- Cita: «Chief Restructuring Officer 2012 – 2013»

### Exemple 2

- ISIN-any: `BE0974464977` 2024 (Syensqo S.A. Actions au Porteur o.N., FounderCEO=0)
- Camp: `registre.url_font/context`
- URL: https://www.syensqo.com/sites/g/files/alwlxe161/files/2025-03/Syensqo-2024-Annual-Integrated-Report.pdf
- URL Wayback: https://web.archive.org/web/20261102114003id_/https://www.syensqo.com/sites/g/files/alwlxe161/files/2025-03/Syensqo-2024-Annual-Integrated-Report.pdf
- Detall: no_coincideix len_cita_norm=94 len_text_norm=1108874 score=0.733
- Cita: «The separation was effected by means of a partial demerger (“scission partielle”) of Solvay SA»

### Exemple 3

- ISIN-any: `CH0012138530` 2022 (Credit Suisse Group AG Namens-Aktien SF, FounderCEO=0)
- Camp: `registre.url_font/ceo`
- URL: https://asfromania.ro/uploads/articole/attachments/63762f72859f0600398350.pdf
- URL Wayback: https://web.archive.org/web/20260306153332id_/https://asfromania.ro/uploads/articole/attachments/63762f72859f0600398350.pdf
- Detall: no_coincideix len_cita_norm=120 len_text_norm=59309 score=0.842
- Cita: «The current composition of the Executive Board of CS* is as follows: Name Function Ulrich Körner Chief Executive Officer»

### Exemple 4

- ISIN-any: `CH0038388911` 2025 (Sulzer AG Namens-Aktien SF -,01, FounderCEO=0)
- Camp: `registre.url_font/fundador`
- URL: https://www.sulzer.com/en/about-us/our-company/history/19th-century
- URL Wayback: https://web.archive.org/web/20260521111937id_/https://www.sulzer.com/en/about-us/our-company/history/19th-century
- Detall: no_coincideix len_cita_norm=107 len_text_norm=21 score=0.062
- Cita: «and lays the foundation stone of “Sulzer Brothers Foundry, Winterthur”, known today as “the 1834 building”.»

### Exemple 5

- ISIN-any: `CH0198251305` 2024 (Coca-Cola HBC AG Nam.-Aktien SF 6,70, FounderCEO=0)
- Camp: `registre.url_font/fundador`
- URL: https://www.coca-colahellenic.com/content/dam/cch/us/documents/investors-and-financial/results-reports-and-presentations/reports/coc122_cch-iar-2017_final-web-ready-pdf_180315.pdf.downloadasset.pdf
- URL Wayback: https://web.archive.org/web/20240616000056id_/https://www.coca-colahellenic.com/content/dam/cch/us/documents/investors-and-financial/results-reports-and-presentations/reports/coc122_cch-iar-2017_final-web-ready-pdf_180315.pdf.downloadasset.pdf
- Detall: no_coincideix len_cita_norm=45 len_text_norm=748441 score=0.833
- Cita: «Zoran Bogdanovic (46) Chief Executive Officer»

### Exemple 6

- ISIN-any: `CH0210483332` 2025 (Cie Financière Richemont SA Namens-Aktien, FounderCEO=0)
- Camp: `registre.url_font/ceo`
- URL: https://www.richemont.com/media/045hlucv/richemont-fy26-annual-report-and-accounts.pdf
- URL Wayback: https://web.archive.org/web/20260622125006id_/https://www.richemont.com/media/045hlucv/richemont-fy26-annual-report-and-accounts.pdf
- Detall: no_coincideix len_cita_norm=56 len_text_norm=225586 score=0.750
- Cita: «Nicolas Bos Burkhart Grund Group Chief Executive Officer»

### Exemple 7

- ISIN-any: `CH0225173167` 2018 (Cembra Money Bank AG Namens-Aktien SF, FounderCEO=0)
- Camp: `font_classificacio_url`
- URL: https://cembra.ch/assets/cembra/investor-relation/berichte-und-praesentationen/finanzberichte/geschaeftsbericht-2013-en.pdf
- URL Wayback: https://web.archive.org/web/20260208144631id_/https://cembra.ch/assets/cembra/investor-relation/berichte-und-praesentationen/finanzberichte/geschaeftsbericht-2013-en.pdf
- Detall: no_coincideix len_cita_norm=82 len_text_norm=228038 score=0.615
- Cita: «joined the General Electric Group in 1999 […] at PSA Peugeot Citroën (1985–1999)»

### Exemple 8

- ISIN-any: `DE0005190003` 2022 (Bayerische Motoren Werke AG Stammaktien, FounderCEO=0)
- Camp: `registre.url_font/fundador`
- URL: https://www.bmwgroup.com/en/unternehmen/historie.html
- URL Wayback: https://web.archive.org/web/20240818094520id_/https://www.bmwgroup.com/en/unternehmen/historie.html
- Detall: no_coincideix len_cita_norm=83 len_text_norm=29640 score=0.562
- Cita: «the foundation of BFW on 7 March 1916 has marked the official founding date of BMW.»

### Exemple 9

- ISIN-any: `GB0009457366` 2018 (Daily Mail & General Trust PLC Reg. Shares, FounderCEO=0)
- Camp: `registre.url_font/fundador`
- URL: https://find-and-update.company-information.service.gov.uk/company/00184594/officers?page=2
- URL Wayback: https://web.archive.org/web/20210522184954id_/https://find-and-update.company-information.service.gov.uk/company/00184594/officers?page=2
- Detall: no_coincideix len_cita_norm=24 len_text_norm=4279 score=0.800
- Cita: «Date of birth March 1967»

### Exemple 10

- ISIN-any: `JE00B5TT1872` 2017 (Centamin PLC Registered Shares o.N., FounderCEO=0)
- Camp: `registre.url_font/datacio`
- URL: https://www.investegate.co.uk/announcement/rns/centamin-di---cey/annual-information-form/1994348
- URL Wayback: https://web.archive.org/web/20261121160653id_/https://www.investegate.co.uk/announcement/rns/centamin-di---cey/annual-information-form/1994348
- Detall: no_coincideix len_cita_norm=64 len_text_norm=3745 score=0.444
- Cita: «Annual Information Form Centamin Egypt Limited 14 September 2009»

## Limitacions (què no s'ha pogut verificar)

- Parells `captura_no_llegible`: 12.512 (dels quals 9.922 perquè la URL no era als resultats Wayback d'aquesta nit, i 2.590 perquè la captura no s'ha pogut llegir).
- Motius de `captura_no_llegible` (prefix de `detall`):
  - `url_absent_als_resultats_wayback_20261122`: 9.922
  - `http_404`: 1.465
  - `pdftotext_error`: 927
  - `binari_no_llegible`: 42
  - `ssl`: 39
  - `http_503`: 39
  - `http_403`: 32
  - `html_sense_text`: 13
  - `mida_excedida`: 10
  - `mida_excedida_content_length`: 8
  - `temps_max_300s`: 8
  - `pdf_escanejat_o_sense_text`: 7
- 24 files del registre no tenen `url_font` i no s'han convertit en parells.
- Les URL noves dels lots 6-8 que no eren a la llista d'aquesta nit no s'han descarregat (això queda per a una passada posterior de Wayback). No s'ha consultat cap altra còpia ni la web en viu.
- Un PDF escanejat (només imatge) queda com a `captura_no_llegible`, no com a `cita_no_trobada`.
- `cita_ok` no garanteix que la cita sigui la prova correcta per a aquella classificació; només que el text literal (ja normalitzat) apareix a la captura.
- Per a `d37_cita_contemp_url` s'ha pres `d37_data_cita` com a cita (com a `urls_main.csv`); `d37_cita_contemporania` és un flag i `d37_cita_contemp_data` pot ser una altra data.
- Les columnes `url_font` (sector, fulls STOXX) i `v75_urls_arxivades` no porten cita literal: queden `sense_cita` i no es comprova cap text.
- La coincidència parcial (≥85% de tokens) no es compta com a OK; cal revisar-la a mà.


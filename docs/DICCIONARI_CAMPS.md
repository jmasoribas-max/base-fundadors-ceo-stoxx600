# Diccionari de camps v8 r3

Data: 19/11/2026 10:14 (CET, Europe/Madrid). Fitxer de dades: `dades/base_isin_any_v8r3.csv` (i `.xlsx`), 6.012 files ISIN-any del panell, **158 columnes** (156 de la v8 r2 + 2 de robustesa de sector). [V]
Unitat: ISIN-any. Clau: `isin` + `any`. SHA de la base: `1b7df913b31300857cbc77332a9aa03626edc0013f3bbb1e8625aa456ee38d4c` [V]. SHA de la taula sectorial: `ddc3d037d796c4053700ce374148f134b09e071579875befe89e664e816899af` [V].

Les columnes heretades no canvien de significat respecte a la v8 r2, tret que a les files 2024-2025 amb `sector_estes_des_2023=1` els camps de sector aplicat (`supersector`, `taxonomia_icb`, `supersector_icb_anterior`, `supersector_icb2020`, `any_font`, `url_font`, `estat_sector`) queden omplerts amb el supersector del PDF de juny 2023. La v8 r3 no modifica FounderCEO ni els comptes principals.

## Columnes noves a la v8 r3 (robustesa de sector)

| # | Camp | Descripció |
|---|---|---|
| 157 | `sector_estes_des_2023` | `1` si la fila és un any 2024 o 2025 el sector de la qual s'ha estès des del PDF de components de juny 2023; `0` en cas contrari. Per excloure aquestes files en una robustesa: `sector_estes_des_2023!=1`. [V] |
| 158 | `supersector_fix` | Supersector fix per empresa (ISIN), copiat de la taula sectorial a totes les files de l'ISIN que hi tenen sector. Buit a les 98 files de les 72 empreses `sense_sector`. No depèn de si la fila 2024-2025 s'ha estès o no. [V] |

---

## Diccionari heretat de la v8 r2 (columnes 1-156)

# Diccionari de camps v8 r2

Data: 19/11/2026 09:48 (CET, Europe/Madrid). Fitxer de dades: `dades/base_isin_any_v8r2.csv` (i `.xlsx`), 6.012 files ISIN-any del panell, **156 columnes** (146 heretades de la v8 r1 + 10 de sector). [V]
Unitat: ISIN-any. Clau: `isin` + `any`. SHA de la base: `1eb35dd77b410eb486e5ce534c9a852357517090b9a7759d25f8de90ee31c68f` [V]. SHA de la taula sectorial: `ddc3d037d796c4053700ce374148f134b09e071579875befe89e664e816899af` [V].

Les 146 columnes heretades no canvien de significat respecte a la v8 r1 (el text de la v8 r1 es conserva més avall, com a document d'origen). La v8 r2 no modifica FounderCEO ni els comptes principals.

## Columnes noves a la v8 r2 (sector ICB per ISIN)

| # | Camp | Descripció |
|---|---|---|
| 147 | `supersector` | Supersector ICB de l'ISIN, pres del PDF públic de components de l'any de la font. Buit si `estat_sector` és `sense_sector` o si l'any és 2024-2025 i el sector no s'ha estès (pendència de Doctorat). |
| 148 | `taxonomia_icb` | `ICB_2020` o `ICB_anterior`, segons el PDF de la font. Buit en els mateixos casos que `supersector`. |
| 149 | `supersector_icb_anterior` | Supersector en taxonomia ICB anterior, quan consta a la font. Buit si no s'aplica el sector a la fila. |
| 150 | `supersector_icb2020` | Supersector en taxonomia ICB 2020, quan consta a la font. Buit si no s'aplica el sector a la fila. |
| 151 | `any_font` | Any del PDF de components d'on s'ha pres el sector (2015-2023). Es conserva com a referència també a les files 2024-2025 pendents d'extensió. |
| 152 | `url_font` | URL original del PDF de components. |
| 153 | `url_wayback_font` | Captura Wayback del PDF, si consta a la taula sectorial. |
| 154 | `metode_nom_isin` | Com s'ha casat l'ISIN amb el nom del PDF: `nom_exacte`, o `nom_stoxx_via_llista_seleccio` (via indirecta, a revisar). |
| 155 | `estat_sector` | `amb_sector`, `revisar`, `pendent_extensio_2024_2025`, `revisar_pendent_extensio_2024_2025` o `sense_sector`. |
| 156 | `motiu_sense_sector` | Motiu si el sector no s'aplica a la fila, o nota de revisió per via indirecta. Les 72 empreses sense sector conserven el motiu de la font. |

---

## Diccionari heretat de la v8 r1 (columnes 1-146)

# Diccionari de camps v8 r1

Data: 18/11/2026 20:56 (CET, Europe/Madrid). Fitxer de dades: `base_isin_any_v8.csv` (i `base_isin_any_v8.xlsx`), 6.012 files ISIN-any del panell, 140 columnes.
Unitat: ISIN-any. Clau: `isin` + `any`. Valors de FounderCEO: `1` (F), `0` (P), `no_determinat` (ND), `NA_sense_ceo` (NA).

Les columnes `sim_*` venen de la simulació r4 v2 (sufix conservat per traçabilitat). Les columnes sense prefix `sim_` que ja existien a la v75r2 es conserven, tret de `FounderCEO`, `a_mostra_principal` i les robusteses explícitament recalculades (vegeu més avall). El camp `ceos` no s'ha sobreescrit.

## Columnes noves o recalculades a la v8

| Camp | Origen | Descripció |
|---|---|---|
| `FounderCEO` | v8 / v2 | Etiqueta de la v8: `1` = F (Founder-CEO), `0` = P (Professional), `no_determinat` = ND, `NA_sense_ceo` = NA. Incorpora els 35 canvis de la v2. |
| `a_mostra_principal` | v8 / v2 | Mostra principal J14 recalculada a la v2/v8: 1 si la fila és del panell, FounderCEO és 0 o 1, i no és `dret_temporal` (D34); ND i NA queden fora (D31). Font del criteri: Jordi 15/11/2026 11:02. n=5.954, F=342. |
| `a_mostra_principal_v75r2` | v8 / v2 | Valor de `a_mostra_principal` a la v75r2, conservat per traçabilitat (n=5.928, F=337). |
| `a_mostra_nomes_certificades` | v8 / v2 | 1 si la fila és a la mostra principal i està certificada (N1, N2 o doctorat). Recalculada a la v2/v8. n=1.755, F=302. |
| `founderceo_rob_sense_decisions_doctorat` | v8 / v2 | Robustesa: FounderCEO sense aplicar les decisions de Doctorat (recalculada a la v2/v8). Orpea 2016-21 hi entra com a P per la cita de Marian. |
| `founderceo_rob_r3_president_exec_com_1` | v8 / v2 | Robustesa R3: president executiu fundador recodificat com a 1. **Heretada de la v75r2, no recalculada** després dels 35 canvis. Vegeu LIMITACIONS_v8.md. |
| `founderceo_rob_sense_fundador_transformador` | v8 / v2 | Robustesa: FounderCEO excloent els casos `fundador_transformador=1`. **Heretada de la v75r2, no recalculada.** |
| `sense_fundador_transformador` | v8 / v2 | Columna demanada per a la v8. No existia amb aquest nom. Valors copiats de `founderceo_rob_sense_fundador_transformador` (dades verificables). No és una variable independent ni un recàlcul. Vegeu LIMITACIONS_v8.md. |
| `ceos` | v8 / v2 | CEO o CEOs registrats a la v75r2. **No s'ha sobreescrit** a la v8. Pot no coincidir amb el CEO aplicat després d'un canvi (vegeu `sim_ceo_aplicat`). |
| `sim_ceo_aplicat` | v8 / v2 | CEO aplicat a la v8 (Oreja a Enagás 2016-21, Ayres a Bellway 2017; a la resta coincideix amb el criteri de la simulació, sense sobreescriure `ceos`). |
| `sim_canvi` | v8 / v2 | 1 si l'etiqueta FounderCEO canvia respecte a la v75r2 (35 files). |
| `sim_canvi_ceo` | v8 / v2 | 1 si el CEO aplicat canvia respecte a `ceos` (7 files). |
| `sim_estat_certificacio` | v8 / v2 | Estat de certificació: `certificada`, `certificada_ceo_pendent`, `no_certificada`, `fora_mostra_auditoria`. |
| `sim_nivell` | v8 / v2 | Nivell si hi ha certificació o ceo_pendent: `N1`, `N2`, `doctorat`, o buit. |
| `sim_estat_cert_rob_cas_esp` | v8 / v2 | Robustesa de certificació tractant els tancaments de ChatGPT a `cas_especific` com a indeterminats. No altera l'etiqueta ni la certificació principal. |
| `sim_nivell_rob_cas_esp` | v8 / v2 | Nivell corresponent a la robustesa anterior. |

## Totes les columnes (ordre del CSV)

| # | Camp | Descripció |
|---|---|---|
| 1 | `isin` | Identificador ISIN de l'emissor. Clau, amb `any`. |
| 2 | `any` | Any natural de la fila (panell 2016-2025). Enter com a text. |
| 3 | `nom_panell` | Nom de l'emissor al panell (heretat; pot contenir sufixos de la sèrie borsària). No s'ha netejat (vegeu typo d'Orpea 2018). |
| 4 | `pes_pct` | Pes al panell (percentatge), heretat. |
| 5 | `fora_panel` | 0 a totes les files d'aquesta base (només panell). A la v75r2, 1 identifica les files 2015, excloses de la v8. |
| 6 | `a_mostra_principal` | Mostra principal J14 recalculada a la v2/v8: 1 si la fila és del panell, FounderCEO és 0 o 1, i no és `dret_temporal` (D34); ND i NA queden fora (D31). Font del criteri: Jordi 15/11/2026 11:02. n=5.954, F=342. |
| 7 | `a_mostra_principal_v5` | Mostra principal de la v5, heretada, no recalculada. |
| 8 | `a_mostra_nomes_verificats` | Mostra restringida a files amb verificació documental, heretada. |
| 9 | `verificacio_documental` | Estat de la verificació documental heretada. |
| 10 | `no_us_article` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 11 | `FounderCEO` | Etiqueta de la v8: `1` = F (Founder-CEO), `0` = P (Professional), `no_determinat` = ND, `NA_sense_ceo` = NA. Incorpora els 35 canvis de la v2. |
| 12 | `FounderCEO_v75r2` | Etiqueta a la v75r2, conservada per traçabilitat. |
| 13 | `founderceo_rob_na_com_0` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 14 | `founderceo_rob_nd_com_0` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 15 | `founderceo_rob_na_i_nd_com_0` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 16 | `founderceo_rob_fundacio_corporativa_com_0` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 17 | `founderceo_rob_r3_president_exec_com_1` | Robustesa R3: president executiu fundador recodificat com a 1. **Heretada de la v75r2, no recalculada** després dels 35 canvis. Vegeu LIMITACIONS_v8.md. |
| 18 | `holding_pura` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 19 | `font_holding_pura` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 20 | `nomes_preferents` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 21 | `estat_nomes_preferents` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 22 | `n_ceos` | Nombre de CEOs al camp `ceos`, heretat. |
| 23 | `ceos` | CEO o CEOs registrats a la v75r2. **No s'ha sobreescrit** a la v8. Pot no coincidir amb el CEO aplicat després d'un canvi (vegeu `sim_ceo_aplicat`). |
| 24 | `via_files` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 25 | `isin_files` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 26 | `regles` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 27 | `marques` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 28 | `estat_verificacio_externa` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 29 | `id_canvi` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 30 | `origen_classificacio` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 31 | `origen_ceo` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 32 | `verificacio_externa_per` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 33 | `regla_aplicada_v3` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 34 | `via_fundador_v3` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 35 | `font_classificacio_url` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 36 | `font_classificacio_cita` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 37 | `font_classificacio_sha_extracte` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 38 | `font_classificacio_pack` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 39 | `es_fundador_pack` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 40 | `x5_es_fundador` | Camp d'una passada anterior (X5/X11), heretat. |
| 41 | `x5_regla_aplicada` | Camp d'una passada anterior (X5/X11), heretat. |
| 42 | `x5_via_fundador` | Camp d'una passada anterior (X5/X11), heretat. |
| 43 | `x5_estat_linia` | Camp d'una passada anterior (X5/X11), heretat. |
| 44 | `x5_id` | Camp d'una passada anterior (X5/X11), heretat. |
| 45 | `x5_tram` | Camp d'una passada anterior (X5/X11), heretat. |
| 46 | `x5_discrepancia` | Camp d'una passada anterior (X5/X11), heretat. |
| 47 | `x5_holding` | Camp d'una passada anterior (X5/X11), heretat. |
| 48 | `x5_relacio_mapatge` | Camp d'una passada anterior (X5/X11), heretat. |
| 49 | `x5_id_mapatge` | Camp d'una passada anterior (X5/X11), heretat. |
| 50 | `estat_verificacio` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 51 | `pendent_que` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 52 | `pack_origen` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 53 | `ids_decisio` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 54 | `ids_fonts` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 55 | `ft` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 56 | `tipus_ft` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 57 | `ft_rob_3anys` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 58 | `spinoff` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 59 | `dret_temporal` | Marca D34 (dret temporal). Si és 1, la fila no entra a la mostra J14. |
| 60 | `estat_x7` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 61 | `founderceo_rob_sense_ft` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 62 | `founderceo_rob_ft_nomes_ab` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 63 | `founderceo_rob_spinoff_com_0` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 64 | `founderceo_rob_r2b_com_na` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 65 | `founderceo_rob_pre_d37` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 66 | `founderceo_rob_sense_origen_intern` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 67 | `founderceo_rob_sense_r3` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 68 | `a_mostra_principal_v6` | Mostra principal de la v6, heretada. |
| 69 | `x11_grup` | Camp d'una passada anterior (X5/X11), heretat. |
| 70 | `id_canvi_v7` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 71 | `regla_canvi_v7` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 72 | `d37_data_cita` | Camp relatiu a la regla D37 (cita de fundador), heretat. |
| 73 | `d37_data_cita_estat` | Camp relatiu a la regla D37 (cita de fundador), heretat. |
| 74 | `d37_cita_contemporania` | Camp relatiu a la regla D37 (cita de fundador), heretat. |
| 75 | `founderceo_rob_cita_contemporania` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 76 | `fundador_transformador` | Marca 1 si la persona no era a la fundació original però l'emissor l'anomena fundador (4 files del panell: Investec/Koseff i WPP/Sorrell, 2016-2017). |
| 77 | `nota_fundador_transformador` | Nota textual de la marca anterior. |
| 78 | `founderceo_rob_sense_fundador_transformador` | Robustesa: FounderCEO excloent els casos `fundador_transformador=1`. **Heretada de la v75r2, no recalculada.** |
| 79 | `sense_fundador_transformador` | Columna demanada per a la v8. No existia amb aquest nom. Valors copiats de `founderceo_rob_sense_fundador_transformador` (dades verificables). No és una variable independent ni un recàlcul. Vegeu LIMITACIONS_v8.md. |
| 80 | `d37d_procedencia` | Camp relatiu a la regla D37 (cita de fundador), heretat. |
| 81 | `fundador_escissio` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 82 | `founderceo_rob_fundador_escissio_com_0` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 83 | `founderceo_rob_nd_com_1` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 84 | `a_mostra_principal_v7` | Mostra principal de la v7, heretada (no tocada a la v2/v8). |
| 85 | `id_canvi_v71` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 86 | `regla_canvi_v71` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 87 | `d37_cita_contemp_url` | Camp relatiu a la regla D37 (cita de fundador), heretat. |
| 88 | `d37_cita_contemp_data` | Camp relatiu a la regla D37 (cita de fundador), heretat. |
| 89 | `d37_cita_contemp_sha_extracte` | Camp relatiu a la regla D37 (cita de fundador), heretat. |
| 90 | `motiu_nd` | Motiu de les files ND. |
| 91 | `detall_motiu_nd` | Detall del motiu ND. |
| 92 | `motiu_nd_article` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 93 | `motiu_na` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 94 | `tancament_nd` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 95 | `packs_provats` | Camp heretat de la v75r2 / simulació v2. El significat no canvia a la v8. |
| 96 | `founderceo_rob_c_com_nd` | Columna de robustesa heretada de la v75r2 (no recalculada a la v8, tret que s'indiqui el contrari més amunt). |
| 97 | `v75_n_fonts` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 98 | `v75_n_fonts_durables` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 99 | `v75_n_fonts_cita_trobada` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 100 | `v75_font_durable` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 101 | `v75_cita_trobada` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 102 | `v75_urls_arxivades` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 103 | `v75_timestamps_wayback` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 104 | `v75_sha256_documents` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 105 | `v75_origen_arxiu` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 106 | `v75_ids_proposta` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 107 | `v75_estat` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 108 | `v75_pendent` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 109 | `v75_marca` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 110 | `v75_decisio_jordi` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 111 | `v75_doc_falta` | Camp de traçabilitat de la v7.5 / v75r2, heretat. |
| 112 | `sim_canvi` | 1 si l'etiqueta FounderCEO canvia respecte a la v75r2 (35 files). |
| 113 | `sim_canvi_de` | Etiqueta v75r2 (F/P/ND/NA) quan `sim_canvi=1`. |
| 114 | `sim_canvi_a` | Etiqueta v8 quan `sim_canvi=1`. |
| 115 | `sim_origen_canvi` | Origen del canvi (`decisio_doctorat` o `decisio_doctorat_r4`). |
| 116 | `sim_estat_certificacio` | Estat de certificació: `certificada`, `certificada_ceo_pendent`, `no_certificada`, `fora_mostra_auditoria`. |
| 117 | `sim_nivell` | Nivell si hi ha certificació o ceo_pendent: `N1`, `N2`, `doctorat`, o buit. |
| 118 | `sim_cert_detall` | Detall textual de la certificació. |
| 119 | `sim_web_nv` | 1 si la fila té evidència web no verificable (pendent o error) i no té cita A/B sòlida. |
| 120 | `sim_validador_error` | Marca d'error de validador, si s'escau. |
| 121 | `sim_id_fila_r4` | Identificador de fila del paquet r4, si la fila hi era. |
| 122 | `sim_founderceo_proposat_chatgpt` | Proposta d'etiqueta de ChatGPT (0/1/indeterminat/sense_ceo). |
| 123 | `sim_founderceo_proposat_claude` | Proposta bruta de Claude. |
| 124 | `sim_founderceo_claude_efectiu` | Proposta efectiva de Claude (errors anulats). |
| 125 | `sim_ceo_chatgpt` | CEO proposat per ChatGPT a r4, si n'hi ha. |
| 126 | `sim_ceo_claude` | CEO proposat per Claude a r4, si n'hi ha. |
| 127 | `sim_ceo_aplicat` | CEO aplicat a la v8 (Oreja a Enagás 2016-21, Ayres a Bellway 2017; a la resta coincideix amb el criteri de la simulació, sense sobreescriure `ceos`). |
| 128 | `sim_canvi_ceo` | 1 si el CEO aplicat canvia respecte a `ceos` (7 files). |
| 129 | `sim_canvi_ceo_de` | Valor de `ceos` (v75r2) quan hi ha canvi de CEO. |
| 130 | `sim_canvi_ceo_a` | CEO aplicat quan hi ha canvi. |
| 131 | `sim_decisio_doctorat` | Identificador de la decisió de Doctorat aplicada a la fila. |
| 132 | `sim_nota` | Nota de la simulació. |
| 133 | `founderceo_rob_sense_decisions_doctorat` | Robustesa: FounderCEO sense aplicar les decisions de Doctorat (recalculada a la v2/v8). Orpea 2016-21 hi entra com a P per la cita de Marian. |
| 134 | `a_mostra_nomes_certificades` | 1 si la fila és a la mostra principal i està certificada (N1, N2 o doctorat). Recalculada a la v2/v8. n=1.755, F=302. |
| 135 | `sim_cas_clau` | Marca dels casos clau no certificats (LVMH, BE Semiconductor, Aberdeen 2016, etc.). |
| 136 | `a_mostra_principal_v75r2` | Valor de `a_mostra_principal` a la v75r2, conservat per traçabilitat (n=5.928, F=337). |
| 137 | `sim_canvi_ceo_pendent` | 1 si el canvi de CEO no s'ha pogut aplicar per falta de cita literal. A la v8 és 0 a totes les files (els 7 canvis s'apliquen). |
| 138 | `sim_canvi_ceo_cita_estat` | Estat de la cita que justifica el canvi de CEO. |
| 139 | `sim_estat_cert_rob_cas_esp` | Robustesa de certificació tractant els tancaments de ChatGPT a `cas_especific` com a indeterminats. No altera l'etiqueta ni la certificació principal. |
| 140 | `sim_nivell_rob_cas_esp` | Nivell corresponent a la robustesa anterior. |

## Valors permesos (camps clau)

- `FounderCEO`, `FounderCEO_v75r2`, `sense_fundador_transformador`, `founderceo_rob_*` (excepte flags 0/1 específics): `0`, `1`, `no_determinat`, `NA_sense_ceo`.
- Flags 0/1: `fora_panel`, `a_mostra_principal`, `a_mostra_nomes_certificades`, `fundador_transformador`, `dret_temporal`, `sim_canvi`, `sim_canvi_ceo`, `sim_canvi_ceo_pendent`.
- `sim_estat_certificacio`: `certificada`, `certificada_ceo_pendent`, `no_certificada`, `fora_mostra_auditoria`.
- `sim_nivell`: buit, `N1`, `N2`, `doctorat`.

## Cotes de les ND (estadística, no són un camp)

No hi ha una columna de cotes. Les cotes es publiquen a `STATS_v8.json` i a la QA: 14 ND al panell; totes a 0 → F 343; totes a 1 → F 357.


## Addenda v8 r1 (19/11/2026 09:31 (CET, Europe/Madrid))

A la v8, `founderceo_rob_r3_president_exec_com_1`, `founderceo_rob_sense_fundador_transformador` i `sense_fundador_transformador` eren herència de la v75r2 (no recalculades). A la r1 s'han recalculat amb les fórmules verificades (vegeu REGISTRE_CANVIS_v8r1.md §4). `founderceo_rob_sense_decisions_doctorat` ja era correcta i es torna a calcular amb la mateixa regla (0 files canviades).

Columnes de traça noves (no substitueixen les oficials):

- `founderceo_rob_sense_decisions_doctorat_v8`, `founderceo_rob_sense_fundador_transformador_v8`, `sense_fundador_transformador_v8`, `founderceo_rob_r3_president_exec_com_1_v8`: valor que tenia la v8.
- `rob_recalcul_v8r1_nota`, `rob_recalcul_v8r1_nv`: nota / marca [NV] del recàlcul. `rob_recalcul_v8r1_nv` és buit a totes les 6.012 files (cap [NV]).

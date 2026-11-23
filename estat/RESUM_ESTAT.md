# Estat de la base per fila

Fitxer generat per `estat/estat_files.py`. No l'editis a mà. Definicions a [`estat/README.md`](README.md).

Entrades llegides:

- `dades/base_isin_any_v8r3.csv` SHA-256 `3d08bb99ede12676f0857bae6d83ba82c29a5dd8975e9a2897edf364688e35b8`
- `docs/REGISTRE_CANVIS.csv` SHA-256 `e31bdddf1dd659754bdcb4a697e0efd402be0e93dbd68a711e5688e4f6ce3c44` (11.656 entrades)
- `PENDENTS.md` SHA-256 `fe0153f26421c0a88b1a0d1596759c826605f99a08a0dce8a12ddc6eb0d06075`
- `estat/dubtes_tancats.csv` SHA-256 `e008e8b1910c0c23c7b80bed48436cc77c9464c86ea5a6c39ea941f81a4c67f1`

## Resum per etiqueta

| Etiqueta | Files | C1 CEO | C2 fundador | C1 i C2 | C4 coherent i sense dubtes | C3 arxiu | **Acabades** |
|---|---:|---:|---:|---:|---:|---:|---:|
| F (`1`) | 349 | 105 (30,1 %) | 292 (83,7 %) | 99 (28,4 %) | 212 (60,7 %) | 0 (0,0 %) | **0 (0,0 %)** |
| P (`0`) | 5.631 | 4.081 (72,5 %) | 4.490 (79,7 %) | 4.035 (71,7 %) | 5.468 (97,1 %) | 278 (4,9 %) | **278 (4,9 %)** |
| NA | 31 | 27 (87,1 %) | 27 (87,1 %) | 27 (87,1 %) | 24 (77,4 %) | 0 (0,0 %) | **0 (0,0 %)** |
| ND | 1 | 1 (100,0 %) | 1 (100,0 %) | 1 (100,0 %) | 0 (0,0 %) | 1 (100,0 %) | **0 (0,0 %)** |
| **Total** | 6.012 | 4.214 (70,1 %) | 4.810 (80,0 %) | 4.162 (69,2 %) | 5.704 (94,9 %) | 279 (4,6 %) | **278 (4,6 %)** |

## Embut

| Pas | Files |
|---|---:|
| Panell | 6.012 |
| Amb evidència de CEO i de fundador (C1 i C2) | 4.162 (69,2 %) |
| … i coherents, sense dubtes oberts (C4) | 4.048 (67,3 %) |
| … i arxivades a Wayback amb la cita verificada (C3): **acabades** | 278 (4,6 %) |

## Què falta, per condició

Una fila pot tenir més d'una mancança.

| Mancança | F | P | NA | ND | Total |
|---|---:|---:|---:|---:|---:|
| `falta_ceo` | 244 | 1.550 | 4 | 0 | 1.798 |
| `falta_fundador` | 57 | 1.141 | 4 | 0 | 1.202 |
| `incoherent` | 7 | 44 | 0 | 0 | 51 |
| `dubte_obert` | 137 | 119 | 7 | 1 | 264 |
| `falta_arxiu` | 349 | 5.353 | 31 | 0 | 5.733 |

## Detall de C1 (CEO) i C2 (fundador)

| Valor de `c1_ceo` | Files |
|---|---:|
| `ok` | 4.187 |
| `falta` | 1.704 |
| `cita_sense_nom` | 85 |
| `rsc_documentat` | 27 |
| `co_ceo_parcial` | 5 |
| `falta_rsc` | 4 |

| Valor de `c2_fundador` | Files |
|---|---:|
| `ok_registre` | 4.348 |
| `falta` | 1.198 |
| `ok_columna_antiga` | 434 |
| `rsc_documentat` | 27 |
| `falta_rsc` | 4 |
| `cerca_documentada` | 1 |

| Valor de `c3_arxiu` | Files |
|---|---:|
| `falta_ceo+fundador` | 3.638 |
| `sense_evidencia` | 1.850 |
| `ok` | 279 |
| `falta_ceo` | 172 |
| `falta_fundador` | 72 |
| `falta_fundador_columna_antiga` | 1 |

## Segons l'estat de certificació antic (`sim_estat_certificacio`)

| Estat antic | Files | C1 i C2 | Acabades |
|---|---:|---:|---:|
| `certificada` | 1.773 | 66 (3,7 %) | 0 (0,0 %) |
| `certificada_ceo_pendent` | 108 | 108 (100,0 %) | 0 (0,0 %) |
| `no_certificada` | 241 | 235 (97,5 %) | 1 (0,4 %) |
| `fora_mostra_auditoria` | 3.890 | 3.753 (96,5 %) | 277 (7,1 %) |

## Per empresa (ISIN)

| | Totes les files amb C1 i C2 | Totes les files acabades | Total |
|---|---:|---:|---:|
| Empreses amb almenys un any F | 16 | 0 | 88 |
| Totes les empreses | 676 | 32 | 1.040 |

## Incoherències del CSV (51 files)

| ISIN | Any | FounderCEO | `ceos` | `regles` | Problema |
|---|---|---|---|---|---|
| `BE0974293251` | 2021 | 0 | Michel Doukeris | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `BE0974293251` | 2022 | 0 | Michel Doukeris | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `BE0974293251` | 2023 | 0 | Michel Doukeris | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `BE0974293251` | 2024 | 0 | Michel Doukeris | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `BE0974293251` | 2025 | 0 | Michel Doukeris | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `DE000A3H3LL2` | 2022 | 0 | Vivek Badrinath | `cap` | P_sense_prova_de_no |
| `DE000KBX1006` | 2019 | 0 | Ralph Heuwing|Peter Laier|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DE000KBX1006` | 2020 | 0 | Peter Laier|Frank Markus Weber|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DK0060252690` | 2018 | 0 | Jeremy Schwartz|Anders Boyer | `R-SC;R2b` | P_sense_prova_de_no |
| `ES0105066007` | 2016 | 1 | Tobías Martínez Gimeno | `b` | F_sense_regla_de_si |
| `ES0105066007` | 2017 | 1 | Tobías Martínez Gimeno | `b` | F_sense_regla_de_si |
| `ES0105066007` | 2018 | 1 | Tobías Martínez Gimeno | `b` | F_sense_regla_de_si |
| `ES0105066007` | 2019 | 1 | Tobías Martínez Gimeno | `b` | F_sense_regla_de_si |
| `ES0105066007` | 2020 | 1 | Tobías Martínez Gimeno | `b` | F_sense_regla_de_si |
| `ES0105066007` | 2021 | 1 | Tobías Martínez Gimeno | `b` | F_sense_regla_de_si |
| `ES0105066007` | 2022 | 1 | Tobías Martínez Gimeno | `b` | F_sense_regla_de_si |
| `ES0130960018` | 2016 | 0 | Antonio Llardén Carratalá | `e` | ceos_diferent_de_sim_ceo_aplicat |
| `ES0130960018` | 2017 | 0 | Antonio Llardén Carratalá | `e` | ceos_diferent_de_sim_ceo_aplicat |
| `ES0130960018` | 2018 | 0 | Antonio Llardén Carratalá | `e` | ceos_diferent_de_sim_ceo_aplicat |
| `ES0130960018` | 2019 | 0 | Antonio Llardén Carratalá | `e` | ceos_diferent_de_sim_ceo_aplicat |
| `ES0130960018` | 2020 | 0 | Antonio Llardén Carratalá | `e` | ceos_diferent_de_sim_ceo_aplicat |
| `ES0130960018` | 2021 | 0 | Antonio Llardén Carratalá | `e` | ceos_diferent_de_sim_ceo_aplicat |
| `ES0180907000` | 2025 | 0 | Isidro Rubiales Gil | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `FI0009005961` | 2020 | 0 | Annica Bresky | `cap` | P_sense_prova_de_no |
| `FI0009005961` | 2021 | 0 | Annica Bresky | `cap` | P_sense_prova_de_no |
| `FI0009005961` | 2022 | 0 | Annica Bresky | `cap` | P_sense_prova_de_no |
| `FI4000552526` | 2025 | 0 | Petri Niemisvirta | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `FR0000184798` | 2016 | 0 | Yves Le Masne | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `FR0000184798` | 2017 | 0 | Yves Le Masne | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `FR0000184798` | 2018 | 0 | Yves Le Masne | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `FR0000184798` | 2019 | 0 | Yves Le Masne | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `FR0000184798` | 2020 | 0 | Yves Le Masne | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `FR0000184798` | 2021 | 0 | Yves Le Masne | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `FR0011594233` | 2016 | 0 | Michel Combes | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `GB0000904986` | 2017 | 0 | John Watson | `b` | ceos_diferent_de_sim_ceo_aplicat |
| `GB0009633180` | 2018 | 0 | Ian Page | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `GB0009633180` | 2019 | 0 | Ian Page | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `GB0009633180` | 2020 | 0 | Ian Page | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `GB0009633180` | 2021 | 0 | Ian Page | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `GB0009633180` | 2022 | 0 | Ian Page | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `GB0009633180` | 2023 | 0 | Ian Page | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `GB00B8HX8Z88` | 2016 | 0 | Danie Meintjes | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `GB00B8HX8Z88` | 2017 | 0 | Danie Meintjes | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `GB00BMBVGQ36` | 2022 | 0 | Linda Z. Cook | `cita_fundador` | P_sense_prova_de_no;P_amb_regla_de_si |
| `GB00BMBVGQ36` | 2023 | 0 | Linda Z. Cook | `cita_fundador` | P_sense_prova_de_no;P_amb_regla_de_si |
| `NL0011375019` | 2016 | 0 | Markus Jooste | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `NL0011375019` | 2017 | 0 | Markus Jooste | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `PLOPTTC00011` | 2023 | 0 | Adam Kiciński | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `SE0000242455` | 2016 | 0 | Birgitte Bonnesen | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `SE0000242455` | 2017 | 0 | Birgitte Bonnesen | `cap` | P_sense_prova_de_no;motiu_nd_residual |
| `SE0000242455` | 2018 | 0 | Birgitte Bonnesen | `cap` | P_sense_prova_de_no;motiu_nd_residual |

## Avisos (no bloquegen)

- `carrec_no_detectat_a_la_cita`: 185 files

# Estat de la base per fila

Fitxer generat per `estat/estat_files.py`. No l'editis a mà. Definicions a [`estat/README.md`](README.md).

Entrades llegides:

- `dades/base_isin_any_v8r3.csv` SHA-256 `f64dd4120acf17d2eff4f7d0f581e910ef8ac09f6f3ca7dadb2e7b0e3a36d6e8`
- `docs/REGISTRE_CANVIS.csv` SHA-256 `e2d4c13ed43739eb27789862d84c9344e3913418621d9f6803a90e1fc5c7f15f` (19.172 entrades)
- `PENDENTS.md` SHA-256 `923f2d5261bb7eb1e63464a375488a6bed135b23921c1175594acfe6bc0cd684`
- `estat/dubtes_tancats.csv` SHA-256 `93457f684d3ec3e9e3ae61b137102e3ddb699916ab11b01b31400430582675a3`

## Resum per etiqueta

| Etiqueta | Files | C1 CEO | C2 fundador | C1 i C2 | C4 coherent i sense dubtes | C3 arxiu | **Acabades** |
|---|---:|---:|---:|---:|---:|---:|---:|
| F (`1`) | 352 | 352 (100,0 %) | 344 (97,7 %) | 344 (97,7 %) | 287 (81,5 %) | 27 (7,7 %) | **22 (6,2 %)** |
| P (`0`) | 5.621 | 5.603 (99,7 %) | 5.573 (99,1 %) | 5.557 (98,9 %) | 5.549 (98,7 %) | 187 (3,3 %) | **187 (3,3 %)** |
| NA | 31 | 30 (96,8 %) | 30 (96,8 %) | 30 (96,8 %) | 24 (77,4 %) | 16 (51,6 %) | **13 (41,9 %)** |
| ND | 8 | 8 (100,0 %) | 8 (100,0 %) | 8 (100,0 %) | 0 (0,0 %) | 0 (0,0 %) | **0 (0,0 %)** |
| **Total** | 6.012 | 5.993 (99,7 %) | 5.955 (99,1 %) | 5.939 (98,8 %) | 5.860 (97,5 %) | 230 (3,8 %) | **222 (3,7 %)** |

## Embut

| Pas | Files |
|---|---:|
| Panell | 6.012 |
| Amb evidència de CEO i de fundador (C1 i C2) | 5.939 (98,8 %) |
| … i coherents, sense dubtes oberts (C4) | 5.809 (96,6 %) |
| … i arxivades a Wayback amb la cita verificada (C3): **acabades** | 222 (3,7 %) |

## Què falta, per condició

Una fila pot tenir més d'una mancança.

| Mancança | F | P | NA | ND | Total |
|---|---:|---:|---:|---:|---:|
| `falta_ceo` | 0 | 18 | 1 | 0 | 19 |
| `falta_fundador` | 8 | 48 | 1 | 0 | 57 |
| `incoherent` | 0 | 2 | 0 | 0 | 2 |
| `dubte_obert` | 65 | 70 | 7 | 8 | 150 |
| `falta_arxiu` | 325 | 5.434 | 15 | 8 | 5.782 |

## Detall de C1 (CEO) i C2 (fundador)

| Valor de `c1_ceo` | Files |
|---|---:|
| `ok` | 5.963 |
| `rsc_documentat` | 30 |
| `falta` | 9 |
| `co_ceo_parcial` | 9 |
| `falta_rsc` | 1 |

| Valor de `c2_fundador` | Files |
|---|---:|
| `ok_prova_b` | 2.060 |
| `ok_prova_a` | 1.925 |
| `ok_prova_d` | 783 |
| `ok_prova_e` | 653 |
| `ok_registre` | 280 |
| `ok_prova_c` | 120 |
| `ok_columna_antiga` | 64 |
| `prova_incompleta` | 48 |
| `rsc_documentat` | 30 |
| `ok_prova_b|b` | 24 |
| `cerca_documentada` | 8 |
| `falta` | 8 |
| `ok_prova_d|d` | 5 |
| `ok_prova_b|b|b|d|b` | 2 |
| `falta_rsc` | 1 |
| `ok_prova_d|b` | 1 |

### C2 de les files P: prova de no fundador completa per parts

Decisió de Jordi del 24/11/2026 (opció b): un 0 només compta com a documentat si la prova té totes les parts, cadascuna amb la seva cita A/B. Parts: a llista de fundadors; e origen estatal o corporatiu; c any de fundació 64 anys o més abans; b any de fundació i naixement del CEO; d any de fundació i ocupador anterior del CEO.

| | Files P |
|---|---:|
| Amb alguna cita de fundador (criteri anterior al 24/11) | 5.560 (98,9 %) |
| Amb una prova completa per parts (criteri vigent) | 5.573 (99,1 %) |
| … prova a (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 1.925 |
| … prova e (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 653 |
| … prova b (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 2.087 |
| … prova d (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 791 |
| … prova c (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 120 |
| Cita que diu que el CEO és fundador (contradicció, a revisar) | 0 |
| Amb alguna part però sense cap prova completa | 48 |
| Sense cap part documentada | 0 |

| Valor de `c3_arxiu` | Files |
|---|---:|
| `falta_ceo+fundador` | 4.972 |
| `falta_fundador` | 498 |
| `falta_ceo` | 238 |
| `ok` | 230 |
| `sense_evidencia` | 73 |
| `falta_fundador_columna_antiga` | 1 |

## Segons l'estat de certificació antic (`sim_estat_certificacio`)

| Estat antic | Files | C1 i C2 | Acabades |
|---|---:|---:|---:|
| `certificada` | 1.773 | 1.745 (98,4 %) | 3 (0,2 %) |
| `certificada_ceo_pendent` | 108 | 108 (100,0 %) | 7 (6,5 %) |
| `no_certificada` | 241 | 241 (100,0 %) | 135 (56,0 %) |
| `fora_mostra_auditoria` | 3.890 | 3.845 (98,8 %) | 77 (2,0 %) |

## Per empresa (ISIN)

| | Totes les files amb C1 i C2 | Totes les files acabades | Total |
|---|---:|---:|---:|
| Empreses amb almenys un any F | 87 | 4 | 90 |
| Totes les empreses | 1.014 | 30 | 1.040 |

## Incoherències del CSV (2 files)

| ISIN | Any | FounderCEO | `ceos` | `regles` | Problema |
|---|---|---|---|---|---|
| `DE000KBX1006` | 2019 | 0 | Ralph Heuwing|Peter Laier|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DE000KBX1006` | 2020 | 0 | Peter Laier|Frank Markus Weber|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |

## Avisos (no bloquegen)

- `carrec_no_detectat_a_la_cita`: 125 files
- `prova_C2_diferent_de_regles`: 3250 files

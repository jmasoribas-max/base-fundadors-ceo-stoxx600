# Estat de la base per fila

Fitxer generat per `estat/estat_files.py`. No l'editis a mà. Definicions a [`estat/README.md`](README.md).

Entrades llegides:

- `dades/base_isin_any_v8r3.csv` SHA-256 `0b969dec106a31be4dbd4a55789aac38042e3f03c4d3690c48dab7c0ee1370d8`
- `docs/REGISTRE_CANVIS.csv` SHA-256 `88f5de7aac6bd703165e612d3b47d75ef1eaeaceb50d2a8f3d904d6f8f42e575` (19.653 entrades)
- `PENDENTS.md` SHA-256 `923f2d5261bb7eb1e63464a375488a6bed135b23921c1175594acfe6bc0cd684`
- `estat/dubtes_tancats.csv` SHA-256 `36daa60fefec9ffddefe88bd2932522a154d1a7019a9da3e916a1cb8beda2667`

## Resum per etiqueta

| Etiqueta | Files | C1 CEO | C2 fundador | C1 i C2 | C4 coherent i sense dubtes | C3 arxiu | **Acabades** |
|---|---:|---:|---:|---:|---:|---:|---:|
| F (`1`) | 351 | 351 (100,0 %) | 349 (99,4 %) | 349 (99,4 %) | 344 (98,0 %) | 31 (8,8 %) | **31 (8,8 %)** |
| P (`0`) | 5.621 | 5.604 (99,7 %) | 5.586 (99,4 %) | 5.571 (99,1 %) | 5.619 (100,0 %) | 627 (11,2 %) | **625 (11,1 %)** |
| NA | 32 | 31 (96,9 %) | 31 (96,9 %) | 31 (96,9 %) | 29 (90,6 %) | 16 (50,0 %) | **16 (50,0 %)** |
| ND | 8 | 8 (100,0 %) | 8 (100,0 %) | 8 (100,0 %) | 8 (100,0 %) | 0 (0,0 %) | **0 (0,0 %)** |
| **Total** | 6.012 | 5.994 (99,7 %) | 5.974 (99,4 %) | 5.959 (99,1 %) | 6.000 (99,8 %) | 674 (11,2 %) | **672 (11,2 %)** |

## Embut

| Pas | Files |
|---|---:|
| Panell | 6.012 |
| Amb evidència de CEO i de fundador (C1 i C2) | 5.959 (99,1 %) |
| … i coherents, sense dubtes oberts (C4) | 5.947 (98,9 %) |
| … i arxivades a Wayback amb la cita verificada (C3): **acabades** | 672 (11,2 %) |

## Què falta, per condició

Una fila pot tenir més d'una mancança.

| Mancança | F | P | NA | ND | Total |
|---|---:|---:|---:|---:|---:|
| `falta_ceo` | 0 | 17 | 1 | 0 | 18 |
| `falta_fundador` | 2 | 35 | 1 | 0 | 38 |
| `incoherent` | 0 | 2 | 0 | 0 | 2 |
| `dubte_obert` | 7 | 0 | 3 | 0 | 10 |
| `falta_arxiu` | 320 | 4.994 | 16 | 8 | 5.338 |

## Detall de C1 (CEO) i C2 (fundador)

| Valor de `c1_ceo` | Files |
|---|---:|
| `ok` | 5.963 |
| `rsc_documentat` | 31 |
| `co_ceo_parcial` | 9 |
| `falta` | 8 |
| `falta_rsc` | 1 |

| Valor de `c2_fundador` | Files |
|---|---:|
| `ok_prova_b` | 2.090 |
| `ok_prova_a` | 1.899 |
| `ok_prova_d` | 790 |
| `ok_prova_e` | 653 |
| `ok_registre` | 339 |
| `ok_prova_c` | 120 |
| `prova_incompleta` | 35 |
| `rsc_documentat` | 31 |
| `ok_prova_b|b` | 24 |
| `ok_columna_antiga` | 10 |
| `cerca_documentada` | 8 |
| `ok_prova_d|d` | 6 |
| `falta` | 2 |
| `ok_prova_b|b|b|d|b` | 2 |
| `falta_rsc` | 1 |
| `ok_prova_d|b` | 1 |
| `ok_prova_b|d` | 1 |

### C2 de les files P: prova de no fundador completa per parts

Decisió de Jordi del 24/11/2026 (opció b): un 0 només compta com a documentat si la prova té totes les parts, cadascuna amb la seva cita A/B. Parts: a llista de fundadors; e origen estatal o corporatiu; c any de fundació 64 anys o més abans; b any de fundació i naixement del CEO; d any de fundació i ocupador anterior del CEO.

| | Files P |
|---|---:|
| Amb alguna cita de fundador (criteri anterior al 24/11) | 5.560 (98,9 %) |
| Amb una prova completa per parts (criteri vigent) | 5.586 (99,4 %) |
| … prova a (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 1.899 |
| … prova e (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 653 |
| … prova b (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 2.118 |
| … prova d (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 800 |
| … prova c (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 120 |
| Cita que diu que el CEO és fundador (contradicció, a revisar) | 0 |
| Amb alguna part però sense cap prova completa | 35 |
| Sense cap part documentada | 0 |

| Valor de `c3_arxiu` | Files |
|---|---:|
| `falta_ceo+fundador` | 4.460 |
| `ok` | 674 |
| `falta_fundador` | 564 |
| `falta_ceo` | 260 |
| `sense_evidencia` | 53 |
| `falta_fundador_columna_antiga` | 1 |

## Segons l'estat de certificació antic (`sim_estat_certificacio`)

| Estat antic | Files | C1 i C2 | Acabades |
|---|---:|---:|---:|
| `certificada` | 1.773 | 1.757 (99,1 %) | 3 (0,2 %) |
| `certificada_ceo_pendent` | 108 | 108 (100,0 %) | 18 (16,7 %) |
| `no_certificada` | 241 | 241 (100,0 %) | 192 (79,7 %) |
| `fora_mostra_auditoria` | 3.890 | 3.853 (99,0 %) | 459 (11,8 %) |

## Per empresa (ISIN)

| | Totes les files amb C1 i C2 | Totes les files acabades | Total |
|---|---:|---:|---:|
| Empreses amb almenys un any F | 88 | 5 | 89 |
| Totes les empreses | 1.019 | 80 | 1.040 |

## Incoherències del CSV (2 files)

| ISIN | Any | FounderCEO | `ceos` | `regles` | Problema |
|---|---|---|---|---|---|
| `DE000KBX1006` | 2019 | 0 | Ralph Heuwing|Peter Laier|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DE000KBX1006` | 2020 | 0 | Peter Laier|Frank Markus Weber|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |

## Avisos (no bloquegen)

- `carrec_no_detectat_a_la_cita`: 121 files
- `prova_C2_diferent_de_regles`: 3225 files

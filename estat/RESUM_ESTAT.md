# Estat de la base per fila

Fitxer generat per `estat/estat_files.py`. No l'editis a mà. Definicions a [`estat/README.md`](README.md).

Entrades llegides:

- `dades/base_isin_any_v8r3.csv` SHA-256 `4fdb26df2e687351c8ed1f75654a8848d32b9db92f6eae1937a6c6f2b588bbc5`
- `docs/REGISTRE_CANVIS.csv` SHA-256 `636d15993261e6eab5591ab2cc7af69a1490d84f01aedf11bede21b59c3c92c7` (19.475 entrades)
- `PENDENTS.md` SHA-256 `923f2d5261bb7eb1e63464a375488a6bed135b23921c1175594acfe6bc0cd684`
- `estat/dubtes_tancats.csv` SHA-256 `93af8c0a8e9b8131c959c5de7de99e74284e1fd5e2352c7aa3507a674c07dbff`

## Resum per etiqueta

| Etiqueta | Files | C1 CEO | C2 fundador | C1 i C2 | C4 coherent i sense dubtes | C3 arxiu | **Acabades** |
|---|---:|---:|---:|---:|---:|---:|---:|
| F (`1`) | 352 | 352 (100,0 %) | 350 (99,4 %) | 350 (99,4 %) | 338 (96,0 %) | 31 (8,8 %) | **31 (8,8 %)** |
| P (`0`) | 5.621 | 5.603 (99,7 %) | 5.586 (99,4 %) | 5.570 (99,1 %) | 5.591 (99,5 %) | 240 (4,3 %) | **240 (4,3 %)** |
| NA | 31 | 30 (96,8 %) | 30 (96,8 %) | 30 (96,8 %) | 29 (93,5 %) | 16 (51,6 %) | **16 (51,6 %)** |
| ND | 8 | 8 (100,0 %) | 8 (100,0 %) | 8 (100,0 %) | 8 (100,0 %) | 0 (0,0 %) | **0 (0,0 %)** |
| **Total** | 6.012 | 5.993 (99,7 %) | 5.974 (99,4 %) | 5.958 (99,1 %) | 5.966 (99,2 %) | 287 (4,8 %) | **287 (4,8 %)** |

## Embut

| Pas | Files |
|---|---:|
| Panell | 6.012 |
| Amb evidència de CEO i de fundador (C1 i C2) | 5.958 (99,1 %) |
| … i coherents, sense dubtes oberts (C4) | 5.919 (98,5 %) |
| … i arxivades a Wayback amb la cita verificada (C3): **acabades** | 287 (4,8 %) |

## Què falta, per condició

Una fila pot tenir més d'una mancança.

| Mancança | F | P | NA | ND | Total |
|---|---:|---:|---:|---:|---:|
| `falta_ceo` | 0 | 18 | 1 | 0 | 19 |
| `falta_fundador` | 2 | 35 | 1 | 0 | 38 |
| `incoherent` | 0 | 2 | 0 | 0 | 2 |
| `dubte_obert` | 14 | 28 | 2 | 0 | 44 |
| `falta_arxiu` | 321 | 5.381 | 15 | 8 | 5.725 |

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
| `ok_prova_b` | 2.068 |
| `ok_prova_a` | 1.919 |
| `ok_prova_d` | 785 |
| `ok_prova_e` | 657 |
| `ok_registre` | 340 |
| `ok_prova_c` | 125 |
| `prova_incompleta` | 35 |
| `rsc_documentat` | 30 |
| `ok_prova_b|b` | 24 |
| `ok_columna_antiga` | 10 |
| `cerca_documentada` | 8 |
| `ok_prova_d|d` | 5 |
| `falta` | 2 |
| `ok_prova_b|b|b|d|b` | 2 |
| `falta_rsc` | 1 |
| `ok_prova_d|b` | 1 |

### C2 de les files P: prova de no fundador completa per parts

Decisió de Jordi del 24/11/2026 (opció b): un 0 només compta com a documentat si la prova té totes les parts, cadascuna amb la seva cita A/B. Parts: a llista de fundadors; e origen estatal o corporatiu; c any de fundació 64 anys o més abans; b any de fundació i naixement del CEO; d any de fundació i ocupador anterior del CEO.

| | Files P |
|---|---:|
| Amb alguna cita de fundador (criteri anterior al 24/11) | 5.560 (98,9 %) |
| Amb una prova completa per parts (criteri vigent) | 5.586 (99,4 %) |
| … prova a (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 1.919 |
| … prova e (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 657 |
| … prova b (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 2.095 |
| … prova d (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 793 |
| … prova c (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 125 |
| Cita que diu que el CEO és fundador (contradicció, a revisar) | 0 |
| Amb alguna part però sense cap prova completa | 35 |
| Sense cap part documentada | 0 |

| Valor de `c3_arxiu` | Files |
|---|---:|
| `falta_ceo+fundador` | 4.926 |
| `falta_fundador` | 512 |
| `ok` | 287 |
| `falta_ceo` | 232 |
| `sense_evidencia` | 54 |
| `falta_fundador_columna_antiga` | 1 |

## Segons l'estat de certificació antic (`sim_estat_certificacio`)

| Estat antic | Files | C1 i C2 | Acabades |
|---|---:|---:|---:|
| `certificada` | 1.773 | 1.757 (99,1 %) | 3 (0,2 %) |
| `certificada_ceo_pendent` | 108 | 108 (100,0 %) | 18 (16,7 %) |
| `no_certificada` | 241 | 241 (100,0 %) | 173 (71,8 %) |
| `fora_mostra_auditoria` | 3.890 | 3.852 (99,0 %) | 93 (2,4 %) |

## Per empresa (ISIN)

| | Totes les files amb C1 i C2 | Totes les files acabades | Total |
|---|---:|---:|---:|
| Empreses amb almenys un any F | 89 | 5 | 90 |
| Totes les empreses | 1.019 | 38 | 1.040 |

## Incoherències del CSV (2 files)

| ISIN | Any | FounderCEO | `ceos` | `regles` | Problema |
|---|---|---|---|---|---|
| `DE000KBX1006` | 2019 | 0 | Ralph Heuwing|Peter Laier|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DE000KBX1006` | 2020 | 0 | Peter Laier|Frank Markus Weber|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |

## Avisos (no bloquegen)

- `carrec_no_detectat_a_la_cita`: 121 files
- `prova_C2_diferent_de_regles`: 3250 files

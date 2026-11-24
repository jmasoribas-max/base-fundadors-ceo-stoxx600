# Estat de la base per fila

Fitxer generat per `estat/estat_files.py`. No l'editis a mà. Definicions a [`estat/README.md`](README.md).

Entrades llegides:

- `dades/base_isin_any_v8r3.csv` SHA-256 `7548d6267aa81145acbcc2bff92fdb70a8aee59020109ea754b874107db765f6`
- `docs/REGISTRE_CANVIS.csv` SHA-256 `929ac654aa49bfd7359779fb2e87223b7954c99067097afc8cff0a989d465248` (15.602 entrades)
- `PENDENTS.md` SHA-256 `923f2d5261bb7eb1e63464a375488a6bed135b23921c1175594acfe6bc0cd684`
- `estat/dubtes_tancats.csv` SHA-256 `1fb00b7ba002b05d3d0a6ad3dcf8f18a86a051054f99acc4f05d91318ae22c3a`

## Resum per etiqueta

| Etiqueta | Files | C1 CEO | C2 fundador | C1 i C2 | C4 coherent i sense dubtes | C3 arxiu | **Acabades** |
|---|---:|---:|---:|---:|---:|---:|---:|
| F (`1`) | 344 | 344 (100,0 %) | 336 (97,7 %) | 336 (97,7 %) | 279 (81,1 %) | 5 (1,5 %) | **3 (0,9 %)** |
| P (`0`) | 5.629 | 5.611 (99,7 %) | 2.339 (41,6 %) | 2.339 (41,6 %) | 5.552 (98,6 %) | 51 (0,9 %) | **51 (0,9 %)** |
| NA | 31 | 30 (96,8 %) | 30 (96,8 %) | 30 (96,8 %) | 24 (77,4 %) | 1 (3,2 %) | **1 (3,2 %)** |
| ND | 8 | 8 (100,0 %) | 8 (100,0 %) | 8 (100,0 %) | 0 (0,0 %) | 0 (0,0 %) | **0 (0,0 %)** |
| **Total** | 6.012 | 5.993 (99,7 %) | 2.713 (45,1 %) | 2.713 (45,1 %) | 5.855 (97,4 %) | 57 (0,9 %) | **55 (0,9 %)** |

## Embut

| Pas | Files |
|---|---:|
| Panell | 6.012 |
| Amb evidència de CEO i de fundador (C1 i C2) | 2.713 (45,1 %) |
| … i coherents, sense dubtes oberts (C4) | 2.627 (43,7 %) |
| … i arxivades a Wayback amb la cita verificada (C3): **acabades** | 55 (0,9 %) |

## Què falta, per condició

Una fila pot tenir més d'una mancança.

| Mancança | F | P | NA | ND | Total |
|---|---:|---:|---:|---:|---:|
| `falta_ceo` | 0 | 18 | 1 | 0 | 19 |
| `falta_fundador` | 8 | 3.290 | 1 | 0 | 3.299 |
| `incoherent` | 0 | 2 | 0 | 0 | 2 |
| `dubte_obert` | 65 | 75 | 7 | 8 | 155 |
| `falta_arxiu` | 339 | 5.578 | 30 | 8 | 5.955 |

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
| `prova_incompleta` | 2.603 |
| `ok_prova_a` | 1.475 |
| `falta` | 685 |
| `ok_prova_e` | 549 |
| `ok_registre` | 270 |
| `ok_prova_b` | 218 |
| `ok_prova_d` | 85 |
| `ok_columna_antiga` | 66 |
| `rsc_documentat` | 30 |
| `ok_prova_c` | 12 |
| `contradiccio` | 10 |
| `cerca_documentada` | 8 |
| `falta_rsc` | 1 |

### C2 de les files P: prova de no fundador completa per parts

Decisió de Jordi del 24/11/2026 (opció b): un 0 només compta com a documentat si la prova té totes les parts, cadascuna amb la seva cita A/B. Parts: a llista de fundadors; e origen estatal o corporatiu; c any de fundació 64 anys o més abans; b any de fundació i naixement del CEO; d any de fundació i ocupador anterior del CEO.

| | Files P |
|---|---:|
| Amb alguna cita de fundador (criteri anterior al 24/11) | 5.005 (88,9 %) |
| Amb una prova completa per parts (criteri vigent) | 2.339 (41,6 %) |
| … prova a (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 1.475 |
| … prova e (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 549 |
| … prova b (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 218 |
| … prova d (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 85 |
| … prova c (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 12 |
| Cita que diu que el CEO és fundador (contradicció, a revisar) | 10 |
| Amb alguna part però sense cap prova completa | 2.603 |
| Sense cap part documentada | 677 |

| Valor de `c3_arxiu` | Files |
|---|---:|
| `sense_evidencia` | 3.299 |
| `falta_ceo+fundador` | 2.343 |
| `falta_fundador` | 198 |
| `falta_ceo` | 114 |
| `ok` | 57 |
| `falta_fundador_columna_antiga` | 1 |

## Segons l'estat de certificació antic (`sim_estat_certificacio`)

| Estat antic | Files | C1 i C2 | Acabades |
|---|---:|---:|---:|
| `certificada` | 1.773 | 790 (44,6 %) | 0 (0,0 %) |
| `certificada_ceo_pendent` | 108 | 43 (39,8 %) | 3 (2,8 %) |
| `no_certificada` | 241 | 204 (84,6 %) | 8 (3,3 %) |
| `fora_mostra_auditoria` | 3.890 | 1.676 (43,1 %) | 44 (1,1 %) |

## Per empresa (ISIN)

| | Totes les files amb C1 i C2 | Totes les files acabades | Total |
|---|---:|---:|---:|
| Empreses amb almenys un any F | 75 | 1 | 88 |
| Totes les empreses | 453 | 10 | 1.040 |

## Incoherències del CSV (2 files)

| ISIN | Any | FounderCEO | `ceos` | `regles` | Problema |
|---|---|---|---|---|---|
| `DE000KBX1006` | 2019 | 0 | Ralph Heuwing|Peter Laier|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DE000KBX1006` | 2020 | 0 | Peter Laier|Frank Markus Weber|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |

## Avisos (no bloquegen)

- `carrec_no_detectat_a_la_cita`: 125 files
- `cita_que_fa_fundador_el_ceo`: 10 files
- `prova_C2_diferent_de_regles`: 1614 files

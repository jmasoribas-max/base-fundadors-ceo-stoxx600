# Estat de la base per fila

Fitxer generat per `estat/estat_files.py`. No l'editis a mà. Definicions a [`estat/README.md`](README.md).

Entrades llegides:

- `dades/base_isin_any_v8r3.csv` SHA-256 `d55dd6883ceb21b7e589ec666c9a9fdca93247ac31e4bb964174616c78980034`
- `docs/REGISTRE_CANVIS.csv` SHA-256 `b74563b3da4a45b928bfae193c280cb35388b81d4f51bc5b22a6f9b142770758` (13.762 entrades)
- `PENDENTS.md` SHA-256 `923f2d5261bb7eb1e63464a375488a6bed135b23921c1175594acfe6bc0cd684`
- `estat/dubtes_tancats.csv` SHA-256 `1fb00b7ba002b05d3d0a6ad3dcf8f18a86a051054f99acc4f05d91318ae22c3a`

## Resum per etiqueta

| Etiqueta | Files | C1 CEO | C2 fundador | C1 i C2 | C4 coherent i sense dubtes | C3 arxiu | **Acabades** |
|---|---:|---:|---:|---:|---:|---:|---:|
| F (`1`) | 349 | 349 (100,0 %) | 336 (96,3 %) | 336 (96,3 %) | 279 (79,9 %) | 5 (1,4 %) | **3 (0,9 %)** |
| P (`0`) | 5.631 | 5.622 (99,8 %) | 1.389 (24,7 %) | 1.389 (24,7 %) | 5.550 (98,6 %) | 50 (0,9 %) | **50 (0,9 %)** |
| NA | 31 | 30 (96,8 %) | 30 (96,8 %) | 30 (96,8 %) | 24 (77,4 %) | 1 (3,2 %) | **1 (3,2 %)** |
| ND | 1 | 1 (100,0 %) | 1 (100,0 %) | 1 (100,0 %) | 0 (0,0 %) | 1 (100,0 %) | **0 (0,0 %)** |
| **Total** | 6.012 | 6.002 (99,8 %) | 1.756 (29,2 %) | 1.756 (29,2 %) | 5.853 (97,4 %) | 57 (0,9 %) | **54 (0,9 %)** |

## Embut

| Pas | Files |
|---|---:|
| Panell | 6.012 |
| Amb evidència de CEO i de fundador (C1 i C2) | 1.756 (29,2 %) |
| … i coherents, sense dubtes oberts (C4) | 1.671 (27,8 %) |
| … i arxivades a Wayback amb la cita verificada (C3): **acabades** | 54 (0,9 %) |

## Què falta, per condició

Una fila pot tenir més d'una mancança.

| Mancança | F | P | NA | ND | Total |
|---|---:|---:|---:|---:|---:|
| `falta_ceo` | 0 | 9 | 1 | 0 | 10 |
| `falta_fundador` | 13 | 4.242 | 1 | 0 | 4.256 |
| `incoherent` | 0 | 3 | 0 | 0 | 3 |
| `dubte_obert` | 70 | 78 | 7 | 1 | 156 |
| `falta_arxiu` | 344 | 5.581 | 30 | 0 | 5.955 |

## Detall de C1 (CEO) i C2 (fundador)

| Valor de `c1_ceo` | Files |
|---|---:|
| `ok` | 5.972 |
| `rsc_documentat` | 30 |
| `falta` | 9 |
| `falta_rsc` | 1 |

| Valor de `c2_fundador` | Files |
|---|---:|
| `prova_incompleta` | 3.005 |
| `falta` | 1.240 |
| `ok_prova_a` | 610 |
| `ok_prova_e` | 446 |
| `ok_registre` | 270 |
| `ok_prova_b` | 236 |
| `ok_prova_d` | 81 |
| `ok_columna_antiga` | 66 |
| `rsc_documentat` | 30 |
| `ok_prova_c` | 16 |
| `contradiccio` | 10 |
| `falta_rsc` | 1 |
| `cerca_documentada` | 1 |

### C2 de les files P: prova de no fundador completa per parts

Decisió de Jordi del 24/11/2026 (opció b): un 0 només compta com a documentat si la prova té totes les parts, cadascuna amb la seva cita A/B. Parts: a llista de fundadors; e origen estatal o corporatiu; c any de fundació 64 anys o més abans; b any de fundació i naixement del CEO; d any de fundació i ocupador anterior del CEO.

| | Files P |
|---|---:|
| Amb alguna cita de fundador (criteri anterior al 24/11) | 4.619 (82,0 %) |
| Amb una prova completa per parts (criteri vigent) | 1.389 (24,7 %) |
| … prova a (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 610 |
| … prova e (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 446 |
| … prova b (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 236 |
| … prova d (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 81 |
| … prova c (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 16 |
| Cita que diu que el CEO és fundador (contradicció, a revisar) | 10 |
| Amb alguna part però sense cap prova completa | 3.005 |
| Sense cap part documentada | 1.227 |

| Valor de `c3_arxiu` | Files |
|---|---:|
| `sense_evidencia` | 4.256 |
| `falta_ceo+fundador` | 1.468 |
| `falta_fundador` | 117 |
| `falta_ceo` | 113 |
| `ok` | 57 |
| `falta_fundador_columna_antiga` | 1 |

## Segons l'estat de certificació antic (`sim_estat_certificacio`)

| Estat antic | Files | C1 i C2 | Acabades |
|---|---:|---:|---:|
| `certificada` | 1.773 | 515 (29,0 %) | 0 (0,0 %) |
| `certificada_ceo_pendent` | 108 | 37 (34,3 %) | 3 (2,8 %) |
| `no_certificada` | 241 | 193 (80,1 %) | 7 (2,9 %) |
| `fora_mostra_auditoria` | 3.890 | 1.011 (26,0 %) | 44 (1,1 %) |

## Per empresa (ISIN)

| | Totes les files amb C1 i C2 | Totes les files acabades | Total |
|---|---:|---:|---:|
| Empreses amb almenys un any F | 73 | 1 | 88 |
| Totes les empreses | 295 | 10 | 1.040 |

## Incoherències del CSV (3 files)

| ISIN | Any | FounderCEO | `ceos` | `regles` | Problema |
|---|---|---|---|---|---|
| `DE000KBX1006` | 2019 | 0 | Ralph Heuwing|Peter Laier|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DE000KBX1006` | 2020 | 0 | Peter Laier|Frank Markus Weber|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DK0060252690` | 2018 | 0 | Jeremy Schwartz|Anders Boyer | `R-SC;R2b` | P_sense_prova_de_no |

## Avisos (no bloquegen)

- `carrec_no_detectat_a_la_cita`: 125 files
- `cita_que_fa_fundador_el_ceo`: 10 files
- `prova_C2_diferent_de_regles`: 803 files

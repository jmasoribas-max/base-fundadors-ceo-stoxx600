# Estat de la base per fila

Fitxer generat per `estat/estat_files.py`. No l'editis a mà. Definicions a [`estat/README.md`](README.md).

Entrades llegides:

- `dades/base_isin_any_v8r3.csv` SHA-256 `d55dd6883ceb21b7e589ec666c9a9fdca93247ac31e4bb964174616c78980034`
- `docs/REGISTRE_CANVIS.csv` SHA-256 `9c3612d517510d130bbbb9dfb82d693d4a43d1356aba229b82f4c2c4800da1e9` (15.427 entrades)
- `PENDENTS.md` SHA-256 `923f2d5261bb7eb1e63464a375488a6bed135b23921c1175594acfe6bc0cd684`
- `estat/dubtes_tancats.csv` SHA-256 `1fb00b7ba002b05d3d0a6ad3dcf8f18a86a051054f99acc4f05d91318ae22c3a`

## Resum per etiqueta

| Etiqueta | Files | C1 CEO | C2 fundador | C1 i C2 | C4 coherent i sense dubtes | C3 arxiu | **Acabades** |
|---|---:|---:|---:|---:|---:|---:|---:|
| F (`1`) | 349 | 349 (100,0 %) | 336 (96,3 %) | 336 (96,3 %) | 279 (79,9 %) | 5 (1,4 %) | **3 (0,9 %)** |
| P (`0`) | 5.631 | 5.622 (99,8 %) | 2.349 (41,7 %) | 2.349 (41,7 %) | 5.550 (98,6 %) | 50 (0,9 %) | **50 (0,9 %)** |
| NA | 31 | 30 (96,8 %) | 30 (96,8 %) | 30 (96,8 %) | 24 (77,4 %) | 1 (3,2 %) | **1 (3,2 %)** |
| ND | 1 | 1 (100,0 %) | 1 (100,0 %) | 1 (100,0 %) | 0 (0,0 %) | 1 (100,0 %) | **0 (0,0 %)** |
| **Total** | 6.012 | 6.002 (99,8 %) | 2.716 (45,2 %) | 2.716 (45,2 %) | 5.853 (97,4 %) | 57 (0,9 %) | **54 (0,9 %)** |

## Embut

| Pas | Files |
|---|---:|
| Panell | 6.012 |
| Amb evidència de CEO i de fundador (C1 i C2) | 2.716 (45,2 %) |
| … i coherents, sense dubtes oberts (C4) | 2.625 (43,7 %) |
| … i arxivades a Wayback amb la cita verificada (C3): **acabades** | 54 (0,9 %) |

## Què falta, per condició

Una fila pot tenir més d'una mancança.

| Mancança | F | P | NA | ND | Total |
|---|---:|---:|---:|---:|---:|
| `falta_ceo` | 0 | 9 | 1 | 0 | 10 |
| `falta_fundador` | 13 | 3.282 | 1 | 0 | 3.296 |
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
| `prova_incompleta` | 2.594 |
| `ok_prova_a` | 1.483 |
| `falta` | 691 |
| `ok_prova_e` | 551 |
| `ok_registre` | 270 |
| `ok_prova_b` | 218 |
| `ok_prova_d` | 85 |
| `ok_columna_antiga` | 66 |
| `rsc_documentat` | 30 |
| `ok_prova_c` | 12 |
| `contradiccio` | 10 |
| `falta_rsc` | 1 |
| `cerca_documentada` | 1 |

### C2 de les files P: prova de no fundador completa per parts

Decisió de Jordi del 24/11/2026 (opció b): un 0 només compta com a documentat si la prova té totes les parts, cadascuna amb la seva cita A/B. Parts: a llista de fundadors; e origen estatal o corporatiu; c any de fundació 64 anys o més abans; b any de fundació i naixement del CEO; d any de fundació i ocupador anterior del CEO.

| | Files P |
|---|---:|
| Amb alguna cita de fundador (criteri anterior al 24/11) | 5.004 (88,9 %) |
| Amb una prova completa per parts (criteri vigent) | 2.349 (41,7 %) |
| … prova a (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 1.483 |
| … prova e (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 551 |
| … prova b (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 218 |
| … prova d (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 85 |
| … prova c (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 12 |
| Cita que diu que el CEO és fundador (contradicció, a revisar) | 10 |
| Amb alguna part però sense cap prova completa | 2.594 |
| Sense cap part documentada | 678 |

| Valor de `c3_arxiu` | Files |
|---|---:|
| `sense_evidencia` | 3.296 |
| `falta_ceo+fundador` | 2.347 |
| `falta_fundador` | 198 |
| `falta_ceo` | 113 |
| `ok` | 57 |
| `falta_fundador_columna_antiga` | 1 |

## Segons l'estat de certificació antic (`sim_estat_certificacio`)

| Estat antic | Files | C1 i C2 | Acabades |
|---|---:|---:|---:|
| `certificada` | 1.773 | 783 (44,2 %) | 0 (0,0 %) |
| `certificada_ceo_pendent` | 108 | 43 (39,8 %) | 3 (2,8 %) |
| `no_certificada` | 241 | 204 (84,6 %) | 7 (2,9 %) |
| `fora_mostra_auditoria` | 3.890 | 1.686 (43,3 %) | 44 (1,1 %) |

## Per empresa (ISIN)

| | Totes les files amb C1 i C2 | Totes les files acabades | Total |
|---|---:|---:|---:|
| Empreses amb almenys un any F | 75 | 1 | 88 |
| Totes les empreses | 456 | 10 | 1.040 |

## Incoherències del CSV (3 files)

| ISIN | Any | FounderCEO | `ceos` | `regles` | Problema |
|---|---|---|---|---|---|
| `DE000KBX1006` | 2019 | 0 | Ralph Heuwing|Peter Laier|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DE000KBX1006` | 2020 | 0 | Peter Laier|Frank Markus Weber|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DK0060252690` | 2018 | 0 | Jeremy Schwartz|Anders Boyer | `R-SC;R2b` | P_sense_prova_de_no |

## Avisos (no bloquegen)

- `carrec_no_detectat_a_la_cita`: 125 files
- `cita_que_fa_fundador_el_ceo`: 10 files
- `prova_C2_diferent_de_regles`: 1644 files

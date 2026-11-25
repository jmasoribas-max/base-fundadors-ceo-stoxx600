# Estat de la base per fila

Fitxer generat per `estat/estat_files.py`. No l'editis a mà. Definicions a [`estat/README.md`](README.md).

Entrades llegides:

- `dades/base_isin_any_v8r3.csv` SHA-256 `7548d6267aa81145acbcc2bff92fdb70a8aee59020109ea754b874107db765f6`
- `docs/REGISTRE_CANVIS.csv` SHA-256 `befc21dbfea006c1599f29377f821dc31f8e8cfc96c96f0ef4941e4642cefd94` (18.900 entrades)
- `PENDENTS.md` SHA-256 `923f2d5261bb7eb1e63464a375488a6bed135b23921c1175594acfe6bc0cd684`
- `estat/dubtes_tancats.csv` SHA-256 `1fb00b7ba002b05d3d0a6ad3dcf8f18a86a051054f99acc4f05d91318ae22c3a`

## Resum per etiqueta

| Etiqueta | Files | C1 CEO | C2 fundador | C1 i C2 | C4 coherent i sense dubtes | C3 arxiu | **Acabades** |
|---|---:|---:|---:|---:|---:|---:|---:|
| F (`1`) | 344 | 344 (100,0 %) | 336 (97,7 %) | 336 (97,7 %) | 279 (81,1 %) | 27 (7,8 %) | **22 (6,4 %)** |
| P (`0`) | 5.629 | 5.611 (99,7 %) | 5.084 (90,3 %) | 5.069 (90,1 %) | 5.552 (98,6 %) | 185 (3,3 %) | **185 (3,3 %)** |
| NA | 31 | 30 (96,8 %) | 30 (96,8 %) | 30 (96,8 %) | 24 (77,4 %) | 16 (51,6 %) | **13 (41,9 %)** |
| ND | 8 | 8 (100,0 %) | 8 (100,0 %) | 8 (100,0 %) | 0 (0,0 %) | 0 (0,0 %) | **0 (0,0 %)** |
| **Total** | 6.012 | 5.993 (99,7 %) | 5.458 (90,8 %) | 5.443 (90,5 %) | 5.855 (97,4 %) | 228 (3,8 %) | **220 (3,7 %)** |

## Embut

| Pas | Files |
|---|---:|
| Panell | 6.012 |
| Amb evidència de CEO i de fundador (C1 i C2) | 5.443 (90,5 %) |
| … i coherents, sense dubtes oberts (C4) | 5.309 (88,3 %) |
| … i arxivades a Wayback amb la cita verificada (C3): **acabades** | 220 (3,7 %) |

## Què falta, per condició

Una fila pot tenir més d'una mancança.

| Mancança | F | P | NA | ND | Total |
|---|---:|---:|---:|---:|---:|
| `falta_ceo` | 0 | 18 | 1 | 0 | 19 |
| `falta_fundador` | 8 | 545 | 1 | 0 | 554 |
| `incoherent` | 0 | 2 | 0 | 0 | 2 |
| `dubte_obert` | 65 | 75 | 7 | 8 | 155 |
| `falta_arxiu` | 317 | 5.444 | 15 | 8 | 5.784 |

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
| `ok_prova_a` | 1.886 |
| `ok_prova_b` | 1.844 |
| `ok_prova_d` | 711 |
| `prova_incompleta` | 535 |
| `ok_prova_e` | 494 |
| `ok_registre` | 272 |
| `ok_prova_c` | 121 |
| `ok_columna_antiga` | 64 |
| `rsc_documentat` | 30 |
| `ok_prova_b|b` | 24 |
| `contradiccio` | 10 |
| `cerca_documentada` | 8 |
| `falta` | 8 |
| `ok_prova_d|d` | 4 |
| `falta_rsc` | 1 |

### C2 de les files P: prova de no fundador completa per parts

Decisió de Jordi del 24/11/2026 (opció b): un 0 només compta com a documentat si la prova té totes les parts, cadascuna amb la seva cita A/B. Parts: a llista de fundadors; e origen estatal o corporatiu; c any de fundació 64 anys o més abans; b any de fundació i naixement del CEO; d any de fundació i ocupador anterior del CEO.

| | Files P |
|---|---:|
| Amb alguna cita de fundador (criteri anterior al 24/11) | 5.536 (98,3 %) |
| Amb una prova completa per parts (criteri vigent) | 5.084 (90,3 %) |
| … prova a (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 1.886 |
| … prova e (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 494 |
| … prova b (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 1.868 |
| … prova d (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 715 |
| … prova c (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 121 |
| Cita que diu que el CEO és fundador (contradicció, a revisar) | 10 |
| Amb alguna part però sense cap prova completa | 535 |
| Sense cap part documentada | 0 |

| Valor de `c3_arxiu` | Files |
|---|---:|
| `falta_ceo+fundador` | 4.551 |
| `sense_evidencia` | 569 |
| `falta_fundador` | 426 |
| `falta_ceo` | 237 |
| `ok` | 228 |
| `falta_fundador_columna_antiga` | 1 |

## Segons l'estat de certificació antic (`sim_estat_certificacio`)

| Estat antic | Files | C1 i C2 | Acabades |
|---|---:|---:|---:|
| `certificada` | 1.773 | 1.626 (91,7 %) | 3 (0,2 %) |
| `certificada_ceo_pendent` | 108 | 94 (87,0 %) | 7 (6,5 %) |
| `no_certificada` | 241 | 212 (88,0 %) | 133 (55,2 %) |
| `fora_mostra_auditoria` | 3.890 | 3.511 (90,3 %) | 77 (2,0 %) |

## Per empresa (ISIN)

| | Totes les files amb C1 i C2 | Totes les files acabades | Total |
|---|---:|---:|---:|
| Empreses amb almenys un any F | 81 | 4 | 88 |
| Totes les empreses | 906 | 29 | 1.040 |

## Incoherències del CSV (2 files)

| ISIN | Any | FounderCEO | `ceos` | `regles` | Problema |
|---|---|---|---|---|---|
| `DE000KBX1006` | 2019 | 0 | Ralph Heuwing|Peter Laier|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DE000KBX1006` | 2020 | 0 | Peter Laier|Frank Markus Weber|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |

## Avisos (no bloquegen)

- `carrec_no_detectat_a_la_cita`: 125 files
- `cita_que_fa_fundador_el_ceo`: 10 files
- `prova_C2_diferent_de_regles`: 2939 files

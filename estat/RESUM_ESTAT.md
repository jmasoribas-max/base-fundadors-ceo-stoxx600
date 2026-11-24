# Estat de la base per fila

Fitxer generat per `estat/estat_files.py`. No l'editis a mà. Definicions a [`estat/README.md`](README.md).

Entrades llegides:

- `dades/base_isin_any_v8r3.csv` SHA-256 `d55dd6883ceb21b7e589ec666c9a9fdca93247ac31e4bb964174616c78980034`
- `docs/REGISTRE_CANVIS.csv` SHA-256 `b548d854c0b718f47831ee37c78f1e823ef5bb4dfaccfef82b8a3378fceb2679` (13.623 entrades)
- `PENDENTS.md` SHA-256 `923f2d5261bb7eb1e63464a375488a6bed135b23921c1175594acfe6bc0cd684`
- `estat/dubtes_tancats.csv` SHA-256 `f64b2f2642272a7a80460e503ba0f26b631a2eb0db74b66941df0038cf6c4714`

## Resum per etiqueta

| Etiqueta | Files | C1 CEO | C2 fundador | C1 i C2 | C4 coherent i sense dubtes | C3 arxiu | **Acabades** |
|---|---:|---:|---:|---:|---:|---:|---:|
| F (`1`) | 349 | 349 (100,0 %) | 329 (94,3 %) | 329 (94,3 %) | 219 (62,8 %) | 0 (0,0 %) | **0 (0,0 %)** |
| P (`0`) | 5.631 | 5.618 (99,8 %) | 0 (0,0 %) | 0 (0,0 %) | 5.501 (97,7 %) | 0 (0,0 %) | **0 (0,0 %)** |
| NA | 31 | 27 (87,1 %) | 27 (87,1 %) | 27 (87,1 %) | 24 (77,4 %) | 0 (0,0 %) | **0 (0,0 %)** |
| ND | 1 | 1 (100,0 %) | 1 (100,0 %) | 1 (100,0 %) | 0 (0,0 %) | 1 (100,0 %) | **0 (0,0 %)** |
| **Total** | 6.012 | 5.995 (99,7 %) | 357 (5,9 %) | 357 (5,9 %) | 5.744 (95,5 %) | 1 (0,0 %) | **0 (0,0 %)** |

## Embut

| Pas | Files |
|---|---:|
| Panell | 6.012 |
| Amb evidència de CEO i de fundador (C1 i C2) | 357 (5,9 %) |
| … i coherents, sense dubtes oberts (C4) | 243 (4,0 %) |
| … i arxivades a Wayback amb la cita verificada (C3): **acabades** | 0 (0,0 %) |

## Què falta, per condició

Una fila pot tenir més d'una mancança.

| Mancança | F | P | NA | ND | Total |
|---|---:|---:|---:|---:|---:|
| `falta_ceo` | 0 | 13 | 4 | 0 | 17 |
| `falta_fundador` | 20 | 5.631 | 4 | 0 | 5.655 |
| `incoherent` | 0 | 3 | 0 | 0 | 3 |
| `dubte_obert` | 130 | 128 | 7 | 1 | 266 |
| `falta_arxiu` | 349 | 5.631 | 31 | 0 | 6.011 |

## Detall de C1 (CEO) i C2 (fundador)

| Valor de `c1_ceo` | Files |
|---|---:|
| `ok` | 5.968 |
| `rsc_documentat` | 27 |
| `falta` | 13 |
| `falta_rsc` | 4 |

| Valor de `c2_fundador` | Files |
|---|---:|
| `falta` | 5.651 |
| `ok_registre` | 263 |
| `ok_columna_antiga` | 66 |
| `rsc_documentat` | 27 |
| `falta_rsc` | 4 |
| `cerca_documentada` | 1 |

### C2 de les files P: prova de no fundador completa per parts

Decisió de Jordi del 24/11/2026 (opció b): un 0 només compta com a documentat si la prova té totes les parts, cadascuna amb la seva cita A/B. Parts: a llista de fundadors; e origen estatal o corporatiu; c any de fundació 64 anys o més abans; b any de fundació i naixement del CEO; d any de fundació i ocupador anterior del CEO.

| | Files P |
|---|---:|
| Amb alguna cita de fundador (criteri anterior al 24/11) | 4.592 (81,5 %) |
| Amb una prova completa per parts (criteri vigent) | 0 (0,0 %) |
| … prova a (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 0 |
| … prova e (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 0 |
| … prova b (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 0 |
| … prova d (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 0 |
| … prova c (per a tots els CEO de la fila o, amb co-CEO, per a algun) | 0 |
| Cita que diu que el CEO és fundador (contradicció, a revisar) | 0 |
| Amb alguna part però sense cap prova completa | 0 |
| Sense cap part documentada | 5.631 |

| Valor de `c3_arxiu` | Files |
|---|---:|
| `sense_evidencia` | 5.655 |
| `falta_ceo+fundador` | 356 |
| `ok` | 1 |

## Segons l'estat de certificació antic (`sim_estat_certificacio`)

| Estat antic | Files | C1 i C2 | Acabades |
|---|---:|---:|---:|
| `certificada` | 1.773 | 296 (16,7 %) | 0 (0,0 %) |
| `certificada_ceo_pendent` | 108 | 23 (21,3 %) | 0 (0,0 %) |
| `no_certificada` | 241 | 37 (15,4 %) | 0 (0,0 %) |
| `fora_mostra_auditoria` | 3.890 | 1 (0,0 %) | 0 (0,0 %) |

## Per empresa (ISIN)

| | Totes les files amb C1 i C2 | Totes les files acabades | Total |
|---|---:|---:|---:|
| Empreses amb almenys un any F | 59 | 0 | 88 |
| Totes les empreses | 62 | 0 | 1.040 |

## Incoherències del CSV (3 files)

| ISIN | Any | FounderCEO | `ceos` | `regles` | Problema |
|---|---|---|---|---|---|
| `DE000KBX1006` | 2019 | 0 | Ralph Heuwing|Peter Laier|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DE000KBX1006` | 2020 | 0 | Peter Laier|Frank Markus Weber|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DK0060252690` | 2018 | 0 | Jeremy Schwartz|Anders Boyer | `R-SC;R2b` | P_sense_prova_de_no |

## Avisos (no bloquegen)

- `carrec_no_detectat_a_la_cita`: 125 files

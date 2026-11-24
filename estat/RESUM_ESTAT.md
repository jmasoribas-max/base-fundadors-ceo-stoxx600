# Estat de la base per fila

Fitxer generat per `estat/estat_files.py`. No l'editis a mà. Definicions a [`estat/README.md`](README.md).

Entrades llegides:

- `dades/base_isin_any_v8r3.csv` SHA-256 `7548d6267aa81145acbcc2bff92fdb70a8aee59020109ea754b874107db765f6`
- `docs/REGISTRE_CANVIS.csv` SHA-256 `8fdcbd13041db8b34167280e08db3eb34b6ad35e37693d00f311f6eec3b96e51` (13.937 entrades)
- `PENDENTS.md` SHA-256 `923f2d5261bb7eb1e63464a375488a6bed135b23921c1175594acfe6bc0cd684`
- `estat/dubtes_tancats.csv` SHA-256 `1fb00b7ba002b05d3d0a6ad3dcf8f18a86a051054f99acc4f05d91318ae22c3a`

## Resum per etiqueta

| Etiqueta | Files | C1 CEO | C2 fundador | C1 i C2 | C4 coherent i sense dubtes | C3 arxiu | **Acabades** |
|---|---:|---:|---:|---:|---:|---:|---:|
| F (`1`) | 344 | 344 (100,0 %) | 336 (97,7 %) | 336 (97,7 %) | 279 (81,1 %) | 5 (1,5 %) | **3 (0,9 %)** |
| P (`0`) | 5.629 | 5.611 (99,7 %) | 4.620 (82,1 %) | 4.606 (81,8 %) | 5.552 (98,6 %) | 353 (6,3 %) | **352 (6,3 %)** |
| NA | 31 | 30 (96,8 %) | 30 (96,8 %) | 30 (96,8 %) | 24 (77,4 %) | 1 (3,2 %) | **1 (3,2 %)** |
| ND | 8 | 8 (100,0 %) | 8 (100,0 %) | 8 (100,0 %) | 0 (0,0 %) | 0 (0,0 %) | **0 (0,0 %)** |
| **Total** | 6.012 | 5.993 (99,7 %) | 4.994 (83,1 %) | 4.980 (82,8 %) | 5.855 (97,4 %) | 359 (6,0 %) | **356 (5,9 %)** |

## Embut

| Pas | Files |
|---|---:|
| Panell | 6.012 |
| Amb evidència de CEO i de fundador (C1 i C2) | 4.980 (82,8 %) |
| … i coherents, sense dubtes oberts (C4) | 4.855 (80,8 %) |
| … i arxivades a Wayback amb la cita verificada (C3): **acabades** | 356 (5,9 %) |

## Què falta, per condició

Una fila pot tenir més d'una mancança.

| Mancança | F | P | NA | ND | Total |
|---|---:|---:|---:|---:|---:|
| `falta_ceo` | 0 | 18 | 1 | 0 | 19 |
| `falta_fundador` | 8 | 1.009 | 1 | 0 | 1.018 |
| `incoherent` | 0 | 2 | 0 | 0 | 2 |
| `dubte_obert` | 65 | 75 | 7 | 8 | 155 |
| `falta_arxiu` | 339 | 5.276 | 30 | 8 | 5.653 |

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
| `ok_registre` | 4.525 |
| `falta` | 1.017 |
| `ok_columna_antiga` | 431 |
| `rsc_documentat` | 30 |
| `cerca_documentada` | 8 |
| `falta_rsc` | 1 |

| Valor de `c3_arxiu` | Files |
|---|---:|
| `falta_ceo+fundador` | 3.814 |
| `sense_evidencia` | 1.032 |
| `falta_ceo` | 660 |
| `ok` | 359 |
| `falta_fundador` | 142 |
| `falta_fundador_columna_antiga` | 5 |

## Segons l'estat de certificació antic (`sim_estat_certificacio`)

| Estat antic | Files | C1 i C2 | Acabades |
|---|---:|---:|---:|
| `certificada` | 1.773 | 774 (43,7 %) | 0 (0,0 %) |
| `certificada_ceo_pendent` | 108 | 108 (100,0 %) | 38 (35,2 %) |
| `no_certificada` | 241 | 241 (100,0 %) | 22 (9,1 %) |
| `fora_mostra_auditoria` | 3.890 | 3.857 (99,2 %) | 296 (7,6 %) |

## Per empresa (ISIN)

| | Totes les files amb C1 i C2 | Totes les files acabades | Total |
|---|---:|---:|---:|
| Empreses amb almenys un any F | 81 | 1 | 88 |
| Totes les empreses | 845 | 37 | 1.040 |

## Incoherències del CSV (2 files)

| ISIN | Any | FounderCEO | `ceos` | `regles` | Problema |
|---|---|---|---|---|---|
| `DE000KBX1006` | 2019 | 0 | Ralph Heuwing|Peter Laier|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DE000KBX1006` | 2020 | 0 | Peter Laier|Frank Markus Weber|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |

## Avisos (no bloquegen)

- `carrec_no_detectat_a_la_cita`: 125 files

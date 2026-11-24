# Estat de la base per fila

Fitxer generat per `estat/estat_files.py`. No l'editis a mà. Definicions a [`estat/README.md`](README.md).

Entrades llegides:

- `dades/base_isin_any_v8r3.csv` SHA-256 `d55dd6883ceb21b7e589ec666c9a9fdca93247ac31e4bb964174616c78980034`
- `docs/REGISTRE_CANVIS.csv` SHA-256 `c3bc7cf9eb52697c4eeddb98c39d6039b38dd64e45421e6e0bdab7263721f9d4` (12.298 entrades)
- `PENDENTS.md` SHA-256 `399a47bab6a4dde3e6e1b2ea075572386dadfb3c929bd6963b179edc741dd8fe`
- `estat/dubtes_tancats.csv` SHA-256 `e008e8b1910c0c23c7b80bed48436cc77c9464c86ea5a6c39ea941f81a4c67f1`

## Resum per etiqueta

| Etiqueta | Files | C1 CEO | C2 fundador | C1 i C2 | C4 coherent i sense dubtes | C3 arxiu | **Acabades** |
|---|---:|---:|---:|---:|---:|---:|---:|
| F (`1`) | 349 | 331 (94,8 %) | 292 (83,7 %) | 275 (78,8 %) | 202 (57,9 %) | 0 (0,0 %) | **0 (0,0 %)** |
| P (`0`) | 5.631 | 4.343 (77,1 %) | 4.592 (81,5 %) | 4.142 (73,6 %) | 5.509 (97,8 %) | 278 (4,9 %) | **278 (4,9 %)** |
| NA | 31 | 27 (87,1 %) | 27 (87,1 %) | 27 (87,1 %) | 24 (77,4 %) | 0 (0,0 %) | **0 (0,0 %)** |
| ND | 1 | 1 (100,0 %) | 1 (100,0 %) | 1 (100,0 %) | 0 (0,0 %) | 1 (100,0 %) | **0 (0,0 %)** |
| **Total** | 6.012 | 4.702 (78,2 %) | 4.912 (81,7 %) | 4.445 (73,9 %) | 5.735 (95,4 %) | 279 (4,6 %) | **278 (4,6 %)** |

## Embut

| Pas | Files |
|---|---:|
| Panell | 6.012 |
| Amb evidència de CEO i de fundador (C1 i C2) | 4.445 (73,9 %) |
| … i coherents, sense dubtes oberts (C4) | 4.281 (71,2 %) |
| … i arxivades a Wayback amb la cita verificada (C3): **acabades** | 278 (4,6 %) |

## Què falta, per condició

Una fila pot tenir més d'una mancança.

| Mancança | F | P | NA | ND | Total |
|---|---:|---:|---:|---:|---:|
| `falta_ceo` | 18 | 1.288 | 4 | 0 | 1.310 |
| `falta_fundador` | 57 | 1.039 | 4 | 0 | 1.100 |
| `incoherent` | 0 | 3 | 0 | 0 | 3 |
| `dubte_obert` | 147 | 119 | 7 | 1 | 274 |
| `falta_arxiu` | 349 | 5.353 | 31 | 0 | 5.733 |

## Detall de C1 (CEO) i C2 (fundador)

| Valor de `c1_ceo` | Files |
|---|---:|
| `ok` | 4.675 |
| `falta` | 1.224 |
| `cita_sense_nom` | 79 |
| `rsc_documentat` | 27 |
| `falta_rsc` | 4 |
| `co_ceo_parcial` | 3 |

| Valor de `c2_fundador` | Files |
|---|---:|
| `ok_registre` | 4.450 |
| `falta` | 1.096 |
| `ok_columna_antiga` | 434 |
| `rsc_documentat` | 27 |
| `falta_rsc` | 4 |
| `cerca_documentada` | 1 |

| Valor de `c3_arxiu` | Files |
|---|---:|
| `falta_ceo+fundador` | 3.921 |
| `sense_evidencia` | 1.567 |
| `ok` | 279 |
| `falta_ceo` | 172 |
| `falta_fundador` | 72 |
| `falta_fundador_columna_antiga` | 1 |

## Segons l'estat de certificació antic (`sim_estat_certificacio`)

| Estat antic | Files | C1 i C2 | Acabades |
|---|---:|---:|---:|
| `certificada` | 1.773 | 343 (19,3 %) | 0 (0,0 %) |
| `certificada_ceo_pendent` | 108 | 108 (100,0 %) | 0 (0,0 %) |
| `no_certificada` | 241 | 241 (100,0 %) | 1 (0,4 %) |
| `fora_mostra_auditoria` | 3.890 | 3.753 (96,5 %) | 277 (7,1 %) |

## Per empresa (ISIN)

| | Totes les files amb C1 i C2 | Totes les files acabades | Total |
|---|---:|---:|---:|
| Empreses amb almenys un any F | 49 | 0 | 88 |
| Totes les empreses | 714 | 32 | 1.040 |

## Incoherències del CSV (3 files)

| ISIN | Any | FounderCEO | `ceos` | `regles` | Problema |
|---|---|---|---|---|---|
| `DE000KBX1006` | 2019 | 0 | Ralph Heuwing|Peter Laier|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DE000KBX1006` | 2020 | 0 | Peter Laier|Frank Markus Weber|Jürgen Wilder | `R-SC;R2b` | P_sense_prova_de_no |
| `DK0060252690` | 2018 | 0 | Jeremy Schwartz|Anders Boyer | `R-SC;R2b` | P_sense_prova_de_no |

## Avisos (no bloquegen)

- `carrec_no_detectat_a_la_cita`: 137 files

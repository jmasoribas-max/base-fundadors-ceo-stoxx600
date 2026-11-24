# Lot de correcció 2: decisions de criteri del 24/11/2026 i tancaments dels lots 19 i 20

> **Canvi a l'hora d'aplicar (Claude, 24/11/2026):** la C3 (Dassault Systèmes 2016-2020, 100 cel·les) queda **fora** d'aquest lot fins que es registri la frase del comunicat que anomena Bernard Charlès amb el nom complet (X03 només diu «Bernard»; el web retornava 403). Els canvis preparats són a `correccio2_c3_dassault_pendent.csv`. Aquest lot aplica 535 cel·les.

- **Proposta de:** Claude, 24/11/2026. **Estat:** preparat, **no aplicat**.
- **Aprovació:** decisions de Jordi del 24/11/2026 a `CLAUDE.md`: «(tarda)» (Q2, Q3, Q8, Q9 a Telefónica, Q11) i «(vespre)» («d'acord amb totes» les recomanacions de [`docs/ANALISI_CRITERIS_v2_20261124.md`](../docs/ANALISI_CRITERIS_v2_20261124.md), regla única del president executiu, C1 no s'aplica, C2, C3 i C4 «amb les marques i robusteses de l'anàlisi»). Els canvis de traçabilitat dels tancaments (blocs T19 i T20) vénen de les frases de `estat/dubtes_tancats.csv` (lots 19 i 20, fusionats per Jordi) i dels resums de la cerca verificats «ok»; el canvi de dades queda pendent de l'OK de Jordi al PR. La columna `aprovacio` de cada fila cita la decisió.
- **Canvis:** [`correccio2_canvis.csv`](correccio2_canvis.csv), **635 cel·les a 139 files** (`CO2-001` a `CO2-635`). **16 files canvien de `FounderCEO`.**
- **Pendents:** [`correccio2_pendents.csv`](correccio2_pendents.csv), 33 línies: canvis que encara no es poden aplicar perquè falta una cita al registre, una cerca o una columna nova.
- **Com s'aplica:** `python3 estat/aplica_canvis.py lots/correccio2_canvis.csv` (prova en sec: 0 discrepàncies de `valor_actual` al CSV i a l'xlsx, comprovat el 24/11/2026); amb `--aplica --origen correccio2_claude` escriu el CSV, l'xlsx, el registre i les fitxes. Després cal regenerar l'estat, el dashboard i el manifest.
- Generat per script a partir de la base (`valor_actual` llegit de `dades/base_isin_any_v8r3.csv`; només s'hi escriuen les cel·les que canvien). Les columnes `sim_*` i les instantànies (`*_v8`, `*_v75r2`, `a_mostra_principal_v*`) no es toquen, llevat de `sim_ceo_aplicat` a Ferrovial (ha de coincidir amb `ceos`, comprovació C4 de `estat/estat_files.py`).

## Què canvia, per decisió

| Bloc | Cel·les | Files | Què |
|---|---:|---:|---|
| C2 Sopra Steria `FR0000050809` 2025 | 25 | 1 | FounderCEO ND → 0 (prova a, P8); `regles` cap → a; marca `llista_exhaustiva=implicita`; entra a la mostra principal; es buiden els 4 camps de motiu de ND; 17 robusteses a 0 |
| C3 Dassault Systèmes `FR0000130650` 2016-2020 | 100 | 5 | FounderCEO 0 → 1 (D37, «Co-Founder»); `regles` a → D37; marca D37; D37a (`d37_data_cita` 2026-02-21, no contemporània); D37b (`fundador_transformador`=1: fundació 1981, entrada 1983); `pre_d37` i sense transformador = ND; 11 robusteses a 1 |
| C4 Bridgepoint `GB00BND88V85` 2021-2022 | 42 | 2 | FounderCEO 0 → 1 (D37, «Bridgepoint's Founder»); `regles` e → D37; marques `fundacio_corporativa;origen_intern;fundacio_no_nova;D37`; D37a (2024-06-06, no); sense origen intern = ND; 15 robusteses a 1 |
| Q3 Cellnex `ES0105066007` 2016-2022 i `ES0105066023` 2019 | 197 | 8 | FounderCEO → ND (7 d'1 i la línia de drets del 2019 de 0); `regles` → cap; motiu de ND; surten de la mostra principal (i de les mostres de verificats i certificades) |
| Q8 Ferrovial (`ES0118900010` 2016-2022, `ES0618900981` 2016, `ES06189009A2` 2017) | 45 | 9 | `ceos` i `sim_ceo_aplicat` + Rafael del Pino y Calvo-Sotelo; `n_ceos` 2; marques `co_ceo;llista_exhaustiva=implicita;a_fundador_unic` (fora `nota_del_pino_president_exec`); `regles` b → a (F01, P8) |
| Q9 i Q9b (regla única) | 20 | 17 | `ceo_president_exec` a Telefónica 2016-2025, Mapfre 2016, 2017, 2019, 2025 i Inditex 2016-2018; Inditex (R3, càrrec vacant) `founderceo_rob_sense_r3` 0 → NA_sense_ceo |
| C1 BME `ES0115056139` 2017-2018 | 2 | 2 | No es canvia el CEO (Zoido, «primer ejecutivo»); només la marca `ceo_president_exec` |
| Q10 Luxottica `IT0001479374` 2016-2017 | 4 | 2 | Fora `co_ceo` (`n_ceos`=1); `founderceo_rob_r3_president_exec_com_1` 0 → 1 (Del Vecchio, fundador i president executiu) |
| Q8b EssilorLuxottica `FR0000121667` 2018-2020 | 3 | 3 | Fora `co_ceo` (`n_ceos`=1) |
| Q11 Rubis (`FR0000121253` 2016, `FR0013269123` 2017-2025) | 10 | 10 | Fora `de_facto` (el Gérant és CEO per R1) |
| Q12 Tritax `GB00BG49KP99` 2018-2025 i Primary Health `GB00BYRJ5J14` 2020 | 9 | 9 | Marca `gestio_externa` |
| Q2 Rightmove 2016, Reply 2021-2025 (i la línia de drets `IT0005619678` 2024) | 7 | 7 | `regles` cita_fundador → D37 |
| Q4 Energean `GB00BG12Y042` 2023 | 3 | 1 | `regles` → D37; D37a (2024-03-20, no) |
| Q5 Paysafe `GB0034264548` 2016-2017 | 8 | 2 | `regles` → D37; D37a (2019-05-30, no); `founderceo_rob_cita_contemporania` 1 → 0 |
| Q5b Merlin `GB00BDZT6P94` 2016-2019 | 24 | 4 | `regles` → D37; marca `fundacio_no_nova` (MBO del 1999, P1); `fundador_transformador`=1; D37a (2023-06-18, no); `founderceo_rob_cita_contemporania` 1 → 0 (cerca negativa a l'AR 2013-2019 i al fullet del 2013) |
| Q6 Evraz `GB00B71N6K86` 2018-2020 | 3 | 3 | Marca `si_font_B` |
| T19 tancaments del lot 19 | 89 | 34 | KPN 2016-2025 i Sandoz 2023-2025 i PZU 2024: `regles` + e i `founderceo_rob_c_com_nd` ND → 0; PKO 2022-2023: `regles` → e (sense b, com diu el tancament) i `c_com_nd` → 0; STMicroelectronics 2018-2025: b → d; Balder 2016-2025: cap;FT → D37, `founderceo_rob_sense_ft` ND → 1, D37a (2025-08-18) i `founderceo_rob_cita_contemporania` 1 → 0 (2016-2024) |
| T20 tancaments del lot 20 (resums «ok») | 44 | 20 | Allreal 2019-2022 b → d; Genmab `DK0010272202` 2016-2025 cita_fundador → D37, D37a (F-1 del 2019-05-28: no el 2016-2018, sí el 2019-2025) i `founderceo_rob_cita_contemporania` 1 → 0 el 2016-2018 (cerca negativa); Pandora 2018 R-SC;R2b → R2b;a; Siemens Gamesa 2020-2021 b → d; `GB00BKX5CN86` 2016 + `conflicte_fonts`; Oxford Nanopore 2022 → D37; RTL 2019 b → d i + `dubte_D1` |

Per camp: `regles` 92, `marques` 69, `d37_data_cita` 34, `d37_cita_contemporania` 34, `founderceo_rob_c_com_nd` 32, `founderceo_rob_cita_contemporania` 27, `founderceo_rob_sense_ft` 26, `founderceo_rob_sense_r3` 19, `founderceo_rob_r3_president_exec_com_1` 18, `FounderCEO` 16, `founderceo_rob_na_com_0`, `_ft_nomes_ab`, `_r2b_com_na`, `_sense_fundador_transformador`, `sense_fundador_transformador`, `_sense_decisions_doctorat` i `_nd_com_1` 16 cadascun, `founderceo_rob_pre_d37` 14, `_spinoff_com_0`, `_sense_origen_intern` i `_fundador_escissio_com_0` 11, `motiu_nd`, `detall_motiu_nd`, `motiu_nd_article`, `_fundacio_corporativa_com_0`, `fundador_transformador`, `ceos`, `sim_ceo_aplicat` i `n_ceos` 9, `a_mostra_principal` 8, `founderceo_rob_nd_com_0`, `_na_i_nd_com_0`, `a_mostra_nomes_verificats` i `a_mostra_nomes_certificades` 7, `tancament_nd` 1.

## Files que canvien de FounderCEO (16)

| ISIN | Empresa | Anys | De | A | Decisió |
|---|---|---|---|---|---|
| `FR0000050809` | Sopra Steria | 2025 | ND | 0 | C2 |
| `FR0000130650` | Dassault Systèmes | 2016-2020 | 0 | 1 | C3 |
| `GB00BND88V85` | Bridgepoint | 2021-2022 | 0 | 1 | C4 |
| `ES0105066007` | Cellnex | 2016-2022 | 1 | ND | Q3 |
| `ES0105066023` | Cellnex (drets) | 2019 | 0 | ND | Q3: mateixa empresa, CEO i any que `ES0105066007` 2019; el 0 era per la regla b sense cap part citada, que amb l'opció b del 24/11 no és un 0 documentat. Ja era fora de la mostra (`dret_temporal`) |

**Mostra principal** (`a_mostra_principal`=1): abans 5.967 files, 348 F i 5.619 P (5,832 %); després **5.961 files, 348 F i 5.613 P (5,838 %)**. Surten 7 F (Cellnex) i entra 1 P (Sopra Steria); 7 P passen a F (Dassault Systèmes i Bridgepoint). La diferència amb l'«efecte conjunt» de l'anàlisi (346 F) és Q1 (Standard Life Aberdeen, −2 F), que va a pendents.

## Regla de cada columna derivada

Comprovades contra tota la base (6.012 files). Les robusteses `founderceo_rob_*` copien `FounderCEO` llevat que la fila tingui el tret que tracta la columna. Hi ha 33 files ND → 0 dels lots de Doctorat i ND-1 i 7 de Cellnex amb robusteses que no es van recalcular (porten el valor de la v75r2); no s'han fet servir per deduir les regles i, fora de Cellnex, no es toquen en aquest lot.

| Columna | Regla | D'on surt |
|---|---|---|
| `a_mostra_principal` | 1 si `fora_panel`=0, FounderCEO ∈ {0, 1} i `dret_temporal`≠1 (J14) | Diccionari; 6.012/6.012 files coherents |
| `a_mostra_nomes_verificats` | 1 si `a_mostra_principal`=1 i `verificacio_documental`=verificat | 6.012/6.012 coherents |
| `a_mostra_nomes_certificades` | 1 si `a_mostra_principal`=1 i `sim_estat_certificacio`=certificada | 6.012/6.012 coherents |
| `founderceo_rob_na_com_0` | NA → 0; resta, còpia (ND es queda ND) | Sopra Steria 2025 i les 31 NA |
| `founderceo_rob_nd_com_0`, `founderceo_rob_na_i_nd_com_0` | ND → 0 (i NA → 0 a la segona); resta, còpia | Sopra Steria 2025 |
| `founderceo_rob_nd_com_1` | ND → 1; resta, còpia | Sopra Steria 2025 |
| `founderceo_rob_fundacio_corporativa_com_0` | F amb la marca `fundacio_corporativa` → 0; resta, còpia | Galapagos, Homeserve |
| `founderceo_rob_r3_president_exec_com_1` | President executiu fundador que només seria CEO per R3 → 1; resta, còpia | Richemont 2017; Q10 (Luxottica) |
| `founderceo_rob_sense_ft`, `founderceo_rob_ft_nomes_ab` | Fila on l'1 ve de l'FT → valor sense FT; resta, còpia | CTS Eventim, LVMH, Balder |
| `founderceo_rob_spinoff_com_0` | F amb `spinoff`=1 → 0; resta, còpia | Arkema, Idorsia, Homeserve |
| `founderceo_rob_fundador_escissio_com_0` | F amb `fundador_escissio`=1 → 0; resta, còpia | Arkema, Homeserve |
| `founderceo_rob_r2b_com_na` | R2b → NA; resta, còpia | Knorr-Bremse, Pandora |
| `founderceo_rob_pre_d37` | Fila on l'1 ve de la D37 → classificació amb el criteri anterior (proves a-e; ND si cap no tanca); resta, còpia | WPP (0), B&M (0), Investec (ND) |
| `founderceo_rob_sense_origen_intern` | F amb la marca `origen_intern` (divisió interna o MBO) → ND; resta, còpia | Merlin, Paysafe, Allfunds, IMCD… i metodologia v0.10.10 |
| `founderceo_rob_sense_r3` | CEO per R3 (càrrec vacant) → NA_sense_ceo; resta, còpia | ITV 2017, Schindler, Vifor, Unipol |
| `founderceo_rob_cita_contemporania` | Fila on l'1 ve d'una D37 sense cap cita contemporània de l'emissor (data ≤ 31/10/t o del mateix any) → 0; resta, còpia | Regla 27 (B&M) i l'anàlisi (Paysafe, Merlin, C3, C4). Vegeu la reserva als pendents: a Investec i Primary Health 2020 la base hi posa el valor de `pre_d37` |
| `founderceo_rob_sense_fundador_transformador` i `sense_fundador_transformador` | Si `fundador_transformador`=1, el valor de `founderceo_rob_pre_d37`; si no, còpia | Fórmula de la v8 r1 (`docs/REGISTRE_CANVIS.md`, §4) |
| `founderceo_rob_c_com_nd` | 0 només per la prova c (`c_AAF64_reserva` sola) → ND; resta, còpia | Metodologia v0.10.10 (P8 de la v7.5) |
| `founderceo_rob_sense_decisions_doctorat` | FounderCEO sense les decisions de Doctorat aplicades a la fila; si la fila ja no depèn de cap decisió de Doctorat, còpia | Fórmula de la v8 r1. A Cellnex la C0220 queda substituïda per la Q3 de Jordi: la columna pren ND |
| `motiu_nd`, `detall_motiu_nd`, `motiu_nd_article`, `tancament_nd` | Es buiden si la fila deixa de ser ND (precedent CO1-002); en una fila nova ND, valors existents a la base (`proves_a_e_no_concloents`, `prova_no_fundador_insuficient`) i detall de la cerca. `tancament_nd` es deixa buit a Cellnex perquè la cerca és oberta | Lot de correcció 1 |
| `regles` | La regla que sosté el valor actual; `cap` a les ND (com Sopra Steria 2025) | Base |
| `fundador_transformador` (D37b) | 1 si el registre documenta que la persona no era a la fundació | Dassault (X01, X02), Merlin (L10-F01) |
| `d37_data_cita`, `d37_cita_contemporania` | Data de la primera cita D37 registrada; `si` si és ≤ 31/10/t, `no` si no | B&M, WPP |

## Criteris d'aplicació que ha fixat Claude (per revisar al PR)

- **Marca `D37`** a `marques` només on l'etiqueta passa a 1 per la D37 (C3, C4), com a B&M; als canvis de traçabilitat només canvia `regles` (com Cellnex al lot de correcció 1).
- **Telefónica 2016** porta `ceo_president_exec` per coherència (mateixa situació que el 2017-2025, C01); `founderceo_rob_sense_r3` no canvia (R1).
- **BME 2017-2018 i Telefónica:** `founderceo_rob_sense_r3` es queda a 0, perquè sense el president hi ha un consejero delegado per R1 (Hernani, Vilá) i tots dos són 0.
- **Ferrovial:** les marques `llista_exhaustiva=implicita` i `a_fundador_unic` acompanyen la prova a per P8 (decisió de Jordi del 24/11/2026, «Un sol fundador»). Els noms de `ceos` s'ordenen alfabèticament, com a la resta de files amb co-CEO.
- **Bridgepoint:** `fundacio_corporativa` i `origen_intern` són les marques que, a la base, porten els valors de robustesa que el PAQUET demana (0 i ND).
- **Reply `IT0005619678` 2024** (línia de drets) s'alinea amb `IT0005282865` 2024: té la seva pròpia entrada D37 (L7-F01, F02).
- **Balder:** `founderceo_rob_cita_contemporania` 1 → 0 perquè la frase del tancament del lot 19 ho diu sense condició; a Ocado, Teleperformance, Eurofins, SalMar i MorphoSys la frase és condicional («si no es troba una cita contemporània») i va a pendents.

## Condicions de registre abans d'aplicar

Són a `correccio2_pendents.csv` i no canvien cap valor d'aquest fitxer:
- **C3:** registrar `L7-FR0000130650-X03` com a `evidencia_fundador` D37, amb la frase del mateix comunicat que porta el nom complet de Bernard Charlès.
- **C4:** registrar `L7-GB00BND88V85-X01` com a `evidencia_fundador` D37, amb la data de l'RNS (06/06/2024) a la nota.
- **Q8:** registrar la frase literal de l'Annex III que anomena fundador Rafael del Pino y Moreno, i passar les entrades X del president a `evidencia_ceo` R1.
- **C2:** que el flux de Wayback verifiqui L3SS-17 a la captura.

## Què no entra en aquest lot

- **C1 (BME):** no s'aplica el canvi de CEO (regla única); només la marca.
- **Q1 (Standard Life Aberdeen), alstria (Q2), Q7 (ACS):** falten entrades o cerques al registre.
- **Columnes noves** (robustesa amb l'altra persona o sense presidents executius, sense gestió externa, sense títol funcional, dues fonts, `founderceo_rob_regla25_nd`, D1 àmplia): es creen per script, no en aquest lot.
- **Columnes que depenen d'un fet que no és al registre** (`a_recalcular`): escissió i fundació corporativa de Dassault Systèmes, `fundador_transformador` de Bridgepoint i Paysafe, `pre_d37` de Merlin i Paysafe, `founderceo_rob_sense_r3` de Mapfre, D37a d'Energean i dels tancaments condicionats.
- Detall i motiu de cada pendent: [`correccio2_pendents.csv`](correccio2_pendents.csv).

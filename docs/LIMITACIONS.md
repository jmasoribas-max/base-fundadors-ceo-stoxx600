# Limitacions v8 r3

Data: 19/11/2026 10:14 (CET, Europe/Madrid). Les xifres de FounderCEO, J14 i certificació són les mateixes que a la v8 r2 [V] (v8 r3 d'origen; després, el lot ND-1, fusionat a `main` el 19/11/2026 amb el PR #2, merge `edea674`, ha canviat els recomptes de FounderCEO: vegeu §2; el recàlcul DF del PR #4 actualitza la mostra J14 a n=5.962, F=342, P=5.620). El text de limitacions anterior es conserva més avall; s'hi afegeix l'extensió de sector.

## Sector ICB estès des de juny 2023 (v8 r3)

- S'ha estès el supersector del PDF de components de juny 2023 als anys 2024-2025 **només** per als 561 ISIN que ja tenien aquesta font (`any_font=2023`): 1.076 files, amb `sector_estes_des_2023=1` i `any_font=2023`. [V]
- **Supòsit, [NV]: no hi ha hagut cap reclassificació ICB entre el 2023 i el 2025.** No s'ha comprovat fila a fila si l'emissor ha canviat de supersector després del juny del 2023. Una robustesa que vulgui evitar aquest supòsit ha d'excloure les files amb `sector_estes_des_2023=1`. El sector fix per empresa, independent de l'extensió, és `supersector_fix`.
- No s'ha posat `any_font=2023` a 33 ISIN (52 files 2024-2025) que tenen un sector a la taula però no una font de juny 2023; queden `pendent_extensio_2024_2025` o `revisar_pendent_extensio_2024_2025`.
- 72 empreses (98 files) queden `sense_sector` i pendents per a Claude, amb una font A (per exemple un informe anual amb la classificació ICB): 48 només presents el 2024-2025 i 24 no casades als PDF 2015-2023 ([NV] ja a la font sectorial).
- 25 empreses casades per via indirecta queden `revisar` o `revisar_pendent_extensio_2024_2025`.

---

# Limitacions v8 r2

Data: 19/11/2026 09:48 (CET, Europe/Madrid). Les xifres de FounderCEO, J14 i certificació són les mateixes que a la v8 r1 [V]. El text de limitacions de la v8 r1 es conserva més avall; s'hi afegeix el sector.

## Sector ICB (addició v8 r2)

- El sector és **per ISIN**, no una sèrie anual observada cada any. La font pública de components amb supersector s'acaba el juny del 2023.
- **No s'ha estès** el sector de 2023 (ni de cap `any_font` ≤ 2023) als anys 2024-2025: 1.128 files queden amb `supersector` buit i estat `pendent_extensio_2024_2025` o `revisar_pendent_extensio_2024_2025`. L'extensió la decideix Doctorat. [V] com a decisió d'aquesta versió; el criteri d'extensió [NV].
- 72 empreses (98 files) queden `sense_sector` amb el motiu de la font: 48 perquè només tenen anys 2024-2025 sense PDF públic posterior a juny 2023; 24 perquè l'ISIN no s'ha trobat als PDF 2015-2023 (canvi d'ISIN o nom no casat) [NV] ja a la font sectorial.
- 25 empreses casades per via indirecta queden `revisar` (9 files amb sector aplicat) o `revisar_pendent_extensio_2024_2025` (33 files).
- `url_wayback_font` pot ser buida a la taula sectorial: aleshores el PDF de sector no es considera durable a efectes d'aquest camp.

La secció 8 de la v8 r1 parlava d'una mostra de 3 fitxes no publicada. En aquest repositori hi ha les **1.040 fitxes**, encara com a arbre local no pujat.

---

# Limitacions v8 r1

Data: 18/11/2026 20:56 (CET, Europe/Madrid). Aquest document recull les limitacions que cal tenir presents en usar la base v8. Les xifres són [V] (simulació v2 / QA v8).

## 1. Senyal `cas_especific` (prova exacta de Fisher)

Entre les files `completa` del paquet r4, ChatGPT tanca (proposta 0 o 1) les files amb marca `cas_especific` més que la resta:

- ChatGPT: OR = 5,11, p = 0,004 (taula: cas tanca 6 / no tanca 13; resta tanca 73 / no tanca 808). [V]
- Claude (proposta efectiva): OR = 0,72, p = 0,59 (no significativa). [V]

Aquest senyal **no afecta cap fila certificada N1/N2 ni cap canvi d'etiqueta**:

- Tancaments de ChatGPT a `cas_especific`: 6 (tots Orpea 2016-2021). [V]
- Files N1/N2 que baixen de nivell si aquests tancaments es tracten com a indeterminats: **0**. [V]
- Canvis d'etiqueta que depenen només d'aquests tancaments: **0**. [V]
- Orpea es certifica amb nivell `doctorat` per la cita verificada de Marian i la decisió de Doctorat (18:43), no pel tancament de ChatGPT.

La v8 no treu aquests tancaments de l'etiqueta ni de la certificació principal; només els documenta com a limitació i com a robustesa de certificació (`sim_estat_cert_rob_cas_esp`, `sim_nivell_rob_cas_esp`).

## 2. Les ND del panell (14 a la v8 r3; 6 després del lot ND-1)

> **Actualització (lot ND-1, fusionat a `main` el 19/11/2026 amb el PR #2, merge `edea674`):** 8 d'aquestes 14 files passen a P: B&M 2016-2021 (regla d) i Steinhoff 2016-2017 (regla b). En queden 6 ND, amb la cerca documentada a cada fitxa: Drillisch 2017, Sopra Steria 2025 i Aroundtown 2017-2020. Cotes amb les 6: si totes passessin a 0, F = 343 (5,73 % de F+P); si totes passessin a 1, F = 349 (5,84 %) [V]. El text i la taula que segueixen són de la v8 r3 d'origen.

El panell té 14 files `no_determinat`. Cotes: si totes passessin a 0, F = 343 (5,73 % de F+P); si totes passessin a 1, F = 357 (5,97 %). [V]

| ISIN | Empresa | Any | Motiu |
|---|---|---|---|
| `DE0005545503` | Drillisch AG Inhaber-Aktien o.N. | 2017 | predecessora_no_documentada_D37d |
| `FR0000050809` | Sopra Steria Group S.A. Actions Port. EO 1 | 2025 | proves_a_e_no_concloents |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2016 | ft_no_acreditat_sense_D37 |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2017 | ft_no_acreditat_sense_D37 |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2018 | ft_no_acreditat_sense_D37 |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2019 | ft_no_acreditat_sense_D37 |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2020 | ft_no_acreditat_sense_D37 |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2021 | ft_no_acreditat_sense_D37 |
| `LU1673108939` | Aroundtown SA Inhaber-Aktien EO -,01 | 2017 | proves_a_e_no_concloents |
| `LU1673108939` | Aroundtown SA Bearer Shares EO -,01 | 2018 | proves_a_e_no_concloents |
| `LU1673108939` | Aroundtown SA Bearer Shares EO -,01 | 2019 | proves_a_e_no_concloents |
| `LU1673108939` | Aroundtown SA Bearer Shares EO -,01 | 2020 | proves_a_e_no_concloents |
| `NL0011375019` | Steinhoff Internatl Hldgs N.V. Aandelen op | 2016 | fusio_D1_sense_prova_concloent |
| `NL0011375019` | Steinhoff Internatl Hldgs N.V. Aandelen op | 2017 | fusio_D1_sense_prova_concloent |

Steinhoff 2016-17 és l'única decisió 14:44 no aplicada (falta cita verificada de l'operació de 1998).

## 3. Casos clau no certificats

Queden a la mostra principal com a F, però **sense certificar** (decisió 10 de Doctorat):

- **LVMH** (`FR0000121014`), anys 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025: etiqueta F, estat no_certificada. Doctorat 10: LVMH es queda F a la mostra principal, sense certificar; cas clau per al tribunal. | LVMH no esta marcada fundador_transformador=1 a la v75r2; la columna founderceo_rob_sense_fundador_transformador ja el deixa com a F. No s'ha alterat.
- **BE Semiconductor** (`NL0012866412`), anys 2020, 2021, 2022, 2023, 2024, 2025: etiqueta F, estat no_certificada. Doctorat 10: BE Semiconductor es queda F a la mostra principal, sense certificar; cas clau.
- **Aberdeen 2016** (`GB0000031285`), anys 2016: etiqueta F, estat no_certificada. Doctorat 10: Aberdeen 2016 es queda F a la mostra principal, sense certificar; cas clau.

## 4. ChatGPT conservador en la verificació web

De les 2,481 evidències web declarades per ChatGPT, **946** s'han trobat literalment (`cita_trobada=literal`, `estat=verificada`). [V] La resta no s'ha pogut confirmar literalment (cita no trobada 1376, pendent d'una verificació externa 141, error 18). La simulació només compta una cita web si l'script la troba literalment.

## 5. Cobertura de la certificació

La certificació (N1, N2, doctorat, ceo_pendent o no_certificada) cobreix les **2.122 files** de l'auditoria r3e, d'un panell de **6.012**. Les altres 3.890 files del panell queden `fora_mostra_auditoria`. [V]

Comptes de certificació al panell (coincidents amb la v2): N1 740, N2 1.018, doctorat 15 (total certificades 1.773); ceo_pendent 108; no_certificada 241.

## 6. Conflicte de fonts a Enagás 2016-2021

**Resultat [V]: conflicte de fonts.** La cita literal de ChatGPT (manifest r4, `estat=verificada`, `cita_trobada=literal`) diu: «Mr. Antonio Llardén Carratalá was Chief Executive Officer of Enagás from 2007 to 2022.» Afirma que Llardén va ser *Chief Executive Officer* (CEO) de 2007 a 2022, període que inclou 2016-2021. No diu «consejero delegado» en aquesta frase, però sí «Chief Executive Officer», que la instrucció de Doctorat equipara a CEO. El mateix document, tot seguit, diu: «Mr. Llardén has been a non-executive Chairman of the Company since 2022» i situa Arturo Gonzalo Aizpiri com a Chief Executive Officer des del febrer del 2022. Això no treu el conflicte: la frase sobre 2007-2022 diu CEO. Claude té cites literals que identifiquen Marcelino Oreja Arburúa com a Consejero Delegado (nomenament el 2012 i càrrec exercit des del 2012) en el mateix període 2016-2021, i la R1 pren el consejero delegado com a CEO. Per tant, les files 2016-2021 es **mantenen sense certificar**. El canvi de CEO aplicat (Oreja) i l'etiqueta P no es toquen; només s'anota el conflicte. L'URL de la cita de ChatGPT apunta a un informe de reelecció / nomenaments de 2026 (document posterior als anys classificats). La baixada r4 és de la URL oficial; no consta Wayback d'aquesta baixada [NV].

## 7. Columnes de robustesa (recalculades a la r1; la v8 les tenia heretades)

`founderceo_rob_r3_president_exec_com_1` i `founderceo_rob_sense_fundador_transformador` (i la còpia `sense_fundador_transformador`) provenen de la v75r2 i **no s'han tornat a calcular** després dels 35 canvis d'etiqueta. En particular, 26 files que passen de ND a P tenen encara `no_determinat` a `sense_fundador_transformador`. No s'ha inventat cap recàlcul: faltenia la fórmula completa reaplicada a l'etiqueta nova, i s'ha preferit heretar el valor verificat i documentar-ho. [V] com a herència; [NV] com a robustesa actualitzada a la v8.

La columna `sense_fundador_transformador` no existia amb aquest nom. S'ha omplert copiant `founderceo_rob_sense_fundador_transformador` (dades verificables ja presents). No és una variable nova independent.

Sí que estan recalculades a la v2/v8: `FounderCEO`, `a_mostra_principal` (J14), `a_mostra_nomes_certificades` i `founderceo_rob_sense_decisions_doctorat`.

## 8. Mostra de fitxes i publicació

La mostra de 3 fitxes i la proposta d'estructura GitHub són un format per a revisió de Jordi. **No s'ha publicat res.** La mostra no cobreix les 6.012 files ni totes les empreses.

## 9. Altres

- La base oficial v8 té 6.012 files del panell. Les 586 files de 2015 (`fora_panel=1`) queden fora d'aquest fitxer; continuen a la v75r2 i a la simulació v2.
- Orpea 2018 conserva un typo al `nom_panell` («1,252)»); no s'ha maquillat.
- La v8 no substitueix la v75r2 com a base vigent fins que Jordi i Doctorat ho decideixin expressament.


## Addenda v8 r1 (19/11/2026 09:31 (CET, Europe/Madrid))

La limitació de la v8 sobre r3 / sense_fundador_transformador «no recalculades» queda resolta a la r1 (fórmules v71/v2, 35 canvis d'etiqueta aplicats, 0 files [NV]). `sense_decisions_doctorat` no canvia. Els fitxers v8 es conserven com a testimoni de l'estat anterior.

Wayback: de les 30 cites que a la v8 no tenien captura, 6 queden `pendent_verificacio_externa` (Mandatum CV i 4 PDF emeis.com) després d'un SPN públic no confirmat amb snapshot descarregable. Bellway 2018 té captura existent però truncada a 1 MiB; la cita no s'ha pogut verificar. No s'ha fet servir cap clau IA_S3, ni `-k`, ni archive.today.

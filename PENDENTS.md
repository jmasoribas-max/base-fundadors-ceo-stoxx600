# Pendents (feina per a Claude Code)

Data: 19/11/2026 10:13 (CET, Europe/Madrid). Extret de `dades/base_isin_any_v8r3.csv`, `docs/REGISTRE_CANVIS.csv` i `dades/sector_icb_v8r3.csv` [V]. No s'hi inventa cap cas. El que no s'ha trobat nominativament als fitxers es marca [NV].

Claude treballa per lots d'empreses **en una branca**, amb cita literal, URL i Wayback a la fitxa i al registre, passa `scripts/valida_pr.py` i obre un PR per lot. **No toca `main`, `scripts/`, `docs/METODOLOGIA.md`, `CLAUDE.md`, les regles ni `.github/`, i no fusiona.** DF valida, Doctorat revisa la metodologia, Jordi aprova.

## Ordre de treball

Segueix aquest ordre, tret que Jordi o un PR ja obert indiquin una altra cosa:

1. **Casos oberts.** Busca fins que trobis la font A/B. Si després d'una cerca exhaustiva i documentada no n'hi ha cap, la fila queda indeterminada i a la fitxa s'explica què s'ha buscat i on. Cap límit d'intents.
   - Les 14 files ND (lot ND-1, fusionat a `main` el 19/11/2026 amb el PR #2, merge `edea674`: 8 passen a P i en queden 6 ND, amb la cerca documentada a la fitxa).
   - Les 108 files `ceo_pendent`, després les 241 `no_certificada` (349 en total).
   - Casos clau: LVMH, BE Semiconductor, Aberdeen 2016, i Anders Dam (Jyske Bank; vegeu la tasca específica més avall).
2. **Les 3890 files sense auditar** (`fora_mostra_auditoria`; recompte comprovat a la base v8 r3: **3890** [V]). Verifica el CEO i l'etiqueta empresa per empresa i afegeix les cites que faltin.
3. **Fitxes completes:** el CEO de cada any amb cita, la prova de fundador o de no fundador, el sector i les fonts amb Wayback.
4. **Errors:** si una dada contradiu la base, encara que estigui certificada, proposa'n la correcció amb la cita.

Tasques complementàries (no alteren l'ordre anterior, es poden encaixar en el lot de l'empresa corresponent):

- **Schulenberg / CTS Eventim:** tasca de forma (vegeu més avall). L'etiqueta no canvia.
- **Sector pendent per a Claude:** les 48 empreses només presents el 2024-2025 i les 24 no casades (font A, per exemple un informe anual amb la classificació ICB). Les 25 de via indirecta queden a `revisar`. Les 33 ISIN amb sector d'una font anterior a juny 2023 no s'han estès.
- Les 6 cites amb Wayback `pendent_verificacio_externa`.
- Les 13 parelles sense documents ([NV] la llista; si no apareix, es regenerarà per script) i les 15 files / 7 ISIN amb E4.

L'extensió del supersector del juny 2023 als anys 2024-2025 ja està aplicada a la v8 r3 per als 561 ISIN que tenien aquesta font. No s'estén cap sector que no tingui aquesta font.

## 1. Casos oberts

### 1.1 Casos clau (inclosos a `no_certificada`, tret d'Anders Dam)

> **Estat (lot 3, 19/11/2026, revisat el 20/11/2026 amb els criteris aprovats per Jordi; proposta pendent del flux DF → Doctorat → Jordi):** LVMH: 10 indeterminades; Aberdeen 2016: 1 confirmada; BE Semiconductor: 6 confirmades. Detall i dubtes a les fitxes, a `docs/REGISTRE_CANVIS.md` (secció «Lot 3») i al PR.

| ISIN | Empresa | Anys | FounderCEO | Estat | Cas | Fitxa |
|---|---|---|---|---|---|---|
| `FR0000121014` | LVMH Moët Henn. L. Vuitton SE Actions Port. | 2016–2025 | F | no_certificada | LVMH_Arnault | [fitxa](empreses/FR0000121014.md) |
| `GB0000031285` | Aberdeen Asset Management PLC Registered | 2016–2016 | F | no_certificada | Aberdeen_Gilbert_2016 | [fitxa](empreses/GB0000031285.md) |
| `NL0012866412` | BE Semiconductor Inds N.V. Aandelen op | 2020–2025 | F | no_certificada | BE_Semiconductor_Blickman | [fitxa](empreses/NL0012866412.md) |

### 1.2 Anders Dam / Jyske Bank (`DK0010307958`) — cas obert

Fitxa: [empreses/DK0010307958.md](empreses/DK0010307958.md).

> **Estat (lot 3, 19/11/2026, revisat el 20/11/2026 amb els criteris aprovats per Jordi; proposta pendent del flux DF → Doctorat → Jordi):** 7 confirmades. Detall, cites i dubtes a la fitxa i a `docs/REGISTRE_CANVIS.md`, secció «Lot 3».

A la base, Anders Dam és CEO els anys 2016-2018 i 2022-2023, FounderCEO=`0`, regla `d`, estat `fora_mostra_auditoria`. [V] Claude ha de buscar una font A/B que sustentil la prova **d** (incorporació tardana) i documentar que les fusions posteriors al 1967 són adquisicions (no una fundació nova ni una fusió entre iguals que reobri la data de fundació rellevant).

| Any | CEO | FounderCEO | Regla | Certificació | Fitxa |
|---|---|---|---|---|---|
| 2016 | Anders Dam | P | d | fora_mostra_auditoria | [fitxa](empreses/DK0010307958.md) |
| 2017 | Anders Dam | P | d | fora_mostra_auditoria | [fitxa](empreses/DK0010307958.md) |
| 2018 | Anders Dam | P | d | fora_mostra_auditoria | [fitxa](empreses/DK0010307958.md) |
| 2022 | Anders Dam | P | d | fora_mostra_auditoria | [fitxa](empreses/DK0010307958.md) |
| 2023 | Anders Dam | P | d | fora_mostra_auditoria | [fitxa](empreses/DK0010307958.md) |
| 2024 | Lars Mørch | P | d | fora_mostra_auditoria | [fitxa](empreses/DK0010307958.md) |
| 2025 | Lars Mørch | P | d | fora_mostra_auditoria | [fitxa](empreses/DK0010307958.md) |

### 1.3 Files ND del panell (14 a la v8 r3; 6 després del lot ND-1)

> **Estat (PR #6 fusionat a `main` el 20/11/2026, merge `5b21049`; ajustos de DF a la branca `df/ajustos-pr6`, pendents de Doctorat i Jordi):** queda **1 ND**: Sopra Steria 2025 (`FR0000050809`), amb `dubte_D1`; les proves b i d no tanquen contra Sopra (1968) i cal una biografia A/B de Xavier Pecquet amb l'any d'entrada o un ocupador anterior. Aroundtown 2017-2020 i Drillisch 2017 són P (decisió de Jordi del 20/11/2026 14:25) i entren a la mostra J14. Pendents de DF: la passada de la regla 25 a tota la base (robustesa `founderceo_rob_regla25_nd` i les específiques, que encara no existeixen com a columnes) i la cita de classificació d'ITV 2017 (`font_classificacio_*`).

> **Estat (lot 3, 19/11/2026, revisat el 20/11/2026 amb els criteris aprovats per Jordi; branca `cas/no-certificada-lot3`, proposta pendent del flux DF → Doctorat → Jordi):** canvis de `FounderCEO` aplicats amb cita A/B: `DE0005545503` 2017 ND → P; `LU1673108939` 2017-2020 ND → P. Sopra Steria 2025 continua ND, amb una proposta ND → 0 no aplicada (depèn de la «D1 estricta»). B&M 2016-2021 passa de 0 a 1 per D37. Detall a `docs/REGISTRE_CANVIS.md`, secció «Lot 3», i a les fitxes.

> **Estat (lot ND-1, fusionat a `main` el 19/11/2026 amb el PR #2, merge `edea674`):** treballades les 14 files. B&M 2016-2021 (regla d) i Steinhoff 2016-2017 (regla b) passen de ND a P (`FounderCEO=0`), amb cita literal A/B. Es mantenen ND, amb la cerca documentada a la fitxa, Drillisch 2017, Sopra Steria 2025 i Aroundtown 2017-2020. Correccions de DF (19/11/2026) aplicades al PR #2: a la base només va canviar `FounderCEO`; Steinhoff per regla b amb el naixement i la fundació de 1963 (l'operació de 1998 no és fundació nova; còpia d'agbiz marcada `font_copia_no_original`); recerca addicional d'Aroundtown (naixement de Mayo, co-CEO del 2020) i de Drillisch (operació d'octubre de 1998), que es mantenen ND. Detall a `docs/REGISTRE_CANVIS.md`, secció «Lot ND-1». **Recàlcul DF (PR #4, branca `df/robustesa-nd-lot1`):** a les 8 files s'han recalculat les columnes derivades (robusteses v8r1, `a_mostra_principal` / mostra J14 n=5.962, F=342, P=5.620, marques `sim_*` i `fundacio_alternativa_1998` a Steinhoff) i s'ha alineat l'`.xlsx`. SHA del CSV `bb9cb759471ef8aa1d912b907ad8213a906405419ae54379e700ef3c46572735` [V]; SHA de l'xlsx `7000e7bce0dcd54e2eac542158148516de852834c965f7b14ed644f49b4ccd5c` [V]. `regles` i `motiu_nd` es queden com a les altres files ND→P de Doctorat. La certificació no ha canviat (`sim_estat_certificacio=no_certificada`). La taula següent és l'estat d'origen (v8 r3) i no s'ha reescrit.

| ISIN | Empresa | Any | Motiu | Detall | Fitxa |
|---|---|---|---|---|---|
| `DE0005545503` | Drillisch AG Inhaber-Aktien o.N. | 2017 | predecessora_no_documentada_D37d | CV de 1&1: Founded E.I.C. GmbH, integrated in the Drillisch-Group in 1998. D37d exigeix predecessora juridica o economica documentada; la integracio 1998 no esta descrita com fusio. Recomanacio ND; seria 1 si Jordi considera EIC predecessora. | [fitxa](empreses/DE0005545503.md) |
| `FR0000050809` | Sopra Steria Group S.A. Actions Port. EO 1 | 2025 | proves_a_e_no_concloents | Naixement 1950; Sopra 1968 i Steria 1969; b no; sense d. | [fitxa](empreses/FR0000050809.md) |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2016 | ft_no_acreditat_sense_D37 | Sense FT (decisio Jordi 14/11/2026 18:33) i sense cita D37 (X10 T1); es mante no_determinat | [fitxa](empreses/LU1072616219.md) |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2017 | ft_no_acreditat_sense_D37 | Sense FT (decisio Jordi 14/11/2026 18:33) i sense cita D37 (X10 T1); es mante no_determinat | [fitxa](empreses/LU1072616219.md) |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2018 | ft_no_acreditat_sense_D37 | Sense FT (decisio Jordi 14/11/2026 18:33) i sense cita D37 (X10 T1); es mante no_determinat | [fitxa](empreses/LU1072616219.md) |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2019 | ft_no_acreditat_sense_D37 | Sense FT (decisio Jordi 14/11/2026 18:33) i sense cita D37 (X10 T1); es mante no_determinat | [fitxa](empreses/LU1072616219.md) |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2020 | ft_no_acreditat_sense_D37 | Sense FT (decisio Jordi 14/11/2026 18:33) i sense cita D37 (X10 T1); es mante no_determinat | [fitxa](empreses/LU1072616219.md) |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2021 | ft_no_acreditat_sense_D37 | Sense FT (decisio Jordi 14/11/2026 18:33) i sense cita D37 (X10 T1); es mante no_determinat | [fitxa](empreses/LU1072616219.md) |
| `LU1673108939` | Aroundtown SA Inhaber-Aktien EO -,01 | 2017 | proves_a_e_no_concloents | Incorporacio 2006 i fundacio rellevant 2004/2007: d no es compleix. | [fitxa](empreses/LU1673108939.md) |
| `LU1673108939` | Aroundtown SA Bearer Shares EO -,01 | 2018 | proves_a_e_no_concloents | Incorporacio 2006 i fundacio rellevant 2004/2007: d no es compleix. | [fitxa](empreses/LU1673108939.md) |
| `LU1673108939` | Aroundtown SA Bearer Shares EO -,01 | 2019 | proves_a_e_no_concloents | Incorporacio 2006 i fundacio rellevant 2004/2007: d no es compleix. | [fitxa](empreses/LU1673108939.md) |
| `LU1673108939` | Aroundtown SA Bearer Shares EO -,01 | 2020 | proves_a_e_no_concloents | Incorporacio 2006 i fundacio rellevant 2004/2007: d no es compleix. | [fitxa](empreses/LU1673108939.md) |
| `NL0011375019` | Steinhoff Internatl Hldgs N.V. Aandelen op | 2016 | fusio_D1_sense_prova_concloent | Sense ocupador anterior ni any de fundacio suficient (Markus Jooste entra a Gommagomma el 1988; Steinhoff 1964). Estructura: D1 no decidida a l'X11; fusio o JV original amb Bruno Steinhoff sense any exacte ni percentatges; any de fundacio de Gommagomma i de constitucio de la NV pendents. | [fitxa](empreses/NL0011375019.md) |
| `NL0011375019` | Steinhoff Internatl Hldgs N.V. Aandelen op | 2017 | fusio_D1_sense_prova_concloent | Sense ocupador anterior ni any de fundacio suficient (Markus Jooste entra a Gommagomma el 1988; Steinhoff 1964). Estructura: D1 no decidida a l'X11; fusio o JV original amb Bruno Steinhoff sense any exacte ni percentatges; any de fundacio de Gommagomma i de constitucio de la NV pendents. | [fitxa](empreses/NL0011375019.md) |

### 1.4 Files `ceo_pendent` (108) i `no_certificada` (241)

#### Motius `ceo_pendent` (`sim_cert_detall`)

| Motiu | Files |
|---|---:|
| r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | 41 |
| r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | 14 |
| r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | 11 |
| r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | 10 |
| r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | 10 |
| r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | 9 |
| Doctorat (previa): ND->0, regla a; els dos models r3e deien 0 amb cita verificada. CEO a 31/10 continua NV (no era al paquet r4). | 6 |
| N2 r4 d'etiqueta (P, Claude tanca, ChatGPT indeterminat), pero CEO [NV] als dos models. | 4 |
| r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=NV (o la cita del CEO no esta verificada) | 3 |

#### Motius `no_certificada`

| Motiu | Files |
|---|---:|
| continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | 183 |
| l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | 17 |
| incidencia greu r3e (E6): no puja a N1/N2 | 17 |
| incidencia greu r3e (E4): no puja a N1/N2 | 13 |
| Doctorat 8: etiqueta 0 per Oreja, pero r3e te incidencia greu E2 i nomes un model s'hi pronuncia. No es certifica. | 6 |
| continua sense certificar (ChatGPT: indeterminat, Claude efectiu: 0) | 2 |
| Doctorat tanca l'etiqueta, pero r3e tenia incidences greus (E4,E6); no puja a N1/N2 | 1 |
| Doctorat tanca l'etiqueta, pero r3e tenia incidences greus (E4); no puja a N1/N2 | 1 |
| Doctorat 9 aplicada (Ayres, FounderCEO=0), pero nomes Claude s'hi pronuncia. No es certifica. El canvi va al registre. | 1 |

#### Llista `ceo_pendent`

> **Estat (19/11/2026, lot 2, branca `cas/ceo-pendent-lot2`, versió corregida segons DF; proposta pendent del flux DF → Doctorat → Jordi):** treballades les 108 files. S'hi incorporen 324 cites literals A/B obertes a la URL original, de les quals **207 són cites del CEO** (nom i càrrec dins el fragment); 56 són de datació i 61 de context i no compten com a cita del CEO. Totes les files tenen almenys una cita del CEO (4 només de nivell B: Tesco 2016-2018 i BBA Aviation 2017). Marques: `informe_exercici` 62, `prova_interval` 37, `prova_interval+prova_interval_retrospectiva` 8, `informe_exercici+ceo_titol_amb_president_executiu` 1. El CEO de la base queda confirmat a les 108 i no es canvia cap dada ni cap columna de certificació o de robustesa. Les files continuen `certificada_ceo_pendent` fins que el flux validi les cites. Cites a cada fitxa i a `docs/REGISTRE_CANVIS.md`, secció «Lot 2»; els dubtes de metodologia (prova per interval, documents de l'emissor fora del seu domini, premsa sectorial, estructura amb president executiu de Bankia, lligam de Saynor amb Sandoz Group AG) són al PR per a Doctorat. La taula següent és l'estat d'origen (v8 r3) i no s'ha reescrit.

| ISIN | Empresa | Any | Nivell | Motiu | Fitxa |
|---|---|---|---|---|---|
| `BE0974259880` | D'Ieteren Group S.A. Parts Sociales au Port. | 2022 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/BE0974259880.md) |
| `CH0008837566` | Allreal Holdings AG Namens-Aktien SF 1,00 | 2019 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/CH0008837566.md) |
| `CH0008837566` | Allreal Holdings AG Namens-Aktien SF 1,00 | 2020 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/CH0008837566.md) |
| `CH0008837566` | Allreal Holdings AG Namens-Aktien SF 1,00 | 2021 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/CH0008837566.md) |
| `CH0008837566` | Allreal Holdings AG Namens-Aktien SF 1,00 | 2022 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/CH0008837566.md) |
| `CH1243598427` | Sandoz Group AG Namens-Aktien SF -,05 | 2023 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/CH1243598427.md) |
| `CH1243598427` | Sandoz Group AG Namens-Aktien SF -,05 | 2024 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/CH1243598427.md) |
| `CH1243598427` | Sandoz Group AG Namens-Aktien SF -,05 | 2025 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/CH1243598427.md) |
| `DE0007100000` | Daimler AG Namens-Aktien o.N. | 2019 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DE0007100000.md) |
| `DE0007100000` | Daimler AG Namens-Aktien o.N. | 2020 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DE0007100000.md) |
| `DE0007100000` | Daimler AG Namens-Aktien o.N. | 2021 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DE0007100000.md) |
| `DE0007100000` | Mercedes-Benz Group AG Namens-Aktien | 2022 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DE0007100000.md) |
| `DE0007100000` | Mercedes-Benz Group AG Namens-Aktien | 2023 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DE0007100000.md) |
| `DE0007100000` | Mercedes-Benz Group AG Namens-Aktien | 2024 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DE0007100000.md) |
| `DE0007100000` | Mercedes-Benz Group AG Namens-Aktien | 2025 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DE0007100000.md) |
| `DE000A2E4K43` | Delivery Hero SE Namens-Aktien o.N. | 2018 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/DE000A2E4K43.md) |
| `DE000A2E4K43` | Delivery Hero SE Namens-Aktien o.N. | 2019 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/DE000A2E4K43.md) |
| `DE000A2E4K43` | Delivery Hero SE Namens-Aktien o.N. | 2020 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/DE000A2E4K43.md) |
| `DE000A2E4K43` | Delivery Hero SE Namens-Aktien o.N. | 2021 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/DE000A2E4K43.md) |
| `DE000A2E4K43` | Delivery Hero SE Namens-Aktien o.N. | 2022 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/DE000A2E4K43.md) |
| `DE000A2E4K43` | Delivery Hero SE Namens-Aktien o.N. | 2023 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/DE000A2E4K43.md) |
| `DE000A2E4K43` | Delivery Hero SE Namens-Aktien o.N. | 2024 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/DE000A2E4K43.md) |
| `DE000A2E4K43` | Delivery Hero SE Namens-Aktien o.N. | 2025 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/DE000A2E4K43.md) |
| `DE000LED4000` | OSRAM Licht AG Namens-Aktien o.N. | 2016 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/DE000LED4000.md) |
| `DE000LED4000` | OSRAM Licht AG Namens-Aktien o.N. | 2017 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/DE000LED4000.md) |
| `DE000LED4000` | OSRAM Licht AG Namens-Aktien o.N. | 2018 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/DE000LED4000.md) |
| `DE000LED4000` | OSRAM Licht AG Namens-Aktien o.N.2) | 2019 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/DE000LED4000.md) |
| `DK0010181759` | Carlsberg AS Navne-Aktier B DK 20 | 2016 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DK0010181759.md) |
| `DK0010181759` | Carlsberg AS Navne-Aktier B DK 20 | 2017 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DK0010181759.md) |
| `DK0010181759` | Carlsberg AS Navne-Aktier B DK 20 | 2018 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DK0010181759.md) |
| `DK0010181759` | Carlsberg AS Navne-Aktier B DK 20 | 2019 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DK0010181759.md) |
| `DK0010181759` | Carlsberg AS Navne-Aktier B DK 20 | 2020 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DK0010181759.md) |
| `DK0010181759` | Carlsberg AS Navne-Aktier B DK 20 | 2021 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DK0010181759.md) |
| `DK0010181759` | Carlsberg AS Navne-Aktier B DK 20 | 2022 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/DK0010181759.md) |
| `DK0060227585` | Christian Hansen Holding AS Navne-Aktier | 2016 | N2 | N2 r4 d'etiqueta (P, Claude tanca, ChatGPT indeterminat), pero CEO [NV] als dos models. | [fitxa](empreses/DK0060227585.md) |
| `DK0060227585` | Christian Hansen Holding AS Navne-Aktier | 2017 | N2 | N2 r4 d'etiqueta (P, Claude tanca, ChatGPT indeterminat), pero CEO [NV] als dos models. | [fitxa](empreses/DK0060227585.md) |
| `ES0113307021` | BANKIA S.A. Acciones Nominativas EO 0,8 | 2016 | N2 | N2 r4 d'etiqueta (P, Claude tanca, ChatGPT indeterminat), pero CEO [NV] als dos models. | [fitxa](empreses/ES0113307021.md) |
| `FR0000071946` | Alten S.A. Actions au Porteur o.N. | 2018 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/FR0000071946.md) |
| `FR0000071946` | Alten S.A. Actions au Porteur EO 1,05 | 2019 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/FR0000071946.md) |
| `FR0000071946` | Alten S.A. Actions au Porteur EO 1,05 | 2020 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/FR0000071946.md) |
| `FR0000071946` | Alten S.A. Actions au Porteur EO 1,05 | 2021 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/FR0000071946.md) |
| `FR0000071946` | Alten S.A. Actions au Porteur EO 1,05 | 2022 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/FR0000071946.md) |
| `FR0000071946` | Alten S.A. Actions au Porteur EO 1,05 | 2023 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/FR0000071946.md) |
| `FR0000071946` | Alten S.A. Actions au Porteur EO 1,05 | 2024 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/FR0000071946.md) |
| `FR0000121667` | Essilor Intl -Cie Génle Opt.SA Actions Port. | 2016 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/FR0000121667.md) |
| `FR0000121667` | Essilor Intl -Cie Génle Opt.SA Actions Port. | 2017 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/FR0000121667.md) |
| `GB0006731235` | Associated British Foods PLC Registered | 2016 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0006731235.md) |
| `GB0006731235` | Associated British Foods PLC Registered | 2017 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0006731235.md) |
| `GB0006731235` | Associated British Foods PLC Registered | 2018 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0006731235.md) |
| `GB0006731235` | Associated British Foods PLC Registered | 2019 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0006731235.md) |
| `GB0006731235` | Associated British Foods PLC Registered | 2020 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0006731235.md) |
| `GB0006731235` | Associated British Foods PLC Registered | 2021 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0006731235.md) |
| `GB0006731235` | Associated British Foods PLC Registered | 2022 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0006731235.md) |
| `GB0006731235` | Associated British Foods PLC Registered | 2023 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0006731235.md) |
| `GB0006731235` | Associated British Foods PLC Registered | 2024 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0006731235.md) |
| `GB0006731235` | Associated British Foods PLC Registered | 2025 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0006731235.md) |
| `GB0008847096` | Tesco PLC Registered Shares LS -,05 | 2016 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0008847096.md) |
| `GB0008847096` | Tesco PLC Registered Shares LS -,05 | 2017 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0008847096.md) |
| `GB0008847096` | Tesco PLC Registered Shares LS -,05 | 2018 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0008847096.md) |
| `GB0009292243` | Victrex PLC Registered Shares LS -,01 | 2018 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0009292243.md) |
| `GB0009292243` | Victrex PLC Registered Shares LS -,01 | 2019 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0009292243.md) |
| `GB0009292243` | Victrex PLC Registered Shares LS -,01 | 2020 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0009292243.md) |
| `GB0009292243` | Victrex PLC Registered Shares LS -,01 | 2021 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0009292243.md) |
| `GB0009292243` | Victrex PLC Registered Shares LS -,01 | 2022 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0009292243.md) |
| `GB0009633180` | Dechra Pharmaceuticals PLC Registered | 2018 | N1 | Doctorat (previa): ND->0, regla a; els dos models r3e deien 0 amb cita verificada. CEO a 31/10 continua NV (no era al paquet r4). | [fitxa](empreses/GB0009633180.md) |
| `GB0009633180` | Dechra Pharmaceuticals PLC Registered | 2019 | N1 | Doctorat (previa): ND->0, regla a; els dos models r3e deien 0 amb cita verificada. CEO a 31/10 continua NV (no era al paquet r4). | [fitxa](empreses/GB0009633180.md) |
| `GB0009633180` | Dechra Pharmaceuticals PLC Registered | 2020 | N1 | Doctorat (previa): ND->0, regla a; els dos models r3e deien 0 amb cita verificada. CEO a 31/10 continua NV (no era al paquet r4). | [fitxa](empreses/GB0009633180.md) |
| `GB0009633180` | Dechra Pharmaceuticals PLC Registered | 2021 | N1 | Doctorat (previa): ND->0, regla a; els dos models r3e deien 0 amb cita verificada. CEO a 31/10 continua NV (no era al paquet r4). | [fitxa](empreses/GB0009633180.md) |
| `GB0009633180` | Dechra Pharmaceuticals PLC Registered | 2022 | N1 | Doctorat (previa): ND->0, regla a; els dos models r3e deien 0 amb cita verificada. CEO a 31/10 continua NV (no era al paquet r4). | [fitxa](empreses/GB0009633180.md) |
| `GB0009633180` | Dechra Pharmaceuticals PLC Registered | 2023 | N1 | Doctorat (previa): ND->0, regla a; els dos models r3e deien 0 amb cita verificada. CEO a 31/10 continua NV (no era al paquet r4). | [fitxa](empreses/GB0009633180.md) |
| `GB0034264548` | Paysafe Group PLC Registered Shares LS | 2016 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0034264548.md) |
| `GB0034264548` | Paysafe Group PLC Registered Shares LS | 2017 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/GB0034264548.md) |
| `GB00B17BBQ50` | Investec PLC Registered Shares LS -,00022) | 2016 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B17BBQ50.md) |
| `GB00B17BBQ50` | Investec PLC Registered Shares LS -,00022) | 2017 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B17BBQ50.md) |
| `GB00B1FP8915` | BBA Aviation PLC Registered Shares LS | 2017 | N2 | N2 r4 d'etiqueta (P, Claude tanca, ChatGPT indeterminat), pero CEO [NV] als dos models. | [fitxa](empreses/GB00B1FP8915.md) |
| `GB00B1KJJ408` | Whitbread PLC Reg. Shares LS -,76797385 | 2016 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B1KJJ408.md) |
| `GB00B1KJJ408` | Whitbread PLC Reg. Shares LS -,76797385 | 2017 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B1KJJ408.md) |
| `GB00B1KJJ408` | Whitbread PLC Reg. Shares LS -,76797385 | 2018 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B1KJJ408.md) |
| `GB00B1KJJ408` | Whitbread PLC Reg. Shares LS -,76797385 | 2019 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B1KJJ408.md) |
| `GB00B1KJJ408` | Whitbread PLC Reg. Shares LS -,76797385 | 2020 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B1KJJ408.md) |
| `GB00B1KJJ408` | Whitbread PLC Reg. Shares LS -,76797385 | 2022 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B1KJJ408.md) |
| `GB00B2B0DG97` | Relx PLC Registered Shares LS -,144397 | 2016 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B2B0DG97.md) |
| `GB00B2B0DG97` | Relx PLC Registered Shares LS -,144397 | 2017 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B2B0DG97.md) |
| `GB00B2B0DG97` | Relx PLC Registered Shares LS -,144397 | 2018 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B2B0DG97.md) |
| `GB00B2B0DG97` | Relx PLC Registered Shares LS -,144397 | 2019 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B2B0DG97.md) |
| `GB00B2B0DG97` | Relx PLC Registered Shares LS -,144397 | 2020 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B2B0DG97.md) |
| `GB00B2B0DG97` | Relx PLC Registered Shares LS -,144397 | 2021 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B2B0DG97.md) |
| `GB00B2B0DG97` | Relx PLC Registered Shares LS -,144397 | 2022 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B2B0DG97.md) |
| `GB00B2B0DG97` | Relx PLC Registered Shares LS -,144397 | 2023 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B2B0DG97.md) |
| `GB00B2B0DG97` | Relx PLC Registered Shares LS -,144397 | 2024 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B2B0DG97.md) |
| `GB00B2B0DG97` | Relx PLC Registered Shares LS -,144397 | 2025 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B2B0DG97.md) |
| `GB00B71N6K86` | Evraz PLC Registered Shares DL 0,05 | 2018 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B71N6K86.md) |
| `GB00B71N6K86` | Evraz PLC Registered Shares DL 0,05 | 2019 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B71N6K86.md) |
| `GB00B71N6K86` | Evraz PLC Registered Shares DL 0,05 | 2020 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B71N6K86.md) |
| `GB00B7T77214` | NatWest Group PLC Registered Shares LS 1 | 2020 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B7T77214.md) |
| `GB00B7T77214` | NatWest Group PLC Registered Shares LS 1 | 2021 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00B7T77214.md) |
| `GB00BGXQNP29` | Phoenix Group Holdings PLC Registered | 2020 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00BGXQNP29.md) |
| `GB00BGXQNP29` | Phoenix Group Holdings PLC Registered | 2021 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00BGXQNP29.md) |
| `GB00BGXQNP29` | Phoenix Group Holdings PLC Registered | 2022 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00BGXQNP29.md) |
| `GB00BGXQNP29` | Phoenix Group Holdings PLC Registered | 2023 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00BGXQNP29.md) |
| `GB00BGXQNP29` | Phoenix Group Holdings PLC Registered | 2024 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00BGXQNP29.md) |
| `GB00BGXQNP29` | Phoenix Group Holdings PLC Registered | 2025 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00BGXQNP29.md) |
| `GB00BNC5T391` | Deliveroo PLC Registered Shares | 2021 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/GB00BNC5T391.md) |
| `JE00B8KF9B49` | WPP PLC Registered Shares LS -,10 | 2025 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/JE00B8KF9B49.md) |
| `NL0011821392` | Signify N.V. Registered Shares EO -,01 | 2022 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/NL0011821392.md) |
| `SE0000108656` | Ericsson Namn-Aktier B (fria) o.N. | 2016 | N2 | r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=si / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/SE0000108656.md) |
| `SE0000869646` | Boliden AB Namn-Aktier SK 2 | 2016 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/SE0000869646.md) |
| `SE0000869646` | Boliden AB Namn-Aktier SK 2 | 2017 | N1 | r3e certificada_ceo_pendent N1; CEO a 31/10 continua ChatGPT=NV / Claude=si (o la cita del CEO no esta verificada) | [fitxa](empreses/SE0000869646.md) |

#### Llista `no_certificada`

> **Estat (lot 3, 19/11/2026, revisat el 20/11/2026 amb els criteris aprovats per Jordi; branca `cas/no-certificada-lot3`, proposta pendent del flux DF → Doctorat → Jordi):** treballades les 241 files `no_certificada`: 211 confirmades (CEO i etiqueta provats amb cita A/B), 11 corregides (canvi de `FounderCEO` aplicat), 8 amb proposta de CEO per a DF i 11 indeterminades; 11 canvis de `FounderCEO` aplicats a la base amb prova A/B. Detall a `docs/REGISTRE_CANVIS.md`, secció «Lot 3», i a cada fitxa; els dubtes que queden són al PR. Les files continuen `no_certificada` fins que el flux les validi. La taula següent és l'estat d'origen (v8 r3) i no s'ha reescrit.

| ISIN | Empresa | Any | Motiu | Fitxa |
|---|---|---|---|---|
| `BE0974320526` | Umicore S.A. Actions Nom. o.N. | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/BE0974320526.md) |
| `BE0974320526` | Umicore S.A. Actions Nom. o.N.2) | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/BE0974320526.md) |
| `BE0974320526` | Umicore S.A. Actions Nom. o.N. | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/BE0974320526.md) |
| `BE0974320526` | Umicore S.A. Actions Nom. o.N. | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/BE0974320526.md) |
| `BE0974400328` | Azelis Group N.V. Actions Nominatives o.N. | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/BE0974400328.md) |
| `BE0974400328` | Azelis Group N.V. Actions Nominatives o.N. | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/BE0974400328.md) |
| `CH0012138530` | Credit Suisse Group AG Namens-Aktien SF | 2022 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/CH0012138530.md) |
| `CH0015536466` | Galenica AG Nam.-Akt. SF 0,10 | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0015536466.md) |
| `CH0030170408` | Geberit AG Nam.-Akt. (Dispost.) SF -,10 | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0030170408.md) |
| `CH0030170408` | Geberit AG Nam.-Akt. (Dispost.) SF -,10 | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0030170408.md) |
| `CH0030170408` | Geberit AG Nam.-Akt. (Dispost.) SF -,102) | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0030170408.md) |
| `CH0030170408` | Geberit AG Nam.-Akt. (Dispost.) SF -,10 | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0030170408.md) |
| `CH0030170408` | Geberit AG Nam.-Akt. (Dispost.) SF -,10 | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0030170408.md) |
| `CH0030170408` | Geberit AG Nam.-Akt. (Dispost.) SF -,10 | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0030170408.md) |
| `CH0030170408` | Geberit AG Nam.-Akt. (Dispost.) SF -,10 | 2022 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0030170408.md) |
| `CH0030170408` | Geberit AG Nam.-Akt. (Dispost.) SF -,10 | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0030170408.md) |
| `CH0030170408` | Geberit AG Nam.-Akt. (Dispost.) SF -,10 | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0030170408.md) |
| `CH0030170408` | Geberit AG Nam.-Akt. (Dispost.) SF -,10 | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0030170408.md) |
| `CH0038389992` | BB Biotech AG Namens-Aktien SF 0,202) | 2017 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/CH0038389992.md) |
| `CH0038389992` | BB Biotech AG Namens-Aktien SF 0,202) | 2018 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/CH0038389992.md) |
| `CH0038389992` | BB Biotech AG Namens-Aktien SF 0,20 | 2019 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/CH0038389992.md) |
| `CH0126881561` | Swiss Re AG Namens-Aktien SF -,10 | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0126881561.md) |
| `CH0126881561` | Swiss Re AG Namens-Aktien SF -,10 | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0126881561.md) |
| `CH0210483332` | Cie Financière Richemont AG Namens-Aktien | 2017 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/CH0210483332.md) |
| `CH0239229302` | SFS Group AG Nam.-Aktien SF -,10 | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0239229302.md) |
| `CH0239229302` | SFS Group AG Nam.-Aktien SF -,10 | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0239229302.md) |
| `CH0239229302` | SFS Group AG Nam.-Aktien SF -,10 | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/CH0239229302.md) |
| `DE0005408116` | Aareal Bank AG Inhaber-Aktien o.N. | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DE0005408116.md) |
| `DE0005408116` | Aareal Bank AG Inhaber-Aktien o.N. | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DE0005408116.md) |
| `DE0005408116` | Aareal Bank AG Inhaber-Aktien o.N. | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DE0005408116.md) |
| `DE0005545503` | Drillisch AG Inhaber-Aktien o.N. | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DE0005545503.md) |
| `DE0005785802` | Fresenius Medical Care KGaA Inhaber-Aktien | 2022 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DE0005785802.md) |
| `DE0006062144` | Covestro AG Inhaber-Aktien o.N. | 2018 | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/DE0006062144.md) |
| `DE0006231004` | Infineon Technologies AG Namens-Aktien | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DE0006231004.md) |
| `DE0006231004` | Infineon Technologies AG Namens-Aktien | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DE0006231004.md) |
| `DE0006231004` | Infineon Technologies AG Namens-Aktien | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DE0006231004.md) |
| `DE0006231004` | Infineon Technologies AG Namens-Aktien | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DE0006231004.md) |
| `DE0006231004` | Infineon Technologies AG Namens-Aktien | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DE0006231004.md) |
| `DE0006231004` | Infineon Technologies AG Namens-Aktien | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DE0006231004.md) |
| `DE0008303504` | TAG Immobilien AG Inhaber-Aktien o.N. | 2021 | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/DE0008303504.md) |
| `DE000A3H3LL2` | Vantage Towers AG Namens-Aktien o.N. | 2022 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DE000A3H3LL2.md) |
| `DE000KSAG888` | K+S Aktiengesellschaft Namens-Aktien o.N. | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DE000KSAG888.md) |
| `DK0010244508` | A.P.Møller-Mærsk A/​S Navne-Aktier B DK | 2016 | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/DK0010244508.md) |
| `DK0010244508` | A.P.Møller-Mærsk A/​S Navne-Aktier B DK | 2018 | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/DK0010244508.md) |
| `DK0010287663` | NKT A/​S Navne-Aktier DK 20 | 2023 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/DK0010287663.md) |
| `DK0010287663` | NKT A/​S Navne-Aktier DK 20 | 2024 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/DK0010287663.md) |
| `DK0010287663` | NKT A/​S Navne-Aktier DK 20 | 2025 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/DK0010287663.md) |
| `DK0060542181` | ISS AS Indehaver Aktier DK 1 | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DK0060542181.md) |
| `DK0060542181` | ISS AS Indehaver Aktier DK 1 | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DK0060542181.md) |
| `DK0060542181` | ISS AS Indehaver Aktier DK 1 | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DK0060542181.md) |
| `DK0060542181` | ISS AS Indehaver Aktier DK 1 | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DK0060542181.md) |
| `DK0060634707` | Royal Unibrew AS Navne-Aktier DK 2 | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DK0060634707.md) |
| `DK0060634707` | Royal Unibrew AS Navne-Aktier DK 2 | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DK0060634707.md) |
| `DK0060634707` | Royal Unibrew AS Navne-Aktier DK 2 | 2022 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DK0060634707.md) |
| `DK0060634707` | Royal Unibrew AS Navne-Aktier DK 2 | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DK0060634707.md) |
| `DK0060634707` | Royal Unibrew AS Navne-Aktier DK 2 | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DK0060634707.md) |
| `DK0060634707` | Royal Unibrew AS Navne-Aktier DK 2 | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/DK0060634707.md) |
| `ES0111845014` | Abertis Infraestructuras S.A. Acciones Nom. | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0111845014.md) |
| `ES0111845014` | Abertis Infraestructuras S.A. Acciones Nom. | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0111845014.md) |
| `ES0116870314` | Gas Natural SDG S.A. Acciones Port. EO 1 | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0116870314.md) |
| `ES0116870314` | Gas Natural SDG S.A. Acciones Port. EO 1 | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0116870314.md) |
| `ES0127797019` | EDP Renováveis S.A. Acciones Port. EO 5 | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0127797019.md) |
| `ES0127797019` | EDP Renováveis S.A. Acciones Port. EO 5 | 2022 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0127797019.md) |
| `ES0127797019` | EDP Renováveis S.A. Acciones Port. EO 5 | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0127797019.md) |
| `ES0127797019` | EDP Renováveis S.A. Acciones Port. EO 5 | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0127797019.md) |
| `ES0127797019` | EDP Renováveis S.A. Acciones Port. EO 5 | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0127797019.md) |
| `ES0130960018` | Enagas S.A. Acciones Port. EO 1,50 | 2016 | Doctorat 8: etiqueta 0 per Oreja, pero r3e te incidencia greu E2 i nomes un model s'hi pronuncia. No es certifica. | [fitxa](empreses/ES0130960018.md) |
| `ES0130960018` | Enagas S.A. Acciones Port. EO 1,50 | 2017 | Doctorat 8: etiqueta 0 per Oreja, pero r3e te incidencia greu E2 i nomes un model s'hi pronuncia. No es certifica. | [fitxa](empreses/ES0130960018.md) |
| `ES0130960018` | Enagas S.A. Acciones Port. EO 1,50 | 2018 | Doctorat 8: etiqueta 0 per Oreja, pero r3e te incidencia greu E2 i nomes un model s'hi pronuncia. No es certifica. | [fitxa](empreses/ES0130960018.md) |
| `ES0130960018` | Enagas S.A. Acciones Port. EO 1,50 | 2019 | Doctorat 8: etiqueta 0 per Oreja, pero r3e te incidencia greu E2 i nomes un model s'hi pronuncia. No es certifica. | [fitxa](empreses/ES0130960018.md) |
| `ES0130960018` | Enagas S.A. Acciones Port. EO 1,50 | 2020 | Doctorat 8: etiqueta 0 per Oreja, pero r3e te incidencia greu E2 i nomes un model s'hi pronuncia. No es certifica. | [fitxa](empreses/ES0130960018.md) |
| `ES0130960018` | Enagas S.A. Acciones Port. EO 1,50 | 2021 | Doctorat 8: etiqueta 0 per Oreja, pero r3e te incidencia greu E2 i nomes un model s'hi pronuncia. No es certifica. | [fitxa](empreses/ES0130960018.md) |
| `ES0173516115` | Repsol S.A. Acciones Port. EO 1 | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0173516115.md) |
| `ES0173516115` | Repsol S.A. Acciones Port. EO 1 | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0173516115.md) |
| `ES0173516115` | Repsol S.A. Acciones Port. EO 1 | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0173516115.md) |
| `ES0173516115` | Repsol S.A. Acciones Port. EO 1 | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0173516115.md) |
| `ES0173516115` | Repsol S.A. Acciones Port. EO 1 | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0173516115.md) |
| `ES0173516115` | Repsol S.A. Acciones Port. EO 1 | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0173516115.md) |
| `ES0173516115` | Repsol S.A. Acciones Port. EO 1 | 2022 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0173516115.md) |
| `ES0173516115` | Repsol S.A. Acciones Port. EO 1 | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0173516115.md) |
| `ES0173516115` | Repsol S.A. Acciones Port. EO 1 | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0173516115.md) |
| `ES0173516115` | Repsol S.A. Acciones Port. EO 1 | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0173516115.md) |
| `ES0184262212` | Viscofan S.A. Acciones Port. EO 0,70 | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0184262212.md) |
| `ES0184262212` | Viscofan S.A. Acciones Port. EO 0,70 | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0184262212.md) |
| `ES0184262212` | Viscofan S.A. Acciones Port. EO 0,70 | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0184262212.md) |
| `ES0184262212` | Viscofan S.A. Acciones Port. EO 0,70 | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0184262212.md) |
| `ES0184262212` | Viscofan S.A. Acciones Port. EO 0,70 | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/ES0184262212.md) |
| `FI0009005870` | Konecranes Oyj Registered Shares o.N. | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FI0009005870.md) |
| `FI4000552526` | Mandatum OYJ Registered Shares o.N. | 2025 | Doctorat tanca l'etiqueta, pero r3e tenia incidences greus (E4,E6); no puja a N1/N2 | [fitxa](empreses/FI4000552526.md) |
| `FR0000035081` | Icade S.A. Actions au Porteur o.N. | 2016 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/FR0000035081.md) |
| `FR0000035081` | Icade S.A. Actions au Porteur o.N. | 2017 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/FR0000035081.md) |
| `FR0000035081` | Icade S.A. Actions au Porteur o.N. | 2018 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/FR0000035081.md) |
| `FR0000035081` | Icade S.A. Actions au Porteur o.N. | 2019 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/FR0000035081.md) |
| `FR0000035081` | Icade S.A. Actions au Porteur o.N. | 2020 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/FR0000035081.md) |
| `FR0000050809` | Sopra Steria Group S.A. Actions Port. EO 1 | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000050809.md) |
| `FR0000120628` | AXA S.A. Actions Port. EO 2,29 | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000120628.md) |
| `FR0000120628` | AXA S.A. Actions Port. EO 2,29 | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000120628.md) |
| `FR0000120628` | AXA S.A. Actions Port. EO 2,29 | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000120628.md) |
| `FR0000120628` | AXA S.A. Actions Port. EO 2,29 | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000120628.md) |
| `FR0000120628` | AXA S.A. Actions Port. EO 2,29 | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000120628.md) |
| `FR0000120628` | AXA S.A. Actions Port. EO 2,29 | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000120628.md) |
| `FR0000120628` | AXA S.A. Actions Port. EO 2,29 | 2022 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000120628.md) |
| `FR0000120628` | AXA S.A. Actions Port. EO 2,29 | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000120628.md) |
| `FR0000120628` | AXA S.A. Actions Port. EO 2,29 | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000120628.md) |
| `FR0000120628` | AXA S.A. Actions Port. EO 2,29 | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000120628.md) |
| `FR0000121014` | LVMH Moët Henn. L. Vuitton SE Actions Port. | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000121014.md) |
| `FR0000121014` | LVMH Moët Henn. L. Vuitton SE Actions Port. | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000121014.md) |
| `FR0000121014` | LVMH Moët Henn. L. Vuitton SE Actions Port. | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000121014.md) |
| `FR0000121014` | LVMH Moët Henn. L. Vuitton SE Actions Port. | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000121014.md) |
| `FR0000121014` | LVMH Moët Henn. L. Vuitton SE Actions Port. | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000121014.md) |
| `FR0000121014` | LVMH Moët Henn. L. Vuitton SE Actions | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000121014.md) |
| `FR0000121014` | LVMH Moët Henn. L. Vuitton SE Actions Port. | 2022 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000121014.md) |
| `FR0000121014` | LVMH Moët Henn. L. Vuitton SE Actions Port. | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000121014.md) |
| `FR0000121014` | LVMH Moët Henn. L. Vuitton SE Actions Port. | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000121014.md) |
| `FR0000121014` | LVMH Moët Henn. L. Vuitton SE Actions Port. | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000121014.md) |
| `FR0000121220` | Sodexo S.A. Actions Port. EO 4 | 2016 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/FR0000121220.md) |
| `FR0000121220` | Sodexo S.A. Actions Port. EO 4 | 2017 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/FR0000121220.md) |
| `FR0000121220` | Sodexo S.A. Actions Port. EO 4 | 2018 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/FR0000121220.md) |
| `FR0000121220` | Sodexo S.A. Actions Port. EO 4 | 2019 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/FR0000121220.md) |
| `FR0000121220` | Sodexo S.A. Actions Port. EO 4 | 2020 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/FR0000121220.md) |
| `FR0000124141` | Veolia Environnement S.A. Actions au | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000124141.md) |
| `FR0000124141` | Veolia Environnement S.A. Actions au | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000124141.md) |
| `FR0000124141` | Veolia Environnement S.A. Actions au | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000124141.md) |
| `FR0000124141` | Veolia Environnement S.A. Actions au | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000124141.md) |
| `FR0000124141` | Veolia Environnement S.A. Actions au | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000124141.md) |
| `FR0000124141` | Veolia Environnement S.A. Actions au | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000124141.md) |
| `FR0000124570` | Compagnie Plastic Omnium S.A. Actions | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000124570.md) |
| `FR0000124570` | Compagnie Plastic Omnium S.A. Actions | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000124570.md) |
| `FR0000124570` | Compagnie Plastic Omnium S.A. Actions | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0000124570.md) |
| `FR0004125920` | Amundi S.A. Actions au Porteur EO 2,5 | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0004125920.md) |
| `FR0004125920` | Amundi S.A. Actions au Porteur EO 2,5 | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0004125920.md) |
| `FR0004125920` | Amundi S.A. Actions au Porteur EO 2,5 | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0004125920.md) |
| `FR0004125920` | Amundi S.A. Actions au Porteur EO 2,5 | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0004125920.md) |
| `FR0010307819` | Legrand S.A. Actions au Port. EO 4 | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0010307819.md) |
| `FR0010307819` | Legrand S.A. Actions au Port. EO 4 | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0010307819.md) |
| `FR0010613471` | Suez S.A. Actions Port. EO 4 | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0010613471.md) |
| `FR0010613471` | Suez S.A. Actions Port. EO 4 | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0010613471.md) |
| `FR0010613471` | Suez S.A. Actions Port. EO 4 | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/FR0010613471.md) |
| `FR0011594233` | SFR Group S.A. Actions Nom. EO 1 | 2016 | Doctorat tanca l'etiqueta, pero r3e tenia incidences greus (E4); no puja a N1/N2 | [fitxa](empreses/FR0011594233.md) |
| `GB0000031285` | Aberdeen Asset Management PLC Registered | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB0000031285.md) |
| `GB0000904986` | Bellway PLC Registered Shares LS -,125 | 2017 | Doctorat 9 aplicada (Ayres, FounderCEO=0), pero nomes Claude s'hi pronuncia. No es certifica. El canvi va al registre. | [fitxa](empreses/GB0000904986.md) |
| `GB0003308607` | Spectris PLC Registered Shares LS -,05 | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB0003308607.md) |
| `GB0003308607` | Spectris PLC Registered Shares LS -,05 | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB0003308607.md) |
| `GB0003308607` | Spectris PLC Registered Shares LS -,05 | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB0003308607.md) |
| `GB0003308607` | Spectris PLC Registered Shares LS -,05 | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB0003308607.md) |
| `GB0003308607` | Spectris PLC Registered Shares LS -,05 | 2022 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB0003308607.md) |
| `GB0003308607` | Spectris PLC Registered Shares LS -,05 | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB0003308607.md) |
| `GB0003308607` | Spectris PLC Registered Shares LS -,05 | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB0003308607.md) |
| `GB0003308607` | Spectris PLC Registered Shares LS -,05 | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB0003308607.md) |
| `GB0005758098` | Meggitt PLC Registered Shares LS -,052) | 2016 | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/GB0005758098.md) |
| `GB0005758098` | Meggitt PLC Registered Shares LS -,05 | 2018 | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/GB0005758098.md) |
| `GB0007197378` | RPC Group PLC Registered Shares LS -,052) | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB0007197378.md) |
| `GB0007197378` | RPC Group PLC Registered Shares LS -,052) | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB0007197378.md) |
| `GB0007197378` | RPC Group PLC Registered Shares LS -,05 | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB0007197378.md) |
| `GB0033986497` | ITV PLC Registered Shares LS -,10 | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB0033986497.md) |
| `GB00B07KD360` | Cobham PLC Registered Shares LS -,0252) | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB00B07KD360.md) |
| `GB00BMJ6DW54` | Informa PLC Registered Shares LS -,001 | 2016 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/GB00BMJ6DW54.md) |
| `GB00BMJ6DW54` | Informa PLC Registered Shares LS -,001 | 2017 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/GB00BMJ6DW54.md) |
| `GB00BMJ6DW54` | Informa PLC Registered Shares LS -,001 | 2018 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/GB00BMJ6DW54.md) |
| `GB00BMJ6DW54` | Informa PLC Registered Shares LS -,001 | 2019 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/GB00BMJ6DW54.md) |
| `GB00BMJ6DW54` | Informa PLC Registered Shares LS -,001 | 2020 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/GB00BMJ6DW54.md) |
| `GB00BMJ6DW54` | Informa PLC Registered Shares LS -,001 | 2021 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/GB00BMJ6DW54.md) |
| `GB00BMJ6DW54` | Informa PLC Registered Shares LS -,001 | 2022 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/GB00BMJ6DW54.md) |
| `GB00BMJ6DW54` | Informa PLC Registered Shares LS -,001 | 2023 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/GB00BMJ6DW54.md) |
| `GB00BMJ6DW54` | Informa PLC Registered Shares LS -,001 | 2024 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/GB00BMJ6DW54.md) |
| `GB00BMJ6DW54` | Informa PLC Registered Shares LS -,001 | 2025 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/GB00BMJ6DW54.md) |
| `GB00BNGDN821` | Melrose Industries PLC Registered Share | 2024 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/GB00BNGDN821.md) |
| `GB00BNGDN821` | Melrose Industries PLC Registered Share | 2025 | incidencia greu r3e (E6): no puja a N1/N2 | [fitxa](empreses/GB00BNGDN821.md) |
| `GB00BQY7BX88` | Micro Focus International PLC Registered | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB00BQY7BX88.md) |
| `GB00BWFGQN14` | Spirax Group PLC Reg. Shares LS | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB00BWFGQN14.md) |
| `GB00BWFGQN14` | Spirax Group PLC Reg. Shares LS | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/GB00BWFGQN14.md) |
| `IE00BF0L3536` | AIB Group PLC Registered Shares EO -,625 | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BF0L3536.md) |
| `IE00BF0L3536` | AIB Group PLC Registered Shares EO -,625 | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BF0L3536.md) |
| `IE00BF0L3536` | AIB Group PLC Registered Shares EO -,625 | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BF0L3536.md) |
| `IE00BF0L3536` | AIB Group PLC Registered Shares EO -,625 | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BF0L3536.md) |
| `IE00BYTBXV33` | Ryanair Holdings PLC Registered Shares EO | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BYTBXV33.md) |
| `IE00BYTBXV33` | Ryanair Holdings PLC Registered Shares EO | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BYTBXV33.md) |
| `IE00BYTBXV33` | Ryanair Holdings PLC Registered Shares EO | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BYTBXV33.md) |
| `IE00BYTBXV33` | Ryanair Holdings PLC Registered Shares EO | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BYTBXV33.md) |
| `IE00BYTBXV33` | Ryanair Holdings PLC Registered Shares EO | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BYTBXV33.md) |
| `IE00BYTBXV33` | Ryanair Holdings PLC Registered Shares EO | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BYTBXV33.md) |
| `IE00BYTBXV33` | Ryanair Holdings PLC Registered Shares EO | 2022 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BYTBXV33.md) |
| `IE00BYTBXV33` | Ryanair Holdings PLC Registered Shares EO | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BYTBXV33.md) |
| `IE00BYTBXV33` | Ryanair Holdings PLC Registered Shares EO | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BYTBXV33.md) |
| `IE00BYTBXV33` | Ryanair Holdings PLC Registered Shares EO | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IE00BYTBXV33.md) |
| `IT0000066123` | BPER Banca S.p.A. Azioni nom. EO 3 | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IT0000066123.md) |
| `IT0003497168` | Telecom Italia S.p.A. Azioni nom. o.N. | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IT0003497168.md) |
| `IT0003497168` | Telecom Italia S.p.A. Azioni nom. o.N. | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IT0003497168.md) |
| `IT0003497168` | Telecom Italia S.p.A. Azioni nom. o.N. | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IT0003497168.md) |
| `IT0003497168` | Telecom Italia S.p.A. Azioni nom. o.N. | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IT0003497168.md) |
| `IT0003497168` | Telecom Italia S.p.A. Azioni nom. o.N. | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/IT0003497168.md) |
| `JE00B5TT1872` | Centamin PLC Registered Shares o.N. | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/JE00B5TT1872.md) |
| `JE00B5TT1872` | Centamin PLC Registered Shares o.N. | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/JE00B5TT1872.md) |
| `JE00B5TT1872` | Centamin PLC Registered Shares o.N. | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/JE00B5TT1872.md) |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/LU1072616219.md) |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/LU1072616219.md) |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/LU1072616219.md) |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/LU1072616219.md) |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/LU1072616219.md) |
| `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/LU1072616219.md) |
| `LU1673108939` | Aroundtown SA Inhaber-Aktien EO -,01 | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/LU1673108939.md) |
| `LU1673108939` | Aroundtown SA Bearer Shares EO -,01 | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/LU1673108939.md) |
| `LU1673108939` | Aroundtown SA Bearer Shares EO -,01 | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/LU1673108939.md) |
| `LU1673108939` | Aroundtown SA Bearer Shares EO -,01 | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/LU1673108939.md) |
| `NL0000008977` | Heineken Holding N.V. Aandelen aan toonder | 2016 | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/NL0000008977.md) |
| `NL0000008977` | Heineken Holding N.V. Aandelen aan toonder | 2018 | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/NL0000008977.md) |
| `NL0000008977` | Heineken Holding N.V. Aandelen aan | 2021 | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/NL0000008977.md) |
| `NL0000008977` | Heineken Holding N.V. Aandelen aan toonder | 2022 | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/NL0000008977.md) |
| `NL0000008977` | Heineken Holding N.V. Aandelen aan toonder | 2023 | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/NL0000008977.md) |
| `NL0000008977` | Heineken Holding N.V. Aandelen aan toonder | 2024 | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/NL0000008977.md) |
| `NL0000008977` | Heineken Holding N.V. Aandelen aan toonder | 2025 | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/NL0000008977.md) |
| `NL0000009165` | Heineken N.V. Aandelen aan toonder EO | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/NL0000009165.md) |
| `NL0000009165` | Heineken N.V. Aandelen aan toonder EO | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/NL0000009165.md) |
| `NL0000009165` | Heineken N.V. Aandelen aan toonder EO | 2018 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/NL0000009165.md) |
| `NL0000009165` | Heineken N.V. Aandelen aan toonder EO | 2019 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/NL0000009165.md) |
| `NL0011375019` | Steinhoff Internatl Hldgs N.V. Aandelen op | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: 0) | [fitxa](empreses/NL0011375019.md) |
| `NL0011375019` | Steinhoff Internatl Hldgs N.V. Aandelen op | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: 0) | [fitxa](empreses/NL0011375019.md) |
| `NL0012866412` | BE Semiconductor Inds N.V. Aandelen op | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/NL0012866412.md) |
| `NL0012866412` | BE Semiconductor Inds N.V. Aandelen op | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/NL0012866412.md) |
| `NL0012866412` | BE Semiconductor Inds N.V. Aandelen op | 2022 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/NL0012866412.md) |
| `NL0012866412` | BE Semiconductor Inds N.V. Aandelen op | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/NL0012866412.md) |
| `NL0012866412` | BE Semiconductor Inds N.V. Aandelen op | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/NL0012866412.md) |
| `NL0012866412` | BE Semiconductor Inds N.V. Aandelen op | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/NL0012866412.md) |
| `NO0012470089` | Tomra Systems ASA Navne-Aksjer NK -,50 | 2022 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/NO0012470089.md) |
| `NO0012470089` | Tomra Systems ASA Navne-Aksjer NK -,50 | 2023 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/NO0012470089.md) |
| `NO0012470089` | Tomra Systems ASA Navne-Aksjer NK -,50 | 2024 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/NO0012470089.md) |
| `NO0012470089` | Tomra Systems ASA Navne-Aksjer NK -,50 | 2025 | l'acord nomes te cites web no verificades (cita_no_trobada o pendent): no es certifica | [fitxa](empreses/NO0012470089.md) |
| `PLPEKAO00016` | Bank Polska Kasa Opieki S.A. Inhaber-Aktien | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/PLPEKAO00016.md) |
| `PLPEKAO00016` | Bank Polska Kasa Opieki S.A. Inhaber- | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/PLPEKAO00016.md) |
| `PLPEKAO00016` | Bank Polska Kasa Opieki S.A. Inhaber-Aktien | 2022 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/PLPEKAO00016.md) |
| `PLPEKAO00016` | Bank Polska Kasa Opieki S.A. Inhaber-Aktien | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/PLPEKAO00016.md) |
| `PLPKO0000016` | Powszechna K.O.(PKO)Bk Polski Inhaber- | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/PLPKO0000016.md) |
| `PLPKO0000016` | Powszechna K.O.(PKO)Bk Polski Inhaber- | 2025 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/PLPKO0000016.md) |
| `PLPZU0000011` | Powszechny Zaklad Ubezpieczen Namens- | 2020 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/PLPZU0000011.md) |
| `PLPZU0000011` | Powszechny Zaklad Ubezpieczen Namens- | 2021 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/PLPZU0000011.md) |
| `PLPZU0000011` | Powszechny Zaklad Ubezpieczen Namens- | 2022 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/PLPZU0000011.md) |
| `PLPZU0000011` | Powszechny Zaklad Ubezpieczen Namens- | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/PLPZU0000011.md) |
| `SE0000806994` | JM AB Namn-Aktier o.N. | 2016 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/SE0000806994.md) |
| `SE0000806994` | JM AB Namn-Aktier o.N. | 2017 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/SE0000806994.md) |
| `SE0015961909` | Hexagon AB Namn-Aktier B (fria) o.N. | 2023 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/SE0015961909.md) |
| `SE0015961909` | Hexagon AB Namn-Aktier B (fria) o.N. | 2024 | continua sense certificar (ChatGPT: indeterminat, Claude efectiu: indeterminat) | [fitxa](empreses/SE0015961909.md) |

## 2. Files sense auditar (3890)

Recompte a la base v8 r3: **3890** files amb `sim_estat_certificacio=fora_mostra_auditoria` [V], d'un panell de 6.012. Verifica el CEO i l'etiqueta empresa per empresa i afegeix les cites que faltin. L'índex de totes les empreses és a [INDEX.md](INDEX.md).

## 3. Fitxes completes

Per a cada ISIN, la fitxa ha d'acabar tenint: el CEO de cada any amb cita, la prova de fundador o de no fundador, el sector i les fonts amb Wayback.

## 4. Errors, també si la fila és certificada

Si una dada contradiu la base, encara que estigui certificada, proposa'n la correcció amb la cita literal, l'URL i el Wayback, en una branca i un PR.

## Schulenberg / CTS Eventim — tasca de forma

Fitxa: [empreses/DE0005470306.md](empreses/DE0005470306.md). ISIN `DE0005470306`, CEO Klaus-Peter Schulenberg, 2019-2025, FounderCEO=`1`, certificada N1. A la base la regla aplicada és `FT` (`regla_aplicada_v3=FT`; `regles=d;FT`) i `fundador_transformador=0`. [V]

Tasca de forma (l'**etiqueta no canvia**): importar la cita B **D1256** del paquet r3e, amb URL i Wayback, i canviar la regla de `FT` a `directa`.

- Cita literal recollida a les afirmacions r3e (id_document `D1256`): «Klaus-Peter Schulenberg ... Founder and CEO, CTS EVENTIM» [V] com a text del camp `cita_literal` d'aquell paquet (els punts suspensius són al camp d'origen).
- URL oficial: https://www.iqmagazine.com/wp-content/uploads/2025/04/IQ96_ISSUU_Preview.pdf [V]
- URL arxivada al paquet r3e: buida. El Wayback queda pendent d'afegir; no s'inventa. [V] com a absència al camp `url_arxivada`.
- `text_al_paquet` d'aquest document: `no`. Cal obrir la font i confirmar la cita literal abans de proposar el canvi de regla.

## Sector pendent

L'extensió del supersector del juny 2023 a 2024-2025 ja està feta a la v8 r3 per als ISIN que tenien `any_font=2023` (1.076 files, 561 ISIN, `sector_estes_des_2023=1`). No s'estén cap altre sector.

### 48 empreses només 2024-2025 (sense font pública després de juny 2023)

Pendent per a Claude: una font A (per exemple un informe anual amb la classificació ICB).

| ISIN | Empresa | Anys al panell | Motiu | Fitxa |
|---|---|---|---|---|
| `BE0003823409` | Financière de Tubize S.A. Actions au Port. | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/BE0003823409.md) |
| `BE0003867844` | KBC Ancora Actions au Port. o.N. | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/BE0003867844.md) |
| `BE0974464977` | Syensqo S.A. Actions au Porteur o.N. | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/BE0974464977.md) |
| `CH0010675863` | Swissquote Grp Holding S.A. Namens-Aktien | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/CH0010675863.md) |
| `CH0011029946` | Inficon Holding AG Nam.-Aktien SF 5 | 2024 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/CH0011029946.md) |
| `CH0011108872` | Mobimo Holding AG Nam.-Aktien SF 3,40 | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/CH0011108872.md) |
| `CH0360826991` | Comet Holding AG Nam.-Akt. SF 1 | 2024 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/CH0360826991.md) |
| `CH0528751586` | VZ Holding AG Nam.-Aktien SF -,05 | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/CH0528751586.md) |
| `CH1335392721` | Galderma Group AG Registered Shares o.N. | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/CH1335392721.md) |
| `CH1386220409` | Sunrise Communications AG Nam.-Aktien | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/CH1386220409.md) |
| `CH1430134226` | Amrize AG Namens-Aktien DL 1000 | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/CH1430134226.md) |
| `DE000A0D6554` | Nordex SE Inhaber-Aktien o.N. | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/DE000A0D6554.md) |
| `DE000AUM0V10` | AUMOVIO SE Namens-Aktien o.N. | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/DE000AUM0V10.md) |
| `DE000FTG1111` | flatexDEGIRO AG Namens-Aktien o.N. | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/DE000FTG1111.md) |
| `DE000HAG0005` | HENSOLDT AG Inhaber-Aktien o.N. | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/DE000HAG0005.md) |
| `DE000RENK730` | RENK Group AG Inhaber-Aktien o.N. | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/DE000RENK730.md) |
| `DK0060257814` | Zealand Pharma A/​S Navne-Aktier DK 1 | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/DK0060257814.md) |
| `ES0105777017` | Puig Brands S.A. Acciones EO 0,06 | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/ES0105777017.md) |
| `ES0118594417` | Indra Sistemas S.A. Acciones Port. EO 0,20 | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/ES0118594417.md) |
| `ES0180907000` | Unicaja Banco S.A. Acciones Nom. EO 0,25 | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/ES0180907000.md) |
| `ES06837469D8` | Vidrala S.A. Anrechte | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/ES06837469D8.md) |
| `FI0009004824` | Kemira Oy Registered Shares o.N. | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/FI0009004824.md) |
| `FI4000552526` | Mandatum OYJ Registered Shares o.N. | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/FI4000552526.md) |
| `FI4000571013` | Hiab Corp. Registered Shares Class B o.N. | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/FI4000571013.md) |
| `FR0000073298` | IPSOS S.A. Actions Port. EO -,25 | 2024 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/FR0000073298.md) |
| `FR0011675362` | NEOEN S.A. Actions Port. EO 2 | 2024 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/FR0011675362.md) |
| `FR0012333284` | Abivax S.A. Actions au Porteur EO -,01 | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/FR0012333284.md) |
| `FR0013258662` | Ayvens S.A. Actions Nom. EO 1,50 | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/FR0013258662.md) |
| `GB00BF4HYT85` | Lion Finance Group PLC Registered Shares | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/GB00BF4HYT85.md) |
| `GB00BVGBY890` | Zegona Communications PLC Registered | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/GB00BVGBY890.md) |
| `GB00BYT18307` | TBC Bank Group PLC Registered Shares LS | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/GB00BYT18307.md) |
| `IL0011284465` | Plus500 Ltd. Registered Shares LS -,01 | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/IL0011284465.md) |
| `IT0001031084` | Banca Generali S.p.A. Azioni nom. B EO 1 | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/IT0001031084.md) |
| `IT0004776628` | Banca Mediolanum S.p.A. Azioni nom. o.N. | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/IT0004776628.md) |
| `IT0005508921` | Bca Monte dei Paschi di Siena Azioni nom. | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/IT0005508921.md) |
| `IT0005541336` | Lottomatica Group S.p.A. Azioni nom. o.N. | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/IT0005541336.md) |
| `IT0005619678` | Reply S.p.A. Anrechte | 2024 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/IT0005619678.md) |
| `JE00BRX98089` | CVC Capital Partners PLC Registered Shares | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/JE00BRX98089.md) |
| `NL00150003E1` | Fugro N.V. Aand.op naam DR EO 0,05 | 2024 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/NL00150003E1.md) |
| `NL0015000LU4` | Iveco Group N.V. Aandelen op naam EUR 1 | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/NL0015000LU4.md) |
| `NO0010631567` | SpareBank 1 Sor-Norge ASA | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/NO0010631567.md) |
| `NO0011202772` | Var Energi ASA Navne-Aksjer | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/NO0011202772.md) |
| `PLBRE0000012` | mBank S.A. Inhaber-Aktien ZY 4 | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/PLBRE0000012.md) |
| `SE0000375115` | Mycronic AB Namn-Aktier SK 1 | 2024 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/SE0000375115.md) |
| `SE0007692850` | Camurus AB Namn-Aktier o.N. | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/SE0007692850.md) |
| `SE0009806607` | Munters Group AB Namn-Aktier B o.N. | 2024 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/SE0009806607.md) |
| `SE0015671995` | Hemnet Group AB Namn-Aktier o.N. | 2024;2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/SE0015671995.md) |
| `SE0025158629` | Mycronic AB Namn-Aktier SK 0,50 | 2025 | cap PDF public de components amb supersector despres de juny 2023 (anys panell 2024-2025 sense font) | [fitxa](empreses/SE0025158629.md) |

### 24 empreses no casades [NV a la font]

Pendent per a Claude: una font A (per exemple un informe anual amb la classificació ICB).

| ISIN | Empresa | Anys al panell | Motiu | Fitxa |
|---|---|---|---|---|
| `BE0974400328` | Azelis Group N.V. Actions Nominatives o.N. | 2023;2024;2025 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/BE0974400328.md) |
| `CH0002178181` | Stadler Rail AG Namens-Aktien SF 0,20 | 2020 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/CH0002178181.md) |
| `CH0239229302` | SFS Group AG Nam.-Aktien SF -,10 | 2023;2024;2025 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/CH0239229302.md) |
| `CH0496451508` | SoftwareONE Holding AG Namens-Aktien SF | 2020 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/CH0496451508.md) |
| `CH0565630669` | Sunrise Communications Gr. AG Nam.- | 2020 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/CH0565630669.md) |
| `CH1169360919` | Accelleron Industries Ltd. Namens-Aktien SF | 2023;2024;2025 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/CH1169360919.md) |
| `CH1243598427` | Sandoz Group AG Namens-Aktien SF -,05 | 2023;2024;2025 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/CH1243598427.md) |
| `DE000A0TGJ55` | VARTA AG Inhaber-Aktien o.N. | 2020 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/DE000A0TGJ55.md) |
| `DK0010287663` | NKT A/​S Navne-Aktier DK 20 | 2023;2024;2025 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/DK0010287663.md) |
| `ES0105066023` | Cellnex Telecom S.A. Acciones Port. Em.10/​ | 2019 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/ES0105066023.md) |
| `ES0618900981` | Ferrovial S.A. Anrechte | 2016 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/ES0618900981.md) |
| `ES06189009A2` | Ferrovial S.A. Anrechte | 2017 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/ES06189009A2.md) |
| `ES06837469B2` | Vidrala S.A. Anrechte | 2023 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/ES06837469B2.md) |
| `GB00BDFB6Q69` | Rolls Royce Holdings PLC Reg.Entitl.Shs.C | 2017 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/GB00BDFB6Q69.md) |
| `GB00BFCMW356` | Rolls Royce Holdings PLC Reg.Entitl.C 01/​19 | 2018 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/GB00BFCMW356.md) |
| `GB00BKT6BP09` | Rolls Royce Holdings PLC Reg.Entitl.C 01/​20 | 2019 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/GB00BKT6BP09.md) |
| `GB00BZC0LD27` | Rolls Royce Holdings PLC Reg.Entitl.Shs.C | 2016 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/GB00BZC0LD27.md) |
| `IE00BYSZ9G33` | Allied Irish Banks PLC Registered Shares EO | 2017 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/IE00BYSZ9G33.md) |
| `IT0001347308` | BUZZI S.p.A. Azioni nom. o.N. | 2023;2024;2025 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/IT0001347308.md) |
| `IT0005217408` | EXOR S.p.A. Anrechte (technisch) | 2016 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/IT0005217408.md) |
| `KYG7091M1740` | Phoenix Group Holdings Anrechte | 2016 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/KYG7091M1740.md) |
| `LU1250154413` | ADLER Group S.A. Actions Nominatives o.N. | 2020 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/LU1250154413.md) |
| `SE0009242266` | Tele2 AB Anrechte B | 2016 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/SE0009242266.md) |
| `ZAE000004875` | Nedbank Group Ltd. Registered Shares RC 1 | 2018 | ISIN no trobat als PDF de components 2015-2023 (canvi d ISIN o nom no casat) [NV] | [fitxa](empreses/ZAE000004875.md) |

### 25 empreses a revisar (via indirecta)

| ISIN | Empresa | Supersector | Mètode | Fitxa |
|---|---|---|---|---|
| `BMG0112X1056` | AEGON Ltd. Registered Shares o.N. | Insurance | nom_stoxx_via_llista_seleccio (al PDF casa amb NL0000303709) | [fitxa](empreses/BMG0112X1056.md) |
| `CH1429326825` | Siegfried Holding AG Nam.Akt. SF 0,72 | Health Care | nom_stoxx_via_llista_seleccio (al PDF casa amb CH0014284498) | [fitxa](empreses/CH1429326825.md) |
| `DE0003304002` | Software AG Inhaber-Aktien o.N. | Technology | nom_stoxx_via_llista_seleccio (al PDF casa amb DE000A2GS401) | [fitxa](empreses/DE0003304002.md) |
| `DK0062498333` | Novo-Nordisk AS Navne-Aktier B DK 0,1 | Health Care | nom_stoxx_via_llista_seleccio (al PDF casa amb DK0060534915) | [fitxa](empreses/DK0062498333.md) |
| `DK0063855168` | Rockwool A/​S Navne-Aktier B DK 1 | Construction & Materials | nom_stoxx_via_llista_seleccio (al PDF casa amb DK0010219153) | [fitxa](empreses/DK0063855168.md) |
| `ES0105046017` | Aena SME S.A. Acciones Port. EO 1 | Industrial Goods & Services | nom_stoxx_via_llista_seleccio (al PDF casa amb ES0105046009) | [fitxa](empreses/ES0105046017.md) |
| `FI4000552500` | Sampo OYJ Registered Shares Cl.A o.N. | Insurance | nom_stoxx_via_llista_seleccio (al PDF casa amb FI0009003305) | [fitxa](empreses/FI4000552500.md) |
| `FR0013506730` | Vallourec S.A. Actions Port. EO 0,02 | Industrial Goods & Services | nom_stoxx_via_llista_seleccio (al PDF casa amb FR0000120354) | [fitxa](empreses/FR0013506730.md) |
| `FR001400J770` | Air France-KLM S.A. Actions Port. EO 1 | Travel & Leisure | nom_stoxx_via_llista_seleccio (al PDF casa amb FR0000031122) | [fitxa](empreses/FR001400J770.md) |
| `GB00BMWC6P49` | Mondi PLC Registered Shares EO -,22 | Industrial Goods & Services | nom_stoxx_via_llista_seleccio (al PDF casa amb GB00B1CRLC47) | [fitxa](empreses/GB00BMWC6P49.md) |
| `GB00BP0RGD03` | Berkeley Group Holdings PLC Reg.Ordinary | Consumer Products & Services | nom_stoxx_via_llista_seleccio (al PDF casa amb GB00BLJNXL82) | [fitxa](empreses/GB00BP0RGD03.md) |
| `GB00BTK05J60` | Anglo American PLC Registered Shs | Basic Resources | nom_stoxx_via_llista_seleccio (al PDF casa amb GB00B1XZS820) | [fitxa](empreses/GB00BTK05J60.md) |
| `IT0005495657` | Saipem S.p.A. Azioni nom. o.N. | Oil & Gas | nom_stoxx_via_llista_seleccio (al PDF casa amb IT0005252140) | [fitxa](empreses/IT0005495657.md) |
| `JE00BMDZN391` | TP ICAP Group PLC Registered Shares LS | Financial Services | nom_stoxx_via_llista_seleccio (al PDF casa amb GB00B1H0DZ51) | [fitxa](empreses/JE00BMDZN391.md) |
| `LU2598331598` | Tenaris S.A. Registered Shares DL 1 | Energy | nom_stoxx_via_llista_seleccio (al PDF casa amb LU0156801721) | [fitxa](empreses/LU2598331598.md) |
| `NL0015001FS8` | Ferrovial SE Registered Shares EO-,01 | Construction & Materials | nom_stoxx_via_llista_seleccio (al PDF casa amb ES0118900010) | [fitxa](empreses/NL0015001FS8.md) |
| `NL0015001WM6` | Qiagen N.V. Aandelen op naam EO -,01 | Health Care | nom_stoxx_via_llista_seleccio (al PDF casa amb NL0012169213) | [fitxa](empreses/NL0015001WM6.md) |
| `NL0015002CX3` | Qiagen N.V. Aandelen op naam EO -,01 | Health Care | nom_stoxx_via_llista_seleccio (al PDF casa amb NL0012169213) | [fitxa](empreses/NL0015002CX3.md) |
| `NO0013536151` | Kongsberg Gruppen AS Navne-Aksjer NK | Industrial Goods & Services | nom_stoxx_via_llista_seleccio (al PDF casa amb NO0003043309) | [fitxa](empreses/NO0013536151.md) |
| `SE0011116508` | Beijer Ref AB Namn-Aktier B O.N. | Industrial Goods & Services | nom_stoxx_via_llista_seleccio (al PDF casa amb SE0015949748) | [fitxa](empreses/SE0011116508.md) |
| `SE0020539310` | Sectra AB Namn-Aktier Ser.B o.N. | Health Care | nom_stoxx_via_llista_seleccio (al PDF casa amb SE0018245953) | [fitxa](empreses/SE0020539310.md) |
| `SE0021628898` | Volvo Car AB Namn-Aktier B o.N. | Automobiles & Parts | nom_stoxx_via_llista_seleccio (al PDF casa amb SE0016844831) | [fitxa](empreses/SE0021628898.md) |
| `SE0021921269` | Saab AB Namn-Aktier B o.N. | Industrial Goods & Services | nom_stoxx_via_llista_seleccio (al PDF casa amb SE0000112385) | [fitxa](empreses/SE0021921269.md) |
| `SE0022060521` | Kinnevik AB Namn-Aktier B o.N. | Financial Services | nom_stoxx_via_llista_seleccio (al PDF casa amb SE0015810247) | [fitxa](empreses/SE0022060521.md) |
| `SE0022419784` | Sectra AB Namn-Aktier Ser.B o.N. | Health Care | nom_stoxx_via_llista_seleccio (al PDF casa amb SE0018245953) | [fitxa](empreses/SE0022419784.md) |

### 33 ISIN no estesos (tenen sector, però no font de juny 2023)

33 ISIN, 52 files 2024-2025, amb `any_font` anterior a 2023. No s'ha posat `any_font=2023` perquè no hi ha aquest PDF per a aquests ISIN. Queden `pendent_extensio_2024_2025` o `revisar_pendent_extensio_2024_2025`. El `supersector_fix` sí que recull el sector d'empresa.

| ISIN | Empresa | Anys | any_font | Estat | Fitxa |
|---|---|---|---|---|---|
| `AT0000606306` | Raiffeisen Bank Intl AG Inhaber-Aktien o.N. | 2024–2025 | 2021 | pendent_extensio_2024_2025 | [fitxa](empreses/AT0000606306.md) |
| `CH0038388911` | Sulzer AG Namens-Aktien SF -,01 | 2024–2025 | 2015 | pendent_extensio_2024_2025 | [fitxa](empreses/CH0038388911.md) |
| `DE0005773303` | Fraport AG Ffm.Airport.Ser.AG Inhaber- | 2025–2025 | 2019 | pendent_extensio_2024_2025 | [fitxa](empreses/DE0005773303.md) |
| `DE0005909006` | Bilfinger SE Inhaber-Aktien o.N. | 2025–2025 | 2016 | pendent_extensio_2024_2025 | [fitxa](empreses/DE0005909006.md) |
| `DE0006070006` | HOCHTIEF AG Inhaber-Aktien o.N. | 2024–2025 | 2019 | pendent_extensio_2024_2025 | [fitxa](empreses/DE0006070006.md) |
| `DE0008303504` | TAG Immobilien AG Inhaber-Aktien o.N. | 2024–2025 | 2021 | pendent_extensio_2024_2025 | [fitxa](empreses/DE0008303504.md) |
| `DE000A2LQ884` | AUTO1 Group SE Inhaber-Aktien o.N. | 2025–2025 | 2021 | pendent_extensio_2024_2025 | [fitxa](empreses/DE000A2LQ884.md) |
| `DK0010234467` | FLSmidth & Co. AS Navne-Aktier B DK 20 | 2024–2025 | 2018 | pendent_extensio_2024_2025 | [fitxa](empreses/DK0010234467.md) |
| `DK0015998017` | Bavarian Nordic Navne-Aktier DK 10 | 2024–2025 | 2022 | pendent_extensio_2024_2025 | [fitxa](empreses/DK0015998017.md) |
| `DK0061802139` | ALK-Abelló AS Navne-Aktier DK -,50 | 2024–2025 | 2022 | pendent_extensio_2024_2025 | [fitxa](empreses/DK0061802139.md) |
| `ES0124244E34` | Mapfre S.A. Acciones Nom. EO -,10 | 2025–2025 | 2019 | pendent_extensio_2024_2025 | [fitxa](empreses/ES0124244E34.md) |
| `FI0009005870` | Konecranes Oyj Registered Shares o.N. | 2024–2025 | 2019 | pendent_extensio_2024_2025 | [fitxa](empreses/FI0009005870.md) |
| `FR0013506730` | Vallourec S.A. Actions Port. EO 0,02 | 2024–2025 | 2015 | revisar_pendent_extensio_2024_2025 | [fitxa](empreses/FR0013506730.md) |
| `GB0002318888` | Cranswick PLC Registered Shares LS -,10 | 2024–2025 | 2020 | pendent_extensio_2024_2025 | [fitxa](empreses/GB0002318888.md) |
| `GB0009697037` | Babcock International Grp PLC Registered | 2025–2025 | 2018 | pendent_extensio_2024_2025 | [fitxa](empreses/GB0009697037.md) |
| `GB0031215220` | Carnival PLC Registered Shares DL 1,66 | 2025–2025 | 2021 | pendent_extensio_2024_2025 | [fitxa](empreses/GB0031215220.md) |
| `GB00B2QPKJ12` | Fresnillo PLC Registered Shares DL -,50 | 2025–2025 | 2017 | pendent_extensio_2024_2025 | [fitxa](empreses/GB00B2QPKJ12.md) |
| `GB00B62G9D36` | Shaftesbury Capital PLC Registered Shares | 2024–2025 | 2017 | pendent_extensio_2024_2025 | [fitxa](empreses/GB00B62G9D36.md) |
| `GB00B7KR2P84` | EasyJet PLC Registered Shares | 2024–2025 | 2019 | pendent_extensio_2024_2025 | [fitxa](empreses/GB00B7KR2P84.md) |
| `GB00BND88V85` | Bridgepoint Advisers Group PLC Registered | 2025–2025 | 2022 | pendent_extensio_2024_2025 | [fitxa](empreses/GB00BND88V85.md) |
| `GB00BYRJ5J14` | Primary Health Properties PLC Registered | 2025–2025 | 2022 | pendent_extensio_2024_2025 | [fitxa](empreses/GB00BYRJ5J14.md) |
| `IT0000784196` | Bca Pop. di Sondrio S.p.A. Azioni nom. EO 3 | 2024–2024 | 2015 | pendent_extensio_2024_2025 | [fitxa](empreses/IT0000784196.md) |
| `IT0004810054` | Unipol Gruppo S.p.A. Azioni nom. o. N. | 2024–2025 | 2016 | pendent_extensio_2024_2025 | [fitxa](empreses/IT0004810054.md) |
| `IT0005495657` | Saipem S.p.A. Azioni nom. o.N. | 2024–2025 | 2019 | revisar_pendent_extensio_2024_2025 | [fitxa](empreses/IT0005495657.md) |
| `JE00BMDZN391` | TP ICAP Group PLC Registered Shares LS | 2025–2025 | 2020 | revisar_pendent_extensio_2024_2025 | [fitxa](empreses/JE00BMDZN391.md) |
| `LU2290522684` | InPost S.A. Actions au Nomin. EO -,01 | 2024–2025 | 2021 | pendent_extensio_2024_2025 | [fitxa](empreses/LU2290522684.md) |
| `NL0000360618` | SBM Offshore N.V. Aandelen op naam EO | 2025–2025 | 2020 | pendent_extensio_2024_2025 | [fitxa](empreses/NL0000360618.md) |
| `NL0009432491` | Koninklijke Vopak N.V. Aandelen aan | 2025–2025 | 2021 | pendent_extensio_2024_2025 | [fitxa](empreses/NL0009432491.md) |
| `PLBZ00000044` | Santander Bank Polska S.A. Inhaber-Aktien | 2024–2025 | 2019 | pendent_extensio_2024_2025 | [fitxa](empreses/PLBZ00000044.md) |
| `PLOPTTC00011` | CD Projekt S.A. Inhaber-Aktien C ZY 1 | 2024–2025 | 2021 | pendent_extensio_2024_2025 | [fitxa](empreses/PLOPTTC00011.md) |
| `PTBCP0AM0015` | Banco Com. Português SA (BCP) Acç. Nom. | 2024–2025 | 2018 | pendent_extensio_2024_2025 | [fitxa](empreses/PTBCP0AM0015.md) |
| `SE0014504817` | Loomis AB Namn-Aktier Series o.N. | 2025–2025 | 2020 | pendent_extensio_2024_2025 | [fitxa](empreses/SE0014504817.md) |
| `SE0017780133` | Wallenstam AB Namn-Akt. Ser.B o.N. | 2024–2025 | 2022 | pendent_extensio_2024_2025 | [fitxa](empreses/SE0017780133.md) |

## Cites amb Wayback pendent (6)

| ISIN | Empresa | Anys | Cita | URL | Fitxa |
|---|---|---|---|---|---|
| `FI4000552526` | Mandatum OYJ Registered Shares o.N. | 2025 | «Life Insurance Sales Manager 1995–1999» | https://www.mandatum.fi/4a5b46/globalassets/konserni/mandatum/johto/johto---cvt/cv_petri_niemisvirta_en.pdf | [fitxa](empreses/FI4000552526.md) |
| `FI4000552526` | Mandatum OYJ Registered Shares o.N. | 2025 | «Born 1970» | https://www.mandatum.fi/4a5b46/globalassets/konserni/mandatum/johto/johto---cvt/cv_petri_niemisvirta_en.pdf | [fitxa](empreses/FI4000552526.md) |
| `FR0000184798` | Orpea Actions Port. EO 1,25 | 2016-2021 | «Co-fondateur du Groupe ORPEA» | https://www.emeis.com/sites/site_corporate/files/medias/documents/orpeaborchuredeconvocationag250614_0.pdf | [fitxa](empreses/FR0000184798.md) |
| `FR0000184798` | Orpea Actions Port. EO 1,25 | 2016-2021 | «Créé en 1989, ORPEA» | https://www.emeis.com/sites/site_corporate/files/medias/documents/cporpea30janvier2022fb5f8.pdf | [fitxa](empreses/FR0000184798.md) |
| `FR0000184798` | Orpea Actions Port. EO 1,25 | 2016-2021 | «Jean-Claude Marian, médecin neuropsychiatre, co-fondateur du Groupe ORPEA» | https://www.emeis.com/sites/default/files/medias/documents/orpeadocderef2013_0.pdf | [fitxa](empreses/FR0000184798.md) |
| `FR0000184798` | Orpea Actions Port. EO 1,25 | 2016-2021 | «1989 : création du Groupe ORPEA par le Docteur Jean-Claude Marian» | https://www.emeis.com/sites/default/files/medias/documents/orpeaddr2014vf_0.pdf | [fitxa](empreses/FR0000184798.md) |

## Tretze parelles sense documents i files E4

### Tretze parelles sense documents

L'informe de recuperació dels 440 documents (17/11/2026 22:07) recull: 179/195 parells tancats; **no es poden tancar 13 parells sense documents**. El recompte intern per classe d'aquella recuperació desagrega aquests 13 en **10 P + 3 NA**. [V] per al recompte.

La llista nominativa de les 13 parelles **no s'ha trobat** als fitxers localitzats. [NV] Si la llista no apareix, es regenerarà per script.

### Files amb incidència E4 a `sim_cert_detall` (15 files, 7 ISIN)

| ISIN | Empresa | Anys | Estat | Detall | Fitxa |
|---|---|---|---|---|---|
| `DE0006062144` | Covestro AG Inhaber-Aktien o.N. | 2018–2018 | no_certificada | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/DE0006062144.md) |
| `DE0008303504` | TAG Immobilien AG Inhaber-Aktien o.N. | 2021–2021 | no_certificada | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/DE0008303504.md) |
| `DK0010244508` | A.P.Møller-Mærsk A/​S Navne-Aktier B DK | 2016, 2018 | no_certificada | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/DK0010244508.md) |
| `FI4000552526` | Mandatum OYJ Registered Shares o.N. | 2025–2025 | no_certificada | Doctorat tanca l'etiqueta, pero r3e tenia incidences greus (E4,E6); no puja a N1/N2 | [fitxa](empreses/FI4000552526.md) |
| `FR0011594233` | SFR Group S.A. Actions Nom. EO 1 | 2016–2016 | no_certificada | Doctorat tanca l'etiqueta, pero r3e tenia incidences greus (E4); no puja a N1/N2 | [fitxa](empreses/FR0011594233.md) |
| `GB0005758098` | Meggitt PLC Registered Shares LS -,052) | 2016, 2018 | no_certificada | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/GB0005758098.md) |
| `NL0000008977` | Heineken Holding N.V. Aandelen aan toonder | 2016, 2018, 2021, 2022, 2023, 2024, 2025 | no_certificada | incidencia greu r3e (E4): no puja a N1/N2 | [fitxa](empreses/NL0000008977.md) |

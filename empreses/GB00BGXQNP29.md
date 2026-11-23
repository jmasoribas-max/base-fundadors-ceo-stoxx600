# Phoenix Group Holdings PLC Registered

- **ISIN:** `GB00BGXQNP29`
- **Nom al panell:** Phoenix Group Holdings PLC Registered
- **Anys al panell:** 2019–2025 (7 files)
- **Font de les dades:** `dades/base_isin_any_v8r3.csv` [V]

## Sector ICB

- **Supersector (aplicat als anys amb sector):** Insurance
- **Taxonomia:** ICB_2020
- **Supersector ICB anterior:** Insurance
- **Supersector ICB 2020:** Insurance
- **Any de la font:** 2023
- **Mètode de casament:** nom_exacte
- **URL de la font:** https://www.stoxx.com/document/Indices/Factsheets_Components/2023/June/SXXP.pdf
- **Wayback de la font:** — (no consta a la taula sectorial)
- **Estat a les files del panell:** `amb_sector`
- **Sector fix (`supersector_fix`):** Insurance
- **Extensió 2024-2025:** 2 files amb `sector_estes_des_2023=1` i `any_font=2023` (supersector del PDF de juny 2023). Per excloure-les en robustesa: `sector_estes_des_2023!=1`. Supòsit de no reclassificació 2023-2025: [NV].

## Sèrie anual

| Any | CEO | CEO aplicat | FounderCEO | Regla | Certificació | Nivell | Cites |
|---|---|---|---|---|---|---|---|
| 2019 | Clive Bannister | — (igual) | P | d | fora_mostra_auditoria | — | — |
| 2020 | Andy Briggs | — (igual) | P | d | certificada_ceo_pendent | N2 | CEO [1]; context [2]; marca `informe_exercici` |
| 2021 | Andy Briggs | — (igual) | P | d | certificada_ceo_pendent | N2 | CEO [1], [3]; marca `informe_exercici` |
| 2022 | Andy Briggs | — (igual) | P | d | certificada_ceo_pendent | N2 | CEO [4]; marca `informe_exercici` |
| 2023 | Andy Briggs | — (igual) | P | d | certificada_ceo_pendent | N2 | CEO [5]; marca `informe_exercici` |
| 2024 | Andy Briggs | — (igual) | P | d | certificada_ceo_pendent | N2 | CEO [6]; marca `informe_exercici` |
| 2025 | Andy Briggs | — (igual) | P | d | certificada_ceo_pendent | N2 | CEO [7]; context [8]; marca `informe_exercici` |

## Cites (URL original i Wayback)

No hi ha cites recollides al registre de canvis ni als camps `font_classificacio_cita` / `d37_cita_contemporania` d'aquesta empresa. [V] com a absència en aquests fitxers d'origen.

**Lot 2 (proposta de Claude Code, 19/11/2026; pendent del flux DF → Doctorat → Jordi): cites del CEO a 31/10.** Cada cita és literal del document obert a la URL original; el Wayback és el que retorna l'API de disponibilitat d'archive.org (la cita no s'ha pogut comprovar a la captura). `funció`: `ceo` = el fragment, per si sol, conté el nom de la persona i el càrrec de CEO o un equivalent legal, i és l'única que compta com a cita del CEO; `datacio` = només data un document o un fet; `context` = la resta (p. ex. registres que diuen «Director», dates sense el càrrec dins la cita, «has led», el càrrec sense la persona o el càrrec d'una altra persona). `allotjament`: on és el document obert (`emissor` = domini propi; `grup` = web d'una altra societat del grup; `successor`; `plataforma` = plataforma o CDN de tercers que allotja el document de l'emissor; `regulador` = regulador, registre oficial o borsa; `mitja`; `tercer` = document d'una altra entitat). Un document de l'emissor penjat fora del seu domini és A si és de l'emissor i la cita és literal. Marca de la fila: `informe_exercici` = cita del CEO de l'informe anual de l'exercici que inclou el 31/10/t, sense canvi documentat fins al tancament; `prova_interval` = sense aquesta cita, la fila es prova amb cites del CEO de documents contemporanis (dins l'exercici o fins a 4 mesos després del tancament) que acoten la data, o amb dates d'inici i fi del mandat; `prova_interval_retrospectiva` (sempre amb `prova_interval`) = cap cita del CEO contemporània: la fila descansa en documents posteriors amb dates explícites. La frase anterior («No hi ha cites recollides…») descriu els fitxers d'origen de la v8 r1 i no s'ha reescrit.

1. [V] «Andy Briggs joined the Board of Phoenix Group Holdings plc on 10 February 2020 as Group CEO Designate and became CEO on 10 March 2020.»  Anys: 2020-2021 · funció: `ceo` · allotjament: `grup` · nivell: A · URL: https://library.standardlife.co.uk/fy-20-annual-report-and-accounts.pdf · Wayback: https://web.archive.org/web/20260415204647/https://library.standardlife.co.uk/fy-20-annual-report-and-accounts.pdf (existent; cita no verificada a la captura) · id: `L2|GB00BGXQNP29|C1` · origen: proposta_claude_lot2 · prova: Data efectiva d'inici com a CEO: 10/03/2020 (abans del 31/10/2020).
2. [V] «Clive Bannister left the role of Group Chief Executive Officer on 10 March 2020 and left Phoenix Group on the same date.»  Anys: 2020 · funció: `context` · allotjament: `grup` · nivell: A · URL: https://library.standardlife.co.uk/fy-20-annual-report-and-accounts.pdf · Wayback: https://web.archive.org/web/20260415204647/https://library.standardlife.co.uk/fy-20-annual-report-and-accounts.pdf (existent; cita no verificada a la captura) · id: `L2|GB00BGXQNP29|C2` · origen: proposta_claude_lot2 · prova: El CEO anterior va deixar el càrrec el 10/03/2020. · per què `context`: Data de sortida del CEO anterior (Clive Bannister, 10/03/2020). No anomena el CEO de la fila (Briggs): «context», no compta com a cita del CEO. AR 2020 de l'emissor; l'script de comprovació literal OK. Mateix allotjament que C1 (grup).
3. [V] «Andy Briggs is Group Chief Executive Officer of the Company.»  Anys: 2021 · funció: `ceo` · allotjament: `grup` · nivell: A · URL: https://library.standardlife.co.uk/phoenix-group-full-year-results-2021.pdf · Wayback: https://web.archive.org/web/20260415190436/https://library.standardlife.co.uk/phoenix-group-full-year-results-2021.pdf (existent; cita no verificada a la captura) · id: `L2|GB00BGXQNP29|C3` · origen: proposta_claude_lot2 · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2021.
4. [V] «Andy Briggs is Group Chief Executive Officer (‘CEO’) of Phoenix.»  Anys: 2022 · funció: `ceo` · allotjament: `grup` · nivell: A · URL: https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2022.pdf · Wayback: https://web.archive.org/web/20260415192505/https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2022.pdf (existent; cita no verificada a la captura) · id: `L2|GB00BGXQNP29|C4` · origen: proposta_claude_lot2 · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2022.
5. [V] «Andy Briggs is the Group Chief Executive Officer (‘CEO’).»  Anys: 2023 · funció: `ceo` · allotjament: `grup` · nivell: A · URL: https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2023.pdf · Wayback: https://web.archive.org/web/20260303032752/https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2023.pdf (existent; cita no verificada a la captura) · id: `L2|GB00BGXQNP29|C5` · origen: proposta_claude_lot2 · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2023.
6. [V] «The Group’s Chief Executive Officer, Andy Briggs, is the Executive Board Director responsible for implementation»  Anys: 2024 · funció: `ceo` · allotjament: `emissor` · nivell: A · URL: https://library.standardlifeplc.com/phoenix_group_annual_report_and_accounts_2024.pdf · Wayback: `pendent_verificacio_externa` · id: `L2|GB00BGXQNP29|C6` · origen: proposta_claude_lot2 · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2024.
7. [V] «Andy Briggs, Group CEO, is responsible for embedding sustainability within»  Anys: 2025 · funció: `ceo` · allotjament: `grup` · nivell: A · URL: https://library.standardlife.co.uk/annual-report-and-accounts-2025-spread.pdf · Wayback: https://web.archive.org/web/20260719182559/https://library.standardlife.co.uk/annual-report-and-accounts-2025-spread.pdf (existent; cita no verificada a la captura) · id: `L2|GB00BGXQNP29|C7` · origen: proposta_claude_lot2 · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2025.
8. [V] «Clive Bannister left the role of Group CEO on 10 March 2020 and left the Group on the same date. Andy Briggs was appointed to the Board on 10 February 2020 and remained as CEO-designate until 10 March 2020.»  Anys: 2025 · funció: `context` · allotjament: `grup` · nivell: A · URL: https://library.standardlife.co.uk/annual-report-and-accounts-2025-spread.pdf · Wayback: https://web.archive.org/web/20260719182559/https://library.standardlife.co.uk/annual-report-and-accounts-2025-spread.pdf (existent; cita no verificada a la captura) · id: `L2|GB00BGXQNP29|C8` · origen: proposta_claude_lot2 · prova: Únic canvi de CEO documentat a la sèrie: 10/03/2020; l'informe 2025 no en registra cap altre. · per què `context`: Nota històrica de la taula de remuneració del CEO a l'AR 2025: el càrrec «Group CEO» s'atribueix a Bannister (predecessor) i Briggs hi surt només com a «CEO-designate until 10 March 2020»; el fragment no diu que Briggs sigui CEO. «Context», no compta com a cita del CEO. l'script de comprovació literal OK. Allotjament grup.

### Lot 7

- `L7-GB00BGXQNP29-C01` [V] (2019, `ceo`, `R1`, Nivell A). «Clive Bannister Group Chief Executive Officer» Pàgina 10 del PDF. Declaració del CEO en els comptes de l’exercici 2019. L’informe del 2020 situa la sortida el 10/03/2020. <https://library.standardlife.co.uk/annual-report-2019.pdf>
- `L7-GB00BGXQNP29-X01` [V] (2019, `context`, Nivell A). «Prior to its acquisition of the Resolution Group, OPB comprised four life assurance companies: Pearl Assurance, London Life, National Provident Life and NPI» Pàgina 108 del PDF. Història de les empreses asseguradores operatives que conformaven el grup abans de l’adquisició del 2008. <https://library.standardlife.co.uk/prospectus-2010.pdf>
- `L7-GB00BGXQNP29-X02` [V] (2019, `context`, Nivell A). «On 1 May 2008, Impala, a holding company incorporated within OPB, acquired the Resolution Group for a purchase price of £5.0 billion.» Pàgina 109 del PDF. Història de l’adquisició de Resolution a través d’Impala. <https://library.standardlife.co.uk/prospectus-2010.pdf>
- `L7-GB00BGXQNP29-X03` [V] (2019, `context`, Nivell A). «Liberty was formed as a non-operating Special Purpose Acquisition Company (“SPAC”) to acquire one or more operating businesses with principal activities outside of North America.» Pàgina 3 del PDF. Estructura anterior del grup. Liberty va passar a ser la matriu de les empreses operatives de Pearl el 02/09/2009. <https://library.standardlife.co.uk/phoenix-ar-2009.pdf>
- `L7-GB00BGXQNP29-X04` [V] (2019, `context`, Nivell A). «in early 2018 to approve the acquisition of Standard Life Assurance.» Pàgina 93 del PDF. Informe de govern corporatiu. L’operació amb Standard Life Assurance consta com una adquisició. <https://library.standardlife.co.uk/annual-report-2019.pdf>
- `L7-GB00BGXQNP29-X05` [V] (2019, `context`, Nivell A). «The scheme of arrangement had the effect of the Company being inserted above Old PGH in the Group legal entity organisational structure and constituted a group reconstruction.» Pàgina 156 del PDF. Nota 1, Basis of preparation. La nova societat de cartera del 12/12/2018 té continuïtat operativa amb el grup anterior (P1). <https://library.standardlife.co.uk/annual-report-2019.pdf>
- `L7-GB00BGXQNP29-F01` [V] (2019, `fundador`, `d`, Nivell A). «Prior to this, Mr Bannister was Group Managing Director of Insurance and Asset Management at HSBC Holdings plc.» Pàgina 80 del PDF. Perfil al consell. La frase anterior data la incorporació a Phoenix el febrer del 2011. HSBC Holdings és l’ocupador anterior. <https://library.standardlife.co.uk/annual-report-2019.pdf>

## Canvis del registre

Aquesta empresa no té entrades al registre de canvis de la v8 r1 (el registre cobreix els canvis documentats amb cita, no totes les files del panell).

Proposta posterior (lot 2, pendent del flux):

| Anys | De | A | Decisió / origen | Certificació al registre |
|---|---|---|---|---|
| 2020-2025 | Andy Briggs (CEO) | Andy Briggs (CEO, sense canvi) | lot2:cita_ceo_31_10_sense_canvi / proposta_claude_lot2 | certificada_ceo_pendent/N2 (sense canvi; pendent del flux) |

## Pendències d'aquesta empresa

- 2020: `certificada_ceo_pendent` / `N2` — r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada)
- 2021: `certificada_ceo_pendent` / `N2` — r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada)
- 2022: `certificada_ceo_pendent` / `N2` — r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada)
- 2023: `certificada_ceo_pendent` / `N2` — r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada)
- 2024: `certificada_ceo_pendent` / `N2` — r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada)
- 2025: `certificada_ceo_pendent` / `N2` — r3e certificada_ceo_pendent N2; CEO a 31/10 continua ChatGPT=NV / Claude=NV (o la cita del CEO no esta verificada)
- **Lot 2 (proposta de Claude Code, 19/11/2026; pendent del flux DF → Doctorat → Jordi)** — 2020-2025: CEO a 31/10 Andy Briggs; 8 cites incorporades ([1]–[8]), de les quals 6 són cites del CEO (`ceo`) i 2 de datació o context. El CEO de la base no canvia i tampoc l'etiqueta FounderCEO. La fila continua `certificada_ceo_pendent` fins que el flux la validi; cap columna de robustesa ni de certificació s'ha tocat.
  - 2020: cites del CEO [1]; context [2]; marca: `informe_exercici`. C1 és una cita «ceo» de l'AR 2020 (exercici natural que inclou el 31/10/2020): Briggs és CEO des del 10/03/2020. La llista del Directors' Report de l'AR 2020 («During 2020 and up to the date of this Directors’ Report...») només recull, pel que fa al CEO, la sortida de Bannister (10/03/2020) i l'entrada de Briggs al consell com a «Group Chief Executive» (10/02/2020). Cap canvi de CEO entre el 31/10/2020 i el tancament. Sense marca. C2 queda com a context.
  - 2021: cites del CEO [1], [3]; marca: `informe_exercici`. C3 és una cita «ceo» de l'AR 2021 (exercici natural que inclou el 31/10/2021). L'únic canvi de consell durant el 2021 i fins a la data del Directors' Report és la dimissió de Christopher Minter (conseller nominat per Swiss Re, 25/06/2021). Cap canvi de CEO. C1 (AR 2020, inici del mandat el 10/03/2020) és una cita «ceo» de suport. Sense marca.
  - 2022: cites del CEO [4]; marca: `informe_exercici`. C4 és una cita «ceo» de l'AR 2022 (exercici natural que inclou el 31/10/2022). Els canvis de consell del 2022 (Murray, Semple, Tumilty, Bruce, sabàtic de Lyons, Barbour Chair, Mayall) no afecten el CEO. Sense marca.
  - 2023: cites del CEO [5]; marca: `informe_exercici`. C5 és una cita «ceo» de l'AR 2023 (exercici natural que inclou el 31/10/2023). Els canvis de consell del 2023 (Gregory, Bruce, Scott, Sorenson, Lyons, Barbour, Bucks) no afecten el CEO. Sense marca.
  - 2024: cites del CEO [6]; marca: `informe_exercici`. C6 és una cita «ceo» de l'AR 2024 (exercici natural que inclou el 31/10/2024). Els canvis del 2024 són la sortida del CFO Thakrar (8/9/2024), l'entrada de Nicandrou (2/12/2024), la retirada de Pollock (31/12/2024) i l'entrada prevista de Coutu (1/5/2025). Cap canvi de CEO. Sense marca. C6 no té Wayback (pendent_verificacio_externa).
  - 2025: cites del CEO [7]; context [8]; marca: `informe_exercici`. C7 és una cita «ceo» de l'AR 2025 de Standard Life plc (antiga Phoenix Group Holdings plc; exercici natural que inclou el 31/10/2025). La llista «During 2025, and up to the date of this Directors’ report» només recull consellers (Coutu, Shott, Richards, Cook, Scott, Boylan). Cap canvi de CEO. Sense marca. C8 queda com a context.
  - Què s'ha buscat i on (primera recerca): Web oficial de l'emissor (ara Standard Life plc, 'Formerly Phoenix Group Holdings plc'): https://www.standardlifeplc.com/investors/results-reports-and-presentations (200, redirigeix a /results-reports-presentations), d'on surten els enllaços als PDF de library.standardlife.co.uk i library.standardlifeplc.com. Baixats amb 200 els informes anuals 2020, 2021, 2022, 2023, 2024 i 2025 (URL a les cites). https://www.thephoenixgroup.com/investor-relations/results-reports-and-presentations/ redirigeix a https://www.standardlifeplc.com/. L'informe 2021 no és a l'URL conjecturada https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2021.pdf (404, igual que altres 10 variants de nom provades); el fitxer correcte és phoenix-group-full-year-results-2021.pdf (portada 'Annual Report and Accounts 2021'). També baixat https://library.standardlife.co.uk/phoenix-group-fy21-rns.pdf (200), no usat com a cita. Totes les cites comprovades amb l'script de comprovació literal (OK).
  - Correspondència entre els ids de treball (els que surten als dubtes) i la numeració d'aquesta fitxa: C1 = [1], C2 = [2], C3 = [3], C4 = [4], C5 = [5], C6 = [6], C7 = [7], C8 = [8].
  - Dubtes de la primera recerca que continuen oberts (per a Doctorat; no decidits): (1) L'emissor va canviar de nom a Standard Life plc (l'informe 2025 diu 'Formerly Phoenix Group Holdings plc'); el nom al panell continua sent Phoenix Group Holdings.
  - Observacions i dubtes de la verificació independent d'aquesta versió (19/11/2026; per a DF i Doctorat; no decidits): (1) Desacord sobre l'allotjament amb la primera classificació. C1-C5, C7 i C8 són a library.standardlife.co.uk. El web standardlife.co.uk (baixat el 19/11/2026) diu «© 2026 Phoenix Group Management Services Limited» i que descriu productes de «Phoenix Life Limited, trading as Standard Life»; totes dues són filials de l'emissor. El domini corporatiu de l'emissor és standardlifeplc.com («© 2026 Standard Life plc»), que enllaça aquests PDF des de la pàgina de resultats. Per això els classifico com a «grup» i no com a «emissor». C6, a library.standardlifeplc.com (subdomini del domini corporatiu), queda com a «emissor». El nivell és A en tots els casos: són informes anuals de l'emissor i les cites són literals. Si Doctorat considera que la biblioteca compartida compta com a domini propi, cal tornar a «emissor». · (2) C6 (AR 2024, library.standardlifeplc.com) no té URL Wayback a la primera versió del PR #3. No he consultat archive.org perquè web.archive.org no era accessible des de la sessió, així que queda com a pendent_verificacio_externa. Per la mateixa raó tampoc he pogut comprovar les URL Wayback declarades de C1-C5, C7 i C8. · (3) Hi estic d'acord: C2 i C8 són «context». C2 anomena només Bannister. C8 atribueix «Group CEO» a Bannister i a Briggs només el títol «CEO-designate». Les files 2020 i 2025 conserven una cita «ceo» de l'informe de l'exercici (C1 i C7). · (4) Qüestió de metodologia per a Doctorat: les frases dels AR 2021-2025 (C3-C7) estan en present i parlen del moment de la publicació (març de t+1). Les he tractat com a cita «ceo» de l'informe de l'exercici que inclou el 31/10/t, sense marca, perquè les llistes de canvis del consell (fins a la data del Directors' Report) no registren cap canvi de CEO. C1 (AR 2020) no és en present, sinó la data d'inici («became CEO on 10 March 2020»), i el mateix informe no registra cap canvi posterior. · (5) L'AR 2025 parla del «role as Dual CEO» d'Andy Briggs (CEO del grup i de les Life Companies). No afecta el càrrec de Group CEO, però en deixo constància. · (6) No hi ha cites noves ni supressions.

Índex: [INDEX.md](../INDEX.md) · Base: [dades/base_isin_any_v8r3.csv](../dades/base_isin_any_v8r3.csv)

## Lot 9 · CEO i fundador

| Any | CEO a 31/10 | Classificació | Estat de la prova |
|---:|---|---|---|
| 2020 | `L9-GB00BGXQNP29-C01` | `L9-GB00BGXQNP29-F01` | Feta |
| 2021 | `L9-GB00BGXQNP29-C02` | `L9-GB00BGXQNP29-F01` | Feta |
| 2022 | `L9-GB00BGXQNP29-C03` | `L9-GB00BGXQNP29-F01` | Feta |
| 2023 | `L9-GB00BGXQNP29-C04` | `L9-GB00BGXQNP29-F01` | Feta |
| 2024 | `L2\|GB00BGXQNP29\|C6` | `L9-GB00BGXQNP29-F01` | Feta |
| 2025 | `L9-GB00BGXQNP29-C05` | `L9-GB00BGXQNP29-F01` | Feta |

### Cites del lot

- **L9-GB00BGXQNP29-C01** (2020, [V], ceo, R1). «Andy Briggs joined the Board of Phoenix Group Holdings plc on 10 February 2020 as Group CEO Designate and became CEO on 10 March 2020.» Nivell A. Informe anual de l’exercici 2020 al domini de la cotitzada. PDF complet idèntic a la còpia del grup de L2|GB00BGXQNP29|C1. Phoenix Group Holdings plc va adoptar la denominació Standard Life plc el 24/02/2026. Pàgina 132 del PDF. <https://library.standardlifeplc.com/fy-20-annual-report-and-accounts.pdf>
- **L9-GB00BGXQNP29-C02** (2021, [V], ceo, R1). «Andy Briggs is Group Chief Executive Officer of the Company.» Nivell A. Informe anual de l’exercici 2021 al domini de la cotitzada. PDF complet idèntic a la còpia del grup de L2|GB00BGXQNP29|C3. Phoenix Group Holdings plc va adoptar la denominació Standard Life plc el 24/02/2026. Pàgina 92 del PDF. <https://library.standardlifeplc.com/phoenix-group-full-year-results-2021.pdf>
- **L9-GB00BGXQNP29-C03** (2022, [V], ceo, R1). «Andy Briggs is Group Chief Executive Officer (‘CEO’) of Phoenix.» Nivell A. Informe anual de l’exercici 2022 al domini de la cotitzada. PDF complet idèntic a la còpia del grup de L2|GB00BGXQNP29|C4. Phoenix Group Holdings plc va adoptar la denominació Standard Life plc el 24/02/2026. Pàgina 84 del PDF. <https://library.standardlifeplc.com/phoenix-group-annual-report-and-accounts-2022.pdf>
- **L9-GB00BGXQNP29-C04** (2023, [V], ceo, R1). «Andy Briggs is the Group Chief Executive Officer (‘CEO’).» Nivell A. Informe anual de l’exercici 2023 al domini de la cotitzada. PDF complet idèntic a la còpia del grup de L2|GB00BGXQNP29|C5. Phoenix Group Holdings plc va adoptar la denominació Standard Life plc el 24/02/2026. Pàgina 71 del PDF. <https://library.standardlifeplc.com/phoenix-group-annual-report-and-accounts-2023.pdf>
- **L9-GB00BGXQNP29-C05** (2025, [V], ceo, R1). «Andy Briggs, Group CEO, is responsible for embedding sustainability within the Group, in line with the strategy set by the Group Board.» Nivell A. Informe anual de l’exercici 2025 al domini de la cotitzada. PDF complet idèntic a la còpia del grup de L2|GB00BGXQNP29|C7. Phoenix Group Holdings plc va adoptar la denominació Standard Life plc el 24/02/2026. Pàgina 40 del PDF. <https://library.standardlifeplc.com/annual-report-and-accounts-2025-spread.pdf>
- **L9-GB00BGXQNP29-F01** (2020-2025, [V], fundador, d). «Andy joined Phoenix Group in 2020 with over 30 years of experience in the insurance industry. He has held senior executive roles across multiple business areas in the industry including CEO of UK Insurance and Global Life and Health at Aviva plc; CEO of Friends Life Group Limited; Managing Director of Scottish Widows; CEO of the Retirement Income Division at Prudential plc and Chair of the Association of British Insurers (‘ABI’).» Nivell A. Informe anual 2023, biografia d’Andy Briggs, Career and experience. Va entrar al grup el 2020 després de treballar a Aviva. L’historial corporatiu documenta el nom Phoenix Group Holdings ja el 2010. Pàgina 66 del PDF. <https://library.standardlifeplc.com/phoenix-group-annual-report-and-accounts-2023.pdf>
- **L9-GB00BGXQNP29-X01** (2020-2025, [V], context). «2010 Pearl Group changes its name to Phoenix Group Holdings» Nivell A. Our history, Key milestones, 2010s. El grup operava amb el nom Phoenix deu anys abans de l’entrada de Briggs. La mateixa cronologia identifica l’adquisició de Standard Life Assurance el 2018 i de ReAssure el 2020. Consulta del document complet el 23/11/2026. <https://www.standardlifeplc.com/about/our-history>

### Revisió del registre anterior

| Entrada | Estat de lectura | Pàgina, secció o incidència |
|---|---|---|
| `L2\|GB00BGXQNP29\|C1` | [V] | PDF complet, pàgina 132 del PDF. |
| `L2\|GB00BGXQNP29\|C2` | [V] | PDF complet, pàgina 147 del PDF. |
| `L2\|GB00BGXQNP29\|C3` | [V] | PDF complet, pàgina 92 del PDF. |
| `L2\|GB00BGXQNP29\|C4` | [V] | PDF complet, pàgina 84 del PDF. |
| `L2\|GB00BGXQNP29\|C5` | [V] | PDF complet, pàgina 71 del PDF. |
| `L2\|GB00BGXQNP29\|C6` | [V] | PDF complet, pàgina 56 del PDF. |
| `L2\|GB00BGXQNP29\|C7` | [V] | PDF complet, pàgina 40 del PDF. |
| `L2\|GB00BGXQNP29\|C8` | [V] | PDF complet, pàgina 87 del PDF. |

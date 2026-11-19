# Registre de canvis

Data d'aquest arbre: 19/11/2026 10:12 (CET, Europe/Madrid). Base: `dades/base_isin_any_v8r3.csv` SHA `1b7df913b31300857cbc77332a9aa03626edc0013f3bbb1e8625aa456ee38d4c` [V].

La v8 r3 **no afegeix canvis d'etiqueta FounderCEO**. El registre que segueix és el de la v8 r1 (cites amb URL original i Wayback). La v8 r3 aplica l'extensió del supersector de juny 2023 als anys 2024-2025 per als ISIN que ja el tenien (`sector_estes_des_2023=1`) i afegeix `supersector_fix`; no canvia cap etiqueta FounderCEO. Qualsevol canvi futur de dades s'ha d'afegir aquí amb cita literal, URL i Wayback, en una branca i via PR.

Proposta posterior, pendent del flux (DF, Doctorat, Jordi): vegeu més avall «Lot ND-1 (proposta de Claude Code)».

Proposta posterior, pendent del flux (DF, Doctorat, Jordi): vegeu al final «Lot 2 (proposta de Claude Code): cites del CEO a 31/10».

---

# Registre de canvis v8 r1

Data: 19/11/2026 09:31 (CET, Europe/Madrid). Base: `base_isin_any_v8r1.csv` (panell, 6.012 files ISIN-any).
Els canvis d'etiqueta i de CEO s'hereten de la simulació v2 (validada per Doctorat) i s'apliquen a la v8.
Les cites i els URL s'han recollit de fonts ja presents al box (paquet r4, texts del paquet, `fonts_v75r2.csv`, manifests de verificació web r4). No s'ha inventat cap cita ni cap hash. El que no s'ha pogut recuperar es marca [NV].
El camp `ceos` de la base no s'ha sobreescrit; el CEO aplicat és a `sim_ceo_aplicat`.

## 1. Canvis d'etiqueta (35 files, 11 grups)

| # | ISIN | Empresa | Anys (n) | v75r2 → v8 | Decisió | Certificació |
|---|---|---|---|---|---|---|
| 1 | `BE0974293251` | Anheuser-Busch InBev S.A./​N.V. Actions au | 2021-2025 (5) | ND → P | previa:C0417 | certificada N2 (2021, 2022); certificada N1 (2023, 2024, 2025) |
| 2 | `ES0105066007` | Cellnex Telecom S.A. Acciones Port. EO -,25 | 2016-2022 (7) | P → F | previa:C0220 | certificada doctorat (2016, 2017, 2018, 2019, 2020, 2021, 2022) |
| 3 | `ES0180907000` | Unicaja Banco S.A. Acciones Nom. EO 0,25 | 2025 (1) | ND → P | 6_unicaja | certificada N2 (2025) |
| 4 | `FI4000552526` | Mandatum OYJ Registered Shares o.N. | 2025 (1) | ND → P | previa:C0180 | no_certificada (2025) |
| 5 | `FR0000184798` | Orpea Actions Port. EO 1,25 | 2016-2021 (6) | ND → P | 2_orpea | certificada doctorat (2016, 2017, 2018, 2019, 2020, 2021) |
| 6 | `FR0011594233` | SFR Group S.A. Actions Nom. EO 1 | 2016 (1) | ND → P | previa:C0302 | no_certificada (2016) |
| 7 | `GB0009633180` | Dechra Pharmaceuticals PLC Registered | 2018-2023 (6) | ND → P | previa:C0369 | certificada_ceo_pendent N1 (2018, 2019, 2020, 2021, 2022, 2023) |
| 8 | `GB00B8HX8Z88` | Mediclinic International PLC Registered | 2016-2017 (2) | ND → P | 4_mediclinic | certificada N2 (2016, 2017) |
| 9 | `GB00BMBVGQ36` | Harbour Energy PLC Registered Shares LS | 2022-2023 (2) | F → P | previa:C0241 | certificada doctorat (2022, 2023) |
| 10 | `PLOPTTC00011` | CD Projekt S.A. Inhaber-Aktien C ZY 1 | 2023 (1) | ND → P | 1_cd_projekt_2023 | certificada N1 (2023) |
| 11 | `SE0000242455` | Swedbank AB Namn-Aktier A o.N. | 2016-2018 (3) | ND → P | 5_swedbank_e | certificada N2 (2016, 2017, 2018) |

Detall per grup, amb cita i URL:

### 1.1 Anheuser-Busch InBev S.A./​N.V. Actions au (`BE0974293251`)

- Canvi: **ND → P** als anys 2021-2025 (n=5).
- Origen: `decisio_doctorat` · decisió: `previa:C0417`.
- Nota de la simulació: ['AB InBev: ND passa a 0, regla b (Doctorat, ja tancada)', 'AB InBev: ND passa a 0, regla b (Doctorat, ja tancada)', 'AB InBev: ND passa a 0, regla b (Doctorat, ja tancada)', 'AB InBev: ND passa a 0, regla b (Doctorat, ja tancada)', 'AB InBev: ND passa a 0, regla b (Doctorat, ja tancada)']
- Cites:

1. [V] «Doukeris joined AB InBev in 1996»
   URL: https://www.ab-inbev.com/our-leaders-michel-doukeris · Wayback: https://web.archive.org/web/20260921125458/https://www.ab-inbev.com/our-leaders-michel-doukeris · id: `D0456` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4 que sustenten la regla b (entrada 1996 / naixement 1973 / fundació o fusió precedente).
2. [V] «Brasserie Piedboeuf SA, founded in 1853»
   URL: https://www.sec.gov/Archives/edgar/data/1140467/000119312514112577/d692738d20f.htm · Wayback: https://web.archive.org/web/20160531105701/http://www.sec.gov:80/Archives/edgar/data/1140467/000119312514112577/d692738d20f.htm (existent; cita verificada a la captura) · id: `D0377` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4 que sustenten la regla b (entrada 1996 / naixement 1973 / fundació o fusió precedente).
3. [V] «Interbrew and AmBev merge to create InBev.»
   URL: https://www.ab-inbev.com/about-us/our-heritage · Wayback: https://web.archive.org/web/20260719173341/https://www.ab-inbev.com/about-us/our-heritage (existent; cita verificada a la captura) · id: `D0218` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4 que sustenten la regla b (entrada 1996 / naixement 1973 / fundació o fusió precedente).
4. [V] «Born in 1973»
   URL: https://www.ab-inbev.com/our-leaders-michel-doukeris · Wayback: https://web.archive.org/web/20260921125458/https://www.ab-inbev.com/our-leaders-michel-doukeris · id: `D0456` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4 que sustenten la regla b (entrada 1996 / naixement 1973 / fundació o fusió precedente).
5. [V] «Interbrew and AmBev merge to create InBev.»
   URL: https://www.ab-inbev.com/about-us/our-heritage · Wayback: https://web.archive.org/web/20260719173341/https://www.ab-inbev.com/about-us/our-heritage · id: `D0416` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4 que sustenten la regla b (entrada 1996 / naixement 1973 / fundació o fusió precedente).


### 1.2 Cellnex Telecom S.A. Acciones Port. EO -,25 (`ES0105066007`)

- Canvi: **P → F** als anys 2016-2022 (n=7).
- Origen: `decisio_doctorat` · decisió: `previa:C0220`.
- Nota de la simulació: ['Cellnex: P passa a 1, D37 i 2.4 (Doctorat, ja tancada)', 'Cellnex: P passa a 1, D37 i 2.4 (Doctorat, ja tancada)', 'Cellnex: P passa a 1, D37 i 2.4 (Doctorat, ja tancada)', 'Cellnex: P passa a 1, D37 i 2.4 (Doctorat, ja tancada)', 'Cellnex: P passa a 1, D37 i 2.4 (Doctorat, ja tancada)', 'Cellnex: P passa a 1, D37 i 2.4 (Doctorat, ja tancada)', 'Cellnex: P passa a 1, D37 i 2.4 (Doctorat, ja tancada)']
- Cites:

1. [V] «Tobias Martinez, CEO fundador de Cellnex, dejará su cargo el 3 de junio tras liderar la empresa durante ocho años»
   URL: https://www.cellnex.com/es/noticias/marco-patuano-sucedera-tobias-martinez-consejero-delegado-partir-4-junio/ · Wayback: https://web.archive.org/web/20251210053003/https://www.cellnex.com/es/noticias/marco-patuano-sucedera-tobias-martinez-consejero-delegado-partir-4-junio/ · id: `D0543` · origen: textos_paquet_r4
   Nota: Comprovat literalment al text de D0543 del paquet r4 (i al REGISTRE_CASOS_DOCTORAT_r4.md). Comunicat de 28/4/2023 (retrospectiu respecte als anys 2016-2022).


### 1.3 Unicaja Banco S.A. Acciones Nom. EO 0,25 (`ES0180907000`)

- Canvi: **ND → P** als anys 2025 (n=1).
- Origen: `decisio_doctorat_r4` · decisió: `6_unicaja`.
- Nota de la simulació: ["Doctorat 6: Unicaja 2025 ND->0 (regla e). Cites d'origen i de CEO verificades."]
- Cites:

1. [V] «los actuales accionistas de Unicaja Banco contarán con el 59,5% del capital»
   URL: https://www.unicajabanco.com/es/sala-de-comunicacion/buscador-noticias/2021/03/las-juntas-de-accionistas-de-unicaja-banco-y-liberbank-aprueban- · Wayback: https://web.archive.org/web/20260520225418/https://www.unicajabanco.com/es/sala-de-comunicacion/buscador-noticias/2021/03/las-juntas-de-accionistas-de-unicaja-banco-y-liberbank-aprueban- (existent; cita verificada a la captura) · id: `D0922` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4 sobre l'origen (1991 / caixes predecessores / fusió Liberbank) i l'entrada del CEO.
2. [V] «Creation of Caja de Ahorros y Monte de Piedad de Cádiz.»
   URL: https://www.unicajabanco.com/content/dam/unicaja/unicaja-corporacion/documentos-corporacion/inversores-y-accionistas/presentacion-corporativa-tercer-trimestre-2017-en.pdf · Wayback: https://web.archive.org/web/20251115054852/https://www.unicajabanco.com/content/dam/unicaja/unicaja-corporacion/documentos-corporacion/inversores-y-accionistas/presentacion-corporativa-tercer-trimestre-2017-en.pdf (existent; cita verificada a la captura) · id: `D1129` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4 sobre l'origen (1991 / caixes predecessores / fusió Liberbank) i l'entrada del CEO.
3. [V] «La caja de ahorros Unicaja nació en marzo de 1991»
   URL: https://www.unicajabanco.com/es/institucional · Wayback: https://web.archive.org/web/20261031122721/https://www.unicajabanco.com/es/institucional · id: `D0633` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4 sobre l'origen (1991 / caixes predecessores / fusió Liberbank) i l'entrada del CEO.
4. [V] «several technical positions from April 1990 to August 2005»
   URL: https://www.unicajabanco.com/content/dam/unicaja/unicaja-corporacion/documentos-corporacion/emisiones/Folleto_Informativo_Salida_Bolsa-en.pdf · Wayback: https://web.archive.org/web/20240804122948/https://www.unicajabanco.com/content/dam/unicaja/unicaja-corporacion/documentos-corporacion/emisiones/Folleto_Informativo_Salida_Bolsa-en.pdf (existent; cita verificada a la captura) · id: `D1048` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4 sobre l'origen (1991 / caixes predecessores / fusió Liberbank) i l'entrada del CEO.


### 1.4 Mandatum OYJ Registered Shares o.N. (`FI4000552526`)

- Canvi: **ND → P** als anys 2025 (n=1).
- Origen: `decisio_doctorat` · decisió: `previa:C0180`.
- Nota de la simulació: ['Mandatum 2025: ND passa a 0, regla e (Doctorat, ja tancada)']
- Cites:

1. [V] «Life Insurance Sales Manager 1995–1999»
   URL: https://www.mandatum.fi/4a5b46/globalassets/konserni/mandatum/johto/johto---cvt/cv_petri_niemisvirta_en.pdf · Wayback: pendent_verificacio_externa · id: `X11|B|B|FI4000552526|persona:Petri Niemisvirta/incorporacio/evidencia|2b4a0087bfdc` · origen: fonts_v75r2
   Nota: tipus=primaria_empresa estat_document=pendent_verificacio_externa
2. [V] «Born 1970»
   URL: https://www.mandatum.fi/4a5b46/globalassets/konserni/mandatum/johto/johto---cvt/cv_petri_niemisvirta_en.pdf · Wayback: pendent_verificacio_externa · id: `X11|B|B|FI4000552526|persona:Petri Niemisvirta/naixement/evidencia|118ce92ff799` · origen: fonts_v75r2
   Nota: tipus=primaria_empresa estat_document=pendent_verificacio_externa
3. [V] «1996: Sampo Life Insurance Company Limited was established.»
   URL: https://www.mandatum.fi/en/group/about-the-company/history/ · Wayback: https://web.archive.org/web/20260421173658/https://www.mandatum.fi/en/group/about-the-company/history/ (existent; cita verificada a la captura) · id: `X11|B|B|FI4000552526|empresa/fundacio/entitats/evidencia|484cfeff8867` · origen: fonts_v75r2
   Nota: tipus=primaria_empresa estat_document=pendent_verificacio_externa
4. [V] «Sampo was founded in Finland in 1909»
   URL: https://www.sampo.com/globalassets/investors/debt-instruments-and-ratings/documents/2025/sampo-emtn-2025---base-prospectus-dated-on-3-december-2025.pdf · Wayback: https://web.archive.org/web/20260416055221/https://www.sampo.com/globalassets/investors/debt-instruments-and-ratings/documents/2025/sampo-emtn-2025---base-prospectus-dated-on-3-december-2025.pdf (existent; cita verificada a la captura) · id: `X11|B|B|FI4000552526|empresa/fundacio/entitats/evidencia|2088f89c23a1` · origen: fonts_v75r2
   Nota: tipus=primaria_empresa estat_document=pendent_verificacio_externa


### 1.5 Orpea Actions Port. EO 1,25 (`FR0000184798`)

- Canvi: **ND → P** als anys 2016-2021 (n=6).
- Origen: `decisio_doctorat_r4` · decisió: `2_orpea`.
- Nota de la simulació: ['Doctorat 2: Orpea ND->0. Cita verificada presenta Marian com a fundador unic (founded by / creation ... par), no com a co-fondateur.', 'Doctorat 2: Orpea ND->0. Cita verificada presenta Marian com a fundador unic (founded by / creation ... par), no com a co-fondateur.', 'Doctorat 2: Orpea ND->0. Cita verificada presenta Marian com a fundador unic (founded by / creation ... par), no com a co-fondateur.', 'Doctorat 2: Orpea ND->0. Cita verificada presenta Marian com a fundador unic (founded by / creation ... par), no com a co-fondateur.', 'Doctorat 2: Orpea ND->0. Cita verificada presenta Marian com a fundador unic (founded by / creation ... par), no com a co-fondateur.', 'Doctorat 2: Orpea ND->0. Cita verificada presenta Marian com a fundador unic (founded by / creation ... par), no com a co-fondateur.']
- Cites:

1. [V] «1989 • Création du groupe ORPEA, par le docteur Jean-Claude Marian, neuropsychiatre»
   URL: https://filings.xbrl.org/969500LHIH3NT7PK1V89/2021-12-31/ESEF/FR/0/969500LHIH3NT7PK1V89-2021-12-31-fr/reports/969500LHIH3NT7PK1V89-2021-12-31-fr.xhtml · Wayback: https://web.archive.org/web/20261119080031/https://filings.xbrl.org/969500LHIH3NT7PK1V89/2021-12-31/ESEF/FR/0/969500LHIH3NT7PK1V89-2021-12-31-fr/reports/969500LHIH3NT7PK1V89-2021-12-31-fr.xhtml (nova; cita verificada a la captura) · id: `R0784|4f87ed142720` · origen: verificacio_web_r4_claude · model: Claude
   Nota: estat=verificada cita_trobada=literal font_baixada=oficial timestamp=
2. [V] «Co-fondateur du Groupe ORPEA»
   URL: https://www.emeis.com/sites/site_corporate/files/medias/documents/orpeaborchuredeconvocationag250614_0.pdf · Wayback: pendent_verificacio_externa · id: `D0763` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4 sobre la creació (1989, Marian) i la fórmula «co-fondateur» present en altres documents del paquet.
3. [V] «Créé en 1989, ORPEA»
   URL: https://www.emeis.com/sites/site_corporate/files/medias/documents/cporpea30janvier2022fb5f8.pdf · Wayback: pendent_verificacio_externa · id: `D0138` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4 sobre la creació (1989, Marian) i la fórmula «co-fondateur» present en altres documents del paquet.
4. [V] «Jean-Claude Marian, médecin neuropsychiatre, co-fondateur du Groupe ORPEA»
   URL: https://www.emeis.com/sites/default/files/medias/documents/orpeadocderef2013_0.pdf · Wayback: pendent_verificacio_externa · id: `D0790` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4 sobre la creació (1989, Marian) i la fórmula «co-fondateur» present en altres documents del paquet.
5. [V] «1989 : création du Groupe ORPEA par le Docteur Jean-Claude Marian»
   URL: https://www.emeis.com/sites/default/files/medias/documents/orpeaddr2014vf_0.pdf · Wayback: pendent_verificacio_externa · id: `D0311` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4 sobre la creació (1989, Marian) i la fórmula «co-fondateur» present en altres documents del paquet.


### 1.6 SFR Group S.A. Actions Nom. EO 1 (`FR0011594233`)

- Canvi: **ND → P** als anys 2016 (n=1).
- Origen: `decisio_doctorat` · decisió: `previa:C0302`.
- Nota de la simulació: ['SFR 2016: ND passa a 0, regla e (Doctorat, ja tancada)']
- Cites:

1. [V] «since September 2015 to November 2017. […] Prior to his tenure at Altice, Mr. Combes served as Chief Executive Officer of Alcatel-Lucent»
   URL: https://www.sec.gov/Archives/edgar/data/101830/000010183018000003/form8-k20180102.htm · Wayback: https://web.archive.org/web/20261119081609/https://www.sec.gov/Archives/edgar/data/101830/000010183018000003/form8-k20180102.htm (nova; cita verificada a la captura) · id: `X11|B|B|FR0011594233|persona:Michel Combes/incorporacio/evidencia|e778f402185c` · origen: fonts_v75r2
   Nota: tipus=altra estat_document=pendent_verificacio_externa
2. [V] «En 1987, la Compagnie Générale des Eaux crée SFR»
   URL: https://static.s-sfr.fr/AlticeFrance/publications/sfr-archives/FinancialDocumentation/2016/16062016_numericablesfr_ddr_2015_fr_1606f.pdf · Wayback: https://web.archive.org/web/20261119081749/https://static.s-sfr.fr/AlticeFrance/publications/sfr-archives/FinancialDocumentation/2016/16062016_numericablesfr_ddr_2015_fr_1606f.pdf (nova; cita verificada a la captura) · id: `X11|B|B|FR0011594233|empresa/fundacio/entitats/evidencia|d610a3ff41dc` · origen: fonts_v75r2
   Nota: tipus=primaria_empresa estat_document=pendent_verificacio_externa
3. [V] «constituée le 2 août 2013»
   URL: https://static.s-sfr.fr/AlticeFrance/publications/sfr-archives/FinancialDocumentation/2016/16062016_numericablesfr_ddr_2015_fr_1606f.pdf · Wayback: https://web.archive.org/web/20261119081749/https://static.s-sfr.fr/AlticeFrance/publications/sfr-archives/FinancialDocumentation/2016/16062016_numericablesfr_ddr_2015_fr_1606f.pdf (nova; cita verificada a la captura) · id: `X11|B|B|FR0011594233|empresa/fundacio/entitats/evidencia|fb05b703b811` · origen: fonts_v75r2
   Nota: tipus=primaria_empresa estat_document=pendent_verificacio_externa
4. [V] «créée en 1998»
   URL: https://static.s-sfr.fr/AlticeFrance/publications/sfr-archives/FinancialDocumentation/2016/16062016_numericablesfr_ddr_2015_fr_1606f.pdf · Wayback: https://web.archive.org/web/20261119081749/https://static.s-sfr.fr/AlticeFrance/publications/sfr-archives/FinancialDocumentation/2016/16062016_numericablesfr_ddr_2015_fr_1606f.pdf (nova; cita verificada a la captura) · id: `X11|B|B|FR0011594233|empresa/fundacio/entitats/evidencia|5889ce5c132b` · origen: fonts_v75r2
   Nota: tipus=primaria_empresa estat_document=pendent_verificacio_externa


### 1.7 Dechra Pharmaceuticals PLC Registered (`GB0009633180`)

- Canvi: **ND → P** als anys 2018-2023 (n=6).
- Origen: `decisio_doctorat` · decisió: `previa:C0369`.
- Nota de la simulació: ['Dechra: ND passa a 0, regla a (Doctorat, ja tancada)', 'Dechra: ND passa a 0, regla a (Doctorat, ja tancada)', 'Dechra: ND passa a 0, regla a (Doctorat, ja tancada)', 'Dechra: ND passa a 0, regla a (Doctorat, ja tancada)', 'Dechra: ND passa a 0, regla a (Doctorat, ja tancada)', 'Dechra: ND passa a 0, regla a (Doctorat, ja tancada)']
- Cites:

1. [V] «Incorporated on
    13 May 1997»
   URL: https://find-and-update.company-information.service.gov.uk/company/03369634 · Wayback: https://web.archive.org/web/20260309190744/https://find-and-update.company-information.service.gov.uk/company/03369634 (existent; cita verificada a la captura) · id: `X6|REF|FU1105` · origen: fonts_v75r2
   Nota: tipus=referencia_R7 estat_document=cobert_arxivador
2. [V] «Aged 41, Ian joined the Group’s principal trading subsidiary NVS at its formation in 1989»
   URL: https://www.dechra.com/Files/Files/Corporate/Financial-reports/Archive/Annual-Report-and-Accounts-2002.pdf · Wayback: https://web.archive.org/web/20261119082044/https://www.dechra.com/Files/Files/Corporate/Financial-reports/Archive/Annual-Report-and-Accounts-2002.pdf (nova; cita verificada a la captura) · id: `X11|B|B|GB0009633180|persona:Ian Page/incorporacio/evidencia|f3eac4332b65` · origen: fonts_v75r2
   Nota: tipus=primaria_empresa estat_document=pendent_verificacio_externa
3. [V] «founded by Peter Ashton, his uncle Alan Ashton and Paul Hill in August 1989. […] The newly formed Group was named “Dechra”.»
   URL: https://www.nvsweb.co.uk/about-us/ · Wayback: https://web.archive.org/web/20261010161900/https://www.nvsweb.co.uk/about-us/ (existent; cita verificada a la captura) · id: `X11|B|B|GB0009633180|empresa/fundacio/entitats/evidencia|4221eb8fa9cb` · origen: fonts_v75r2
   Nota: tipus=primaria_empresa estat_document=pendent_verificacio_externa
4. [V] «se remonta a 1819, cuando la compañía fue creada como Arnolds & Son»
   URL: https://www.dechra.mx/acerca-de/historia · Wayback: https://web.archive.org/web/20260415072304/https://www.dechra.mx/acerca-de/historia (existent; cita verificada a la captura) · id: `X11|B|B|GB0009633180|empresa/fundacio/entitats/evidencia|b871b612b6db` · origen: fonts_v75r2
   Nota: tipus=primaria_empresa estat_document=pendent_verificacio_externa
5. [V] «Dales’ history stretches back to 1948»
   URL: https://www.vetsurgeon.org/veterinary-practice/2009/vp_jul2009.pdf · Wayback: https://web.archive.org/web/20261119082138/https://www.vetsurgeon.org/veterinary-practice/2009/vp_jul2009.pdf (nova; cita verificada a la captura) · id: `X11|B|B|GB0009633180|empresa/fundacio/entitats/evidencia|23f3ddf4df8d` · origen: fonts_v75r2
   Nota: tipus=secundaria_reputada estat_document=pendent_verificacio_externa


### 1.8 Mediclinic International PLC Registered (`GB00B8HX8Z88`)

- Canvi: **ND → P** als anys 2016-2017 (n=2).
- Origen: `decisio_doctorat_r4` · decisió: `4_mediclinic`.
- Nota de la simulació: ['Doctorat 4: Mediclinic ND->0 (regla a). Cites verificades del fundador unic (Hertzog) i del CEO.', 'Doctorat 4: Mediclinic ND->0 (regla a). Cites verificades del fundador unic (Hertzog) i del CEO.']
- Cites:

1. [V] «having joined Medi-Clinic from the Human Resources Department of the then Rembrandt Group (now Remgro) in 1985»
   URL: https://www.ufs.ac.za/alumni/alumni-awards/winners-2017-2018/danie-meintjes · Wayback: https://web.archive.org/web/20260207172302/https://www.ufs.ac.za/alumni/alumni-awards/winners-2017-2018/danie-meintjes · id: `D0565` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4: Hertzog com a fundador (1983) i entrada de Meintjes (1985).
2. [V] «In 1983, founder Dr Edwin Hertzog had a vision for a strong private hospital brand»
   URL: https://www.mediclinic.com/en/mediclinic-40th.html · Wayback: https://web.archive.org/web/20260421014451/https://www.mediclinic.com/en/mediclinic-40th.html · id: `D1064` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4: Hertzog com a fundador (1983) i entrada de Meintjes (1985).


### 1.9 Harbour Energy PLC Registered Shares LS (`GB00BMBVGQ36`)

- Canvi: **F → P** als anys 2022-2023 (n=2).
- Origen: `decisio_doctorat` · decisió: `previa:C0241`.
- Nota de la simulació: ['Harbour Energy: F passa a 0, regla e (Doctorat, ja tancada)', 'Harbour Energy: F passa a 0, regla e (Doctorat, ja tancada)']
- Cites:

1. [V] «Linda Z. Cook Chief Executive Officer Appointed 31 March 2021»
   URL: https://www.harbourenergy.com/who-we-are/leadership/our-senior-team/ · Wayback: https://web.archive.org/web/20261008094545/https://www.harbourenergy.com/who-we-are/leadership/our-senior-team/ · id: `D0594` · origen: sortida_claude_r4_paquet · model: Claude
   Nota: Cita literal declarada per Claude a la completació r4 (origen paquet, font A). El canvi F→P és la decisió prèvia C0241 (regla e): l'emissor atribueix la fundació a EIG, no a Linda Z. Cook.
2. [V] «Linda Z. Cook Chief Executive Officer Appointed 31 March 2021»
   URL: https://cdn.financialreports.eu/financialreports/media/filings/4658/2025/10-K/4658_10-k_2025-03-27_fa2420e3-b19f-4a86-ab14-9a4725afed93.pdf · Wayback: https://web.archive.org/web/20261119082320/https://cdn.financialreports.eu/financialreports/media/filings/4658/2025/10-K/4658_10-k_2025-03-27_fa2420e3-b19f-4a86-ab14-9a4725afed93.pdf (nova; cita verificada a la captura) · id: `D0358` · origen: sortida_claude_r4_paquet · model: Claude
   Nota: Cita literal declarada per Claude a la completació r4 (origen paquet, font A). El canvi F→P és la decisió prèvia C0241 (regla e): l'emissor atribueix la fundació a EIG, no a Linda Z. Cook.
3. [V] «Harbour Energy was founded by private equity firm EIG Global Energy Partners with a goal to build a new global, independent oil and gas company by acquisition»
   URL: https://www.harbourenergy.com/who-we-are/our-history/ · Wayback: https://web.archive.org/web/20260711202329/https://www.harbourenergy.com/who-we-are/our-history/ · id: `D0988` · origen: sortida_claude_r4_paquet · model: Claude
   Nota: Cita literal declarada per Claude a la completació r4 (origen paquet, font A). El canvi F→P és la decisió prèvia C0241 (regla e): l'emissor atribueix la fundació a EIG, no a Linda Z. Cook.
4. [V] «at both Royal Dutch Shell where she worked for almost 30 years and subsequently in private equity at EIG and Harbour Energy»
   URL: https://www.harbourenergy.com/who-we-are/leadership/our-senior-team/ · Wayback: https://web.archive.org/web/20261008094545/https://www.harbourenergy.com/who-we-are/leadership/our-senior-team/ · id: `D0594` · origen: sortida_claude_r4_paquet · model: Claude
   Nota: Cita literal declarada per Claude a la completació r4 (origen paquet, font A). El canvi F→P és la decisió prèvia C0241 (regla e): l'emissor atribueix la fundació a EIG, no a Linda Z. Cook.


### 1.10 CD Projekt S.A. Inhaber-Aktien C ZY 1 (`PLOPTTC00011`)

- Canvi: **ND → P** als anys 2023 (n=1).
- Origen: `decisio_doctorat_r4` · decisió: `1_cd_projekt_2023`.
- Nota de la simulació: ['Doctorat 1: CD Projekt 2023 ND->0 (regla a). Cita de fundadors verificada literalment. CEO també verificat.']
- Cites:

1. [V] «OPTIMUS S.A. działa od grudnia 1988 roku.»
   URL: https://www.cdprojekt.com/pl/wp-content/uploads-pl/2016/03/R4_zal_Sprawozdanie_Zarzadu_jednostkowe_2009_korekta.pdf · Wayback: https://web.archive.org/web/20240528060703/https://www.cdprojekt.com/pl/wp-content/uploads-pl/2016/03/R4_zal_Sprawozdanie_Zarzadu_jednostkowe_2009_korekta.pdf (existent; cita verificada a la captura) · id: `D0940` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4: naixement 1969, entrada 1994, i origens 1988/1994.
2. [V] «In mid-1994, he joined CD PROJEKT RED as the first employee […] Born in 1969»
   URL: https://www.cdprojekt.com/en/capital-group/supervisory-board/ · Wayback: https://web.archive.org/web/20261027081450/https://www.cdprojekt.com/en/capital-group/supervisory-board/ · id: `D0095` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4: naixement 1969, entrada 1994, i origens 1988/1994.
3. [V] «in 1994, with the establishment of CDP.pl»
   URL: https://www.cdprojekt.com/en/capital-group/history/ · Wayback: https://web.archive.org/web/20260619113020/https://www.cdprojekt.com/en/capital-group/history/ · id: `D0810` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4: naixement 1969, entrada 1994, i origens 1988/1994.


### 1.11 Swedbank AB Namn-Aktier A o.N. (`SE0000242455`)

- Canvi: **ND → P** als anys 2016-2018 (n=3).
- Origen: `decisio_doctorat_r4` · decisió: `5_swedbank_e`.
- Nota de la simulació: ["Doctorat 5: Swedbank ND->0 per regla e, amb cita d'origen verificada literalment.", "Doctorat 5: Swedbank ND->0 per regla e, amb cita d'origen verificada literalment.", "Doctorat 5: Swedbank ND->0 per regla e, amb cita d'origen verificada literalment."]
- Cites:

1. [V] «FöreningsSparbanken is formed through a merger between Sparbanken Sverige and Föreningsbanken.»
   URL: https://www.swedbank.com/about-swedbank/our-history/our-history-in-brief.html · Wayback: https://web.archive.org/web/20260808003740/https://www.swedbank.com/about-swedbank/our-history/our-history-in-brief.html · id: `D0323` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4: fusió d'origen i entrada/naixement de Bonnesen.
2. [V] «Birgitte Bonnesen […] Born 1956. Employed since 1987»
   URL: https://www.annualreports.com/HostedData/AnnualReportArchive/s/swedbank-ab_2016.pdf · Wayback: https://web.archive.org/web/20240612085801/https://www.annualreports.com/HostedData/AnnualReportArchive/s/swedbank-ab_2016.pdf · id: `D0981` · origen: paquet_r4_afirmacio
   Nota: Cites de paquet r4: fusió d'origen i entrada/naixement de Bonnesen.


## 2. Canvis de CEO (7 files)

El camp `ceos` resta el valor de la v75r2. El CEO aplicat a la v8 és `sim_ceo_aplicat`.

| ISIN | Empresa | Any | `ceos` (v75r2) → `sim_ceo_aplicat` | Decisió | Etiqueta | Certificació |
|---|---|---|---|---|---|---|
| `ES0130960018` | Enagas S.A. Acciones Port. EO 1,50 | 2016 | Antonio Llardén Carratalá → Marcelino Oreja Arburúa | 8_enagas_regla_e | es queda P | no_certificada |
| `ES0130960018` | Enagas S.A. Acciones Port. EO 1,50 | 2017 | Antonio Llardén Carratalá → Marcelino Oreja Arburúa | 8_enagas_regla_e | es queda P | no_certificada |
| `ES0130960018` | Enagas S.A. Acciones Port. EO 1,50 | 2018 | Antonio Llardén Carratalá → Marcelino Oreja Arburúa | 8_enagas_regla_e | es queda P | no_certificada |
| `ES0130960018` | Enagas S.A. Acciones Port. EO 1,50 | 2019 | Antonio Llardén Carratalá → Marcelino Oreja Arburúa | 8_enagas_regla_e | es queda P | no_certificada |
| `ES0130960018` | Enagas S.A. Acciones Port. EO 1,50 | 2020 | Antonio Llardén Carratalá → Marcelino Oreja Arburúa | 8_enagas_regla_e | es queda P | no_certificada |
| `ES0130960018` | Enagas S.A. Acciones Port. EO 1,50 | 2021 | Antonio Llardén Carratalá → Marcelino Oreja Arburúa | 8_enagas_regla_e | es queda P | no_certificada |
| `GB0000904986` | Bellway PLC Registered Shares LS -,125 | 2017 | John Watson → Ted Ayres | 9_bellway | es queda P | no_certificada |

### 2.1 Enagás 2016-2021 (`ES0130960018`) — conflicte de fonts

Instrucció de Doctorat per a la v8: segons la R1, el CEO és el consejero delegado; el president executiu només compta per la R3 si el càrrec és vacant. Calia revisar la cita literal de ChatGPT sobre Llardén: si diu «consejero delegado» o «CEO» per a algun any de 2016 a 2021, anotar-ho com a conflicte de fonts i mantenir la fila sense certificar.

**Resultat [V]: conflicte de fonts.** La cita literal de ChatGPT (manifest r4, `estat=verificada`, `cita_trobada=literal`) diu: «Mr. Antonio Llardén Carratalá was Chief Executive Officer of Enagás from 2007 to 2022.» Afirma que Llardén va ser *Chief Executive Officer* (CEO) de 2007 a 2022, període que inclou 2016-2021. No diu «consejero delegado» en aquesta frase, però sí «Chief Executive Officer», que la instrucció de Doctorat equipara a CEO. El mateix document, tot seguit, diu: «Mr. Llardén has been a non-executive Chairman of the Company since 2022» i situa Arturo Gonzalo Aizpiri com a Chief Executive Officer des del febrer del 2022. Això no treu el conflicte: la frase sobre 2007-2022 diu CEO. Claude té cites literals que identifiquen Marcelino Oreja Arburúa com a Consejero Delegado (nomenament el 2012 i càrrec exercit des del 2012) en el mateix període 2016-2021, i la R1 pren el consejero delegado com a CEO. Per tant, les files 2016-2021 es **mantenen sense certificar**. El canvi de CEO aplicat (Oreja) i l'etiqueta P no es toquen; només s'anota el conflicte. L'URL de la cita de ChatGPT apunta a un informe de reelecció / nomenaments de 2026 (document posterior als anys classificats). La baixada r4 és de la URL oficial; no consta Wayback d'aquesta baixada [NV].

Cites recollides (Oreja, Claude; i Llardén, ChatGPT):

1. [V] «el nombramiento de Marcelino Oreja Arburúa como Consejero Delegado de Enagás»
   URL: https://www.enagas.es/es/sala-comunicacion/actualidad/notas-prensa/2012-09-17_segregacion/ · Wayback: https://web.archive.org/web/20220811023530id_/https://www.enagas.es/es/sala-comunicacion/actualidad/notas-prensa/2012-09-17_Segregacion/ · id: `R0868|d0af22c8f819` · origen: verificacio_web_r4_claude · model: Claude
   Nota: estat=verificada cita_trobada=literal font_baixada=wayback_api timestamp=20220811023530
2. [V] «ejo a Marcelino Oreja Arburúa Marcelino Oreja Arburúa ha ejercido como Consejero Delegado de Enagás desde 2012»
   URL: https://www.enagas.es/es/sala-comunicacion/actualidad/notas-prensa/nombramiento-arturo-gonzalo-ceo/ · Wayback: https://web.archive.org/web/20220811023917id_/https://www.enagas.es/es/sala-comunicacion/actualidad/notas-prensa/nombramiento-arturo-gonzalo-CEO/ · id: `R0868|249db8008394` · origen: verificacio_web_r4_claude · model: Claude
   Nota: estat=verificada cita_trobada=literal font_baixada=wayback_api timestamp=20220811023917
3. [V] «D. Marcelino Oreja Arburúa (Consejero Delegado)»
   URL: https://filings.xbrl.org/213800OU3FQKGM4M2U23/2020-12-31/ESEF/ES/0/213800OU3FQKGM4M2U23-20201231/reports/213800OU3FQKGM4M2U23-20201231.xhtml · Wayback: https://web.archive.org/web/20261119082511/https://filings.xbrl.org/213800OU3FQKGM4M2U23/2020-12-31/ESEF/ES/0/213800OU3FQKGM4M2U23-20201231/reports/213800OU3FQKGM4M2U23-20201231.xhtml (nova; cita verificada a la captura) · id: `R0868|2abb1885e4a8` · origen: verificacio_web_r4_claude · model: Claude
   Nota: estat=verificada cita_trobada=literal font_baixada=oficial timestamp=
4. [V] «Mr. Antonio Llardén Carratalá was Chief Executive Officer of Enagás from 2007 to 2022»
   URL: https://www.enagas.es/content/dam/enagas/en/files/accionistas-e-inversores/gobierno-corporativo/junta-general-accionistas/propuestas-documentacion/informe-consejo-reeleccion-nombramientos-2026-en.pdf · Wayback: https://web.archive.org/web/20261119082659/https://www.enagas.es/content/dam/enagas/en/files/accionistas-e-inversores/gobierno-corporativo/junta-general-accionistas/propuestas-documentacion/informe-consejo-reeleccion-nombramientos-2026-en.pdf (nova; cita verificada a la captura) · id: `R0868|124d0a295296` · origen: verificacio_web_r4_chatgpt · model: ChatGPT
   Nota: estat=verificada cita_trobada=literal font_baixada=oficial timestamp=


Les sis files (2016-2021) queden amb `sim_canvi_ceo=1`, `ceos=Antonio Llardén Carratalá` (inalterat), `sim_ceo_aplicat=Marcelino Oreja Arburúa`, etiqueta **P**, i `sim_estat_certificacio=no_certificada` (com a la v2; a més, ara queda documentat el conflicte de fonts).

### 2.2 Bellway 2017 (`GB0000904986`)

Canvi aplicat: John Watson → Ted Ayres. Etiqueta P. Certificació: no_certificada (només un model s'hi pronuncia). `ceos` no sobreescrit.

1. [V] «Chief Operating Officer, was appointed as Chief Executive on 1 August 2018, replacing Ted Ayres, who left the Board after a period of poor health on 31 July 2018»
   URL: https://www.annualreports.com/HostedData/AnnualReportArchive/b/LSE_BWY_2018.pdf · Wayback: https://web.archive.org/web/20250124165107/https://www.annualreports.com/HostedData/AnnualReportArchive/b/LSE_BWY_2018.pdf (existent; captura truncada, cita no verificada) · id: `R1082|aa693fca7260` · origen: verificacio_web_r4_claude · model: Claude
   Nota: estat=verificada cita_trobada=literal font_baixada=oficial timestamp=
2. [V] «AYRES, Edward Francis Correspondence address Seaton Burn House, Dudley Lane, Seaton Burn, Newcastle Upon Tyne, NE13 6BE Role Resigned Director Date of birth October 1962»
   URL: https://find-and-update.company-information.service.gov.uk/company/01372603/officers · Wayback: https://web.archive.org/web/20240127170526/https://find-and-update.company-information.service.gov.uk/company/01372603/officers (existent; cita verificada a la captura) · id: `X2|GB0000904986|Ted Ayres|p0|2015` · origen: fonts_v75r2
   Nota: tipus=prova_classificacio estat_document=pendent_verificacio_externa
3. [V] «Ted was appointed 2012. Keith joined the Company in he held for 12 years. John joined to the Board as Operations Director»
   URL: https://www.bellwayplc.co.uk/media/1175/annual-report-nov-2015.pdf · Wayback: https://web.archive.org/web/20230315060724/https://www.bellwayplc.co.uk/media/1175/annual-report-nov-2015.pdf (existent; cita verificada a la captura) · id: `X2|GB0000904986|Ted Ayres|p1|2015` · origen: fonts_v75r2
   Nota: tipus=prova_classificacio estat_document=verificat


## 3. El que no canvia

- Cap altre canvi d'etiqueta ni de CEO a la v8 respecte a la v2.
- Decisió 14:44 no aplicada (igual que a la v2): Steinhoff 2016-17 es queda ND (falta cita verificada de l'operació de 1998).
- El camp `ceos` no s'ha modificat en cap fila.


## 4. Recàlcul de robustesa (v8 r1)

Els fitxers v8 (`base_isin_any_v8.csv/.xlsx` i la documentació v8) es conserven intactes. Aquesta r1 reaplica les fórmules verificades (v71/v2) sobre l'etiqueta v8, inclosos els 35 canvis (26 ND→P).

Regles aplicades [V]:

- `founderceo_rob_sense_decisions_doctorat`: es parteix del FounderCEO nou i es reverteix a `FounderCEO_v75r2` per a Cellnex (C0220), Harbour (C0241) i les decisions `3_steinhoff`, `4_mediclinic`, `5_swedbank_b`, `5_swedbank_e`, `6_unicaja`. Orpea i la resta de ND→P es queden amb l'etiqueta nova. La columna ja era correcta a la v8; 0 files canviades.
- `founderceo_rob_sense_fundador_transformador` / `sense_fundador_transformador`: si `fundador_transformador=1`, es pren `founderceo_rob_pre_d37`; si no, `FounderCEO`. Les 4 files FT del panell (Investec 2016-17, WPP 2016-17) ja tenien `pre_d37` informat. 35 files canviades (exactament els 35 canvis d'etiqueta).
- `founderceo_rob_r3_president_exec_com_1`: «1» si (ISIN, any) és Richemont 2017 (`CH0210483332`, 2017); si no, `FounderCEO`. Richemont 2017 ja era 1. 35 files canviades.

Comptes al panell (6.012), abans (v8 heretada) → després (v8r1):

| Columna | Abans | Després | Files canviades |
|---|---|---|---|
| `founderceo_rob_sense_decisions_doctorat` | F 338, P 5623, ND 20, NA 31 | F 338, P 5623, ND 20, NA 31 | 0 |
| `founderceo_rob_sense_fundador_transformador` / `sense_fundador_transformador` | F 334, P 5605, ND 42, NA 31 | F 339, P 5626, ND 16, NA 31 | 35 |
| `founderceo_rob_r3_president_exec_com_1` | F 339, P 5603, ND 40, NA 30 | F 344, P 5624, ND 14, NA 30 | 35 |
| `FounderCEO` (no es toca) | F 343, P 5624, ND 14, NA 31 | F 343, P 5624, ND 14, NA 31 | 0 |

Cap fila ha quedat [NV] per aquest recàlcul: `pre_d37` és ple a les 4 files FT i el conjunt R3 està verificat. Les columnes `*_v8` conserven el valor heretat de la v8 per traça. `ceos` no s'ha modificat (idèntic a v8 i a v75r2 al panell).

## 5. Wayback de les 30 cites que a la v8 no en tenien

Cerca amb l'API pública de disponibilitat i el CDX d'archive.org; si no n'hi havia, Save Page Now només a l'endpoint públic `https://web.archive.org/save` (POST `url=`, sense claus, sense `-k`, sense archive.today). Un 200/202 o un timestamp prematur no es compta com a captura si el snapshot servit és el 404 de Wayback («has not archived that URL»).

Resum (30 cites / 27 URL úniques):

- **Captura existent:** 14 cites (13 amb la cita verificada literalment a la captura; 1 —Bellway 2018— amb captura truncada a 1 MiB, cita no verificable).
- **Captura nova (SPN públic):** 10 cites (8 URL; la DDR SFR 2015 cobreix 3 cites). Totes 10 amb la cita verificada a la captura.
- **pendent_verificacio_externa:** 6 cites / 5 URL (Mandatum CV de Petri Niemisvirta, 2 cites; 4 PDF emeis.com/Orpea). S'ha sol·licitat SPN públic una vegada; no s'ha repetit el POST. El snapshot no s'ha pogut descarregar com a document (404 de Wayback o cap índex després d'espera addicional).
- **Cites amb Wayback útil i cita verificada:** 23 (13 existents + 10 noves).
- **Cites amb Wayback però cita no verificada:** 1 (Bellway 2018, snapshot truncat).
- **Cites encara sense Wayback útil:** 6.

Detall:

- idx 1: existent; cita_verificada=si; https://web.archive.org/web/20160531105701/http://www.sec.gov:80/Archives/edgar/data/1140467/000119312514112577/d692738d20f.htm — https://www.sec.gov/Archives/edgar/data/1140467/000119312514112577/d692738d20f.htm
- idx 2: existent; cita_verificada=si; https://web.archive.org/web/20260719173341/https://www.ab-inbev.com/about-us/our-heritage — https://www.ab-inbev.com/about-us/our-heritage
- idx 6: existent; cita_verificada=si; https://web.archive.org/web/20260520225418/https://www.unicajabanco.com/es/sala-de-comunicacion/buscador-noticias/2021/03/las-juntas-de-accionistas-de-unicaja-banco-y-liberbank-aprueban- — https://www.unicajabanco.com/es/sala-de-comunicacion/buscador-noticias/2021/03/las-juntas-de-accionistas-de-unicaja-banco-y-liberbank-aprueban-
- idx 7: existent; cita_verificada=si; https://web.archive.org/web/20251115054852/https://www.unicajabanco.com/content/dam/unicaja/unicaja-corporacion/documentos-corporacion/inversores-y-accionistas/presentacion-corporativa-tercer-trimestre-2017-en.pdf — https://www.unicajabanco.com/content/dam/unicaja/unicaja-corporacion/documentos-corporacion/inversores-y-accionistas/presentacion-corporativa-tercer-trimestre-2017-en.pdf
- idx 9: existent; cita_verificada=si; https://web.archive.org/web/20240804122948/https://www.unicajabanco.com/content/dam/unicaja/unicaja-corporacion/documentos-corporacion/emisiones/Folleto_Informativo_Salida_Bolsa-en.pdf — https://www.unicajabanco.com/content/dam/unicaja/unicaja-corporacion/documentos-corporacion/emisiones/Folleto_Informativo_Salida_Bolsa-en.pdf
- idx 10: pendent_verificacio_externa; cita_verificada=no — https://www.mandatum.fi/4a5b46/globalassets/konserni/mandatum/johto/johto---cvt/cv_petri_niemisvirta_en.pdf
- idx 11: pendent_verificacio_externa; cita_verificada=no — https://www.mandatum.fi/4a5b46/globalassets/konserni/mandatum/johto/johto---cvt/cv_petri_niemisvirta_en.pdf
- idx 12: existent; cita_verificada=si; https://web.archive.org/web/20260421173658/https://www.mandatum.fi/en/group/about-the-company/history/ — https://www.mandatum.fi/en/group/about-the-company/history/
- idx 13: existent; cita_verificada=si; https://web.archive.org/web/20260416055221/https://www.sampo.com/globalassets/investors/debt-instruments-and-ratings/documents/2025/sampo-emtn-2025---base-prospectus-dated-on-3-december-2025.pdf — https://www.sampo.com/globalassets/investors/debt-instruments-and-ratings/documents/2025/sampo-emtn-2025---base-prospectus-dated-on-3-december-2025.pdf
- idx 14: nova; cita_verificada=si; https://web.archive.org/web/20261119080031/https://filings.xbrl.org/969500LHIH3NT7PK1V89/2021-12-31/ESEF/FR/0/969500LHIH3NT7PK1V89-2021-12-31-fr/reports/969500LHIH3NT7PK1V89-2021-12-31-fr.xhtml — https://filings.xbrl.org/969500LHIH3NT7PK1V89/2021-12-31/ESEF/FR/0/969500LHIH3NT7PK1V89-2021-12-31-fr/reports/969500LHIH3NT7PK1V89-2021-12-31-fr.xhtml
- idx 15: pendent_verificacio_externa; cita_verificada=no — https://www.emeis.com/sites/site_corporate/files/medias/documents/orpeaborchuredeconvocationag250614_0.pdf
- idx 16: pendent_verificacio_externa; cita_verificada=no — https://www.emeis.com/sites/site_corporate/files/medias/documents/cporpea30janvier2022fb5f8.pdf
- idx 17: pendent_verificacio_externa; cita_verificada=no — https://www.emeis.com/sites/default/files/medias/documents/orpeadocderef2013_0.pdf
- idx 18: pendent_verificacio_externa; cita_verificada=no — https://www.emeis.com/sites/default/files/medias/documents/orpeaddr2014vf_0.pdf
- idx 19: nova; cita_verificada=si; https://web.archive.org/web/20261119081609/https://www.sec.gov/Archives/edgar/data/101830/000010183018000003/form8-k20180102.htm — https://www.sec.gov/Archives/edgar/data/101830/000010183018000003/form8-k20180102.htm
- idx 20: nova; cita_verificada=si; https://web.archive.org/web/20261119081749/https://static.s-sfr.fr/AlticeFrance/publications/sfr-archives/FinancialDocumentation/2016/16062016_numericablesfr_ddr_2015_fr_1606f.pdf — https://static.s-sfr.fr/AlticeFrance/publications/sfr-archives/FinancialDocumentation/2016/16062016_numericablesfr_ddr_2015_fr_1606f.pdf
- idx 21: nova; cita_verificada=si; https://web.archive.org/web/20261119081749/https://static.s-sfr.fr/AlticeFrance/publications/sfr-archives/FinancialDocumentation/2016/16062016_numericablesfr_ddr_2015_fr_1606f.pdf — https://static.s-sfr.fr/AlticeFrance/publications/sfr-archives/FinancialDocumentation/2016/16062016_numericablesfr_ddr_2015_fr_1606f.pdf
- idx 22: nova; cita_verificada=si; https://web.archive.org/web/20261119081749/https://static.s-sfr.fr/AlticeFrance/publications/sfr-archives/FinancialDocumentation/2016/16062016_numericablesfr_ddr_2015_fr_1606f.pdf — https://static.s-sfr.fr/AlticeFrance/publications/sfr-archives/FinancialDocumentation/2016/16062016_numericablesfr_ddr_2015_fr_1606f.pdf
- idx 23: existent; cita_verificada=si; https://web.archive.org/web/20260309190744/https://find-and-update.company-information.service.gov.uk/company/03369634 — https://find-and-update.company-information.service.gov.uk/company/03369634
- idx 24: nova; cita_verificada=si; https://web.archive.org/web/20261119082044/https://www.dechra.com/Files/Files/Corporate/Financial-reports/Archive/Annual-Report-and-Accounts-2002.pdf — https://www.dechra.com/Files/Files/Corporate/Financial-reports/Archive/Annual-Report-and-Accounts-2002.pdf
- idx 25: existent; cita_verificada=si; https://web.archive.org/web/20261010161900/https://www.nvsweb.co.uk/about-us/ — https://www.nvsweb.co.uk/about-us/
- idx 26: existent; cita_verificada=si; https://web.archive.org/web/20260415072304/https://www.dechra.mx/acerca-de/historia — https://www.dechra.mx/acerca-de/historia
- idx 27: nova; cita_verificada=si; https://web.archive.org/web/20261119082138/https://www.vetsurgeon.org/veterinary-practice/2009/vp_jul2009.pdf — https://www.vetsurgeon.org/veterinary-practice/2009/vp_jul2009.pdf
- idx 31: nova; cita_verificada=si; https://web.archive.org/web/20261119082320/https://cdn.financialreports.eu/financialreports/media/filings/4658/2025/10-K/4658_10-k_2025-03-27_fa2420e3-b19f-4a86-ab14-9a4725afed93.pdf — https://cdn.financialreports.eu/financialreports/media/filings/4658/2025/10-K/4658_10-k_2025-03-27_fa2420e3-b19f-4a86-ab14-9a4725afed93.pdf
- idx 34: existent; cita_verificada=si; https://web.archive.org/web/20240528060703/https://www.cdprojekt.com/pl/wp-content/uploads-pl/2016/03/R4_zal_Sprawozdanie_Zarzadu_jednostkowe_2009_korekta.pdf — https://www.cdprojekt.com/pl/wp-content/uploads-pl/2016/03/R4_zal_Sprawozdanie_Zarzadu_jednostkowe_2009_korekta.pdf
- idx 41: nova; cita_verificada=si; https://web.archive.org/web/20261119082511/https://filings.xbrl.org/213800OU3FQKGM4M2U23/2020-12-31/ESEF/ES/0/213800OU3FQKGM4M2U23-20201231/reports/213800OU3FQKGM4M2U23-20201231.xhtml — https://filings.xbrl.org/213800OU3FQKGM4M2U23/2020-12-31/ESEF/ES/0/213800OU3FQKGM4M2U23-20201231/reports/213800OU3FQKGM4M2U23-20201231.xhtml
- idx 42: nova; cita_verificada=si; https://web.archive.org/web/20261119082659/https://www.enagas.es/content/dam/enagas/en/files/accionistas-e-inversores/gobierno-corporativo/junta-general-accionistas/propuestas-documentacion/informe-consejo-reeleccion-nombramientos-2026-en.pdf — https://www.enagas.es/content/dam/enagas/en/files/accionistas-e-inversores/gobierno-corporativo/junta-general-accionistas/propuestas-documentacion/informe-consejo-reeleccion-nombramientos-2026-en.pdf
- idx 43: existent_truncada; cita_verificada=no; https://web.archive.org/web/20250124165107/https://www.annualreports.com/HostedData/AnnualReportArchive/b/LSE_BWY_2018.pdf — https://www.annualreports.com/HostedData/AnnualReportArchive/b/LSE_BWY_2018.pdf
- idx 44: existent; cita_verificada=si; https://web.archive.org/web/20240127170526/https://find-and-update.company-information.service.gov.uk/company/01372603/officers — https://find-and-update.company-information.service.gov.uk/company/01372603/officers
- idx 45: existent; cita_verificada=si; https://web.archive.org/web/20230315060724/https://www.bellwayplc.co.uk/media/1175/annual-report-nov-2015.pdf — https://www.bellwayplc.co.uk/media/1175/annual-report-nov-2015.pdf

Notes de verificació: s'ha normalitzat espai, entitats HTML i etiquetes; als PDF s'ha fet servir pdftotext (i `-layout` si calia). La cita de Bellway 2015 és un artefacte de lectura horitzontal de tres columnes; la cadena literal del registre apareix amb `pdftotext -layout`. El snapshot XBRL d'Orpea 2021 arriba gzip; s'ha descomprimit abans de verificar. No s'ha llegit ni utilitzat cap clau `IA_S3`.

---

# Lot ND-1 (proposta de Claude Code)

Data: 19/11/2026 (CET, Europe/Madrid). Branca `cas/nd-lot1-14-files`. Tasca: PENDENTS §1.3, les 14 files ND del panell (5 ISIN). **Proposta, no certificació**: no compta com a tercer model a cegues; la certificació queda dins el flux (DF, Doctorat, Jordi).

Resultat: **8 files passen de ND a P** (B&M 2016-2021, regla d; Steinhoff 2016-2017, regla b) i **6 files es mantenen ND** amb la cerca documentada (Drillisch 2017, Sopra Steria 2025, Aroundtown 2017-2020).

Correccions de DF (19/11/2026) aplicades en aquesta branca: a la base només canvia `FounderCEO`; Steinhoff per regla b amb `ND1-ST1` i `ND1-ST2` (l'operació de 1998 no és fundació nova) i la còpia d'agbiz marcada `font_copia_no_original`; recerca addicional per a Aroundtown 2017-2020 i Drillisch 2017, que es mantenen ND. S'hi afegeixen 44 cites (`ND1-ST7`–`ND1-ST21`, `ND1-AT6`–`ND1-AT21`, `ND1-DR8`–`ND1-DR20`).

Mètode: cada cita s'ha verificat literalment per script al document baixat de la URL original (pdftotext per als PDF, text sense etiquetes per a l'HTML; espais i lligadures normalitzats). Les URL de Wayback són captures existents segons l'API de disponibilitat d'archive.org; **no s'han pogut obrir** (web.archive.org tallava la connexió des de la sessió), de manera que la cita no està verificada a la captura (`cita_verificada_a_captura=no`). No s'ha creat cap captura nova.

Columna modificada a `dades/base_isin_any_v8r3.csv` a les 8 files al PR #2: **només `FounderCEO`** (no_determinat → 0). El recàlcul de les columnes derivades i l'alineació del `.xlsx` és a la branca `df/robustesa-nd-lot1` (secció «Recàlcul de robustesa del lot ND-1» més avall).

Comptes de `FounderCEO` (ja a main després del PR #2): F 343, P 5.632 (+8), ND 6 (−8), NA 31. La certificació no canvia (`no_certificada`).


### Recàlcul de robustesa del lot ND-1 (DF, 19/11/2026)

Branca `df/robustesa-nd-lot1`, a partir de `main` `8bda957d` (PR #2 i PR #3 ja fusionats). Jordi va aprovar el recàlcul el 19/11/2026 a les 15:51 (Europe/Madrid). **La fusió d'aquest recàlcul la decideix Jordi.** No es fusiona des d'aquesta branca.

A les 8 files que el PR #2 va passar de ND a P (B&M 2016-2021, regla d; Steinhoff 2016-2017, regla b), s'apliquen les fórmules de la v8 r1 i el precedent de les files ND→P per decisió de Doctorat (Mandatum, SFR, AB InBev, Orpea, Dechra). `FounderCEO` al CSV ja era 0; al `.xlsx` s'hi alinea (al PR #2 havia quedat pendent). Cap altra fila no canvia.

Columnes actualitzades a les 8 files:

- `founderceo_rob_r3_president_exec_com_1`, `founderceo_rob_sense_fundador_transformador`, `sense_fundador_transformador`, `founderceo_rob_sense_decisions_doctorat`: no_determinat → 0 (fórmula v8r1: no són Richemont 2017; `fundador_transformador=0`; `sim_decisio_doctorat` no és a la llista de reversió).
- `a_mostra_principal`: 0 → 1 (regla J14: `fora_panel=0`, FounderCEO tancat, sense `dret_temporal`).
- `sim_canvi=1`, `sim_canvi_de=ND`, `sim_canvi_a=P`, `sim_origen_canvi=decisio_doctorat`.
- `sim_decisio_doctorat`: `lot_nd1:regla_d` (B&M) i `lot_nd1:regla_b` (Steinhoff). No es reutilitza el codi `3_steinhoff` (és a la llista de reversió de `founderceo_rob_sense_decisions_doctorat`).
- `sim_nota` i `sim_cert_detall` actualitzats; la certificació es manté `no_certificada`.
- Steinhoff: s'afegeix la marca `fundacio_alternativa_1998` (Doctorat 19/11/2026 11:20).

No s'han modificat, amb el mateix criteri que les altres files ND→P de Doctorat: la resta de `founderceo_rob_*` (inclòs `founderceo_rob_nd_com_1`, que es queda 1, com a 28 files equivalents), `regles` (`cap`), `motiu_nd`, `detall_motiu_nd`, les instantànies `_v8` i `a_mostra_principal_v*`, i `a_mostra_nomes_certificades` (0, perquè no estan certificades). La prova per interval del lot 2 no s'ha incorporat a cap robustesa.

Recomptes a les 6.012 files (abans → després):

| Columna | Abans | Després |
|---|---|---|
| `FounderCEO` (sense canvi en aquest PR) | 0: 5.632 · 1: 343 · no_determinat: 6 · NA_sense_ceo: 31 | igual |
| `founderceo_rob_r3_president_exec_com_1` | 0: 5.624 · 1: 344 · no_determinat: 14 · NA_sense_ceo: 30 | 0: 5.632 (+8) · 1: 344 · no_determinat: 6 (−8) · NA_sense_ceo: 30 |
| `founderceo_rob_sense_fundador_transformador` (i `sense_fundador_transformador`, alias) | 0: 5.626 · 1: 339 · no_determinat: 16 · NA_sense_ceo: 31 | 0: 5.634 (+8) · 1: 339 · no_determinat: 8 (−8) · NA_sense_ceo: 31 |
| `founderceo_rob_sense_decisions_doctorat` | 0: 5.623 · 1: 338 · no_determinat: 20 · NA_sense_ceo: 31 | 0: 5.631 (+8) · 1: 338 · no_determinat: 12 (−8) · NA_sense_ceo: 31 |
| `a_mostra_principal` (mostra J14) | 1: 5.954 · 0: 58 · J14: n=5.954, F=342, P=5.612 | 1: 5.962 (+8) · 0: 50 · J14: n=5.962, F=342, P=5.620 |
| `sim_canvi` | 0: 5.977 · 1: 35 | 0: 5.969 · 1: 43 (+8) |
| `sim_origen_canvi` | (buit): 5.977 · decisio_doctorat: 22 · decisio_doctorat_r4: 13 | (buit): 5.969 · decisio_doctorat: 30 (+8) · decisio_doctorat_r4: 13 |
| `founderceo_rob_nd_com_1` (sense canvi) | 0: 5.603 · 1: 378 · NA_sense_ceo: 31 | igual |
| `sim_estat_certificacio` (sense canvi) | certificada: 1.773 · certificada_ceo_pendent: 108 · no_certificada: 241 · fora_mostra_auditoria: 3.890 | igual |

Entrades noves al CSV del registre: `DF-ROB-ND1-BM` i `DF-ROB-ND1-ST` (`tipus=etiqueta`, `marca_veritat=[NV]`, sense cita nova).

| # | ISIN | Empresa | Anys (n) | Actual → proposat | Regla | Efecte esperat |
|---|---|---|---|---|---|---|
| 12 | `LU1072616219` | B & M Europ.Value Retail S.A. Actions | 2016-2021 (6) | ND → P | d | no_certificada, dins el flux |
| 13 | `NL0011375019` | Steinhoff Internatl Hldgs N.V. Aandelen op | 2016-2017 (2) | ND → P | b | no_certificada, dins el flux |
| 14 | `DE0005545503` | Drillisch AG Inhaber-Aktien o.N. | 2017 (1) | ND → ND (sense canvi) | cap | sense efecte |
| 15 | `FR0000050809` | Sopra Steria Group S.A. Actions Port. EO 1 | 2025 (1) | ND → ND (sense canvi) | cap | sense efecte |
| 16 | `LU1673108939` | Aroundtown SA | 2017-2020 (4) | ND → ND (sense canvi) | cap | sense efecte |

### B & M Europ.Value Retail S.A. Actions (`LU1072616219`)

- isin i anys: `LU1072616219`, 2016-2021 (n=6). CEO: Simon Arora.
- FounderCEO actual → proposat: **no_determinat (ND) → 0 (P)**.
- Regla aplicada: d.
- Justificació: Regla d (incorporació tardana): l'emissor situa la fundació del negoci el 1978 [`ND1-BM1`] i l'entrada de Simon Arora el desembre de 2004, per compra de l'empresa [`ND1-BM2`, `ND1-BM3`], amb ocupadors anteriors citats [`ND1-BM4`]. Una compra no és una fundació nova (METODOLOGIA §2, prova d). No s'ha trobat cap cita de l'emissor que l'anomeni fundador de B&M (D37) als documents oberts (pàgina d'història, informes anuals 2022 i 2023, convocatòries de junta 2016-2021; el fullet de la sortida a borsa de 2014 no s'ha localitzat a la web de l'emissor): l'única menció «co-founder» es refereix a Orient Sourcing Services, una altra entitat [`ND1-BM4`]. La via FT ja va ser descartada per Jordi (14/11/2026 18:33) i no es reobre.
- Efecte esperat sobre la certificació: no_certificada (sense canvi d'estat): la proposta no és un tercer model; la certificació queda dins el flux (DF, Doctorat, Jordi).
- Cites:

1. [`ND1-BM1`] [V] «The business was founded in 1978 with the first store opening in Blackpool.»
   Nivell A · prova: fundació rellevant (1978) · URL: https://www.bandmretail.com/about-us/our-history · Wayback: https://web.archive.org/web/20251206084922/https://www.bandmretail.com/about-us/our-history (existent; cita no verificada a la captura) · id: `ND1-BM1`

2. [`ND1-BM2`] [V] «B&M was acquired by Simon and Bobby Arora in December 2004 from Phildrew Investments»
   Nivell A · prova: entrada per compra (desembre 2004) · URL: https://www.bandmretail.com/about-us/our-history · Wayback: https://web.archive.org/web/20251206084922/https://www.bandmretail.com/about-us/our-history (existent; cita no verificada a la captura) · id: `ND1-BM2`

3. [`ND1-BM3`] [V] «Simon was Chief Executive Officer of the B&M Group from 1 December 2004 until the appointment of Alex Russo to that role on 26 September 2022.»
   Nivell A · prova: CEO 2016-2021 (mandat 1/12/2004-26/9/2022) · URL: https://www.bandmretail.com/~/media/Files/B/Bmstores-Corp/documents/investors/company-meetings/agm/annual-report-2023.pdf · Wayback: https://web.archive.org/web/20260310214905/https://www.bandmretail.com/~/media/Files/B/Bmstores-Corp/documents/investors/company-meetings/agm/annual-report-2023.pdf (existent; cita no verificada a la captura) · id: `ND1-BM3`

4. [`ND1-BM4`] [V] «Simon was a co-founder and Managing Director of the wholesale homeware business, Orient Sourcing Services, before acquiring B&M jointly with his family. Prior to the acquisition of B&M, Simon held various positions with McKinsey & Co., 3i Group plc and Barclays Bank plc.»
   Nivell A · prova: ocupador anterior · URL: https://www.bandmretail.com/~/media/Files/B/Bmstores-Corp/documents/investors/company-meetings/agm/annual-report-2023.pdf · Wayback: https://web.archive.org/web/20260310214905/https://www.bandmretail.com/~/media/Files/B/Bmstores-Corp/documents/investors/company-meetings/agm/annual-report-2023.pdf (existent; cita no verificada a la captura) · id: `ND1-BM4`

5. [`ND1-BM5`] [V] «Simon has been Chief Executive Officer of the B&M Group since 1 December 2004.»
   Nivell A · prova: CEO (document contemporani, 2019) · URL: https://www.bandmretail.com/~/media/Files/B/Bmstores-Corp/documents/investors/company-meetings/agm/2019/notice-of-agm-2019.pdf · Wayback: https://web.archive.org/web/20260310220456/https://www.bandmretail.com/~/media/Files/B/Bmstores-Corp/documents/investors/company-meetings/agm/2019/notice-of-agm-2019.pdf (existent; cita no verificada a la captura) · id: `ND1-BM5`

6. [`ND1-BM6`] [V] «Simon has been Chief Executive Officer of the B&M Group since 1 December 2004.»
   Nivell A · prova: CEO (document contemporani, 2020) · URL: https://www.bandmretail.com/~/media/Files/B/Bmstores-Corp/documents/investors/company-meetings/agm/2020/notice-of-agm-2020.pdf · Wayback: https://web.archive.org/web/20260310213333/https://www.bandmretail.com/~/media/Files/B/Bmstores-Corp/documents/investors/company-meetings/agm/2020/notice-of-agm-2020.pdf (existent; cita no verificada a la captura) · id: `ND1-BM6`

7. [`ND1-BM7`] [V] «Simon has been Chief Executive Officer of the B&M Group since 1 December 2004.»
   Nivell A · prova: CEO (document contemporani, 2021) · URL: https://www.bandmretail.com/~/media/Files/B/Bmstores-Corp/documents/investors/company-meetings/agm/2021/360930-b-and-m-notice-of-agm-web.pdf · Wayback: https://web.archive.org/web/20260310221611/https://www.bandmretail.com/~/media/Files/B/Bmstores-Corp/documents/investors/company-meetings/agm/2021/360930-b-and-m-notice-of-agm-web.pdf (existent; cita no verificada a la captura) · id: `ND1-BM7`


### Steinhoff Internatl Hldgs N.V. Aandelen op (`NL0011375019`)

- isin i anys: `NL0011375019`, 2016-2017 (n=2). CEO: Markus Jooste.
- FounderCEO actual → proposat: **no_determinat (ND) → 0 (P)**.
- Regla aplicada: b.
- Justificació: Regla b (edat), aplicada segons la correcció de DF (19/11/2026): l'operació de 1997-1998 no és una fundació nova. Markus Jooste va néixer el gener de 1961 [`ND1-ST1`] (data completa, 22/01/1961, en un document de l'emissor [`ND1-ST13`]) i la font situa l'inici de l'activitat del fundador Bruno Steinhoff el 1963 [`ND1-ST2`; el mateix passatge a la URL original de Business Day: `ND1-ST10`]: 1963 − 1961 = 2 < 18. L'emissor anomena Bruno Steinhoff fundador del grup [`ND1-ST14`] i situa l'inici del seu negoci propi el juny de 1964 [`ND1-ST15`]; amb 1964 el resultat no canvia (3 < 18). Les cites de l'operació de 1997-1998 [`ND1-ST3`, `ND1-ST4`, `ND1-ST6`] queden com a context. [`ND1-ST5`] (afirmació de no fundador) és corroboració B, no cap de les proves a-e. CEO a 31/10: 2016, Jooste CEO durant l'exercici 1/10/2016-30/9/2017 [`ND1-ST16`]; 2017, nomenat el 30/11/2015 i dimissió acceptada el 5/12/2017 [`ND1-ST17`, `ND1-ST18`] (prova d'interval retrospectiva).
- Efecte esperat sobre la certificació: no_certificada (sense canvi d'estat); aporta la cita de l'operació de 1997-1998 que la nota «Doctorat 3 no aplicada» declarava pendent. La certificació queda dins el flux.
- Font de `ND1-ST2`, `ND1-ST3`, `ND1-ST5`, `ND1-ST7`, `ND1-ST8` i `ND1-ST9`: **`font_copia_no_original`**. És una còpia, allotjada a agbiz.co.za, de l'informe especial «Business Perspectives on the Steinhoff Saga» (juny 2018) de la University of Stellenbosch Business School (USB). La còpia identifica l'autoria i la institució originals [`ND1-ST7`, `ND1-ST8`, `ND1-ST9`] i, per la correcció de DF, compta com a B. Business Day va publicar el text de la USB en quatre parts [`ND1-ST11`]: a la seva URL original hi ha [`ND1-ST10`] (el passatge de `ND1-ST2`, amb petites diferències de redacció) i [`ND1-ST12`] (idèntica a `ND1-ST5`).
- Wayback: la còpia té captura (20261012052927), però la cita **no s'ha pogut verificar a la captura** perquè web.archive.org no és accessible des de la sessió: `pendent_verificacio_externa`. Original: https://www.usb.ac.za/wp-content/uploads/2018/06/USB-Management-Report-Steinhoff-Saga.pdf (pista d'un fòrum, font C) redirigeix a stellenboschbusiness.ac.za i retorna 403 amb repte de Cloudflare (tot el domini). L'API de disponibilitat d'archive.org no té cap captura del PDF original (provades 9 variants de la URL, amb i sense www, http/https, usb.ac.za i stellenboschbusiness.ac.za); només en té de la pàgina índex https://www.usb.ac.za/managementreview/ (20200806213444), que no s'ha pogut obrir. Cap altre allotjament de l'original trobat amb WebSearch; les republicacions de Fin24 i News24 retornen 403 de Cloudflare.
- Dubtes per a Doctorat (no decidits): (1) 1963 (USB, «first became involved in sourcing and selling household goods») i juny de 1964 (emissor, «started his furniture trade and distribution business») descriuen fets diferents o són una contradicció sobre la fundació (METODOLOGIA §2: dues fonts A/B contradictòries → indeterminat); la regla b dona el mateix resultat amb tots dos anys. (2) Contraprova considerada: fonts B atribueixen a Jooste un paper actiu en l'estructura de 1995-1998 [`ND1-ST19`, `ND1-ST20`]; cap no fa servir «founder/co-founder», i DF ha decidit que l'operació de 1998 no és fundació nova. (3) L'emissor cotitzat (N.V.) és un holding nou de 2015 sense canvi en els actius subjacents [`ND1-ST21`]; METODOLOGIA d) no esmenta aquest cas. (4) Prova principal del naixement: `ND1-ST1` (Companies House, que avisa que no comprova l'exactitud de les dades) o `ND1-ST13` (emissor). (5) `ND1-ST17` i `ND1-ST18` són les dues meitats d'una frase partida per un peu de pàgina, verificades per separat.
- Cerca addicional (19/11/2026): còpia d'agbiz tornada a baixar (mateix SHA-256 que la primera baixada); URL original de la USB i variants (usb.ac.za, stellenboschbusiness.ac.za, pàgines managementreview) → 301/403 Cloudflare; API de disponibilitat d'archive.org per a 9 variants; Steinhoff Annual Report 2017 (irpages2.eqs.com, plataforma EQS de l'emissor); Business Day/BusinessLIVE parts 1 i 3 de la sèrie (15 i 20/6/2018); amaBhungane/Financial Mail (1/11/2018; la versió del Financial Mail és de pagament); Companies House (full de nomenaments de Markus Johannes Jooste); Fin24 i News24 (403).
- Cites:

1. [`ND1-ST1`] [V] «Date of birth January 1961»
   Nivell A · prova: naixement de Markus Jooste (gener 1961) · URL: https://find-and-update.company-information.service.gov.uk/officers/MRjrIvkfM8rqVRz5xVuOkLXYQ-8/appointments · Wayback: https://web.archive.org/web/20260105045936/https://find-and-update.company-information.service.gov.uk/officers/MRjrIvkfM8rqVRz5xVuOkLXYQ-8/appointments (existent; cita no verificada a la captura) · id: `ND1-ST1`

2. [`ND1-ST2`] [V] «Steinhoff first became involved in sourcing and selling household goods in 1963 when its founder, an enterprising West German by the name of Bruno Steinhoff,»
   Nivell B · prova: inici de l'activitat del fundador Bruno Steinhoff (1963); regla b amb ND1-ST1 · URL: https://agbiz.co.za/uploads/AgbizNews18/180803_Steinhoff-Saga.pdf · Wayback: https://web.archive.org/web/20261012052927/https://agbiz.co.za/uploads/AgbizNews18/180803_Steinhoff-Saga.pdf (existent; cita no verificada a la captura) · id: `ND1-ST2` · `font_copia_no_original` (còpia a agbiz.co.za de l'informe de la University of Stellenbosch Business School; verificació a la captura de la còpia: `pendent_verificacio_externa`)

3. [`ND1-ST3`] [V] «Not long afterwards, in 1997, Bruno Steinhoff acquired a 35 percent stake in Gommagomma from Daun & Cie.»
   Nivell B · prova: operació 1997: Steinhoff compra el 35% de Gommagomma · URL: https://agbiz.co.za/uploads/AgbizNews18/180803_Steinhoff-Saga.pdf · Wayback: https://web.archive.org/web/20261012052927/https://agbiz.co.za/uploads/AgbizNews18/180803_Steinhoff-Saga.pdf (existent; cita no verificada a la captura) · id: `ND1-ST3` · `font_copia_no_original` (còpia a agbiz.co.za de l'informe de la University of Stellenbosch Business School; verificació a la captura de la còpia: `pendent_verificacio_externa`)

4. [`ND1-ST4`] [V] «by 1998 Steinhoff Europe and Steinhoff Africa (formerly Gommagomma) had consolidated their operations. Steinhoff International Holdings listed on the JSE in 1998.»
   Nivell B · prova: operació 1998: consolidació i sortida a borsa · URL: https://www.businessday.co.za/rdm/business/2018-06-15-the-steinhoff-saga-part-one-the-making-of-a-corporate-giant/ · Wayback: https://web.archive.org/web/20261006080717/https://www.businessday.co.za/rdm/business/2018-06-15-the-steinhoff-saga-part-one-the-making-of-a-corporate-giant/ (existent; cita no verificada a la captura) · id: `ND1-ST4`

5. [`ND1-ST5`] [V] «Although Jooste was not the founder of the company, he behaved as if Steinhoff and its assets belonged to him personally.»
   Nivell B · prova: afirmació directa de no fundador · URL: https://agbiz.co.za/uploads/AgbizNews18/180803_Steinhoff-Saga.pdf · Wayback: https://web.archive.org/web/20261012052927/https://agbiz.co.za/uploads/AgbizNews18/180803_Steinhoff-Saga.pdf (existent; cita no verificada a la captura) · id: `ND1-ST5` · `font_copia_no_original` (còpia a agbiz.co.za de l'informe de la University of Stellenbosch Business School; verificació a la captura de la còpia: `pendent_verificacio_externa`)

6. [`ND1-ST6`] [V] «Bruno and Daun had been acquaintances in Germany and Jooste was Daun’s CEO.»
   Nivell B · prova: Jooste, directiu de Daun (Gommagomma) abans de l'operació · URL: https://www.businessday.co.za/rdm/business/2018-06-15-the-steinhoff-saga-part-one-the-making-of-a-corporate-giant/ · Wayback: https://web.archive.org/web/20261006080717/https://www.businessday.co.za/rdm/business/2018-06-15-the-steinhoff-saga-part-one-the-making-of-a-corporate-giant/ (existent; cita no verificada a la captura) · id: `ND1-ST6`

7. [`ND1-ST7`] [V] «SPECIAL REPORT JUNE 2018 BUSINESS PERSPECTIVES ON THE STEINHOFF SAGA»
   Nivell B · prova: identificació de la còpia: portada de l'informe especial de juny de 2018 · URL: https://agbiz.co.za/uploads/AgbizNews18/180803_Steinhoff-Saga.pdf · Wayback: https://web.archive.org/web/20261012052927/https://agbiz.co.za/uploads/AgbizNews18/180803_Steinhoff-Saga.pdf (existent; cita no verificada a la captura) · id: `ND1-ST7` · `font_copia_no_original` (còpia a agbiz.co.za de l'informe de la University of Stellenbosch Business School; verificació a la captura de la còpia: `pendent_verificacio_externa`)

8. [`ND1-ST8`] [V] «Piet Naudé Brett Hamilton Marius Ungerer Daniel Malan Mias de Klerk»
   Nivell B · prova: identificació de la còpia: llista d'autors de l'informe original · URL: https://agbiz.co.za/uploads/AgbizNews18/180803_Steinhoff-Saga.pdf · Wayback: https://web.archive.org/web/20261012052927/https://agbiz.co.za/uploads/AgbizNews18/180803_Steinhoff-Saga.pdf (existent; cita no verificada a la captura) · id: `ND1-ST8` · `font_copia_no_original` (còpia a agbiz.co.za de l'informe de la University of Stellenbosch Business School; verificació a la captura de la còpia: `pendent_verificacio_externa`)

9. [`ND1-ST9`] [V] «Published June 2018 Copyright © 2018 University of Stellenbosch Business School»
   Nivell B · prova: identificació de la còpia: institució original (University of Stellenbosch Business School) i data de publicació · URL: https://agbiz.co.za/uploads/AgbizNews18/180803_Steinhoff-Saga.pdf · Wayback: https://web.archive.org/web/20261012052927/https://agbiz.co.za/uploads/AgbizNews18/180803_Steinhoff-Saga.pdf (existent; cita no verificada a la captura) · id: `ND1-ST9` · `font_copia_no_original` (còpia a agbiz.co.za de l'informe de la University of Stellenbosch Business School; verificació a la captura de la còpia: `pendent_verificacio_externa`)

10. [`ND1-ST10`] [V] «The company first became involved in sourcing and selling household goods in 1963 when its founder, an enterprising West German by the name of Bruno Steinhoff»
   Nivell B · prova: versió de premsa B, a la URL original, del passatge de ND1-ST2: inici de l'activitat del fundador Bruno Steinhoff el 1963 · URL: https://www.businesslive.co.za/rdm/business/2018-06-15-the-steinhoff-saga-part-one-the-making-of-a-corporate-giant/ · Wayback: https://web.archive.org/web/20250613221240/https://www.businesslive.co.za/rdm/business/2018-06-15-the-steinhoff-saga-part-one-the-making-of-a-corporate-giant/ (existent; cita no verificada a la captura) · id: `ND1-ST10`

11. [`ND1-ST11`] [V] «This is part three of a four part series on South Africa's biggest corporate meltdown which has been researched and written at the University of Stellenbosch Business School.»
   Nivell B · prova: la sèrie de Business Day és el text de la USB (atribució de l'autoria) · URL: https://www.businesslive.co.za/rdm/business/2018-06-20-the-steinhoff-saga-part-three-arrogance-impunity-and-entitlement/ · Wayback: https://web.archive.org/web/20250710234459/https://www.businesslive.co.za/rdm/business/2018-06-20-the-steinhoff-saga-part-three-arrogance-impunity-and-entitlement/ (existent; cita no verificada a la captura) · id: `ND1-ST11`

12. [`ND1-ST12`] [V] «Although Jooste was not the founder of the company, he behaved as if Steinhoff and its assets belonged to him personally.»
   Nivell B · prova: versió de premsa B, a la URL original, de ND1-ST5 (corroboració; no és cap prova a-e) · URL: https://www.businesslive.co.za/rdm/business/2018-06-20-the-steinhoff-saga-part-three-arrogance-impunity-and-entitlement/ · Wayback: https://web.archive.org/web/20250710234459/https://www.businesslive.co.za/rdm/business/2018-06-20-the-steinhoff-saga-part-three-arrogance-impunity-and-entitlement/ (existent; cita no verificada a la captura) · id: `ND1-ST12`

13. [`ND1-ST13`] [V] «Markus Johannes (Markus) Jooste South African, Male (date of birth: 22 January 1961)»
   Nivell A · prova: naixement de Jooste (22/01/1961) en un document de l'emissor; corrobora ND1-ST1 · URL: https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20230926192658/https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf (existent; cita no verificada a la captura) · id: `ND1-ST13`

14. [`ND1-ST14`] [V] «Bruno Steinhoff is the founder of the Group and was chairman of Steinhoff Limited until the end of September 2008.»
   Nivell A · prova: l'emissor anomena Bruno Steinhoff fundador del grup · URL: https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20230926192658/https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf (existent; cita no verificada a la captura) · id: `ND1-ST14`

15. [`ND1-ST15`] [V] «Bruno Steinhoff started his furniture trade and distribution business in Westerstede, Germany, in June 1964.»
   Nivell A · prova: l'emissor situa l'inici del negoci de Bruno Steinhoff el juny de 1964 (amb 1964 la regla b també es compleix: 1964−1961=3) · URL: https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20230926192658/https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf (existent; cita no verificada a la captura) · id: `ND1-ST15`

16. [`ND1-ST16`] [V] «During the Reporting Period, Markus Jooste served as the Company’s Chief Executive Officer.»
   Nivell A · prova: CEO durant l'exercici 1/10/2016-30/9/2017 (cobreix el 31/10/2016) · URL: https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20230926192658/https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf (existent; cita no verificada a la captura) · id: `ND1-ST16`

17. [`ND1-ST17`] [V] «Markus Jooste was appointed on 30 November 2015. On 4 December 2017, Markus Jooste offered to resign as Chief»
   Nivell A · prova: CEO des del 30/11/2015; ofereix la dimissió el 4/12/2017 (primera meitat de la frase; la segona és ND1-ST18) · URL: https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20230926192658/https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf (existent; cita no verificada a la captura) · id: `ND1-ST17`

18. [`ND1-ST18`] [V] «Executive Officer and Managing Director of the Company, which offer was accepted by the Supervisory Board on 5 December 2017.»
   Nivell A · prova: dimissió acceptada el 5/12/2017: CEO el 31/10/2017 (prova d'interval retrospectiva) · URL: https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20230926192658/https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf (existent; cita no verificada a la captura) · id: `ND1-ST18`

19. [`ND1-ST19`] [V] «The three formed a joint venture in SA that would become the platform for the modern Steinhoff.»
   Nivell B · prova: contraprova considerada per a Doctorat: l'empresa conjunta de 1995-1998 com a plataforma de l'Steinhoff modern · URL: https://amabhungane.org/steinhoffs-secret-history-how-markus-joostes-scam-began/ · Wayback: https://web.archive.org/web/20260714013131/https://amabhungane.org/steinhoffs-secret-history-how-markus-joostes-scam-began/ (existent; cita no verificada a la captura) · id: `ND1-ST19`

20. [`ND1-ST20`] [V] «Jooste floated the idea of merging the South African assets of Daun with Steinhoff Europe»
   Nivell B · prova: contraprova considerada per a Doctorat: paper de Jooste en la fusió dels actius sud-africans amb Steinhoff Europe (1996) · URL: https://www.businesslive.co.za/rdm/business/2018-06-15-the-steinhoff-saga-part-one-the-making-of-a-corporate-giant/ · Wayback: https://web.archive.org/web/20250613221240/https://www.businesslive.co.za/rdm/business/2018-06-15-the-steinhoff-saga-part-one-the-making-of-a-corporate-giant/ (existent; cita no verificada a la captura) · id: `ND1-ST20`

21. [`ND1-ST21`] [V] «Steinhoff N.V. was introduced as a new holding company and, as a result of the earlier consolidation of GIH, there was no change to the underlying assets of the Group when Steinhoff N.V. was incorporated as the ultimate holding company.»
   Nivell A · prova: contraprova considerada per a Doctorat: l'emissor cotitzat (N.V.) és un holding nou de 2015, sense canvi en els actius subjacents · URL: https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20230926192658/https://irpages2.eqs.com/Download/Companies/steinhoffintnv/Annual%20Reports/NL0011375019-JA-2016-EQ-E-00.pdf (existent; cita no verificada a la captura) · id: `ND1-ST21`


### Drillisch AG Inhaber-Aktien o.N. (`DE0005545503`)

- isin i anys: `DE0005545503`, 2017 (n=1). CEO: Vlasios Choulidis.
- FounderCEO actual → proposat: **no_determinat (ND) → no_determinat (sense canvi)**.
- Regla aplicada: cap (indeterminat).
- Justificació: Es manté ND. CEO del 31/10/2017 confirmat [`ND1-DR1`, `ND1-DR2`]. Cap prova de «no» s'aplica: b no (naixement 1958 al mateix CV); d no, perquè la cronologia de l'emissor situa la fundació de Drillisch AG el 1997 [`ND1-DR5`] i la integració del grup Alphatel l'octubre de 1998 [`ND1-DR7`], menys de 3 anys després; a i e no. Tampoc hi ha prova de «sí»: el CV diu que va fundar E.I.C. GmbH (incl. grup Alphatel), integrada al grup Drillisch el 1998 [`ND1-DR3`], després de la sortida a borsa [`ND1-DR6`]; cap document obert descriu E.I.C./Alphatel com a predecessora jurídica o econòmica de la cotitzada ni l'anomena fundador de Drillisch (D37).
- Cerca feta: Oberts i llegits: CV oficial en alemany i en anglès (imagepool.1und1.ag), informe anual 2003 de Drillisch (cronologia «Unternehmenshistorie»), comptes anuals 2016 de Drillisch AG, informe anual 2017 en anglès. Cerca web (pista, no evidència): «Drillisch AG Geschichte 1997 Alphatel Choulidis», perfils d'agregadors (font C, descartats). No s'ha trobat el fullet de la sortida a borsa de 1998 ni cap document del registre mercantil sobre l'operació d'octubre de 1998 (aportació, compra o fusió); és el document que podria reobrir el cas.
- **Correccions de DF (19/11/2026): documentació de l'operació d'octubre de 1998.** Es manté ND (indeterminat).
- Forma de l'operació: adquisició, no fusió. Drillisch AG compra el 100% d'E.I.C. Beteiligungs-GmbH (societat de control del grup Alphatel) [`ND1-DR10`, `ND1-DR14`] i la consolida pel mètode d'adquisició (IAS 22) [`ND1-DR11`]. Contraprestació mixta: ampliació de capital per aportació no dinerària (Sacheinlage) de participacions d'AlphaTel GmbH el 22/10/1998 [`ND1-DR8`, `ND1-DR9`] i una resta de preu en efectiu de 6,5 milions de DM [`ND1-DR12`]. L'única fusió (Verschmelzung) documentada és interna del subgrup Alphatel, amb efecte 1/1/1999 [`ND1-DR13`]. Comunicat de l'emissor del 23/10/1998 [`ND1-DR20`].
- Percentatges: les accions noves de l'aportació són el 9,67% del capital posterior a l'ampliació (càlcul propi amb les dues xifres de [`ND1-DR8`]: 492.650,18 / 5.094.277,11 EUR; no és cita). Cap document A/B trobat diu qui va rebre aquestes accions ni en quina proporció.
- D37 i predecessora: l'emissor anomena Choulidis «einer der Gründer der Alphatel-Gruppe» [`ND1-DR15`], una altra entitat (la filial adquirida), i data la fundació de Drillisch AG el 1997 [`ND1-DR16`]. Cap document descriu E.I.C./Alphatel com a predecessora de Drillisch AG ni anomena Choulidis fundador de Drillisch.
- Proves de «no»: b no (naixement el 1958 [`ND1-DR19`]); c no (hi ha dada d'edat); d no amb la fundació de 1997 (menys de 3 anys). Punt per a Doctorat (no decidit): hi havia un grup Drillisch anterior a l'AG [`ND1-DR17`] i l'emissor parla de «Vorgängergesellschaften» sense dir quines [`ND1-DR18`]; si el 1997 fos una reorganització i no una fundació nova, la fundació rellevant seria anterior i caldria decidir també si entrar per la venda de la pròpia empresa és «incorporació tardana».
- Dates a les fonts A: adquisició l'1/10/1998 [`ND1-DR10`], ampliació de capital el 22/10/1998 [`ND1-DR8`] i junta extraordinària convocada per al 23/10/1998 [`ND1-DR20`]; cap document no explica la seqüència ni dona el resultat de la votació.
- No trobat: informe anual 1998, fullet de la sortida a borsa de 1998, informe de l'aportació no dinerària, acta de la junta del 23/10/1998, inscripcions al registre mercantil de 1998, i l'ad hoc DGAP del 17/07/1998 a la URL original (només una còpia a aktiencheck.de, que és pista). Cerca addicional (19/11/2026): informes anuals 1999, 2001 i 2003 i informes trimestrals 1999-2000 (imagepool.1und1.ag i imagepool.drillisch.de, fitxers idèntics; 17 noms de fitxer de 1998-2000 provats amb 404); comunicats a OTS (23/10/1998, 30/12/1998, 21/1/1999, 18/3/1999) i cerques a OTS; DGAP/EQS (redirigeixen a la portada); Börsen-Zeitung (B); Wirtschaftswoche i Handelsblatt (pàgines sense contingut, no evidència); teltarif (sense dades de 1998).
- Cites:

1. [`ND1-DR1`] [V] «Mitglied des Vorstands und bis zum 31.12.2017 Vorstandssprecher der Drillisch Aktiengesellschaft, Maintal»
   Nivell A · prova: CEO el 31/10/2017 (portaveu del consell fins al 31/12/2017) · URL: https://imagepool.1und1.ag/v2/download/HV/2018/2018-03-05-Lebenslauf_Vlasios-Choulidis_Drillisch-DEU.pdf · Wayback: https://web.archive.org/web/20240615184021/https://imagepool.1und1.ag/v2/download/HV/2018/2018-03-05-Lebenslauf_Vlasios-Choulidis_Drillisch-DEU.pdf (existent; cita no verificada a la captura) · id: `ND1-DR1`

2. [`ND1-DR2`] [V] «Mr Ralph Dommermuth was appointed as CEO, effective per 1 January 2018.»
   Nivell A · prova: el successor comença l'1/1/2018 · URL: https://imagepool.1und1.ag/v2/download/berichte/2018-03-22_Drillisch_GB_2017_ENGLISH.pdf · Wayback: https://web.archive.org/web/20250908144015/https://imagepool.1und1.ag/v2/download/berichte/2018-03-22_Drillisch_GB_2017_ENGLISH.pdf (existent; cita no verificada a la captura) · id: `ND1-DR2`

3. [`ND1-DR3`] [V] «Gründung und Leitung der E.I.C. GmbH (inkl. Alphatel-Gruppe), die im Jahr 1998 in den Drillisch-Konzern integriert wurde»
   Nivell A · prova: fundador d'E.I.C./Alphatel, integrada a Drillisch el 1998 · URL: https://imagepool.1und1.ag/v2/download/HV/2018/2018-03-05-Lebenslauf_Vlasios-Choulidis_Drillisch-DEU.pdf · Wayback: https://web.archive.org/web/20240615184021/https://imagepool.1und1.ag/v2/download/HV/2018/2018-03-05-Lebenslauf_Vlasios-Choulidis_Drillisch-DEU.pdf (existent; cita no verificada a la captura) · id: `ND1-DR3`

4. [`ND1-DR4`] [V] «Honeywell Deutschland GmbH (Vertriebsingenieur für Gebäudeleitsysteme)»
   Nivell A · prova: ocupador anterior (1987-1991) · URL: https://imagepool.1und1.ag/v2/download/HV/2018/2018-03-05-Lebenslauf_Vlasios-Choulidis_Drillisch-DEU.pdf · Wayback: https://web.archive.org/web/20240615184021/https://imagepool.1und1.ag/v2/download/HV/2018/2018-03-05-Lebenslauf_Vlasios-Choulidis_Drillisch-DEU.pdf (existent; cita no verificada a la captura) · id: `ND1-DR4`

5. [`ND1-DR5`] [V] «Gründung der Drillisch AG»
   Nivell A · prova: cronologia de l'emissor: 1997, fundació de Drillisch AG · URL: https://imagepool.1und1.ag/download/berichte/2003-GB-Konzern220304.pdf · Wayback: https://web.archive.org/web/20240615190827/https://imagepool.1und1.ag/download/berichte/2003-GB-Konzern220304.pdf (existent; cita no verificada a la captura) · id: `ND1-DR5`

6. [`ND1-DR6`] [V] «Börsengang am 22.04.1998»
   Nivell A · prova: cronologia de l'emissor: sortida a borsa · URL: https://imagepool.1und1.ag/download/berichte/2003-GB-Konzern220304.pdf · Wayback: https://web.archive.org/web/20240615190827/https://imagepool.1und1.ag/download/berichte/2003-GB-Konzern220304.pdf (existent; cita no verificada a la captura) · id: `ND1-DR6`

7. [`ND1-DR7`] [V] «Integration der AlphatelGruppe»
   Nivell A · prova: cronologia de l'emissor: 10/98, integració del grup Alphatel · URL: https://imagepool.1und1.ag/download/berichte/2003-GB-Konzern220304.pdf · Wayback: https://web.archive.org/web/20240615190827/https://imagepool.1und1.ag/download/berichte/2003-GB-Konzern220304.pdf (existent; cita no verificada a la captura) · id: `ND1-DR7`

8. [`ND1-DR8`] [V] «Das Grundkapital wurde am 22. Oktober 1998 durch Sacheinlage um 492.650,18 Euro auf 5.094.277,11 Euro erhöht (Integration Alphatel GmbH).»
   Nivell A · prova: forma jurídica: ampliació de capital per aportació no dinerària (Sacheinlage) el 22/10/1998, lligada a la integració d'Alphatel; les accions noves són el 9,67% del capital posterior (càlcul propi: 492.650,18/5.094.277,11) · URL: https://imagepool.1und1.ag/download/berichte/2001-GB-D-01.pdf · Wayback: https://web.archive.org/web/20240616082735/https://imagepool.1und1.ag/download/berichte/2001-GB-D-01.pdf (existent; cita no verificada a la captura) · id: `ND1-DR8`

9. [`ND1-DR9`] [V] «Der Unterschied zwischen der Kapitalrücklage der Drillisch AG und des Konzerns in Höhe von TDM 24.699 resultiert aus der unterschiedlichen Bewertung der 1998 eingebrachten Anteile an der AlphaTel GmbH nach HGB und IAS.»
   Nivell A · prova: els béns aportats el 1998 eren participacions d'AlphaTel GmbH · URL: https://imagepool.1und1.ag/download/berichte/1999-GB.pdf · Wayback: https://web.archive.org/web/20240616013158/https://imagepool.1und1.ag/download/berichte/1999-GB.pdf (existent; cita no verificada a la captura) · id: `ND1-DR9`

10. [`ND1-DR10`] [V] «In die Vorjahreskonzernzahlen wurden die AlphaTel GmbH und die Shop GmbH ab dem Zeitpunkt des Erwerbs (1. Oktober 1998) einbezogen.»
   Nivell A · prova: data de l'adquisició: 1/10/1998 · URL: https://imagepool.1und1.ag/download/berichte/1999-GB.pdf · Wayback: https://web.archive.org/web/20240616013158/https://imagepool.1und1.ag/download/berichte/1999-GB.pdf (existent; cita no verificada a la captura) · id: `ND1-DR10`

11. [`ND1-DR11`] [V] «Die Kapitalkonsolidierung erfolgte gemäß IAS 22 nach der Erwerbsmethode»
   Nivell A · prova: consolidació pel mètode d'adquisició (IAS 22): Drillisch és l'adquirent · URL: https://imagepool.1und1.ag/download/berichte/1999-GB.pdf · Wayback: https://web.archive.org/web/20240616013158/https://imagepool.1und1.ag/download/berichte/1999-GB.pdf (existent; cita no verificada a la captura) · id: `ND1-DR11`

12. [`ND1-DR12`] [V] «Bei den Investitionen in den Erwerb der E.I.C.-GmbH (Alphatel-Gruppe) und der NetControl GmbH handelt es sich mit 6,5 Mio. DM um die Restkaufpreisverpflichtung für den Erwerb der E.I.C.-GmbH»
   Nivell A · prova: contraprestació mixta: resta de preu de compra en efectiu de 6,5 milions de DM per l'adquisició d'E.I.C. · URL: https://imagepool.1und1.ag/download/berichte/1999-Q3.pdf · Wayback: https://web.archive.org/web/20240615183948/https://imagepool.1und1.ag/download/berichte/1999-Q3.pdf (existent; cita no verificada a la captura) · id: `ND1-DR12`

13. [`ND1-DR13`] [V] «auf die E.I.C. Beteiligungs-GmbH, Maintal, verschmolzen wurden. Gleichzeitig wurde die E.I.C. Beteiligungs GmbH umfirmiert in AlphaTel Kommunikationstechnik GmbH.»
   Nivell A · prova: l'única fusió (Verschmelzung) és interna del subgrup Alphatel (efecte 1/1/1999); E.I.C. canvia de nom · URL: https://imagepool.1und1.ag/download/berichte/1999-GB.pdf · Wayback: https://web.archive.org/web/20240616013158/https://imagepool.1und1.ag/download/berichte/1999-GB.pdf (existent; cita no verificada a la captura) · id: `ND1-DR13`

14. [`ND1-DR14`] [V] «durch seine 100%ige Tochtergesellschaft Alphatel GmbH»
   Nivell A · prova: Alphatel GmbH és filial al 100% de Drillisch AG · URL: https://imagepool.1und1.ag/download/berichte/2000-Q1.pdf · Wayback: https://web.archive.org/web/20230320135706/https://imagepool.1und1.ag/download/berichte/2000-Q1.pdf (existent; cita no verificada a la captura) · id: `ND1-DR14`

15. [`ND1-DR15`] [V] «der HONEYWELL Deutschland GmbH und war nebenberuflich selbstständig. Herr Choulidis ist einer der Gründer der Alphatel-Gruppe, die im Jahr 1998 in den Drillisch-Konzern integriert wurde.»
   Nivell A · prova: l'emissor anomena Choulidis un dels fundadors del grup Alphatel (una altra entitat), no de Drillisch · URL: https://imagepool.1und1.ag/download/berichte/2001-GB-D-01.pdf · Wayback: https://web.archive.org/web/20240616082735/https://imagepool.1und1.ag/download/berichte/2001-GB-D-01.pdf (existent; cita no verificada a la captura) · id: `ND1-DR15`

16. [`ND1-DR16`] [V] «Herr Brucherseifer ist Vorstandssprecher der 1997 gegründeten Drillisch AG»
   Nivell A · prova: l'emissor data la fundació de Drillisch AG el 1997 · URL: https://imagepool.1und1.ag/download/berichte/2001-GB-D-01.pdf · Wayback: https://web.archive.org/web/20240616082735/https://imagepool.1und1.ag/download/berichte/2001-GB-D-01.pdf (existent; cita no verificada a la captura) · id: `ND1-DR16`

17. [`ND1-DR17`] [V] «Seit 1994 ist er in der Geschäftsleitung der Drillisch-Gruppe tätig.»
   Nivell A · prova: hi havia un grup Drillisch anterior a l'AG (Brucherseifer, a la direcció des del 1994): punt per a Doctorat sobre la fundació rellevant · URL: https://imagepool.1und1.ag/download/berichte/2001-GB-D-01.pdf · Wayback: https://web.archive.org/web/20240616082735/https://imagepool.1und1.ag/download/berichte/2001-GB-D-01.pdf (existent; cita no verificada a la captura) · id: `ND1-DR17`

18. [`ND1-DR18`] [V] «Durch die mehr als 20-jährige Tätigkeit von Drillisch und den Vorgängergesellschaften im Mobilfunkmarkt hat sich das Unternehmen eine Vertrauensposition bei den Kunden und Netzanbietern erarbeitet.»
   Nivell A · prova: l'emissor esmenta «Vorgängergesellschaften» sense dir quines · URL: https://imagepool.1und1.ag/v2/download/HV/2018/DAG-Jahresabschluss-2016.pdf · Wayback: https://web.archive.org/web/20240616054505/https://imagepool.1und1.ag/v2/download/HV/2018/DAG-Jahresabschluss-2016.pdf (existent; cita no verificada a la captura) · id: `ND1-DR18`

19. [`ND1-DR19`] [V] «Aufsichtsrat, Gelnhausen, Deutschland Geburtsjahr: 1958»
   Nivell A · prova: any de naixement de Choulidis (1958): b no s'aplica · URL: https://imagepool.1und1.ag/v2/download/HV/2018/2018-03-05-Lebenslauf_Vlasios-Choulidis_Drillisch-DEU.pdf · Wayback: https://web.archive.org/web/20240615184021/https://imagepool.1und1.ag/v2/download/HV/2018/2018-03-05-Lebenslauf_Vlasios-Choulidis_Drillisch-DEU.pdf (existent; cita no verificada a la captura) · id: `ND1-DR19`

20. [`ND1-DR20`] [V] «Integration Alphatel-Gruppe (mit einem garantierten Jahresüberschuß 1998 nach Steuern von 3,2 Mio DM)»
   Nivell A · prova: comunicat de l'emissor del 23/10/1998 (OTS): integració del grup Alphatel amb un benefici garantit per al 1998 · URL: https://www.ots.at/presseaussendung/OTS_19981023_OTS0021/drillisch-ag-paragraph-15-wphg-mitteilung · Wayback: https://web.archive.org/web/20251005163025/https://www.ots.at/presseaussendung/OTS_19981023_OTS0021/drillisch-ag-paragraph-15-wphg-mitteilung (existent; cita no verificada a la captura) · id: `ND1-DR20`


### Sopra Steria Group S.A. Actions Port. EO 1 (`FR0000050809`)

- isin i anys: `FR0000050809`, 2025 (n=1). CEO: Xavier Pecquet.
- FounderCEO actual → proposat: **no_determinat (ND) → no_determinat (sense canvi)**.
- Regla aplicada: cap (indeterminat).
- Justificació: Es manté ND. CEO del 31/10/2025 confirmat: Xavier Pecquet, nomenat Directeur Général el 8/10/2025 fins a l'arribada del successor, que comença el 2/2/2026 [`ND1-SS1`, `ND1-SS2`, `ND1-SS3`, `ND1-SS6`] (un CEO interí compta, R2). Cap prova de «no» s'aplica: b no (naixement 1950 a la base; Sopra 1968 [`ND1-SS4`] i Steria 1969 [`ND1-SS5`]); a no, perquè l'emissor parla de «He and his associates» i de «co-founded» sense donar una llista tancada; d no, perquè no s'ha trobat cap document A/B amb la data d'incorporació de Pecquet a Sopra ni el seu ocupador anterior. Tampoc hi ha cap cita que l'anomeni fundador.
- Cerca feta: Oberts i llegits: Document d'enregistrement universel 2025 (versió anglesa, soprasteria.com i còpia a live.euronext.com), comunicat de governança del 8/10/2025, comunicat de nomenament del 12/12/2025, pàgina de governança de soprasteria.com, fitxa personal a soprasteria.fr (sense biografia), La Lettre des Masters núm. 55 (març 2017; presenta Aeroline, sense dates de carrera de Pecquet). Cerca web (pista): «Xavier Pecquet Sopra joined / a rejoint / entré chez Sopra»; només agregadors i registres (font C). Falta: un document de l'emissor (document de référence antic o comunicat) amb l'any d'entrada a Sopra i l'ocupador anterior.
- Cites:

1. [`ND1-SS1`] [V] «appointed Xavier Pecquet as Chief Executive Officer until the arrival of a new Chief Executive Officer recruited from outside the Group.»
   Nivell A · prova: CEO el 31/10/2025 · URL: https://www.soprasteria.com/docs/librariesprovider2/sopra-steria-corporate/finance/rapports-financiers/sopra_steria_urd_2025_en_assemblage_opti.pdf · Wayback: https://web.archive.org/web/20260321043614/https://www.soprasteria.com/docs/librariesprovider2/sopra-steria-corporate/finance/rapports-financiers/sopra_steria_urd_2025_en_assemblage_opti.pdf (existent; cita no verificada a la captura) · id: `ND1-SS1`

2. [`ND1-SS2`] [V] «Xavier Pecquet was appointed Chief Executive Officer with effect from 8 October 2025.»
   Nivell A · prova: inici del mandat (8/10/2025) · URL: https://www.soprasteria.com/docs/librariesprovider2/sopra-steria-corporate/finance/rapports-financiers/sopra_steria_urd_2025_en_assemblage_opti.pdf · Wayback: https://web.archive.org/web/20260321043614/https://www.soprasteria.com/docs/librariesprovider2/sopra-steria-corporate/finance/rapports-financiers/sopra_steria_urd_2025_en_assemblage_opti.pdf (existent; cita no verificada a la captura) · id: `ND1-SS2`

3. [`ND1-SS3`] [V] «Sopra Steria’s Board of Directors duly noted Cyril Malargé’s decision to pursue a new opportunity and to step down as Chief Executive Officer.»
   Nivell A · prova: sortida del CEO anterior (8/10/2025) · URL: https://www.soprasteria.com/docs/librariesprovider2/sopra-steria-corporate/finance/cp-fi/sopra-steria_governance_08102025_en_def2.pdf?sfvrsn=670a37db_6 · Wayback: https://web.archive.org/web/20260122230142/https://www.soprasteria.com/docs/librariesprovider2/sopra-steria-corporate/finance/cp-fi/sopra-steria_governance_08102025_en_def2.pdf?sfvrsn=670a37db_6 (existent; cita no verificada a la captura) · id: `ND1-SS3`

4. [`ND1-SS4`] [V] «He and his associates founded Sopra Group in 1968, and he chairs the Board of Directors.»
   Nivell A · prova: fundació de Sopra (Pierre Pasquier i socis, 1968; llista no tancada) · URL: https://www.soprasteria.com/docs/librariesprovider2/sopra-steria-corporate/finance/rapports-financiers/sopra_steria_urd_2025_en_assemblage_opti.pdf · Wayback: https://web.archive.org/web/20260321043614/https://www.soprasteria.com/docs/librariesprovider2/sopra-steria-corporate/finance/rapports-financiers/sopra_steria_urd_2025_en_assemblage_opti.pdf (existent; cita no verificada a la captura) · id: `ND1-SS4`

5. [`ND1-SS5`] [V] «Éric Hayat co-founded Groupe Steria in 1969 and served as its Deputy Chief Executive Officer.»
   Nivell A · prova: fundació de Steria (1969; llista no tancada) · URL: https://www.soprasteria.com/docs/librariesprovider2/sopra-steria-corporate/finance/rapports-financiers/sopra_steria_urd_2025_en_assemblage_opti.pdf · Wayback: https://web.archive.org/web/20260321043614/https://www.soprasteria.com/docs/librariesprovider2/sopra-steria-corporate/finance/rapports-financiers/sopra_steria_urd_2025_en_assemblage_opti.pdf (existent; cita no verificada a la captura) · id: `ND1-SS5`

6. [`ND1-SS6`] [V] «He will take up his new role on 2 February 2026.»
   Nivell A · prova: el successor (Rajesh Krishnamurthy) comença el 2/2/2026 · URL: https://www.soprasteria.com/docs/librariesprovider2/sopra-steria-corporate/finance/cp-fi/sopra-steria_-ceo-announcement_eng.pdf · Wayback: `pendent_verificacio_externa` · id: `ND1-SS6`


### Aroundtown SA (`LU1673108939`)

- isin i anys: `LU1673108939`, 2017-2020 (n=4). CEO: Shmuel Mayo.
- FounderCEO actual → proposat: **no_determinat (ND) → no_determinat (sense canvi)**.
- Regla aplicada: cap (indeterminat).
- Justificació: Es manté ND. CEO confirmat fins al 25/11/2020 [`ND1-AT5`]. Cap prova de «no» s'aplica amb les regles vigents: d no, perquè Mayo és a la direcció des del 2006 [`ND1-AT1`], només 2 anys després de la constitució del 2004 [`ND1-AT3`], encara que l'emissor cita l'ocupador anterior [`ND1-AT2`]; a no, perquè l'emissor anomena Yakir Gabay «Founder of the Group in 2004» [`ND1-AT4`] però no presenta cap llista de fundadors com a completa; b, c i e no. Tampoc hi ha cap cita que anomeni Mayo fundador. Es deixa a Doctorat la qüestió de si un fundador únic anomenat per l'emissor equival a una llista tancada (prova a); aquí no s'ha forçat.
- Cerca feta: Oberts i llegits: informes anuals 2016, 2017, 2018, 2019 i 2020 d'Aroundtown, informe de remuneracions 2020, presentacions de resultats Q1 2017, Q3 2017, FY 2017, FY 2018 i FY 2019. Cerca web (pista): fullet d'admissió i biografies; només agregadors (font C). No s'ha trobat el fullet d'admissió a Prime Standard (2017) a la web de l'emissor (la pàgina de fullets retorna 404).
- **Correccions de DF (19/11/2026): recerca addicional.** Es manté ND (indeterminat) a les quatre files.
- Llista tancada de fundadors: no s'ha trobat. L'emissor només anomena Yakir Gabay, amb la fórmula «Founder of the Group in 2004» [`ND1-AT4`] (presentacions Q3 2018, Q3 2019, H1 2020 i Q3 2020 i presentació corporativa actual; no a la presentació Q3 2017), sense «sole» ni «only». La Börsen-Zeitung l'anomena «Aroundtown-Gründer» [`ND1-AT10`]. Els fullets de 2017 (CySEC) i 2019 (CSSF) tenen secció d'història però no anomenen cap fundador. Si un sol fundador anomenat equival a llista tancada (prova a) continua sent decisió de Doctorat.
- Any de naixement de Mayo: 1961 [`ND1-AT6`] (fullet d'admissió aprovat per CySEC, 30/5/2017). b no s'aplica (2004 − 1961 = 43); c no s'aplica (hi ha dada d'edat). d tampoc: a la direcció des del 2006 i CEO des del novembre de 2014 [`ND1-AT7`], constitució el maig de 2004 [`ND1-AT9`], ocupador anterior citat [`ND1-AT8`].
- CEO únic el 31/10 de 2017, 2018 i 2019 [`ND1-AT11`, `ND1-AT12`, `ND1-AT13`]; el 2018 i el 2019 Andrew Wallis era Deputy CEO, no co-CEO.
- L'altre co-CEO del 2020 és Barak Bar-Hen, però les fonts no coincideixen sobre la data d'inici: el comunicat del 29/10/2020 diu que el nomenament «became effective» [`ND1-AT14`]; l'informe de remuneracions i l'informe anual 2020 diuen que va començar l'1/11/2020 [`ND1-AT15`, `ND1-AT16`]; TLG diu que va plegar com a CEO de TLG al final del 31/10/2020 [`ND1-AT17`]. Cap cita A/B l'anomena fundador; l'emissor diu que es va incorporar a la direcció «this quarter» i que abans era CEO de TLG [`ND1-AT18`]. Amb R1 («compta des del dia en què comença a exercir») la majoria de fonts situen el 31/10/2020 abans del co-CEO. Si Doctorat dona prioritat al comunicat del 29/10, la fila 2020 tindria dos CEO, cosa que tocaria `ceos` (fora de l'abast d'aquest lot). En cap dels dos casos canvia FounderCEO: amb Mayo indeterminat, la regla de co-CEO no pot donar 0.
- Punt nou per a Doctorat (no aplicat): Gabay presidia l'Advisory Board el 2017 [`ND1-AT19`] i n'era vicepresident el 2018-2020 [`ND1-AT20`]; l'Advisory Board no és un òrgan estatutari ni té autoritat societària [`ND1-AT21`]. Cal decidir si la regla «Si el fundador és president i el CEO és una altra persona, la classificació és 0» s'aplica a aquest càrrec. A més, la base parla de «fundació rellevant 2004/2007», però no s'ha trobat cap font del 2007 (l'únic fet posterior és el trasllat de seu de Xipre a Luxemburg del 2017, que és la mateixa societat).
- Cerca addicional (19/11/2026): fullet d'admissió al Prime Standard (30/5/2017, CySEC); fullet de valors CSSF (17/12/2019); document d'oferta per TLG (18/12/2019) i presentació de la fusió; informes i presentacions Q3 2017-2020 i H1 2020; informe anual 2020 i informe de remuneracions 2020; informes anuals 2014 i 2015; presentació corporativa vigent; webs de l'emissor (direcció, empresa, 254 notícies, entre les quals les del 2/6/2020, 29/10/2020 i 25/11/2020); fullets de bons d'ATF Netherlands a Euronext Dublin (2016-2017); Grand City Properties (direcció i presentació Q3 2020); informe del consell de supervisió de TLG 2020 i comunicat de TLG a EQS; Börsen-Zeitung, Calcalist, Globes i Walla (pistes); Cyprus Business Now (2023, «founded in 2004 by Yakir Gabay»: nivell dubtós, només pista). Cap cita A/B anomena Mayo fundador.
- Cites:

1. [`ND1-AT1`] [V] «Mr. Mayo is since 2006 in the management of Aroundtown and its subsidiaries»
   Nivell A · prova: incorporació de Shmuel Mayo (2006) · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/Q1%202017%20Financials/q1_2017-financials-presentation.pdf · Wayback: https://web.archive.org/web/20250208224250/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/Q1%202017%20Financials/q1_2017-financials-presentation.pdf (existent; cita no verificada a la captura) · id: `ND1-AT1`

2. [`ND1-AT2`] [V] «Previously, Mr. Mayo was the CEO of the Dankner Group»
   Nivell A · prova: ocupador anterior · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/Q1%202017%20Financials/q1_2017-financials-presentation.pdf · Wayback: https://web.archive.org/web/20250208224250/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/Q1%202017%20Financials/q1_2017-financials-presentation.pdf (existent; cita no verificada a la captura) · id: `ND1-AT2`

3. [`ND1-AT3`] [V] «Aroundtown Property Holdings PLC (“the Company”) was incorporated on May 7, 2004 as a private limited liability company under the Cyprus Companies Law, Cap. 113.»
   Nivell A · prova: constitució (7/5/2004) · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/FY%202016%20Financials/at_fy_2016.pdf · Wayback: https://web.archive.org/web/20251209043547/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/FY%202016%20Financials/at_fy_2016.pdf (existent; cita no verificada a la captura) · id: `ND1-AT3`

4. [`ND1-AT4`] [V] «Advisory Board Deputy Chairman. Founder of the Group in 2004.»
   Nivell A · prova: l'emissor anomena Yakir Gabay fundador del grup (2004); no és una llista declarada completa · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/FY%202018%20Financials/AT_FY_2018_financial_presentation.pdf · Wayback: https://web.archive.org/web/20250208220734/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/FY%202018%20Financials/AT_FY_2018_financial_presentation.pdf (existent; cita no verificada a la captura) · id: `ND1-AT4`

5. [`ND1-AT5`] [V] «Mr. Shmuel Mayo stepped down from his position as CEO on November 25, 2020.»
   Nivell A · prova: fi del mandat (25/11/2020): CEO el 31/10/2020 · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/General%20Meetings/AGM%202021/2020_AT_Remuneration_Report.pdf · Wayback: https://web.archive.org/web/20251110192339/https://www.aroundtown.de/aroundtown.de/Data_Objects/General%20Meetings/AGM%202021/2020_AT_Remuneration_Report.pdf (existent; cita no verificada a la captura) · id: `ND1-AT5`

6. [`ND1-AT6`] [V] «Mr. Mayo was born in 1961 in Israel.»
   Nivell A · prova: any de naixement de Mayo (1961): b no s'aplica (2004−1961=43) · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Share/aroundtown_property_holdings_plc_prospectus.pdf · Wayback: https://web.archive.org/web/20260415191132/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Share/aroundtown_property_holdings_plc_prospectus.pdf (existent; cita no verificada a la captura) · id: `ND1-AT6`

7. [`ND1-AT7`] [V] «Since 2006 Mr. Mayo has occupied various management positions in the Company. In November 2014 Mr. Mayo was appointed the Company’s CEO.»
   Nivell A · prova: Mayo a la direcció des del 2006 i CEO des del novembre de 2014 · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Share/aroundtown_property_holdings_plc_prospectus.pdf · Wayback: https://web.archive.org/web/20260415191132/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Share/aroundtown_property_holdings_plc_prospectus.pdf (existent; cita no verificada a la captura) · id: `ND1-AT7`

8. [`ND1-AT8`] [V] «From 2002 to 2004 he was the CFO and Business Development Manager at Galor System & Software Development ltd.»
   Nivell A · prova: ocupador anterior de Mayo (2002-2004) · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Share/aroundtown_property_holdings_plc_prospectus.pdf · Wayback: https://web.archive.org/web/20260415191132/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Share/aroundtown_property_holdings_plc_prospectus.pdf (existent; cita no verificada a la captura) · id: `ND1-AT8`

9. [`ND1-AT9`] [V] «Incorporation of the Company in May 2004 under the name Redspot Media Limited and change of name into Aroundtown Property Holdings Limited in October 2004.»
   Nivell A · prova: constitució de la societat el maig de 2004 · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Share/aroundtown_property_holdings_plc_prospectus.pdf · Wayback: https://web.archive.org/web/20260415191132/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Share/aroundtown_property_holdings_plc_prospectus.pdf (existent; cita no verificada a la captura) · id: `ND1-AT9`

10. [`ND1-AT10`] [V] «Hinter Avisco steht der in London lebende israelische Milliardär und Aroundtown-Gründer Yakir Gabay mit 40 % der Anteile.»
   Nivell B · prova: premsa B: Gabay «Aroundtown-Gründer» (un sol nom, sense presentar-lo com a llista completa) · URL: https://www.boersen-zeitung.de/unternehmen-branchen/tlg-und-aroundtown-fadeln-milliardenfusion-ein · Wayback: https://web.archive.org/web/20250914113340/https://www.boersen-zeitung.de/unternehmen-branchen/tlg-und-aroundtown-fadeln-milliardenfusion-ein (existent; cita no verificada a la captura) · id: `ND1-AT10`

11. [`ND1-AT11`] [V] «SENIOR AND KEY MANAGEMENT Name Position Mr. Shmuel Mayo CEO Mr. Eyal Ben David CFO»
   Nivell A · prova: CEO únic a la data de l'informe Q3 2017 (27/11/2017) · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/Q3%202017%20Financials/at_q3_2017.pdf · Wayback: https://web.archive.org/web/20250208222559/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/Q3%202017%20Financials/at_q3_2017.pdf (existent; cita no verificada a la captura) · id: `ND1-AT11`

12. [`ND1-AT12`] [V] «Mr. Shmuel Mayo CEO Mr. Andrew Wallis Deputy CEO»
   Nivell A · prova: CEO i Deputy CEO (no co-CEO) a l'informe Q3 2018 · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/Q3%202018%20Financials/AT_Q3_2018.pdf · Wayback: https://web.archive.org/web/20250208224724/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/Q3%202018%20Financials/AT_Q3_2018.pdf (existent; cita no verificada a la captura) · id: `ND1-AT12`

13. [`ND1-AT13`] [V] «SENIOR AND KEY MANAGEMENT Name Position Mr. Shmuel Mayo CEO Mr. Andrew Wallis Deputy CEO»
   Nivell A · prova: CEO i Deputy CEO (no co-CEO) a l'informe Q3 2019 · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/Q3%202019%20Financials/AT_Q3_2019.pdf · Wayback: https://web.archive.org/web/20250208224209/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/Q3%202019%20Financials/AT_Q3_2019.pdf (existent; cita no verificada a la captura) · id: `ND1-AT13`

14. [`ND1-AT14`] [V] «Further, it is hereby announced that following the merger with TLG, the nomination of Mr. Barak Bar-Hen as Aroundtown's Co-CEO and COO and Mr. Klaus Krägel as CDO (Chief Development Officer) became effective.»
   Nivell A · prova: comunicat del 29/10/2020: el nomenament de Bar-Hen com a Co-CEO «became effective» · URL: https://www.aroundtown.de/newsDetail/104251 · Wayback: https://web.archive.org/web/20260415201502/https://www.aroundtown.de/newsDetail/104251 (existent; cita no verificada a la captura) · id: `ND1-AT14`

15. [`ND1-AT15`] [V] «Mr. Barak Bar-Hen began to serve as CO-CEO and COO on November 1, 2020.»
   Nivell A · prova: Bar-Hen comença com a Co-CEO l'1/11/2020 (informe de remuneracions 2020) · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/General%20Meetings/AGM%202021/2020_AT_Remuneration_Report.pdf · Wayback: https://web.archive.org/web/20251110192339/https://www.aroundtown.de/aroundtown.de/Data_Objects/General%20Meetings/AGM%202021/2020_AT_Remuneration_Report.pdf (existent; cita no verificada a la captura) · id: `ND1-AT15`

16. [`ND1-AT16`] [V] «Mr. Barak Bar-Hen began to serve as the Company’s Co-CEO and COO on November 1, 2020»
   Nivell A · prova: Bar-Hen comença com a Co-CEO l'1/11/2020 (informe anual 2020) · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/FY%202020%20Financials/AT_FY_2020.pdf · Wayback: https://web.archive.org/web/20251209043617/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/FY%202020%20Financials/AT_FY_2020.pdf (existent; cita no verificada a la captura) · id: `ND1-AT16`

17. [`ND1-AT17`] [V] «Mit Wirkung zum Ablauf des 31. Oktober 2020 hat Herr Bar-Hen sein Amt als Vorstand und als Vorstandsvorsitzender niedergelegt.»
   Nivell A · prova: Bar-Hen plega com a CEO de TLG al final del 31/10/2020 (informe del consell de supervisió de TLG) · URL: https://ir-api.eqs.com//media/document/0254c4ea-3952-4946-bdee-3e2eb12cb325/assets/TLG_Report_Supervisory_Board_de.pdf · Wayback: `pendent_verificacio_externa` · id: `ND1-AT17`

18. [`ND1-AT18`] [V] «BARAK BAR-HEN – CO-CEO & COO (CO-CHIEF EXECUTIVE OFFICER AND CHIEF OPERATING OFFICER) JOINED THE MANAGEMENT OF AROUNDTOWN AND ITS SUBSIDIARIES THIS QUARTER. PREVIOUSLY, HE WAS TLG’S CEO AND CHAIRMAN OF THE MANAGEMENT BOARD. HE HAS EXTENSIVE EXPERIENCE IN EUROPEAN REAL ESTATE AND SERVED AS A CEO OF ELAD EUROPE.»
   Nivell A · prova: Bar-Hen s'incorpora a la direcció d'Aroundtown «this quarter»; abans era CEO de TLG (cap cita l'anomena fundador) · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/Q3%202020%20Financials/AT_Q3_2020_financials_presentation.pdf · Wayback: https://web.archive.org/web/20250208232857/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Financial_Reports/Q3%202020%20Financials/AT_Q3_2020_financials_presentation.pdf (existent; cita no verificada a la captura) · id: `ND1-AT18`

19. [`ND1-AT19`] [V] «The current members of the advisory board are Mr. Yakir Gabay (Chairman), Mr. Dr. Axel Froese and Mr. Frank Roseen.»
   Nivell A · prova: Gabay presideix l'Advisory Board (2017): punt nou per a Doctorat (fundador president) · URL: https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Share/aroundtown_property_holdings_plc_prospectus.pdf · Wayback: https://web.archive.org/web/20260415191132/https://www.aroundtown.de/aroundtown.de/Data_Objects/Downloads/Share/aroundtown_property_holdings_plc_prospectus.pdf (existent; cita no verificada a la captura) · id: `ND1-AT19`

20. [`ND1-AT20`] [V] «Dr. Gerhard Cromme (Chairman), Mr. Yakir Gabay (Deputy Chairman) Mr. Claudio Jarczyk and Mr. David Maimon.»
   Nivell A · prova: Gabay vicepresident de l'Advisory Board (2019) · URL: https://www.aroundtown.de/aroundtown.de/Documents/Takeover%20Offer%20TLG%20IMMOBILIEN%20AG/Documents/Aroundtown_SA_-_Securities_Prospectus_20191217.pdf · Wayback: https://web.archive.org/web/20260614094036/https://www.aroundtown.de/aroundtown.de/Documents/Takeover%20Offer%20TLG%20IMMOBILIEN%20AG/Documents/Aroundtown_SA_-_Securities_Prospectus_20191217.pdf (existent; cita no verificada a la captura) · id: `ND1-AT20`

21. [`ND1-AT21`] [V] «The advisory board of the Company is not a statutory body under Luxembourg law and has no corporate authority.»
   Nivell A · prova: l'Advisory Board no és un òrgan estatutari ni té autoritat societària · URL: https://www.aroundtown.de/aroundtown.de/Documents/Takeover%20Offer%20TLG%20IMMOBILIEN%20AG/Documents/Aroundtown_SA_-_Securities_Prospectus_20191217.pdf · Wayback: https://web.archive.org/web/20260614094036/https://www.aroundtown.de/aroundtown.de/Documents/Takeover%20Offer%20TLG%20IMMOBILIEN%20AG/Documents/Aroundtown_SA_-_Securities_Prospectus_20191217.pdf (existent; cita no verificada a la captura) · id: `ND1-AT21`

---

# Lot 2 (proposta de Claude Code): cites del CEO a 31/10 per a les 108 files `ceo_pendent`

Data: 19/11/2026. Branca `cas/ceo-pendent-lot2`. **Proposta pendent del flux DF → Doctorat → Jordi; no s'autodeclara cap certificació.** Aquesta és la versió corregida segons la revisió de DF del 19/11/2026 (vegeu «Correccions de DF» més avall).

- Abast: les 108 files amb `sim_estat_certificacio=certificada_ceo_pendent` (28 ISIN).
- **Cap canvi a `dades/`**: el CEO de la base queda confirmat a les 108 files i l'etiqueta FounderCEO no es toca. No s'ha modificat cap columna de robustesa (`founderceo_rob_*`, `sim_*`), ni regles, ni `motiu_nd`, ni el `.xlsx`.
- Què s'afegeix: 324 cites literals de fonts A/B obertes a la URL original (files `tipus=evidencia_ceo`, id `L2|ISIN|cita` a `docs/REGISTRE_CANVIS.csv`), i les mateixes cites a cada fitxa. **Només 207 són cites del CEO** (`funcio_cita=ceo`: el fragment, per si sol, conté el nom de la persona i el càrrec de CEO o un equivalent legal). Les altres 117 no compten com a cita del CEO: 56 són de **datació** (només daten un document o un fet: dates, capçaleres, títols de taula) i 61 de **context** (registres que diuen «Director», dates sense el càrrec dins la cita, «has led», el càrrec sense la persona o el d'una altra persona). La primera versió del PR comptava 260 cites sense aquesta distinció; d'aquesta versió, 78 cites són noves o substitueixen cites anteriors.
- Totes les files tenen almenys una cita `ceo`. A 4 files les cites `ceo` són només de nivell B: Tesco PLC Registered Shares LS -,05 (`GB0008847096`) 2016, Tesco PLC Registered Shares LS -,05 (`GB0008847096`) 2017, Tesco PLC Registered Shares LS -,05 (`GB0008847096`) 2018, BBA Aviation PLC Registered Shares LS (`GB00B1FP8915`) 2017.
- Verificació: cada cita s'ha comprovat literalment per script al document baixat de la URL original (text de PDF o HTML; espais, lligadures i guionets tous normalitzats) i s'ha tornat a baixar i comprovar en una segona passada independent i adversarial. Cap còpia de tercers s'ha fet servir com a prova.
- Wayback: 218 de 324 cites tenen una captura existent segons l'API de disponibilitat d'archive.org; la resta queda `pendent_verificacio_externa`. `web.archive.org` no era accessible des de la sessió: cap cita s'ha pogut comprovar a la captura (`cita_verificada_a_captura=no`) ni s'ha pogut demanar cap captura nova.
- Regla del CEO: R1 (títol de CEO o equivalent legal) a totes les files, tret d'Ericsson 2016 i BBA Aviation 2017 (R2, CEO interí).

## Columnes noves de `docs/REGISTRE_CANVIS.csv`

S'hi afegeixen tres columnes al final. Són buides a les files anteriors al lot 2.

- `funcio_cita`: `ceo`, `datacio` o `context` (definicions a dalt). Només `ceo` compta com a cita del CEO. Les files de suport porten `decisio=lot2:suport_datacio_no_compta_com_cita_ceo` o `lot2:suport_context_no_compta_com_cita_ceo`.
- `allotjament`: on és el document obert. `emissor` = domini o subdomini propi de l'emissor; `grup` = web d'una altra societat del grup; `successor` = web de l'entitat successora o continuadora; `plataforma` = plataforma o CDN de tercers que allotja el document de l'emissor (EQS, imgix, Mynewsdesk, Cision...); `regulador` = regulador, registre oficial o borsa (CNMV, AMF/DILA, BALO, Companies House, SHAB, Nasdaq, FCA NSM, LSE); `mitja` = premsa al web del mitjà; `tercer` = document d'una altra entitat. Un document de l'emissor penjat fora del seu domini compta com a **A** si és de l'emissor i la cita és literal. Recompte: emissor 137, grup 60, regulador 52, mitja 31, plataforma 29, successor 10, tercer 5.
- `marca_prova`: per a cada any que sosté la cita, la marca de la fila (`any=marca`). `informe_exercici` = la fila té una cita `ceo` de l'informe anual (o document anual equivalent) de l'exercici que inclou el 31/10/t i l'informe no documenta cap canvi de CEO fins al tancament (aproximació de METODOLOGIA §1). `prova_interval` = sense aquesta cita, la fila es prova amb cites `ceo` de documents contemporanis (datats dins l'exercici o fins a 4 mesos després del tancament) que acoten la data, o amb dates d'inici i fi del mandat. `prova_interval_retrospectiva` (sempre amb `prova_interval`) = no hi ha cap cita `ceo` contemporània: la fila descansa en documents posteriors amb dates explícites d'inici o fi del mandat. `ceo_titol_amb_president_executiu` = el CEO de la fila té el títol de CEO (consejero delegado) però hi ha un president executiu (Bankia 2016).

Marques per fila (108 files): `informe_exercici` 62, `prova_interval` 37, `prova_interval+prova_interval_retrospectiva` 8, `informe_exercici+ceo_titol_amb_president_executiu` 1.

## Correccions de DF aplicades (19/11/2026)

- Cites de datació o context etiquetades com a tals i excloses del recompte de cites del CEO (columna `funcio_cita`).
- BBA Aviation 2017: les cites de Companies House C8-C10 se substitueixen per C8n-C10n, amb el nom de l'officer (Simon Pryce, Mark Johnstone, Wayne Edmunds), el rol i les dates; el registre diu «Director», no CEO, i són `context`.
- Tesco: c9 se substitueix per c9n (David John Lewis, «Director»; `context`). A la fila 2018 es treu l'article de la BBC del 7/10/2020 (c7) i la fila es prova amb RTÉ/Reuters del 3/10/2018 (c5) i la BBC del 10/4/2019 (c6).
- Victrex: C9 se substitueix per C9n (Jakob Oskar Sigurdsson, «Director»; `context`).
- Bankia 2016: es citen senceres i literalment les dues frases de l'IAGC 2016 dipositat a la CNMV (c7: Goirigolzarri, Presidente ejecutivo; c8: facultats delegades a Sevilla), totes dues `context`. Desapareix l'expressió «facultades limitadas», que no era una cita. El CEO continua sent José Sevilla Álvarez (Consejero Delegado: c2, c3) i la fila porta `ceo_titol_amb_president_executiu`.
- Sandoz 2023: s'hi afegeixen cites de documents posteriors a l'spin-off del 4/10/2023: el comunicat ad hoc del 24/10/2023 signat «Richard Saynor - CEO Sandoz» (SIX:SDZ, és a dir, Sandoz Group AG segons l'informe anual) i la taula de remuneració del Comitè Executiu de Sandoz Group AG del període del 4/10 al 31/12/2023 («Richard Saynor (CEO, highest paid)»). Cap fragment contigu no conté alhora «Sandoz Group AG», Saynor i el càrrec: el lligam és pel document; dubte per a Doctorat.
- Delivery Hero: C2025a es torna a extreure sencera (C2025a_s), i també C2019 i C2020 (C2019_s, C2020_s), sense talls de guionet.
- Dechra: C1 es torna a extreure sencera (C1_s).
- Marques `prova_interval` i `prova_interval_retrospectiva` aplicades fila a fila; columna `allotjament` afegida.
- A més, la verificació ha afegit cites `ceo` de documents de l'emissor o de reguladors que abans no s'havien pogut obrir o no s'havien buscat (p. ex. informes anuals d'OSRAM a EQS, l'informe anual 2016 i comunicats d'Ericsson a Cision, informes anuals de Chr. Hansen a Nasdaq Copenhagen, dipòsits AMF/BALO d'Alten, el Document de référence 2017 d'Essilor, l'informe anual 2016 d'Investec plc, l'AR 2023 de Deliveroo a l'FCA NSM). Totes surten a la taula de cada empresa.

## Resum per empresa

| ISIN | Empresa | Anys | CEO a 31/10 (sense canvi) | Cites (ceo / datació / context) | Nivells | Marques |
|---|---|---|---|---|---|---|
| `BE0974259880` | D'Ieteren Group S.A. Parts Sociales au Port. | 2022 | Francis Deprez | 5 (1 / 0 / 4) | A | `informe_exercici` 1 |
| `CH0008837566` | Allreal Holdings AG Namens-Aktien SF 1,00 | 2019-2022 | Roger Herzog | 10 (6 / 0 / 4) | A, B | `prova_interval` 4 |
| `CH1243598427` | Sandoz Group AG Namens-Aktien SF -,05 | 2023-2025 | Richard Saynor | 17 (6 / 3 / 8) | A | `informe_exercici` 3 |
| `DE0007100000` | Mercedes-Benz Group AG Namens-Aktien | 2019-2025 | Ola Källenius | 19 (16 / 2 / 1) | A | `prova_interval` 7 |
| `DE000A2E4K43` | Delivery Hero SE Namens-Aktien o.N. | 2018-2025 | Niklas Östberg | 14 (12 / 1 / 1) | A | `informe_exercici` 8 |
| `DE000LED4000` | OSRAM Licht AG Namens-Aktien o.N.2) | 2016-2019 | Olaf Berlien | 22 (11 / 10 / 1) | A | `informe_exercici` 3, `prova_interval` 1 |
| `DK0010181759` | Carlsberg AS Navne-Aktier B DK 20 | 2016-2022 | Cees ’t Hart | 15 (12 / 0 / 3) | A | `informe_exercici` 7 |
| `DK0060227585` | Christian Hansen Holding AS Navne-Aktier | 2016-2017 | Cees de Jong | 16 (7 / 7 / 2) | A | `informe_exercici` 1, `prova_interval` 1 |
| `ES0113307021` | BANKIA S.A. Acciones Nominativas EO 0,8 | 2016 | José Sevilla Álvarez | 8 (3 / 2 / 3) | A, B | `informe_exercici+ceo_titol_amb_president_executiu` 1 |
| `FR0000071946` | Alten S.A. Actions au Porteur EO 1,05 | 2018-2024 | Simon Azoulay | 22 (12 / 9 / 1) | A | `prova_interval` 2, `informe_exercici` 5 |
| `FR0000121667` | Essilor Intl -Cie Génle Opt.SA Actions Port. | 2016-2017 | Hubert Sagnières | 9 (9 / 0 / 0) | A | `prova_interval` 1, `informe_exercici` 1 |
| `GB0006731235` | Associated British Foods PLC Registered | 2016-2025 | George Weston | 23 (17 / 6 / 0) | A, B | `prova_interval` 9, `informe_exercici` 1 |
| `GB0008847096` | Tesco PLC Registered Shares LS -,05 | 2016-2018 | Dave Lewis | 8 (7 / 0 / 1) | A, B | `prova_interval` 3 |
| `GB0009292243` | Victrex PLC Registered Shares LS -,01 | 2018-2022 | Jakob Sigurdsson | 8 (3 / 2 / 3) | A | `prova_interval+prova_interval_retrospectiva` 5 |
| `GB0009633180` | Dechra Pharmaceuticals PLC Registered | 2018-2023 | Ian Page | 11 (8 / 0 / 3) | A, B | `prova_interval+prova_interval_retrospectiva` 2, `informe_exercici` 2, `prova_interval` 2 |
| `GB0034264548` | Paysafe Group PLC Registered Shares LS | 2016-2017 | Joel Leonoff | 10 (5 / 4 / 1) | A | `prova_interval` 2 |
| `GB00B17BBQ50` | Investec PLC Registered Shares LS -,00022) | 2016-2017 | Stephen Koseff | 6 (6 / 0 / 0) | A | `informe_exercici` 2 |
| `GB00B1FP8915` | BBA Aviation PLC Registered Shares LS | 2017 | Wayne Edmunds | 10 (4 / 0 / 6) | A, B | `prova_interval` 1 |
| `GB00B1KJJ408` | Whitbread PLC Reg. Shares LS -,76797385 | 2016-2020, 2022 | Alison Brittain | 21 (13 / 6 / 2) | A | `informe_exercici` 5, `prova_interval` 1 |
| `GB00B2B0DG97` | Relx PLC Registered Shares LS -,144397 | 2016-2025 | Erik Engstrom | 16 (10 / 0 / 6) | A | `informe_exercici` 10 |
| `GB00B71N6K86` | Evraz PLC Registered Shares DL 0,05 | 2018-2020 | Alexander Frolov | 8 (5 / 2 / 1) | A, B | `prova_interval` 2, `prova_interval+prova_interval_retrospectiva` 1 |
| `GB00B7T77214` | NatWest Group PLC Registered Shares LS 1 | 2020-2021 | Alison Rose | 6 (4 / 0 / 2) | A | `informe_exercici` 2 |
| `GB00BGXQNP29` | Phoenix Group Holdings PLC Registered | 2020-2025 | Andy Briggs | 8 (6 / 0 / 2) | A | `informe_exercici` 6 |
| `GB00BNC5T391` | Deliveroo PLC Registered Shares | 2021 | Will Shu | 7 (5 / 1 / 1) | A | `prova_interval` 1 |
| `JE00B8KF9B49` | WPP PLC Registered Shares LS -,10 | 2025 | Cindy Rose | 7 (4 / 0 / 3) | A | `informe_exercici` 1 |
| `NL0011821392` | Signify N.V. Registered Shares EO -,01 | 2022 | Eric Rondolat | 2 (2 / 0 / 0) | A | `informe_exercici` 1 |
| `SE0000108656` | Ericsson Namn-Aktier B (fria) o.N. | 2016 | Jan Frykhammar | 10 (8 / 1 / 1) | A, B | `informe_exercici` 1 |
| `SE0000869646` | Boliden AB Namn-Aktier SK 2 | 2016-2017 | Lennart Evrell | 6 (5 / 0 / 1) | A | `informe_exercici` 2 |

### L2.1 D'Ieteren Group S.A. Parts Sociales au Port. (`BE0974259880`)

- isin i anys: `BE0974259880`, 2022 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Francis Deprez → Francis Deprez (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2022: marca `informe_exercici`; cites del CEO `L2|BE0974259880|C3`; context `L2|BE0974259880|C1`, `L2|BE0974259880|C2`, `L2|BE0974259880|C4`, `L2|BE0974259880|C5`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/BE0974259880.md](../empreses/BE0974259880.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|BE0974259880|C1`] [V] «Composition of the Executive Committee on 31 December 2022 Francis Deprez (57) Arnaud Laviolette (61) Chairman of the Executive Committee and CEO»
   Anys: 2022 · funció: `context` · allotjament: `plataforma` · nivell A · prova: Francis Deprez era president del Comitè Executiu i CEO el 31/12/2022 · URL: https://dieterengroup.imgix.net/annual-reports/INTERACTIF-RAPPORT-FINANCIER-2022-ENG_2023-06-09-094530_rscg.pdf · Wayback: `pendent_verificacio_externa`

2. [`L2|BE0974259880|C2`] [V] «Start of mandate 2019 (as CEO)»
   Anys: 2022 · funció: `context` · allotjament: `plataforma` · nivell A · prova: A la taula del Comitè Executiu, l'inici de mandat de Francis Deprez com a CEO és 2019 (la columna correspon a la seva fila; el text extret és d'una taula) · URL: https://dieterengroup.imgix.net/annual-reports/INTERACTIF-RAPPORT-FINANCIER-2022-ENG_2023-06-09-094530_rscg.pdf · Wayback: `pendent_verificacio_externa`

3. [`L2|BE0974259880|C3`] [V] «Two members Francis Deprez: CEO Arnaud Laviolette: CFO»
   Anys: 2022 · funció: `ceo` · allotjament: `plataforma` · nivell A · prova: Francis Deprez figura com a CEO del grup a l'informe integrat de l'exercici 2022 · URL: https://dieterengroup.imgix.net/annual-reports/INTEGRATED-REPORT-2022-ENG-VFF.pdf · Wayback: https://web.archive.org/web/20230628173924/https://dieterengroup.imgix.net/annual-reports/INTEGRATED-REPORT-2022-ENG-VFF.pdf (existent; cita no verificada a la captura)

4. [`L2|BE0974259880|C4`] [V] «Composition of the Executive Committee on 31 December 2021 Francis Deprez (56)»
   Anys: 2022 · funció: `context` · allotjament: `plataforma` · nivell A · prova: Francis Deprez ja era membre del Comitè Executiu el 31/12/2021 (límit inferior de l'interval) · URL: https://dieterengroup.imgix.net/annual-reports/RAPPORT-FINANCIER-2021-ENG-INTERACTIF-21-6-22.pdf · Wayback: `pendent_verificacio_externa`

5. [`L2|BE0974259880|C5`] [V] «Start of mandate Chairman of the Executive Committee and CEO»
   Anys: 2022 · funció: `context` · allotjament: `plataforma` · nivell A · prova: A la mateixa taula del 31/12/2021 (C4), el càrrec de Francis Deprez és Chairman of the Executive Committee and CEO (text extret de taula: 'Start of mandate' és una capçalera de columna adjacent) · URL: https://dieterengroup.imgix.net/annual-reports/RAPPORT-FINANCIER-2021-ENG-INTERACTIF-21-6-22.pdf · Wayback: `pendent_verificacio_externa`

### L2.2 Allreal Holdings AG Namens-Aktien SF 1,00 (`CH0008837566`)

- isin i anys: `CH0008837566`, 2019-2022 (n=4). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Roger Herzog → Roger Herzog (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A, B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2019: marca `prova_interval`; cites del CEO `L2|CH0008837566|c7`, `L2|CH0008837566|c11`, `L2|CH0008837566|c1`; context `L2|CH0008837566|c8`, `L2|CH0008837566|c9`.
- 2020: marca `prova_interval`; cites del CEO `L2|CH0008837566|c7`, `L2|CH0008837566|c11`, `L2|CH0008837566|c1`; context `L2|CH0008837566|c8`, `L2|CH0008837566|c9`.
- 2021: marca `prova_interval`; cites del CEO `L2|CH0008837566|c10`, `L2|CH0008837566|c11`, `L2|CH0008837566|c3`, `L2|CH0008837566|c1`; context `L2|CH0008837566|c8`, `L2|CH0008837566|c9`.
- 2022: marca `prova_interval`; cites del CEO `L2|CH0008837566|c3`, `L2|CH0008837566|c4`, `L2|CH0008837566|c1`; context `L2|CH0008837566|c5`, `L2|CH0008837566|c6`.
- Correccions de DF: `L2|CH0008837566|c11` substitueix `L2|CH0008837566|c2`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/CH0008837566.md](../empreses/CH0008837566.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|CH0008837566|c1`] [V] «Ausgeschiedene Personen und erloschene Unterschriften: Herzog, Roger, von Zürich, in Zürich, Vorsitzender der Geschäftsleitung, mit Kollektivunterschrift zu zweien. Eingetragene Personen neu oder mutierend: Widrig, Stephan, von Bad Ragaz, in Wallisellen, Vorsitzender der Geschäftsleitung, mit Kollektivunterschrift zu zweien.»
   Anys: 2019-2022 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Fi del mandat: Roger Herzog consta inscrit com a Vorsitzender der Geschäftsleitung (CEO) d'Allreal Holding AG fins a la mutació publicada l'01.06.2023, en què el substitueix Stephan Widrig. Per tant no va ser substituït abans de 2023. · URL: https://www.zefix.ch/ZefixREST/api/v1/firm/462500.json · Wayback: `pendent_verificacio_externa`

2. [`L2|CH0008837566|c3`] [V] «Konzernchef Roger Herzog gibt seine Funktion als CEO im Frühjahr 2023 ab.»
   Anys: 2021-2022 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: El 14.07.2022 Herzog és el CEO en exercici i la sortida s'anuncia per a la primavera de 2023 (posterior al 31/10/2022). · URL: https://www.moneycab.com/schweiz/allreal-ceo-roger-herzog-tritt-im-fruehjahr-2023-zurueck/ · Wayback: https://web.archive.org/web/20250807071308/https://www.moneycab.com/schweiz/allreal-ceo-roger-herzog-tritt-im-fruehjahr-2023-zurueck/ (existent; cita no verificada a la captura)

3. [`L2|CH0008837566|c4`] [V] «Bis zu seinem Austritt im Frühjahr 2023 werde Herzog seine Aufgaben als CEO unverändert wahrnehmen»
   Anys: 2022 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Continuïtat anunciada com a CEO fins a la primavera de 2023. · URL: https://www.moneycab.com/schweiz/allreal-ceo-roger-herzog-tritt-im-fruehjahr-2023-zurueck/ · Wayback: https://web.archive.org/web/20250807071308/https://www.moneycab.com/schweiz/allreal-ceo-roger-herzog-tritt-im-fruehjahr-2023-zurueck/ (existent; cita no verificada a la captura)

4. [`L2|CH0008837566|c5`] [V] «Ab Mai 2023 wird Widrig bei Allreal das Zepter führen. Er löst dort Roger Herzog ab, wie Allreal in einer eigenen Mitteilung schreibt. Der Rücktritt von Herzog per Ende März 2023 wurde allerdings bereits im Juli kommuniziert.»
   Anys: 2022 · funció: `context` · allotjament: `mitja` · nivell B · prova: El 27.10.2022 (4 dies abans del 31/10/2022) el successor encara no ha entrat: Widrig comença el maig de 2023 i Herzog plega a final de març de 2023. · URL: https://www.moneycab.com/schweiz/flughafenzuerich-verliert-ceo-stephan-widrig-an-allreal/ · Wayback: https://web.archive.org/web/20260213172944/https://www.moneycab.com/schweiz/flughafenzuerich-verliert-ceo-stephan-widrig-an-allreal/ (existent; cita no verificada a la captura)

5. [`L2|CH0008837566|c6`] [V] «From May 2023, Stephan Widrig will be CEO of Allreal Holding AG, one of the largest listed real estate companies in Switzerland. He will therefore be leaving Flughafen Zürich AG at the end of April 2023.»
   Anys: 2022 · funció: `context` · allotjament: `tercer` · nivell B · prova: Widrig no és CEO d'Allreal fins al maig de 2023; el 31/10/2022 encara és CEO de Flughafen Zürich. · URL: https://www.flughafen-zuerich.ch/newsroom/en/change-in-the-management-board-of-flughafen-zuerich-ag/ · Wayback: https://web.archive.org/web/20231207112746/https://www.flughafen-zuerich.ch/newsroom/en/change-in-the-management-board-of-flughafen-zuerich-ag/ (existent; cita no verificada a la captura)

6. [`L2|CH0008837566|c7`] [V] «Er übernimmt diese Aufgabe von CEO Roger Herzog, welcher die Sparte bisher direkt geleitet hat.»
   Anys: 2019-2020 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Document contemporani: el 12.02.2020 Roger Herzog és el CEO d'Allreal. · URL: https://www.moneycab.com/schweiz/allreal-simon-raebsamen-wird-neuer-leiter-realisation/ · Wayback: https://web.archive.org/web/20250807164849/https://www.moneycab.com/schweiz/allreal-simon-raebsamen-wird-neuer-leiter-realisation/ (existent; cita no verificada a la captura)

7. [`L2|CH0008837566|c8`] [V] «Bettoni leitet das Unternehmen seit der Gründung im Jahr 1999 und wird dies noch bis Anfang Mai tun, wie Allreal am Donnerstag mitteilt. Dann übernimmt Herzog.»
   Anys: 2019-2021 · funció: `context` · allotjament: `mitja` · nivell B · prova: Inici del mandat: Herzog assumeix la direcció a principis de maig de 2015. · URL: https://www.moneycab.com/?p=1064109 · Wayback: `pendent_verificacio_externa`

8. [`L2|CH0008837566|c9`] [V] «Herr Herzog, nach zehn Jahren als Finanzchef von Allreal haben Sie Anfang Mai die Führung des Unternehmens übernommen.»
   Anys: 2019-2021 · funció: `context` · allotjament: `mitja` · nivell B · prova: Inici efectiu del mandat: principis de maig de 2015. · URL: https://www.moneycab.com/?p=1054743 · Wayback: `pendent_verificacio_externa`

9. [`L2|CH0008837566|c10`] [V] ««A l’avenir, cela aura un effet positif sur le dividende», a indiqué dans une téléconférence Roger Herzog, directeur général (CEO) d’Allreal.»
   Anys: 2021 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Document contemporani de l'exercici 2021 (exercici natural): el 16.09.2021 Roger Herzog és el «directeur général (CEO)» d'Allreal. · URL: https://allnews.ch/content/immobilier/allreal-d%C3%A9bourse-plusieurs-centaines-de-millions-pour-se-renforcer-en-romandie · Wayback: https://web.archive.org/web/20211018173455/https://allnews.ch/content/immobilier/allreal-d%C3%A9bourse-plusieurs-centaines-de-millions-pour-se-renforcer-en-romandie (existent; cita no verificada a la captura)

10. [`L2|CH0008837566|c11`] [V] «Herzog mit Jahrgang 1972 war fast 20 Jahre für den Immobilienkonzern tätig. Zunächst war er Finanzchef und ab 2015 Konzernchef.»
   Anys: 2019-2021 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Inici del mandat amb el càrrec: Herzog és Konzernchef (CEO) des de 2015. És el passatge contigu de c2 ampliat amb la frase anterior perquè el nom i el càrrec quedin dins el fragment. · URL: https://www.moneycab.com/schweiz/allreal-ceo-roger-herzog-tritt-im-fruehjahr-2023-zurueck/ · Wayback: https://web.archive.org/web/20250807071308/https://www.moneycab.com/schweiz/allreal-ceo-roger-herzog-tritt-im-fruehjahr-2023-zurueck/ (existent; cita no verificada a la captura) · substitueix `L2|CH0008837566|c2`

### L2.3 Sandoz Group AG Namens-Aktien SF -,05 (`CH1243598427`)

- isin i anys: `CH1243598427`, 2023-2025 (n=3). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Richard Saynor → Richard Saynor (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2023: marca `informe_exercici`; cites del CEO `L2|CH1243598427|C2023a`, `L2|CH1243598427|C2023c`, `L2|CH1243598427|C2023g`; datació `L2|CH1243598427|C2023d`, `L2|CH1243598427|C2023h`, `L2|CH1243598427|C2023i`; context `L2|CH1243598427|C2023b`, `L2|CH1243598427|C2023e`, `L2|CH1243598427|C2023f`.
- 2024: marca `informe_exercici`; cites del CEO `L2|CH1243598427|C2024a`, `L2|CH1243598427|C2024c`; context `L2|CH1243598427|C2024b`, `L2|CH1243598427|C2024d`.
- 2025: marca `informe_exercici`; cites del CEO `L2|CH1243598427|C2025a`; context `L2|CH1243598427|C2025b`, `L2|CH1243598427|C2025c`, `L2|CH1243598427|C2025d`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/CH1243598427.md](../empreses/CH1243598427.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|CH1243598427|C2023a`] [V] «As of December 31, 2023, the Sandoz Executive Committee was composed of the following individuals: Executive Committee Richard Saynor Chief Executive Officer»
   Anys: 2023 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Richard Saynor era Chief Executive Officer de Sandoz el 31/12/2023 · URL: https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf · Wayback: https://web.archive.org/web/20240829080930/https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf (existent; cita no verificada a la captura)

2. [`L2|CH1243598427|C2023b`] [V] «Richard Saynor has led Sandoz since 2019, offering a proven track record as a senior leader»
   Anys: 2023 · funció: `context` · allotjament: `emissor` · nivell A · prova: Saynor dirigeix Sandoz de manera continuada des del 2019 (inici de l'interval) · URL: https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf · Wayback: https://web.archive.org/web/20240829080930/https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf (existent; cita no verificada a la captura)

3. [`L2|CH1243598427|C2024a`] [V] «As of December 31, 2024, the Sandoz Executive Committee was composed of the following individuals: Richard Saynor Chief Executive Officer»
   Anys: 2024 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Richard Saynor era Chief Executive Officer de Sandoz el 31/12/2024 · URL: https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz_2024_annual_report.pdf · Wayback: https://web.archive.org/web/20260624233323/https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz_2024_annual_report.pdf (existent; cita no verificada a la captura)

4. [`L2|CH1243598427|C2024b`] [V] «Richard Saynor has led Sandoz since 2019, offering a proven track record as a senior leader»
   Anys: 2024 · funció: `context` · allotjament: `emissor` · nivell A · prova: Saynor dirigeix Sandoz de manera continuada des del 2019 (inici de l'interval) · URL: https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz_2024_annual_report.pdf · Wayback: https://web.archive.org/web/20260624233323/https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz_2024_annual_report.pdf (existent; cita no verificada a la captura)

5. [`L2|CH1243598427|C2024c`] [V] «Richard Saynor, Chief Executive Officer of Sandoz, said:»
   Anys: 2024 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Saynor signava com a CEO en el comunicat del 30/10/2024, la vigília de la data de referència · URL: https://www.sandoz.com/sandoz-reports-third-quarter-and-nine-month-2024-sales/ · Wayback: https://web.archive.org/web/20260424070914/https://www.sandoz.com/sandoz-reports-third-quarter-and-nine-month-2024-sales/ (existent; cita no verificada a la captura)

6. [`L2|CH1243598427|C2025a`] [V] «As of December 31, 2025, the Sandoz Executive Committee was composed of the following individuals: Richard Saynor Chief Executive Officer»
   Anys: 2025 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Richard Saynor era Chief Executive Officer de Sandoz el 31/12/2025 · URL: https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf · Wayback: https://web.archive.org/web/20261107224146/https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf (existent; cita no verificada a la captura)

7. [`L2|CH1243598427|C2025b`] [V] «Richard Saynor has led Sandoz since 2019, offering a proven track record as a senior leader»
   Anys: 2025 · funció: `context` · allotjament: `emissor` · nivell A · prova: Saynor dirigeix Sandoz de manera continuada des del 2019 (inici de l'interval) · URL: https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf · Wayback: https://web.archive.org/web/20261107224146/https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf (existent; cita no verificada a la captura)

8. [`L2|CH1243598427|C2025c`] [V] «Changes to the Executive Committee in 2025 Peter Stenico, former Global Platform Head Biosimilars and Country President Austria, was appointed President Region International effective March 1, 2025, succeeding Francisco Ballester who retired from his position as of February 28, 2025.»
   Anys: 2025 · funció: `context` · allotjament: `emissor` · nivell A · prova: L'únic canvi al Comitè Executiu el 2025 que informa l'apartat no afecta el CEO · URL: https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf · Wayback: https://web.archive.org/web/20261107224146/https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf (existent; cita no verificada a la captura)

9. [`L2|CH1243598427|C2023c`] [V] «Richard Saynor (CEO, highest paid)»
   Anys: 2023 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: El Remuneration Report de Sandoz Group AG de l'exercici 2023 (C2023e) retribueix el Comitè Executiu només pel període posterior a l'spin-off, del 4/10/2023 al 31/12/2023 (C2023d per a l'Exhibit 1.2; C2023i per a l'Exhibit 2.4.1, auditat). Hi posa Richard Saynor com a «CEO, highest paid». Per tant, Saynor era el CEO de Sandoz Group AG durant tot aquest període, que inclou el 31/10/2023. És un document posterior al 4/10/2023, tal com demana la correcció. · URL: https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf · Wayback: https://web.archive.org/web/20240829080930/https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf (existent; cita no verificada a la captura)

10. [`L2|CH1243598427|C2023d`] [V] «Exhibit 1.2: Executive Committee compensation October 4, 2023 – December 31, 2023»
   Anys: 2023 · funció: `datacio` · allotjament: `emissor` · nivell A · prova: Data el període de la taula on surt C2023c: del 4/10/2023 (spin-off) al 31/12/2023, un interval que inclou el 31/10/2023. · URL: https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf · Wayback: https://web.archive.org/web/20240829080930/https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf (existent; cita no verificada a la captura)

11. [`L2|CH1243598427|C2023e`] [V] «We have audited the Remuneration Report of Sandoz Group AG (the Company) for the year ended 31 December 2023»
   Anys: 2023 · funció: `context` · allotjament: `emissor` · nivell A · prova: Lliga a Sandoz Group AG l'informe de remuneracions d'on surt C2023c: és el Remuneration Report de Sandoz Group AG de l'exercici 2023. L'auditoria només cobreix les pàgines impreses 100, 102, 106, 107, 109 i 110; l'Exhibit 2.4.1 (pàg. 100) hi és inclòs i l'Exhibit 1.2 (pàg. 93) no. · URL: https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf · Wayback: https://web.archive.org/web/20240829080930/https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf (existent; cita no verificada a la captura)

12. [`L2|CH1243598427|C2023f`] [V] «On December 31, 2023, the share capital of Sandoz Group AG was composed of 431,000,000 registered shares, fully paid in, each with a nominal value of CHF 0.05. Shares are listed on the SIX Swiss Exchange (ISIN: CH1243598427, symbol: SDZ).»
   Anys: 2023 · funció: `context` · allotjament: `emissor` · nivell A · prova: Lliga el símbol SIX «SDZ» i l'ISIN CH1243598427 a les accions de Sandoz Group AG. Per tant, el comunicat ad hoc de «Sandoz (SIX:SDZ/OTCQX:SDZNY)» del 24/10/2023 (C2023g, C2023h) és de la societat cotitzada Sandoz Group AG. · URL: https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf · Wayback: https://web.archive.org/web/20240829080930/https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf (existent; cita no verificada a la captura)

13. [`L2|CH1243598427|C2023g`] [V] «Richard Saynor - CEO Sandoz»
   Anys: 2023 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Document contemporani: és posterior a l'spin-off del 4/10/2023 i anterior en 7 dies al 31/10/2023. El comunicat ad hoc és de «Sandoz (SIX:SDZ/OTCQX:SDZNY)» (C2023h), és a dir, de l'emissor cotitzat Sandoz Group AG segons C2023f. «Richard Saynor - CEO Sandoz» signa la declaració que diu «With the spin-off successfully completed on October 4, 2023». · URL: https://www.sandoz.com/sandoz_reports_year-to-date_sales_for_the_first_nine_months_of_2023/ · Wayback: https://web.archive.org/web/20260424065651/https://www.sandoz.com/sandoz_reports_year-to-date_sales_for_the_first_nine_months_of_2023/ (existent; cita no verificada a la captura)

14. [`L2|CH1243598427|C2023h`] [V] «Basel, October 24, 2023 – Sandoz (SIX:SDZ/OTCQX:SDZNY), the global leader in generic and biosimilar medicines»
   Anys: 2023 · funció: `datacio` · allotjament: `emissor` · nivell A · prova: Data el comunicat de C2023g el 24/10/2023 i n'identifica l'emissor pel símbol SIX:SDZ. · URL: https://www.sandoz.com/sandoz_reports_year-to-date_sales_for_the_first_nine_months_of_2023/ · Wayback: https://web.archive.org/web/20260424065651/https://www.sandoz.com/sandoz_reports_year-to-date_sales_for_the_first_nine_months_of_2023/ (existent; cita no verificada a la captura)

15. [`L2|CH1243598427|C2023i`] [V] «All numbers disclosed in exhibit 2.4.1 represent payments or benefits for the period from October 4 to December 31, 2023, i.e., 89 days.»
   Anys: 2023 · funció: `datacio` · allotjament: `emissor` · nivell A · prova: Data el període de l'Exhibit 2.4.1, la taula auditada on també surt «Richard Saynor (CEO, highest paid)» (C2023c): del 4/10/2023 al 31/12/2023, un interval que inclou el 31/10/2023. L'he afegida a la verificació, perquè C2023d data l'Exhibit 1.2, que no és a les pàgines auditades. · URL: https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf · Wayback: https://web.archive.org/web/20240829080930/https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf (existent; cita no verificada a la captura)

16. [`L2|CH1243598427|C2024d`] [V] «We have audited the Remuneration Report of Sandoz Group AG (the Company) for the year ended 31 December 2024»
   Anys: 2024 · funció: `context` · allotjament: `emissor` · nivell A · prova: Mostra que l'Integrated Annual Report 2024, d'on surt C2024a, és un document de Sandoz Group AG posterior a l'spin-off, que conté el Remuneration Report de Sandoz Group AG de l'exercici 2024. · URL: https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz_2024_annual_report.pdf · Wayback: https://web.archive.org/web/20260624233323/https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz_2024_annual_report.pdf (existent; cita no verificada a la captura)

17. [`L2|CH1243598427|C2025d`] [V] «We have audited the Remuneration Report of Sandoz Group AG (the Company) for the year ended 31 December 2025»
   Anys: 2025 · funció: `context` · allotjament: `emissor` · nivell A · prova: Mostra que l'Integrated Annual Report 2025, d'on surt C2025a, és un document de Sandoz Group AG, que conté el Remuneration Report de Sandoz Group AG de l'exercici 2025. · URL: https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf · Wayback: https://web.archive.org/web/20261107224146/https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf (existent; cita no verificada a la captura)

### L2.4 Mercedes-Benz Group AG Namens-Aktien (`DE0007100000`)

- isin i anys: `DE0007100000`, 2019-2025 (n=7). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Ola Källenius → Ola Källenius (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2019: marca `prova_interval`; cites del CEO `L2|DE0007100000|c02`, `L2|DE0007100000|c04`, `L2|DE0007100000|c01`; datació `L2|DE0007100000|c03`.
- 2020: marca `prova_interval`; cites del CEO `L2|DE0007100000|c05`, `L2|DE0007100000|c17`, `L2|DE0007100000|c06`, `L2|DE0007100000|c01`.
- 2021: marca `prova_interval`; cites del CEO `L2|DE0007100000|c07`, `L2|DE0007100000|c08`, `L2|DE0007100000|c01`.
- 2022: marca `prova_interval`; cites del CEO `L2|DE0007100000|c09`, `L2|DE0007100000|c10`; context `L2|DE0007100000|c12`.
- 2023: marca `prova_interval`; cites del CEO `L2|DE0007100000|c11`, `L2|DE0007100000|c13`; context `L2|DE0007100000|c12`.
- 2024: marca `prova_interval`; cites del CEO `L2|DE0007100000|c13`, `L2|DE0007100000|c14`, `L2|DE0007100000|c11`.
- 2025: marca `prova_interval`; cites del CEO `L2|DE0007100000|c15`, `L2|DE0007100000|c16`, `L2|DE0007100000|c18`, `L2|DE0007100000|c11`; datació `L2|DE0007100000|c19`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/DE0007100000.md](../empreses/DE0007100000.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|DE0007100000|c01`] [V] «the Supervisory Board of Daimler AG therefore decided to appoint Ola Källenius for a new term of five years as Chairman of the Board of Management of Daimler AG, effective in direct connection»
   Anys: 2019-2021 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat del 26/09/2018: nomenament de Källenius com a Vorstandsvorsitzender per cinc anys, amb efecte tot seguit de la sortida de Zetsche al final de la junta general de 2019. · URL: https://media.mercedes-benz.it/daimler-sets-its-course-for-the-future-dieter-zetsche-to-succeed-manfred-bischoff-in-the-supervisory-board--ola-kallenius-to-become-chairman-of-the-board-of-management-of-daimler-ag-in-2019/ · Wayback: https://web.archive.org/web/20210116235438/https://media.mercedes-benz.it/daimler-sets-its-course-for-the-future-dieter-zetsche-to-succeed-manfred-bischoff-in-the-supervisory-board--ola-kallenius-to-become-chairman-of-the-board-of-management-of-daimler-ag-in-2019/ (existent; cita no verificada a la captura)

2. [`L2|DE0007100000|c02`] [V] «Ola Källenius took over from Zetsche at the end of the Annual Shareholders’ Meeting as Chairman of the Board of Management of Daimler AG and Head of Mercedes-Benz Cars.»
   Anys: 2019 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat datat el 23/05/2019 sobre la junta general: Källenius assumeix la presidència del Vorstand al final de la junta (inici efectiu del mandat, maig de 2019). · URL: https://media.mercedes-benz.it/large-majority-of-daimler-shareholders-approve-new-group-structure-with-daimler-ag-as-parent-company/ · Wayback: https://web.archive.org/web/20240227172537/https://media.mercedes-benz.it/large-majority-of-daimler-shareholders-approve-new-group-structure-with-daimler-ag-as-parent-company/ (existent; cita no verificada a la captura)

3. [`L2|DE0007100000|c03`] [V] «Annual General Meeting of Daimler AG on May 22, 2019 in Berlin.»
   Anys: 2019 · funció: `datacio` · allotjament: `grup` · nivell A · prova: Peu de foto del comunicat datat el 23/05/2019: la junta general de 2019 es va fer el 22/05/2019 (data efectiva del relleu Zetsche -> Källenius, segons c02). · URL: https://media.mercedes-benz.it/large-majority-of-daimler-shareholders-approve-new-group-structure-with-daimler-ag-as-parent-company/ · Wayback: https://web.archive.org/web/20240227172537/https://media.mercedes-benz.it/large-majority-of-daimler-shareholders-approve-new-group-structure-with-daimler-ag-as-parent-company/ (existent; cita no verificada a la captura)

4. [`L2|DE0007100000|c04`] [V] «said Ola Källenius, Chairman of the Board of Management of Daimler AG and Mercedes-Benz AG.»
   Anys: 2019 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat datat el 14/11/2019 (Capital Market Day): Källenius és Chairman of the Board of Management de Daimler AG; continuïtat després del 31/10/2019. · URL: https://media.mercedes-benz.it/daimler-cuts-costs-and-sets-course-for-the-future/ · Wayback: https://web.archive.org/web/20240301211357/https://media.mercedes-benz.it/daimler-cuts-costs-and-sets-course-for-the-future/ (existent; cita no verificada a la captura)

5. [`L2|DE0007100000|c05`] [V] «Ola Källenius, Chairman of the Board of Management of Daimler AG and Mercedes-Benz AG: “Due to the unprecedented COVID-19 pandemic, we had to endure a challenging quarter.»
   Anys: 2020 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat datat el 23/07/2020 (resultats T2 2020): Källenius és Chairman of the Board of Management de Daimler AG abans del 31/10/2020. · URL: https://media.mercedes-benz.it/daimler-reports-second-quarter-2020-results/ · Wayback: https://web.archive.org/web/20240301212603/https://media.mercedes-benz.it/daimler-reports-second-quarter-2020-results/ (existent; cita no verificada a la captura)

6. [`L2|DE0007100000|c06`] [V] «stated Ola Källenius, Chairman of the Board of Management of Daimler AG and Mercedes-Benz AG.»
   Anys: 2020 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat datat el 29/01/2021 (resultats preliminars 2020): continua com a Chairman of the Board of Management de Daimler AG després del 31/10/2020. · URL: https://media.mercedes-benz.it/preliminary-results-for-the-financial-year-2020-significantly-above-guidance-and-market-expectations/ · Wayback: https://web.archive.org/web/20240424231852/https://media.mercedes-benz.it/preliminary-results-for-the-financial-year-2020-significantly-above-guidance-and-market-expectations/ (existent; cita no verificada a la captura)

7. [`L2|DE0007100000|c07`] [V] «Ola Källenius, Chairman of the Board of Management of Daimler AG and Mercedes-Benz AG : “Daimler’s realignment makes one success story into two.»
   Anys: 2021 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat datat el 30/07/2021: Källenius és Chairman of the Board of Management de Daimler AG abans del 31/10/2021. · URL: https://media.mercedes-benz.it/go-ahead-for-mercedes-benz-cars-and-daimler-truck-as-independent-companies-by-board-of-management-and-supervisory-board/ · Wayback: https://web.archive.org/web/20240229194524/https://media.mercedes-benz.it/go-ahead-for-mercedes-benz-cars-and-daimler-truck-as-independent-companies-by-board-of-management-and-supervisory-board/ (existent; cita no verificada a la captura)

8. [`L2|DE0007100000|c08`] [V] «Ola Källenius, Chief Executive Officer of Daimler AG and Mercedes-Benz AG : “Our goal is technological leadership in the automotive luxury segment»
   Anys: 2021 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat datat el 03/12/2021: Källenius és Chief Executive Officer de Daimler AG després del 31/10/2021. · URL: https://media.mercedes-benz.it/supervisory-board-confirms-business-plan---mercedes-benz-to-invest-60-billion-euros-into-the-future/ · Wayback: https://web.archive.org/web/20240424221123/https://media.mercedes-benz.it/supervisory-board-confirms-business-plan---mercedes-benz-to-invest-60-billion-euros-into-the-future/ (existent; cita no verificada a la captura)

9. [`L2|DE0007100000|c09`] [V] «said Ola Källenius, Chairman of the Board of Management of Mercedes-Benz Group AG .»
   Anys: 2022 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat datat el 29/04/2022 (junta general 2022): Källenius és Chairman of the Board of Management de Mercedes-Benz Group AG abans del 31/10/2022. · URL: https://media.mercedes-benz.it/annual-meeting-mercedes-benz-continues-its-successful-transformation/ · Wayback: https://web.archive.org/web/20240422182920/https://media.mercedes-benz.it/annual-meeting-mercedes-benz-continues-its-successful-transformation/ (existent; cita no verificada a la captura)

10. [`L2|DE0007100000|c10`] [V] «said Ola Kaellenius, Chief Executive Officer of Mercedes-Benz Group AG.»
   Anys: 2022 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat datat el 17/02/2023 (resultats 2022): continua com a CEO de Mercedes-Benz Group AG després del 31/10/2022. · URL: https://media.mercedes-benz.it/mercedes-benz-delivers-strong-full-year-results-in-2022/ · Wayback: https://web.archive.org/web/20240415060830/https://media.mercedes-benz.it/mercedes-benz-delivers-strong-full-year-results-in-2022/ (existent; cita no verificada a la captura)

11. [`L2|DE0007100000|c11`] [V] «The Supervisory Board reappointed Ola Källenius (54) as Chairman of the Board of Management of Mercedes-Benz Group AG until May 21, 2029, at its meeting today.»
   Anys: 2023-2025 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat del 27/07/2023: renovació de Källenius com a Chairman of the Board of Management fins al 21/05/2029 (cita d interval; en funcions abans del 31/10/2023). · URL: https://media.mercedes-benz.it/download/52b30d94-8c94-4537-83fc-47cba9af5822/20230727-pi-mercedes-benz-entscheidungenar-en-final.pdf · Wayback: https://web.archive.org/web/20240716160203/https://media.mercedes-benz.it/download/52b30d94-8c94-4537-83fc-47cba9af5822/20230727-pi-mercedes-benz-entscheidungenar-en-final.pdf (existent; cita no verificada a la captura)

12. [`L2|DE0007100000|c12`] [V] «contracts of Ola Källenius and Markus Schäfer are due to expire in May 2024.»
   Anys: 2022-2023 · funció: `context` · allotjament: `grup` · nivell A · prova: El mandat vigent al juliol de 2023 (el de cinc anys iniciat a la junta de 2019) vencia el maig de 2024. · URL: https://media.mercedes-benz.it/download/52b30d94-8c94-4537-83fc-47cba9af5822/20230727-pi-mercedes-benz-entscheidungenar-en-final.pdf · Wayback: https://web.archive.org/web/20240716160203/https://media.mercedes-benz.it/download/52b30d94-8c94-4537-83fc-47cba9af5822/20230727-pi-mercedes-benz-entscheidungenar-en-final.pdf (existent; cita no verificada a la captura)

13. [`L2|DE0007100000|c13`] [V] «Ola Kaellenius, Chief Executive Officer of Mercedes-Benz Group AG.»
   Anys: 2023-2024 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat datat el 22/02/2024 (resultats 2023): continua com a CEO després del 31/10/2023 i abans del 31/10/2024. · URL: https://media.mercedes-benz.it/mercedes-benz-group-2023-results-cash-generation-at-work/ · Wayback: https://web.archive.org/web/20240424215755/https://media.mercedes-benz.it/mercedes-benz-group-2023-results-cash-generation-at-work/ (existent; cita no verificada a la captura)

14. [`L2|DE0007100000|c14`] [V] «has elected Ola Källenius, Chairman of the Board of Management of Mercedes-Benz Group AG, as the new ACEA President for 2025.»
   Anys: 2024 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat datat l 11/12/2024: Källenius és Chairman of the Board of Management de Mercedes-Benz Group AG després del 31/10/2024. · URL: https://media.mercedes-benz.it/acea-ola-kallenius/ · Wayback: `pendent_verificacio_externa`

15. [`L2|DE0007100000|c15`] [V] «Ola Kaellenius, Chief Executive Officer of Mercedes-Benz Group AG»
   Anys: 2025 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat de resultats del T3 datat el 29/10/2025: Källenius és CEO de Mercedes-Benz Group AG dos dies abans del 31/10/2025. · URL: https://media.mercedes-benz.it/download/9f8e075d-8822-437b-9ca4-46fe7aa7ecd2/20251029_mbgroupag_pressinformation_resultsq3_media.pdf · Wayback: `pendent_verificacio_externa`

16. [`L2|DE0007100000|c16`] [V] «Board of Management: Ola Källenius, Chairman; Jörg Burzer, Renata Jungo Brüngger»
   Anys: 2025 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Peu legal del comunicat del 29/10/2025: Källenius, Chairman del Board of Management. · URL: https://media.mercedes-benz.it/download/9f8e075d-8822-437b-9ca4-46fe7aa7ecd2/20251029_mbgroupag_pressinformation_resultsq3_media.pdf · Wayback: `pendent_verificacio_externa`

17. [`L2|DE0007100000|c17`] [V] «said Ola Källenius, Chairman of the Board of Management of Daimler AG and Mercedes-Benz AG»
   Anys: 2020 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Comunicat datat el 06/10/2020 (Strategy Update): Källenius és Chairman of the Board of Management de Daimler AG tres setmanes abans del 31/10/2020. · URL: https://media.mercedes-benz.it/new-mercedes-benz-strategy-announced---targeting-structurally-higher-profitability/ · Wayback: https://web.archive.org/web/20240228020814/https://media.mercedes-benz.it/new-mercedes-benz-strategy-announced---targeting-structurally-higher-profitability/ (existent; cita no verificada a la captura)

18. [`L2|DE0007100000|c18`] [V] «Ola Källenius, Chairman of the Board of Management, Mercedes-Benz Group AG»
   Anys: 2025 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El comunicat de resultats de l'exercici 2025 és del 12/02/2026 (datePublished 2026-02-12T07:30:21+01:00), dins dels 4 mesos posteriors al tancament del 31/12/2025. Hi consta que, després del 31/10/2025, Källenius continua sent Chairman of the Board of Management (Vorstandsvorsitzender) de Mercedes-Benz Group AG; és la firma de la declaració inicial sobre els resultats. Amb c15 i c16 (29/10/2025) tanca l'interval de la fila 2025. · URL: https://media.mercedes-benz.it/mercedes-benz-group-ag-solid-cash-generation-and-shareholder-returns-in-2025-as-product-launch-campaign-gains-traction/ · Wayback: `pendent_verificacio_externa`

19. [`L2|DE0007100000|c19`] [V] «12 Febbraio 2026 | 07:30 Europe/Amsterdam Mercedes-Benz Group AG: Solid cash generation and shareholder returns in 2025»
   Anys: 2025 · funció: `datacio` · allotjament: `grup` · nivell A · prova: Data del document de c18: 12/02/2026. Coincideix amb el datePublished de la pàgina. · URL: https://media.mercedes-benz.it/mercedes-benz-group-ag-solid-cash-generation-and-shareholder-returns-in-2025-as-product-launch-campaign-gains-traction/ · Wayback: `pendent_verificacio_externa`

### L2.5 Delivery Hero SE Namens-Aktien o.N. (`DE000A2E4K43`)

- isin i anys: `DE000A2E4K43`, 2018-2025 (n=8). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Niklas Östberg → Niklas Östberg (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2018: marca `informe_exercici`; cites del CEO `L2|DE000A2E4K43|C2018a`, `L2|DE000A2E4K43|C2018b`, `L2|DE000A2E4K43|C2018c`; datació `L2|DE000A2E4K43|C2018d`; context `L2|DE000A2E4K43|C_int`.
- 2019: marca `informe_exercici`; cites del CEO `L2|DE000A2E4K43|C2019_s`; context `L2|DE000A2E4K43|C_int`.
- 2020: marca `informe_exercici`; cites del CEO `L2|DE000A2E4K43|C2020_s`; context `L2|DE000A2E4K43|C_int`.
- 2021: marca `informe_exercici`; cites del CEO `L2|DE000A2E4K43|C2021`; context `L2|DE000A2E4K43|C_int`.
- 2022: marca `informe_exercici`; cites del CEO `L2|DE000A2E4K43|C2022a`, `L2|DE000A2E4K43|C2022b`; context `L2|DE000A2E4K43|C_int`.
- 2023: marca `informe_exercici`; cites del CEO `L2|DE000A2E4K43|C2023`; context `L2|DE000A2E4K43|C_int`.
- 2024: marca `informe_exercici`; cites del CEO `L2|DE000A2E4K43|C2024`; context `L2|DE000A2E4K43|C_int`.
- 2025: marca `informe_exercici`; cites del CEO `L2|DE000A2E4K43|C2025a_s`, `L2|DE000A2E4K43|C2025b`; context `L2|DE000A2E4K43|C_int`.
- Correccions de DF: `L2|DE000A2E4K43|C2025a_s` substitueix `L2|DE000A2E4K43|C2025a`; `L2|DE000A2E4K43|C2019_s` substitueix `L2|DE000A2E4K43|C2019`; `L2|DE000A2E4K43|C2020_s` substitueix `L2|DE000A2E4K43|C2020`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/DE000A2E4K43.md](../empreses/DE000A2E4K43.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|DE000A2E4K43|C2018a`] [V] «The CEO Niklas Östberg is responsible for the areas Strategy, Operations,»
   Anys: 2018 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Östberg és el CEO durant l'exercici 2018 · URL: https://ir.deliveryhero.com/media/document/af63258d-50e8-4ccc-8ea4-be622a8e5a06/assets/Final_secured_en.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/af63258d-50e8-4ccc-8ea4-be622a8e5a06/assets/Final_secured_en.pdf (existent; cita no verificada a la captura)

2. [`L2|DE000A2E4K43|C2018b`] [V] «Östberg (chair and CEO) and Emmanuel Thomassin (CFO)»
   Anys: 2018 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Östberg president del Vorstand i CEO a l'exercici 2018 · URL: https://ir.deliveryhero.com/media/document/af63258d-50e8-4ccc-8ea4-be622a8e5a06/assets/Final_secured_en.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/af63258d-50e8-4ccc-8ea4-be622a8e5a06/assets/Final_secured_en.pdf (existent; cita no verificada a la captura)

3. [`L2|DE000A2E4K43|C2018c`] [V] «Niklas Östberg, CEO of Delivery Hero, said:»
   Anys: 2018 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Östberg és CEO el 7/11/2018 (contemporani al 31/10/2018) · URL: https://ir.deliveryhero.com/media/document/5d01ee49-4fc6-48ab-a825-0c5ae78259da/assets/DE000A2E4K43-Q3-2018-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/5d01ee49-4fc6-48ab-a825-0c5ae78259da/assets/DE000A2E4K43-Q3-2018-EQ-E-00.pdf (existent; cita no verificada a la captura)

4. [`L2|DE000A2E4K43|C2018d`] [V] «Berlin, 07 November 2018 – Delivery Hero Group»
   Anys: 2018 · funció: `datacio` · allotjament: `emissor` · nivell A · prova: Data del comunicat C2018c · URL: https://ir.deliveryhero.com/media/document/5d01ee49-4fc6-48ab-a825-0c5ae78259da/assets/DE000A2E4K43-Q3-2018-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/5d01ee49-4fc6-48ab-a825-0c5ae78259da/assets/DE000A2E4K43-Q3-2018-EQ-E-00.pdf (existent; cita no verificada a la captura)

5. [`L2|DE000A2E4K43|C2021`] [V] «Niklas Östberg (CEO) is responsible for the areas Strategy, Operations, Technology, Product, Personnel,»
   Anys: 2021 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Östberg CEO a l'exercici 2021 · URL: https://ir.deliveryhero.com/media/document/35f8a680-3a33-44e4-b1a0-0b750e751b60/assets/DE000A2E4K43-JA-2021-EQ-E-01.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/35f8a680-3a33-44e4-b1a0-0b750e751b60/assets/DE000A2E4K43-JA-2021-EQ-E-01.pdf (existent; cita no verificada a la captura)

6. [`L2|DE000A2E4K43|C2022a`] [V] «The Delivery Hero SE Management Board in financial year 2022 comprised: − Chief Executive Officer Niklas Östberg, businessman, Zollikon, Switzerland – chair of Management Board»
   Anys: 2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Östberg CEO i president del Vorstand durant l'exercici 2022 · URL: https://ir.deliveryhero.com/media/document/2b71e5bb-9774-4dfc-aaff-5367c14005a8/assets/AGM%202023_Annual%20Financial%20Statement_Delivery_Hero_SE_2022.pdf · Wayback: https://web.archive.org/web/20231110115552/https://ir.deliveryhero.com/media/document/2b71e5bb-9774-4dfc-aaff-5367c14005a8/assets/AGM%202023_Annual%20Financial%20Statement_Delivery_Hero_SE_2022.pdf (existent; cita no verificada a la captura)

7. [`L2|DE000A2E4K43|C2022b`] [V] «Niklas Östberg, CEO and Co-Founder of Delivery Hero, said:»
   Anys: 2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Östberg CEO el 10/11/2022 · URL: https://ir.deliveryhero.com/media/document/c5286361-0cd8-4fc5-97ed-5402ab870e37/assets/DE000A2E4K43-Q3-2022-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/c5286361-0cd8-4fc5-97ed-5402ab870e37/assets/DE000A2E4K43-Q3-2022-EQ-E-00.pdf (existent; cita no verificada a la captura)

8. [`L2|DE000A2E4K43|C2023`] [V] «Niklas Östberg (CEO) is responsible for the areas of Strategy, Business Development, Technology, Product, Personnel, Marketing, Payment Solutions,»
   Anys: 2023 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Östberg CEO a l'exercici 2023 · URL: https://ir.deliveryhero.com/media/document/f39e4797-91e8-43f2-82be-e852444a4879/assets/DE000A2E4K43-JA-2023-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20250331005315/https://ir.deliveryhero.com/media/document/f39e4797-91e8-43f2-82be-e852444a4879/assets/DE000A2E4K43-JA-2023-EQ-E-00.pdf (existent; cita no verificada a la captura)

9. [`L2|DE000A2E4K43|C2024`] [V] «SE, Niklas Östberg (Chair of the Management Board, Chief Executive Officer) and Pieter-Jan Vandepitte (Chief Operating Officer) are personally responsible»
   Anys: 2024 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Östberg president del Vorstand i CEO a l'exercici 2024 · URL: https://ir.deliveryhero.com/media/document/c38c7d53-cd6e-44de-8b1f-3559d5c43e6b/assets/DE000A2E4K43-JA-2024-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20260707230924/https://ir.deliveryhero.com/media/document/c38c7d53-cd6e-44de-8b1f-3559d5c43e6b/assets/DE000A2E4K43-JA-2024-EQ-E-00.pdf (existent; cita no verificada a la captura)

10. [`L2|DE000A2E4K43|C2025b`] [V] «Niklas Östberg (CEO) oversees Strategy, Business Development,»
   Anys: 2025 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Östberg CEO a l'exercici 2025 · URL: https://ir.deliveryhero.com/media/document/51222150-5c1c-46db-977b-a078706cccdf/assets/DE000A2E4K43-JA-2025-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20260403040123/https://ir.deliveryhero.com/media/document/51222150-5c1c-46db-977b-a078706cccdf/assets/DE000A2E4K43-JA-2025-EQ-E-00.pdf (existent; cita no verificada a la captura)

11. [`L2|DE000A2E4K43|C_int`] [V] «Niklas Östberg was first appointed as a member of the Company’s Management Board in financial year 2017»
   Anys: 2018-2025 · funció: `context` · allotjament: `emissor` · nivell A · prova: Membre del Vorstand de la SE des de l'exercici 2017 (continuïtat) · URL: https://ir.deliveryhero.com/media/document/51222150-5c1c-46db-977b-a078706cccdf/assets/DE000A2E4K43-JA-2025-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20260403040123/https://ir.deliveryhero.com/media/document/51222150-5c1c-46db-977b-a078706cccdf/assets/DE000A2E4K43-JA-2025-EQ-E-00.pdf (existent; cita no verificada a la captura)

12. [`L2|DE000A2E4K43|C2025a_s`] [V] «In the financial year 2025, Niklas Östberg (Chair of the Management Board, Chief Executive Officer), Pieter-Jan Vandepitte (Chief Operating Officer) and Marie-Anne Popp (Chief Financial Officer) as the Management Board of Delivery Hero SE, managed the business divisions assigned to them under their own responsibility.»
   Anys: 2025 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Durant l'exercici 2025, Östberg va ser president del Management Board i Chief Executive Officer de Delivery Hero SE. · URL: https://ir.deliveryhero.com/media/document/51222150-5c1c-46db-977b-a078706cccdf/assets/DE000A2E4K43-JA-2025-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20260403040123/https://ir.deliveryhero.com/media/document/51222150-5c1c-46db-977b-a078706cccdf/assets/DE000A2E4K43-JA-2025-EQ-E-00.pdf (existent; cita no verificada a la captura) · substitueix `L2|DE000A2E4K43|C2025a`

13. [`L2|DE000A2E4K43|C2019_s`] [V] «As the Management Board of Delivery Hero SE, Niklas Östberg (Chair and CEO) and Emmanuel Thomassin (CFO) are personally responsible for managing the Company’s divisions assigned to them.»
   Anys: 2019 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Östberg era president del Management Board i CEO de Delivery Hero SE a l'exercici 2019. · URL: https://ir.deliveryhero.com/media/document/76180021-64c4-4482-b6ab-638acaada132/assets/DE000A2E4K43-JA-2019-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/76180021-64c4-4482-b6ab-638acaada132/assets/DE000A2E4K43-JA-2019-EQ-E-00.pdf (existent; cita no verificada a la captura) · substitueix `L2|DE000A2E4K43|C2019`

14. [`L2|DE000A2E4K43|C2020_s`] [V] «As the Management Board of Delivery Hero SE, Niklas Östberg (CEO) and Emmanuel Thomassin (CFO), are personally responsible for managing the Company’s business divisions assigned to them.»
   Anys: 2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Östberg era CEO de Delivery Hero SE a l'exercici 2020. · URL: https://ir.deliveryhero.com/media/document/755d9dfe-ac35-4e66-a5c7-37c32cfd69b5/assets/DE000A2E4K43-JA-2020-EQ-E-01.pdf · Wayback: https://web.archive.org/web/20240420045036/https://ir.deliveryhero.com/media/document/755d9dfe-ac35-4e66-a5c7-37c32cfd69b5/assets/DE000A2E4K43-JA-2020-EQ-E-01.pdf (existent; cita no verificada a la captura) · substitueix `L2|DE000A2E4K43|C2020`

### L2.6 OSRAM Licht AG Namens-Aktien o.N.2) (`DE000LED4000`)

- isin i anys: `DE000LED4000`, 2016-2019 (n=4). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Olaf Berlien → Olaf Berlien (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2016: marca `informe_exercici`; cites del CEO `L2|DE000LED4000|C8`, `L2|DE000LED4000|C3`, `L2|DE000LED4000|C2`, `L2|DE000LED4000|C1`, `L2|DE000LED4000|C7`; datació `L2|DE000LED4000|C9`, `L2|DE000LED4000|C17`, `L2|DE000LED4000|C18`, `L2|DE000LED4000|C22`.
- 2017: marca `informe_exercici`; cites del CEO `L2|DE000LED4000|C10`, `L2|DE000LED4000|C4`, `L2|DE000LED4000|C2`, `L2|DE000LED4000|C1`, `L2|DE000LED4000|C7`; datació `L2|DE000LED4000|C11`, `L2|DE000LED4000|C19`, `L2|DE000LED4000|C18`, `L2|DE000LED4000|C22`.
- 2018: marca `prova_interval`; cites del CEO `L2|DE000LED4000|C5`, `L2|DE000LED4000|C10`, `L2|DE000LED4000|C13`, `L2|DE000LED4000|C2`, `L2|DE000LED4000|C1`, `L2|DE000LED4000|C7`; datació `L2|DE000LED4000|C20`, `L2|DE000LED4000|C11`, `L2|DE000LED4000|C14`, `L2|DE000LED4000|C18`, `L2|DE000LED4000|C22`, `L2|DE000LED4000|C16`; context `L2|DE000LED4000|C15`.
- 2019: marca `informe_exercici`; cites del CEO `L2|DE000LED4000|C12`, `L2|DE000LED4000|C13`, `L2|DE000LED4000|C6`, `L2|DE000LED4000|C2`, `L2|DE000LED4000|C1`, `L2|DE000LED4000|C7`; datació `L2|DE000LED4000|C14`, `L2|DE000LED4000|C21`, `L2|DE000LED4000|C18`, `L2|DE000LED4000|C22`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/DE000LED4000.md](../empreses/DE000LED4000.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|DE000LED4000|C1`] [V] «Prior to becoming CEO of Osram in January 2015, Olaf Berlien was CEO of M+W Group GmbH.»
   Anys: 2016-2019 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Inici del mandat: Berlien es CEO d'Osram des del gener de 2015. · URL: https://ams-osram.com/news/press-releases/pr-14-02-2017 · Wayback: https://web.archive.org/web/20260618021349/https://ams-osram.com/news/press-releases/pr-14-02-2017 (existent; cita no verificada a la captura)

2. [`L2|DE000LED4000|C2`] [V] «the supervisory board of OSRAM Licht AG extended the appointment of Chief Executive Officer Olaf Berlien, 54, by five years. The new term will start on January 1, 2018, and run until December 31, 2022.»
   Anys: 2016-2019 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 14/02/2017 Berlien era CEO i el consell de vigilancia li prorroga el nomenament (nou mandat 01/01/2018-31/12/2022): continuitat entre 2016 i 2018. · URL: https://ams-osram.com/news/press-releases/pr-14-02-2017 · Wayback: https://web.archive.org/web/20260618021349/https://ams-osram.com/news/press-releases/pr-14-02-2017 (existent; cita no verificada a la captura)

3. [`L2|DE000LED4000|C3`] [V] «said Olaf Berlien, Chief Executive Officer of OSRAM Licht AG»
   Anys: 2016 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Nou dies despres del 31/10/2016 Berlien es identificat com a CEO d'OSRAM Licht AG. · URL: https://ams-osram.com/news/press-releases/pr-09-11-2016 · Wayback: https://web.archive.org/web/20260718053054/https://ams-osram.com/news/press-releases/pr-09-11-2016 (existent; cita no verificada a la captura)

4. [`L2|DE000LED4000|C4`] [V] «said Olaf Berlien, CEO of OSRAM Licht AG.»
   Anys: 2017 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Sis dies despres del 31/10/2017 Berlien es identificat com a CEO d'OSRAM Licht AG. · URL: https://ams-osram.com/news/press-releases/pr-06-11-2017 · Wayback: https://web.archive.org/web/20260216103531/https://ams-osram.com/news/press-releases/pr-06-11-2017 (existent; cita no verificada a la captura)

5. [`L2|DE000LED4000|C5`] [V] «we are on the right track," said Olaf Berlien, CEO of OSRAM Licht AG.»
   Anys: 2018 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Sis dies despres del 31/10/2018 Berlien es identificat com a CEO d'OSRAM Licht AG. · URL: https://ams-osram.com/news/press-releases/pr-06-11-2018 · Wayback: https://web.archive.org/web/20260512030258/https://ams-osram.com/news/press-releases/pr-06-11-2018 (existent; cita no verificada a la captura)

6. [`L2|DE000LED4000|C6`] [V] «said Olaf Berlien, CEO of OSRAM Licht AG.»
   Anys: 2019 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Dotze dies despres del 31/10/2019 Berlien es identificat com a CEO d'OSRAM Licht AG. · URL: https://ams-osram.com/news/press-releases/pr-12-11-2019 · Wayback: https://web.archive.org/web/20260712083935/https://ams-osram.com/news/press-releases/pr-12-11-2019 (existent; cita no verificada a la captura)

7. [`L2|DE000LED4000|C7`] [V] «CEO Olaf Berlien will leave Osram on February 28 by mutual agreement.»
   Anys: 2016-2019 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Fi del mandat: Berlien continua sent CEO fins al 28/02/2021 (posterior a tots els 31/10 del panell); el mateix document diu que el succeeix Ingo Bank. · URL: https://ams-osram.com/about-us/investor-relations/osram-investor-relations/regulatory-news-en-02-23-2021 · Wayback: https://web.archive.org/web/20241109132604/https://ams-osram.com/about-us/investor-relations/osram-investor-relations/regulatory-news-en-02-23-2021 (existent; cita no verificada a la captura)

8. [`L2|DE000LED4000|C8`] [V] «Dr. Olaf Berlien Chairman of the Managing Board (CEO) Born September 20, 1962 January 1, 2015 December 31, 2022»
   Anys: 2016 · funció: `ceo` · allotjament: `plataforma` · nivell A · prova: Informe anual de l'exercici que inclou el 31/10/2016. Berlien hi consta com a Chairman of the Managing Board (CEO), en el càrrec el 30/09/2017, amb primer nomenament l'01/01/2015. L'informe no documenta cap canvi de CEO a l'exercici: el Report of the Supervisory Board només n'esmenta la pròrroga del mandat (sessió del 14/02/2017), i l'apartat A.3 Events After the Reporting Date diu que no hi ha cap transacció significativa. · URL: https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2016-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20250505141414/https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2016-EQ-E-00.pdf (existent; cita no verificada a la captura)

9. [`L2|DE000LED4000|C9`] [V] «Managing Board of OSRAM Licht AG Members in Office as of September 30, 2017»
   Anys: 2016 · funció: `datacio` · allotjament: `plataforma` · nivell A · prova: Data la taula de C8: membres en el càrrec el 30/09/2017. · URL: https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2016-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20250505141414/https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2016-EQ-E-00.pdf (existent; cita no verificada a la captura)

10. [`L2|DE000LED4000|C10`] [V] «Dr. Olaf Berlien Chairman of the Managing Board (CEO) Born September 20, 1962 January 1, 2015 December 31, 2022»
   Anys: 2017-2018 · funció: `ceo` · allotjament: `plataforma` · nivell A · prova: 2017: és l'informe anual de l'exercici que inclou el 31/10/2017. Berlien hi és CEO, en el càrrec el 30/09/2018, amb primer nomenament l'01/01/2015, i no hi consta cap canvi de CEO: l'apartat C.3.4 només recull canvis al Supervisory Board (Brandt) i els fets posteriors al tancament són la reducció de capital, la recompra i la nova estratègia. 2018: és un document datat dins l'exercici 2019 que confirma Berlien com a CEO amb mandat fins al 31/12/2022. · URL: https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2017-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20240812172129/https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2017-EQ-E-00.pdf (existent; cita no verificada a la captura)

11. [`L2|DE000LED4000|C11`] [V] «Managing Board of OSRAM Licht AG Members in Office as of September 30, 2018»
   Anys: 2017-2018 · funció: `datacio` · allotjament: `plataforma` · nivell A · prova: Data la taula de C10: membres en el càrrec el 30/09/2018. · URL: https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2017-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20240812172129/https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2017-EQ-E-00.pdf (existent; cita no verificada a la captura)

12. [`L2|DE000LED4000|C12`] [V] «As of September 30, 2020, the Supervisory Board had appointed three members of the Managing Board and Dr. Berlien as Chairman of the Managing Board.»
   Anys: 2019 · funció: `ceo` · allotjament: `plataforma` · nivell A · prova: Informe anual de l'exercici que inclou el 31/10/2019: Berlien és Chairman of the Managing Board el 30/09/2020. A l'apartat C.3.5, els únics canvis al Managing Board de l'exercici són el del CFO (Bank surt el 30/04/2020 i Dahnke entra el 16/04/2020). Els del CEO (resolució de l'01/12/2020 i sortida a finals de febrer de 2021) són posteriors al tancament. · URL: https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2019-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20240812142154/https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2019-EQ-E-00.pdf (existent; cita no verificada a la captura)

13. [`L2|DE000LED4000|C13`] [V] «Dr. Olaf Berlien Chairman of the Managing Board (CEO) Born September 20, 1962 January 1, 2015 December 31, 2022»
   Anys: 2018-2019 · funció: `ceo` · allotjament: `plataforma` · nivell A · prova: Berlien és Chairman of the Managing Board (CEO), en el càrrec el 30/09/2020, amb primer nomenament l'01/01/2015. Per al 2019 és l'informe de l'exercici. Per al 2018 és un suport retrospectiu de l'interval. · URL: https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2019-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20240812142154/https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2019-EQ-E-00.pdf (existent; cita no verificada a la captura)

14. [`L2|DE000LED4000|C14`] [V] «Managing Board of OSRAM Licht AG Members in Office as of September 30, 2020»
   Anys: 2018-2019 · funció: `datacio` · allotjament: `plataforma` · nivell A · prova: Data la taula de C13: membres en el càrrec el 30/09/2020. · URL: https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2019-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20240812142154/https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2019-EQ-E-00.pdf (existent; cita no verificada a la captura)

15. [`L2|DE000LED4000|C15`] [V] «Changes to the Supervisory Board and the Managing Board Mr. Michael Knuth stepped down as a member of the Supervisory Boards of OSRAM Licht AG and OSRAM GmbH with effect from the end of the Supervisory Board meeting on May 7, 2019.»
   Anys: 2018 · funció: `context` · allotjament: `plataforma` · nivell A · prova: Context per al 2018: l'apartat de canvis al Supervisory Board i al Managing Board de l'exercici que inclou el 31/10/2018 només recull canvis al Supervisory Board (Knuth i Schulz). No anomena el CEO ni el càrrec, i és un argument per silenci. · URL: https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2018-EQ-E-01.pdf · Wayback: https://web.archive.org/web/20240812152812/https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2018-EQ-E-01.pdf (existent; cita no verificada a la captura)

16. [`L2|DE000LED4000|C16`] [V] «Munich, December 4, 2019 On behalf of the Supervisory Board»
   Anys: 2018 · funció: `datacio` · allotjament: `plataforma` · nivell A · prova: Data l'extracte de C15 el 04/12/2019. · URL: https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2018-EQ-E-01.pdf · Wayback: https://web.archive.org/web/20240812152812/https://irpages2.eqs.com/Download/Companies/osram/Annual%20Reports/DE000LED4000-JA-2018-EQ-E-01.pdf (existent; cita no verificada a la captura)

17. [`L2|DE000LED4000|C17`] [V] «Osram looks back on extraordinarily successful fiscal year 09. November 2016»
   Anys: 2016 · funció: `datacio` · allotjament: `grup` · nivell A · prova: Data el document de C3 el 09/11/2016, dins l'exercici 2017. · URL: https://ams-osram.com/news/press-releases/pr-09-11-2016 · Wayback: https://web.archive.org/web/20260718053054/https://ams-osram.com/news/press-releases/pr-09-11-2016 (existent; cita no verificada a la captura)

18. [`L2|DE000LED4000|C18`] [V] «Osram supervisory board extends appointment of Olaf Berlien 14. February 2017»
   Anys: 2016-2019 · funció: `datacio` · allotjament: `grup` · nivell A · prova: Data el document de C1 i C2 el 14/02/2017. Anomena Berlien però no el càrrec de CEO, per això només serveix de datació. · URL: https://ams-osram.com/news/press-releases/pr-14-02-2017 · Wayback: https://web.archive.org/web/20260618021349/https://ams-osram.com/news/press-releases/pr-14-02-2017 (existent; cita no verificada a la captura)

19. [`L2|DE000LED4000|C19`] [V] «Strong fiscal year lays the foundation for further growth at Osram 06. November 2017»
   Anys: 2017 · funció: `datacio` · allotjament: `grup` · nivell A · prova: Data el document de C4 el 06/11/2017, dins l'exercici 2018. · URL: https://ams-osram.com/news/press-releases/pr-06-11-2017 · Wayback: https://web.archive.org/web/20260216103531/https://ams-osram.com/news/press-releases/pr-06-11-2017 (existent; cita no verificada a la captura)

20. [`L2|DE000LED4000|C20`] [V] «Osram sharpens focus on digital future 06. November 2018»
   Anys: 2018 · funció: `datacio` · allotjament: `grup` · nivell A · prova: Data el document de C5 el 06/11/2018, dins l'exercici 2019, el que inclou el 31/10/2018. · URL: https://ams-osram.com/news/press-releases/pr-06-11-2018 · Wayback: https://web.archive.org/web/20260512030258/https://ams-osram.com/news/press-releases/pr-06-11-2018 (existent; cita no verificada a la captura)

21. [`L2|DE000LED4000|C21`] [V] «Osram recommends current takeover offer from ams 12. November 2019»
   Anys: 2019 · funció: `datacio` · allotjament: `grup` · nivell A · prova: Data el document de C6 el 12/11/2019, dins l'exercici 2020. · URL: https://ams-osram.com/news/press-releases/pr-12-11-2019 · Wayback: https://web.archive.org/web/20260712083935/https://ams-osram.com/news/press-releases/pr-12-11-2019 (existent; cita no verificada a la captura)

22. [`L2|DE000LED4000|C22`] [V] «DGAP-News : OSRAM Licht AG / Key word(s): AGM/EGM Osram well equipped for the future thanks to efficient management 23.02.2021 / 10:00»
   Anys: 2016-2019 · funció: `datacio` · allotjament: `grup` · nivell A · prova: Data el document de C7 el 23/02/2021, de manera que el «February 28» de la sortida és el 28/02/2021. · URL: https://ams-osram.com/about-us/investor-relations/osram-investor-relations/regulatory-news-en-02-23-2021 · Wayback: https://web.archive.org/web/20241109132604/https://ams-osram.com/about-us/investor-relations/osram-investor-relations/regulatory-news-en-02-23-2021 (existent; cita no verificada a la captura)

### L2.7 Carlsberg AS Navne-Aktier B DK 20 (`DK0010181759`)

- isin i anys: `DK0010181759`, 2016-2022 (n=7). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Cees ’t Hart → Cees ’t Hart (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2016: marca `informe_exercici`; cites del CEO `L2|DK0010181759|AR2016-sig`, `L2|DK0010181759|AR2016-excom`, `L2|DK0010181759|AR2023-inici`; context `L2|DK0010181759|AR2023-fi`, `L2|DK0010181759|AR2023-successor`.
- 2017: marca `informe_exercici`; cites del CEO `L2|DK0010181759|AR2017-sig`, `L2|DK0010181759|AR2023-inici`; context `L2|DK0010181759|AR2023-fi`, `L2|DK0010181759|AR2023-successor`.
- 2018: marca `informe_exercici`; cites del CEO `L2|DK0010181759|AR2018-sig`, `L2|DK0010181759|AR2023-inici`; context `L2|DK0010181759|AR2023-fi`, `L2|DK0010181759|AR2023-successor`.
- 2019: marca `informe_exercici`; cites del CEO `L2|DK0010181759|AR2019-sig`, `L2|DK0010181759|AR2019-excom`, `L2|DK0010181759|AR2023-inici`; context `L2|DK0010181759|AR2023-fi`, `L2|DK0010181759|AR2023-successor`.
- 2020: marca `informe_exercici`; cites del CEO `L2|DK0010181759|AR2020-sig`, `L2|DK0010181759|AR2020-excom`, `L2|DK0010181759|AR2023-inici`; context `L2|DK0010181759|AR2023-fi`, `L2|DK0010181759|AR2023-successor`.
- 2021: marca `informe_exercici`; cites del CEO `L2|DK0010181759|AR2021-sig`, `L2|DK0010181759|AR2021-excom`, `L2|DK0010181759|AR2023-inici`; context `L2|DK0010181759|AR2023-fi`, `L2|DK0010181759|AR2023-successor`.
- 2022: marca `informe_exercici`; cites del CEO `L2|DK0010181759|AR2022-carta`, `L2|DK0010181759|AR2023-inici`; context `L2|DK0010181759|AR2022-sig`, `L2|DK0010181759|AR2023-fi`, `L2|DK0010181759|AR2023-successor`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/DK0010181759.md](../empreses/DK0010181759.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|DK0010181759|AR2016-sig`] [V] «Copenhagen, 8 February 2017 Executive Board of Carlsberg A/S Cees 't Hart CEO»
   Anys: 2016 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Declaració de la direcció de l'informe anual 2016, signada el febrer de 2017: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/ye3p241k/carlsberg-group-annual-report-2016.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-annual-report-2016/ · Wayback: `pendent_verificacio_externa`

2. [`L2|DK0010181759|AR2017-sig`] [V] «Copenhagen, 7 February 2018 Executive Board of Carlsberg A/S Cees 't Hart President & CEO»
   Anys: 2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Declaració de la direcció de l'informe anual 2017, signada el febrer de 2018: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/2emjcnhk/carlsberg-as_annual-report-2017.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-annual-report-2017/ · Wayback: `pendent_verificacio_externa`

3. [`L2|DK0010181759|AR2018-sig`] [V] «Copenhagen, 6 February 2019 Executive Board of Carlsberg A/S Cees 't Hart President & CEO»
   Anys: 2018 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Declaració de la direcció de l'informe anual 2018, signada el febrer de 2019: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/1xcd3qqb/carlsberg-as-2018-annual-report.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-annual-report-2018/ · Wayback: `pendent_verificacio_externa`

4. [`L2|DK0010181759|AR2019-sig`] [V] «Copenhagen, 4 February 2020 Executive Board of Carlsberg A/S Cees ’t Hart President & CEO»
   Anys: 2019 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Declaració de la direcció de l'informe anual 2019, signada el febrer de 2020: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/ffqdx3n0/carlsberg-as-annual-report-2019.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-annual-report-2019/ · Wayback: `pendent_verificacio_externa`

5. [`L2|DK0010181759|AR2020-sig`] [V] «Copenhagen, 5 February 2021 Executive Board of Carlsberg A/S Cees ’t Hart President & CEO»
   Anys: 2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Declaració de la direcció de l'informe anual 2020, signada el febrer de 2021: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/fb2firdc/carlsberg-group-annual-report-2020_final.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2020-annual-report/ · Wayback: `pendent_verificacio_externa`

6. [`L2|DK0010181759|AR2021-sig`] [V] «Copenhagen, 4 February 2022 Executive Board of Carlsberg A/S Cees ’t Hart President & CEO»
   Anys: 2021 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Declaració de la direcció de l'informe anual 2021, signada el febrer de 2022: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/l2phgf1k/carlsberg-goup-annual-report-2021.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2021-annual-report/ · Wayback: `pendent_verificacio_externa`

7. [`L2|DK0010181759|AR2022-sig`] [V] «Copenhagen, 7 February 2023 Executive Board of Carlsberg A/S Cees 't Hart Ulrica Fearn President & CEO CFO»
   Anys: 2022 · funció: `context` · allotjament: `emissor` · nivell A · prova: Declaració de la direcció de l'informe anual 2022, signada el febrer de 2023: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/rscmtzgy/carlsberg-group-annual-report-2022.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2022-annual-report/ · Wayback: `pendent_verificacio_externa`

8. [`L2|DK0010181759|AR2016-excom`] [V] «Executive Committee (ExCom) Cees ’t Hart CEO since 2015.»
   Anys: 2016 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Cees 't Hart és CEO des de 2015 (secció del comitè executiu de l'informe 2016). (La URL redirigeix a https://www.carlsberggroup.com/media/ye3p241k/carlsberg-group-annual-report-2016.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-annual-report-2016/ · Wayback: `pendent_verificacio_externa`

9. [`L2|DK0010181759|AR2019-excom`] [V] «CEES ’T HART CEO Nationality: Dutch Year of birth: 1958 Appointed: 2015»
   Anys: 2019 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Fitxa del comitè executiu de l'informe 2019: Cees 't Hart, CEO, nomenat el 2015. (La URL redirigeix a https://www.carlsberggroup.com/media/ffqdx3n0/carlsberg-as-annual-report-2019.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-annual-report-2019/ · Wayback: `pendent_verificacio_externa`

10. [`L2|DK0010181759|AR2020-excom`] [V] «CEES ’T HART CEO Nationality: Dutch Year of birth: 1958 Appointed: 2015»
   Anys: 2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Fitxa del comitè executiu de l'informe 2020: Cees 't Hart, CEO, nomenat el 2015. (La URL redirigeix a https://www.carlsberggroup.com/media/fb2firdc/carlsberg-group-annual-report-2020_final.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2020-annual-report/ · Wayback: `pendent_verificacio_externa`

11. [`L2|DK0010181759|AR2021-excom`] [V] «CEES ’T HART CEO Nationality: Dutch Year of birth: 1958 Appointed: 2015»
   Anys: 2021 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Fitxa del comitè executiu de l'informe 2021: Cees 't Hart, CEO, nomenat el 2015. (La URL redirigeix a https://www.carlsberggroup.com/media/l2phgf1k/carlsberg-goup-annual-report-2021.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2021-annual-report/ · Wayback: `pendent_verificacio_externa`

12. [`L2|DK0010181759|AR2022-carta`] [V] «deliver strong results despite significant challenges during the year. Cees ’t Hart CEO»
   Anys: 2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Carta als accionistes de l'informe 2022, amb Cees 't Hart identificat com a CEO. (La URL redirigeix a https://www.carlsberggroup.com/media/rscmtzgy/carlsberg-group-annual-report-2022.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2022-annual-report/ · Wayback: `pendent_verificacio_externa`

13. [`L2|DK0010181759|AR2023-inici`] [V] «We said farewell to Cees ’t Hart, our CEO since June 2015.»
   Anys: 2016-2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Interval: 't Hart va ser CEO des de juny de 2015. (La URL redirigeix a https://www.carlsberggroup.com/media/3kjbpwaa/carlsberg-group-2023-annual-report.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2023-annual-report/ · Wayback: `pendent_verificacio_externa`

14. [`L2|DK0010181759|AR2023-fi`] [V] «After eight years at the helm of the Carlsberg Group, Cees ’t Hart retired at the end of August.»
   Anys: 2016-2022 · funció: `context` · allotjament: `emissor` · nivell A · prova: Interval: 't Hart es va retirar a finals d'agost de 2023 (segons el context del document, que parla de 2023). (La URL redirigeix a https://www.carlsberggroup.com/media/3kjbpwaa/carlsberg-group-2023-annual-report.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2023-annual-report/ · Wayback: `pendent_verificacio_externa`

15. [`L2|DK0010181759|AR2023-successor`] [V] «On 1 September, we welcomed Jacob Aarup-Andersen as the new CEO of the Carlsberg Group.»
   Anys: 2016-2022 · funció: `context` · allotjament: `emissor` · nivell A · prova: El successor entra l'1 de setembre (de 2023, segons l'informe 2023); per tant no hi ha canvi de CEO a prop de cap 31/10 de 2016-2022. (La URL redirigeix a https://www.carlsberggroup.com/media/3kjbpwaa/carlsberg-group-2023-annual-report.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2023-annual-report/ · Wayback: `pendent_verificacio_externa`

### L2.8 Christian Hansen Holding AS Navne-Aktier (`DK0060227585`)

- isin i anys: `DK0060227585`, 2016-2017 (n=2). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Cees de Jong → Cees de Jong (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2016: marca `informe_exercici`; cites del CEO `L2|DK0060227585|C1`, `L2|DK0060227585|C5`, `L2|DK0060227585|C10`, `L2|DK0060227585|C11`; datació `L2|DK0060227585|C2`, `L2|DK0060227585|C7`, `L2|DK0060227585|C15`; context `L2|DK0060227585|C6`.
- 2017: marca `prova_interval`; cites del CEO `L2|DK0060227585|C3`, `L2|DK0060227585|C5`, `L2|DK0060227585|C12`, `L2|DK0060227585|C13`; datació `L2|DK0060227585|C4`, `L2|DK0060227585|C7`, `L2|DK0060227585|C9`, `L2|DK0060227585|C14`, `L2|DK0060227585|C16`; context `L2|DK0060227585|C8`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/DK0060227585.md](../empreses/DK0060227585.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|DK0060227585|C1`] [V] «So I can only be pleased with how we performed in 2015/16” says CEO Cees de Jong.»
   Anys: 2016 · funció: `ceo` · allotjament: `plataforma` · nivell A · prova: Comunicat de resultats anuals 2015/16: Cees de Jong hi parla com a CEO. · URL: https://www.mynewsdesk.com/com/chr-hansen/pressreleases/very-satisfactory-annual-result-12-procent-growth-1622919 · Wayback: `pendent_verificacio_externa`

2. [`L2|DK0060227585|C2`] [V] «Press release — 26 October 2016»
   Anys: 2016 · funció: `datacio` · allotjament: `plataforma` · nivell A · prova: Data del comunicat C1 (26/10/2016, cinc dies abans del 31/10/2016). · URL: https://www.mynewsdesk.com/com/chr-hansen/pressreleases/very-satisfactory-annual-result-12-procent-growth-1622919 · Wayback: `pendent_verificacio_externa`

3. [`L2|DK0060227585|C3`] [V] «in line with our Nature’s no. 1 strategy,” says CEO Cees de Jong.»
   Anys: 2017 · funció: `ceo` · allotjament: `plataforma` · nivell A · prova: Comunicat de resultats anuals 2016/17: Cees de Jong hi parla com a CEO. · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/another-good-year-for-chr-hansen-10-procent-organic-growth-2231116 · Wayback: https://web.archive.org/web/20190916201847/http://www.mynewsdesk.com/chr-hansen/pressreleases/another-good-year-for-chr-hansen-10-procent-organic-growth-2231116 (existent; cita no verificada a la captura)

4. [`L2|DK0060227585|C4`] [V] «Press release — 25 October 2017»
   Anys: 2017 · funció: `datacio` · allotjament: `plataforma` · nivell A · prova: Data del comunicat C3 (25/10/2017, sis dies abans del 31/10/2017). · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/another-good-year-for-chr-hansen-10-procent-organic-growth-2231116 · Wayback: https://web.archive.org/web/20190916201847/http://www.mynewsdesk.com/chr-hansen/pressreleases/another-good-year-for-chr-hansen-10-procent-organic-growth-2231116 (existent; cita no verificada a la captura)

5. [`L2|DK0060227585|C5`] [V] «The Company has initiated a process to find his replacement, and until then Cees de Jong will continue as CEO of Chr. Hansen.»
   Anys: 2016-2017 · funció: `ceo` · allotjament: `plataforma` · nivell A · prova: El 28/11/2017 De Jong encara és CEO i continua fins que hi hagi substitut. · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/cees-de-jong-will-step-down-as-ceo-of-chr-hansen-holding-a-skraastreg-s-2302223 · Wayback: https://web.archive.org/web/20171203185341/http://www.mynewsdesk.com:80/chr-hansen/pressreleases/cees-de-jong-will-step-down-as-ceo-of-chr-hansen-holding-a-skraastreg-s-2302223 (existent; cita no verificada a la captura)

6. [`L2|DK0060227585|C6`] [V] «it is, and has been, a privilege to be the CEO since 2013.»
   Anys: 2016 · funció: `context` · allotjament: `plataforma` · nivell A · prova: De Jong (cita seva al comunicat) és CEO de manera continuada des del 2013. · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/cees-de-jong-will-step-down-as-ceo-of-chr-hansen-holding-a-skraastreg-s-2302223 · Wayback: https://web.archive.org/web/20171203185341/http://www.mynewsdesk.com:80/chr-hansen/pressreleases/cees-de-jong-will-step-down-as-ceo-of-chr-hansen-holding-a-skraastreg-s-2302223 (existent; cita no verificada a la captura)

7. [`L2|DK0060227585|C7`] [V] «Press release — 28 November 2017»
   Anys: 2016-2017 · funció: `datacio` · allotjament: `plataforma` · nivell A · prova: Data del comunicat C5/C6. · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/cees-de-jong-will-step-down-as-ceo-of-chr-hansen-holding-a-skraastreg-s-2302223 · Wayback: https://web.archive.org/web/20171203185341/http://www.mynewsdesk.com:80/chr-hansen/pressreleases/cees-de-jong-will-step-down-as-ceo-of-chr-hansen-holding-a-skraastreg-s-2302223 (existent; cita no verificada a la captura)

8. [`L2|DK0060227585|C8`] [V] «The Board of Directors of Chr. Hansen Holding A/S has today appointed Mauricio Graber as new Chief Executive Officer (CEO) as of 1 June 2018.»
   Anys: 2017 · funció: `context` · allotjament: `plataforma` · nivell A · prova: El successor Mauricio Graber és CEO amb efecte 1/6/2018; fins llavors no hi ha canvi. · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/mauricio-graber-appointed-new-ceo-of-chr-hansen-holding-a-skraastreg-s-2361711 · Wayback: https://web.archive.org/web/20230207171338/https://www.mynewsdesk.com/chr-hansen/pressreleases/mauricio-graber-appointed-new-ceo-of-chr-hansen-holding-a-skraastreg-s-2361711 (existent; cita no verificada a la captura)

9. [`L2|DK0060227585|C9`] [V] «Press release — 8 January 2018»
   Anys: 2017 · funció: `datacio` · allotjament: `plataforma` · nivell A · prova: Data del comunicat C8. · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/mauricio-graber-appointed-new-ceo-of-chr-hansen-holding-a-skraastreg-s-2361711 · Wayback: https://web.archive.org/web/20230207171338/https://www.mynewsdesk.com/chr-hansen/pressreleases/mauricio-graber-appointed-new-ceo-of-chr-hansen-holding-a-skraastreg-s-2361711 (existent; cita no verificada a la captura)

10. [`L2|DK0060227585|C10`] [V] «CEES DE JONG – President & Chief Executive Officer Born 1961. Dutch national. Joined Chr. Hansen in 2013.»
   Anys: 2016 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: La secció «Executive Board – Chr. Hansen Holding A/S» de l'informe anual de l'exercici que inclou el 31/10/2016 anomena Cees de Jong President & Chief Executive Officer. · URL: https://attachment.news.eu.nasdaq.com/a5065e5640d97b2a2a51d989188c0e3e1 · Wayback: `pendent_verificacio_externa`

11. [`L2|DK0060227585|C11`] [V] «Hørsholm, 25 October 2017 Executive Board Cees de Jong President and CEO»
   Anys: 2016 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Cees de Jong signa l'informe anual 2016/17 com a President and CEO el 25/10/2017. El nom i el càrrec són tots dos dins el fragment. · URL: https://attachment.news.eu.nasdaq.com/a5065e5640d97b2a2a51d989188c0e3e1 · Wayback: `pendent_verificacio_externa`

12. [`L2|DK0060227585|C15`] [V] «adopted the Annual Report of Chr. Hansen Holding A/S for the financial year 1 September 2016 – 31 August 2017.»
   Anys: 2016 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: L'exercici de l'informe de C10 i C11 va de l'1/9/2016 al 31/8/2017 i, per tant, inclou el 31/10/2016. · URL: https://attachment.news.eu.nasdaq.com/a5065e5640d97b2a2a51d989188c0e3e1 · Wayback: `pendent_verificacio_externa`

13. [`L2|DK0060227585|C12`] [V] «On June 1, 2018, Mauricio Graber replaced Cees de Jong as CEO of Chr. Hansen.»
   Anys: 2017 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: L'informe anual de l'exercici que inclou el 31/10/2017 diu que De Jong era el CEO fins que Graber el va substituir l'1/6/2018. Documenta, per tant, un canvi de CEO entre el 31/10/2017 i el tancament. · URL: https://attachment.news.eu.nasdaq.com/aaadd97cba48fc4f2e37000cd2d509c4c · Wayback: `pendent_verificacio_externa`

14. [`L2|DK0060227585|C16`] [V] «adopted the Annual Report of Chr. Hansen Holding A/S for the financial year September 1, 2017 – August 31, 2018.»
   Anys: 2017 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: L'exercici de l'informe de C12 va de l'1/9/2017 al 31/8/2018 i, per tant, inclou el 31/10/2017. · URL: https://attachment.news.eu.nasdaq.com/aaadd97cba48fc4f2e37000cd2d509c4c · Wayback: `pendent_verificacio_externa`

15. [`L2|DK0060227585|C13`] [V] «CEO Cees de Jong says: “We have had a solid start to the year»
   Anys: 2017 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: L'informe del trimestre que inclou el 31/10/2017 anomena Cees de Jong CEO. És un document contemporani de l'exercici 2017/18. · URL: https://attachment.news.eu.nasdaq.com/a104fcd7d7254ff535cd063e1a92b2c57 · Wayback: `pendent_verificacio_externa`

16. [`L2|DK0060227585|C14`] [V] «INTERIM REPORT 1 SEPTEMBER 2017 - 30 NOVEMBER 2017»
   Anys: 2017 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: Període cobert per C13 (1/9/2017-30/11/2017), que inclou el 31/10/2017. · URL: https://attachment.news.eu.nasdaq.com/a104fcd7d7254ff535cd063e1a92b2c57 · Wayback: `pendent_verificacio_externa`

### L2.9 BANKIA S.A. Acciones Nominativas EO 0,8 (`ES0113307021`)

- isin i anys: `ES0113307021`, 2016 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **José Sevilla Álvarez → José Sevilla Álvarez (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A, B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2016: marca `informe_exercici+ceo_titol_amb_president_executiu`; cites del CEO `L2|ES0113307021|c2`, `L2|ES0113307021|c3`, `L2|ES0113307021|c5`; datació `L2|ES0113307021|c1`, `L2|ES0113307021|c6`; context `L2|ES0113307021|c4`, `L2|ES0113307021|c7`, `L2|ES0113307021|c8`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/ES0113307021.md](../empreses/ES0113307021.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|ES0113307021|c1`] [V] «correspondientes al ejercicio anual terminado el 31 de diciembre de 2016»
   Anys: 2016 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: El document cobreix l'exercici natural 2016, que inclou el 31/10/2016. · URL: https://www.cnmv.es/AUDITA/2016/16764.pdf · Wayback: https://web.archive.org/web/20240528024914/https://www.cnmv.es/AUDITA/2016/16764.pdf (existent; cita no verificada a la captura)

2. [`L2|ES0113307021|c2`] [V] «D. José Sevilla Álvarez. Consejero Delegado»
   Anys: 2016 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Composició del consell a l'informe de gestió de 2016: Sevilla és el Consejero Delegado. · URL: https://www.cnmv.es/AUDITA/2016/16764.pdf · Wayback: https://web.archive.org/web/20240528024914/https://www.cnmv.es/AUDITA/2016/16764.pdf (existent; cita no verificada a la captura)

3. [`L2|ES0113307021|c3`] [V] «DON JOSÉ SEVILLA ÁLVAREZ CONSEJERO DELEGADO»
   Anys: 2016 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Càrrec a l'organigrama a l'IAGC de l'exercici tancat el 31/12/2016: Consejero Delegado. · URL: https://www.cnmv.es/AUDITA/2016/16764.pdf · Wayback: https://web.archive.org/web/20240528024914/https://www.cnmv.es/AUDITA/2016/16764.pdf (existent; cita no verificada a la captura)

4. [`L2|ES0113307021|c4`] [V] «Asimismo, la Junta General de Accionistas acordó reelegir como consejeros, con sus calificaciones correspondientes, por el plazo estatutario de cuatro años, a D. José Sevilla Álvarez»
   Anys: 2016 · funció: `context` · allotjament: `regulador` · nivell A · prova: Reelecció de Sevilla com a conseller per la Junta de 2016 (continuïtat durant l'exercici). · URL: https://www.cnmv.es/AUDITA/2016/16764.pdf · Wayback: https://web.archive.org/web/20240528024914/https://www.cnmv.es/AUDITA/2016/16764.pdf (existent; cita no verificada a la captura)

5. [`L2|ES0113307021|c5`] [V] «Así lo afirmó este miércoles el consejero delegado de Bankia, José Sevilla, durante la presentación de los resultados del banco en el tercer trimestre del año.»
   Anys: 2016 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Sevilla actua com a consejero delegado de Bankia el 26/10/2016, cinc dies abans de la data de referència. · URL: https://www.elindependiente.com/?p=26973 · Wayback: `pendent_verificacio_externa`

6. [`L2|ES0113307021|c6`] [V] «2016-10-26T12:04:24+00:00»
   Anys: 2016 · funció: `datacio` · allotjament: `mitja` · nivell B · prova: Data de publicació de la notícia de c5 (26/10/2016). · URL: https://www.elindependiente.com/?p=26973 · Wayback: `pendent_verificacio_externa`

7. [`L2|ES0113307021|c7`] [V] «DON JOSÉ IGNACIO GOIRIGOLZARRI TELLAECHE Breve descripción: El Presidente del Consejo de Administración ostenta amplios poderes de representación y administración acordes con las características y necesidades del cargo de Presidente ejecutivo de la entidad, teniendo delegadas todas y cada una de las facultades, salvo las legal y estatutariamente indelegables.»
   Anys: 2016 · funció: `context` · allotjament: `regulador` · nivell A · prova: A l'IAGC de l'exercici 2016, José Ignacio Goirigolzarri Tellaeche és el Presidente del Consejo amb el càrrec de Presidente ejecutivo. Té delegades «todas y cada una de las facultades, salvo las legal y estatutariamente indelegables». Documenta l'estructura amb president executiu; no és cita del CEO de la fila. · URL: https://www.cnmv.es/AUDITA/2016/16764.pdf · Wayback: https://web.archive.org/web/20240528024914/https://www.cnmv.es/AUDITA/2016/16764.pdf (existent; cita no verificada a la captura)

8. [`L2|ES0113307021|c8`] [V] «DON JOSÉ SEVILLA ÁLVAREZ Breve descripción: El Sr. Sevilla tiene delegadas con carácter solidario a su favor todas las facultades legal y estatutariamente delegables en las áreas de dirección financiera y de riesgos, intervención y auditoría interna, así como inmobiliario y empresas participadas, y asesoramiento jurídico, fiscal y cumplimiento.»
   Anys: 2016 · funció: `context` · allotjament: `regulador` · nivell A · prova: Facultats delegades a José Sevilla Álvarez a l'exercici 2016, en els termes literals de la frase. El càrrec de Consejero Delegado no és dins el fragment: surt a c2 i c3 del mateix PDF. · URL: https://www.cnmv.es/AUDITA/2016/16764.pdf · Wayback: https://web.archive.org/web/20240528024914/https://www.cnmv.es/AUDITA/2016/16764.pdf (existent; cita no verificada a la captura)

### L2.10 Alten S.A. Actions au Porteur EO 1,05 (`FR0000071946`)

- isin i anys: `FR0000071946`, 2018-2024 (n=7). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Simon Azoulay → Simon Azoulay (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2018: marca `prova_interval`; cites del CEO `L2|FR0000071946|c22`, `L2|FR0000071946|c14`, `L2|FR0000071946|c19`, `L2|FR0000071946|c13`, `L2|FR0000071946|c11`, `L2|FR0000071946|c1`; datació `L2|FR0000071946|c23`, `L2|FR0000071946|c15`, `L2|FR0000071946|c20`; context `L2|FR0000071946|c2`.
- 2019: marca `prova_interval`; cites del CEO `L2|FR0000071946|c19`, `L2|FR0000071946|c16`, `L2|FR0000071946|c21`, `L2|FR0000071946|c13`, `L2|FR0000071946|c11`, `L2|FR0000071946|c1`; datació `L2|FR0000071946|c20`, `L2|FR0000071946|c17`; context `L2|FR0000071946|c2`.
- 2020: marca `informe_exercici`; cites del CEO `L2|FR0000071946|c1`, `L2|FR0000071946|c13`; datació `L2|FR0000071946|c4`; context `L2|FR0000071946|c2`.
- 2021: marca `informe_exercici`; cites del CEO `L2|FR0000071946|c5`, `L2|FR0000071946|c11`; datació `L2|FR0000071946|c18`.
- 2022: marca `informe_exercici`; cites del CEO `L2|FR0000071946|c6`, `L2|FR0000071946|c11`; datació `L2|FR0000071946|c7`.
- 2023: marca `informe_exercici`; cites del CEO `L2|FR0000071946|c8`, `L2|FR0000071946|c11`; datació `L2|FR0000071946|c9`.
- 2024: marca `informe_exercici`; cites del CEO `L2|FR0000071946|c10`, `L2|FR0000071946|c11`; datació `L2|FR0000071946|c12`.
- Correccions de DF: `L2|FR0000071946|c13` substitueix `L2|FR0000071946|c3`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/FR0000071946.md](../empreses/FR0000071946.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|FR0000071946|c1`] [V] «Le Conseil d’administration d’ALTEN a ainsi opté, depuis 2002, pour le cumul des fonctions de Président du Conseil d’administration et de Directeur général. La Direction générale de la Société est exercée par Monsieur Simon AZOULAY, assisté de deux Directeurs Généraux Délégués.»
   Anys: 2018-2020 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Des de 2002 les funcions de president i Directeur général estan acumulades i la Direction générale l'exerceix Simon Azoulay (document de l'exercici 2020). · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf · Wayback: https://web.archive.org/web/20210712185007/https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf (existent; cita no verificada a la captura)

2. [`L2|FR0000071946|c2`] [V] «19 février 1997 (Administrateur) – 22 septembre 1998 (PDG). DATE DU DERNIER RENOUVELLEMENT : 22 juin 2017 (Administrateur et PDG).»
   Anys: 2018-2020 · funció: `context` · allotjament: `regulador` · nivell A · prova: Fitxa de mandats de 'M. SIMON AZOULAY Président-Directeur général d’ALTEN': primer nomenament com a PDG el 22/09/1998 i darrera renovació com a PDG el 22/06/2017. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf · Wayback: https://web.archive.org/web/20210712185007/https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf (existent; cita no verificada a la captura)

3. [`L2|FR0000071946|c4`] [V] «Le document d’enregistrement universel a été déposé auprès de l’AMF, le 28 avril 2021»
   Anys: 2020 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: Data de dipòsit de l'URD 2020. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf · Wayback: https://web.archive.org/web/20210712185007/https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf (existent; cita no verificada a la captura)

4. [`L2|FR0000071946|c5`] [V] «En 2002, le Conseil d’administration a décidé l’unicité des fonctions de Président du Conseil d’administration et de Directeur général. Cette décision n’a pas été modifiée depuis lors. Ces fonctions sont exercées par Monsieur Simon AZOULAY, assisté par un Directeur Général Délégué.»
   Anys: 2021 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Unicitat de les funcions de president i Directeur général des de 2002, sense modificació, exercides per Simon Azoulay (document de l'exercici 2021). · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317442505_20220429.zip · Wayback: `pendent_verificacio_externa`

5. [`L2|FR0000071946|c6`] [V] «En 2002, le Conseil d’administration a décidé l’unicité des fonctions de Président du Conseil d’administration et de Directeur général. Cette décision n’a pas été modifiée depuis lors. Ces fonctions sont exercées par Monsieur Simon AZOULAY»
   Anys: 2022 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Unicitat de funcions des de 2002, no modificada des d'aleshores, exercides per Simon Azoulay (document de l'exercici 2022). · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317481759_20230427.pdf · Wayback: https://web.archive.org/web/20261112013824/https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317481759_20230427.pdf (existent; cita no verificada a la captura)

6. [`L2|FR0000071946|c7`] [V] «Le Document d’enregistrement universel a été déposé le 27 avril 2023 auprès de l’AMF»
   Anys: 2022 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: Data de dipòsit de l'URD 2022. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317481759_20230427.pdf · Wayback: https://web.archive.org/web/20261112013824/https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317481759_20230427.pdf (existent; cita no verificada a la captura)

7. [`L2|FR0000071946|c8`] [V] «En 2002, le Conseil d’administration a décidé l’unicité des fonctions de Président du Conseil d’administration et de Directeur général. Cette décision n’a pas été modifiée depuis lors. Ces fonctions sont exercées par Monsieur Simon AZOULAY»
   Anys: 2023 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Unicitat de funcions des de 2002, no modificada des d'aleshores, exercides per Simon Azoulay (document de l'exercici 2023). · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317528771_20240426.pdf · Wayback: `pendent_verificacio_externa`

8. [`L2|FR0000071946|c9`] [V] «Le Document d’enregistrement universel a été déposé le 26 avril 2024 auprès de l’AMF»
   Anys: 2023 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: Data de dipòsit de l'URD 2023. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317528771_20240426.pdf · Wayback: `pendent_verificacio_externa`

9. [`L2|FR0000071946|c10`] [V] «Monsieur Simon AZOULAY exerce les fonctions de Président-Directeur général. Son mandat arrive à échéance lors de l’Assemblée générale annuelle 2025.»
   Anys: 2024 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Simon Azoulay exerceix de Président-Directeur général (document de l'exercici 2024, dipositat l'abril de 2025). · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip · Wayback: `pendent_verificacio_externa`

10. [`L2|FR0000071946|c11`] [V] «Simon AZOULAY Président-Directeur général Date de début de mandat : 22/09/1998 Date de fin de mandat : Assemblée à tenir en 2025 et appelée à statuer sur les comptes de l’exercice 2024.»
   Anys: 2018-2019, 2021-2024 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Interval de mandat: PDG des del 22/09/1998 fins a la junta de 2025 que aprova els comptes de 2024; cobreix tots els 31/10 de 2018 a 2024. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip · Wayback: `pendent_verificacio_externa`

11. [`L2|FR0000071946|c12`] [V] «Le Document d’enregistrement universel a été déposé le 25 avril 2025 auprès de l’AMF»
   Anys: 2024 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: Data de dipòsit de l'URD 2024. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip · Wayback: `pendent_verificacio_externa`

12. [`L2|FR0000071946|c13`] [V] «Simon AZOULAY Président-Directeur général Date de début de mandat : 22/09/1998 Date de fin de mandat : Assemblée à tenir en 2021 et appelée à statuer sur les comptes de l’exercice écoulé.»
   Anys: 2018-2020 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Fila de la taula amb el nom i el càrrec (Simon AZOULAY, Président-Directeur général) i el mandat des del 22/09/1998 fins a la junta de 2021, tot a la mateixa cel·la. Cobreix el 31/10 de 2018, 2019 i 2020. Amplia de manera contigua l'antiga c3, que no tenia nom ni càrrec. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf · Wayback: https://web.archive.org/web/20210712185007/https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf (existent; cita no verificada a la captura) · substitueix `L2|FR0000071946|c3`

13. [`L2|FR0000071946|c14`] [V] «approuve les éléments fixes, variables et exceptionnels composant la rémunération totale et les avantages de toute nature versés ou attribués au titre de l'exercice écoulé en raison de son mandat à Monsieur Simon AZOULAY, Président Directeur général, tels que présentés dans le document de référence page 181.»
   Anys: 2018 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: L'anunci de l'emissor del 16/05/2018, dins l'exercici 2018, anomena Simon AZOULAY «Président Directeur général». És una cita contemporània per a 2018. La resolució aprova la remuneració de l'exercici anterior. · URL: https://www.journal-officiel.gouv.fr/telechargements/BALO/pdf/2018/0516/201805161801885.pdf · Wayback: `pendent_verificacio_externa`

14. [`L2|FR0000071946|c15`] [V] «16 mai 2018 BULLETIN DES ANNONCES LEGALES OBLIGATOIRES Avis de convocation / avis de réunion»
   Anys: 2018 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: Data de publicació de l'avis de réunion: 16/05/2018. · URL: https://www.journal-officiel.gouv.fr/telechargements/BALO/pdf/2018/0516/201805161801885.pdf · Wayback: `pendent_verificacio_externa`

15. [`L2|FR0000071946|c16`] [V] «approuve les éléments fixes, variables et exceptionnels composant la rémunération totale et les avantages de toute nature versés ou attribués au titre de l'exercice écoulé en raison de son mandat à Monsieur Simon AZOULAY, Président directeur général, tels que présentés dans le document de référence 2018 paragraphe 15.1.2.»
   Anys: 2019 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: L'anunci de l'emissor del 10/05/2019, dins l'exercici 2019, anomena Simon AZOULAY «Président directeur général». És una cita contemporània per a 2019. · URL: https://www.journal-officiel.gouv.fr/telechargements/BALO/pdf/2019/0510/201905101901713.pdf · Wayback: `pendent_verificacio_externa`

16. [`L2|FR0000071946|c17`] [V] «10 mai 2019 BULLETIN DES ANNONCES LEGALES OBLIGATOIRES Avis de convocation / avis de réunion»
   Anys: 2019 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: Data de publicació de l'avis de réunion: 10/05/2019. · URL: https://www.journal-officiel.gouv.fr/telechargements/BALO/pdf/2019/0510/201905101901713.pdf · Wayback: `pendent_verificacio_externa`

17. [`L2|FR0000071946|c18`] [V] «nous avons effectué l’audit des comptes consolidés de la société ALTEN SA relatifs à l’exercice clos le 31 décembre 2021»
   Anys: 2021 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: Data el document que conté c5 com l'URD de l'exercici tancat el 31/12/2021, que inclou el 31/10/2021. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317442505_20220429.zip · Wayback: `pendent_verificacio_externa`

18. [`L2|FR0000071946|c19`] [V] «Madame Azoulay est administrateur non-exécutif et est liée à Monsieur Simon Azoulay, PDG d’ALTEN.»
   Anys: 2018-2019 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: El 24/04/2019 l'emissor anomena Simon Azoulay «PDG d'ALTEN», en present. Per a 2018 és contemporània: és posterior al 31/10/2018 i cau dins els 4 mesos després del tancament de l'exercici 2018 (31/12/2018, és a dir, fins al 30/04/2019). Acota el 31/10/2018 per darrere, juntament amb c22 i c14 per davant. Per a 2019 és dins l'exercici. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2019/04/FCECO050736_20190424.pdf · Wayback: https://web.archive.org/web/20210712115100/https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2019/04/FCECO050736_20190424.pdf (existent; cita no verificada a la captura)

19. [`L2|FR0000071946|c20`] [V] «COMMUNIQUÉ DE PRESSE Le 24/04/2019 17h45 Assemblée générale mixte d’ALTEN SA du 18 juin 2019»
   Anys: 2018-2019 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: Data del comunicat que conté c19: 24/04/2019. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2019/04/FCECO050736_20190424.pdf · Wayback: https://web.archive.org/web/20210712115100/https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2019/04/FCECO050736_20190424.pdf (existent; cita no verificada a la captura)

20. [`L2|FR0000071946|c21`] [V] «Fait le 23 septembre 2019. Simon AZOULAY Président - Directeur Général»
   Anys: 2019 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Bloc de signatura amb data, nom i càrrec dins el fragment: el 23/09/2019, dins l'exercici 2019 i 38 dies abans del 31/10/2019, Simon AZOULAY signa com a Président-Directeur Général. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2019/09/FCECO052418_20190923.pdf · Wayback: https://web.archive.org/web/20210712115233/https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2019/09/FCECO052418_20190923.pdf (existent; cita no verificada a la captura)

21. [`L2|FR0000071946|c22`] [V] «afin d’assurer un juste équilibre des pouvoirs au sein du Conseil d’administration, Monsieur Simon AZOULAY exerçant les fonctions de Président-Directeur Général, le Conseil d’administration a décidé de créer la fonction d’Administrateur référent»
   Anys: 2018 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: El 25/04/2018, dins l'exercici 2018, l'emissor diu en present que Simon AZOULAY exerceix les funcions de Président-Directeur Général. És una cita contemporània per a 2018 que no depèn de la redacció de remuneració de l'exercici anterior de c14. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2018/04/FCECO046707_20180425.pdf · Wayback: https://web.archive.org/web/20260714033538/https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2018/04/FCECO046707_20180425.pdf (existent; cita no verificada a la captura)

22. [`L2|FR0000071946|c23`] [V] «Paris, le 25 avril 2018 17 heures 45 Assemblée générale mixte d’ALTEN SA du 20 juin 2018»
   Anys: 2018 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: Data del comunicat que conté c22: 25/04/2018. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2018/04/FCECO046707_20180425.pdf · Wayback: https://web.archive.org/web/20260714033538/https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2018/04/FCECO046707_20180425.pdf (existent; cita no verificada a la captura)

### L2.11 Essilor Intl -Cie Génle Opt.SA Actions Port. (`FR0000121667`)

- isin i anys: `FR0000121667`, 2016-2017 (n=2). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Hubert Sagnières → Hubert Sagnières (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2016: marca `prova_interval`; cites del CEO `L2|FR0000121667|C1`, `L2|FR0000121667|C2a`, `L2|FR0000121667|C3`, `L2|FR0000121667|C4`.
- 2017: marca `informe_exercici`; cites del CEO `L2|FR0000121667|C1`, `L2|FR0000121667|C2a`, `L2|FR0000121667|C5`, `L2|FR0000121667|C6`, `L2|FR0000121667|C7`, `L2|FR0000121667|C8`, `L2|FR0000121667|C9`.
- Correccions de DF: `L2|FR0000121667|C2a` substitueix `L2|FR0000121667|C2`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/FR0000121667.md](../empreses/FR0000121667.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|FR0000121667|C1`] [V] «Mr. Hubert Sagnières has been Chairman and Chief Executive Officer of Essilor since January 2, 2012.»
   Anys: 2016-2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Interval: PDG d'Essilor de manera continuada des del 2/1/2012 fins a la data del document (28/09/2018); cobreix el 31/10/2016 i el 31/10/2017. · URL: https://www.essilorluxottica.com/cap/content/118376/?_iframe=true · Wayback: `pendent_verificacio_externa`

2. [`L2|FR0000121667|C3`] [V] «favoriser une accélération de la croissance en 2017 », a déclaré Hubert Sagnières, Président-Directeur Général du groupe.»
   Anys: 2016 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Document contemporani: Sagnières és Président-Directeur Général el 21/10/2016. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/CNS/2016/10/FCCNS148981_20161021.pdf · Wayback: https://web.archive.org/web/20210712200345/https://echanges.dila.gouv.fr/OPENDATA/AMF/CNS/2016/10/FCCNS148981_20161021.pdf (existent; cita no verificada a la captura)

3. [`L2|FR0000121667|C4`] [V] «At the December 6, 2016 Board of Directors' meeting, Hubert Sagnières, Chairman and Chief Executive Officer of Essilor, proposed strengthening the Company's executive management»
   Anys: 2016 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Continuïtat després del 31/10/2016: Sagnières és Chairman and CEO el 6-7/12/2016. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/CNS/2016/12/FCCNS150096_20161207.pdf · Wayback: https://web.archive.org/web/20210712195705/https://echanges.dila.gouv.fr/OPENDATA/AMF/CNS/2016/12/FCCNS150096_20161207.pdf (existent; cita no verificada a la captura)

4. [`L2|FR0000121667|C5`] [V] «Commenting on these results, Hubert Sagnières, Chairman and Chief Executive Officer of Essilor, said:»
   Anys: 2017 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Sagnières és Chairman and CEO el juliol de 2017 (abans del 31/10/2017). · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/CNS/2017/07/FCCNS156663_20170728.pdf · Wayback: https://web.archive.org/web/20210712211427/https://echanges.dila.gouv.fr/OPENDATA/AMF/CNS/2017/07/FCCNS156663_20170728.pdf (existent; cita no verificada a la captura)

5. [`L2|FR0000121667|C6`] [V] «respect of the 2017 fiscal year to Mr. Hubert SAGNIÈRES, Chairman and Chief Executive Officer»
   Anys: 2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Sagnières figura com a Chairman and CEO respecte de l'exercici 2017 i a la junta d'abril de 2018 (continuïtat després del 31/10/2017). · URL: https://www.essilorluxottica.com/cap/content/118350/?_iframe=true · Wayback: `pendent_verificacio_externa`

6. [`L2|FR0000121667|C7`] [V] «decision of Hubert Sagnières, Président-Directeur Général of the Issuer, dated 27 June 2017»
   Anys: 2017 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Sagnières és Président-Directeur Général de l'emissor el 27/06/2017. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/152/8888/01/FC152181638_20170628.pdf · Wayback: https://web.archive.org/web/20210712194748/https://echanges.dila.gouv.fr/OPENDATA/AMF/152/8888/01/FC152181638_20170628.pdf (existent; cita no verificada a la captura)

7. [`L2|FR0000121667|C2a`] [V] «Hubert SAGNIÈRES President and Chief Operating Officer until December 31, 2009, Chief Executive Officer from January 1, 2010, Chairman and Chief Executive Officer from January 2, 2012, and Executive Vice-Chairman from October 1, 2018»
   Anys: 2016-2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Interval retrospectiu amb dates explícites i el nom dins la cita. Hubert Sagnières va ser Chief Executive Officer des de l'1/1/2010, Chairman and Chief Executive Officer des del 2/1/2012 i Executive Vice-Chairman des de l'1/10/2018. L'interval de CEO cobreix el 31/10/2016 i el 31/10/2017. · URL: https://www.essilorluxottica.com/cap/content/56508/?_iframe=true · Wayback: `pendent_verificacio_externa` · substitueix `L2|FR0000121667|C2`

8. [`L2|FR0000121667|C8`] [V] «Hubert Sagnières, Chairman and Chief Executive Officer since January 2, 2012;»
   Anys: 2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: És l'informe anual de l'exercici 2017 (natural; inclou el 31/10/2017). Hubert Sagnières hi és Chairman and Chief Executive Officer des del 2/1/2012 i continuava en el càrrec a la data del document. · URL: https://www.essilorluxottica.com/cap/content/101900/?_iframe=true · Wayback: `pendent_verificacio_externa`

9. [`L2|FR0000121667|C9`] [V] «Holding Company (listed company) Chairman and Chief Executive Officer: Hubert Sagnières»
   Anys: 2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Al tancament de l'exercici 2017 (31/12/2017), el Chairman and Chief Executive Officer de la societat cotitzada (holding) és Hubert Sagnières. És posterior al hive-down de l'1/11/2017: la cotitzada no canvia de CEO, i la filial operativa SAS també té Sagnières com a CEO. · URL: https://www.essilorluxottica.com/cap/content/101900/?_iframe=true · Wayback: `pendent_verificacio_externa`

### L2.12 Associated British Foods PLC Registered (`GB0006731235`)

- isin i anys: `GB0006731235`, 2016-2025 (n=10). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **George Weston → George Weston (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A, B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2016: marca `prova_interval`; cites del CEO `L2|GB0006731235|R2015`, `L2|GB0006731235|R2016`, `L2|GB0006731235|AR2019c`, `L2|GB0006731235|AR2019b`.
- 2017: marca `prova_interval`; cites del CEO `L2|GB0006731235|R2016`, `L2|GB0006731235|R2017`, `L2|GB0006731235|AR2019c`, `L2|GB0006731235|AR2019b`.
- 2018: marca `informe_exercici`; cites del CEO `L2|GB0006731235|R2017`, `L2|GB0006731235|R2018`, `L2|GB0006731235|AR2019c`, `L2|GB0006731235|AR2019b`, `L2|GB0006731235|AR2019e`; datació `L2|GB0006731235|AR2019d`.
- 2019: marca `prova_interval`; cites del CEO `L2|GB0006731235|R2018`, `L2|GB0006731235|R2019`, `L2|GB0006731235|AR2019c`, `L2|GB0006731235|AR2019b`, `L2|GB0006731235|AR2019e`.
- 2020: marca `prova_interval`; cites del CEO `L2|GB0006731235|R2019`, `L2|GB0006731235|R2020`.
- 2021: marca `prova_interval`; cites del CEO `L2|GB0006731235|R2020`, `L2|GB0006731235|R2021`.
- 2022: marca `prova_interval`; cites del CEO `L2|GB0006731235|R2021`, `L2|GB0006731235|R2022`.
- 2023: marca `prova_interval`; cites del CEO `L2|GB0006731235|R2022`, `L2|GB0006731235|R2023`.
- 2024: marca `prova_interval`; cites del CEO `L2|GB0006731235|R2023`, `L2|GB0006731235|T2024b`, `L2|GB0006731235|P2024`, `L2|GB0006731235|I2025b`; datació `L2|GB0006731235|T2024a`, `L2|GB0006731235|P2024d`, `L2|GB0006731235|I2025a`.
- 2025: marca `prova_interval`; cites del CEO `L2|GB0006731235|I2025b`, `L2|GB0006731235|R2025b`, `L2|GB0006731235|I2026b`; datació `L2|GB0006731235|I2025a`, `L2|GB0006731235|R2025a`, `L2|GB0006731235|I2026a`.
- Correccions de DF: `L2|GB0006731235|AR2019c` substitueix `L2|GB0006731235|AR2019a`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/GB0006731235.md](../empreses/GB0006731235.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|GB0006731235|R2015`] [V] «2015 Annual Results Announcement 03 Nov 2015 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2016 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 03 Nov 2015 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2015). · URL: https://www.abfingredients.com/en/news-and-events/news/2015-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260514171725/https://www.abfingredients.com/en/news-and-events/news/2015-annual-results-announcement/ (existent; cita no verificada a la captura)

2. [`L2|GB0006731235|R2016`] [V] «2016 Annual Results Announcement 08 Nov 2016 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2016-2017 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 08 Nov 2016 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2016). · URL: https://www.abfingredients.com/en/news-and-events/news/2016-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260617013406/https://www.abfingredients.com/en/news-and-events/news/2016-annual-results-announcement/ (existent; cita no verificada a la captura)

3. [`L2|GB0006731235|R2017`] [V] «2017 Annual Results Announcement 09 Nov 2017 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2017-2018 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 09 Nov 2017 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2017). · URL: https://www.abfingredients.com/en/news-and-events/news/2017-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260719053551/https://www.abfingredients.com/en/news-and-events/news/2017-annual-results-announcement/ (existent; cita no verificada a la captura)

4. [`L2|GB0006731235|R2018`] [V] «2018 Annual Results Announcement 06 Nov 2018 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2018-2019 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 06 Nov 2018 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2018). · URL: https://www.abfingredients.com/en/news-and-events/news/2018-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260719054927/https://www.abfingredients.com/en/news-and-events/news/2018-annual-results-announcement/ (existent; cita no verificada a la captura)

5. [`L2|GB0006731235|R2019`] [V] «2019 Annual Results Announcement 05 Nov 2019 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2019-2020 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 05 Nov 2019 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2019). · URL: https://www.abfingredients.com/en/news-and-events/news/2019-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260719055141/https://www.abfingredients.com/en/news-and-events/news/2019-annual-results-announcement/ (existent; cita no verificada a la captura)

6. [`L2|GB0006731235|R2020`] [V] «2020 Annual Results Announcement 03 Nov 2020 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2020-2021 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 03 Nov 2020 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2020). · URL: https://www.abfingredients.com/en/news-and-events/news/2020-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260617000638/https://www.abfingredients.com/en/news-and-events/news/2020-annual-results-announcement/ (existent; cita no verificada a la captura)

7. [`L2|GB0006731235|R2021`] [V] «2021 Annual Results Announcement 09 Nov 2021 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2021-2022 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 09 Nov 2021 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2021). · URL: https://www.abfingredients.com/en/news-and-events/news/2021-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260719055247/https://www.abfingredients.com/en/news-and-events/news/2021-annual-results-announcement/ (existent; cita no verificada a la captura)

8. [`L2|GB0006731235|R2022`] [V] «2022 Annual Results Announcement 08 Nov 2022 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2022-2023 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 08 Nov 2022 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2022). · URL: https://www.abfingredients.com/en/news-and-events/news/2022-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260514160650/https://www.abfingredients.com/en/news-and-events/news/2022-annual-results-announcement/ (existent; cita no verificada a la captura)

9. [`L2|GB0006731235|R2023`] [V] «2023 Annual Results Announcement 07 Nov 2023 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2023-2024 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 07 Nov 2023 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2023). · URL: https://www.abfingredients.com/en/news-and-events/news/2023-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260617002913/https://www.abfingredients.com/en/news-and-events/news/2023-annual-results-announcement/ (existent; cita no verificada a la captura)

10. [`L2|GB0006731235|AR2019b`] [V] «George Weston (Chief Executive)»
   Anys: 2016-2019 · funció: `ceo` · allotjament: `grup` · nivell A · prova: L informe anual 2019 llista George Weston com a Executive director (Chief Executive). · URL: https://www.azucarera.es/wp-content/uploads/2019/11/ar2019b.pdf · Wayback: `pendent_verificacio_externa`

11. [`L2|GB0006731235|T2024a`] [V] «09/2024 Pre Close Period Trading Update 05 Sept 2024 Financial Trading Update 05 Sep 2024»
   Anys: 2024 · funció: `datacio` · allotjament: `grup` · nivell A · prova: Data del trading update: 5 de setembre de 2024. · URL: https://www.abfingredients.com/en/news-and-events/news/092024-pre-close-period-trading-update/ · Wayback: https://web.archive.org/web/20260617012935/https://www.abfingredients.com/en/news-and-events/news/092024-pre-close-period-trading-update/ (existent; cita no verificada a la captura)

12. [`L2|GB0006731235|T2024b`] [V] «George Weston, Chief Executive of Associated British Foods, said:»
   Anys: 2024 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 5/09/2024 George Weston es Chief Executive d Associated British Foods. · URL: https://www.abfingredients.com/en/news-and-events/news/092024-pre-close-period-trading-update/ · Wayback: https://web.archive.org/web/20260617012935/https://www.abfingredients.com/en/news-and-events/news/092024-pre-close-period-trading-update/ (existent; cita no verificada a la captura)

13. [`L2|GB0006731235|P2024`] [V] «George Weston, CEO of Associated British Foods, told Reuters in an interview after the group reported annual results.»
   Anys: 2024 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: El 5/11/2024 (resultats anuals) George Weston es CEO d Associated British Foods. · URL: https://www.rte.ie/news/business/2024/1105/1479133-associated-british-foods-results · Wayback: https://web.archive.org/web/20241107001332/https://www.rte.ie/news/business/2024/1105/1479133-associated-british-foods-results/ (existent; cita no verificada a la captura)

14. [`L2|GB0006731235|P2024d`] [V] «Updated / Tuesday, 5 Nov 2024»
   Anys: 2024 · funció: `datacio` · allotjament: `mitja` · nivell B · prova: Data de la noticia: 5 de novembre de 2024. · URL: https://www.rte.ie/news/business/2024/1105/1479133-associated-british-foods-results · Wayback: https://web.archive.org/web/20241107001332/https://www.rte.ie/news/business/2024/1105/1479133-associated-british-foods-results/ (existent; cita no verificada a la captura)

15. [`L2|GB0006731235|I2025a`] [V] «2025 Interim Results Announcement 29 Apr 2025 Financial Associated British Foods plc results for the 24 weeks»
   Anys: 2024-2025 · funció: `datacio` · allotjament: `grup` · nivell A · prova: Data del comunicat: 29 d abril de 2025. · URL: https://www.abfingredients.com/en/news-and-events/news/2025-interim-results-announcement/ · Wayback: https://web.archive.org/web/20260719070107/https://www.abfingredients.com/en/news-and-events/news/2025-interim-results-announcement/ (existent; cita no verificada a la captura)

16. [`L2|GB0006731235|I2025b`] [V] «George Weston, Chief Executive of Associated British Foods, said:»
   Anys: 2024-2025 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 29/04/2025 George Weston es Chief Executive. · URL: https://www.abfingredients.com/en/news-and-events/news/2025-interim-results-announcement/ · Wayback: https://web.archive.org/web/20260719070107/https://www.abfingredients.com/en/news-and-events/news/2025-interim-results-announcement/ (existent; cita no verificada a la captura)

17. [`L2|GB0006731235|R2025a`] [V] «2025 Annual Results Announcement 05 Nov 2025 Financial Associated British Foods plc results for the 52 weeks ended 13 September 2025»
   Anys: 2025 · funció: `datacio` · allotjament: `grup` · nivell A · prova: Data del comunicat: 5 de novembre de 2025. · URL: https://www.abfingredients.com/en/news-and-events/news/2025-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260514163236/https://www.abfingredients.com/en/news-and-events/news/2025-annual-results-announcement/ (existent; cita no verificada a la captura)

18. [`L2|GB0006731235|R2025b`] [V] «George Weston, Chief Executive of Associated British Foods, said:»
   Anys: 2025 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 5/11/2025 George Weston es Chief Executive. · URL: https://www.abfingredients.com/en/news-and-events/news/2025-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260514163236/https://www.abfingredients.com/en/news-and-events/news/2025-annual-results-announcement/ (existent; cita no verificada a la captura)

19. [`L2|GB0006731235|I2026a`] [V] «2026 Interim Results Announcement 21 Apr 2026 Financial Associated British Foods plc results for the 24 weeks ended 28 February 2026»
   Anys: 2025 · funció: `datacio` · allotjament: `grup` · nivell A · prova: Data del comunicat: 21 d abril de 2026. · URL: https://www.abfingredients.com/en/news-and-events/news/2026-interim-results-announcement/ · Wayback: https://web.archive.org/web/20260809020926/https://www.abfingredients.com/en/news-and-events/news/2026-interim-results-announcement/ (existent; cita no verificada a la captura)

20. [`L2|GB0006731235|I2026b`] [V] «George Weston, Chief Executive of Associated British Foods, said:»
   Anys: 2025 · funció: `ceo` · allotjament: `grup` · nivell A · prova: El 21/04/2026 George Weston continua sent Chief Executive (continuitat posterior al 31/10/2025). · URL: https://www.abfingredients.com/en/news-and-events/news/2026-interim-results-announcement/ · Wayback: https://web.archive.org/web/20260809020926/https://www.abfingredients.com/en/news-and-events/news/2026-interim-results-announcement/ (existent; cita no verificada a la captura)

21. [`L2|GB0006731235|AR2019c`] [V] «George Weston Chief Executive George was appointed to the board in 1999 and took up his current appointment as Chief Executive in April 2005.»
   Anys: 2016-2019 · funció: `ceo` · allotjament: `grup` · nivell A · prova: George Weston és Chief Executive des d'abril de 2005 i encara hi és a la data de l'informe (novembre de 2019). L'interval cobreix el 31/10 dels anys 2016 a 2019. · URL: https://www.azucarera.es/wp-content/uploads/2019/11/ar2019b.pdf · Wayback: `pendent_verificacio_externa` · substitueix `L2|GB0006731235|AR2019a`

22. [`L2|GB0006731235|AR2019d`] [V] «The directors of Associated British Foods plc present their report for the 52 weeks ended 14 September 2019»
   Anys: 2018 · funció: `datacio` · allotjament: `grup` · nivell A · prova: L'informe anual 2019 cobreix l'exercici de 52 setmanes tancat el 14/09/2019. El mateix informe dona el tancament anterior: «Balance as at 15 September 2018». Per tant, és l'informe de l'exercici que inclou el 31/10/2018. · URL: https://www.azucarera.es/wp-content/uploads/2019/11/ar2019b.pdf · Wayback: `pendent_verificacio_externa`

23. [`L2|GB0006731235|AR2019e`] [V] «On behalf of the board Michael McLintock Chairman George Weston Chief Executive John Bason Finance Director 5 November 2019»
   Anys: 2018-2019 · funció: `ceo` · allotjament: `grup` · nivell A · prova: George Weston signa com a Chief Executive, el 05/11/2019, la declaració de responsabilitat dels administradors de l'informe anual de l'exercici tancat el 14/09/2019. Nom i càrrec són dins el fragment. · URL: https://www.azucarera.es/wp-content/uploads/2019/11/ar2019b.pdf · Wayback: `pendent_verificacio_externa`

### L2.13 Tesco PLC Registered Shares LS -,05 (`GB0008847096`)

- isin i anys: `GB0008847096`, 2016-2018 (n=3). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Dave Lewis → Dave Lewis (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2016: marca `prova_interval`; cites del CEO `L2|GB0008847096|c1`, `L2|GB0008847096|c2`; context `L2|GB0008847096|c9n`.
- 2017: marca `prova_interval`; cites del CEO `L2|GB0008847096|c3`, `L2|GB0008847096|c4`; context `L2|GB0008847096|c9n`.
- 2018: marca `prova_interval`; cites del CEO `L2|GB0008847096|c5`, `L2|GB0008847096|c6`, `L2|GB0008847096|c8`; context `L2|GB0008847096|c9n`.
- Correccions de DF: `L2|GB0008847096|c9n` substitueix `L2|GB0008847096|c9`; `L2|GB0008847096|c7` es treu de 2018.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/GB0008847096.md](../empreses/GB0008847096.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|GB0008847096|c1`] [V] «Although chief executive Dave Lewis said prices at the retailer were down six per cent on a year ago»
   Anys: 2016 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Dave Lewis era chief executive de Tesco el 5/10/2016 (resultats semestrals). · URL: https://www.cityam.com/tesco-posts-increase-uk-like-like-sales-but-profit-drops-28/ · Wayback: `pendent_verificacio_externa`

2. [`L2|GB0008847096|c2`] [V] «Tesco chief executive Dave Lewis has warned global suppliers not to artificially inflate their prices because of the fall in the pound.»
   Anys: 2016 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Dave Lewis continuava sent chief executive de Tesco el 18/11/2016, després del 31/10/2016. · URL: https://www.bbc.co.uk/news/business-38023732 · Wayback: https://web.archive.org/web/20250816105846/https://www.bbc.co.uk/news/business-38023732 (existent; cita no verificada a la captura)

3. [`L2|GB0008847096|c3`] [V] «Tesco chief executive Dave Lewis has said the supermarket's turnaround is "very firmly on track" as sales rose for the seventh quarter in a row.»
   Anys: 2017 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Dave Lewis era chief executive de Tesco el 4/10/2017. · URL: https://www.bbc.co.uk/news/business-41495322 · Wayback: https://web.archive.org/web/20260419062114/https://www.bbc.co.uk/news/business-41495322 (existent; cita no verificada a la captura)

4. [`L2|GB0008847096|c4`] [V] «Chief executive Dave Lewis said: "We have continued to outperform the market throughout this period»
   Anys: 2017 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Dave Lewis continuava sent chief executive de Tesco l'11/1/2018, després del 31/10/2017. · URL: https://www.bbc.co.uk/news/business-42646021 · Wayback: https://web.archive.org/web/20260419032936/https://www.bbc.co.uk/news/business-42646021 (existent; cita no verificada a la captura)

5. [`L2|GB0008847096|c5`] [V] «Chief executive Dave Lewis has been rebuilding Tesco since 2014, when an accounting scandal capped a dramatic downturn in trading.»
   Anys: 2018 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Dave Lewis era chief executive de Tesco el 3/10/2018 i ho era des del 2014. · URL: https://www.rte.ie/news/business/2018/1003/1000600-tesco-half-yearly-results · Wayback: `pendent_verificacio_externa`

6. [`L2|GB0008847096|c6`] [V] «Chief executive Dave Lewis said the group was on track to meet the "vast majority" of the turnaround goals he set when he was appointed four years ago after an accounting scandal.»
   Anys: 2018 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Dave Lewis continuava sent chief executive de Tesco el 10/4/2019, després del 31/10/2018. · URL: https://www.bbc.co.uk/news/business-47877524 · Wayback: https://web.archive.org/web/20260418221159/https://www.bbc.co.uk/news/business-47877524 (existent; cita no verificada a la captura)

7. [`L2|GB0008847096|c8`] [V] «Tesco's chief executive Dave Lewis is to leave next year after leading a turnaround plan for Britain's biggest supermarket chain.»
   Anys: 2018 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: El 2/10/2019 Dave Lewis encara era chief executive i la sortida era prevista per al 2020; cap canvi de CEO entre 2016 i 2018. · URL: https://www.bbc.co.uk/news/business-49903696 · Wayback: https://web.archive.org/web/20261109130627/https://www.bbc.co.uk/news/business-49903696 (existent; cita no verificada a la captura)

8. [`L2|GB0008847096|c9n`] [V] «LEWIS, David John Correspondence address Tesco House, Shire Park, Kestrel Way, Welwyn Garden City, United Kingdom, AL7 1GA Role Resigned Director Date of birth March 1965 Appointed on 1 September 2014 Resigned on 30 September 2020»
   Anys: 2016-2018 · funció: `context` · allotjament: `regulador` · nivell A · prova: L'officer LEWIS, David John (Dave Lewis) figura com a conseller de Tesco PLC des de l'1/9/2014 fins al 30/9/2020. El registre diu «Director», no CEO ni chief executive: acota el mandat al consell, però no prova el càrrec de CEO. És una cita de context. · URL: https://find-and-update.company-information.service.gov.uk/company/00445790/officers?page=2 · Wayback: https://web.archive.org/web/20240506204257/https://find-and-update.company-information.service.gov.uk/company/00445790/officers?page=2 (existent; cita no verificada a la captura) · substitueix `L2|GB0008847096|c9`

### L2.14 Victrex PLC Registered Shares LS -,01 (`GB0009292243`)

- isin i anys: `GB0009292243`, 2018-2022 (n=5). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Jakob Sigurdsson → Jakob Sigurdsson (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2018: marca `prova_interval+prova_interval_retrospectiva`; cites del CEO `L2|GB0009292243|C1`, `L2|GB0009292243|C6`, `L2|GB0009292243|C7`; datació `L2|GB0009292243|C3`, `L2|GB0009292243|C5`; context `L2|GB0009292243|C2`, `L2|GB0009292243|C4`, `L2|GB0009292243|C9n`.
- 2019: marca `prova_interval+prova_interval_retrospectiva`; cites del CEO `L2|GB0009292243|C1`, `L2|GB0009292243|C6`, `L2|GB0009292243|C7`; datació `L2|GB0009292243|C3`, `L2|GB0009292243|C5`; context `L2|GB0009292243|C2`, `L2|GB0009292243|C4`, `L2|GB0009292243|C9n`.
- 2020: marca `prova_interval+prova_interval_retrospectiva`; cites del CEO `L2|GB0009292243|C1`, `L2|GB0009292243|C6`, `L2|GB0009292243|C7`; datació `L2|GB0009292243|C3`, `L2|GB0009292243|C5`; context `L2|GB0009292243|C2`, `L2|GB0009292243|C4`, `L2|GB0009292243|C9n`.
- 2021: marca `prova_interval+prova_interval_retrospectiva`; cites del CEO `L2|GB0009292243|C1`, `L2|GB0009292243|C6`, `L2|GB0009292243|C7`; datació `L2|GB0009292243|C3`, `L2|GB0009292243|C5`; context `L2|GB0009292243|C2`, `L2|GB0009292243|C4`, `L2|GB0009292243|C9n`.
- 2022: marca `prova_interval+prova_interval_retrospectiva`; cites del CEO `L2|GB0009292243|C1`, `L2|GB0009292243|C6`, `L2|GB0009292243|C7`; datació `L2|GB0009292243|C3`, `L2|GB0009292243|C5`; context `L2|GB0009292243|C2`, `L2|GB0009292243|C4`, `L2|GB0009292243|C9n`.
- Correccions de DF: `L2|GB0009292243|C9n` substitueix `L2|GB0009292243|C9`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/GB0009292243.md](../empreses/GB0009292243.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|GB0009292243|C1`] [V] «Jakob Sigurdsson was appointed as CEO on 1 October 2017. His first tranche of LTIPs was eligible to vest in 2020.»
   Anys: 2018-2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Data efectiva d inici del mandat de CEO: 1/10/2017. · URL: https://www.victrexplc.com/media/glmpw22b/victrex-plc-annual-report-2024.pdf · Wayback: `pendent_verificacio_externa`

2. [`L2|GB0009292243|C2`] [V] «The total remuneration figures for the Chief Executive Officer during each of the last 10 financial years are shown in the table below.»
   Anys: 2018-2022 · funció: `context` · allotjament: `emissor` · nivell A · prova: Encapçalament de la taula que identifica el CEO de cada un dels 10 darrers exercicis. · URL: https://www.victrexplc.com/media/glmpw22b/victrex-plc-annual-report-2024.pdf · Wayback: `pendent_verificacio_externa`

3. [`L2|GB0009292243|C3`] [V] «30 September 2024 2023 2022 2021 2020 2019 2018 2017 2016 2015»
   Anys: 2018-2022 · funció: `datacio` · allotjament: `emissor` · nivell A · prova: Columnes de la taula: exercicis tancats el 30/09 de 2024 a 2015, en aquest ordre. · URL: https://www.victrexplc.com/media/glmpw22b/victrex-plc-annual-report-2024.pdf · Wayback: `pendent_verificacio_externa`

4. [`L2|GB0009292243|C4`] [V] «Sigurdsson Sigurdsson Sigurdsson Sigurdsson Sigurdsson Sigurdsson Sigurdsson Hummel Hummel Hummel»
   Anys: 2018-2022 · funció: `context` · allotjament: `emissor` · nivell A · prova: A la mateixa taula, el CEO dels set exercicis 2024-2018 és (J O) Sigurdsson i el dels tres 2017-2015 és (D R) Hummel; un sol nom per exercici. · URL: https://www.victrexplc.com/media/glmpw22b/victrex-plc-annual-report-2024.pdf · Wayback: `pendent_verificacio_externa`

5. [`L2|GB0009292243|C5`] [V] «Leadership – our governance framework as at 30 September 2024»
   Anys: 2018-2022 · funció: `datacio` · allotjament: `emissor` · nivell A · prova: Data de referència del quadre de govern (30/09/2024) on figura C6. · URL: https://www.victrexplc.com/media/glmpw22b/victrex-plc-annual-report-2024.pdf · Wayback: `pendent_verificacio_externa`

6. [`L2|GB0009292243|C6`] [V] «Chief Executive Officer: Jakob Sigurdsson»
   Anys: 2018-2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Sigurdsson continua com a CEO el 30/09/2024 (posterior a tots els 31/10 de 2018-2022). · URL: https://www.victrexplc.com/media/glmpw22b/victrex-plc-annual-report-2024.pdf · Wayback: `pendent_verificacio_externa`

7. [`L2|GB0009292243|C7`] [V] «Jakob Sigurdsson will step down as CEO and be replaced by Dr James Routh on 1 January 2026.»
   Anys: 2018-2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Fi del mandat de CEO: substituït l 1/1/2026; per tant CEO sense interrupció documentada fins llavors. · URL: https://www.victrexplc.com/media/2brmqozs/victrex-plc-annual-report-2025.pdf · Wayback: `pendent_verificacio_externa`

8. [`L2|GB0009292243|C9n`] [V] «SIGURDSSON, Jakob Oskar Correspondence address Victrex Technology Centre, Hillhouse International, Thornton Cleveleys, Lancashire, FY5 4QD Role Resigned Director Date of birth March 1964 Appointed on 1 October 2017 Resigned on 6 February 2026»
   Anys: 2018-2022 · funció: `context` · allotjament: `regulador` · nivell A · prova: El registre diu «Director» («Role Resigned Director»), no CEO. Només prova que Jakob Oskar Sigurdsson va ser administrador de Victrex plc de l'1/10/2017 al 6/2/2026. És suport de continuïtat i no prova el càrrec de CEO. · URL: https://find-and-update.company-information.service.gov.uk/company/02793780/officers?page=2 · Wayback: `pendent_verificacio_externa` · substitueix `L2|GB0009292243|C9`

### L2.15 Dechra Pharmaceuticals PLC Registered (`GB0009633180`)

- isin i anys: `GB0009633180`, 2018-2023 (n=6). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Ian Page → Ian Page (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2018: marca `prova_interval+prova_interval_retrospectiva`; cites del CEO `L2|GB0009633180|C1_s`, `L2|GB0009633180|C2`; context `L2|GB0009633180|C8`, `L2|GB0009633180|C9`.
- 2019: marca `prova_interval+prova_interval_retrospectiva`; cites del CEO `L2|GB0009633180|C1_s`, `L2|GB0009633180|C2`; context `L2|GB0009633180|C8`, `L2|GB0009633180|C9`.
- 2020: marca `informe_exercici`; cites del CEO `L2|GB0009633180|C3`, `L2|GB0009633180|C2`, `L2|GB0009633180|C1_s`; context `L2|GB0009633180|C8`.
- 2021: marca `informe_exercici`; cites del CEO `L2|GB0009633180|C4`, `L2|GB0009633180|C1_s`; context `L2|GB0009633180|C8`.
- 2022: marca `prova_interval`; cites del CEO `L2|GB0009633180|C4`, `L2|GB0009633180|C5`, `L2|GB0009633180|C1_s`; context `L2|GB0009633180|C8`.
- 2023: marca `prova_interval`; cites del CEO `L2|GB0009633180|C11`, `L2|GB0009633180|C6`, `L2|GB0009633180|C7`, `L2|GB0009633180|C1_s`; context `L2|GB0009633180|C10`, `L2|GB0009633180|C8`.
- Correccions de DF: `L2|GB0009633180|C1_s` substitueix `L2|GB0009633180|C1`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/GB0009633180.md](../empreses/GB0009633180.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|GB0009633180|C2`] [V] «Over this period, Ian Page, our Chief Executive Officer, has had one base salary increase of 4% in the 2020 financial year. Ian Page’s salary had not previously been increased since 2016.»
   Anys: 2018-2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Ian Page és el CEO a l'exercici 2021 i el seu salari de CEO es remunta com a mínim al 2016 (continuïtat 2016-2021). · URL: https://www.dechra.com/Files/Files/Dechra_s-annual-report-and-accounts-for-the-year-ended-30-June-2021.pdf · Wayback: `pendent_verificacio_externa`

2. [`L2|GB0009633180|C3`] [V] «Ian Page Chief Executive Officer 6 September 2021»
   Anys: 2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Ian Page signa com a CEO l'informe de l'exercici que inclou el 31/10/2020. · URL: https://www.dechra.com/Files/Files/Dechra_s-annual-report-and-accounts-for-the-year-ended-30-June-2021.pdf · Wayback: `pendent_verificacio_externa`

3. [`L2|GB0009633180|C4`] [V] «Signed by order of the Board. Ian Page Chief Executive Officer Paul Sandland Chief Financial Officer 5 September 2022»
   Anys: 2021-2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Ian Page signa com a CEO l'informe de l'exercici que inclou el 31/10/2021. · URL: https://www.dechra.com/Files/Files/Dechra_s-annual-report-and-accounts-for-the-year-ended-30-June-2022.pdf · Wayback: `pendent_verificacio_externa`

4. [`L2|GB0009633180|C5`] [V] «Ian Page, Chief Executive Officer Paul Sandland, Chief Financial Officer»
   Anys: 2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Ian Page és el CEO en l'informe del semestre 1/7/2022-31/12/2022, que inclou el 31/10/2022. · URL: https://www.dechra.com/Admin/Public/DWSDownload.aspx?File=%2fFiles%2fFiles%2fDechra_s-half-yearly-financial-report-for-the-period-ended-31-December-2022.pdf · Wayback: `pendent_verificacio_externa`

5. [`L2|GB0009633180|C6`] [V] «Ian Page, Chief Executive Officer Paul Sandland, Chief Financial Officer»
   Anys: 2023 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Ian Page segueix com a CEO el 30/11/2023 (després del 31/10/2023). · URL: https://www.dechra.com/Files/Files/Diana-Final-RNS-Update-on-Conditions-29-11-2023-124231702-v3-002.pdf · Wayback: `pendent_verificacio_externa`

6. [`L2|GB0009633180|C7`] [V] «Ian Page, Chief Executive Officer Paul Sandland, Chief Financial Officer»
   Anys: 2023 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Ian Page segueix com a CEO el 12/01/2024. · URL: https://www.dechra.com/Files/Files/2024-01-12-Court-Sanction-Announcement.pdf · Wayback: `pendent_verificacio_externa`

7. [`L2|GB0009633180|C8`] [V] «today announces the appointment of Jesper Nordengaard as its CEO and retirement of Ian Page effective June 10, 2024»
   Anys: 2018-2023 · funció: `context` · allotjament: `emissor` · nivell A · prova: Fi del mandat: Ian Page es retira i Jesper Nordengaard és CEO amb efecte 10/06/2024. · URL: https://www.dechra.com/jesper-nordengaard · Wayback: https://web.archive.org/web/20241114185348/https://www.dechra.com/jesper-nordengaard (existent; cita no verificada a la captura)

8. [`L2|GB0009633180|C9`] [V] «It has been a privilege to lead the business as CEO over the last 23 years.»
   Anys: 2018-2019 · funció: `context` · allotjament: `emissor` · nivell A · prova: Mandat continu d'Ian Page com a CEO durant els 23 anys anteriors a maig de 2024. · URL: https://www.dechra.com/jesper-nordengaard · Wayback: https://web.archive.org/web/20241114185348/https://www.dechra.com/jesper-nordengaard (existent; cita no verificada a la captura)

9. [`L2|GB0009633180|C10`] [V] «Since the Initial Public Offering in 2000 and my appointment as chief executive officer in 2001, being a listed company has served Dechra well»
   Anys: 2023 · funció: `context` · allotjament: `mitja` · nivell B · prova: Ian Page, CEO a l'octubre de 2023, nomenat CEO el 2001. · URL: https://northernfinancialreview.com/2023/10/12/dechra-revenue-rises-to-761m-before-it-goes-private · Wayback: https://web.archive.org/web/20260411155253/https://northernfinancialreview.com/2023/10/12/dechra-revenue-rises-to-761m-before-it-goes-private/ (existent; cita no verificada a la captura)

10. [`L2|GB0009633180|C1_s`] [V] «Ian David Page’s service contract, dated 1 September 2008, as amended from time to time, states that his continuous employment commenced on 1 May 1989, and his appointment as Chief Executive Officer commenced on 5 November 2001 and will continue until terminated by either Ian David Page giving not less than six months written notice to Dechra or by Dechra giving not less than twelve months written notice to Ian David Page.»
   Anys: 2018-2023 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: El nomenament d'Ian David Page com a Chief Executive Officer va començar el 5/11/2001 i continua fins que s'hi posi fi amb preavís. És un sol nomenament continu, vigent a la data del document (26/06/2023). · URL: https://www.dechra.com/Files/Files/Scheme-document.pdf · Wayback: `pendent_verificacio_externa` · substitueix `L2|GB0009633180|C1`

11. [`L2|GB0009633180|C11`] [V] «Ian Page, Chief Executive Officer Paul Sandland, Chief Financial Officer»
   Anys: 2023 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Ian Page és el CEO de Dechra el 20/07/2023. És un document contemporani de l'exercici 1/7/2023-30/6/2024, anterior al 31/10/2023. · URL: https://www.dechra.com/Files/Files/2023-07-20-Results-of-Court-Meeting-and-General-Meeting.pdf · Wayback: `pendent_verificacio_externa`

### L2.16 Paysafe Group PLC Registered Shares LS (`GB0034264548`)

- isin i anys: `GB0034264548`, 2016-2017 (n=2). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Joel Leonoff → Joel Leonoff (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2016: marca `prova_interval`; cites del CEO `L2|GB0034264548|c4`, `L2|GB0034264548|c5`, `L2|GB0034264548|c1`; datació `L2|GB0034264548|c3`, `L2|GB0034264548|c6`; context `L2|GB0034264548|c2`.
- 2017: marca `prova_interval`; cites del CEO `L2|GB0034264548|c7`, `L2|GB0034264548|c9`, `L2|GB0034264548|c1`; datació `L2|GB0034264548|c8`, `L2|GB0034264548|c10`; context `L2|GB0034264548|c2`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/GB0034264548.md](../empreses/GB0034264548.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|GB0034264548|c1`] [V] «Leonoff founded Paysafe, originally Optimal Payments, in 1997 and has held the position of President and CEO since 2008.»
   Anys: 2016-2017 · funció: `ceo` · allotjament: `successor` · nivell A · prova: Interval: Leonoff President i CEO de manera continuada des de 2008 fins al comunicat de 30/05/2019; cobreix 31/10/2016 i 31/10/2017. · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-appoints-philip-mchugh-as-ceo/ · Wayback: https://web.archive.org/web/20260520172624/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-appoints-philip-mchugh-as-ceo/ (existent; cita no verificada a la captura)

2. [`L2|GB0034264548|c2`] [V] «today announced the appointment of Philip McHugh as its CEO, effective June 24, 2019. McHugh replaces Joel Leonoff»
   Anys: 2016-2017 · funció: `context` · allotjament: `successor` · nivell A · prova: Fi del mandat: el successor substitueix Leonoff amb efecte 24/06/2019, posterior al 31/10/2017. · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-appoints-philip-mchugh-as-ceo/ · Wayback: https://web.archive.org/web/20260520172624/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-appoints-philip-mchugh-as-ceo/ (existent; cita no verificada a la captura)

3. [`L2|GB0034264548|c3`] [V] «Paysafe Group plc Trading Update Nov 08, 2016»
   Anys: 2016 · funció: `datacio` · allotjament: `successor` · nivell A · prova: Data del document: 8 de novembre de 2016. · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-plc-trading-update/ · Wayback: https://web.archive.org/web/20260607200911/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-plc-trading-update/ (existent; cita no verificada a la captura)

4. [`L2|GB0034264548|c4`] [V] «Paysafe President and Chief Executive Officer Joel Leonoff said: “I am delighted to report that we are on track to achieve the upgraded revenue and adjusted EBITDA projections for the current financial year»
   Anys: 2016 · funció: `ceo` · allotjament: `successor` · nivell A · prova: Leonoff és President i CEO el 08/11/2016 (vuit dies després del 31/10/2016). · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-plc-trading-update/ · Wayback: https://web.archive.org/web/20260607200911/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-plc-trading-update/ (existent; cita no verificada a la captura)

5. [`L2|GB0034264548|c5`] [V] «Commenting on the results, Paysafe President and Chief Executive Officer Joel Leonoff said:»
   Anys: 2016 · funció: `ceo` · allotjament: `successor` · nivell A · prova: Leonoff és President i CEO el 10/08/2016 (abans del 31/10/2016). · URL: https://www.paysafe.com/en/paysafegroup/news/detail/unaudited-interim-results-for-the-6-months-ended-30-june-2016/ · Wayback: https://web.archive.org/web/20260615180315/https://www.paysafe.com/en/paysafegroup/news/detail/unaudited-interim-results-for-the-6-months-ended-30-june-2016/ (existent; cita no verificada a la captura)

6. [`L2|GB0034264548|c6`] [V] «LONDON (10 August 2016) – Paysafe Group plc»
   Anys: 2016 · funció: `datacio` · allotjament: `successor` · nivell A · prova: Data del document c5. · URL: https://www.paysafe.com/en/paysafegroup/news/detail/unaudited-interim-results-for-the-6-months-ended-30-june-2016/ · Wayback: https://web.archive.org/web/20260615180315/https://www.paysafe.com/en/paysafegroup/news/detail/unaudited-interim-results-for-the-6-months-ended-30-june-2016/ (existent; cita no verificada a la captura)

7. [`L2|GB0034264548|c7`] [V] «Paysafe President and Chief Executive Officer Joel Leonoff said Brian’s leadership had been an inspiration»
   Anys: 2017 · funció: `ceo` · allotjament: `successor` · nivell A · prova: Leonoff és President i CEO el 17/05/2017 (abans del 31/10/2017). · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-s-brian-mcarthur-muscroft-named-inspirational-finance-director-of-the-year-at-2017-fds-excellence-awards/ · Wayback: https://web.archive.org/web/20260419210133/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-s-brian-mcarthur-muscroft-named-inspirational-finance-director-of-the-year-at-2017-fds-excellence-awards/ (existent; cita no verificada a la captura)

8. [`L2|GB0034264548|c8`] [V] «LONDON, 17 May 2017 – Brian McArthur-Muscroft, Chief Financial Officer at leading global payments provider Paysafe»
   Anys: 2017 · funció: `datacio` · allotjament: `successor` · nivell A · prova: Data del document c7. · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-s-brian-mcarthur-muscroft-named-inspirational-finance-director-of-the-year-at-2017-fds-excellence-awards/ · Wayback: https://web.archive.org/web/20260419210133/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-s-brian-mcarthur-muscroft-named-inspirational-finance-director-of-the-year-at-2017-fds-excellence-awards/ (existent; cita no verificada a la captura)

9. [`L2|GB0034264548|c9`] [V] «President and Chief Executive Officer at Paysafe, Joel Leonoff, commented:»
   Anys: 2017 · funció: `ceo` · allotjament: `successor` · nivell A · prova: Leonoff és President i CEO el 23/01/2018 (després del 31/10/2017). · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-wins-record-number-of-awards-in-2017/ · Wayback: https://web.archive.org/web/20260212063140/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-wins-record-number-of-awards-in-2017/ (existent; cita no verificada a la captura)

10. [`L2|GB0034264548|c10`] [V] «Paysafe wins record number of awards in 2017 Jan 23, 2018»
   Anys: 2017 · funció: `datacio` · allotjament: `successor` · nivell A · prova: Data del document c9. · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-wins-record-number-of-awards-in-2017/ · Wayback: https://web.archive.org/web/20260212063140/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-wins-record-number-of-awards-in-2017/ (existent; cita no verificada a la captura)

### L2.17 Investec PLC Registered Shares LS -,00022) (`GB00B17BBQ50`)

- isin i anys: `GB00B17BBQ50`, 2016-2017 (n=2). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Stephen Koseff → Stephen Koseff (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2016: marca `informe_exercici`; cites del CEO `L2|GB00B17BBQ50|C6`, `L2|GB00B17BBQ50|C1`, `L2|GB00B17BBQ50|C2`, `L2|GB00B17BBQ50|C5`.
- 2017: marca `informe_exercici`; cites del CEO `L2|GB00B17BBQ50|C3`, `L2|GB00B17BBQ50|C4`, `L2|GB00B17BBQ50|C5`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/GB00B17BBQ50.md](../empreses/GB00B17BBQ50.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|GB00B17BBQ50|C1`] [V] «The payment and deferral profile of the remuneration awarded to S Koseff (CEO) and B Kantor (MD) during the 2017 financial year»
   Anys: 2016 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Koseff era CEO durant l'exercici 2017 (abril 2016-març 2017), que inclou el 31/10/2016 · URL: https://www.investec.com/content/dam/investor-relations/investor-centre/equity/investec-group-2017/Annual-Report.pdf · Wayback: `pendent_verificacio_externa`

2. [`L2|GB00B17BBQ50|C2`] [V] «Stephen Koseff, group chief executive officer»
   Anys: 2016 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Fitxa de conseller a l'informe de l'exercici tancat el 31/3/2017: Koseff és group CEO · URL: https://www.investec.com/content/dam/investor-relations/investor-centre/equity/investec-group-2017/Annual-Report.pdf · Wayback: `pendent_verificacio_externa`

3. [`L2|GB00B17BBQ50|C3`] [V] «The payment and deferral profile of the remuneration awarded to S Koseff (CEO) and B Kantor (MD) during the 2018 financial year»
   Anys: 2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Koseff era CEO durant l'exercici 2018 (abril 2017-març 2018), que inclou el 31/10/2017 · URL: https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2018/FINAL-Investec-DLC-Vol%201-15-June-2018.pdf · Wayback: https://web.archive.org/web/20251006115950/https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2018/FINAL-Investec-DLC-Vol%201-15-June-2018.pdf (existent; cita no verificada a la captura)

4. [`L2|GB00B17BBQ50|C4`] [V] «In terms of the group’s succession announcement made on 6 February 2018, Stephen Koseff (current CEO) and Bernard Kantor (current MD) will step down from these roles on 1 October 2018.»
   Anys: 2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Koseff encara és CEO al juny de 2018 i deixarà el càrrec l'1/10/2018 · URL: https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2018/FINAL-Investec-DLC-Vol%201-15-June-2018.pdf · Wayback: https://web.archive.org/web/20251006115950/https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2018/FINAL-Investec-DLC-Vol%201-15-June-2018.pdf (existent; cita no verificada a la captura)

5. [`L2|GB00B17BBQ50|C5`] [V] «S Koseff stepped down as group CEO on 1 October 2018.»
   Anys: 2016-2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Data efectiva de fi del mandat de Koseff com a group CEO: 1/10/2018 (posterior al 31/10/2017) · URL: https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2019/investec-dlc-vol-1-annual-report-2019.pdf · Wayback: https://web.archive.org/web/20240715051352/https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2019/investec-dlc-vol-1-annual-report-2019.pdf (existent; cita no verificada a la captura)

6. [`L2|GB00B17BBQ50|C6`] [V] «Approved and authorised for issue by the board of directors on 9 June 2017 and signed on its behalf by: Stephen Koseff Chief executive officer 9 June 2017»
   Anys: 2016 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Stephen Koseff signa com a «Chief executive officer» el balanç d'Investec plc de l'exercici tancat el 31/3/2017, que inclou el 31/10/2016. Ho fa a l'informe anual propi de l'emissor (ISIN GB00B17BBQ50), que no documenta cap canvi de CEO durant l'exercici. · URL: https://www.investec.com/content/dam/investor-relations/investor-centre/debt/investec-plc-2017/Annual-Report.pdf · Wayback: https://web.archive.org/web/20251227135926/https://www.investec.com/content/dam/investor-relations/investor-centre/debt/investec-plc-2017/Annual-Report.pdf (existent; cita no verificada a la captura)

### L2.18 BBA Aviation PLC Registered Shares LS (`GB00B1FP8915`)

- isin i anys: `GB00B1FP8915`, 2017 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Wayne Edmunds → Wayne Edmunds (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R2 (CEO interí). Nivell de les cites del CEO: B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2017: marca `prova_interval`; cites del CEO `L2|GB00B1FP8915|C1`, `L2|GB00B1FP8915|C2`, `L2|GB00B1FP8915|C4`, `L2|GB00B1FP8915|C6`; context `L2|GB00B1FP8915|C3`, `L2|GB00B1FP8915|C5`, `L2|GB00B1FP8915|C7`, `L2|GB00B1FP8915|C8n`, `L2|GB00B1FP8915|C9n`, `L2|GB00B1FP8915|C10n`.
- Correccions de DF: `L2|GB00B1FP8915|C8n` substitueix `L2|GB00B1FP8915|C8`; `L2|GB00B1FP8915|C9n` substitueix `L2|GB00B1FP8915|C9`; `L2|GB00B1FP8915|C10n` substitueix `L2|GB00B1FP8915|C10`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/GB00B1FP8915.md](../empreses/GB00B1FP8915.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|GB00B1FP8915|C1`] [V] «As announced on 5 June 2017, Wayne Edmunds was appointed interim CEO at BBA Aviation.»
   Anys: 2017 · funció: `ceo` · allotjament: `tercer` · nivell B · prova: Nomenament de Wayne Edmunds com a CEO interí de BBA Aviation, anunciat el 5/6/2017 · URL: https://www.dialight.com/wp-content/uploads/2022/07/21617_dialight_ar17_222_final.pdf · Wayback: https://web.archive.org/web/20230703010445/https://www.dialight.com/wp-content/uploads/2022/07/21617_dialight_ar17_222_final.pdf (existent; cita no verificada a la captura)

2. [`L2|GB00B1FP8915|C2`] [V] «Wayne Edmunds will be stepping down as interim CEO of BBA Aviation on 1 April.»
   Anys: 2017 · funció: `ceo` · allotjament: `tercer` · nivell B · prova: Edmunds continuava com a CEO interí de BBA Aviation en la data de l'informe (exercici 2017, publicat el 2018) i deixaria el càrrec l'1 d'abril · URL: https://www.dialight.com/wp-content/uploads/2022/07/21617_dialight_ar17_222_final.pdf · Wayback: https://web.archive.org/web/20230703010445/https://www.dialight.com/wp-content/uploads/2022/07/21617_dialight_ar17_222_final.pdf (existent; cita no verificada a la captura)

3. [`L2|GB00B1FP8915|C3`] [V] «Interim Chief Executive of BBA Aviation plc until 1 April 2018 (after which he will continue on the Board as a Non-Executive Director).»
   Anys: 2017 · funció: `context` · allotjament: `tercer` · nivell B · prova: Edmunds és Interim Chief Executive de BBA Aviation plc fins a l'1/4/2018 · URL: https://www.dialight.com/wp-content/uploads/2022/07/21617_dialight_ar17_222_final.pdf · Wayback: https://web.archive.org/web/20230703010445/https://www.dialight.com/wp-content/uploads/2022/07/21617_dialight_ar17_222_final.pdf (existent; cita no verificada a la captura)

4. [`L2|GB00B1FP8915|C4`] [V] «Simon Pryce, who has served as CEO of BBA Aviation for the past 10 years, is stepping down on June 30. Wayne Edmunds, a non-executive director of the group since 2013, will serve as interim CEO until a permanent successor is named.»
   Anys: 2017 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Pryce deixa el càrrec de CEO el 30/6/2017 i Edmunds el substitueix com a CEO interí · URL: https://www.ainonline.com/aviation-news/business-aviation/2017-06-20/simon-pryce-depart-bba-aviation-end-june · Wayback: https://web.archive.org/web/20260519091547/https://www.ainonline.com/aviation-news/business-aviation/2017-06-20/simon-pryce-depart-bba-aviation-end-june (existent; cita no verificada a la captura)

5. [`L2|GB00B1FP8915|C5`] [V] «Simon Pryce, who has served as CEO of BBA Aviation for the past 10 years, stepped down on June 30.»
   Anys: 2017 · funció: `context` · allotjament: `mitja` · nivell B · prova: Sortida efectiva de Pryce el 30/6/2017 (ja en passat) · URL: https://ainonline.com/aviation-news/business-aviation/2017-08-06/people-aviation-august-2017 · Wayback: https://web.archive.org/web/20260612083901/https://www.ainonline.com/aviation-news/business-aviation/2017-08-06/people-aviation-august-2017 (existent; cita no verificada a la captura)

6. [`L2|GB00B1FP8915|C6`] [V] «Interim group CEO Wayne Edmunds will step down on 1 April, remaining on the board as a non-executive director.»
   Anys: 2017 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: El 2/1/2018 Edmunds encara és CEO interí del grup i ho serà fins a l'1 d'abril · URL: https://www.corporatejetinvestor.com/news/bba-aviation-appoints-new-ceo-614/ · Wayback: https://web.archive.org/web/20260305234859/https://www.corporatejetinvestor.com/news/bba-aviation-appoints-new-ceo-614/ (existent; cita no verificada a la captura)

7. [`L2|GB00B1FP8915|C7`] [V] «Johnstone (pictured) will take up his new role on 1 April 2018 and will be based in Orlando, Florida.»
   Anys: 2017 · funció: `context` · allotjament: `mitja` · nivell B · prova: El successor (Mark Johnstone, group chief executive) no assumeix el càrrec fins a l'1/4/2018 · URL: https://www.corporatejetinvestor.com/news/bba-aviation-appoints-new-ceo-614/ · Wayback: https://web.archive.org/web/20260305234859/https://www.corporatejetinvestor.com/news/bba-aviation-appoints-new-ceo-614/ (existent; cita no verificada a la captura)

8. [`L2|GB00B1FP8915|C8n`] [V] «PRYCE, Simon Charles Conrad Correspondence address Hackers House, Junction Road Churchill, Nr Chipping Norton, Oxfordshire, OX7 6NW Role Resigned Director Date of birth December 1961 Appointed on 11 June 2007 Resigned on 30 June 2017»
   Anys: 2017 · funció: `context` · allotjament: `regulador` · nivell A · prova: El registre inscriu Simon Pryce amb el rol 'Director' ('Role Resigned Director'), no CEO, i no consigna cap càrrec executiu. Nomenat l'11/6/2007 i dimitit el 30/6/2017. Només situa la seva sortida del consell el 30/6/2017, coherent amb la fi del mandat de CEO que descriuen C4 i C5. No prova cap càrrec de CEO. · URL: https://find-and-update.company-information.service.gov.uk/company/00053688/officers · Wayback: https://web.archive.org/web/20220121171646/https://find-and-update.company-information.service.gov.uk/company/00053688/officers (existent; cita no verificada a la captura) · substitueix `L2|GB00B1FP8915|C8`

9. [`L2|GB00B1FP8915|C9n`] [V] «JOHNSTONE, Mark Robin Correspondence address 105 Wigmore Street, London, W1U 1QY Role Resigned Director Date of birth September 1968 Appointed on 1 April 2018 Resigned on 9 June 2021»
   Anys: 2017 · funció: `context` · allotjament: `regulador` · nivell A · prova: El registre inscriu Mark Johnstone amb el rol 'Director' ('Role Resigned Director'), no CEO, i no consigna cap càrrec executiu. Nomenat l'1/4/2018 i dimitit el 9/6/2021. Només prova que el successor no entra al consell fins a l'1/4/2018, després del 31/10/2017. No prova cap càrrec de CEO. · URL: https://find-and-update.company-information.service.gov.uk/company/00053688/officers · Wayback: https://web.archive.org/web/20220121171646/https://find-and-update.company-information.service.gov.uk/company/00053688/officers (existent; cita no verificada a la captura) · substitueix `L2|GB00B1FP8915|C9`

10. [`L2|GB00B1FP8915|C10n`] [V] «EDMUNDS, Wayne Edward Correspondence address 3rd Floor, 105 Wigmore Street, London, United Kingdom, W1U 1QY Role Resigned Director Date of birth February 1956 Appointed on 7 August 2013 Resigned on 1 June 2021»
   Anys: 2017 · funció: `context` · allotjament: `regulador` · nivell A · prova: El registre inscriu Wayne Edmunds amb el rol 'Director' ('Role Resigned Director'), no CEO, i no consigna el càrrec executiu. Nomenat el 7/8/2013 i dimitit l'1/6/2021, de manera que era administrador de forma contínua el 31/10/2017. No prova el càrrec de CEO interí (fila d'un CEO interí, R2): aquest càrrec el proven C1, C2, C4 i C6. · URL: https://find-and-update.company-information.service.gov.uk/company/00053688/officers · Wayback: https://web.archive.org/web/20220121171646/https://find-and-update.company-information.service.gov.uk/company/00053688/officers (existent; cita no verificada a la captura) · substitueix `L2|GB00B1FP8915|C10`

### L2.19 Whitbread PLC Reg. Shares LS -,76797385 (`GB00B1KJJ408`)

- isin i anys: `GB00B1KJJ408`, 2016-2020, 2022 (n=6). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Alison Brittain → Alison Brittain (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2016: marca `informe_exercici`; cites del CEO `L2|GB00B1KJJ408|W03`, `L2|GB00B1KJJ408|W04`, `L2|GB00B1KJJ408|W01`, `L2|GB00B1KJJ408|W18`; datació `L2|GB00B1KJJ408|W02`.
- 2017: marca `informe_exercici`; cites del CEO `L2|GB00B1KJJ408|W06`, `L2|GB00B1KJJ408|W04`, `L2|GB00B1KJJ408|W07`, `L2|GB00B1KJJ408|W01`, `L2|GB00B1KJJ408|W18`; datació `L2|GB00B1KJJ408|W05`.
- 2018: marca `informe_exercici`; cites del CEO `L2|GB00B1KJJ408|W09`, `L2|GB00B1KJJ408|W21`, `L2|GB00B1KJJ408|W07`, `L2|GB00B1KJJ408|W01`, `L2|GB00B1KJJ408|W18`; datació `L2|GB00B1KJJ408|W08`.
- 2019: marca `informe_exercici`; cites del CEO `L2|GB00B1KJJ408|W11`, `L2|GB00B1KJJ408|W12`, `L2|GB00B1KJJ408|W01`, `L2|GB00B1KJJ408|W18`; datació `L2|GB00B1KJJ408|W10`.
- 2020: marca `informe_exercici`; cites del CEO `L2|GB00B1KJJ408|W14`, `L2|GB00B1KJJ408|W15`, `L2|GB00B1KJJ408|W12`, `L2|GB00B1KJJ408|W01`, `L2|GB00B1KJJ408|W18`; datació `L2|GB00B1KJJ408|W13`.
- 2022: marca `prova_interval`; cites del CEO `L2|GB00B1KJJ408|W17`, `L2|GB00B1KJJ408|W18`, `L2|GB00B1KJJ408|W01`; datació `L2|GB00B1KJJ408|W16`; context `L2|GB00B1KJJ408|W19`, `L2|GB00B1KJJ408|W20`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/GB00B1KJJ408.md](../empreses/GB00B1KJJ408.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|GB00B1KJJ408|W01`] [V] «In September 2015, Alison Brittain joined Whitbread as Chief Executive Designate before taking over as Chief Executive in December.»
   Anys: 2016-2020, 2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Inici del mandat: Brittain assumeix el càrrec de Chief Executive el desembre de 2015 · URL: https://cdn.whitbread.co.uk/media/2026/07/Annual_Report_and_Accounts_2015_16.pdf · Wayback: `pendent_verificacio_externa`

2. [`L2|GB00B1KJJ408|W02`] [V] «Released : 25 October 2016»
   Anys: 2016 · funció: `datacio` · allotjament: `emissor` · nivell A · prova: Data del comunicat de resultats semestrals: 25 d octubre de 2016 · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread-Interim-Results.pdf · Wayback: `pendent_verificacio_externa`

3. [`L2|GB00B1KJJ408|W03`] [V] «Alison Brittain, Chief Executive, said:»
   Anys: 2016 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Brittain és Chief Executive al comunicat del 25/10/2016 · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread-Interim-Results.pdf · Wayback: `pendent_verificacio_externa`

4. [`L2|GB00B1KJJ408|W04`] [V] «Alison Brittain Chief Executive 24 April 2017»
   Anys: 2016-2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Brittain signa com a Chief Executive l informe de l exercici 2016/17 el 24/4/2017 · URL: https://cdn.whitbread.co.uk/media/2026/07/whitbread_interactive_2017.pdf · Wayback: `pendent_verificacio_externa`

5. [`L2|GB00B1KJJ408|W05`] [V] «Released : 24 October 2017»
   Anys: 2017 · funció: `datacio` · allotjament: `emissor` · nivell A · prova: Data del comunicat: 24 d octubre de 2017 · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread-Interim-Results-2017.pdf · Wayback: `pendent_verificacio_externa`

6. [`L2|GB00B1KJJ408|W06`] [V] «Alison Brittain, Whitbread Chief Executive Officer, commented:»
   Anys: 2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Brittain és Chief Executive Officer al comunicat del 24/10/2017 · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread-Interim-Results-2017.pdf · Wayback: `pendent_verificacio_externa`

7. [`L2|GB00B1KJJ408|W07`] [V] «Alison Brittain Chief Executive 24 April 2018»
   Anys: 2017-2018 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Brittain signa com a Chief Executive l informe de l exercici 2017/18 el 24/4/2018 · URL: https://cdn.whitbread.co.uk/media/2018/05/2018-annual-report-and-accounts.pdf · Wayback: `pendent_verificacio_externa`

8. [`L2|GB00B1KJJ408|W08`] [V] «Interim results | FY19 23 October 2018»
   Anys: 2018 · funció: `datacio` · allotjament: `emissor` · nivell A · prova: Data del comunicat: 23 d octubre de 2018 · URL: https://cdn.whitbread.co.uk/media/2026/07/interim-results-press-release-23-10-2018.pdf · Wayback: `pendent_verificacio_externa`

9. [`L2|GB00B1KJJ408|W09`] [V] «Alison Brittain, Whitbread Chief Executive Officer, commented:»
   Anys: 2018 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Brittain és Chief Executive Officer al comunicat del 23/10/2018 · URL: https://cdn.whitbread.co.uk/media/2026/07/interim-results-press-release-23-10-2018.pdf · Wayback: `pendent_verificacio_externa`

10. [`L2|GB00B1KJJ408|W10`] [V] «FY20 Interim Results 22 October 2019»
   Anys: 2019 · funció: `datacio` · allotjament: `emissor` · nivell A · prova: Data del comunicat: 22 d octubre de 2019 · URL: https://cdn.whitbread.co.uk/media/2026/07/interim-results-2019.pdf · Wayback: `pendent_verificacio_externa`

11. [`L2|GB00B1KJJ408|W11`] [V] «Alison Brittain, Whitbread Chief Executive Officer, commented:»
   Anys: 2019 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Brittain és Chief Executive Officer al comunicat del 22/10/2019 · URL: https://cdn.whitbread.co.uk/media/2026/07/interim-results-2019.pdf · Wayback: `pendent_verificacio_externa`

12. [`L2|GB00B1KJJ408|W12`] [V] «Alison Brittain Chief Executive 21 May 2020»
   Anys: 2019-2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Brittain signa com a Chief Executive l informe de l exercici 2019/20 el 21/5/2020 · URL: https://cdn.whitbread.co.uk/media/2026/07/2020-annual-report-and-accounts.pdf · Wayback: `pendent_verificacio_externa`

13. [`L2|GB00B1KJJ408|W13`] [V] «FY21 Interim Results 27 October 2020»
   Anys: 2020 · funció: `datacio` · allotjament: `emissor` · nivell A · prova: Data del comunicat: 27 d octubre de 2020 · URL: https://cdn.whitbread.co.uk/media/2026/07/interim-results-2020-1.pdf · Wayback: `pendent_verificacio_externa`

14. [`L2|GB00B1KJJ408|W14`] [V] «Alison Brittain, Whitbread Chief Executive Officer, commented:»
   Anys: 2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Brittain és Chief Executive Officer al comunicat del 27/10/2020 · URL: https://cdn.whitbread.co.uk/media/2026/07/interim-results-2020-1.pdf · Wayback: `pendent_verificacio_externa`

15. [`L2|GB00B1KJJ408|W15`] [V] «Alison Brittain Chief Executive 26 April 2021»
   Anys: 2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Brittain signa com a Chief Executive l informe de l exercici 2020/21 el 26/4/2021 · URL: https://cdn.whitbread.co.uk/media/2026/08/Whitbread_AR2020-21.pdf · Wayback: `pendent_verificacio_externa`

16. [`L2|GB00B1KJJ408|W16`] [V] «FY23 H1 Results 25 October 2022»
   Anys: 2022 · funció: `datacio` · allotjament: `emissor` · nivell A · prova: Data del comunicat: 25 d octubre de 2022 · URL: https://cdn.whitbread.co.uk/media/2026/07/H1-FY23-RNS-FINAL-v2.pdf · Wayback: `pendent_verificacio_externa`

17. [`L2|GB00B1KJJ408|W17`] [V] «Commenting on today’s results, Alison Brittain, Whitbread Chief Executive Officer, said:»
   Anys: 2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Brittain és Chief Executive Officer al comunicat del 25/10/2022 · URL: https://cdn.whitbread.co.uk/media/2026/07/H1-FY23-RNS-FINAL-v2.pdf · Wayback: `pendent_verificacio_externa`

18. [`L2|GB00B1KJJ408|W18`] [V] «Alison Brittain stepping down as Chief Executive on 17 January 2023.»
   Anys: 2016-2020, 2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Fi del mandat: Brittain deixa el càrrec de Chief Executive el 17/1/2023 · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread_AR22_Interactive.pdf · Wayback: `pendent_verificacio_externa`

19. [`L2|GB00B1KJJ408|W19`] [V] «Dominic Paul joined Whitbread on 10 January 2023 and joined the Board and became Chief Executive with effect from 17 January 2023.»
   Anys: 2022 · funció: `context` · allotjament: `emissor` · nivell A · prova: El successor Dominic Paul esdevé Chief Executive amb efecte 17/1/2023 (posterior al 31/10/2022) · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread_AR22_Interactive.pdf · Wayback: `pendent_verificacio_externa`

20. [`L2|GB00B1KJJ408|W20`] [V] «reflecting that Dominic Paul became CEO with effect from the close of the Board meeting held on that day.»
   Anys: 2022 · funció: `context` · allotjament: `emissor` · nivell A · prova: Confirma el relleu de CEO a Dominic Paul (la frase anterior del document situa el dia al 17 January 2023) · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread-PLC-Annual-Report-and-Accounts-2023_24_Single_pages.pdf · Wayback: `pendent_verificacio_externa`

21. [`L2|GB00B1KJJ408|W21`] [V] «Alison Brittain Chief Executive 29 April 2019»
   Anys: 2018 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Brittain signa com a Chief Executive el 29/4/2019 l'informe de l'exercici 2018/19 (2/3/2018-28/2/2019), que inclou el 31/10/2018. L'informe no documenta cap canvi de CEO entre el 31/10/2018 i el 28/2/2019. · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread_18-19-Full-Report_Final_Final-1.pdf · Wayback: `pendent_verificacio_externa`

### L2.20 Relx PLC Registered Shares LS -,144397 (`GB00B2B0DG97`)

- isin i anys: `GB00B2B0DG97`, 2016-2025 (n=10). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Erik Engstrom → Erik Engstrom (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2016: marca `informe_exercici`; cites del CEO `L2|GB00B2B0DG97|RELX2016a`; context `L2|GB00B2B0DG97|RELX2016b`.
- 2017: marca `informe_exercici`; cites del CEO `L2|GB00B2B0DG97|RELX2017a`; context `L2|GB00B2B0DG97|RELX2017b`.
- 2018: marca `informe_exercici`; cites del CEO `L2|GB00B2B0DG97|RELX2018a`; context `L2|GB00B2B0DG97|RELX2018b`.
- 2019: marca `informe_exercici`; cites del CEO `L2|GB00B2B0DG97|RELX2019a`; context `L2|GB00B2B0DG97|RELX2019b`.
- 2020: marca `informe_exercici`; cites del CEO `L2|GB00B2B0DG97|RELX2020a`; context `L2|GB00B2B0DG97|RELX2020b`.
- 2021: marca `informe_exercici`; cites del CEO `L2|GB00B2B0DG97|RELX2021a`; context `L2|GB00B2B0DG97|RELX2021b`.
- 2022: marca `informe_exercici`; cites del CEO `L2|GB00B2B0DG97|RELX2022a`.
- 2023: marca `informe_exercici`; cites del CEO `L2|GB00B2B0DG97|RELX2023a`.
- 2024: marca `informe_exercici`; cites del CEO `L2|GB00B2B0DG97|RELX2024a`.
- 2025: marca `informe_exercici`; cites del CEO `L2|GB00B2B0DG97|RELX2025a`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/GB00B2B0DG97.md](../empreses/GB00B2B0DG97.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|GB00B2B0DG97|RELX2016a`] [V] «Erik Engstrom (53) Chief Executive Officer»
   Anys: 2016 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Erik Engstrom figura com a Chief Executive Officer al consell de l'informe anual 2016 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2016-annual-report.pdf · Wayback: https://web.archive.org/web/20260122230843/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2016-annual-report.pdf (existent; cita no verificada a la captura)

2. [`L2|GB00B2B0DG97|RELX2016b`] [V] «Appointed: Chief Executive Officer of RELX Group since November 2009. Joined the Group as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2016 · funció: `context` · allotjament: `emissor` · nivell A · prova: La fitxa biogràfica que segueix el nom d'Engstrom diu que és CEO des de novembre de 2009 (mandat continu) · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2016-annual-report.pdf · Wayback: https://web.archive.org/web/20260122230843/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2016-annual-report.pdf (existent; cita no verificada a la captura)

3. [`L2|GB00B2B0DG97|RELX2017a`] [V] «Erik Engstrom (54) Chief Executive Officer»
   Anys: 2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Erik Engstrom figura com a Chief Executive Officer al consell de l'informe anual 2017 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2017-annual-report.pdf · Wayback: https://web.archive.org/web/20261003193538/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2017-annual-report.pdf (existent; cita no verificada a la captura)

4. [`L2|GB00B2B0DG97|RELX2017b`] [V] «Appointed: Chief Executive Officer of RELX Group since November 2009. Joined the Group as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2017 · funció: `context` · allotjament: `emissor` · nivell A · prova: La fitxa biogràfica que segueix el nom d'Engstrom diu que és CEO des de novembre de 2009 (mandat continu) · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2017-annual-report.pdf · Wayback: https://web.archive.org/web/20261003193538/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2017-annual-report.pdf (existent; cita no verificada a la captura)

5. [`L2|GB00B2B0DG97|RELX2018a`] [V] «Erik Engstrom (55) Chief Executive Officer»
   Anys: 2018 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Erik Engstrom figura com a Chief Executive Officer al consell de l'informe anual 2018 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2018-annual-report.pdf · Wayback: https://web.archive.org/web/20260801055453/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2018-annual-report.pdf (existent; cita no verificada a la captura)

6. [`L2|GB00B2B0DG97|RELX2018b`] [V] «Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2018 · funció: `context` · allotjament: `emissor` · nivell A · prova: La fitxa biogràfica que segueix el nom d'Engstrom diu que és CEO des de novembre de 2009 (mandat continu) · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2018-annual-report.pdf · Wayback: https://web.archive.org/web/20260801055453/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2018-annual-report.pdf (existent; cita no verificada a la captura)

7. [`L2|GB00B2B0DG97|RELX2019a`] [V] «Erik Engstrom (56) Chief Executive Officer»
   Anys: 2019 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Erik Engstrom figura com a Chief Executive Officer al consell de l'informe anual 2019 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2019-annual-report.pdf · Wayback: https://web.archive.org/web/20261018031645/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2019-annual-report.pdf (existent; cita no verificada a la captura)

8. [`L2|GB00B2B0DG97|RELX2019b`] [V] «Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2019 · funció: `context` · allotjament: `emissor` · nivell A · prova: La fitxa biogràfica que segueix el nom d'Engstrom diu que és CEO des de novembre de 2009 (mandat continu) · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2019-annual-report.pdf · Wayback: https://web.archive.org/web/20261018031645/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2019-annual-report.pdf (existent; cita no verificada a la captura)

9. [`L2|GB00B2B0DG97|RELX2020a`] [V] «Erik Engstrom (57) Chief Executive Officer»
   Anys: 2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Erik Engstrom figura com a Chief Executive Officer al consell de l'informe anual 2020 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2020-annual-report.pdf · Wayback: https://web.archive.org/web/20261005133031/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2020-annual-report.pdf (existent; cita no verificada a la captura)

10. [`L2|GB00B2B0DG97|RELX2020b`] [V] «Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2020 · funció: `context` · allotjament: `emissor` · nivell A · prova: La fitxa biogràfica que segueix el nom d'Engstrom diu que és CEO des de novembre de 2009 (mandat continu) · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2020-annual-report.pdf · Wayback: https://web.archive.org/web/20261005133031/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2020-annual-report.pdf (existent; cita no verificada a la captura)

11. [`L2|GB00B2B0DG97|RELX2021a`] [V] «Erik Engstrom (58) Chief Executive Officer»
   Anys: 2021 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Erik Engstrom figura com a Chief Executive Officer al consell de l'informe anual 2021 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2021-annual-report.pdf · Wayback: https://web.archive.org/web/20260906115229/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2021-annual-report.pdf (existent; cita no verificada a la captura)

12. [`L2|GB00B2B0DG97|RELX2021b`] [V] «Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2021 · funció: `context` · allotjament: `emissor` · nivell A · prova: La fitxa biogràfica que segueix el nom d'Engstrom diu que és CEO des de novembre de 2009 (mandat continu) · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2021-annual-report.pdf · Wayback: https://web.archive.org/web/20260906115229/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2021-annual-report.pdf (existent; cita no verificada a la captura)

13. [`L2|GB00B2B0DG97|RELX2022a`] [V] «Erik Engstrom (59) Chief Executive Officer Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Erik Engstrom és CEO de RELX des de novembre de 2009 segons l'informe anual 2022 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2022-annual-report.pdf · Wayback: https://web.archive.org/web/20260122231239/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2022-annual-report.pdf (existent; cita no verificada a la captura)

14. [`L2|GB00B2B0DG97|RELX2023a`] [V] «Erik Engstrom (60) Chief Executive Officer Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2023 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Erik Engstrom és CEO de RELX des de novembre de 2009 segons l'informe anual 2023 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2023-annual-report.pdf · Wayback: https://web.archive.org/web/20261027083858/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2023-annual-report.pdf (existent; cita no verificada a la captura)

15. [`L2|GB00B2B0DG97|RELX2024a`] [V] «Erik Engstrom (61) Chief Executive Officer Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2024 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Erik Engstrom és CEO de RELX des de novembre de 2009 segons l'informe anual 2024 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2024-annual-report.pdf · Wayback: https://web.archive.org/web/20261114104137/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2024-annual-report.pdf (existent; cita no verificada a la captura)

16. [`L2|GB00B2B0DG97|RELX2025a`] [V] «Erik Engstrom (62) Chief Executive Officer Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2025 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Erik Engstrom és CEO de RELX des de novembre de 2009 segons l'informe anual 2025 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2025-annual-report.pdf · Wayback: https://web.archive.org/web/20260927162153/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2025-annual-report.pdf (existent; cita no verificada a la captura)

### L2.21 Evraz PLC Registered Shares DL 0,05 (`GB00B71N6K86`)

- isin i anys: `GB00B71N6K86`, 2018-2020 (n=3). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Alexander Frolov → Alexander Frolov (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A, B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2018: marca `prova_interval`; cites del CEO `L2|GB00B71N6K86|C1`, `L2|GB00B71N6K86|C2`, `L2|GB00B71N6K86|C4`; datació `L2|GB00B71N6K86|C5`; context `L2|GB00B71N6K86|C3`.
- 2019: marca `prova_interval+prova_interval_retrospectiva`; cites del CEO `L2|GB00B71N6K86|C1`, `L2|GB00B71N6K86|C2`, `L2|GB00B71N6K86|C6`; context `L2|GB00B71N6K86|C3`.
- 2020: marca `prova_interval`; cites del CEO `L2|GB00B71N6K86|C1`, `L2|GB00B71N6K86|C2`, `L2|GB00B71N6K86|C6`, `L2|GB00B71N6K86|C7`; datació `L2|GB00B71N6K86|C8`; context `L2|GB00B71N6K86|C3`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/GB00B71N6K86.md](../empreses/GB00B71N6K86.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|GB00B71N6K86|C1`] [V] «Mr Frolov was CEO of EVRAZ plc from 14 October 2011 until 31 August 2021.»
   Anys: 2018-2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Interval del mandat d'Alexander Frolov com a CEO d'EVRAZ plc: 14/10/2011-31/08/2021; cobreix el 31/10 de 2018, 2019 i 2020. · URL: https://ar2021.evraz.com/download/full-reports/ar_en_annual-report_pages_evraz_2021.pdf · Wayback: https://web.archive.org/web/20260720011131/https://ar2021.evraz.com/download/full-reports/ar_en_annual-report_pages_evraz_2021.pdf (existent; cita no verificada a la captura)

2. [`L2|GB00B71N6K86|C2`] [V] «Alexander Frolov stepped down from his role of CEO, effective from 31 August 2021.»
   Anys: 2018-2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Data efectiva de fi del mandat de Frolov (informe de remuneracions). · URL: https://ar2021.evraz.com/download/full-reports/ar_en_annual-report_pages_evraz_2021.pdf · Wayback: https://web.archive.org/web/20260720011131/https://ar2021.evraz.com/download/full-reports/ar_en_annual-report_pages_evraz_2021.pdf (existent; cita no verificada a la captura)

3. [`L2|GB00B71N6K86|C3`] [V] «the Board appointed Aleksey Ivanov as CEO effective from 1 September 2021»
   Anys: 2018-2020 · funció: `context` · allotjament: `emissor` · nivell A · prova: Data efectiva d'inici del successor (coherent amb la fila 2021 de la base). · URL: https://ar2021.evraz.com/download/full-reports/ar_en_annual-report_pages_evraz_2021.pdf · Wayback: https://web.archive.org/web/20260720011131/https://ar2021.evraz.com/download/full-reports/ar_en_annual-report_pages_evraz_2021.pdf (existent; cita no verificada a la captura)

4. [`L2|GB00B71N6K86|C4`] [V] «MOSCOW. Aug 9 (Interfax) - Evraz will next pay dividends upon the conclusion of 2018 under the baseline development scenario, CEO Alexander Frolov said during a conference call.»
   Anys: 2018 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Alexander Frolov era CEO d'Evraz el 9/08/2018, dins l'exercici 2018 (tancament el 31/12) i abans del 31/10/2018. És una cita «ceo» contemporània. El límit posterior al 31/10/2018 el donen C1/C2 (fi el 31/08/2021). · URL: https://interfax.com/newsroom/top-stories/23142/ · Wayback: https://web.archive.org/web/20260813033036/https://interfax.com/newsroom/top-stories/23142/ (existent; cita no verificada a la captura)

5. [`L2|GB00B71N6K86|C5`] [V] «9 Aug 2018 15:07 Evraz CEO: next distribution to be final dividend for 2018 under baseline scenario»
   Anys: 2018 · funció: `datacio` · allotjament: `mitja` · nivell B · prova: Data de publicació de C4 (9/08/2018), perquè el cos de la notícia només diu «Aug 9», sense l'any. La capçalera diu «CEO» però no anomena la persona: és datació. · URL: https://interfax.com/newsroom/top-stories/23142/ · Wayback: https://web.archive.org/web/20260813033036/https://interfax.com/newsroom/top-stories/23142/ (existent; cita no verificada a la captura)

6. [`L2|GB00B71N6K86|C6`] [V] «will help us ensure a sustainable future for the Group. Alexander Frolov CEO»
   Anys: 2019-2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: El missatge del CEO de l'informe de sostenibilitat 2019 el signa Alexander Frolov com a CEO, amb el nom i el càrrec dins el fragment. El mateix document diu «Sustainability Report 2019 was issued in Spring 2020» i les metadades del PDF diuen 20/05/2020. Per tant, prova que Frolov era CEO a la primavera de 2020. Per a 2020 és una cita contemporània: és dins l'exercici 2020 i anterior al 31/10/2020, i juntament amb C7 (25/02/2021) acota el 31/10/2020 pels dos costats. Per a 2019 no és contemporània: és posterior al 30/04/2020 segons les metadades, no és l'informe anual i no dona dates de mandat. · URL: https://sr2019.evraz.com/download/full-reports/csr_en_annual-report_spreads_evraz_2019.pdf · Wayback: https://web.archive.org/web/20220121111455/https://sr2019.evraz.com/download/full-reports/csr_en_annual-report_spreads_evraz_2019.pdf (existent; cita no verificada a la captura)

7. [`L2|GB00B71N6K86|C7`] [V] «Evraz CEO and co-founder Alexander Frolov said on a conference call for reporters.»
   Anys: 2020 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Alexander Frolov era CEO d'Evraz el 25/02/2021. La data és dins els 4 mesos posteriors al tancament de l'exercici 2020 (31/12/2020, finestra fins al 30/04/2021), i per tant és una cita «ceo» contemporània posterior al 31/10/2020. · URL: https://interfax.com/newsroom/top-stories/71177/ · Wayback: https://web.archive.org/web/20210225172011/https://interfax.com/newsroom/top-stories/71177/ (existent; cita no verificada a la captura)

8. [`L2|GB00B71N6K86|C8`] [V] «25 Feb 2021 16:49 Evraz speaks of growing interest of companies in M&A in U.S. but yet to see interesting propositions»
   Anys: 2020 · funció: `datacio` · allotjament: `mitja` · nivell B · prova: Data de publicació de C7 (25/02/2021), perquè el cos de la notícia només diu «Feb 25», sense l'any. · URL: https://interfax.com/newsroom/top-stories/71177/ · Wayback: https://web.archive.org/web/20210225172011/https://interfax.com/newsroom/top-stories/71177/ (existent; cita no verificada a la captura)

### L2.22 NatWest Group PLC Registered Shares LS 1 (`GB00B7T77214`)

- isin i anys: `GB00B7T77214`, 2020-2021 (n=2). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Alison Rose → Alison Rose (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2020: marca `informe_exercici`; cites del CEO `L2|GB00B7T77214|C1`, `L2|GB00B7T77214|C3`; context `L2|GB00B7T77214|C2`.
- 2021: marca `informe_exercici`; cites del CEO `L2|GB00B7T77214|C4`, `L2|GB00B7T77214|C6`; context `L2|GB00B7T77214|C5`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/GB00B7T77214.md](../empreses/GB00B7T77214.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|GB00B7T77214|C1`] [V] «As highlighted in last year’s report, Alison Rose was appointed as CEO on 1 November 2019»
   Anys: 2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Inici del mandat d'Alison Rose com a CEO: 1/11/2019 (informe de l'exercici 2020). · URL: https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/19022021/natwest-group-annual-report-accounts-2020.pdf · Wayback: https://web.archive.org/web/20210406172341/https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/19022021/natwest-group-annual-report-accounts-2020.pdf (existent; cita no verificada a la captura)

2. [`L2|GB00B7T77214|C2`] [V] «The data for 2020 is based on remuneration earned by Alison Rose»
   Anys: 2020 · funció: `context` · allotjament: `emissor` · nivell A · prova: La ràtio salarial del CEO de 2020 es calcula amb la remuneració d'Alison Rose (CEO durant l'exercici 2020). · URL: https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/19022021/natwest-group-annual-report-accounts-2020.pdf · Wayback: https://web.archive.org/web/20210406172341/https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/19022021/natwest-group-annual-report-accounts-2020.pdf (existent; cita no verificada a la captura)

3. [`L2|GB00B7T77214|C3`] [V] «Alison Rose-Slade Group Chief Executive Officer»
   Anys: 2020 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Signa l'informe anual 2020 (publicat el 19/2/2021) com a Group Chief Executive Officer: continuïtat després del 31/10/2020. · URL: https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/19022021/natwest-group-annual-report-accounts-2020.pdf · Wayback: https://web.archive.org/web/20210406172341/https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/19022021/natwest-group-annual-report-accounts-2020.pdf (existent; cita no verificada a la captura)

4. [`L2|GB00B7T77214|C4`] [V] «Alison Rose, CEO, was appointed on 1 November 2019 and therefore the annual change comparison to 2020 is not relevant»
   Anys: 2021 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Informe de l'exercici 2021: Alison Rose és la CEO, nomenada l'1/11/2019. · URL: https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/18022022/natwest-group-annual-report-accounts-2021.pdf · Wayback: https://web.archive.org/web/20260716195759/https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/18022022/natwest-group-annual-report-accounts-2021.pdf (existent; cita no verificada a la captura)

5. [`L2|GB00B7T77214|C5`] [V] «The data for 2021 is based on remuneration earned by Alison Rose»
   Anys: 2021 · funció: `context` · allotjament: `emissor` · nivell A · prova: La ràtio salarial del CEO de 2021 es calcula amb la remuneració d'Alison Rose (CEO durant l'exercici 2021). · URL: https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/18022022/natwest-group-annual-report-accounts-2021.pdf · Wayback: https://web.archive.org/web/20260716195759/https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/18022022/natwest-group-annual-report-accounts-2021.pdf (existent; cita no verificada a la captura)

6. [`L2|GB00B7T77214|C6`] [V] «Alison Rose-Slade Group Chief Executive Officer»
   Anys: 2021 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Signa l'informe anual 2021 (publicat el 18/2/2022) com a Group Chief Executive Officer: continuïtat després del 31/10/2021. · URL: https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/18022022/natwest-group-annual-report-accounts-2021.pdf · Wayback: https://web.archive.org/web/20260716195759/https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/18022022/natwest-group-annual-report-accounts-2021.pdf (existent; cita no verificada a la captura)

### L2.23 Phoenix Group Holdings PLC Registered (`GB00BGXQNP29`)

- isin i anys: `GB00BGXQNP29`, 2020-2025 (n=6). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Andy Briggs → Andy Briggs (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2020: marca `informe_exercici`; cites del CEO `L2|GB00BGXQNP29|C1`; context `L2|GB00BGXQNP29|C2`.
- 2021: marca `informe_exercici`; cites del CEO `L2|GB00BGXQNP29|C3`, `L2|GB00BGXQNP29|C1`.
- 2022: marca `informe_exercici`; cites del CEO `L2|GB00BGXQNP29|C4`.
- 2023: marca `informe_exercici`; cites del CEO `L2|GB00BGXQNP29|C5`.
- 2024: marca `informe_exercici`; cites del CEO `L2|GB00BGXQNP29|C6`.
- 2025: marca `informe_exercici`; cites del CEO `L2|GB00BGXQNP29|C7`; context `L2|GB00BGXQNP29|C8`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/GB00BGXQNP29.md](../empreses/GB00BGXQNP29.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|GB00BGXQNP29|C1`] [V] «Andy Briggs joined the Board of Phoenix Group Holdings plc on 10 February 2020 as Group CEO Designate and became CEO on 10 March 2020.»
   Anys: 2020-2021 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Data efectiva d'inici com a CEO: 10/03/2020 (abans del 31/10/2020). · URL: https://library.standardlife.co.uk/fy-20-annual-report-and-accounts.pdf · Wayback: https://web.archive.org/web/20260415204647/https://library.standardlife.co.uk/fy-20-annual-report-and-accounts.pdf (existent; cita no verificada a la captura)

2. [`L2|GB00BGXQNP29|C2`] [V] «Clive Bannister left the role of Group Chief Executive Officer on 10 March 2020 and left Phoenix Group on the same date.»
   Anys: 2020 · funció: `context` · allotjament: `grup` · nivell A · prova: El CEO anterior va deixar el càrrec el 10/03/2020. · URL: https://library.standardlife.co.uk/fy-20-annual-report-and-accounts.pdf · Wayback: https://web.archive.org/web/20260415204647/https://library.standardlife.co.uk/fy-20-annual-report-and-accounts.pdf (existent; cita no verificada a la captura)

3. [`L2|GB00BGXQNP29|C3`] [V] «Andy Briggs is Group Chief Executive Officer of the Company.»
   Anys: 2021 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2021. · URL: https://library.standardlife.co.uk/phoenix-group-full-year-results-2021.pdf · Wayback: https://web.archive.org/web/20260415190436/https://library.standardlife.co.uk/phoenix-group-full-year-results-2021.pdf (existent; cita no verificada a la captura)

4. [`L2|GB00BGXQNP29|C4`] [V] «Andy Briggs is Group Chief Executive Officer (‘CEO’) of Phoenix.»
   Anys: 2022 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2022. · URL: https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2022.pdf · Wayback: https://web.archive.org/web/20260415192505/https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2022.pdf (existent; cita no verificada a la captura)

5. [`L2|GB00BGXQNP29|C5`] [V] «Andy Briggs is the Group Chief Executive Officer (‘CEO’).»
   Anys: 2023 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2023. · URL: https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2023.pdf · Wayback: https://web.archive.org/web/20260303032752/https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2023.pdf (existent; cita no verificada a la captura)

6. [`L2|GB00BGXQNP29|C6`] [V] «The Group’s Chief Executive Officer, Andy Briggs, is the Executive Board Director responsible for implementation»
   Anys: 2024 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2024. · URL: https://library.standardlifeplc.com/phoenix_group_annual_report_and_accounts_2024.pdf · Wayback: `pendent_verificacio_externa`

7. [`L2|GB00BGXQNP29|C7`] [V] «Andy Briggs, Group CEO, is responsible for embedding sustainability within»
   Anys: 2025 · funció: `ceo` · allotjament: `grup` · nivell A · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2025. · URL: https://library.standardlife.co.uk/annual-report-and-accounts-2025-spread.pdf · Wayback: https://web.archive.org/web/20260719182559/https://library.standardlife.co.uk/annual-report-and-accounts-2025-spread.pdf (existent; cita no verificada a la captura)

8. [`L2|GB00BGXQNP29|C8`] [V] «Clive Bannister left the role of Group CEO on 10 March 2020 and left the Group on the same date. Andy Briggs was appointed to the Board on 10 February 2020 and remained as CEO-designate until 10 March 2020.»
   Anys: 2025 · funció: `context` · allotjament: `grup` · nivell A · prova: Únic canvi de CEO documentat a la sèrie: 10/03/2020; l'informe 2025 no en registra cap altre. · URL: https://library.standardlife.co.uk/annual-report-and-accounts-2025-spread.pdf · Wayback: https://web.archive.org/web/20260719182559/https://library.standardlife.co.uk/annual-report-and-accounts-2025-spread.pdf (existent; cita no verificada a la captura)

### L2.24 Deliveroo PLC Registered Shares (`GB00BNC5T391`)

- isin i anys: `GB00BNC5T391`, 2021 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Will Shu → Will Shu (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2021: marca `prova_interval`; cites del CEO `L2|GB00BNC5T391|C1`, `L2|GB00BNC5T391|C3`, `L2|GB00BNC5T391|C5`, `L2|GB00BNC5T391|C6`, `L2|GB00BNC5T391|C7`; datació `L2|GB00BNC5T391|C2`; context `L2|GB00BNC5T391|C4`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/GB00BNC5T391.md](../empreses/GB00BNC5T391.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|GB00BNC5T391|C1`] [V] «Will Shu, Founder and CEO of Deliveroo, said:»
   Anys: 2021 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: L'emissor identifica Will Shu com a Founder and CEO al comunicat del 20/10/2021 (11 dies abans del 31/10/2021). · URL: https://www.rns-pdf.londonstockexchange.com/rns/5922P_1-2021-10-19.pdf · Wayback: https://web.archive.org/web/20240513152637/https://www.rns-pdf.londonstockexchange.com/rns/5922P_1-2021-10-19.pdf (existent; cita no verificada a la captura)

2. [`L2|GB00BNC5T391|C2`] [V] «Deliveroo plc Q3 2021 Trading Update 20 October 2021»
   Anys: 2021 · funció: `datacio` · allotjament: `regulador` · nivell A · prova: Data del comunicat de la cita C1: 20 d'octubre de 2021. · URL: https://www.rns-pdf.londonstockexchange.com/rns/5922P_1-2021-10-19.pdf · Wayback: https://web.archive.org/web/20240513152637/https://www.rns-pdf.londonstockexchange.com/rns/5922P_1-2021-10-19.pdf (existent; cita no verificada a la captura)

3. [`L2|GB00BNC5T391|C3`] [V] «** This is the date on which Will Shu was appointed as CEO. Will Shu was appointed to the Deliveroo plc Board on 19 March 2021.»
   Anys: 2021 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Nota de la taula de contractes: la data marcada amb ** (1 February 2013) es la del nomenament de Will Shu com a CEO. · URL: https://data.fca.org.uk/artefacts/NSM/Portal/NI-000092427/NI-000092427.pdf · Wayback: `pendent_verificacio_externa`

4. [`L2|GB00BNC5T391|C4`] [V] «Will Shu 1 February 2013** 22 March 2021 12 months 6 months»
   Anys: 2021 · funció: `context` · allotjament: `regulador` · nivell A · prova: Data de nomenament al carrec (CEO): 1 de febrer de 2013; contracte vigent del 22/03/2021. Inici del mandat anterior al 31/10/2021. · URL: https://data.fca.org.uk/artefacts/NSM/Portal/NI-000092427/NI-000092427.pdf · Wayback: `pendent_verificacio_externa`

5. [`L2|GB00BNC5T391|C5`] [V] «Will Shu Founder and Chief Executive Officer 13 March 2024»
   Anys: 2021 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Will Shu continua com a Founder and CEO el 13/03/2024: continuitat documentada en una data posterior al 31/10/2021. · URL: https://data.fca.org.uk/artefacts/NSM/Portal/NI-000092427/NI-000092427.pdf · Wayback: `pendent_verificacio_externa`

6. [`L2|GB00BNC5T391|C6`] [V] «The Company’s Chief Executive Officer is Will Shu, born in 1979»
   Anys: 2021 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: Will Shu es el CEO de la societat a la data del prospecte (marc 2021). · URL: https://data.fca.org.uk/artefacts/NSM/Portal/NI-000022020/NI-000022020.pdf · Wayback: https://web.archive.org/web/20230604024150/https://data.fca.org.uk/artefacts/NSM/Portal/NI-000022020/NI-000022020.pdf (existent; cita no verificada a la captura)

7. [`L2|GB00BNC5T391|C7`] [V] «Will Shu Chief Executive Officer Appointed as CEO: 1 February 2013 Appointed to Deliveroo plc: 19 March 2021»
   Anys: 2021 · funció: `ceo` · allotjament: `regulador` · nivell A · prova: En un sol fragment hi ha el nom (Will Shu), el càrrec (Chief Executive Officer) i la data de nomenament com a CEO (1/02/2013). És l'inici del mandat, anterior al 31/10/2021. És retrospectiu (document del 13/03/2024). · URL: https://data.fca.org.uk/artefacts/NSM/Portal/NI-000092427/NI-000092427.pdf · Wayback: `pendent_verificacio_externa`

### L2.25 WPP PLC Registered Shares LS -,10 (`JE00B8KF9B49`)

- isin i anys: `JE00B8KF9B49`, 2025 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Cindy Rose → Cindy Rose (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2025: marca `informe_exercici`; cites del CEO `L2|JE00B8KF9B49|c1`, `L2|JE00B8KF9B49|c3`, `L2|JE00B8KF9B49|c4`, `L2|JE00B8KF9B49|c5`; context `L2|JE00B8KF9B49|c2`, `L2|JE00B8KF9B49|c6`, `L2|JE00B8KF9B49|c7`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/JE00B8KF9B49.md](../empreses/JE00B8KF9B49.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|JE00B8KF9B49|c1`] [V] «Cindy Rose has been appointed as Chief Executive Officer (CEO) of the Company, effective 1 September 2025»
   Anys: 2025 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Nomenament de Cindy Rose com a CEO amb efecte 1/9/2025 · URL: https://www.wpp.com/en/news/2025/07/chief-executive-officer-appointment · Wayback: https://web.archive.org/web/20261006023253/https://www.wpp.com/en/news/2025/07/chief-executive-officer-appointment (existent; cita no verificada a la captura)

2. [`L2|JE00B8KF9B49|c2`] [V] «Cindy succeeds Mark Read who will step down as CEO on the same date»
   Anys: 2025 · funció: `context` · allotjament: `emissor` · nivell A · prova: Mark Read deixa de ser CEO l'1/9/2025 · URL: https://www.wpp.com/en/news/2025/07/chief-executive-officer-appointment · Wayback: https://web.archive.org/web/20261006023253/https://www.wpp.com/en/news/2025/07/chief-executive-officer-appointment (existent; cita no verificada a la captura)

3. [`L2|JE00B8KF9B49|c3`] [V] «Cindy Rose assumed the role of CEO from 1 September»
   Anys: 2025 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Document datat el 30/10/2025: Rose va assumir el càrrec l'1/9 · URL: https://www.wpp.com/en/news/2025/10/third-quarter-trading-update-2025 · Wayback: https://web.archive.org/web/20260128150642/https://www.wpp.com/en/news/2025/10/third-quarter-trading-update-2025 (existent; cita no verificada a la captura)

4. [`L2|JE00B8KF9B49|c4`] [V] «Cindy Rose, Chief Executive Officer of WPP, said:»
   Anys: 2025 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Rose és CEO el 30/10/2025 (vigília de la data de referència) · URL: https://www.wpp.com/en/news/2025/10/third-quarter-trading-update-2025 · Wayback: https://web.archive.org/web/20260128150642/https://www.wpp.com/en/news/2025/10/third-quarter-trading-update-2025 (existent; cita no verificada a la captura)

5. [`L2|JE00B8KF9B49|c5`] [V] «Cindy Rose previously served as a Non-Executive Director on the WPP Board and served on the Audit and Nomination Committees until her appointment as CEO on 1 September 2025.»
   Anys: 2025 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Informe anual de l'exercici 2025: nomenament com a CEO l'1/9/2025 · URL: https://cdn.wpp.com/raw/upload/v1778673483/wpp/project/wpp/files/investors/2026/annual-report/wpp_annual_report_2025.pdf · Wayback: https://web.archive.org/web/20260822193651/https://cdn.wpp.com/raw/upload/v1778673483/wpp/project/wpp/files/investors/2026/annual-report/wpp_annual_report_2025.pdf (existent; cita no verificada a la captura)

6. [`L2|JE00B8KF9B49|c6`] [V] «Appointed: 1 April 2019 (Chief Executive Officer from 1 September 2025)»
   Anys: 2025 · funció: `context` · allotjament: `emissor` · nivell A · prova: Biografia de Cindy Rose al consell: CEO des de l'1/9/2025, vigent a la publicació de l'informe (2026) · URL: https://cdn.wpp.com/raw/upload/v1778673483/wpp/project/wpp/files/investors/2026/annual-report/wpp_annual_report_2025.pdf · Wayback: https://web.archive.org/web/20260822193651/https://cdn.wpp.com/raw/upload/v1778673483/wpp/project/wpp/files/investors/2026/annual-report/wpp_annual_report_2025.pdf (existent; cita no verificada a la captura)

7. [`L2|JE00B8KF9B49|c7`] [V] «Mark Read – stepped down from the Board on 1 September 2025»
   Anys: 2025 · funció: `context` · allotjament: `emissor` · nivell A · prova: Sortida de Mark Read l'1/9/2025 · URL: https://cdn.wpp.com/raw/upload/v1778673483/wpp/project/wpp/files/investors/2026/annual-report/wpp_annual_report_2025.pdf · Wayback: https://web.archive.org/web/20260822193651/https://cdn.wpp.com/raw/upload/v1778673483/wpp/project/wpp/files/investors/2026/annual-report/wpp_annual_report_2025.pdf (existent; cita no verificada a la captura)

### L2.26 Signify N.V. Registered Shares EO -,01 (`NL0011821392`)

- isin i anys: `NL0011821392`, 2022 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Eric Rondolat → Eric Rondolat (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2022: marca `informe_exercici`; cites del CEO `L2|NL0011821392|c1`, `L2|NL0011821392|c2`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/NL0011821392.md](../empreses/NL0011821392.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|NL0011821392|c1`] [V] «Eric Rondolat Born 1966, Italian/French Chief Executive Officer Chair of the Board of Management since May 2016»
   Anys: 2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Rondolat és CEO i president del Board of Management des del maig de 2016, vigent a l'informe de l'exercici 2022 · URL: https://www.signify.com/static/2022/signify-annual-report-2022.pdf · Wayback: https://web.archive.org/web/20260705192635/https://www.signify.com/static/2022/signify-annual-report-2022.pdf (existent; cita no verificada a la captura)

2. [`L2|NL0011821392|c2`] [V] «Eric Rondolat CEO Signify Signify Annual Report 2022»
   Anys: 2022 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Rondolat signa la carta del CEO de l'informe anual 2022 com a CEO de Signify · URL: https://www.signify.com/static/2022/signify-annual-report-2022.pdf · Wayback: https://web.archive.org/web/20260705192635/https://www.signify.com/static/2022/signify-annual-report-2022.pdf (existent; cita no verificada a la captura)

### L2.27 Ericsson Namn-Aktier B (fria) o.N. (`SE0000108656`)

- isin i anys: `SE0000108656`, 2016 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Jan Frykhammar → Jan Frykhammar (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R2 (CEO interí). Nivell de les cites del CEO: A, B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2016: marca `informe_exercici`; cites del CEO `L2|SE0000108656|c5`, `L2|SE0000108656|c7`, `L2|SE0000108656|c8`, `L2|SE0000108656|c9`, `L2|SE0000108656|c10`, `L2|SE0000108656|c1`, `L2|SE0000108656|c3`, `L2|SE0000108656|c4`; datació `L2|SE0000108656|c6`; context `L2|SE0000108656|c2`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/SE0000108656.md](../empreses/SE0000108656.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|SE0000108656|c1`] [V] «He will take over at Ericsson on January 16 from acting CEO Jan Frykhammar.»
   Anys: 2016 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: El 26/10/2016 Frykhammar era CEO en funcions i Ekholm no assumia fins al 16 de gener · URL: https://fortune.com/2016/10/26/ericsson-new-ceo-borje-ekholm · Wayback: https://web.archive.org/web/20241217090637/https://fortune.com/2016/10/26/ericsson-new-ceo-borje-ekholm/ (existent; cita no verificada a la captura)

2. [`L2|SE0000108656|c2`] [V] «Ericsson’s Board of Directors has appointed Börje Ekholm as new CEO, effective January 16, 2017.»
   Anys: 2016 · funció: `context` · allotjament: `tercer` · nivell B · prova: Data efectiva del nomenament d'Ekholm: 16/01/2017 (posterior al 31/10/2016) (comunicat d'un accionista, no de l'emissor: es publica com a B; nivell a decidir per Doctorat) · URL: https://www.investorab.com/press/borje-ekholm-appointed-new-ceo-ericsson-steps-down-ceo-patricia-industries-1439281 · Wayback: `pendent_verificacio_externa`

3. [`L2|SE0000108656|c3`] [V] «Jan Frykhammar, who has been working for the company since 1991 will be stepping in as interim CEO»
   Anys: 2016 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Inici del mandat interí de Frykhammar el 25/07/2016, quan Vestberg plega amb efecte immediat · URL: https://techcrunch.com/2016/07/25/ericsson-ceo · Wayback: https://web.archive.org/web/20261003101954/https://techcrunch.com/2016/07/25/ericsson-ceo/ (existent; cita no verificada a la captura)

4. [`L2|SE0000108656|c4`] [V] «Frykhammar will remain interim CEO until Jan. 16, 2017.»
   Anys: 2016 · funció: `ceo` · allotjament: `mitja` · nivell B · prova: Frykhammar continua com a CEO interí fins al 16/01/2017 · URL: https://www.rcrwireless.com/20161028/5g/ericsson-new-ceo-tag31-2 · Wayback: `pendent_verificacio_externa`

5. [`L2|SE0000108656|c5`] [V] «Jan Frykhammar served as President and CEO from July 25, 2016 to January 16, 2017.»
   Anys: 2016 · funció: `ceo` · allotjament: `plataforma` · nivell A · prova: L'informe anual de l'exercici que inclou el 31/10/2016 (exercici natural) diu que Frykhammar va ser President and CEO del 25/07/2016 al 16/01/2017, i per tant era el CEO el 31/10/2016. El mateix informe situa el relleu el 16/01/2017, després del tancament, i no documenta cap altre canvi de CEO entre el 31/10 i el 31/12/2016. Passatges de context comprovats: «Effective January 16, 2017, Börje Ekholm was appointed new President and CEO of the Group» i «Effective July 25, 2016, Jan Frykhammar was appointed new President and CEO». · URL: https://mb.cision.com/Main/15448/2304133/697891.pdf · Wayback: https://web.archive.org/web/20191217050757/https://mb.cision.com/Main/15448/2304133/697891.pdf (existent; cita no verificada a la captura)

6. [`L2|SE0000108656|c6`] [V] «Ericsson Annual Report 2016»
   Anys: 2016 · funció: `datacio` · allotjament: `plataforma` · nivell A · prova: Identifica el document de c5 com l'informe anual de l'exercici 2016. Només data el document. · URL: https://mb.cision.com/Main/15448/2304133/697891.pdf · Wayback: https://web.archive.org/web/20191217050757/https://mb.cision.com/Main/15448/2304133/697891.pdf (existent; cita no verificada a la captura)

7. [`L2|SE0000108656|c7`] [V] «Effective immediately Jan Frykhammar, Executive Vice President and CFO, steps into the position as President and CEO until the now initiated recruitment search has been concluded.»
   Anys: 2016 · funció: `ceo` · allotjament: `plataforma` · nivell A · prova: Frykhammar comença com a President and CEO el 25/07/2016, amb efecte immediat · URL: https://news.cision.com/ericsson/r/ericsson-s-vestberg-steps-down---search-for-new-ceo-initiated,c2304157 · Wayback: https://web.archive.org/web/20191111065817/https://news.cision.com/ericsson/r/ericsson-s-vestberg-steps-down---search-for-new-ceo-initiated,c2304157 (existent; cita no verificada a la captura)

8. [`L2|SE0000108656|c8`] [V] «Comments from Jan Frykhammar, President and CEO of Ericsson»
   Anys: 2016 · funció: `ceo` · allotjament: `plataforma` · nivell A · prova: Frykhammar signa com a President and CEO l'informe trimestral del 21/10/2016, deu dies abans del 31/10/2016 · URL: https://news.cision.com/ericsson/r/ericsson-reports-third-quarter-results-2016,c2176813 · Wayback: https://web.archive.org/web/20191111091224/https://news.cision.com/ericsson/r/ericsson-reports-third-quarter-results-2016,c2176813 (existent; cita no verificada a la captura)

9. [`L2|SE0000108656|c9`] [V] «Jan Frykhammar will remain interim CEO until January 16, 2017.»
   Anys: 2016 · funció: `ceo` · allotjament: `plataforma` · nivell A · prova: El 26/10/2016 Frykhammar era el CEO interí i ho continuaria sent fins al 16/01/2017, data efectiva d'Ekholm · URL: https://news.cision.com/ericsson/r/ericsson-s-board-names-borje-ekholm-new-president-and-ceo,c2304148 · Wayback: https://web.archive.org/web/20191111090743/https://news.cision.com/ericsson/r/ericsson-s-board-names-borje-ekholm-new-president-and-ceo,c2304148 (existent; cita no verificada a la captura)

10. [`L2|SE0000108656|c10`] [V] «Jan Frykhammar who has served as interim CEO since July last year»
   Anys: 2016 · funció: `ceo` · allotjament: `plataforma` · nivell A · prova: Confirma el 16/01/2017, dins els 4 mesos posteriors al tancament de l'exercici 2016, que Frykhammar havia estat CEO interí des del juliol de 2016. El mateix comunicat diu que aquell dia Ekholm «assumes today the position as President and CEO of Ericsson». · URL: https://news.cision.com/ericsson/r/borje-ekholm-takes-office-as-president-and-ceo,c2176772 · Wayback: https://web.archive.org/web/20191111100051/https://news.cision.com/ericsson/r/borje-ekholm-takes-office-as-president-and-ceo,c2176772 (existent; cita no verificada a la captura)

### L2.28 Boliden AB Namn-Aktier SK 2 (`SE0000869646`)

- isin i anys: `SE0000869646`, 2016-2017 (n=2). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Lennart Evrell → Lennart Evrell (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de les cites del CEO: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites i, a les files amb `prova_interval`, si Doctorat accepta la prova per interval; no s'autodeclara.
- 2016: marca `informe_exercici`; cites del CEO `L2|SE0000869646|C1`, `L2|SE0000869646|C2`, `L2|SE0000869646|C3`.
- 2017: marca `informe_exercici`; cites del CEO `L2|SE0000869646|C4`, `L2|SE0000869646|C6`; context `L2|SE0000869646|C5`.
- Justificació, cerca feta i dubtes per a Doctorat: a la fitxa [empreses/SE0000869646.md](../empreses/SE0000869646.md), secció «Pendències d'aquesta empresa».
- Cites:

1. [`L2|SE0000869646|C1`] [V] «Stockholm, 20 October 2016 Lennart Evrell President & CEO»
   Anys: 2016 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Evrell signa com a President & CEO l'informe intermedi el 20/10/2016 · URL: https://investors.boliden.com/sites/boliden-ir/files/pr/201610206170-1.pdf · Wayback: https://web.archive.org/web/20241208120618/https://investors.boliden.com/sites/boliden-ir/files/pr/201610206170-1.pdf (existent; cita no verificada a la captura)

2. [`L2|SE0000869646|C2`] [V] «Evrell, President & CEO of Boliden, summarising the past quarter.»
   Anys: 2016 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Evrell és President & CEO de Boliden el 20/10/2016 · URL: https://investors.boliden.com/sites/boliden-ir/files/pr/201610206172-1.pdf · Wayback: https://web.archive.org/web/20241208123757/https://investors.boliden.com/sites/boliden-ir/files/pr/201610206172-1.pdf (existent; cita no verificada a la captura)

3. [`L2|SE0000869646|C3`] [V] «Boliden has posted one of its strongest years ever. Lennart Evrell President & CEO»
   Anys: 2016 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Evrell signa com a President & CEO la carta de l'informe anual de l'exercici 2016 (exercici natural, inclou el 31/10/2016) · URL: https://investors.boliden.com/sites/boliden-ir/files/pr/201703089998-1.pdf · Wayback: https://web.archive.org/web/20260512121320/https://investors.boliden.com/sites/boliden-ir/files/pr/201703089998-1.pdf (existent; cita no verificada a la captura)

4. [`L2|SE0000869646|C4`] [V] «Stockholm, 24 October 2017 Lennart Evrell President & CEO»
   Anys: 2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Evrell signa com a President & CEO l'informe intermedi el 24/10/2017 · URL: https://investors.boliden.com/sites/boliden-ir/files/pr/201710247984-1.pdf · Wayback: https://web.archive.org/web/20260512121618/https://investors.boliden.com/sites/boliden-ir/files/pr/201710247984-1.pdf (existent; cita no verificada a la captura)

5. [`L2|SE0000869646|C5`] [V] «Mikael Staffas has been appointed as the new President and CEO of Boliden. He will take up the position on 1 June 2018.»
   Anys: 2017 · funció: `context` · allotjament: `emissor` · nivell A · prova: El successor no pren el càrrec fins a l'1/6/2018; per tant no hi ha canvi de CEO abans d'aquesta data · URL: https://investors.boliden.com/sites/boliden-ir/files/pr/201803060710-1.pdf · Wayback: https://web.archive.org/web/20241208132648/https://investors.boliden.com/sites/boliden-ir/files/pr/201803060710-1.pdf (existent; cita no verificada a la captura)

6. [`L2|SE0000869646|C6`] [V] «take over the leadership of Boliden. I will miss you all. Lennart Evrell President & CEO»
   Anys: 2017 · funció: `ceo` · allotjament: `emissor` · nivell A · prova: Evrell signa com a President & CEO la carta de l'informe anual de l'exercici 2017 (inclou el 31/10/2017) · URL: https://investors.boliden.com/sites/boliden-ir/files/pr/201803060710-1.pdf · Wayback: https://web.archive.org/web/20241208132648/https://investors.boliden.com/sites/boliden-ir/files/pr/201803060710-1.pdf (existent; cita no verificada a la captura)


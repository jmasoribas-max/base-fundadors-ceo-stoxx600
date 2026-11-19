# Registre de canvis

Data d'aquest arbre: 19/11/2026 10:12 (CET, Europe/Madrid). Base: `dades/base_isin_any_v8r3.csv` SHA `1b7df913b31300857cbc77332a9aa03626edc0013f3bbb1e8625aa456ee38d4c` [V].

La v8 r3 **no afegeix canvis d'etiqueta FounderCEO**. El registre que segueix és el de la v8 r1 (cites amb URL original i Wayback). La v8 r3 aplica l'extensió del supersector de juny 2023 als anys 2024-2025 per als ISIN que ja el tenien (`sector_estes_des_2023=1`) i afegeix `supersector_fix`; no canvia cap etiqueta FounderCEO. Qualsevol canvi futur de dades s'ha d'afegir aquí amb cita literal, URL i Wayback, en una branca i via PR.

Proposta posterior, pendent del flux (DF, Doctorat, Jordi): vegeu al final «Lot ND-1 (proposta de Claude Code)».

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

Columna modificada a `dades/base_isin_any_v8r3.csv` a les 8 files: **només `FounderCEO`** (no_determinat → 0). Correcció de DF (19/11/2026): la resta de columnes (`founderceo_rob_*`, `regles`, `motiu_nd`, `detall_motiu_nd`, `sim_*`, `a_mostra_principal`, `sense_fundador_transformador`...) queden amb el valor de `main` i les recalcula DF amb els seus scripts; el `.xlsx` és el de `main` (el regenera DF).

Comptes de `FounderCEO` si s'aprova: F 343, P 5.632 (+8), ND 6 (−8), NA 31. Els comptes de les mostres i de robustesa (J14 i altres) els recalcula DF. La certificació no canvia.

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


# Registre de canvis

Data d'aquest arbre: 19/11/2026 10:12 (CET, Europe/Madrid). Base: `dades/base_isin_any_v8r3.csv` SHA `1b7df913b31300857cbc77332a9aa03626edc0013f3bbb1e8625aa456ee38d4c` [V].

La v8 r3 **no afegeix canvis d'etiqueta FounderCEO**. El registre que segueix és el de la v8 r1 (cites amb URL original i Wayback). La v8 r3 aplica l'extensió del supersector de juny 2023 als anys 2024-2025 per als ISIN que ja el tenien (`sector_estes_des_2023=1`) i afegeix `supersector_fix`; no canvia cap etiqueta FounderCEO. Qualsevol canvi futur de dades s'ha d'afegir aquí amb cita literal, URL i Wayback, en una branca i via PR.

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

# Lot 2 (proposta de Claude Code): cites del CEO a 31/10 per a les 108 files `ceo_pendent`

Data: 19/11/2026. Branca `cas/ceo-pendent-lot2`. **Proposta pendent del flux DF → Doctorat → Jordi; no s'autodeclara cap certificació.**

- Abast: les 108 files amb `sim_estat_certificacio=certificada_ceo_pendent` (28 ISIN).
- **Cap canvi a `dades/`**: el CEO de la base queda confirmat a les 108 files i l'etiqueta FounderCEO no es toca. No s'ha modificat cap columna de robustesa (`founderceo_rob_*`, `sim_*`), ni regles, ni `motiu_nd`, ni el `.xlsx`.
- Què s'afegeix: 260 cites literals (files `tipus=evidencia_ceo`, id `L2|ISIN|cita` a `docs/REGISTRE_CANVIS.csv`) de fonts A/B obertes a la URL original, i les mateixes cites a cada fitxa.
- Verificació: cada cita s'ha comprovat literalment per script al document baixat de la URL original (text de PDF o HTML; espais, lligadures i guionets tous normalitzats) i s'ha tornat a baixar i comprovar en una segona passada independent que intentava refutar el CEO. Cap còpia de tercers s'ha fet servir com a prova.
- Wayback: 175 de 260 cites tenen una captura existent segons l'API de disponibilitat d'archive.org; la resta queda `pendent_verificacio_externa`. `web.archive.org` no era accessible des de la sessió: cap cita s'ha pogut comprovar a la captura (`cita_verificada_a_captura=no`) ni s'ha pogut demanar cap captura nova.
- Efecte esperat sobre la certificació: si DF valida les cites i Doctorat accepta el criteri de prova, les files podrien passar de `certificada_ceo_pendent` a `certificada` amb el mateix nivell (N1/N2). Ho decideix el flux.
- Regla del CEO: R1 (títol de CEO o equivalent legal) a totes les files, tret d'Ericsson 2016 i BBA Aviation 2017 (R2, CEO interí).

| ISIN | Empresa | Anys | CEO a 31/10 (sense canvi) | Cites | Nivells |
|---|---|---|---|---|---|
| `BE0974259880` | D'Ieteren Group S.A. Parts Sociales au Port. | 2022 | Francis Deprez | 5 | A |
| `CH0008837566` | Allreal Holdings AG Namens-Aktien SF 1,00 | 2019-2022 | Roger Herzog | 9 | A, B |
| `CH1243598427` | Sandoz Group AG Namens-Aktien SF -,05 | 2023-2025 | Richard Saynor | 8 | A |
| `DE0007100000` | Mercedes-Benz Group AG Namens-Aktien | 2019-2025 | Ola Källenius | 17 | A |
| `DE000A2E4K43` | Delivery Hero SE Namens-Aktien o.N. | 2018-2025 | Niklas Östberg | 14 | A |
| `DE000LED4000` | OSRAM Licht AG Namens-Aktien o.N.2) | 2016-2019 | Olaf Berlien | 7 | A |
| `DK0010181759` | Carlsberg AS Navne-Aktier B DK 20 | 2016-2022 | Cees ’t Hart | 15 | A |
| `DK0060227585` | Christian Hansen Holding AS Navne-Aktier | 2016-2017 | Cees de Jong | 9 | A |
| `ES0113307021` | BANKIA S.A. Acciones Nominativas EO 0,8 | 2016 | José Sevilla Álvarez | 6 | A, B |
| `FR0000071946` | Alten S.A. Actions au Porteur EO 1,05 | 2018-2024 | Simon Azoulay | 12 | A |
| `FR0000121667` | Essilor Intl -Cie Génle Opt.SA Actions Port. | 2016-2017 | Hubert Sagnières | 7 | A |
| `GB0006731235` | Associated British Foods PLC Registered | 2016-2025 | George Weston | 21 | A, B |
| `GB0008847096` | Tesco PLC Registered Shares LS -,05 | 2016-2018 | Dave Lewis | 9 | A, B |
| `GB0009292243` | Victrex PLC Registered Shares LS -,01 | 2018-2022 | Jakob Sigurdsson | 8 | A |
| `GB0009633180` | Dechra Pharmaceuticals PLC Registered | 2018-2023 | Ian Page | 10 | A, B |
| `GB0034264548` | Paysafe Group PLC Registered Shares LS | 2016-2017 | Joel Leonoff | 10 | A |
| `GB00B17BBQ50` | Investec PLC Registered Shares LS -,00022) | 2016-2017 | Stephen Koseff | 5 | A |
| `GB00B1FP8915` | BBA Aviation PLC Registered Shares LS | 2017 | Wayne Edmunds | 10 | A, B |
| `GB00B1KJJ408` | Whitbread PLC Reg. Shares LS -,76797385 | 2016-2020, 2022 | Alison Brittain | 20 | A |
| `GB00B2B0DG97` | Relx PLC Registered Shares LS -,144397 | 2016-2025 | Erik Engstrom | 16 | A |
| `GB00B71N6K86` | Evraz PLC Registered Shares DL 0,05 | 2018-2020 | Alexander Frolov | 3 | A |
| `GB00B7T77214` | NatWest Group PLC Registered Shares LS 1 | 2020-2021 | Alison Rose | 6 | A |
| `GB00BGXQNP29` | Phoenix Group Holdings PLC Registered | 2020-2025 | Andy Briggs | 8 | A |
| `GB00BNC5T391` | Deliveroo PLC Registered Shares | 2021 | Will Shu | 6 | A |
| `JE00B8KF9B49` | WPP PLC Registered Shares LS -,10 | 2025 | Cindy Rose | 7 | A |
| `NL0011821392` | Signify N.V. Registered Shares EO -,01 | 2022 | Eric Rondolat | 2 | A |
| `SE0000108656` | Ericsson Namn-Aktier B (fria) o.N. | 2016 | Jan Frykhammar | 4 | A, B |
| `SE0000869646` | Boliden AB Namn-Aktier SK 2 | 2016-2017 | Lennart Evrell | 6 | A |

### L2.1 D'Ieteren Group S.A. Parts Sociales au Port. (`BE0974259880`)

- isin i anys: `BE0974259880`, 2022 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Francis Deprez → Francis Deprez (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Web oficial de l'emissor: https://www.dieterengroup.com/history/ (200, sense menció de Deprez al text), https://www.dieterengroup.com/annual-reports/ (200, índex d'informes 2015-2025), https://www.dieterengroup.com/annual-reports/annual-report-2022/ (200; enllaça els PDF) i https://www.dieterengroup.com/annual-reports/annual-report-2021/ (200). PDF baixats dels enllaços oficials (dieterengroup.imgix.net, CDN de la web de l'emissor): informe financer 2022 (200, 4,6 MB), informe integrat 2022 (200, 8,3 MB), informe financer 2021 (200, 4,3 MB). https://www.dieterengroup.com/financial-reports/ va donar 404. La llista de comunicats https://www.dieterengroup.com/press-releases/?page=N es pagina amb JavaScript i sempre torna la primera pàgina, de manera que no s'han pogut localitzar comunicats de 2022 ni el comunicat de nomenament de 2019; no ha calgut perquè els informes anuals cobreixen l'interval. No s'ha fet servir cap font de tercers.
- Dubtes de metodologia per a Doctorat (no decidits): (1) No hi ha cap frase que digui literalment que Deprez era CEO el 31/10/2022: la prova és per interval (CEO el 31/12/2021 i el 31/12/2022, inici de mandat com a CEO el 2019, exercici natural). Doctorat ha de decidir si aquest acotament amb dos informes anuals consecutius és suficient. · (2) Les cites C1, C2 i C5 provenen de taules del PDF: el text extret per pdftotext és contigu, però l'associació nom-càrrec-any d'inici depèn de la disposició en columnes (a la versió -layout '2019 (as CEO)' apareix a la fila de Francis Deprez). · (3) Els PDF són al domini dieterengroup.imgix.net (CDN d'imatges/documents enllaçat des de la web oficial dieterengroup.com), no al domini dieterengroup.com mateix; s'ha tractat com a web oficial de l'emissor (nivell A).
- Cites:

1. [`L2|BE0974259880|C1`] [V] «Composition of the Executive Committee on 31 December 2022 Francis Deprez (57) Arnaud Laviolette (61) Chairman of the Executive Committee and CEO»
   Anys: 2022 · Nivell A · prova: Francis Deprez era president del Comitè Executiu i CEO el 31/12/2022 · URL: https://dieterengroup.imgix.net/annual-reports/INTERACTIF-RAPPORT-FINANCIER-2022-ENG_2023-06-09-094530_rscg.pdf · Wayback: `pendent_verificacio_externa`

2. [`L2|BE0974259880|C2`] [V] «Start of mandate 2019 (as CEO)»
   Anys: 2022 · Nivell A · prova: A la taula del Comitè Executiu, l'inici de mandat de Francis Deprez com a CEO és 2019 (la columna correspon a la seva fila; el text extret és d'una taula) · URL: https://dieterengroup.imgix.net/annual-reports/INTERACTIF-RAPPORT-FINANCIER-2022-ENG_2023-06-09-094530_rscg.pdf · Wayback: `pendent_verificacio_externa`

3. [`L2|BE0974259880|C3`] [V] «Two members Francis Deprez: CEO Arnaud Laviolette: CFO»
   Anys: 2022 · Nivell A · prova: Francis Deprez figura com a CEO del grup a l'informe integrat de l'exercici 2022 · URL: https://dieterengroup.imgix.net/annual-reports/INTEGRATED-REPORT-2022-ENG-VFF.pdf · Wayback: https://web.archive.org/web/20230628173924/https://dieterengroup.imgix.net/annual-reports/INTEGRATED-REPORT-2022-ENG-VFF.pdf (existent; cita no verificada a la captura)

4. [`L2|BE0974259880|C4`] [V] «Composition of the Executive Committee on 31 December 2021 Francis Deprez (56)»
   Anys: 2022 · Nivell A · prova: Francis Deprez ja era membre del Comitè Executiu el 31/12/2021 (límit inferior de l'interval) · URL: https://dieterengroup.imgix.net/annual-reports/RAPPORT-FINANCIER-2021-ENG-INTERACTIF-21-6-22.pdf · Wayback: `pendent_verificacio_externa`

5. [`L2|BE0974259880|C5`] [V] «Start of mandate Chairman of the Executive Committee and CEO»
   Anys: 2022 · Nivell A · prova: A la mateixa taula del 31/12/2021 (C4), el càrrec de Francis Deprez és Chairman of the Executive Committee and CEO (text extret de taula: 'Start of mandate' és una capçalera de columna adjacent) · URL: https://dieterengroup.imgix.net/annual-reports/RAPPORT-FINANCIER-2021-ENG-INTERACTIF-21-6-22.pdf · Wayback: `pendent_verificacio_externa`

### L2.2 Allreal Holdings AG Namens-Aktien SF 1,00 (`CH0008837566`)

- isin i anys: `CH0008837566`, 2019-2022 (n=4). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Roger Herzog → Roger Herzog (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A, B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Web oficial de l'emissor: https://www.allreal.ch/ , /en/ , /investoren/berichte-und-praesentationen/ i /en/investors-and-media/reporting/sustainability-report-2025/governance -> HTTP 403 (pàgina de desafiament de Cloudflare 'Just a moment...'), no és evidència. Subdominis oficials amb els informes anuals: https://ir.allreal.ch/{en,de}/gb2019..gb2023/management-report/organisation/group-management.html i https://ir.allreal.ch/ -> 'CONNECT tunnel failed, response 502' en tots els intents; https://nachhaltigkeit.allreal.ch/fileadmin/user_upload/redakteure/GB{2019..2023}/PDF/{EN,DE}/Allreal-Kompletter-Geschaeftsbericht-*.pdf i https://nachhaltigkeit.allreal.ch/ -> 502; reports.allreal.ch, report.allreal.ch, geschaeftsbericht.allreal.ch -> 502. Cap informe anual de l'emissor s'ha pogut obrir. Registre oficial: Zefix REST (https://www.zefix.ch/ZefixREST/api/v1/firm/search.json i /firm/462500.json) -> 200, amb les publicacions SHAB des de 2016 (cita c1); l'extracte cantonal https://zh.chregister.ch/cr-portal/auszug/auszug.xhtml?uid=CHE-101.079.312 -> 200 però el contingut es carrega amb JavaScript i no s'hi veu cap persona. La inscripció inicial de Herzog (2015) queda fora de l'historial que serveix Zefix. Premsa: moneycab.com (200) - articles del 26.02.2015, 09.09.2015, 12.02.2020, 14.07.2022 i 27.10.2022 (cites c2-c5, c7-c9), més articles de resultats 2019-2023 que no esmenten el CEO al text; newsroom oficial de Flughafen Zürich (200, c6). immobilienbusiness.ch -> 403; realassets.ipe.com -> 405; finews.ch cerca -> 404; cash.ch i nzz.ch cerques -> 200 sense resultats útils; broker.zkb.ch -> redirigeix al calendari genèric. Descartats com a prova (només pista): marktpuls.ch (còpia de tercers del comunicat d'Allreal del 26.02.2015, que diu 'per 1. Mai 2015'), immo-invest.ch (reproducció del comunicat del 15.07.2022), MarketScreener, i els peus de foto 'Allreal-CEO Roger Herzog' de Moneycab (metadada d'imatge reutilitzada, no contemporània).
- Dubtes de metodologia per a Doctorat (no decidits): (1) Els anys 2019 i 2021 es proven per interval (inici maig 2015; 'ab 2015 Konzernchef' en un article del 14.07.2022; baixa al registre mercantil el 2023) i no amb un document contemporani de l'emissor, perquè la web oficial i els subdominis dels informes anuals no s'han pogut obrir (403/502). Doctorat ha de decidir si aquesta prova d'interval amb fonts A (registre) + B (premsa) és suficient o si cal l'informe anual de cada exercici. · (2) Nivell de Moneycab: s'ha classificat com a B (portal suís de notícies econòmiques, sovint amb textos d'agència AWP). Cal validar que compta com a premsa econòmica de qualitat. · (3) El comunicat de Flughafen Zürich AG (c6) és un document oficial d'una empresa tercera, no de l'emissor; s'ha etiquetat B i no A. Cal confirmar el nivell. · (4) La cita del registre mercantil (c1) prova el càrrec 'Vorsitzender der Geschäftsleitung' (equivalent legal de CEO) i la data de publicació de la baixa (SHAB 01.06.2023, diari 26.05.2023), però no la data efectiva de sortida; la premsa diu final de març de 2023 per a Herzog i maig de 2023 per a Widrig. Això pot implicar un mes (abril 2023) sense CEO documentat o amb interí; no afecta cap 31/10 però convé saber-ho per a la fila 2023 (fora d'aquest lot). · (5) La data d'inici exacta (1 de maig de 2015) només s'ha vist en una còpia de tercers del comunicat (marktpuls.ch), no usada com a prova; les cites obertes diuen 'Anfang Mai' 2015.
- Cites:

1. [`L2|CH0008837566|c1`] [V] «Ausgeschiedene Personen und erloschene Unterschriften: Herzog, Roger, von Zürich, in Zürich, Vorsitzender der Geschäftsleitung, mit Kollektivunterschrift zu zweien. Eingetragene Personen neu oder mutierend: Widrig, Stephan, von Bad Ragaz, in Wallisellen, Vorsitzender der Geschäftsleitung, mit Kollektivunterschrift zu zweien.»
   Anys: 2019-2022 · Nivell A · prova: Fi del mandat: Roger Herzog consta inscrit com a Vorsitzender der Geschäftsleitung (CEO) d'Allreal Holding AG fins a la mutació publicada l'01.06.2023, en què el substitueix Stephan Widrig. Per tant no va ser substituït abans de 2023. · URL: https://www.zefix.ch/ZefixREST/api/v1/firm/462500.json · Wayback: `pendent_verificacio_externa`

2. [`L2|CH0008837566|c2`] [V] «Zunächst war er Finanzchef und ab 2015 Konzernchef.»
   Anys: 2019-2021 · Nivell B · prova: Interval: el juliol de 2022 la premsa descriu Herzog com a Konzernchef (CEO) des de 2015, sense interrupció. · URL: https://www.moneycab.com/schweiz/allreal-ceo-roger-herzog-tritt-im-fruehjahr-2023-zurueck/ · Wayback: https://web.archive.org/web/20250807071308/https://www.moneycab.com/schweiz/allreal-ceo-roger-herzog-tritt-im-fruehjahr-2023-zurueck/ (existent; cita no verificada a la captura)

3. [`L2|CH0008837566|c3`] [V] «Konzernchef Roger Herzog gibt seine Funktion als CEO im Frühjahr 2023 ab.»
   Anys: 2021-2022 · Nivell B · prova: El 14.07.2022 Herzog és el CEO en exercici i la sortida s'anuncia per a la primavera de 2023 (posterior al 31/10/2022). · URL: https://www.moneycab.com/schweiz/allreal-ceo-roger-herzog-tritt-im-fruehjahr-2023-zurueck/ · Wayback: https://web.archive.org/web/20250807071308/https://www.moneycab.com/schweiz/allreal-ceo-roger-herzog-tritt-im-fruehjahr-2023-zurueck/ (existent; cita no verificada a la captura)

4. [`L2|CH0008837566|c4`] [V] «Bis zu seinem Austritt im Frühjahr 2023 werde Herzog seine Aufgaben als CEO unverändert wahrnehmen»
   Anys: 2022 · Nivell B · prova: Continuïtat anunciada com a CEO fins a la primavera de 2023. · URL: https://www.moneycab.com/schweiz/allreal-ceo-roger-herzog-tritt-im-fruehjahr-2023-zurueck/ · Wayback: https://web.archive.org/web/20250807071308/https://www.moneycab.com/schweiz/allreal-ceo-roger-herzog-tritt-im-fruehjahr-2023-zurueck/ (existent; cita no verificada a la captura)

5. [`L2|CH0008837566|c5`] [V] «Ab Mai 2023 wird Widrig bei Allreal das Zepter führen. Er löst dort Roger Herzog ab, wie Allreal in einer eigenen Mitteilung schreibt. Der Rücktritt von Herzog per Ende März 2023 wurde allerdings bereits im Juli kommuniziert.»
   Anys: 2022 · Nivell B · prova: El 27.10.2022 (4 dies abans del 31/10/2022) el successor encara no ha entrat: Widrig comença el maig de 2023 i Herzog plega a final de març de 2023. · URL: https://www.moneycab.com/schweiz/flughafenzuerich-verliert-ceo-stephan-widrig-an-allreal/ · Wayback: https://web.archive.org/web/20260213172944/https://www.moneycab.com/schweiz/flughafenzuerich-verliert-ceo-stephan-widrig-an-allreal/ (existent; cita no verificada a la captura)

6. [`L2|CH0008837566|c6`] [V] «From May 2023, Stephan Widrig will be CEO of Allreal Holding AG, one of the largest listed real estate companies in Switzerland. He will therefore be leaving Flughafen Zürich AG at the end of April 2023.»
   Anys: 2022 · Nivell B · prova: Widrig no és CEO d'Allreal fins al maig de 2023; el 31/10/2022 encara és CEO de Flughafen Zürich. · URL: https://www.flughafen-zuerich.ch/newsroom/en/change-in-the-management-board-of-flughafen-zuerich-ag/ · Wayback: https://web.archive.org/web/20231207112746/https://www.flughafen-zuerich.ch/newsroom/en/change-in-the-management-board-of-flughafen-zuerich-ag/ (existent; cita no verificada a la captura)

7. [`L2|CH0008837566|c7`] [V] «Er übernimmt diese Aufgabe von CEO Roger Herzog, welcher die Sparte bisher direkt geleitet hat.»
   Anys: 2019-2020 · Nivell B · prova: Document contemporani: el 12.02.2020 Roger Herzog és el CEO d'Allreal. · URL: https://www.moneycab.com/schweiz/allreal-simon-raebsamen-wird-neuer-leiter-realisation/ · Wayback: https://web.archive.org/web/20250807164849/https://www.moneycab.com/schweiz/allreal-simon-raebsamen-wird-neuer-leiter-realisation/ (existent; cita no verificada a la captura)

8. [`L2|CH0008837566|c8`] [V] «Bettoni leitet das Unternehmen seit der Gründung im Jahr 1999 und wird dies noch bis Anfang Mai tun, wie Allreal am Donnerstag mitteilt. Dann übernimmt Herzog.»
   Anys: 2019-2021 · Nivell B · prova: Inici del mandat: Herzog assumeix la direcció a principis de maig de 2015. · URL: https://www.moneycab.com/?p=1064109 · Wayback: `pendent_verificacio_externa`

9. [`L2|CH0008837566|c9`] [V] «Herr Herzog, nach zehn Jahren als Finanzchef von Allreal haben Sie Anfang Mai die Führung des Unternehmens übernommen.»
   Anys: 2019-2021 · Nivell B · prova: Inici efectiu del mandat: principis de maig de 2015. · URL: https://www.moneycab.com/?p=1054743 · Wayback: `pendent_verificacio_externa`

### L2.3 Sandoz Group AG Namens-Aktien SF -,05 (`CH1243598427`)

- isin i anys: `CH1243598427`, 2023-2025 (n=3). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Richard Saynor → Richard Saynor (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Web oficial sandoz.com: sitemap-root.xml (200) per localitzar pàgines; /investors/annual-report/ (200) dona el PDF de l'informe 2025 (200). Informes 2024 i 2023: diversos noms provats sota sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/ (Sandoz%20Integrated%20Annual%20Report%202024.pdf, ...2023.pdf, variants _0 i amb guions) van donar 404; les URL bones es van localitzar per WebSearch (pista): Sandoz_2024_annual_report.pdf (200) i prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf (200, redirigeix a static-my-sandoz-com.cms.sandoz.com). També baixats de sandoz.com: biografia de Saynor, comunicats 9M 2023 (24/10/2023) i 9M 2024 (30/10/2024). URL que van donar 404: sandoz.com/annual-report-2023/, /about-us/leadership/, /investors/financial-reports-and-publications/. La pista de Novartis (comunicat de l'spin-off) es va baixar (200) però no esmenta Saynor.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Les cites proven el càrrec a 31/12 de cada any i que Saynor dirigeix Sandoz 'since 2019' (literal 'has led Sandoz', no 'CEO since'); la continuïtat el 31/10 es dedueix de l'interval, no d'una frase amb aquesta data exacta. Per al 2023 i el 2025 no s'ha inclòs cap document datat exactament a l'entorn del 31/10 (el comunicat 9M 2023, del 24/10/2023, el signa com 'Richard Saynor - CEO Sandoz', però no s'ha fet servir com a cita). · (2) El PDF de l'informe 2023 és en un domini de Sandoz diferent de sandoz.com (prod.cms.static.my-sandoz.com, que redirigeix a static-my-sandoz-com.cms.sandoz.com); s'ha tractat com a web oficial de l'emissor (nivell A). · (3) L'informe 2023 situa l'spin-off de Sandoz el 4/10/2023 ('On October 4, 2023, we celebrated a successful spin-off'); la frase 'has led Sandoz since 2019' es refereix, doncs, també al període anterior a la cotització independent. No afecta el 31/10 de 2023-2025, però Doctorat pot voler decidir com es llegeix 'since 2019'.
- Cites:

1. [`L2|CH1243598427|C2023a`] [V] «As of December 31, 2023, the Sandoz Executive Committee was composed of the following individuals: Executive Committee Richard Saynor Chief Executive Officer»
   Anys: 2023 · Nivell A · prova: Richard Saynor era Chief Executive Officer de Sandoz el 31/12/2023 · URL: https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf · Wayback: https://web.archive.org/web/20240829080930/https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf (existent; cita no verificada a la captura)

2. [`L2|CH1243598427|C2023b`] [V] «Richard Saynor has led Sandoz since 2019, offering a proven track record as a senior leader»
   Anys: 2023 · Nivell A · prova: Saynor dirigeix Sandoz de manera continuada des del 2019 (inici de l'interval) · URL: https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf · Wayback: https://web.archive.org/web/20240829080930/https://prod.cms.static.my-sandoz.com/ar/sandoz2023-12March2024-V2/documents/2023-Integrated-Annual-Report.pdf (existent; cita no verificada a la captura)

3. [`L2|CH1243598427|C2024a`] [V] «As of December 31, 2024, the Sandoz Executive Committee was composed of the following individuals: Richard Saynor Chief Executive Officer»
   Anys: 2024 · Nivell A · prova: Richard Saynor era Chief Executive Officer de Sandoz el 31/12/2024 · URL: https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz_2024_annual_report.pdf · Wayback: https://web.archive.org/web/20260624233323/https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz_2024_annual_report.pdf (existent; cita no verificada a la captura)

4. [`L2|CH1243598427|C2024b`] [V] «Richard Saynor has led Sandoz since 2019, offering a proven track record as a senior leader»
   Anys: 2024 · Nivell A · prova: Saynor dirigeix Sandoz de manera continuada des del 2019 (inici de l'interval) · URL: https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz_2024_annual_report.pdf · Wayback: https://web.archive.org/web/20260624233323/https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz_2024_annual_report.pdf (existent; cita no verificada a la captura)

5. [`L2|CH1243598427|C2024c`] [V] «Richard Saynor, Chief Executive Officer of Sandoz, said:»
   Anys: 2024 · Nivell A · prova: Saynor signava com a CEO en el comunicat del 30/10/2024, la vigília de la data de referència · URL: https://www.sandoz.com/sandoz-reports-third-quarter-and-nine-month-2024-sales/ · Wayback: https://web.archive.org/web/20260424070914/https://www.sandoz.com/sandoz-reports-third-quarter-and-nine-month-2024-sales/ (existent; cita no verificada a la captura)

6. [`L2|CH1243598427|C2025a`] [V] «As of December 31, 2025, the Sandoz Executive Committee was composed of the following individuals: Richard Saynor Chief Executive Officer»
   Anys: 2025 · Nivell A · prova: Richard Saynor era Chief Executive Officer de Sandoz el 31/12/2025 · URL: https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf · Wayback: https://web.archive.org/web/20261107224146/https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf (existent; cita no verificada a la captura)

7. [`L2|CH1243598427|C2025b`] [V] «Richard Saynor has led Sandoz since 2019, offering a proven track record as a senior leader»
   Anys: 2025 · Nivell A · prova: Saynor dirigeix Sandoz de manera continuada des del 2019 (inici de l'interval) · URL: https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf · Wayback: https://web.archive.org/web/20261107224146/https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf (existent; cita no verificada a la captura)

8. [`L2|CH1243598427|C2025c`] [V] «Changes to the Executive Committee in 2025 Peter Stenico, former Global Platform Head Biosimilars and Country President Austria, was appointed President Region International effective March 1, 2025, succeeding Francisco Ballester who retired from his position as of February 28, 2025.»
   Anys: 2025 · Nivell A · prova: L'únic canvi al Comitè Executiu el 2025 que informa l'apartat no afecta el CEO · URL: https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf · Wayback: https://web.archive.org/web/20261107224146/https://sandoz-com.cms.sandoz.com/sites/default/files/Media%20Documents/Sandoz%20Integrated%20Annual%20Report%202025.pdf (existent; cita no verificada a la captura)

### L2.4 Mercedes-Benz Group AG Namens-Aktien (`DE0007100000`)

- isin i anys: `DE0007100000`, 2019-2025 (n=7). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Ola Källenius → Ola Källenius (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Web oficial de l emissor group.mercedes-benz.com: 403 'Access Denied' (Akamai) a tot el que s ha provat: informes anuals 2019-2020 (/documents/investors/reports/annual-report/daimler/daimler-ir-annual-report-<any>-incl-combined-management-report-daimler-ag.pdf), 2021-2025 (/mercedes-benz/mercedes-benz-ir-annual-report-<any>-incl-combined-management-report-mbg-ag.pdf; URL construïdes per patró, no confirmades), la fitxa /company/corporate-governance/board-of-management/kaellenius/ i /company/news/231213-reappointment-kohleisen-burzer.html. www.daimler.com: error de handshake TLS. annualreport.daimler.com i annualreport.mercedes-benz.com: 502 del proxy (CONNECT). www.mercedes-benz.com: 403. media.mercedes-benz.com: 200 però és una SPA sense contingut al HTML (cerca no utilitzable). businesswire.com (comunicat 27/07/2023): error HTTP/2, no obert. sec.gov: 403. Font oberta: media.mercedes-benz.it (sala de premsa oficial de Mercedes-Benz Italia S.p.A., filial del grup), que republica els comunicats del grup en anglès; localitzats amb el seu sitemap.xml i WebSearch (només com a pista). Baixats i verificats amb vq.py: comunicats de 26/09/2018, 23/05/2019, 14/11/2019, 23/07/2020, 06/10/2020, 29/01/2021, 30/07/2021, 03/12/2021, 29/04/2022, 17/02/2023, 27/07/2023 (PDF), 22/02/2024, 11/12/2024 i 29/10/2025 (PDF). També baixats però no usats com a cita: comunicats de resultats T3 de 23/10/2020, 29/10/2021 i 26/10/2022 (el text HTML no anomena Källenius; els .docx adjunts de 2020 i 2021 porten al peu 'Board of Management: Ola Källenius, Chairman;' però vq.py no llegeix .docx, i el .docx de 2022 no s ha inspeccionat), el PDF de T3 del 25/10/2024 (només cita el CFO), i prnewswire.com 10/02/2017 (pròrroga de contracte com a vocal, anterior al període). No s ha pogut obrir cap informe anual 2019-2025.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Totes les cites provenen de media.mercedes-benz.it (sala de premsa de Mercedes-Benz Italia S.p.A.; el peu del web diu '© Mercedes-Benz Italia S.p.A. All rights reserved.'), no de la web de l emissor group.mercedes-benz.com, que retorna 403 des d aquí. S han classificat com a nivell A (document de l empresa en un web oficial del grup); Doctorat ha de decidir si una sala de premsa d una filial compta com a 'web oficial de l emissor' o si cal reobrir els informes anuals a group.mercedes-benz.com des d una altra xarxa. · (2) Cap any està cobert per l informe anual; s han usat comunicats de premsa datats abans i després de cada 31/10 (prova per interval) més les cites de mandat (nomenament 2018 per cinc anys des de la junta del 22/05/2019; renovació 27/07/2023 fins al 21/05/2029). La data de cada comunicat HTML és la que mostra la pàgina de la sala de premsa italiana. · (3) 2025: l única prova contemporània és del 29/10/2025 (dos dies abans del 31/10); la continuïtat al 31/10/2025 es recolza en la renovació fins al 21/05/2029, sense document posterior obert. · (4) Els comunicats alternen 'Chairman of the Board of Management' i 'Chief Executive Officer' (i les grafies Källenius/Kaellenius) per a la mateixa persona; s han tractat com a equivalents (Vorstandsvorsitzender). · (5) L emissor va canviar de nom de Daimler AG a Mercedes-Benz Group AG el febrer de 2022 (comunicat baixat a it_2022_02_01.html, no citat); el nom al panell continua sent Daimler AG.
- Cites:

1. [`L2|DE0007100000|c01`] [V] «the Supervisory Board of Daimler AG therefore decided to appoint Ola Källenius for a new term of five years as Chairman of the Board of Management of Daimler AG, effective in direct connection»
   Anys: 2019-2021 · Nivell A · prova: Comunicat del 26/09/2018: nomenament de Källenius com a Vorstandsvorsitzender per cinc anys, amb efecte tot seguit de la sortida de Zetsche al final de la junta general de 2019. · URL: https://media.mercedes-benz.it/daimler-sets-its-course-for-the-future-dieter-zetsche-to-succeed-manfred-bischoff-in-the-supervisory-board--ola-kallenius-to-become-chairman-of-the-board-of-management-of-daimler-ag-in-2019/ · Wayback: https://web.archive.org/web/20210116235438/https://media.mercedes-benz.it/daimler-sets-its-course-for-the-future-dieter-zetsche-to-succeed-manfred-bischoff-in-the-supervisory-board--ola-kallenius-to-become-chairman-of-the-board-of-management-of-daimler-ag-in-2019/ (existent; cita no verificada a la captura)

2. [`L2|DE0007100000|c02`] [V] «Ola Källenius took over from Zetsche at the end of the Annual Shareholders’ Meeting as Chairman of the Board of Management of Daimler AG and Head of Mercedes-Benz Cars.»
   Anys: 2019 · Nivell A · prova: Comunicat datat el 23/05/2019 sobre la junta general: Källenius assumeix la presidència del Vorstand al final de la junta (inici efectiu del mandat, maig de 2019). · URL: https://media.mercedes-benz.it/large-majority-of-daimler-shareholders-approve-new-group-structure-with-daimler-ag-as-parent-company/ · Wayback: https://web.archive.org/web/20240227172537/https://media.mercedes-benz.it/large-majority-of-daimler-shareholders-approve-new-group-structure-with-daimler-ag-as-parent-company/ (existent; cita no verificada a la captura)

3. [`L2|DE0007100000|c03`] [V] «Annual General Meeting of Daimler AG on May 22, 2019 in Berlin.»
   Anys: 2019 · Nivell A · prova: Peu de foto del comunicat datat el 23/05/2019: la junta general de 2019 es va fer el 22/05/2019 (data efectiva del relleu Zetsche -> Källenius, segons c02). · URL: https://media.mercedes-benz.it/large-majority-of-daimler-shareholders-approve-new-group-structure-with-daimler-ag-as-parent-company/ · Wayback: https://web.archive.org/web/20240227172537/https://media.mercedes-benz.it/large-majority-of-daimler-shareholders-approve-new-group-structure-with-daimler-ag-as-parent-company/ (existent; cita no verificada a la captura)

4. [`L2|DE0007100000|c04`] [V] «said Ola Källenius, Chairman of the Board of Management of Daimler AG and Mercedes-Benz AG.»
   Anys: 2019 · Nivell A · prova: Comunicat datat el 14/11/2019 (Capital Market Day): Källenius és Chairman of the Board of Management de Daimler AG; continuïtat després del 31/10/2019. · URL: https://media.mercedes-benz.it/daimler-cuts-costs-and-sets-course-for-the-future/ · Wayback: https://web.archive.org/web/20240301211357/https://media.mercedes-benz.it/daimler-cuts-costs-and-sets-course-for-the-future/ (existent; cita no verificada a la captura)

5. [`L2|DE0007100000|c05`] [V] «Ola Källenius, Chairman of the Board of Management of Daimler AG and Mercedes-Benz AG: “Due to the unprecedented COVID-19 pandemic, we had to endure a challenging quarter.»
   Anys: 2020 · Nivell A · prova: Comunicat datat el 23/07/2020 (resultats T2 2020): Källenius és Chairman of the Board of Management de Daimler AG abans del 31/10/2020. · URL: https://media.mercedes-benz.it/daimler-reports-second-quarter-2020-results/ · Wayback: https://web.archive.org/web/20240301212603/https://media.mercedes-benz.it/daimler-reports-second-quarter-2020-results/ (existent; cita no verificada a la captura)

6. [`L2|DE0007100000|c06`] [V] «stated Ola Källenius, Chairman of the Board of Management of Daimler AG and Mercedes-Benz AG.»
   Anys: 2020 · Nivell A · prova: Comunicat datat el 29/01/2021 (resultats preliminars 2020): continua com a Chairman of the Board of Management de Daimler AG després del 31/10/2020. · URL: https://media.mercedes-benz.it/preliminary-results-for-the-financial-year-2020-significantly-above-guidance-and-market-expectations/ · Wayback: https://web.archive.org/web/20240424231852/https://media.mercedes-benz.it/preliminary-results-for-the-financial-year-2020-significantly-above-guidance-and-market-expectations/ (existent; cita no verificada a la captura)

7. [`L2|DE0007100000|c07`] [V] «Ola Källenius, Chairman of the Board of Management of Daimler AG and Mercedes-Benz AG : “Daimler’s realignment makes one success story into two.»
   Anys: 2021 · Nivell A · prova: Comunicat datat el 30/07/2021: Källenius és Chairman of the Board of Management de Daimler AG abans del 31/10/2021. · URL: https://media.mercedes-benz.it/go-ahead-for-mercedes-benz-cars-and-daimler-truck-as-independent-companies-by-board-of-management-and-supervisory-board/ · Wayback: https://web.archive.org/web/20240229194524/https://media.mercedes-benz.it/go-ahead-for-mercedes-benz-cars-and-daimler-truck-as-independent-companies-by-board-of-management-and-supervisory-board/ (existent; cita no verificada a la captura)

8. [`L2|DE0007100000|c08`] [V] «Ola Källenius, Chief Executive Officer of Daimler AG and Mercedes-Benz AG : “Our goal is technological leadership in the automotive luxury segment»
   Anys: 2021 · Nivell A · prova: Comunicat datat el 03/12/2021: Källenius és Chief Executive Officer de Daimler AG després del 31/10/2021. · URL: https://media.mercedes-benz.it/supervisory-board-confirms-business-plan---mercedes-benz-to-invest-60-billion-euros-into-the-future/ · Wayback: https://web.archive.org/web/20240424221123/https://media.mercedes-benz.it/supervisory-board-confirms-business-plan---mercedes-benz-to-invest-60-billion-euros-into-the-future/ (existent; cita no verificada a la captura)

9. [`L2|DE0007100000|c09`] [V] «said Ola Källenius, Chairman of the Board of Management of Mercedes-Benz Group AG .»
   Anys: 2022 · Nivell A · prova: Comunicat datat el 29/04/2022 (junta general 2022): Källenius és Chairman of the Board of Management de Mercedes-Benz Group AG abans del 31/10/2022. · URL: https://media.mercedes-benz.it/annual-meeting-mercedes-benz-continues-its-successful-transformation/ · Wayback: https://web.archive.org/web/20240422182920/https://media.mercedes-benz.it/annual-meeting-mercedes-benz-continues-its-successful-transformation/ (existent; cita no verificada a la captura)

10. [`L2|DE0007100000|c10`] [V] «said Ola Kaellenius, Chief Executive Officer of Mercedes-Benz Group AG.»
   Anys: 2022 · Nivell A · prova: Comunicat datat el 17/02/2023 (resultats 2022): continua com a CEO de Mercedes-Benz Group AG després del 31/10/2022. · URL: https://media.mercedes-benz.it/mercedes-benz-delivers-strong-full-year-results-in-2022/ · Wayback: https://web.archive.org/web/20240415060830/https://media.mercedes-benz.it/mercedes-benz-delivers-strong-full-year-results-in-2022/ (existent; cita no verificada a la captura)

11. [`L2|DE0007100000|c11`] [V] «The Supervisory Board reappointed Ola Källenius (54) as Chairman of the Board of Management of Mercedes-Benz Group AG until May 21, 2029, at its meeting today.»
   Anys: 2023-2025 · Nivell A · prova: Comunicat del 27/07/2023: renovació de Källenius com a Chairman of the Board of Management fins al 21/05/2029 (cita d interval; en funcions abans del 31/10/2023). · URL: https://media.mercedes-benz.it/download/52b30d94-8c94-4537-83fc-47cba9af5822/20230727-pi-mercedes-benz-entscheidungenar-en-final.pdf · Wayback: https://web.archive.org/web/20240716160203/https://media.mercedes-benz.it/download/52b30d94-8c94-4537-83fc-47cba9af5822/20230727-pi-mercedes-benz-entscheidungenar-en-final.pdf (existent; cita no verificada a la captura)

12. [`L2|DE0007100000|c12`] [V] «contracts of Ola Källenius and Markus Schäfer are due to expire in May 2024.»
   Anys: 2022-2023 · Nivell A · prova: El mandat vigent al juliol de 2023 (el de cinc anys iniciat a la junta de 2019) vencia el maig de 2024. · URL: https://media.mercedes-benz.it/download/52b30d94-8c94-4537-83fc-47cba9af5822/20230727-pi-mercedes-benz-entscheidungenar-en-final.pdf · Wayback: https://web.archive.org/web/20240716160203/https://media.mercedes-benz.it/download/52b30d94-8c94-4537-83fc-47cba9af5822/20230727-pi-mercedes-benz-entscheidungenar-en-final.pdf (existent; cita no verificada a la captura)

13. [`L2|DE0007100000|c13`] [V] «Ola Kaellenius, Chief Executive Officer of Mercedes-Benz Group AG.»
   Anys: 2023-2024 · Nivell A · prova: Comunicat datat el 22/02/2024 (resultats 2023): continua com a CEO després del 31/10/2023 i abans del 31/10/2024. · URL: https://media.mercedes-benz.it/mercedes-benz-group-2023-results-cash-generation-at-work/ · Wayback: https://web.archive.org/web/20240424215755/https://media.mercedes-benz.it/mercedes-benz-group-2023-results-cash-generation-at-work/ (existent; cita no verificada a la captura)

14. [`L2|DE0007100000|c14`] [V] «has elected Ola Källenius, Chairman of the Board of Management of Mercedes-Benz Group AG, as the new ACEA President for 2025.»
   Anys: 2024 · Nivell A · prova: Comunicat datat l 11/12/2024: Källenius és Chairman of the Board of Management de Mercedes-Benz Group AG després del 31/10/2024. · URL: https://media.mercedes-benz.it/acea-ola-kallenius/ · Wayback: `pendent_verificacio_externa`

15. [`L2|DE0007100000|c15`] [V] «Ola Kaellenius, Chief Executive Officer of Mercedes-Benz Group AG»
   Anys: 2025 · Nivell A · prova: Comunicat de resultats del T3 datat el 29/10/2025: Källenius és CEO de Mercedes-Benz Group AG dos dies abans del 31/10/2025. · URL: https://media.mercedes-benz.it/download/9f8e075d-8822-437b-9ca4-46fe7aa7ecd2/20251029_mbgroupag_pressinformation_resultsq3_media.pdf · Wayback: `pendent_verificacio_externa`

16. [`L2|DE0007100000|c16`] [V] «Board of Management: Ola Källenius, Chairman; Jörg Burzer, Renata Jungo Brüngger»
   Anys: 2025 · Nivell A · prova: Peu legal del comunicat del 29/10/2025: Källenius, Chairman del Board of Management. · URL: https://media.mercedes-benz.it/download/9f8e075d-8822-437b-9ca4-46fe7aa7ecd2/20251029_mbgroupag_pressinformation_resultsq3_media.pdf · Wayback: `pendent_verificacio_externa`

17. [`L2|DE0007100000|c17`] [V] «said Ola Källenius, Chairman of the Board of Management of Daimler AG and Mercedes-Benz AG»
   Anys: 2020 · Nivell A · prova: Comunicat datat el 06/10/2020 (Strategy Update): Källenius és Chairman of the Board of Management de Daimler AG tres setmanes abans del 31/10/2020. · URL: https://media.mercedes-benz.it/new-mercedes-benz-strategy-announced---targeting-structurally-higher-profitability/ · Wayback: https://web.archive.org/web/20240228020814/https://media.mercedes-benz.it/new-mercedes-benz-strategy-announced---targeting-structurally-higher-profitability/ (existent; cita no verificada a la captura)

### L2.5 Delivery Hero SE Namens-Aktien o.N. (`DE000A2E4K43`)

- isin i anys: `DE000A2E4K43`, 2018-2025 (n=8). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Niklas Östberg → Niklas Östberg (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: La web ir.deliveryhero.com és una SPA (les pàgines HTML retornen només l'esquelet, 3138 bytes) i www.deliveryhero.com/about/ dona 403; les URL dels PDF s'han localitzat amb WebSearch i amb el patró irpages2.eqs.com/download/companies/delivery/Annual Reports/DE000A2E4K43-JA-<any>-EQ-E-0x.pdf, que redirigeix a ir-api.eqs.com/media/document/<uuid>/...; els mateixos uuid s'han baixat directament del domini oficial https://ir.deliveryhero.com/media/document/<uuid>/assets/... (HTTP 200, application/pdf) i són les URL citades. Baixats: informes anuals 2018 (Final_secured_en.pdf), 2019, 2020, 2021, 2023, 2024, 2025; comptes anuals individuals 2022 (AGM 2023); comunicats Q3 2018 i Q3 2022; també Corporate Governance 2018 i 2022 (no citats). L'informe anual consolidat 2022 no s'ha localitzat (patrons JA-2022-EQ-E-00..06 a irpages2.eqs.com: 404); l'any 2022 es cobreix amb els comptes anuals individuals de la SE i el comunicat Q3 2022.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Els PDF se serveixen a ir.deliveryhero.com/media/document/<uuid>, que és la plataforma IR d'EQS sota el domini oficial de l'emissor; s'ha tractat com a font A (web oficial de l'emissor). · (2) Per a 2019, 2020 i 2025 (C2025a) la cita comença o acaba al costat d'un guionet tou de salt de línia del PDF, i per això el nom de pila 'Niklas' (o la continuació 'Management Board, Chief Executive Officer') queda fora del fragment contigu verificable; el context és inequívoc al document. · (3) Els informes anuals proven el càrrec per a l'exercici sencer, no literalment la data 31/10; només 2018 i 2022 tenen a més un document datat a primers de novembre.
- Cites:

1. [`L2|DE000A2E4K43|C2018a`] [V] «The CEO Niklas Östberg is responsible for the areas Strategy, Operations,»
   Anys: 2018 · Nivell A · prova: Östberg és el CEO durant l'exercici 2018 · URL: https://ir.deliveryhero.com/media/document/af63258d-50e8-4ccc-8ea4-be622a8e5a06/assets/Final_secured_en.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/af63258d-50e8-4ccc-8ea4-be622a8e5a06/assets/Final_secured_en.pdf (existent; cita no verificada a la captura)

2. [`L2|DE000A2E4K43|C2018b`] [V] «Östberg (chair and CEO) and Emmanuel Thomassin (CFO)»
   Anys: 2018 · Nivell A · prova: Östberg president del Vorstand i CEO a l'exercici 2018 · URL: https://ir.deliveryhero.com/media/document/af63258d-50e8-4ccc-8ea4-be622a8e5a06/assets/Final_secured_en.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/af63258d-50e8-4ccc-8ea4-be622a8e5a06/assets/Final_secured_en.pdf (existent; cita no verificada a la captura)

3. [`L2|DE000A2E4K43|C2018c`] [V] «Niklas Östberg, CEO of Delivery Hero, said:»
   Anys: 2018 · Nivell A · prova: Östberg és CEO el 7/11/2018 (contemporani al 31/10/2018) · URL: https://ir.deliveryhero.com/media/document/5d01ee49-4fc6-48ab-a825-0c5ae78259da/assets/DE000A2E4K43-Q3-2018-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/5d01ee49-4fc6-48ab-a825-0c5ae78259da/assets/DE000A2E4K43-Q3-2018-EQ-E-00.pdf (existent; cita no verificada a la captura)

4. [`L2|DE000A2E4K43|C2018d`] [V] «Berlin, 07 November 2018 – Delivery Hero Group»
   Anys: 2018 · Nivell A · prova: Data del comunicat C2018c · URL: https://ir.deliveryhero.com/media/document/5d01ee49-4fc6-48ab-a825-0c5ae78259da/assets/DE000A2E4K43-Q3-2018-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/5d01ee49-4fc6-48ab-a825-0c5ae78259da/assets/DE000A2E4K43-Q3-2018-EQ-E-00.pdf (existent; cita no verificada a la captura)

5. [`L2|DE000A2E4K43|C2019`] [V] «Östberg (Chair and CEO) and Emmanuel Thomassin (CFO)»
   Anys: 2019 · Nivell A · prova: Östberg president del Vorstand i CEO a l'exercici 2019 (el text complet diu 'Niklas Östberg'; la cita comença després del guionet tou de final de línia) · URL: https://ir.deliveryhero.com/media/document/76180021-64c4-4482-b6ab-638acaada132/assets/DE000A2E4K43-JA-2019-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/76180021-64c4-4482-b6ab-638acaada132/assets/DE000A2E4K43-JA-2019-EQ-E-00.pdf (existent; cita no verificada a la captura)

6. [`L2|DE000A2E4K43|C2020`] [V] «Östberg (CEO) and Emmanuel Thomassin (CFO), are personally responsible for managing the Company’s business»
   Anys: 2020 · Nivell A · prova: Östberg CEO a l'exercici 2020 (precedit de 'Niklas' a la línia anterior) · URL: https://ir.deliveryhero.com/media/document/755d9dfe-ac35-4e66-a5c7-37c32cfd69b5/assets/DE000A2E4K43-JA-2020-EQ-E-01.pdf · Wayback: https://web.archive.org/web/20240420045036/https://ir.deliveryhero.com/media/document/755d9dfe-ac35-4e66-a5c7-37c32cfd69b5/assets/DE000A2E4K43-JA-2020-EQ-E-01.pdf (existent; cita no verificada a la captura)

7. [`L2|DE000A2E4K43|C2021`] [V] «Niklas Östberg (CEO) is responsible for the areas Strategy, Operations, Technology, Product, Personnel,»
   Anys: 2021 · Nivell A · prova: Östberg CEO a l'exercici 2021 · URL: https://ir.deliveryhero.com/media/document/35f8a680-3a33-44e4-b1a0-0b750e751b60/assets/DE000A2E4K43-JA-2021-EQ-E-01.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/35f8a680-3a33-44e4-b1a0-0b750e751b60/assets/DE000A2E4K43-JA-2021-EQ-E-01.pdf (existent; cita no verificada a la captura)

8. [`L2|DE000A2E4K43|C2022a`] [V] «The Delivery Hero SE Management Board in financial year 2022 comprised: − Chief Executive Officer Niklas Östberg, businessman, Zollikon, Switzerland – chair of Management Board»
   Anys: 2022 · Nivell A · prova: Östberg CEO i president del Vorstand durant l'exercici 2022 · URL: https://ir.deliveryhero.com/media/document/2b71e5bb-9774-4dfc-aaff-5367c14005a8/assets/AGM%202023_Annual%20Financial%20Statement_Delivery_Hero_SE_2022.pdf · Wayback: https://web.archive.org/web/20231110115552/https://ir.deliveryhero.com/media/document/2b71e5bb-9774-4dfc-aaff-5367c14005a8/assets/AGM%202023_Annual%20Financial%20Statement_Delivery_Hero_SE_2022.pdf (existent; cita no verificada a la captura)

9. [`L2|DE000A2E4K43|C2022b`] [V] «Niklas Östberg, CEO and Co-Founder of Delivery Hero, said:»
   Anys: 2022 · Nivell A · prova: Östberg CEO el 10/11/2022 · URL: https://ir.deliveryhero.com/media/document/c5286361-0cd8-4fc5-97ed-5402ab870e37/assets/DE000A2E4K43-Q3-2022-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20241222143433/https://ir.deliveryhero.com/media/document/c5286361-0cd8-4fc5-97ed-5402ab870e37/assets/DE000A2E4K43-Q3-2022-EQ-E-00.pdf (existent; cita no verificada a la captura)

10. [`L2|DE000A2E4K43|C2023`] [V] «Niklas Östberg (CEO) is responsible for the areas of Strategy, Business Development, Technology, Product, Personnel, Marketing, Payment Solutions,»
   Anys: 2023 · Nivell A · prova: Östberg CEO a l'exercici 2023 · URL: https://ir.deliveryhero.com/media/document/f39e4797-91e8-43f2-82be-e852444a4879/assets/DE000A2E4K43-JA-2023-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20250331005315/https://ir.deliveryhero.com/media/document/f39e4797-91e8-43f2-82be-e852444a4879/assets/DE000A2E4K43-JA-2023-EQ-E-00.pdf (existent; cita no verificada a la captura)

11. [`L2|DE000A2E4K43|C2024`] [V] «SE, Niklas Östberg (Chair of the Management Board, Chief Executive Officer) and Pieter-Jan Vandepitte (Chief Operating Officer) are personally responsible»
   Anys: 2024 · Nivell A · prova: Östberg president del Vorstand i CEO a l'exercici 2024 · URL: https://ir.deliveryhero.com/media/document/c38c7d53-cd6e-44de-8b1f-3559d5c43e6b/assets/DE000A2E4K43-JA-2024-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20260707230924/https://ir.deliveryhero.com/media/document/c38c7d53-cd6e-44de-8b1f-3559d5c43e6b/assets/DE000A2E4K43-JA-2024-EQ-E-00.pdf (existent; cita no verificada a la captura)

12. [`L2|DE000A2E4K43|C2025a`] [V] «In the financial year 2025, Niklas Östberg (Chair of the»
   Anys: 2025 · Nivell A · prova: Östberg president del Vorstand durant l'exercici 2025 (la frase continua 'Management Board, Chief Executive Officer)') · URL: https://ir.deliveryhero.com/media/document/51222150-5c1c-46db-977b-a078706cccdf/assets/DE000A2E4K43-JA-2025-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20260403040123/https://ir.deliveryhero.com/media/document/51222150-5c1c-46db-977b-a078706cccdf/assets/DE000A2E4K43-JA-2025-EQ-E-00.pdf (existent; cita no verificada a la captura)

13. [`L2|DE000A2E4K43|C2025b`] [V] «Niklas Östberg (CEO) oversees Strategy, Business Development,»
   Anys: 2025 · Nivell A · prova: Östberg CEO a l'exercici 2025 · URL: https://ir.deliveryhero.com/media/document/51222150-5c1c-46db-977b-a078706cccdf/assets/DE000A2E4K43-JA-2025-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20260403040123/https://ir.deliveryhero.com/media/document/51222150-5c1c-46db-977b-a078706cccdf/assets/DE000A2E4K43-JA-2025-EQ-E-00.pdf (existent; cita no verificada a la captura)

14. [`L2|DE000A2E4K43|C_int`] [V] «Niklas Östberg was first appointed as a member of the Company’s Management Board in financial year 2017»
   Anys: 2018-2025 · Nivell A · prova: Membre del Vorstand de la SE des de l'exercici 2017 (continuïtat) · URL: https://ir.deliveryhero.com/media/document/51222150-5c1c-46db-977b-a078706cccdf/assets/DE000A2E4K43-JA-2025-EQ-E-00.pdf · Wayback: https://web.archive.org/web/20260403040123/https://ir.deliveryhero.com/media/document/51222150-5c1c-46db-977b-a078706cccdf/assets/DE000A2E4K43-JA-2025-EQ-E-00.pdf (existent; cita no verificada a la captura)

### L2.6 OSRAM Licht AG Namens-Aktien o.N.2) (`DE000LED4000`)

- isin i anys: `DE000LED4000`, 2016-2019 (n=4). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Olaf Berlien → Olaf Berlien (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Exercici fiscal d'OSRAM: 1 d'octubre - 30 de setembre, de manera que cada 31/10 cau al primer mes de l'exercici seguent. Obert amb HTTP 200 a ams-osram.com (web oficial del grup que allotja la seccio 'OSRAM Investor Relations' i l'arxiu de notes de premsa d'OSRAM): /news/press-releases/pr-14-02-2017, pr-09-11-2016, pr-06-11-2017, pr-06-11-2018, pr-12-11-2019, pr-29-11-2017, pr-07-02-2018, pr-14-11-2018, pr-15-11-2018; /about-us/investor-relations/osram-investor-relations (pagina index) i regulatory-news-en-02-23-2021, -02-09-2021, -01-26-2021, -11-06-2018, -11-12-2019, -11-06-2017. 404: pr-07-11-2018, pr-08-11-2018, pr-05-11-2018, regulatory-news-en-11-07-2018, -11-08-2018, -11-09-2016 (URL provades per data, no existeixen). Informes anuals d'OSRAM Licht AG dels exercicis 2017-2020: no n'he trobat cap enllac a la pagina OSRAM Investor Relations ni a financial-results-and-reports d'ams-osram.com (nomes hi ha comptes HGB de 2021 en endavant i documents de junta 2020-2024); www.osram-group.com i www.osram-group.de redirigeixen a ams-osram.com. WebSearch nomes va localitzar una copia de l'informe anual 2017 en un allotjament de tercers (uploads1.craft.co), que no s'ha fet servir. Per aixo la prova es per interval (inici gener 2015, fi 28/02/2021) mes una nota de premsa de l'emissor datada 6-12 dies despres de cada 31/10. Les pistes ams-osram.com/about-us/120-years-of-the-osram-brand i management-kolloquium.de es van baixar (200) pero no s'han fet servir com a prova.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Cap document obert no es l'informe anual de l'exercici que conte el 31/10/t; la cobertura es per interval (C1 inici, C7 fi) mes notes de premsa de l'emissor datades pocs dies despres de cada 31/10. Doctorat ha de decidir si aixo es suficient o si cal l'informe anual. · (2) La data de cada nota de premsa consta a la pagina ('09. November 2016', etc.) i a la URL, pero es massa curta (<25 caracters) per verificar-la amb vq.py com a cita independent. · (3) C1 dona l'inici nomes amb precisio de mes ('January 2015'), sense dia efectiu; no afecta cap 31/10 del panell. · (4) Les fonts son a ams-osram.com (grup matriu que allotja la IR i l'arxiu de premsa d'OSRAM Licht AG), no al domini historic osram-group.com/osram.com; les he classificat com a nivell A (web oficial de l'emissor/successora).
- Cites:

1. [`L2|DE000LED4000|C1`] [V] «Prior to becoming CEO of Osram in January 2015, Olaf Berlien was CEO of M+W Group GmbH.»
   Anys: 2016-2019 · Nivell A · prova: Inici del mandat: Berlien es CEO d'Osram des del gener de 2015. · URL: https://ams-osram.com/news/press-releases/pr-14-02-2017 · Wayback: https://web.archive.org/web/20260618021349/https://ams-osram.com/news/press-releases/pr-14-02-2017 (existent; cita no verificada a la captura)

2. [`L2|DE000LED4000|C2`] [V] «the supervisory board of OSRAM Licht AG extended the appointment of Chief Executive Officer Olaf Berlien, 54, by five years. The new term will start on January 1, 2018, and run until December 31, 2022.»
   Anys: 2016-2019 · Nivell A · prova: El 14/02/2017 Berlien era CEO i el consell de vigilancia li prorroga el nomenament (nou mandat 01/01/2018-31/12/2022): continuitat entre 2016 i 2018. · URL: https://ams-osram.com/news/press-releases/pr-14-02-2017 · Wayback: https://web.archive.org/web/20260618021349/https://ams-osram.com/news/press-releases/pr-14-02-2017 (existent; cita no verificada a la captura)

3. [`L2|DE000LED4000|C3`] [V] «said Olaf Berlien, Chief Executive Officer of OSRAM Licht AG»
   Anys: 2016 · Nivell A · prova: Nou dies despres del 31/10/2016 Berlien es identificat com a CEO d'OSRAM Licht AG. · URL: https://ams-osram.com/news/press-releases/pr-09-11-2016 · Wayback: https://web.archive.org/web/20260718053054/https://ams-osram.com/news/press-releases/pr-09-11-2016 (existent; cita no verificada a la captura)

4. [`L2|DE000LED4000|C4`] [V] «said Olaf Berlien, CEO of OSRAM Licht AG.»
   Anys: 2017 · Nivell A · prova: Sis dies despres del 31/10/2017 Berlien es identificat com a CEO d'OSRAM Licht AG. · URL: https://ams-osram.com/news/press-releases/pr-06-11-2017 · Wayback: https://web.archive.org/web/20260216103531/https://ams-osram.com/news/press-releases/pr-06-11-2017 (existent; cita no verificada a la captura)

5. [`L2|DE000LED4000|C5`] [V] «we are on the right track," said Olaf Berlien, CEO of OSRAM Licht AG.»
   Anys: 2018 · Nivell A · prova: Sis dies despres del 31/10/2018 Berlien es identificat com a CEO d'OSRAM Licht AG. · URL: https://ams-osram.com/news/press-releases/pr-06-11-2018 · Wayback: https://web.archive.org/web/20260512030258/https://ams-osram.com/news/press-releases/pr-06-11-2018 (existent; cita no verificada a la captura)

6. [`L2|DE000LED4000|C6`] [V] «said Olaf Berlien, CEO of OSRAM Licht AG.»
   Anys: 2019 · Nivell A · prova: Dotze dies despres del 31/10/2019 Berlien es identificat com a CEO d'OSRAM Licht AG. · URL: https://ams-osram.com/news/press-releases/pr-12-11-2019 · Wayback: https://web.archive.org/web/20260712083935/https://ams-osram.com/news/press-releases/pr-12-11-2019 (existent; cita no verificada a la captura)

7. [`L2|DE000LED4000|C7`] [V] «CEO Olaf Berlien will leave Osram on February 28 by mutual agreement.»
   Anys: 2016-2019 · Nivell A · prova: Fi del mandat: Berlien continua sent CEO fins al 28/02/2021 (posterior a tots els 31/10 del panell); el mateix document diu que el succeeix Ingo Bank. · URL: https://ams-osram.com/about-us/investor-relations/osram-investor-relations/regulatory-news-en-02-23-2021 · Wayback: https://web.archive.org/web/20241109132604/https://ams-osram.com/about-us/investor-relations/osram-investor-relations/regulatory-news-en-02-23-2021 (existent; cita no verificada a la captura)

### L2.7 Carlsberg AS Navne-Aktier B DK 20 (`DK0010181759`)

- isin i anys: `DK0010181759`, 2016-2022 (n=7). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Cees ’t Hart → Cees ’t Hart (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Web oficial de l'emissor (carlsberggroup.com). https://www.carlsberggroup.com/investor-relations/investor-home/reports-archive/ -> 404. https://www.carlsberggroup.com/reports-downloads/ -> 200 (índex, només llista documents recents). Els informes anuals 2016-2023 s'han obtingut provant slugs sota /reports-downloads/: carlsberg-group-annual-report-{2016..2019} i carlsberg-group-{2020..2023}-annual-report -> 200 application/pdf (redirecció a /media/...). Altres variants de slug provades (carlsberg-as-annual-report-AAAA, AAAA-annual-report, i la variant creuada de cada any) -> 404. No s'han cercat comunicats de premsa del nomenament de 2015 ni del relleu de 2023 perquè l'informe anual 2023 ja dona les dates de l'interval. Cap font de tercers utilitzada.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Les cites de signatura (declaració de la direcció) són fragments contigus del text extret amb pdftotext d'un bloc de signatures; el 2022 el bloc té dues columnes i el text extret queda 'Cees 't Hart Ulrica Fearn President & CEO CFO' (noms i després càrrecs). S'hi afegeix la cita de la carta als accionistes 2022 ('Cees ’t Hart CEO') per evitar ambigüitat. Doctorat ha de decidir si aquest tipus de cita de bloc de signatura és acceptable. · (2) Els informes anuals identifiquen el CEO de l'exercici i en la data de signatura (febrer de t+1), però no diuen literalment 'CEO el 31/10/t'; la cobertura de la data exacta es recolza en l'interval de l'informe 2023 (CEO des de juny de 2015; retirat a finals d'agost; successor l'1 de setembre), on l'any 2023 de les dues darreres dates es dedueix del context del document i no de la frase citada. · (3) Als informes 2017 i 2018 la fitxa del comitè executiu no dona text contigu útil amb pdftotext (noms i càrrecs en blocs separats); per a aquests anys la prova contemporània és només la signatura de la declaració de la direcció, més l'interval.
- Cites:

1. [`L2|DK0010181759|AR2016-sig`] [V] «Copenhagen, 8 February 2017 Executive Board of Carlsberg A/S Cees 't Hart CEO»
   Anys: 2016 · Nivell A · prova: Declaració de la direcció de l'informe anual 2016, signada el febrer de 2017: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/ye3p241k/carlsberg-group-annual-report-2016.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-annual-report-2016/ · Wayback: `pendent_verificacio_externa`

2. [`L2|DK0010181759|AR2017-sig`] [V] «Copenhagen, 7 February 2018 Executive Board of Carlsberg A/S Cees 't Hart President & CEO»
   Anys: 2017 · Nivell A · prova: Declaració de la direcció de l'informe anual 2017, signada el febrer de 2018: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/2emjcnhk/carlsberg-as_annual-report-2017.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-annual-report-2017/ · Wayback: `pendent_verificacio_externa`

3. [`L2|DK0010181759|AR2018-sig`] [V] «Copenhagen, 6 February 2019 Executive Board of Carlsberg A/S Cees 't Hart President & CEO»
   Anys: 2018 · Nivell A · prova: Declaració de la direcció de l'informe anual 2018, signada el febrer de 2019: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/1xcd3qqb/carlsberg-as-2018-annual-report.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-annual-report-2018/ · Wayback: `pendent_verificacio_externa`

4. [`L2|DK0010181759|AR2019-sig`] [V] «Copenhagen, 4 February 2020 Executive Board of Carlsberg A/S Cees ’t Hart President & CEO»
   Anys: 2019 · Nivell A · prova: Declaració de la direcció de l'informe anual 2019, signada el febrer de 2020: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/ffqdx3n0/carlsberg-as-annual-report-2019.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-annual-report-2019/ · Wayback: `pendent_verificacio_externa`

5. [`L2|DK0010181759|AR2020-sig`] [V] «Copenhagen, 5 February 2021 Executive Board of Carlsberg A/S Cees ’t Hart President & CEO»
   Anys: 2020 · Nivell A · prova: Declaració de la direcció de l'informe anual 2020, signada el febrer de 2021: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/fb2firdc/carlsberg-group-annual-report-2020_final.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2020-annual-report/ · Wayback: `pendent_verificacio_externa`

6. [`L2|DK0010181759|AR2021-sig`] [V] «Copenhagen, 4 February 2022 Executive Board of Carlsberg A/S Cees ’t Hart President & CEO»
   Anys: 2021 · Nivell A · prova: Declaració de la direcció de l'informe anual 2021, signada el febrer de 2022: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/l2phgf1k/carlsberg-goup-annual-report-2021.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2021-annual-report/ · Wayback: `pendent_verificacio_externa`

7. [`L2|DK0010181759|AR2022-sig`] [V] «Copenhagen, 7 February 2023 Executive Board of Carlsberg A/S Cees 't Hart Ulrica Fearn President & CEO CFO»
   Anys: 2022 · Nivell A · prova: Declaració de la direcció de l'informe anual 2022, signada el febrer de 2023: Cees 't Hart signa com a (President &) CEO de Carlsberg A/S. (La URL redirigeix a https://www.carlsberggroup.com/media/rscmtzgy/carlsberg-group-annual-report-2022.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2022-annual-report/ · Wayback: `pendent_verificacio_externa`

8. [`L2|DK0010181759|AR2016-excom`] [V] «Executive Committee (ExCom) Cees ’t Hart CEO since 2015.»
   Anys: 2016 · Nivell A · prova: Cees 't Hart és CEO des de 2015 (secció del comitè executiu de l'informe 2016). (La URL redirigeix a https://www.carlsberggroup.com/media/ye3p241k/carlsberg-group-annual-report-2016.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-annual-report-2016/ · Wayback: `pendent_verificacio_externa`

9. [`L2|DK0010181759|AR2019-excom`] [V] «CEES ’T HART CEO Nationality: Dutch Year of birth: 1958 Appointed: 2015»
   Anys: 2019 · Nivell A · prova: Fitxa del comitè executiu de l'informe 2019: Cees 't Hart, CEO, nomenat el 2015. (La URL redirigeix a https://www.carlsberggroup.com/media/ffqdx3n0/carlsberg-as-annual-report-2019.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-annual-report-2019/ · Wayback: `pendent_verificacio_externa`

10. [`L2|DK0010181759|AR2020-excom`] [V] «CEES ’T HART CEO Nationality: Dutch Year of birth: 1958 Appointed: 2015»
   Anys: 2020 · Nivell A · prova: Fitxa del comitè executiu de l'informe 2020: Cees 't Hart, CEO, nomenat el 2015. (La URL redirigeix a https://www.carlsberggroup.com/media/fb2firdc/carlsberg-group-annual-report-2020_final.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2020-annual-report/ · Wayback: `pendent_verificacio_externa`

11. [`L2|DK0010181759|AR2021-excom`] [V] «CEES ’T HART CEO Nationality: Dutch Year of birth: 1958 Appointed: 2015»
   Anys: 2021 · Nivell A · prova: Fitxa del comitè executiu de l'informe 2021: Cees 't Hart, CEO, nomenat el 2015. (La URL redirigeix a https://www.carlsberggroup.com/media/l2phgf1k/carlsberg-goup-annual-report-2021.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2021-annual-report/ · Wayback: `pendent_verificacio_externa`

12. [`L2|DK0010181759|AR2022-carta`] [V] «deliver strong results despite significant challenges during the year. Cees ’t Hart CEO»
   Anys: 2022 · Nivell A · prova: Carta als accionistes de l'informe 2022, amb Cees 't Hart identificat com a CEO. (La URL redirigeix a https://www.carlsberggroup.com/media/rscmtzgy/carlsberg-group-annual-report-2022.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2022-annual-report/ · Wayback: `pendent_verificacio_externa`

13. [`L2|DK0010181759|AR2023-inici`] [V] «We said farewell to Cees ’t Hart, our CEO since June 2015.»
   Anys: 2016-2022 · Nivell A · prova: Interval: 't Hart va ser CEO des de juny de 2015. (La URL redirigeix a https://www.carlsberggroup.com/media/3kjbpwaa/carlsberg-group-2023-annual-report.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2023-annual-report/ · Wayback: `pendent_verificacio_externa`

14. [`L2|DK0010181759|AR2023-fi`] [V] «After eight years at the helm of the Carlsberg Group, Cees ’t Hart retired at the end of August.»
   Anys: 2016-2022 · Nivell A · prova: Interval: 't Hart es va retirar a finals d'agost de 2023 (segons el context del document, que parla de 2023). (La URL redirigeix a https://www.carlsberggroup.com/media/3kjbpwaa/carlsberg-group-2023-annual-report.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2023-annual-report/ · Wayback: `pendent_verificacio_externa`

15. [`L2|DK0010181759|AR2023-successor`] [V] «On 1 September, we welcomed Jacob Aarup-Andersen as the new CEO of the Carlsberg Group.»
   Anys: 2016-2022 · Nivell A · prova: El successor entra l'1 de setembre (de 2023, segons l'informe 2023); per tant no hi ha canvi de CEO a prop de cap 31/10 de 2016-2022. (La URL redirigeix a https://www.carlsberggroup.com/media/3kjbpwaa/carlsberg-group-2023-annual-report.pdf, HTTP 200 application/pdf.) · URL: https://www.carlsberggroup.com/reports-downloads/carlsberg-group-2023-annual-report/ · Wayback: `pendent_verificacio_externa`

### L2.8 Christian Hansen Holding AS Navne-Aktier (`DK0060227585`)

- isin i anys: `DK0060227585`, 2016-2017 (n=2). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Cees de Jong → Cees de Jong (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Informes anuals 2016/17 i 2017/18 (exercici 1/9-31/8) NO obtinguts de la web de la successora: backend.novonesis.com/sites/default/files/document/{2024-04..2024-08}/Chr-Hansen_Annual_report_{2015-16,2016-17,2017-18}.pdf i variants de nom -> 404 (només hi respon el 2021-22, 200, que no esmenta De Jong). https://www.novonesis.com/en/investor/financial-reports-and-presentations -> 404. https://www.chr-hansen.com/en/investors/reports-and-presentations -> 403. globenewswire.com (anuncis Annual Report 2017/18 i 2016/17) -> 403. distribution.virk.dk (registre danes de comptes, CVR 28318677) -> host no resoluble. Copies de tercers (api.risika.dk, financialreports.eu) localitzades pero no usades com a prova. Obert amb 200: quatre comunicats de la sala de premsa oficial de Chr. Hansen a mynewsdesk.com (26/10/2016, 25/10/2017, 28/11/2017, 8/1/2018), dels quals surten totes les cites. Tambe obert (200) el PDF Statement of Results 2017/18 a ml-eu.globenewswire.com/Resource/Download/84bd6bb4-f438-487c-a3ca-c19684554225 (15/10/2018, 'CEO Mauricio Graber says'), no usat com a cita perque es fora dels anys demanats.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Les cites provenen de la sala de premsa de l'emissor allotjada a mynewsdesk.com (plataforma de distribucio de comunicats que l'empresa gestionava), no del domini chr-hansen.com/novonesis.com. S'han classificat com a nivell A (document del mateix emissor); Doctorat ha de decidir si un comunicat de l'emissor en una plataforma de distribucio compta com a A, com a B, o com a copia de tercers. · (2) Cap cita es exactament del 31/10: la prova es per interval (comunicats de 5-6 dies abans i del 28/11/2017 que afirma continuitat des del 2013). No s'ha pogut obrir cap informe anual dels exercicis 2016/17 i 2017/18. · (3) La data de cada comunicat es una cita separada de la capcalera ('Press release — data'), verificada en mode html_sense_etiquetes, no dins la mateixa frase que el carrec. · (4) Fora de l'abast del lot: la cita [1] de la fitxa ('Cees de Jong Chair of the Board', pagina actual de Novonesis) no prova que fos CEO el 2016-2017; les cites d'aquest lot la podrien substituir.
- Cites:

1. [`L2|DK0060227585|C1`] [V] «So I can only be pleased with how we performed in 2015/16” says CEO Cees de Jong.»
   Anys: 2016 · Nivell A · prova: Comunicat de resultats anuals 2015/16: Cees de Jong hi parla com a CEO. · URL: https://www.mynewsdesk.com/com/chr-hansen/pressreleases/very-satisfactory-annual-result-12-procent-growth-1622919 · Wayback: `pendent_verificacio_externa`

2. [`L2|DK0060227585|C2`] [V] «Press release — 26 October 2016»
   Anys: 2016 · Nivell A · prova: Data del comunicat C1 (26/10/2016, cinc dies abans del 31/10/2016). · URL: https://www.mynewsdesk.com/com/chr-hansen/pressreleases/very-satisfactory-annual-result-12-procent-growth-1622919 · Wayback: `pendent_verificacio_externa`

3. [`L2|DK0060227585|C3`] [V] «in line with our Nature’s no. 1 strategy,” says CEO Cees de Jong.»
   Anys: 2017 · Nivell A · prova: Comunicat de resultats anuals 2016/17: Cees de Jong hi parla com a CEO. · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/another-good-year-for-chr-hansen-10-procent-organic-growth-2231116 · Wayback: https://web.archive.org/web/20190916201847/http://www.mynewsdesk.com/chr-hansen/pressreleases/another-good-year-for-chr-hansen-10-procent-organic-growth-2231116 (existent; cita no verificada a la captura)

4. [`L2|DK0060227585|C4`] [V] «Press release — 25 October 2017»
   Anys: 2017 · Nivell A · prova: Data del comunicat C3 (25/10/2017, sis dies abans del 31/10/2017). · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/another-good-year-for-chr-hansen-10-procent-organic-growth-2231116 · Wayback: https://web.archive.org/web/20190916201847/http://www.mynewsdesk.com/chr-hansen/pressreleases/another-good-year-for-chr-hansen-10-procent-organic-growth-2231116 (existent; cita no verificada a la captura)

5. [`L2|DK0060227585|C5`] [V] «The Company has initiated a process to find his replacement, and until then Cees de Jong will continue as CEO of Chr. Hansen.»
   Anys: 2016-2017 · Nivell A · prova: El 28/11/2017 De Jong encara és CEO i continua fins que hi hagi substitut. · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/cees-de-jong-will-step-down-as-ceo-of-chr-hansen-holding-a-skraastreg-s-2302223 · Wayback: https://web.archive.org/web/20171203185341/http://www.mynewsdesk.com:80/chr-hansen/pressreleases/cees-de-jong-will-step-down-as-ceo-of-chr-hansen-holding-a-skraastreg-s-2302223 (existent; cita no verificada a la captura)

6. [`L2|DK0060227585|C6`] [V] «it is, and has been, a privilege to be the CEO since 2013.»
   Anys: 2016 · Nivell A · prova: De Jong (cita seva al comunicat) és CEO de manera continuada des del 2013. · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/cees-de-jong-will-step-down-as-ceo-of-chr-hansen-holding-a-skraastreg-s-2302223 · Wayback: https://web.archive.org/web/20171203185341/http://www.mynewsdesk.com:80/chr-hansen/pressreleases/cees-de-jong-will-step-down-as-ceo-of-chr-hansen-holding-a-skraastreg-s-2302223 (existent; cita no verificada a la captura)

7. [`L2|DK0060227585|C7`] [V] «Press release — 28 November 2017»
   Anys: 2016-2017 · Nivell A · prova: Data del comunicat C5/C6. · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/cees-de-jong-will-step-down-as-ceo-of-chr-hansen-holding-a-skraastreg-s-2302223 · Wayback: https://web.archive.org/web/20171203185341/http://www.mynewsdesk.com:80/chr-hansen/pressreleases/cees-de-jong-will-step-down-as-ceo-of-chr-hansen-holding-a-skraastreg-s-2302223 (existent; cita no verificada a la captura)

8. [`L2|DK0060227585|C8`] [V] «The Board of Directors of Chr. Hansen Holding A/S has today appointed Mauricio Graber as new Chief Executive Officer (CEO) as of 1 June 2018.»
   Anys: 2017 · Nivell A · prova: El successor Mauricio Graber és CEO amb efecte 1/6/2018; fins llavors no hi ha canvi. · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/mauricio-graber-appointed-new-ceo-of-chr-hansen-holding-a-skraastreg-s-2361711 · Wayback: https://web.archive.org/web/20230207171338/https://www.mynewsdesk.com/chr-hansen/pressreleases/mauricio-graber-appointed-new-ceo-of-chr-hansen-holding-a-skraastreg-s-2361711 (existent; cita no verificada a la captura)

9. [`L2|DK0060227585|C9`] [V] «Press release — 8 January 2018»
   Anys: 2017 · Nivell A · prova: Data del comunicat C8. · URL: https://www.mynewsdesk.com/chr-hansen/pressreleases/mauricio-graber-appointed-new-ceo-of-chr-hansen-holding-a-skraastreg-s-2361711 · Wayback: https://web.archive.org/web/20230207171338/https://www.mynewsdesk.com/chr-hansen/pressreleases/mauricio-graber-appointed-new-ceo-of-chr-hansen-holding-a-skraastreg-s-2361711 (existent; cita no verificada a la captura)

### L2.9 BANKIA S.A. Acciones Nominativas EO 0,8 (`ES0113307021`)

- isin i anys: `ES0113307021`, 2016 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **José Sevilla Álvarez → José Sevilla Álvarez (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A, B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Obert a la URL original: https://www.cnmv.es/AUDITA/2016/16764.pdf (HTTP 200, PDF 6,56 MB; el primer intent va quedar truncat i el reintent el va baixar sencer): comptes anuals individuals, informe de gestió i IAGC 2016 de Bankia. https://www.elindependiente.com/?p=26973 (HTTP 200, redirigeix a https://www.elindependiente.com/economia/2016/10/26/bankia-espera-acelerar-privatizacion-partir-2017/). També oberts a la web de la successora legal CaixaBank, sense fer-los servir com a cita: https://www.caixabank.com/deployedfiles/caixabank/Estaticos/PDFs/Informacion_accionistas_inversores/Cuentas_consolidadas_2017_Bankia_EN.pdf (200; comptes consolidats 2017 de Bankia, on Sevilla consta com a 'Chief Executive Officer', continuïtat posterior) i https://www.caixabank.com/deployedfiles/caixabank_com/Estaticos/PDFs/Accionistasinversores/Emisiones_CaixaBank/2_Supl_FB_2016_Es.pdf (200; suplement de fullet de 28/02/2017, sense menció del càrrec). Fallats: https://www.bankia.com/es/ (el proxy no hi pot connectar, 502: el domini de l'emissor ja no respon); https://www.caixabank.com/es/accionistas-inversores/informacion-general/informacion-bankia.html (404, URL provada a cegues); https://boe.gob.es/borme/dias/2016/02/12/pdfs/BORME-C-2016-623.pdf i https://boe.gob.es/borme/dias/2017/02/23/pdfs/BORME-C-2017-832.pdf (HTTP 200 però pàgina HTML de 3 kB, no el PDF: no usats). Les còpies de l'informe anual a ddd.uab.cat (dipòsit de tercers) no s'han fet servir. No s'ha buscat la data de nomenament inicial de Sevilla com a conseller delegat (no cal per al 2016; l'IAGC només dona la data de primer nomenament com a conseller, 25/05/2012). Les pistes d'items.json (bde.es Guia.pdf, cnmc.es) no s'han obert perquè no calien.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Bankia tenia el 2016 una estructura dual: el mateix document (https://www.cnmv.es/AUDITA/2016/16764.pdf) anomena José Ignacio Goirigolzarri Tellaeche 'Presidente Ejecutivo' (quadre C.1.3: 'PRESIDENTE EJECUTIVO') amb 'delegadas todas y cada una de las facultades, salvo las legal y estatutariamente indelegables', mentre que José Sevilla és 'Consejero Delegado' amb facultats delegades 'en las áreas de dirección financiera y de riesgos, intervención y auditoría interna, así como inmobiliario y empresas participadas, y asesoramiento jurídico, fiscal y cumplimiento'. La base pren el titular del títol 'consejero delegado' (Sevilla), que és el criteri literal de la regla; Doctorat hauria de confirmar si en casos de president executiu amb totes les facultats delegades compta el consejero delegado o el president executiu. L'etiqueta FounderCEO no en depèn previsiblement (cap dels dos és fundador), però no ho he verificat. · (2) La cita c5 és d'El Independiente (diari digital generalista amb secció d'economia); Doctorat ha de decidir si compta com a premsa econòmica de qualitat (nivell B). La fila ja queda coberta amb les cites de nivell A (c1-c4), que proven el càrrec a l'exercici 2016 i al tancament però no porten literalment la data del 31/10.
- Cites:

1. [`L2|ES0113307021|c1`] [V] «correspondientes al ejercicio anual terminado el 31 de diciembre de 2016»
   Anys: 2016 · Nivell A · prova: El document cobreix l'exercici natural 2016, que inclou el 31/10/2016. · URL: https://www.cnmv.es/AUDITA/2016/16764.pdf · Wayback: https://web.archive.org/web/20240528024914/https://www.cnmv.es/AUDITA/2016/16764.pdf (existent; cita no verificada a la captura)

2. [`L2|ES0113307021|c2`] [V] «D. José Sevilla Álvarez. Consejero Delegado»
   Anys: 2016 · Nivell A · prova: Composició del consell a l'informe de gestió de 2016: Sevilla és el Consejero Delegado. · URL: https://www.cnmv.es/AUDITA/2016/16764.pdf · Wayback: https://web.archive.org/web/20240528024914/https://www.cnmv.es/AUDITA/2016/16764.pdf (existent; cita no verificada a la captura)

3. [`L2|ES0113307021|c3`] [V] «DON JOSÉ SEVILLA ÁLVAREZ CONSEJERO DELEGADO»
   Anys: 2016 · Nivell A · prova: Càrrec a l'organigrama a l'IAGC de l'exercici tancat el 31/12/2016: Consejero Delegado. · URL: https://www.cnmv.es/AUDITA/2016/16764.pdf · Wayback: https://web.archive.org/web/20240528024914/https://www.cnmv.es/AUDITA/2016/16764.pdf (existent; cita no verificada a la captura)

4. [`L2|ES0113307021|c4`] [V] «Asimismo, la Junta General de Accionistas acordó reelegir como consejeros, con sus calificaciones correspondientes, por el plazo estatutario de cuatro años, a D. José Sevilla Álvarez»
   Anys: 2016 · Nivell A · prova: Reelecció de Sevilla com a conseller per la Junta de 2016 (continuïtat durant l'exercici). · URL: https://www.cnmv.es/AUDITA/2016/16764.pdf · Wayback: https://web.archive.org/web/20240528024914/https://www.cnmv.es/AUDITA/2016/16764.pdf (existent; cita no verificada a la captura)

5. [`L2|ES0113307021|c5`] [V] «Así lo afirmó este miércoles el consejero delegado de Bankia, José Sevilla, durante la presentación de los resultados del banco en el tercer trimestre del año.»
   Anys: 2016 · Nivell B · prova: Sevilla actua com a consejero delegado de Bankia el 26/10/2016, cinc dies abans de la data de referència. · URL: https://www.elindependiente.com/?p=26973 · Wayback: `pendent_verificacio_externa`

6. [`L2|ES0113307021|c6`] [V] «2016-10-26T12:04:24+00:00»
   Anys: 2016 · Nivell B · prova: Data de publicació de la notícia de c5 (26/10/2016). · URL: https://www.elindependiente.com/?p=26973 · Wayback: `pendent_verificacio_externa`

### L2.10 Alten S.A. Actions au Porteur EO 1,05 (`FR0000071946`)

- isin i anys: `FR0000071946`, 2018-2024 (n=7). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Simon Azoulay → Simon Azoulay (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Web de l'emissor: https://www.alten.com/alten-group/who-we-are/ , https://www.alten.com/investors/regulated-information/ , https://www.alten.com/robots.txt , https://www.alten.fr/ i els PDF d'URD https://www.alten.com/wp-content/uploads/2024/04/ALTEN-URD-2023-EN.pdf (URL provada a cegues) i https://alten.com/wp-content/uploads/2024/04/2023-Universal-Registration-Document.pdf: tots HTTP 403 amb pàgina de comprovació antibot ('Checking your browser'), no utilitzables. Alternativa oficial: dipòsit d'informació regulada de l'AMF servit per la DILA (echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/), HTTP 200: URD 2020 (FC317381551_20210428.pdf), URD 2021 (FC317442505_20220429.zip, ESEF), URD 2022 (FC317481759_20230427.pdf), URD 2023 (FC317528771_20240426.pdf), URD 2024 (FC317579970_20250425.zip, ESEF). El llistat d'aquest directori comença el 2021: no hi ha el document de referència 2018 ni l'URD 2019. El fitxer FC317380249_20210414.pdf del mateix directori és d'un altre emissor (descartat). FC317626500_20260429.zip (URD 2025) es va tallar per temps i no s'ha fet servir (2025 no és al lot). Per a 2018-2019 també s'han obert comunicats d'Alten al dipòsit AMF/DILA (ECO/2019/01/FCECO049642_20190129.pdf, ECO/2019/10/FCECO052818_20191023.pdf, ECO/2019/12/FCECO053303_20191211.pdf, ECO/2020/02/FCECO053904_20200218.pdf) i dues declaracions de franqueig de llindar (307/8888/01/FC307295136_20190809.pdf, FC307321441_20191118.pdf): tots HTTP 200 però cap esmenta el PDG. WebSearch només com a pista; les còpies de companiesmarketcap.com i calameo no s'han fet servir.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Les cites provenen del dipòsit oficial de l'AMF servit per la DILA (echanges.dila.gouv.fr/OPENDATA/AMF), no de la web de l'emissor (alten.com retorna 403 antibot). S'ha classificat com a nivell A (regulador/registre oficial); Doctorat ha de confirmar que aquest dipòsit compta com a URL original. · (2) Els URD 2021 i 2024 només hi són com a paquet ESEF (.zip). La URL citada és la del .zip i vq.py s'ha executat sobre el fitxer .xhtml/.html extret del zip (sense cap altra transformació). Cal decidir si això és acceptable com a comprovació literal. · (3) 2018 i 2019 no tenen document contemporani obert: es cobreixen només amb cites d'interval de documents posteriors (URD 2020 i URD 2024: PDG des del 22/09/1998, renovat el 22/06/2017, cúmul de funcions sense canvis des de 2002). Cal decidir si n'hi ha prou o si cal el document de referència 2018 / URD 2019. · (4) La cita c2 (dates de nomenament i renovació com a PDG) és un fragment de la fitxa individual de 'M. SIMON AZOULAY' a l'URD 2020; el nom no surt dins del fragment contigu, sinó a la capçalera de la mateixa fitxa.
- Cites:

1. [`L2|FR0000071946|c1`] [V] «Le Conseil d’administration d’ALTEN a ainsi opté, depuis 2002, pour le cumul des fonctions de Président du Conseil d’administration et de Directeur général. La Direction générale de la Société est exercée par Monsieur Simon AZOULAY, assisté de deux Directeurs Généraux Délégués.»
   Anys: 2018-2020 · Nivell A · prova: Des de 2002 les funcions de president i Directeur général estan acumulades i la Direction générale l'exerceix Simon Azoulay (document de l'exercici 2020). · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf · Wayback: https://web.archive.org/web/20210712185007/https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf (existent; cita no verificada a la captura)

2. [`L2|FR0000071946|c2`] [V] «19 février 1997 (Administrateur) – 22 septembre 1998 (PDG). DATE DU DERNIER RENOUVELLEMENT : 22 juin 2017 (Administrateur et PDG).»
   Anys: 2018-2020 · Nivell A · prova: Fitxa de mandats de 'M. SIMON AZOULAY Président-Directeur général d’ALTEN': primer nomenament com a PDG el 22/09/1998 i darrera renovació com a PDG el 22/06/2017. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf · Wayback: https://web.archive.org/web/20210712185007/https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf (existent; cita no verificada a la captura)

3. [`L2|FR0000071946|c3`] [V] «Date de début de mandat : 22/09/1998 Date de fin de mandat : Assemblée à tenir en 2021 et appelée à statuer sur les comptes de l’exercice écoulé.»
   Anys: 2018-2020 · Nivell A · prova: Taula de mandataris: el mandat de Simon AZOULAY Président-Directeur général comença el 22/09/1998 i venç a la junta de 2021. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf · Wayback: https://web.archive.org/web/20210712185007/https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf (existent; cita no verificada a la captura)

4. [`L2|FR0000071946|c4`] [V] «Le document d’enregistrement universel a été déposé auprès de l’AMF, le 28 avril 2021»
   Anys: 2020 · Nivell A · prova: Data de dipòsit de l'URD 2020. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf · Wayback: https://web.archive.org/web/20210712185007/https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317381551_20210428.pdf (existent; cita no verificada a la captura)

5. [`L2|FR0000071946|c5`] [V] «En 2002, le Conseil d’administration a décidé l’unicité des fonctions de Président du Conseil d’administration et de Directeur général. Cette décision n’a pas été modifiée depuis lors. Ces fonctions sont exercées par Monsieur Simon AZOULAY, assisté par un Directeur Général Délégué.»
   Anys: 2021 · Nivell A · prova: Unicitat de les funcions de president i Directeur général des de 2002, sense modificació, exercides per Simon Azoulay (document de l'exercici 2021). · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317442505_20220429.zip · Wayback: `pendent_verificacio_externa`

6. [`L2|FR0000071946|c6`] [V] «En 2002, le Conseil d’administration a décidé l’unicité des fonctions de Président du Conseil d’administration et de Directeur général. Cette décision n’a pas été modifiée depuis lors. Ces fonctions sont exercées par Monsieur Simon AZOULAY»
   Anys: 2022 · Nivell A · prova: Unicitat de funcions des de 2002, no modificada des d'aleshores, exercides per Simon Azoulay (document de l'exercici 2022). · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317481759_20230427.pdf · Wayback: https://web.archive.org/web/20261112013824/https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317481759_20230427.pdf (existent; cita no verificada a la captura)

7. [`L2|FR0000071946|c7`] [V] «Le Document d’enregistrement universel a été déposé le 27 avril 2023 auprès de l’AMF»
   Anys: 2022 · Nivell A · prova: Data de dipòsit de l'URD 2022. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317481759_20230427.pdf · Wayback: https://web.archive.org/web/20261112013824/https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317481759_20230427.pdf (existent; cita no verificada a la captura)

8. [`L2|FR0000071946|c8`] [V] «En 2002, le Conseil d’administration a décidé l’unicité des fonctions de Président du Conseil d’administration et de Directeur général. Cette décision n’a pas été modifiée depuis lors. Ces fonctions sont exercées par Monsieur Simon AZOULAY»
   Anys: 2023 · Nivell A · prova: Unicitat de funcions des de 2002, no modificada des d'aleshores, exercides per Simon Azoulay (document de l'exercici 2023). · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317528771_20240426.pdf · Wayback: `pendent_verificacio_externa`

9. [`L2|FR0000071946|c9`] [V] «Le Document d’enregistrement universel a été déposé le 26 avril 2024 auprès de l’AMF»
   Anys: 2023 · Nivell A · prova: Data de dipòsit de l'URD 2023. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317528771_20240426.pdf · Wayback: `pendent_verificacio_externa`

10. [`L2|FR0000071946|c10`] [V] «Monsieur Simon AZOULAY exerce les fonctions de Président-Directeur général. Son mandat arrive à échéance lors de l’Assemblée générale annuelle 2025.»
   Anys: 2024 · Nivell A · prova: Simon Azoulay exerceix de Président-Directeur général (document de l'exercici 2024, dipositat l'abril de 2025). · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip · Wayback: `pendent_verificacio_externa`

11. [`L2|FR0000071946|c11`] [V] «Simon AZOULAY Président-Directeur général Date de début de mandat : 22/09/1998 Date de fin de mandat : Assemblée à tenir en 2025 et appelée à statuer sur les comptes de l’exercice 2024.»
   Anys: 2018-2019, 2021-2024 · Nivell A · prova: Interval de mandat: PDG des del 22/09/1998 fins a la junta de 2025 que aprova els comptes de 2024; cobreix tots els 31/10 de 2018 a 2024. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip · Wayback: `pendent_verificacio_externa`

12. [`L2|FR0000071946|c12`] [V] «Le Document d’enregistrement universel a été déposé le 25 avril 2025 auprès de l’AMF»
   Anys: 2024 · Nivell A · prova: Data de dipòsit de l'URD 2024. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/317/8888/01/FC317579970_20250425.zip · Wayback: `pendent_verificacio_externa`

### L2.11 Essilor Intl -Cie Génle Opt.SA Actions Port. (`FR0000121667`)

- isin i anys: `FR0000121667`, 2016-2017 (n=2). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Hubert Sagnières → Hubert Sagnières (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Web oficial de la successora (essilorluxottica.com): baixats amb HTTP 200 els PDF cap/content/118376 (Update to the 2017 Registration Document), 56508 (URD 2019), 56466 (URD 2020), 118350 (presentació AG 24/04/2018), 118396 (resultats 1S 2018) i api/getCapContent id=247426 (URD 2024) i id=262758 (Q3 2025); les URL cap/content/<id>/ sense ?_iframe=true tornen un HTML embolcall (no prova), amb ?_iframe=true tornen el PDF. Open data AMF (echanges.dila.gouv.fr), tots HTTP 200: FCCNS148981_20161021 (T3 2016), FCCNS150096/150098_20161207 (comunicat organització, EN/FR), FCCNS146973_20160729 (informe semestral 2016), FCCNS156663_20170728 (informe semestral 2017), FC152181638_20170628 (Final Terms), FCCNS158478/158479_20171012 (hive-down). No s'han localitzat a la web de la successora els Documents de référence 2016 i 2017 complets (WebSearch no en retorna la URL); no ha calgut perquè les cites d'interval i contemporànies cobreixen els dos anys. No s'ha intentat web.archive.org. Cap URL ha fallat.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Hive-down: segons la presentació de l'AG 2018 (cap118350) i el comunicat del 12/10/2017, les activitats d'Essilor es van aportar a una filial (Essilor International SAS) amb efecte l'1/11/2017; la societat cotitzada (ISIN FR0000121667) va mantenir Sagnières com a Chairman and CEO. No afecta el 31/10/2017, però Doctorat pot voler confirmar que el criteri és el CEO de la societat cotitzada. · (2) La fitxa del repositori anomena l'empresa EssilorLuxottica (nom actual de l'ISIN) mentre que items.json diu Essilor International; el 2016-2017 l'emissor era Essilor International (Compagnie Générale d'Optique). Només és una qüestió de denominació. · (3) Per al 31/10/2017 no hi ha un document datat exactament a l'entorn d'aquell dia (el més proper és el comunicat del 12/10/2017, que no li dona literalment el títol de PDG de la cotitzada); la prova és l'interval (C1, C2) més documents de juny/juliol 2017 i d'abril 2018.
- Cites:

1. [`L2|FR0000121667|C1`] [V] «Mr. Hubert Sagnières has been Chairman and Chief Executive Officer of Essilor since January 2, 2012.»
   Anys: 2016-2017 · Nivell A · prova: Interval: PDG d'Essilor de manera continuada des del 2/1/2012 fins a la data del document (28/09/2018); cobreix el 31/10/2016 i el 31/10/2017. · URL: https://www.essilorluxottica.com/cap/content/118376/?_iframe=true · Wayback: `pendent_verificacio_externa`

2. [`L2|FR0000121667|C2`] [V] «Chairman and Chief Executive Officer from January 2, 2012, and Executive Vice-Chairman from October 1, 2018»
   Anys: 2016-2017 · Nivell A · prova: Interval de mandat de Hubert Sagnières (el text figura sota el seu nom): PDG des del 2/1/2012 i Executive Vice-Chairman des de l'1/10/2018. · URL: https://www.essilorluxottica.com/cap/content/56508/?_iframe=true · Wayback: `pendent_verificacio_externa`

3. [`L2|FR0000121667|C3`] [V] «favoriser une accélération de la croissance en 2017 », a déclaré Hubert Sagnières, Président-Directeur Général du groupe.»
   Anys: 2016 · Nivell A · prova: Document contemporani: Sagnières és Président-Directeur Général el 21/10/2016. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/CNS/2016/10/FCCNS148981_20161021.pdf · Wayback: https://web.archive.org/web/20210712200345/https://echanges.dila.gouv.fr/OPENDATA/AMF/CNS/2016/10/FCCNS148981_20161021.pdf (existent; cita no verificada a la captura)

4. [`L2|FR0000121667|C4`] [V] «At the December 6, 2016 Board of Directors' meeting, Hubert Sagnières, Chairman and Chief Executive Officer of Essilor, proposed strengthening the Company's executive management»
   Anys: 2016 · Nivell A · prova: Continuïtat després del 31/10/2016: Sagnières és Chairman and CEO el 6-7/12/2016. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/CNS/2016/12/FCCNS150096_20161207.pdf · Wayback: https://web.archive.org/web/20210712195705/https://echanges.dila.gouv.fr/OPENDATA/AMF/CNS/2016/12/FCCNS150096_20161207.pdf (existent; cita no verificada a la captura)

5. [`L2|FR0000121667|C5`] [V] «Commenting on these results, Hubert Sagnières, Chairman and Chief Executive Officer of Essilor, said:»
   Anys: 2017 · Nivell A · prova: Sagnières és Chairman and CEO el juliol de 2017 (abans del 31/10/2017). · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/CNS/2017/07/FCCNS156663_20170728.pdf · Wayback: https://web.archive.org/web/20210712211427/https://echanges.dila.gouv.fr/OPENDATA/AMF/CNS/2017/07/FCCNS156663_20170728.pdf (existent; cita no verificada a la captura)

6. [`L2|FR0000121667|C6`] [V] «respect of the 2017 fiscal year to Mr. Hubert SAGNIÈRES, Chairman and Chief Executive Officer»
   Anys: 2017 · Nivell A · prova: Sagnières figura com a Chairman and CEO respecte de l'exercici 2017 i a la junta d'abril de 2018 (continuïtat després del 31/10/2017). · URL: https://www.essilorluxottica.com/cap/content/118350/?_iframe=true · Wayback: `pendent_verificacio_externa`

7. [`L2|FR0000121667|C7`] [V] «decision of Hubert Sagnières, Président-Directeur Général of the Issuer, dated 27 June 2017»
   Anys: 2017 · Nivell A · prova: Sagnières és Président-Directeur Général de l'emissor el 27/06/2017. · URL: https://echanges.dila.gouv.fr/OPENDATA/AMF/152/8888/01/FC152181638_20170628.pdf · Wayback: https://web.archive.org/web/20210712194748/https://echanges.dila.gouv.fr/OPENDATA/AMF/152/8888/01/FC152181638_20170628.pdf (existent; cita no verificada a la captura)

### L2.12 Associated British Foods PLC Registered (`GB0006731235`)

- isin i anys: `GB0006731235`, 2016-2025 (n=10). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **George Weston → George Weston (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A, B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: 1) Web oficial de l emissor abf.co.uk: bloquejada. https://www.abf.co.uk/investors/results-reports-and-presentations i https://www.abf.co.uk/about-us/our-board retornen una pagina 'Challenge Validation' (anti-bot, 200 amb 1854 bytes, sense contingut); els PDF directes retornen 403: https://www.abf.co.uk/content/dam/abf/corporate/Documents/investors/annual-and-interim-reports/2023/Annual%20Report%202023.pdf , https://www.abf.co.uk/content/dam/abf/corporate/ar-assets-2024/pdfs/abf-ar-governance-report-2024.pdf.downloadasset.pdf , https://abf.co.uk/content/dam/abf/corporate/oar-and-rr-2023/oar/abf-ar-governance-report-2023.pdf.downloadasset.pdf , https://abf.co.uk/content/dam/abf/corporate/Documents/investors/abf-annual-results-announcement-5-november.pdf (tots 403). 2) Companies House (company 00293262): filing history obert (47 pagines) i baixats els comptes anuals de grup (AA) dels exercicis 2016 a 2025 (fitxers ch_aa_2016.pdf ... ch_aa_2025.pdf, URL https://find-and-update.company-information.service.gov.uk/company/00293262/filing-history/<id>/document?format=pdf&download=0). Son PDF escanejats sense capa de text (pdftotext retorna nomes salts de pagina) i no hi ha OCR disponible, de manera que no s hi pot verificar cap cita literal amb vq.py: NO s han fet servir com a prova. La pagina d oficial de Companies House (pista de items.json) s obre i mostra George Garfield WESTON com a Director actiu d ASSOCIATED BRITISH FOODS PLC nomenat el 19 April 1999, pero nomes prova el carrec de conseller, no el de CEO, i no s ha inclos com a cita. 3) FCA National Storage Mechanism: l intent de consultar-ne l API de cerca va ser denegat pel sistema de permisos de la sessio; no s ha insistit. 4) Webs del mateix grup que serveixen documents de l emissor (obertes amb 200): abfingredients.com (divisio ABF Ingredients) publica el text dels comunicats de resultats d Associated British Foods plc: Annual Results Announcement 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 i 2025 (el de 2024 i el de 2026 retornen 404), Interim Results 2024, 2025 i 2026, i trading updates (09/2024, 01/25; el de 01/25 no nomena el CEO). azucarera.es (filial AB Sugar a Espanya) serveix el PDF de l Annual Report and Accounts 2019 d ABF (https://www.azucarera.es/wp-content/uploads/2019/11/ar2019b.pdf, 190 pagines, amb capa de text). 5) Premsa: RTE News (https://www.rte.ie/news/business/2024/1105/1479133-associated-british-foods-results, 200) per cobrir el novembre de 2024. WebSearch nomes s ha fet servir per localitzar URL. Pistes no usades com a prova: lse.co.uk, investegate, marketscreener, simplywall.st, stockopedia, fashionunited.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Les cites A provenen de webs de filials/divisions del grup (abfingredients.com, azucarera.es) que reprodueixen o allotgen documents d Associated British Foods plc, no de la web corporativa de l emissor (abf.co.uk, bloquejada per anti-bot amb 403). Doctorat ha de decidir si una web d una filial controlada compta com a font de nivell A ('document de la mateixa empresa a la seva web oficial') o s ha de tractar com a copia; si no compta, les files quedarien pendent_verificacio_externa excepte el 2024 (cobert tambe per RTE, nivell B). · (2) Cap document obert diu literalment qui era CEO el dia 31/10/t: la data queda acotada entre documents que el nomenen Chief Executive abans i pocs dies despres (3-9 de novembre) de cada 31/10, mes la cita d interval de l informe anual 2019 ('current appointment as Chief Executive in April 2005') per a 2016-2019. Per a 2020-2025 no s ha pogut obrir cap informe anual amb cita d interval (abf.co.uk 403; Companies House escanejat sense text). · (3) L exercici fiscal d ABF tanca a mitjan setembre: l informe anual de l exercici t se signa a principis de novembre de t (p. ex. 5 November 2019), es a dir, despres del 31/10/t; cal confirmar que aquesta data de signatura es acceptable per cobrir el 31/10/t. · (4) Els comptes anuals dipositats a Companies House (font A, registre oficial) estan baixats pero son imatges sense text; si l orquestrador disposa d OCR, podrien servir de verificacio independent, tot i que una cita sobre OCR no seria estrictament 'literal del fitxer'. · (5) La noticia de RTE de 5/11/2024 incorpora text d agencia (Reuters); s ha classificat com a nivell B (premsa de qualitat a la seva URL original).
- Cites:

1. [`L2|GB0006731235|R2015`] [V] «2015 Annual Results Announcement 03 Nov 2015 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2016 · Nivell A · prova: El 03 Nov 2015 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2015). · URL: https://www.abfingredients.com/en/news-and-events/news/2015-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260514171725/https://www.abfingredients.com/en/news-and-events/news/2015-annual-results-announcement/ (existent; cita no verificada a la captura)

2. [`L2|GB0006731235|R2016`] [V] «2016 Annual Results Announcement 08 Nov 2016 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2016-2017 · Nivell A · prova: El 08 Nov 2016 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2016). · URL: https://www.abfingredients.com/en/news-and-events/news/2016-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260617013406/https://www.abfingredients.com/en/news-and-events/news/2016-annual-results-announcement/ (existent; cita no verificada a la captura)

3. [`L2|GB0006731235|R2017`] [V] «2017 Annual Results Announcement 09 Nov 2017 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2017-2018 · Nivell A · prova: El 09 Nov 2017 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2017). · URL: https://www.abfingredients.com/en/news-and-events/news/2017-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260719053551/https://www.abfingredients.com/en/news-and-events/news/2017-annual-results-announcement/ (existent; cita no verificada a la captura)

4. [`L2|GB0006731235|R2018`] [V] «2018 Annual Results Announcement 06 Nov 2018 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2018-2019 · Nivell A · prova: El 06 Nov 2018 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2018). · URL: https://www.abfingredients.com/en/news-and-events/news/2018-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260719054927/https://www.abfingredients.com/en/news-and-events/news/2018-annual-results-announcement/ (existent; cita no verificada a la captura)

5. [`L2|GB0006731235|R2019`] [V] «2019 Annual Results Announcement 05 Nov 2019 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2019-2020 · Nivell A · prova: El 05 Nov 2019 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2019). · URL: https://www.abfingredients.com/en/news-and-events/news/2019-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260719055141/https://www.abfingredients.com/en/news-and-events/news/2019-annual-results-announcement/ (existent; cita no verificada a la captura)

6. [`L2|GB0006731235|R2020`] [V] «2020 Annual Results Announcement 03 Nov 2020 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2020-2021 · Nivell A · prova: El 03 Nov 2020 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2020). · URL: https://www.abfingredients.com/en/news-and-events/news/2020-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260617000638/https://www.abfingredients.com/en/news-and-events/news/2020-annual-results-announcement/ (existent; cita no verificada a la captura)

7. [`L2|GB0006731235|R2021`] [V] «2021 Annual Results Announcement 09 Nov 2021 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2021-2022 · Nivell A · prova: El 09 Nov 2021 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2021). · URL: https://www.abfingredients.com/en/news-and-events/news/2021-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260719055247/https://www.abfingredients.com/en/news-and-events/news/2021-annual-results-announcement/ (existent; cita no verificada a la captura)

8. [`L2|GB0006731235|R2022`] [V] «2022 Annual Results Announcement 08 Nov 2022 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2022-2023 · Nivell A · prova: El 08 Nov 2022 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2022). · URL: https://www.abfingredients.com/en/news-and-events/news/2022-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260514160650/https://www.abfingredients.com/en/news-and-events/news/2022-annual-results-announcement/ (existent; cita no verificada a la captura)

9. [`L2|GB0006731235|R2023`] [V] «2023 Annual Results Announcement 07 Nov 2023 Financial George Weston, Chief Executive of Associated British Foods»
   Anys: 2023-2024 · Nivell A · prova: El 07 Nov 2023 George Weston signa com a Chief Executive d Associated British Foods (comunicat de resultats anuals de l exercici 2023). · URL: https://www.abfingredients.com/en/news-and-events/news/2023-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260617002913/https://www.abfingredients.com/en/news-and-events/news/2023-annual-results-announcement/ (existent; cita no verificada a la captura)

10. [`L2|GB0006731235|AR2019a`] [V] «George was appointed to the board in 1999 and took up his current appointment as Chief Executive in April 2005.»
   Anys: 2016-2019 · Nivell A · prova: Interval: George Weston es Chief Executive des d abril de 2005 i ho continua sent en la data de l informe (novembre de 2019). · URL: https://www.azucarera.es/wp-content/uploads/2019/11/ar2019b.pdf · Wayback: `pendent_verificacio_externa`

11. [`L2|GB0006731235|AR2019b`] [V] «George Weston (Chief Executive)»
   Anys: 2016-2019 · Nivell A · prova: L informe anual 2019 llista George Weston com a Executive director (Chief Executive). · URL: https://www.azucarera.es/wp-content/uploads/2019/11/ar2019b.pdf · Wayback: `pendent_verificacio_externa`

12. [`L2|GB0006731235|T2024a`] [V] «09/2024 Pre Close Period Trading Update 05 Sept 2024 Financial Trading Update 05 Sep 2024»
   Anys: 2024 · Nivell A · prova: Data del trading update: 5 de setembre de 2024. · URL: https://www.abfingredients.com/en/news-and-events/news/092024-pre-close-period-trading-update/ · Wayback: https://web.archive.org/web/20260617012935/https://www.abfingredients.com/en/news-and-events/news/092024-pre-close-period-trading-update/ (existent; cita no verificada a la captura)

13. [`L2|GB0006731235|T2024b`] [V] «George Weston, Chief Executive of Associated British Foods, said:»
   Anys: 2024 · Nivell A · prova: El 5/09/2024 George Weston es Chief Executive d Associated British Foods. · URL: https://www.abfingredients.com/en/news-and-events/news/092024-pre-close-period-trading-update/ · Wayback: https://web.archive.org/web/20260617012935/https://www.abfingredients.com/en/news-and-events/news/092024-pre-close-period-trading-update/ (existent; cita no verificada a la captura)

14. [`L2|GB0006731235|P2024`] [V] «George Weston, CEO of Associated British Foods, told Reuters in an interview after the group reported annual results.»
   Anys: 2024 · Nivell B · prova: El 5/11/2024 (resultats anuals) George Weston es CEO d Associated British Foods. · URL: https://www.rte.ie/news/business/2024/1105/1479133-associated-british-foods-results · Wayback: https://web.archive.org/web/20241107001332/https://www.rte.ie/news/business/2024/1105/1479133-associated-british-foods-results/ (existent; cita no verificada a la captura)

15. [`L2|GB0006731235|P2024d`] [V] «Updated / Tuesday, 5 Nov 2024»
   Anys: 2024 · Nivell B · prova: Data de la noticia: 5 de novembre de 2024. · URL: https://www.rte.ie/news/business/2024/1105/1479133-associated-british-foods-results · Wayback: https://web.archive.org/web/20241107001332/https://www.rte.ie/news/business/2024/1105/1479133-associated-british-foods-results/ (existent; cita no verificada a la captura)

16. [`L2|GB0006731235|I2025a`] [V] «2025 Interim Results Announcement 29 Apr 2025 Financial Associated British Foods plc results for the 24 weeks»
   Anys: 2024-2025 · Nivell A · prova: Data del comunicat: 29 d abril de 2025. · URL: https://www.abfingredients.com/en/news-and-events/news/2025-interim-results-announcement/ · Wayback: https://web.archive.org/web/20260719070107/https://www.abfingredients.com/en/news-and-events/news/2025-interim-results-announcement/ (existent; cita no verificada a la captura)

17. [`L2|GB0006731235|I2025b`] [V] «George Weston, Chief Executive of Associated British Foods, said:»
   Anys: 2024-2025 · Nivell A · prova: El 29/04/2025 George Weston es Chief Executive. · URL: https://www.abfingredients.com/en/news-and-events/news/2025-interim-results-announcement/ · Wayback: https://web.archive.org/web/20260719070107/https://www.abfingredients.com/en/news-and-events/news/2025-interim-results-announcement/ (existent; cita no verificada a la captura)

18. [`L2|GB0006731235|R2025a`] [V] «2025 Annual Results Announcement 05 Nov 2025 Financial Associated British Foods plc results for the 52 weeks ended 13 September 2025»
   Anys: 2025 · Nivell A · prova: Data del comunicat: 5 de novembre de 2025. · URL: https://www.abfingredients.com/en/news-and-events/news/2025-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260514163236/https://www.abfingredients.com/en/news-and-events/news/2025-annual-results-announcement/ (existent; cita no verificada a la captura)

19. [`L2|GB0006731235|R2025b`] [V] «George Weston, Chief Executive of Associated British Foods, said:»
   Anys: 2025 · Nivell A · prova: El 5/11/2025 George Weston es Chief Executive. · URL: https://www.abfingredients.com/en/news-and-events/news/2025-annual-results-announcement/ · Wayback: https://web.archive.org/web/20260514163236/https://www.abfingredients.com/en/news-and-events/news/2025-annual-results-announcement/ (existent; cita no verificada a la captura)

20. [`L2|GB0006731235|I2026a`] [V] «2026 Interim Results Announcement 21 Apr 2026 Financial Associated British Foods plc results for the 24 weeks ended 28 February 2026»
   Anys: 2025 · Nivell A · prova: Data del comunicat: 21 d abril de 2026. · URL: https://www.abfingredients.com/en/news-and-events/news/2026-interim-results-announcement/ · Wayback: https://web.archive.org/web/20260809020926/https://www.abfingredients.com/en/news-and-events/news/2026-interim-results-announcement/ (existent; cita no verificada a la captura)

21. [`L2|GB0006731235|I2026b`] [V] «George Weston, Chief Executive of Associated British Foods, said:»
   Anys: 2025 · Nivell A · prova: El 21/04/2026 George Weston continua sent Chief Executive (continuitat posterior al 31/10/2025). · URL: https://www.abfingredients.com/en/news-and-events/news/2026-interim-results-announcement/ · Wayback: https://web.archive.org/web/20260809020926/https://www.abfingredients.com/en/news-and-events/news/2026-interim-results-announcement/ (existent; cita no verificada a la captura)

### L2.13 Tesco PLC Registered Shares LS -,05 (`GB0008847096`)

- isin i anys: `GB0008847096`, 2016-2018 (n=3). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Dave Lewis → Dave Lewis (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A, B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: tescoplc.com (web oficial): 403 'Access Denied' (Akamai) a https://www.tescoplc.com/ i als PDF dels informes anuals 2017, 2018, 2019 i 2020 (/media/392373/68336_tesco_ar_digital_interactive_250417.pdf, /media/474793/tesco_ar_2018.pdf, /media/476422/tesco_ara2019_full_report_web.pdf, /media/755761/tes006_ar2020_web_updated_200505.pdf): original no obrible. Companies House (00445790): baixats els comptes anuals a 25/2/2017, 24/2/2018 i 23/2/2019 i el TM01 de David John Lewis (fitxers ch_aa2017.pdf, ch_aa2018.pdf, ch_aa2019.pdf, ch_tm01_lewis.pdf), pero son imatges escanejades sense capa de text i no hi ha OCR disponible: no s'hi pot verificar cap cita literal amb vq.py, no s'han fet servir. Si que s'ha pogut citar la llista d'officers (HTML, pagina 2). FCA National Storage Mechanism: l'API de cerca ha respost 400 'Invalid index' i no s'ha pogut consultar (un segon intent amb capçaleres Origin/Referer el va denegar el sistema de permisos i no s'ha insistit). sec.gov: 403. theguardian.com: pagina de bloqueig (200, 3 kB). itv.com: error HTTP/2. retail-week.com i thegrocer.co.uk: 405. expressandstar.com: 403. bbc.com/news/business-49906702: 404 (URL endevinada erronia). Oberts correctament: BBC News (cerca interna de bbc.co.uk per localitzar articles; articles de 18/11/2016, 4/10/2017, 11/1/2018, 10/10/2018, 10/4/2019, 2/10/2019, 7/10/2020), City A.M. (5/10/2016), RTE/Reuters (3/10/2018), Fortune/Reuters (5/10/2016, no citat), ii.co.uk (no citat). investegate i lse.co.uk nomes han sortit com a pista a WebSearch i no s'han usat.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Cap document de nivell A amb el titol 'chief executive' s'ha pogut verificar literalment: la web de l'emissor dona 403 i els informes anuals de Companies House son escanejats sense text (caldria OCR). La prova del titol de CEO es de nivell B (BBC, City A.M., RTE/Reuters); el nivell A (Companies House) nomes diu 'Director' amb dates 1/9/2014-30/9/2020. Doctorat ha de decidir si n'hi ha prou. · (2) Cap cita no es exactament del 31/10: cada any es prova amb una cita anterior i una de posterior a la data (interval de setmanes o mesos) mes l'absencia de canvi documentada; cal decidir si aquesta acotacio es acceptable. · (3) L'article de RTE es un teletip de Reuters republicat per RTE a la seva propia web (font indicada 'Source: Reuters'); s'ha tractat com a premsa de nivell B a la URL original de RTE, no com a copia de tercers.
- Cites:

1. [`L2|GB0008847096|c1`] [V] «Although chief executive Dave Lewis said prices at the retailer were down six per cent on a year ago»
   Anys: 2016 · Nivell B · prova: Dave Lewis era chief executive de Tesco el 5/10/2016 (resultats semestrals). · URL: https://www.cityam.com/tesco-posts-increase-uk-like-like-sales-but-profit-drops-28/ · Wayback: `pendent_verificacio_externa`

2. [`L2|GB0008847096|c2`] [V] «Tesco chief executive Dave Lewis has warned global suppliers not to artificially inflate their prices because of the fall in the pound.»
   Anys: 2016 · Nivell B · prova: Dave Lewis continuava sent chief executive de Tesco el 18/11/2016, després del 31/10/2016. · URL: https://www.bbc.co.uk/news/business-38023732 · Wayback: https://web.archive.org/web/20250816105846/https://www.bbc.co.uk/news/business-38023732 (existent; cita no verificada a la captura)

3. [`L2|GB0008847096|c3`] [V] «Tesco chief executive Dave Lewis has said the supermarket's turnaround is "very firmly on track" as sales rose for the seventh quarter in a row.»
   Anys: 2017 · Nivell B · prova: Dave Lewis era chief executive de Tesco el 4/10/2017. · URL: https://www.bbc.co.uk/news/business-41495322 · Wayback: https://web.archive.org/web/20260419062114/https://www.bbc.co.uk/news/business-41495322 (existent; cita no verificada a la captura)

4. [`L2|GB0008847096|c4`] [V] «Chief executive Dave Lewis said: "We have continued to outperform the market throughout this period»
   Anys: 2017 · Nivell B · prova: Dave Lewis continuava sent chief executive de Tesco l'11/1/2018, després del 31/10/2017. · URL: https://www.bbc.co.uk/news/business-42646021 · Wayback: https://web.archive.org/web/20260419032936/https://www.bbc.co.uk/news/business-42646021 (existent; cita no verificada a la captura)

5. [`L2|GB0008847096|c5`] [V] «Chief executive Dave Lewis has been rebuilding Tesco since 2014, when an accounting scandal capped a dramatic downturn in trading.»
   Anys: 2018 · Nivell B · prova: Dave Lewis era chief executive de Tesco el 3/10/2018 i ho era des del 2014. · URL: https://www.rte.ie/news/business/2018/1003/1000600-tesco-half-yearly-results · Wayback: `pendent_verificacio_externa`

6. [`L2|GB0008847096|c6`] [V] «Chief executive Dave Lewis said the group was on track to meet the "vast majority" of the turnaround goals he set when he was appointed four years ago after an accounting scandal.»
   Anys: 2018 · Nivell B · prova: Dave Lewis continuava sent chief executive de Tesco el 10/4/2019, després del 31/10/2018. · URL: https://www.bbc.co.uk/news/business-47877524 · Wayback: https://web.archive.org/web/20260418221159/https://www.bbc.co.uk/news/business-47877524 (existent; cita no verificada a la captura)

7. [`L2|GB0008847096|c7`] [V] «Ken Murphy, who started last week. He replaces Dave Lewis, who had been running the UK's biggest retailer since 2014.»
   Anys: 2018 · Nivell B · prova: Interval: Dave Lewis va dirigir Tesco des del 2014 fins que Ken Murphy el va substituir (finals de setembre/1 d'octubre de 2020). · URL: https://www.bbc.co.uk/news/business-54445399 · Wayback: https://web.archive.org/web/20260731101555/https://www.bbc.co.uk/news/business-54445399 (existent; cita no verificada a la captura)

8. [`L2|GB0008847096|c8`] [V] «Tesco's chief executive Dave Lewis is to leave next year after leading a turnaround plan for Britain's biggest supermarket chain.»
   Anys: 2018 · Nivell B · prova: El 2/10/2019 Dave Lewis encara era chief executive i la sortida era prevista per al 2020; cap canvi de CEO entre 2016 i 2018. · URL: https://www.bbc.co.uk/news/business-49903696 · Wayback: https://web.archive.org/web/20261109130627/https://www.bbc.co.uk/news/business-49903696 (existent; cita no verificada a la captura)

9. [`L2|GB0008847096|c9`] [V] «LEWIS, David John Correspondence address Tesco House, Shire Park, Kestrel Way, Welwyn Garden City, United Kingdom, AL7 1GA Role Resigned Director Date of birth March 1965 Appointed on 1 September 2014 Resigned on 30 September 2020»
   Anys: 2016-2018 · Nivell A · prova: Entrada de LEWIS, David John: conseller de Tesco PLC de l'1/9/2014 al 30/9/2020 (el registre diu 'Director', no 'CEO'; acota el mandat al consell). · URL: https://find-and-update.company-information.service.gov.uk/company/00445790/officers?page=2 · Wayback: https://web.archive.org/web/20240506204257/https://find-and-update.company-information.service.gov.uk/company/00445790/officers?page=2 (existent; cita no verificada a la captura)

### L2.14 Victrex PLC Registered Shares LS -,01 (`GB0009292243`)

- isin i anys: `GB0009292243`, 2018-2022 (n=5). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Jakob Sigurdsson → Jakob Sigurdsson (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Web oficial victrexplc.com: la pàgina https://www.victrexplc.com/investors/results-reports-and-presentations/ (200) només enllaça en HTML estàtic els documents de 2024-2026; els informes anuals 2018-2023 són a la pestanya 'Archive', que es carrega per una API interna (/umbraco/api/listing/GetListingItems) que NO s ha consultat (crida denegada pel classificador de permisos de l entorn), de manera que no s han obtingut les URL dels informes anuals contemporanis. Baixats i llegits: Annual Report 2024 (https://www.victrexplc.com/media/glmpw22b/victrex-plc-annual-report-2024.pdf, 200) i Annual Report 2025 (https://www.victrexplc.com/media/2brmqozs/victrex-plc-annual-report-2025.pdf, 200). URL fallides: https://www.victrexplc.com/en/investors/reports-and-presentations (404); https://www.victrexplc.com/investors-media/investor-overview (404); https://www.victrexplc.com/wp-content/uploads/2019/05/Victrex-plc-Interim-Results-Announcement-2019-FINAL-13-05-19.pdf (404); ESEF https://www.victrexplc.com/esef/213800UYNPHAUNHPXL67-2023-09-30/reports/213800UYNPHAUNHPXL67-2023-09-30-T01.xhtml i anàlegs 2022 i 2021 (404). Companies House (02793780): officers pàg. 1 i 2 (200; entrada de Sigurdsson a ?page=2) i filing-history pàg. 1-5 (200); baixats els comptes anuals dipositats dels exercicis 2020, 2021, 2022 i 2023 (PDF 200), però són imatges escanejades sense capa de text (pdftotext retorna buit), no verificables amb vq.py i no usats com a cita. WebSearch només ha donat còpies de tercers dels informes (financialreports.eu, sustainabilityreports.com, reports.ticker.app, investegate), no usades.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Exercici fiscal no natural (tanca el 30/09): el 31/10/t cau dins l exercici t+1. Cap informe anual contemporani (2019-2023) s ha pogut obrir a la web de l emissor; la prova dels cinc anys és d interval (nomenament 1/10/2017, taula del CEO per exercici 2018-2024 a l Annual Report 2024, continuïtat a 30/09/2024 i relleu 1/1/2026). Doctorat ha de decidir si n hi ha prou o si cal una cita contemporània per any. · (2) La taula 'CEO total remuneration' identifica el CEO per exercici sencer (un nom per columna), no en una data concreta; s interpreta que un sol nom per exercici implica el mateix CEO el 31/10. Les cites C3 i C4 són files de taula (verificades amb pdftotext -layout), no frases. · (3) Els comptes dipositats a Companies House per als exercicis 2020-2023 existeixen i s obren, però són escanejats sense text; caldria OCR per citar-los i no s ha fet perquè la cita no seria verificable literalment amb vq.py.
- Cites:

1. [`L2|GB0009292243|C1`] [V] «Jakob Sigurdsson was appointed as CEO on 1 October 2017. His first tranche of LTIPs was eligible to vest in 2020.»
   Anys: 2018-2022 · Nivell A · prova: Data efectiva d inici del mandat de CEO: 1/10/2017. · URL: https://www.victrexplc.com/media/glmpw22b/victrex-plc-annual-report-2024.pdf · Wayback: `pendent_verificacio_externa`

2. [`L2|GB0009292243|C2`] [V] «The total remuneration figures for the Chief Executive Officer during each of the last 10 financial years are shown in the table below.»
   Anys: 2018-2022 · Nivell A · prova: Encapçalament de la taula que identifica el CEO de cada un dels 10 darrers exercicis. · URL: https://www.victrexplc.com/media/glmpw22b/victrex-plc-annual-report-2024.pdf · Wayback: `pendent_verificacio_externa`

3. [`L2|GB0009292243|C3`] [V] «30 September 2024 2023 2022 2021 2020 2019 2018 2017 2016 2015»
   Anys: 2018-2022 · Nivell A · prova: Columnes de la taula: exercicis tancats el 30/09 de 2024 a 2015, en aquest ordre. · URL: https://www.victrexplc.com/media/glmpw22b/victrex-plc-annual-report-2024.pdf · Wayback: `pendent_verificacio_externa`

4. [`L2|GB0009292243|C4`] [V] «Sigurdsson Sigurdsson Sigurdsson Sigurdsson Sigurdsson Sigurdsson Sigurdsson Hummel Hummel Hummel»
   Anys: 2018-2022 · Nivell A · prova: A la mateixa taula, el CEO dels set exercicis 2024-2018 és (J O) Sigurdsson i el dels tres 2017-2015 és (D R) Hummel; un sol nom per exercici. · URL: https://www.victrexplc.com/media/glmpw22b/victrex-plc-annual-report-2024.pdf · Wayback: `pendent_verificacio_externa`

5. [`L2|GB0009292243|C5`] [V] «Leadership – our governance framework as at 30 September 2024»
   Anys: 2018-2022 · Nivell A · prova: Data de referència del quadre de govern (30/09/2024) on figura C6. · URL: https://www.victrexplc.com/media/glmpw22b/victrex-plc-annual-report-2024.pdf · Wayback: `pendent_verificacio_externa`

6. [`L2|GB0009292243|C6`] [V] «Chief Executive Officer: Jakob Sigurdsson»
   Anys: 2018-2022 · Nivell A · prova: Sigurdsson continua com a CEO el 30/09/2024 (posterior a tots els 31/10 de 2018-2022). · URL: https://www.victrexplc.com/media/glmpw22b/victrex-plc-annual-report-2024.pdf · Wayback: `pendent_verificacio_externa`

7. [`L2|GB0009292243|C7`] [V] «Jakob Sigurdsson will step down as CEO and be replaced by Dr James Routh on 1 January 2026.»
   Anys: 2018-2022 · Nivell A · prova: Fi del mandat de CEO: substituït l 1/1/2026; per tant CEO sense interrupció documentada fins llavors. · URL: https://www.victrexplc.com/media/2brmqozs/victrex-plc-annual-report-2025.pdf · Wayback: `pendent_verificacio_externa`

8. [`L2|GB0009292243|C9`] [V] «Date of birth March 1964 Appointed on 1 October 2017 Resigned on 6 February 2026»
   Anys: 2018-2022 · Nivell A · prova: Suport: Sigurdsson va ser administrador (director) de Victrex plc de l 1/10/2017 al 6/2/2026 (el registre no indica el càrrec de CEO). · URL: https://find-and-update.company-information.service.gov.uk/company/02793780/officers?page=2 · Wayback: `pendent_verificacio_externa`

### L2.15 Dechra Pharmaceuticals PLC Registered (`GB0009633180`)

- isin i anys: `GB0009633180`, 2018-2023 (n=6). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Ian Page → Ian Page (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A, B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Obert a dechra.com (HTTP 200): Scheme-document.pdf (idèntic a la pista FCA NSM NI-000078013, també 200), informes anuals FY2021 i FY2022, informe semestral a 31/12/2022, anuncis RNS de 30/11/2023 i 12/01/2024 (tots enllaçats des de https://www.dechra.com/documents-relating-to-possible-offer), i el comunicat https://www.dechra.com/jesper-nordengaard (també a dechra-us.com, 200). Premsa: northernfinancialreview.com 200. Fallats: https://www.dechra.com/investors/reports-and-presentations (404); informes anuals 2018, 2019, 2020 i 2023 a dechra.com no localitzats (provats patrons Files/Files/Dechra_s-annual-report-and-accounts-for-the-year-ended-30-June-AAAA.pdf, Corporate/Financial-reports/Archive/Annual-Report-and-Accounts-AAAA.pdf, Dechra-ARAAAA.pdf: tots 404; l'arxiu sí que serveix 2002 i 2010). Companies House (company 03369634): els comptes de grup FY2018, FY2019, FY2020, FY2023 i FY2024 es baixen (200) però són PDF escanejats sense capa de text (pdftotext retorna buit), de manera que no se'n pot verificar cap cita literal; la pàgina d'officers (200) dona Ian David Page com a director del 13/06/1997 al 10/06/2024 (no indica el càrrec de CEO, no usada com a cita). Premsa bloquejada: yorkshirepost.co.uk i pocklingtonpost.co.uk (403, pàgina de verificació), thebusinessdesk.com (403). L'API de cerca de l'FCA NSM ha retornat 'Invalid index'. MarketScreener, investegate, lse.co.uk i sharecast només com a pista.
- Dubtes de metodologia per a Doctorat (no decidits): (1) 2018 i 2019 queden provats només per cites d'interval (inici 5/11/2001, continuïtat documentada el 2021 i 2023, fi el 10/06/2024), sense document contemporani amb text verificable: els comptes anuals d'aquells exercicis a Companies House són imatges escanejades. Doctorat ha de decidir si l'interval és suficient o si cal OCR dels originals de Companies House. · (2) Les cites C5, C6 i C7 són el mateix text literal (bloc de contactes 'Ian Page, Chief Executive Officer') en tres documents diferents; la data la dona cada document, no la cita. · (3) C8 diu literalment 'retirement of Ian Page effective June 10, 2024' sense dir 'com a CEO' dins la mateixa frase; el càrrec surt de C9 i del relleu per Jesper Nordengaard. A més, des del gener de 2024 l'empresa ja no cotitza (Dechra Pharmaceuticals Limited), fet que no afecta els anys del panell.
- Cites:

1. [`L2|GB0009633180|C1`] [V] «his continuous employment commenced on 1 May 1989, and his appointment as Chief Executive Officer commenced on 5 November 2001 and will continue until terminated by either Ian David Page»
   Anys: 2018-2023 · Nivell A · prova: Inici del mandat d'Ian Page com a CEO: 5/11/2001; contracte vigent a la data del document (juny 2023). · URL: https://www.dechra.com/Files/Files/Scheme-document.pdf · Wayback: `pendent_verificacio_externa`

2. [`L2|GB0009633180|C2`] [V] «Over this period, Ian Page, our Chief Executive Officer, has had one base salary increase of 4% in the 2020 financial year. Ian Page’s salary had not previously been increased since 2016.»
   Anys: 2018-2020 · Nivell A · prova: Ian Page és el CEO a l'exercici 2021 i el seu salari de CEO es remunta com a mínim al 2016 (continuïtat 2016-2021). · URL: https://www.dechra.com/Files/Files/Dechra_s-annual-report-and-accounts-for-the-year-ended-30-June-2021.pdf · Wayback: `pendent_verificacio_externa`

3. [`L2|GB0009633180|C3`] [V] «Ian Page Chief Executive Officer 6 September 2021»
   Anys: 2020 · Nivell A · prova: Ian Page signa com a CEO l'informe de l'exercici que inclou el 31/10/2020. · URL: https://www.dechra.com/Files/Files/Dechra_s-annual-report-and-accounts-for-the-year-ended-30-June-2021.pdf · Wayback: `pendent_verificacio_externa`

4. [`L2|GB0009633180|C4`] [V] «Signed by order of the Board. Ian Page Chief Executive Officer Paul Sandland Chief Financial Officer 5 September 2022»
   Anys: 2021 · Nivell A · prova: Ian Page signa com a CEO l'informe de l'exercici que inclou el 31/10/2021. · URL: https://www.dechra.com/Files/Files/Dechra_s-annual-report-and-accounts-for-the-year-ended-30-June-2022.pdf · Wayback: `pendent_verificacio_externa`

5. [`L2|GB0009633180|C5`] [V] «Ian Page, Chief Executive Officer Paul Sandland, Chief Financial Officer»
   Anys: 2022 · Nivell A · prova: Ian Page és el CEO en l'informe del semestre 1/7/2022-31/12/2022, que inclou el 31/10/2022. · URL: https://www.dechra.com/Admin/Public/DWSDownload.aspx?File=%2fFiles%2fFiles%2fDechra_s-half-yearly-financial-report-for-the-period-ended-31-December-2022.pdf · Wayback: `pendent_verificacio_externa`

6. [`L2|GB0009633180|C6`] [V] «Ian Page, Chief Executive Officer Paul Sandland, Chief Financial Officer»
   Anys: 2023 · Nivell A · prova: Ian Page segueix com a CEO el 30/11/2023 (després del 31/10/2023). · URL: https://www.dechra.com/Files/Files/Diana-Final-RNS-Update-on-Conditions-29-11-2023-124231702-v3-002.pdf · Wayback: `pendent_verificacio_externa`

7. [`L2|GB0009633180|C7`] [V] «Ian Page, Chief Executive Officer Paul Sandland, Chief Financial Officer»
   Anys: 2023 · Nivell A · prova: Ian Page segueix com a CEO el 12/01/2024. · URL: https://www.dechra.com/Files/Files/2024-01-12-Court-Sanction-Announcement.pdf · Wayback: `pendent_verificacio_externa`

8. [`L2|GB0009633180|C8`] [V] «today announces the appointment of Jesper Nordengaard as its CEO and retirement of Ian Page effective June 10, 2024»
   Anys: 2018-2023 · Nivell A · prova: Fi del mandat: Ian Page es retira i Jesper Nordengaard és CEO amb efecte 10/06/2024. · URL: https://www.dechra.com/jesper-nordengaard · Wayback: https://web.archive.org/web/20241114185348/https://www.dechra.com/jesper-nordengaard (existent; cita no verificada a la captura)

9. [`L2|GB0009633180|C9`] [V] «It has been a privilege to lead the business as CEO over the last 23 years.»
   Anys: 2018-2019 · Nivell A · prova: Mandat continu d'Ian Page com a CEO durant els 23 anys anteriors a maig de 2024. · URL: https://www.dechra.com/jesper-nordengaard · Wayback: https://web.archive.org/web/20241114185348/https://www.dechra.com/jesper-nordengaard (existent; cita no verificada a la captura)

10. [`L2|GB0009633180|C10`] [V] «Since the Initial Public Offering in 2000 and my appointment as chief executive officer in 2001, being a listed company has served Dechra well»
   Anys: 2023 · Nivell B · prova: Ian Page, CEO a l'octubre de 2023, nomenat CEO el 2001. · URL: https://northernfinancialreview.com/2023/10/12/dechra-revenue-rises-to-761m-before-it-goes-private · Wayback: https://web.archive.org/web/20260411155253/https://northernfinancialreview.com/2023/10/12/dechra-revenue-rises-to-761m-before-it-goes-private/ (existent; cita no verificada a la captura)

### L2.16 Paysafe Group PLC Registered Shares LS (`GB0034264548`)

- isin i anys: `GB0034264548`, 2016-2017 (n=2). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Joel Leonoff → Joel Leonoff (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Obert (HTTP 200) a paysafe.com/en/paysafegroup/news/detail/: paysafe-group-appoints-philip-mchugh-as-ceo (30/05/2019), paysafe-group-plc-trading-update (08/11/2016), unaudited-interim-results-for-the-6-months-ended-30-june-2016, paysafe-group-plc-trading-update-for-year-ended-31-december-2016 (12/01/2017), paysafe-group-plc-final-results-for-year-ended-31-december-2016 (07/03/2017), ...fds-excellence-awards (17/05/2017), paysafe-wins-record-number-of-awards-in-2017 (23/01/2018), stuart-c-harvey-jr-appointed-chairman-of-paysafe-1 (09/04/2018); i financemagnates.com (200). Fallits: globenewswire.com/news-release/2019/05/30/1859525/... (403; el mateix comunicat s'ha obert a paysafe.com); paysafe.com/fileadmin/content/pdf/Paysafe_Annual_Report_2016.pdf (404, URL provada a cegues); efts.sec.gov full-text search (403) i sec.gov browse-edgar (403, bloqueig d'eina automatitzada); paymentexpert.com (403); cinc URL endevinades de paysafe.com per a semestrals 2017 / finalització de l'scheme (404). No s'ha localitzat l'informe anual 2016 ni el scheme document de 31/08/2017 a la web de l'emissor; WebSearch no ha donat cap comunicat de paysafe.com datat d'octubre a desembre de 2017. ir.paysafe.com (200) és el web de la successora Paysafe Limited (NYSE) i no s'hi ha buscat l'arxiu de la plc.
- Dubtes de metodologia per a Doctorat (no decidits): (1) 2017: no hi ha document de l'emissor datat entre octubre i desembre de 2017; la prova del 31/10/2017 és per interval (c1/c2) més cites contemporànies abans (17/05/2017) i després (23/01/2018). Doctorat ha de decidir si n'hi ha prou. · (2) El comunicat de 2019 diu 'President and CEO since 2008' referint-se a 'Paysafe, originally Optimal Payments'; l'entitat cotitzada del panell (Paysafe Group plc, abans Optimal Payments plc / Neovia) podria haver-lo tingut com a CEO només a partir d'una data posterior (pista no verificada). No afecta 2016-2017, però sí la lectura literal de l'interval. · (3) Paysafe Group plc va deixar de cotitzar el desembre de 2017 (adquisició per Blackstone/CVC, pista de WebSearch no verificada amb document obert); la fila 2017 es manté al panell perquè el 31/10/2017 encara cotitzava. · (4) c3 i c10 són el títol i la data de capçalera de la pàgina web (vq: html_sense_etiquetes), no una frase del cos del comunicat.
- Cites:

1. [`L2|GB0034264548|c1`] [V] «Leonoff founded Paysafe, originally Optimal Payments, in 1997 and has held the position of President and CEO since 2008.»
   Anys: 2016-2017 · Nivell A · prova: Interval: Leonoff President i CEO de manera continuada des de 2008 fins al comunicat de 30/05/2019; cobreix 31/10/2016 i 31/10/2017. · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-appoints-philip-mchugh-as-ceo/ · Wayback: https://web.archive.org/web/20260520172624/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-appoints-philip-mchugh-as-ceo/ (existent; cita no verificada a la captura)

2. [`L2|GB0034264548|c2`] [V] «today announced the appointment of Philip McHugh as its CEO, effective June 24, 2019. McHugh replaces Joel Leonoff»
   Anys: 2016-2017 · Nivell A · prova: Fi del mandat: el successor substitueix Leonoff amb efecte 24/06/2019, posterior al 31/10/2017. · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-appoints-philip-mchugh-as-ceo/ · Wayback: https://web.archive.org/web/20260520172624/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-appoints-philip-mchugh-as-ceo/ (existent; cita no verificada a la captura)

3. [`L2|GB0034264548|c3`] [V] «Paysafe Group plc Trading Update Nov 08, 2016»
   Anys: 2016 · Nivell A · prova: Data del document: 8 de novembre de 2016. · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-plc-trading-update/ · Wayback: https://web.archive.org/web/20260607200911/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-plc-trading-update/ (existent; cita no verificada a la captura)

4. [`L2|GB0034264548|c4`] [V] «Paysafe President and Chief Executive Officer Joel Leonoff said: “I am delighted to report that we are on track to achieve the upgraded revenue and adjusted EBITDA projections for the current financial year»
   Anys: 2016 · Nivell A · prova: Leonoff és President i CEO el 08/11/2016 (vuit dies després del 31/10/2016). · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-plc-trading-update/ · Wayback: https://web.archive.org/web/20260607200911/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-group-plc-trading-update/ (existent; cita no verificada a la captura)

5. [`L2|GB0034264548|c5`] [V] «Commenting on the results, Paysafe President and Chief Executive Officer Joel Leonoff said:»
   Anys: 2016 · Nivell A · prova: Leonoff és President i CEO el 10/08/2016 (abans del 31/10/2016). · URL: https://www.paysafe.com/en/paysafegroup/news/detail/unaudited-interim-results-for-the-6-months-ended-30-june-2016/ · Wayback: https://web.archive.org/web/20260615180315/https://www.paysafe.com/en/paysafegroup/news/detail/unaudited-interim-results-for-the-6-months-ended-30-june-2016/ (existent; cita no verificada a la captura)

6. [`L2|GB0034264548|c6`] [V] «LONDON (10 August 2016) – Paysafe Group plc»
   Anys: 2016 · Nivell A · prova: Data del document c5. · URL: https://www.paysafe.com/en/paysafegroup/news/detail/unaudited-interim-results-for-the-6-months-ended-30-june-2016/ · Wayback: https://web.archive.org/web/20260615180315/https://www.paysafe.com/en/paysafegroup/news/detail/unaudited-interim-results-for-the-6-months-ended-30-june-2016/ (existent; cita no verificada a la captura)

7. [`L2|GB0034264548|c7`] [V] «Paysafe President and Chief Executive Officer Joel Leonoff said Brian’s leadership had been an inspiration»
   Anys: 2017 · Nivell A · prova: Leonoff és President i CEO el 17/05/2017 (abans del 31/10/2017). · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-s-brian-mcarthur-muscroft-named-inspirational-finance-director-of-the-year-at-2017-fds-excellence-awards/ · Wayback: https://web.archive.org/web/20260419210133/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-s-brian-mcarthur-muscroft-named-inspirational-finance-director-of-the-year-at-2017-fds-excellence-awards/ (existent; cita no verificada a la captura)

8. [`L2|GB0034264548|c8`] [V] «LONDON, 17 May 2017 – Brian McArthur-Muscroft, Chief Financial Officer at leading global payments provider Paysafe»
   Anys: 2017 · Nivell A · prova: Data del document c7. · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-s-brian-mcarthur-muscroft-named-inspirational-finance-director-of-the-year-at-2017-fds-excellence-awards/ · Wayback: https://web.archive.org/web/20260419210133/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-s-brian-mcarthur-muscroft-named-inspirational-finance-director-of-the-year-at-2017-fds-excellence-awards/ (existent; cita no verificada a la captura)

9. [`L2|GB0034264548|c9`] [V] «President and Chief Executive Officer at Paysafe, Joel Leonoff, commented:»
   Anys: 2017 · Nivell A · prova: Leonoff és President i CEO el 23/01/2018 (després del 31/10/2017). · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-wins-record-number-of-awards-in-2017/ · Wayback: https://web.archive.org/web/20260212063140/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-wins-record-number-of-awards-in-2017/ (existent; cita no verificada a la captura)

10. [`L2|GB0034264548|c10`] [V] «Paysafe wins record number of awards in 2017 Jan 23, 2018»
   Anys: 2017 · Nivell A · prova: Data del document c9. · URL: https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-wins-record-number-of-awards-in-2017/ · Wayback: https://web.archive.org/web/20260212063140/https://www.paysafe.com/en/paysafegroup/news/detail/paysafe-wins-record-number-of-awards-in-2017/ (existent; cita no verificada a la captura)

### L2.17 Investec PLC Registered Shares LS -,00022) (`GB00B17BBQ50`)

- isin i anys: `GB00B17BBQ50`, 2016-2017 (n=2). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Stephen Koseff → Stephen Koseff (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Exercici fiscal d'Investec: 1 d'abril-31 de març. Baixats de investec.com (HTTP 200, PDF): informe abreujat 2017 (.../investor-centre/equity/investec-group-2017/Annual-Report.pdf), informe anual 2018 Vol 1 i informe anual 2019 Vol 1 (.../group-financial-results/2018|2019/...). També baixats sense fer-los servir com a cita: Vol 2 i Vol 3 de 2017 i el SENS de resultats a 31/3/2017. Fallits: https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2017/Investec-DLC-annual-report-volume-1.PDF (403, pàgina de bloqueig; variant .pdf en minúscules 404); pàgines HTML de investec.com (group-financial-results.html i stephen-koseff.html: 403); cinc URL endevinades d'informes 2017/2018 (404). WebSearch només per localitzar URL.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Investec és una estructura de doble cotització (Investec plc + Investec Limited) amb un sol consell i un sol group CEO; les cites són dels informes del grup DLC, no d'un document exclusiu d'Investec plc (ISIN GB00B17BBQ50). · (2) Per al 2016 la cita prové de l'informe abreujat ('integrated annual review and summary financial statements 2017'), perquè el Vol 1 complet de 2017 retorna 403 a la URL original; és igualment un document de l'emissor a la seva web. · (3) Les cites C1/C3 identifiquen el CEO per a tot l'exercici fiscal (no per al dia 31/10 literalment); la cobertura del 31/10 es dedueix del fet que no hi ha cap canvi de CEO documentat fins a l'1/10/2018 (C5).
- Cites:

1. [`L2|GB00B17BBQ50|C1`] [V] «The payment and deferral profile of the remuneration awarded to S Koseff (CEO) and B Kantor (MD) during the 2017 financial year»
   Anys: 2016 · Nivell A · prova: Koseff era CEO durant l'exercici 2017 (abril 2016-març 2017), que inclou el 31/10/2016 · URL: https://www.investec.com/content/dam/investor-relations/investor-centre/equity/investec-group-2017/Annual-Report.pdf · Wayback: `pendent_verificacio_externa`

2. [`L2|GB00B17BBQ50|C2`] [V] «Stephen Koseff, group chief executive officer»
   Anys: 2016 · Nivell A · prova: Fitxa de conseller a l'informe de l'exercici tancat el 31/3/2017: Koseff és group CEO · URL: https://www.investec.com/content/dam/investor-relations/investor-centre/equity/investec-group-2017/Annual-Report.pdf · Wayback: `pendent_verificacio_externa`

3. [`L2|GB00B17BBQ50|C3`] [V] «The payment and deferral profile of the remuneration awarded to S Koseff (CEO) and B Kantor (MD) during the 2018 financial year»
   Anys: 2017 · Nivell A · prova: Koseff era CEO durant l'exercici 2018 (abril 2017-març 2018), que inclou el 31/10/2017 · URL: https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2018/FINAL-Investec-DLC-Vol%201-15-June-2018.pdf · Wayback: https://web.archive.org/web/20251006115950/https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2018/FINAL-Investec-DLC-Vol%201-15-June-2018.pdf (existent; cita no verificada a la captura)

4. [`L2|GB00B17BBQ50|C4`] [V] «In terms of the group’s succession announcement made on 6 February 2018, Stephen Koseff (current CEO) and Bernard Kantor (current MD) will step down from these roles on 1 October 2018.»
   Anys: 2017 · Nivell A · prova: Koseff encara és CEO al juny de 2018 i deixarà el càrrec l'1/10/2018 · URL: https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2018/FINAL-Investec-DLC-Vol%201-15-June-2018.pdf · Wayback: https://web.archive.org/web/20251006115950/https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2018/FINAL-Investec-DLC-Vol%201-15-June-2018.pdf (existent; cita no verificada a la captura)

5. [`L2|GB00B17BBQ50|C5`] [V] «S Koseff stepped down as group CEO on 1 October 2018.»
   Anys: 2016-2017 · Nivell A · prova: Data efectiva de fi del mandat de Koseff com a group CEO: 1/10/2018 (posterior al 31/10/2017) · URL: https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2019/investec-dlc-vol-1-annual-report-2019.pdf · Wayback: https://web.archive.org/web/20240715051352/https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2019/investec-dlc-vol-1-annual-report-2019.pdf (existent; cita no verificada a la captura)

### L2.18 BBA Aviation PLC Registered Shares LS (`GB00B1FP8915`)

- isin i anys: `GB00B1FP8915`, 2017 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Wayne Edmunds → Wayne Edmunds (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R2 (CEO interí). Nivell de font: A, B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: 1) Web de l'emissor/successora: https://www.bbaaviation.com/ -> error del proxy (CONNECT 502, domini no servit); https://www.signatureaviation.com/investors -> 404; dues URL conjecturals de l'informe anual 2017 sota signatureaviation.com/~/media/... -> 404; sitemaps de signatureaviation.com (static.xml, news.xml) oberts: ja no hi ha secció d'inversors ni informes anuals ni comunicats de 2017-2018. 2) Companies House (societat 00053688, ara Signature Aviation Limited): llista d'officers oberta (200) -> cites C8-C10. Historial de presentacions obert (pàgines 4-12); baixats els comptes de grup a 31/12/2017 (presentats el 18/5/2018): https://find-and-update.company-information.service.gov.uk/company/00053688/filing-history/MzIwNTExODkyOGFkaXF6a2N4/document?format=pdf&download=0 -> 200, PDF de 184 pàgines ESCANEJAT sense capa de text (pdftotext retorna 0 caràcters), de manera que vq.py no hi pot verificar cap cita (FAIL). Inspecció visual de la pàgina 47 del PDF (Board of Directors): la biografia de Wayne Edmunds hi porta el títol 'Interim Group Chief Executive' i diu que va entrar al consell l'agost de 2013 i que va esdevenir Interim Group Chief Executive l'1 de juliol de 2017; NO s'inclou com a cita perquè no és verificable amb vq.py (no hi ha OCR disponible a l'entorn; la instal·lació d'un OCR va ser denegada).  3) Regulador/borsa: API del National Storage Mechanism de la FCA -> 'Invalid index' i un segon intent denegat per l'entorn; londonstockexchange.com/news-article/... -> redirigeix a la portada de notícies (pàgina JS, sense contingut). SEC EDGAR (proxy DEF 14A 2019 de MSCI Inc., https://www.sec.gov/Archives/edgar/data/1408198/000119312519070934/d685466ddef14a.htm) -> 403; cerca de text complet efts.sec.gov -> 403; https://ir.msci.com/board-directors/wayne-edmunds -> 403. 4) Document d'una tercera cotitzada: informe anual 2017 de Dialight plc a dialight.com -> 200, PDF amb text -> C1-C3. 5) Premsa: ainonline.com (dues notícies, 200) -> C4, C5; corporatejetinvestor.com (200) -> C6, C7; businessairportinternational.com (200, notícia del 26/6/2017 coherent, no usada com a cita); reuters.com -> 401; sharecast.com -> 403; aviationweek.com -> bucle de redireccions al login. MarketScreener, shareprices, lse.co.uk i Yahoo (còpies de RNS/Reuters) només com a pista, no usades.
- Dubtes de metodologia per a Doctorat (no decidits): (1) L'únic document del mateix emissor que cobreix el 31/10/2017 (comptes de grup 2017 a Companies House) és un PDF escanejat sense capa de text: la frase es llegeix a la imatge (p. 47 del PDF: Wayne Edmunds, Interim Group Chief Executive, des de l'1 de juliol de 2017) però no es pot verificar amb vq.py. Cal decidir si s'admet una cita transcrita/OCR d'un document de registre oficial escanejat. · (2) Les cites C1-C3 són de l'informe anual d'una tercera empresa cotitzada (Dialight plc, de la qual Edmunds era president), no de l'emissor. S'han classificat com a nivell B; cal decidir si aquest tipus de document compta com a A, B o només com a pista. · (3) Les cites C4-C7 són de premsa sectorial especialitzada (Aviation International News, Corporate Jet Investor), no de premsa econòmica generalista; cal decidir si compleixen el nivell B. L'article d'AIN del 20/6/2017 és parcialment de pagament: la cita és al fragment obert. · (4) Les cites de Companies House (C8-C10) proven dates d'administrador, no el càrrec de CEO; només acoten l'interval en combinació amb les altres. · (5) La data exacta d'inici difereix lleugerament segons la font: sortida de Pryce el 30/6/2017 (AIN, Companies House) i inici d'Edmunds l'1/7/2017 (informe anual de l'emissor, llegit a la imatge). No afecta el 31/10/2017.
- Cites:

1. [`L2|GB00B1FP8915|C1`] [V] «As announced on 5 June 2017, Wayne Edmunds was appointed interim CEO at BBA Aviation.»
   Anys: 2017 · Nivell B · prova: Nomenament de Wayne Edmunds com a CEO interí de BBA Aviation, anunciat el 5/6/2017 · URL: https://www.dialight.com/wp-content/uploads/2022/07/21617_dialight_ar17_222_final.pdf · Wayback: https://web.archive.org/web/20230703010445/https://www.dialight.com/wp-content/uploads/2022/07/21617_dialight_ar17_222_final.pdf (existent; cita no verificada a la captura)

2. [`L2|GB00B1FP8915|C2`] [V] «Wayne Edmunds will be stepping down as interim CEO of BBA Aviation on 1 April.»
   Anys: 2017 · Nivell B · prova: Edmunds continuava com a CEO interí de BBA Aviation en la data de l'informe (exercici 2017, publicat el 2018) i deixaria el càrrec l'1 d'abril · URL: https://www.dialight.com/wp-content/uploads/2022/07/21617_dialight_ar17_222_final.pdf · Wayback: https://web.archive.org/web/20230703010445/https://www.dialight.com/wp-content/uploads/2022/07/21617_dialight_ar17_222_final.pdf (existent; cita no verificada a la captura)

3. [`L2|GB00B1FP8915|C3`] [V] «Interim Chief Executive of BBA Aviation plc until 1 April 2018 (after which he will continue on the Board as a Non-Executive Director).»
   Anys: 2017 · Nivell B · prova: Edmunds és Interim Chief Executive de BBA Aviation plc fins a l'1/4/2018 · URL: https://www.dialight.com/wp-content/uploads/2022/07/21617_dialight_ar17_222_final.pdf · Wayback: https://web.archive.org/web/20230703010445/https://www.dialight.com/wp-content/uploads/2022/07/21617_dialight_ar17_222_final.pdf (existent; cita no verificada a la captura)

4. [`L2|GB00B1FP8915|C4`] [V] «Simon Pryce, who has served as CEO of BBA Aviation for the past 10 years, is stepping down on June 30. Wayne Edmunds, a non-executive director of the group since 2013, will serve as interim CEO until a permanent successor is named.»
   Anys: 2017 · Nivell B · prova: Pryce deixa el càrrec de CEO el 30/6/2017 i Edmunds el substitueix com a CEO interí · URL: https://www.ainonline.com/aviation-news/business-aviation/2017-06-20/simon-pryce-depart-bba-aviation-end-june · Wayback: https://web.archive.org/web/20260519091547/https://www.ainonline.com/aviation-news/business-aviation/2017-06-20/simon-pryce-depart-bba-aviation-end-june (existent; cita no verificada a la captura)

5. [`L2|GB00B1FP8915|C5`] [V] «Simon Pryce, who has served as CEO of BBA Aviation for the past 10 years, stepped down on June 30.»
   Anys: 2017 · Nivell B · prova: Sortida efectiva de Pryce el 30/6/2017 (ja en passat) · URL: https://ainonline.com/aviation-news/business-aviation/2017-08-06/people-aviation-august-2017 · Wayback: https://web.archive.org/web/20260612083901/https://www.ainonline.com/aviation-news/business-aviation/2017-08-06/people-aviation-august-2017 (existent; cita no verificada a la captura)

6. [`L2|GB00B1FP8915|C6`] [V] «Interim group CEO Wayne Edmunds will step down on 1 April, remaining on the board as a non-executive director.»
   Anys: 2017 · Nivell B · prova: El 2/1/2018 Edmunds encara és CEO interí del grup i ho serà fins a l'1 d'abril · URL: https://www.corporatejetinvestor.com/news/bba-aviation-appoints-new-ceo-614/ · Wayback: https://web.archive.org/web/20260305234859/https://www.corporatejetinvestor.com/news/bba-aviation-appoints-new-ceo-614/ (existent; cita no verificada a la captura)

7. [`L2|GB00B1FP8915|C7`] [V] «Johnstone (pictured) will take up his new role on 1 April 2018 and will be based in Orlando, Florida.»
   Anys: 2017 · Nivell B · prova: El successor (Mark Johnstone, group chief executive) no assumeix el càrrec fins a l'1/4/2018 · URL: https://www.corporatejetinvestor.com/news/bba-aviation-appoints-new-ceo-614/ · Wayback: https://web.archive.org/web/20260305234859/https://www.corporatejetinvestor.com/news/bba-aviation-appoints-new-ceo-614/ (existent; cita no verificada a la captura)

8. [`L2|GB00B1FP8915|C8`] [V] «Date of birth December 1961 Appointed on 11 June 2007 Resigned on 30 June 2017»
   Anys: 2017 · Nivell A · prova: Simon Pryce deixa de ser administrador el 30/6/2017 (coherent amb la fi del seu mandat de CEO) · URL: https://find-and-update.company-information.service.gov.uk/company/00053688/officers · Wayback: https://web.archive.org/web/20220121171646/https://find-and-update.company-information.service.gov.uk/company/00053688/officers (existent; cita no verificada a la captura)

9. [`L2|GB00B1FP8915|C9`] [V] «Date of birth September 1968 Appointed on 1 April 2018 Resigned on 9 June 2021»
   Anys: 2017 · Nivell A · prova: Mark Johnstone no entra al consell fins a l'1/4/2018 (posterior al 31/10/2017) · URL: https://find-and-update.company-information.service.gov.uk/company/00053688/officers · Wayback: https://web.archive.org/web/20220121171646/https://find-and-update.company-information.service.gov.uk/company/00053688/officers (existent; cita no verificada a la captura)

10. [`L2|GB00B1FP8915|C10`] [V] «Date of birth February 1956 Appointed on 7 August 2013 Resigned on 1 June 2021»
   Anys: 2017 · Nivell A · prova: Wayne Edmunds és administrador de la societat de manera contínua del 7/8/2013 a l'1/6/2021, període que inclou el 31/10/2017 (el registre no en diu el càrrec executiu) · URL: https://find-and-update.company-information.service.gov.uk/company/00053688/officers · Wayback: https://web.archive.org/web/20220121171646/https://find-and-update.company-information.service.gov.uk/company/00053688/officers (existent; cita no verificada a la captura)

### L2.19 Whitbread PLC Reg. Shares LS -,76797385 (`GB00B1KJJ408`)

- isin i anys: `GB00B1KJJ408`, 2016-2020, 2022 (n=6). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Alison Brittain → Alison Brittain (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Web oficial de l emissor: pàgina https://www.whitbread.co.uk/investors/results-reports-and-presentations/ (200) i índex de mitjans de WordPress https://www.whitbread.co.uk/wp-json/wp/v2/media?search=... (200) per localitzar els PDF a cdn.whitbread.co.uk; tots els documents citats s han baixat amb 200 de la URL original. Oberts: informes anuals 2015/16, 2016/17, 2017/18, 2019/20, 2020/21, 2021/22 (Whitbread_AR21-1.pdf), 2022/23 (Whitbread_AR22_Interactive.pdf), 2023/24; comunicats de resultats semestrals d octubre de 2016, 2017, 2018, 2019, 2020 i 2022; declaració S430(2B) sobre Alison Brittain (S4302B-statement-for-Alson-Brittain.pdf, no citada perquè el text extret té lligadures trencades). Fallits: l informe anual 2018/19 no apareix a l índex de mitjans; URL endevinades amb 403: cdn.whitbread.co.uk/media/2026/07/2019-annual-report-and-accounts.pdf, /2019/05/2019-annual-report-and-accounts.pdf, /2019/04/2019-annual-report-and-accounts.pdf, i igualment /2026/07/, /2017/05/ i /2017/04/2017-annual-report-and-accounts.pdf (l informe 2016/17 sí que s ha trobat com a whitbread_interactive_2017.pdf), /2026/07/Whitbread_AR20.pdf i Whitbread_AR20-1.pdf (403); https://www.whitbread.co.uk/investors/annual-reports/ (404). No s ha consultat Companies House (pista de la base) perquè els documents de l emissor ja cobreixen tots els anys; no s ha fet servir WebSearch.
- Dubtes de metodologia per a Doctorat (no decidits): (1) La cita actual de la base per a aquests anys (Companies House, «BRITTAIN, Alison Jane») prova que era administradora, no que fos CEO; es proposa substituir-la o complementar-la amb les cites W01-W19. Decisió de Doctorat. · (2) Les cites W04, W07, W12 i W15 són blocs de signatura (nom, càrrec i data en línies consecutives del PDF) i les cites de data W08, W10, W13 i W16 són capçaleres (títol i data en línies consecutives); són fragments contigus del text extret, però no frases. Doctorat ha de dir si accepta aquest tipus de cita. · (3) Per al 2018 no s ha pogut obrir l informe anual 2018/19; l any es prova amb el comunicat del 23/10/2018 (vuit dies abans del 31/10) més l interval de mandat (desembre 2015 - 17/1/2023). W01 dona només el mes d inici (December 2015), no el dia.
- Cites:

1. [`L2|GB00B1KJJ408|W01`] [V] «In September 2015, Alison Brittain joined Whitbread as Chief Executive Designate before taking over as Chief Executive in December.»
   Anys: 2016-2020, 2022 · Nivell A · prova: Inici del mandat: Brittain assumeix el càrrec de Chief Executive el desembre de 2015 · URL: https://cdn.whitbread.co.uk/media/2026/07/Annual_Report_and_Accounts_2015_16.pdf · Wayback: `pendent_verificacio_externa`

2. [`L2|GB00B1KJJ408|W02`] [V] «Released : 25 October 2016»
   Anys: 2016 · Nivell A · prova: Data del comunicat de resultats semestrals: 25 d octubre de 2016 · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread-Interim-Results.pdf · Wayback: `pendent_verificacio_externa`

3. [`L2|GB00B1KJJ408|W03`] [V] «Alison Brittain, Chief Executive, said:»
   Anys: 2016 · Nivell A · prova: Brittain és Chief Executive al comunicat del 25/10/2016 · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread-Interim-Results.pdf · Wayback: `pendent_verificacio_externa`

4. [`L2|GB00B1KJJ408|W04`] [V] «Alison Brittain Chief Executive 24 April 2017»
   Anys: 2016-2017 · Nivell A · prova: Brittain signa com a Chief Executive l informe de l exercici 2016/17 el 24/4/2017 · URL: https://cdn.whitbread.co.uk/media/2026/07/whitbread_interactive_2017.pdf · Wayback: `pendent_verificacio_externa`

5. [`L2|GB00B1KJJ408|W05`] [V] «Released : 24 October 2017»
   Anys: 2017 · Nivell A · prova: Data del comunicat: 24 d octubre de 2017 · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread-Interim-Results-2017.pdf · Wayback: `pendent_verificacio_externa`

6. [`L2|GB00B1KJJ408|W06`] [V] «Alison Brittain, Whitbread Chief Executive Officer, commented:»
   Anys: 2017 · Nivell A · prova: Brittain és Chief Executive Officer al comunicat del 24/10/2017 · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread-Interim-Results-2017.pdf · Wayback: `pendent_verificacio_externa`

7. [`L2|GB00B1KJJ408|W07`] [V] «Alison Brittain Chief Executive 24 April 2018»
   Anys: 2017-2018 · Nivell A · prova: Brittain signa com a Chief Executive l informe de l exercici 2017/18 el 24/4/2018 · URL: https://cdn.whitbread.co.uk/media/2018/05/2018-annual-report-and-accounts.pdf · Wayback: `pendent_verificacio_externa`

8. [`L2|GB00B1KJJ408|W08`] [V] «Interim results | FY19 23 October 2018»
   Anys: 2018 · Nivell A · prova: Data del comunicat: 23 d octubre de 2018 · URL: https://cdn.whitbread.co.uk/media/2026/07/interim-results-press-release-23-10-2018.pdf · Wayback: `pendent_verificacio_externa`

9. [`L2|GB00B1KJJ408|W09`] [V] «Alison Brittain, Whitbread Chief Executive Officer, commented:»
   Anys: 2018 · Nivell A · prova: Brittain és Chief Executive Officer al comunicat del 23/10/2018 · URL: https://cdn.whitbread.co.uk/media/2026/07/interim-results-press-release-23-10-2018.pdf · Wayback: `pendent_verificacio_externa`

10. [`L2|GB00B1KJJ408|W10`] [V] «FY20 Interim Results 22 October 2019»
   Anys: 2019 · Nivell A · prova: Data del comunicat: 22 d octubre de 2019 · URL: https://cdn.whitbread.co.uk/media/2026/07/interim-results-2019.pdf · Wayback: `pendent_verificacio_externa`

11. [`L2|GB00B1KJJ408|W11`] [V] «Alison Brittain, Whitbread Chief Executive Officer, commented:»
   Anys: 2019 · Nivell A · prova: Brittain és Chief Executive Officer al comunicat del 22/10/2019 · URL: https://cdn.whitbread.co.uk/media/2026/07/interim-results-2019.pdf · Wayback: `pendent_verificacio_externa`

12. [`L2|GB00B1KJJ408|W12`] [V] «Alison Brittain Chief Executive 21 May 2020»
   Anys: 2019-2020 · Nivell A · prova: Brittain signa com a Chief Executive l informe de l exercici 2019/20 el 21/5/2020 · URL: https://cdn.whitbread.co.uk/media/2026/07/2020-annual-report-and-accounts.pdf · Wayback: `pendent_verificacio_externa`

13. [`L2|GB00B1KJJ408|W13`] [V] «FY21 Interim Results 27 October 2020»
   Anys: 2020 · Nivell A · prova: Data del comunicat: 27 d octubre de 2020 · URL: https://cdn.whitbread.co.uk/media/2026/07/interim-results-2020-1.pdf · Wayback: `pendent_verificacio_externa`

14. [`L2|GB00B1KJJ408|W14`] [V] «Alison Brittain, Whitbread Chief Executive Officer, commented:»
   Anys: 2020 · Nivell A · prova: Brittain és Chief Executive Officer al comunicat del 27/10/2020 · URL: https://cdn.whitbread.co.uk/media/2026/07/interim-results-2020-1.pdf · Wayback: `pendent_verificacio_externa`

15. [`L2|GB00B1KJJ408|W15`] [V] «Alison Brittain Chief Executive 26 April 2021»
   Anys: 2020 · Nivell A · prova: Brittain signa com a Chief Executive l informe de l exercici 2020/21 el 26/4/2021 · URL: https://cdn.whitbread.co.uk/media/2026/08/Whitbread_AR2020-21.pdf · Wayback: `pendent_verificacio_externa`

16. [`L2|GB00B1KJJ408|W16`] [V] «FY23 H1 Results 25 October 2022»
   Anys: 2022 · Nivell A · prova: Data del comunicat: 25 d octubre de 2022 · URL: https://cdn.whitbread.co.uk/media/2026/07/H1-FY23-RNS-FINAL-v2.pdf · Wayback: `pendent_verificacio_externa`

17. [`L2|GB00B1KJJ408|W17`] [V] «Commenting on today’s results, Alison Brittain, Whitbread Chief Executive Officer, said:»
   Anys: 2022 · Nivell A · prova: Brittain és Chief Executive Officer al comunicat del 25/10/2022 · URL: https://cdn.whitbread.co.uk/media/2026/07/H1-FY23-RNS-FINAL-v2.pdf · Wayback: `pendent_verificacio_externa`

18. [`L2|GB00B1KJJ408|W18`] [V] «Alison Brittain stepping down as Chief Executive on 17 January 2023.»
   Anys: 2016-2020, 2022 · Nivell A · prova: Fi del mandat: Brittain deixa el càrrec de Chief Executive el 17/1/2023 · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread_AR22_Interactive.pdf · Wayback: `pendent_verificacio_externa`

19. [`L2|GB00B1KJJ408|W19`] [V] «Dominic Paul joined Whitbread on 10 January 2023 and joined the Board and became Chief Executive with effect from 17 January 2023.»
   Anys: 2022 · Nivell A · prova: El successor Dominic Paul esdevé Chief Executive amb efecte 17/1/2023 (posterior al 31/10/2022) · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread_AR22_Interactive.pdf · Wayback: `pendent_verificacio_externa`

20. [`L2|GB00B1KJJ408|W20`] [V] «reflecting that Dominic Paul became CEO with effect from the close of the Board meeting held on that day.»
   Anys: 2022 · Nivell A · prova: Confirma el relleu de CEO a Dominic Paul (la frase anterior del document situa el dia al 17 January 2023) · URL: https://cdn.whitbread.co.uk/media/2026/07/Whitbread-PLC-Annual-Report-and-Accounts-2023_24_Single_pages.pdf · Wayback: `pendent_verificacio_externa`

### L2.20 Relx PLC Registered Shares LS -,144397 (`GB00B2B0DG97`)

- isin i anys: `GB00B2B0DG97`, 2016-2025 (n=10). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Erik Engstrom → Erik Engstrom (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Informes anuals 2016-2025 baixats de relx.com (tots HTTP 200, PDF). Les URL s'han localitzat a https://www.relx.com/investors/annual-reports/archive i /2024. Intents fallits (404): .../2016-annual-report.pdf, .../2017-annual-report.pdf, .../2021..2025-annual-report.pdf (patró sense prefix), .../relx-2016-annual-report.pdf, .../relx-2017-annual-report.pdf, .../relx2019-annual-report.pdf, .../relx-2019-annual-report.pdf; els noms correctes són relx2016/relx2017, 2018/2019/2020 i relx-2021..2025. Totes les cites comprovades amb vq.py (OK).
- Dubtes de metodologia per a Doctorat (no decidits): (1) 2016-2017: l'informe anual diu 'Chief Executive Officer of RELX Group' (el document esmenta RELX PLC i RELX NV com a copropietaris de RELX Group plc). S'ha entes que es el CEO de l'emissor RELX PLC; a validar per Doctorat. · (2) A 2016-2021 el nom i la frase 'Appointed: ... since November 2009' no són contigus al text extret (maquetació en columnes), per això es donen dues cites per any (nom+càrrec, i data de nomenament del mateix bloc biogràfic).
- Cites:

1. [`L2|GB00B2B0DG97|RELX2016a`] [V] «Erik Engstrom (53) Chief Executive Officer»
   Anys: 2016 · Nivell A · prova: Erik Engstrom figura com a Chief Executive Officer al consell de l'informe anual 2016 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2016-annual-report.pdf · Wayback: https://web.archive.org/web/20260122230843/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2016-annual-report.pdf (existent; cita no verificada a la captura)

2. [`L2|GB00B2B0DG97|RELX2016b`] [V] «Appointed: Chief Executive Officer of RELX Group since November 2009. Joined the Group as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2016 · Nivell A · prova: La fitxa biogràfica que segueix el nom d'Engstrom diu que és CEO des de novembre de 2009 (mandat continu) · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2016-annual-report.pdf · Wayback: https://web.archive.org/web/20260122230843/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2016-annual-report.pdf (existent; cita no verificada a la captura)

3. [`L2|GB00B2B0DG97|RELX2017a`] [V] «Erik Engstrom (54) Chief Executive Officer»
   Anys: 2017 · Nivell A · prova: Erik Engstrom figura com a Chief Executive Officer al consell de l'informe anual 2017 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2017-annual-report.pdf · Wayback: https://web.archive.org/web/20261003193538/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2017-annual-report.pdf (existent; cita no verificada a la captura)

4. [`L2|GB00B2B0DG97|RELX2017b`] [V] «Appointed: Chief Executive Officer of RELX Group since November 2009. Joined the Group as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2017 · Nivell A · prova: La fitxa biogràfica que segueix el nom d'Engstrom diu que és CEO des de novembre de 2009 (mandat continu) · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2017-annual-report.pdf · Wayback: https://web.archive.org/web/20261003193538/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx2017-annual-report.pdf (existent; cita no verificada a la captura)

5. [`L2|GB00B2B0DG97|RELX2018a`] [V] «Erik Engstrom (55) Chief Executive Officer»
   Anys: 2018 · Nivell A · prova: Erik Engstrom figura com a Chief Executive Officer al consell de l'informe anual 2018 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2018-annual-report.pdf · Wayback: https://web.archive.org/web/20260801055453/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2018-annual-report.pdf (existent; cita no verificada a la captura)

6. [`L2|GB00B2B0DG97|RELX2018b`] [V] «Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2018 · Nivell A · prova: La fitxa biogràfica que segueix el nom d'Engstrom diu que és CEO des de novembre de 2009 (mandat continu) · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2018-annual-report.pdf · Wayback: https://web.archive.org/web/20260801055453/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2018-annual-report.pdf (existent; cita no verificada a la captura)

7. [`L2|GB00B2B0DG97|RELX2019a`] [V] «Erik Engstrom (56) Chief Executive Officer»
   Anys: 2019 · Nivell A · prova: Erik Engstrom figura com a Chief Executive Officer al consell de l'informe anual 2019 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2019-annual-report.pdf · Wayback: https://web.archive.org/web/20261018031645/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2019-annual-report.pdf (existent; cita no verificada a la captura)

8. [`L2|GB00B2B0DG97|RELX2019b`] [V] «Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2019 · Nivell A · prova: La fitxa biogràfica que segueix el nom d'Engstrom diu que és CEO des de novembre de 2009 (mandat continu) · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2019-annual-report.pdf · Wayback: https://web.archive.org/web/20261018031645/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2019-annual-report.pdf (existent; cita no verificada a la captura)

9. [`L2|GB00B2B0DG97|RELX2020a`] [V] «Erik Engstrom (57) Chief Executive Officer»
   Anys: 2020 · Nivell A · prova: Erik Engstrom figura com a Chief Executive Officer al consell de l'informe anual 2020 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2020-annual-report.pdf · Wayback: https://web.archive.org/web/20261005133031/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2020-annual-report.pdf (existent; cita no verificada a la captura)

10. [`L2|GB00B2B0DG97|RELX2020b`] [V] «Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2020 · Nivell A · prova: La fitxa biogràfica que segueix el nom d'Engstrom diu que és CEO des de novembre de 2009 (mandat continu) · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2020-annual-report.pdf · Wayback: https://web.archive.org/web/20261005133031/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2020-annual-report.pdf (existent; cita no verificada a la captura)

11. [`L2|GB00B2B0DG97|RELX2021a`] [V] «Erik Engstrom (58) Chief Executive Officer»
   Anys: 2021 · Nivell A · prova: Erik Engstrom figura com a Chief Executive Officer al consell de l'informe anual 2021 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2021-annual-report.pdf · Wayback: https://web.archive.org/web/20260906115229/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2021-annual-report.pdf (existent; cita no verificada a la captura)

12. [`L2|GB00B2B0DG97|RELX2021b`] [V] «Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2021 · Nivell A · prova: La fitxa biogràfica que segueix el nom d'Engstrom diu que és CEO des de novembre de 2009 (mandat continu) · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2021-annual-report.pdf · Wayback: https://web.archive.org/web/20260906115229/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2021-annual-report.pdf (existent; cita no verificada a la captura)

13. [`L2|GB00B2B0DG97|RELX2022a`] [V] «Erik Engstrom (59) Chief Executive Officer Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2022 · Nivell A · prova: Erik Engstrom és CEO de RELX des de novembre de 2009 segons l'informe anual 2022 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2022-annual-report.pdf · Wayback: https://web.archive.org/web/20260122231239/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2022-annual-report.pdf (existent; cita no verificada a la captura)

14. [`L2|GB00B2B0DG97|RELX2023a`] [V] «Erik Engstrom (60) Chief Executive Officer Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2023 · Nivell A · prova: Erik Engstrom és CEO de RELX des de novembre de 2009 segons l'informe anual 2023 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2023-annual-report.pdf · Wayback: https://web.archive.org/web/20261027083858/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2023-annual-report.pdf (existent; cita no verificada a la captura)

15. [`L2|GB00B2B0DG97|RELX2024a`] [V] «Erik Engstrom (61) Chief Executive Officer Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2024 · Nivell A · prova: Erik Engstrom és CEO de RELX des de novembre de 2009 segons l'informe anual 2024 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2024-annual-report.pdf · Wayback: https://web.archive.org/web/20261114104137/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2024-annual-report.pdf (existent; cita no verificada a la captura)

16. [`L2|GB00B2B0DG97|RELX2025a`] [V] «Erik Engstrom (62) Chief Executive Officer Appointed: Chief Executive Officer of RELX since November 2009. Joined as Chief Executive Officer of Elsevier in 2004.»
   Anys: 2025 · Nivell A · prova: Erik Engstrom és CEO de RELX des de novembre de 2009 segons l'informe anual 2025 · URL: https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2025-annual-report.pdf · Wayback: https://web.archive.org/web/20260927162153/https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2025-annual-report.pdf (existent; cita no verificada a la captura)

### L2.21 Evraz PLC Registered Shares DL 0,05 (`GB00B71N6K86`)

- isin i anys: `GB00B71N6K86`, 2018-2020 (n=3). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Alexander Frolov → Alexander Frolov (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Obert (HTTP 200, PDF 17,4 MB): https://ar2021.evraz.com/download/full-reports/ar_en_annual-report_pages_evraz_2021.pdf (informe anual 2021, web oficial); d'aqui surten les tres cites, verificades amb vq.py sobre el text extret amb pdftotext. Tambe obert https://ar2021.evraz.com/en/corporate-governance/management (200, no usat). Documents contemporanis provats sense exit: https://ar2018.evraz.com/..., https://ar2019.evraz.com/... i https://ar2020.evraz.com/... (tant /download/full-reports/ar_en_annual-report_pages_evraz_<any>.pdf com /en/corporate-governance/management i l'arrel de ar2020) -> HTTP 401 (pagina de bloqueig de 172 bytes); https://www.evraz.com/en/investors/annual-reports/ i https://www.evraz.com/upload/iblock/annual-report-2020.pdf (URL de prova) -> sense connexio (codi 000 / timeout). Companies House (empresa 07784342): l'historial de presentacions s'obre (200) i s'han baixat els comptes de grup dels exercicis 2018, 2019 i 2020 (filing-history/MzIzNzQ5MDU5NGFkaXF6a2N4, MzI2ODEzNjk3NWFkaXF6a2N4, MzMwNjAyNjU1MmFkaXF6a2N4, /document?format=pdf&download=0; 200, 263/260/265 pagines), pero son PDF escanejats sense capa de text i no hi ha OCR disponible a l'entorn, de manera que no se n'ha pogut extreure cap cita literal verificable. No s'ha intentat web.archive.org.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Els tres anys es cobreixen amb una cita d'interval retrospectiva (informe anual 2021 de l'emissor), no amb un document contemporani de cada exercici: els informes 2018-2020 a la web de l'emissor retornen 401 i les copies de Companies House son escanejos sense text (caldria OCR). Doctorat ha de decidir si la cita d'interval es suficient o si vol l'OCR dels comptes dipositats a Companies House.
- Cites:

1. [`L2|GB00B71N6K86|C1`] [V] «Mr Frolov was CEO of EVRAZ plc from 14 October 2011 until 31 August 2021.»
   Anys: 2018-2020 · Nivell A · prova: Interval del mandat d'Alexander Frolov com a CEO d'EVRAZ plc: 14/10/2011-31/08/2021; cobreix el 31/10 de 2018, 2019 i 2020. · URL: https://ar2021.evraz.com/download/full-reports/ar_en_annual-report_pages_evraz_2021.pdf · Wayback: https://web.archive.org/web/20260720011131/https://ar2021.evraz.com/download/full-reports/ar_en_annual-report_pages_evraz_2021.pdf (existent; cita no verificada a la captura)

2. [`L2|GB00B71N6K86|C2`] [V] «Alexander Frolov stepped down from his role of CEO, effective from 31 August 2021.»
   Anys: 2018-2020 · Nivell A · prova: Data efectiva de fi del mandat de Frolov (informe de remuneracions). · URL: https://ar2021.evraz.com/download/full-reports/ar_en_annual-report_pages_evraz_2021.pdf · Wayback: https://web.archive.org/web/20260720011131/https://ar2021.evraz.com/download/full-reports/ar_en_annual-report_pages_evraz_2021.pdf (existent; cita no verificada a la captura)

3. [`L2|GB00B71N6K86|C3`] [V] «the Board appointed Aleksey Ivanov as CEO effective from 1 September 2021»
   Anys: 2018-2020 · Nivell A · prova: Data efectiva d'inici del successor (coherent amb la fila 2021 de la base). · URL: https://ar2021.evraz.com/download/full-reports/ar_en_annual-report_pages_evraz_2021.pdf · Wayback: https://web.archive.org/web/20260720011131/https://ar2021.evraz.com/download/full-reports/ar_en_annual-report_pages_evraz_2021.pdf (existent; cita no verificada a la captura)

### L2.22 NatWest Group PLC Registered Shares LS 1 (`GB00B7T77214`)

- isin i anys: `GB00B7T77214`, 2020-2021 (n=2). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Alison Rose → Alison Rose (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Baixats de la web oficial de l'emissor (investors.natwestgroup.com) els Annual Report and Accounts 2020 (HTTP 200, PDF 367 pàg.; la URL redirigeix a ...natwest-group-annual-report-accounts-2020-v1.pdf) i 2021 (HTTP 200, PDF). Text extret amb pdftotext i cites comprovades amb vq.py (totes OK). Provada també una URL conjecturada de l'informe 2019 (https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/14022020/rbs-annual-report-and-accounts-2019.pdf): 404, no usada ni necessària. No s'ha fet servir cap font de tercers.
- Dubtes de metodologia per a Doctorat (no decidits): (1) El nom al panell és 'Royal Bk of Scotld Grp PLC' però l'emissor es presenta com a NatWest Group plc als informes 2020 i 2021 (mateix ISIN); no s'ha buscat cita del canvi de nom perquè no afecta el CEO. Als documents la persona signa com a 'Alison Rose-Slade' i la base diu 'Alison Rose' (mateixa persona segons el mateix informe, que usa les dues formes).
- Cites:

1. [`L2|GB00B7T77214|C1`] [V] «As highlighted in last year’s report, Alison Rose was appointed as CEO on 1 November 2019»
   Anys: 2020 · Nivell A · prova: Inici del mandat d'Alison Rose com a CEO: 1/11/2019 (informe de l'exercici 2020). · URL: https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/19022021/natwest-group-annual-report-accounts-2020.pdf · Wayback: https://web.archive.org/web/20210406172341/https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/19022021/natwest-group-annual-report-accounts-2020.pdf (existent; cita no verificada a la captura)

2. [`L2|GB00B7T77214|C2`] [V] «The data for 2020 is based on remuneration earned by Alison Rose»
   Anys: 2020 · Nivell A · prova: La ràtio salarial del CEO de 2020 es calcula amb la remuneració d'Alison Rose (CEO durant l'exercici 2020). · URL: https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/19022021/natwest-group-annual-report-accounts-2020.pdf · Wayback: https://web.archive.org/web/20210406172341/https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/19022021/natwest-group-annual-report-accounts-2020.pdf (existent; cita no verificada a la captura)

3. [`L2|GB00B7T77214|C3`] [V] «Alison Rose-Slade Group Chief Executive Officer»
   Anys: 2020 · Nivell A · prova: Signa l'informe anual 2020 (publicat el 19/2/2021) com a Group Chief Executive Officer: continuïtat després del 31/10/2020. · URL: https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/19022021/natwest-group-annual-report-accounts-2020.pdf · Wayback: https://web.archive.org/web/20210406172341/https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/19022021/natwest-group-annual-report-accounts-2020.pdf (existent; cita no verificada a la captura)

4. [`L2|GB00B7T77214|C4`] [V] «Alison Rose, CEO, was appointed on 1 November 2019 and therefore the annual change comparison to 2020 is not relevant»
   Anys: 2021 · Nivell A · prova: Informe de l'exercici 2021: Alison Rose és la CEO, nomenada l'1/11/2019. · URL: https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/18022022/natwest-group-annual-report-accounts-2021.pdf · Wayback: https://web.archive.org/web/20260716195759/https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/18022022/natwest-group-annual-report-accounts-2021.pdf (existent; cita no verificada a la captura)

5. [`L2|GB00B7T77214|C5`] [V] «The data for 2021 is based on remuneration earned by Alison Rose»
   Anys: 2021 · Nivell A · prova: La ràtio salarial del CEO de 2021 es calcula amb la remuneració d'Alison Rose (CEO durant l'exercici 2021). · URL: https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/18022022/natwest-group-annual-report-accounts-2021.pdf · Wayback: https://web.archive.org/web/20260716195759/https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/18022022/natwest-group-annual-report-accounts-2021.pdf (existent; cita no verificada a la captura)

6. [`L2|GB00B7T77214|C6`] [V] «Alison Rose-Slade Group Chief Executive Officer»
   Anys: 2021 · Nivell A · prova: Signa l'informe anual 2021 (publicat el 18/2/2022) com a Group Chief Executive Officer: continuïtat després del 31/10/2021. · URL: https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/18022022/natwest-group-annual-report-accounts-2021.pdf · Wayback: https://web.archive.org/web/20260716195759/https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/18022022/natwest-group-annual-report-accounts-2021.pdf (existent; cita no verificada a la captura)

### L2.23 Phoenix Group Holdings PLC Registered (`GB00BGXQNP29`)

- isin i anys: `GB00BGXQNP29`, 2020-2025 (n=6). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Andy Briggs → Andy Briggs (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Web oficial de l'emissor (ara Standard Life plc, 'Formerly Phoenix Group Holdings plc'): https://www.standardlifeplc.com/investors/results-reports-and-presentations (200, redirigeix a /results-reports-presentations), d'on surten els enllaços als PDF de library.standardlife.co.uk i library.standardlifeplc.com. Baixats amb 200 els informes anuals 2020, 2021, 2022, 2023, 2024 i 2025 (URL a les cites). https://www.thephoenixgroup.com/investor-relations/results-reports-and-presentations/ redirigeix a https://www.standardlifeplc.com/. L'informe 2021 no és a l'URL conjecturada https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2021.pdf (404, igual que altres 10 variants de nom provades); el fitxer correcte és phoenix-group-full-year-results-2021.pdf (portada 'Annual Report and Accounts 2021'). També baixat https://library.standardlife.co.uk/phoenix-group-fy21-rns.pdf (200), no usat com a cita. Totes les cites comprovades amb vq.py (OK).
- Dubtes de metodologia per a Doctorat (no decidits): (1) Els documents són servits des de library.standardlife.co.uk i library.standardlifeplc.com, biblioteques de documents enllaçades des de la web oficial standardlifeplc.com (la mateixa societat, rebatejada Standard Life plc). S'han tractat com a nivell A (web oficial de l'emissor); que Doctorat confirmi que aquests dominis compten com a 'web oficial'. · (2) Les frases dels informes anuals 2021-2025 estan en present ('is Group Chief Executive Officer') i daten de la publicació de l'informe (març de t+1); proven el CEO de l'exercici t i no esmenten cap canvi, però no citen literalment la data 31/10/t. La continuïtat es recolza en la nota que només registra el canvi de CEO del 10/03/2020 (C8). · (3) L'informe 2025 parla del 'role as Dual CEO' d'Andy Briggs (CEO del Grup i de les Life Companies); no afecta el càrrec de Group CEO però es deixa constància. · (4) L'emissor va canviar de nom a Standard Life plc (l'informe 2025 diu 'Formerly Phoenix Group Holdings plc'); el nom al panell continua sent Phoenix Group Holdings.
- Cites:

1. [`L2|GB00BGXQNP29|C1`] [V] «Andy Briggs joined the Board of Phoenix Group Holdings plc on 10 February 2020 as Group CEO Designate and became CEO on 10 March 2020.»
   Anys: 2020-2021 · Nivell A · prova: Data efectiva d'inici com a CEO: 10/03/2020 (abans del 31/10/2020). · URL: https://library.standardlife.co.uk/fy-20-annual-report-and-accounts.pdf · Wayback: https://web.archive.org/web/20260415204647/https://library.standardlife.co.uk/fy-20-annual-report-and-accounts.pdf (existent; cita no verificada a la captura)

2. [`L2|GB00BGXQNP29|C2`] [V] «Clive Bannister left the role of Group Chief Executive Officer on 10 March 2020 and left Phoenix Group on the same date.»
   Anys: 2020 · Nivell A · prova: El CEO anterior va deixar el càrrec el 10/03/2020. · URL: https://library.standardlife.co.uk/fy-20-annual-report-and-accounts.pdf · Wayback: https://web.archive.org/web/20260415204647/https://library.standardlife.co.uk/fy-20-annual-report-and-accounts.pdf (existent; cita no verificada a la captura)

3. [`L2|GB00BGXQNP29|C3`] [V] «Andy Briggs is Group Chief Executive Officer of the Company.»
   Anys: 2021 · Nivell A · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2021. · URL: https://library.standardlife.co.uk/phoenix-group-full-year-results-2021.pdf · Wayback: https://web.archive.org/web/20260415190436/https://library.standardlife.co.uk/phoenix-group-full-year-results-2021.pdf (existent; cita no verificada a la captura)

4. [`L2|GB00BGXQNP29|C4`] [V] «Andy Briggs is Group Chief Executive Officer (‘CEO’) of Phoenix.»
   Anys: 2022 · Nivell A · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2022. · URL: https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2022.pdf · Wayback: https://web.archive.org/web/20260415192505/https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2022.pdf (existent; cita no verificada a la captura)

5. [`L2|GB00BGXQNP29|C5`] [V] «Andy Briggs is the Group Chief Executive Officer (‘CEO’).»
   Anys: 2023 · Nivell A · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2023. · URL: https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2023.pdf · Wayback: https://web.archive.org/web/20260303032752/https://library.standardlife.co.uk/phoenix-group-annual-report-and-accounts-2023.pdf (existent; cita no verificada a la captura)

6. [`L2|GB00BGXQNP29|C6`] [V] «The Group’s Chief Executive Officer, Andy Briggs, is the Executive Board Director responsible for implementation»
   Anys: 2024 · Nivell A · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2024. · URL: https://library.standardlifeplc.com/phoenix_group_annual_report_and_accounts_2024.pdf · Wayback: `pendent_verificacio_externa`

7. [`L2|GB00BGXQNP29|C7`] [V] «Andy Briggs, Group CEO, is responsible for embedding sustainability within»
   Anys: 2025 · Nivell A · prova: Briggs és Group CEO segons l'informe anual de l'exercici 2025. · URL: https://library.standardlife.co.uk/annual-report-and-accounts-2025-spread.pdf · Wayback: https://web.archive.org/web/20260719182559/https://library.standardlife.co.uk/annual-report-and-accounts-2025-spread.pdf (existent; cita no verificada a la captura)

8. [`L2|GB00BGXQNP29|C8`] [V] «Clive Bannister left the role of Group CEO on 10 March 2020 and left the Group on the same date. Andy Briggs was appointed to the Board on 10 February 2020 and remained as CEO-designate until 10 March 2020.»
   Anys: 2025 · Nivell A · prova: Únic canvi de CEO documentat a la sèrie: 10/03/2020; l'informe 2025 no en registra cap altre. · URL: https://library.standardlife.co.uk/annual-report-and-accounts-2025-spread.pdf · Wayback: https://web.archive.org/web/20260719182559/https://library.standardlife.co.uk/annual-report-and-accounts-2025-spread.pdf (existent; cita no verificada a la captura)

### L2.24 Deliveroo PLC Registered Shares (`GB00BNC5T391`)

- isin i anys: `GB00BNC5T391`, 2021 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Will Shu → Will Shu (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Obert i usat: (1) RNS Q3 2021 Trading Update al servidor oficial de la LSE https://www.rns-pdf.londonstockexchange.com/rns/5922P_1-2021-10-19.pdf (200, PDF amb text); (2) Annual Report 2023 al NSM de la FCA https://data.fca.org.uk/artefacts/NSM/Portal/NI-000092427/NI-000092427.pdf (200); (3) prospecte de marc 2021 al NSM (URL de pista, 200). Fallits o no utilitzables: web corporativa corporate.deliveroo.co.uk (pagina de resultats, Q3 trading update /investors/news/q3-trading-update/, /media/n1ib3wun/deliveroo-plc-annual-report-2021.pdf [URL conjecturada], /assets/1716/4750/0874/Deliveroo_FY2021_Prelims_RNS_Final.pdf): totes 'CONNECT tunnel failed, response 502' (host no assolible des d'aqui), per tant l'Annual Report 2021 de la web de l'emissor no s'ha pogut obrir. Companies House (companyia 13227665): historial de dipòsits obert (200) i 'Full accounts made up to 31 December 2021' (dipositat 18/07/2022) baixat (200, 195 pagines) pero es un PDF escanejat sense capa de text (pdftotext = 0 text; no hi ha OCR disponible), no es pot verificar cap cita literal amb vq.py i no s'ha usat. NSM de la FCA: no s'ha localitzat l'URL del Annual Report 2021 ni dels RNS de gener/marc 2022 (l'API de cerca del NSM no s'ha pogut consultar: la crida va ser denegada pel control de permisos de l'entorn; proves amb identificadors veins NI-000072720..27 van donar documents d'altres emissors o l'AGM 2023 de Deliveroo, NI-000072722, obert pero no usat). londonstockexchange.com/news-article/... redirigeix a la portada de noticies (pagina JS, sense contingut); reuters.com 401; theguardian.com (URL conjecturada) pagina de 3 KB sense article; riders.deliveroo.co.uk 403 (pagina 'Just a moment'). WebSearch usat nomes com a pista; copies de tercers (investegate, lse.co.uk, sharesmagazine, design-portfolio.co.uk) no usades.
- Dubtes de metodologia per a Doctorat (no decidits): (1) No s'ha pogut citar l'Annual Report de l'exercici 2021 (web de l'emissor inaccessible; copia de Companies House escanejada sense text). La prova del 31/10/2021 es per interval: comunicat RNS del 20/10/2021 + data de nomenament com a CEO (1/02/2013) i continuitat a 13/03/2024 segons l'Annual Report 2023. Les cites C3-C5 no diuen literalment 'ininterrompudament'; Doctorat ha de decidir si aquesta combinacio es suficient. · (2) La cita C4 prove d'una taula (les cel·les son contigues al text extret amb pdftotext, pero en l'original son columnes): confirmar si s'accepten cites de files de taula. · (3) El comunicat RNS s'ha obert al servidor de PDF de la London Stock Exchange (rns-pdf.londonstockexchange.com), considerat nivell A (borsa / document de l'emissor); confirmar que aquest host compta com a URL original.
- Cites:

1. [`L2|GB00BNC5T391|C1`] [V] «Will Shu, Founder and CEO of Deliveroo, said:»
   Anys: 2021 · Nivell A · prova: L'emissor identifica Will Shu com a Founder and CEO al comunicat del 20/10/2021 (11 dies abans del 31/10/2021). · URL: https://www.rns-pdf.londonstockexchange.com/rns/5922P_1-2021-10-19.pdf · Wayback: https://web.archive.org/web/20240513152637/https://www.rns-pdf.londonstockexchange.com/rns/5922P_1-2021-10-19.pdf (existent; cita no verificada a la captura)

2. [`L2|GB00BNC5T391|C2`] [V] «Deliveroo plc Q3 2021 Trading Update 20 October 2021»
   Anys: 2021 · Nivell A · prova: Data del comunicat de la cita C1: 20 d'octubre de 2021. · URL: https://www.rns-pdf.londonstockexchange.com/rns/5922P_1-2021-10-19.pdf · Wayback: https://web.archive.org/web/20240513152637/https://www.rns-pdf.londonstockexchange.com/rns/5922P_1-2021-10-19.pdf (existent; cita no verificada a la captura)

3. [`L2|GB00BNC5T391|C3`] [V] «** This is the date on which Will Shu was appointed as CEO. Will Shu was appointed to the Deliveroo plc Board on 19 March 2021.»
   Anys: 2021 · Nivell A · prova: Nota de la taula de contractes: la data marcada amb ** (1 February 2013) es la del nomenament de Will Shu com a CEO. · URL: https://data.fca.org.uk/artefacts/NSM/Portal/NI-000092427/NI-000092427.pdf · Wayback: `pendent_verificacio_externa`

4. [`L2|GB00BNC5T391|C4`] [V] «Will Shu 1 February 2013** 22 March 2021 12 months 6 months»
   Anys: 2021 · Nivell A · prova: Data de nomenament al carrec (CEO): 1 de febrer de 2013; contracte vigent del 22/03/2021. Inici del mandat anterior al 31/10/2021. · URL: https://data.fca.org.uk/artefacts/NSM/Portal/NI-000092427/NI-000092427.pdf · Wayback: `pendent_verificacio_externa`

5. [`L2|GB00BNC5T391|C5`] [V] «Will Shu Founder and Chief Executive Officer 13 March 2024»
   Anys: 2021 · Nivell A · prova: Will Shu continua com a Founder and CEO el 13/03/2024: continuitat documentada en una data posterior al 31/10/2021. · URL: https://data.fca.org.uk/artefacts/NSM/Portal/NI-000092427/NI-000092427.pdf · Wayback: `pendent_verificacio_externa`

6. [`L2|GB00BNC5T391|C6`] [V] «The Company’s Chief Executive Officer is Will Shu, born in 1979»
   Anys: 2021 · Nivell A · prova: Will Shu es el CEO de la societat a la data del prospecte (marc 2021). · URL: https://data.fca.org.uk/artefacts/NSM/Portal/NI-000022020/NI-000022020.pdf · Wayback: https://web.archive.org/web/20230604024150/https://data.fca.org.uk/artefacts/NSM/Portal/NI-000022020/NI-000022020.pdf (existent; cita no verificada a la captura)

### L2.25 WPP PLC Registered Shares LS -,10 (`JE00B8KF9B49`)

- isin i anys: `JE00B8KF9B49`, 2025 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Cindy Rose → Cindy Rose (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Tot a la web oficial de l'emissor, obert a la URL original amb get.sh: (1) pista https://www.wpp.com/en/news/2025/07/chief-executive-officer-appointment -> 200; (2) https://www.wpp.com/en/news/2025/10/third-quarter-trading-update-2025 -> 200 (localitzada via https://www.wpp.com/en/investors/financial-releases, 200); (3) Annual Report 2025 a cdn.wpp.com (enllaç trobat a https://www.wpp.com/en/investors/results-presentations-and-reports, 200) -> 200, PDF 22,5 MB. URL endevinades que han donat 404 (no usades): /en/news/2025/10/third-quarter-trading-update, /en/news/2025/10/2025-third-quarter-trading-update, /en/news/2026/02/2025-preliminary-results, /en/investors/results-centre, /en/about/our-leadership/cindy-rose, /sitemap.xml, /en/news/third-quarter-trading-update-2025. No s'ha fet servir cap font de tercers.
- Cites:

1. [`L2|JE00B8KF9B49|c1`] [V] «Cindy Rose has been appointed as Chief Executive Officer (CEO) of the Company, effective 1 September 2025»
   Anys: 2025 · Nivell A · prova: Nomenament de Cindy Rose com a CEO amb efecte 1/9/2025 · URL: https://www.wpp.com/en/news/2025/07/chief-executive-officer-appointment · Wayback: https://web.archive.org/web/20261006023253/https://www.wpp.com/en/news/2025/07/chief-executive-officer-appointment (existent; cita no verificada a la captura)

2. [`L2|JE00B8KF9B49|c2`] [V] «Cindy succeeds Mark Read who will step down as CEO on the same date»
   Anys: 2025 · Nivell A · prova: Mark Read deixa de ser CEO l'1/9/2025 · URL: https://www.wpp.com/en/news/2025/07/chief-executive-officer-appointment · Wayback: https://web.archive.org/web/20261006023253/https://www.wpp.com/en/news/2025/07/chief-executive-officer-appointment (existent; cita no verificada a la captura)

3. [`L2|JE00B8KF9B49|c3`] [V] «Cindy Rose assumed the role of CEO from 1 September»
   Anys: 2025 · Nivell A · prova: Document datat el 30/10/2025: Rose va assumir el càrrec l'1/9 · URL: https://www.wpp.com/en/news/2025/10/third-quarter-trading-update-2025 · Wayback: https://web.archive.org/web/20260128150642/https://www.wpp.com/en/news/2025/10/third-quarter-trading-update-2025 (existent; cita no verificada a la captura)

4. [`L2|JE00B8KF9B49|c4`] [V] «Cindy Rose, Chief Executive Officer of WPP, said:»
   Anys: 2025 · Nivell A · prova: Rose és CEO el 30/10/2025 (vigília de la data de referència) · URL: https://www.wpp.com/en/news/2025/10/third-quarter-trading-update-2025 · Wayback: https://web.archive.org/web/20260128150642/https://www.wpp.com/en/news/2025/10/third-quarter-trading-update-2025 (existent; cita no verificada a la captura)

5. [`L2|JE00B8KF9B49|c5`] [V] «Cindy Rose previously served as a Non-Executive Director on the WPP Board and served on the Audit and Nomination Committees until her appointment as CEO on 1 September 2025.»
   Anys: 2025 · Nivell A · prova: Informe anual de l'exercici 2025: nomenament com a CEO l'1/9/2025 · URL: https://cdn.wpp.com/raw/upload/v1778673483/wpp/project/wpp/files/investors/2026/annual-report/wpp_annual_report_2025.pdf · Wayback: https://web.archive.org/web/20260822193651/https://cdn.wpp.com/raw/upload/v1778673483/wpp/project/wpp/files/investors/2026/annual-report/wpp_annual_report_2025.pdf (existent; cita no verificada a la captura)

6. [`L2|JE00B8KF9B49|c6`] [V] «Appointed: 1 April 2019 (Chief Executive Officer from 1 September 2025)»
   Anys: 2025 · Nivell A · prova: Biografia de Cindy Rose al consell: CEO des de l'1/9/2025, vigent a la publicació de l'informe (2026) · URL: https://cdn.wpp.com/raw/upload/v1778673483/wpp/project/wpp/files/investors/2026/annual-report/wpp_annual_report_2025.pdf · Wayback: https://web.archive.org/web/20260822193651/https://cdn.wpp.com/raw/upload/v1778673483/wpp/project/wpp/files/investors/2026/annual-report/wpp_annual_report_2025.pdf (existent; cita no verificada a la captura)

7. [`L2|JE00B8KF9B49|c7`] [V] «Mark Read – stepped down from the Board on 1 September 2025»
   Anys: 2025 · Nivell A · prova: Sortida de Mark Read l'1/9/2025 · URL: https://cdn.wpp.com/raw/upload/v1778673483/wpp/project/wpp/files/investors/2026/annual-report/wpp_annual_report_2025.pdf · Wayback: https://web.archive.org/web/20260822193651/https://cdn.wpp.com/raw/upload/v1778673483/wpp/project/wpp/files/investors/2026/annual-report/wpp_annual_report_2025.pdf (existent; cita no verificada a la captura)

### L2.26 Signify N.V. Registered Shares EO -,01 (`NL0011821392`)

- isin i anys: `NL0011821392`, 2022 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Eric Rondolat → Eric Rondolat (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Baixat l'informe anual 2022 de la web oficial de l'emissor: https://www.signify.com/static/2022/signify-annual-report-2022.pdf (HTTP 200, application/pdf, 18,8 MB). Text extret amb pdftotext i cerca de 'Rondolat'. També s'ha baixat https://www.signify.com/static/2023/signify-annual-report-2023.pdf (HTTP 200), no utilitzat com a prova. Cap URL ha fallat.
- Dubtes de metodologia per a Doctorat (no decidits): (1) La cita c1 és d'interval obert ('since May 2016') dins l'informe de l'exercici 2022 (publicat el febrer de 2023); no hi ha una frase que digui literalment 'el 31/10/2022', la cobertura es dedueix de l'inici del mandat i de la vigència a l'informe de l'exercici.
- Cites:

1. [`L2|NL0011821392|c1`] [V] «Eric Rondolat Born 1966, Italian/French Chief Executive Officer Chair of the Board of Management since May 2016»
   Anys: 2022 · Nivell A · prova: Rondolat és CEO i president del Board of Management des del maig de 2016, vigent a l'informe de l'exercici 2022 · URL: https://www.signify.com/static/2022/signify-annual-report-2022.pdf · Wayback: https://web.archive.org/web/20260705192635/https://www.signify.com/static/2022/signify-annual-report-2022.pdf (existent; cita no verificada a la captura)

2. [`L2|NL0011821392|c2`] [V] «Eric Rondolat CEO Signify Signify Annual Report 2022»
   Anys: 2022 · Nivell A · prova: Rondolat signa la carta del CEO de l'informe anual 2022 com a CEO de Signify · URL: https://www.signify.com/static/2022/signify-annual-report-2022.pdf · Wayback: https://web.archive.org/web/20260705192635/https://www.signify.com/static/2022/signify-annual-report-2022.pdf (existent; cita no verificada a la captura)

### L2.27 Ericsson Namn-Aktier B (fria) o.N. (`SE0000108656`)

- isin i anys: `SE0000108656`, 2016 (n=1). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Jan Frykhammar → Jan Frykhammar (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R2 (CEO interí). Nivell de font: A, B.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Emissor: ericsson.com retorna 403 (challenge de Cloudflare 'Just a moment...') a totes les URL provades: informe anual 2016 (/4ac57e/assets/local/investors/documents/financial-reports-and-filings/annual-reports/ericsson-annual-report-2016-en.pdf i /assets/local/investors/documents/2016/ericsson-annual-report-2016-en.pdf, camins deduïts de la pista 2015), pàgina d'informes anuals, i comunicats /en/press-releases/2016/7/ericssons-vestberg-steps-down---search-for-new-ceo-initiated, /2016/10/ericssons-board-names-borje-ekholm-new-president-and-ceo i /2017/1/borje-ekholm-takes-office-as-president-and-ceo. SEC: data.sec.gov/submissions/CIK0000717826.json s'obre (200) i localitza el 20-F de 2016 (0001193125-17-139501) i els 6-K de 25/07/2016, 26/10/2016 i 17/01/2017, però www.sec.gov/Archives i efts.sec.gov retornen 403 ('Undeclared Automated Tool'); no s'ha forçat. mb.cision.com 403; news.cision.com: URL provada 404. Reuters 401, CNBC 403, NYT 403, telecoms.com 403. La pista de Husqvarna s'obre però no esmenta Frykhammar. Oberts amb èxit (200): Fortune/Reuters 26/10/2016, comunicat d'Investor AB 26/10/2016, TechCrunch 25/07/2016, RCR Wireless 28/10/2016. Business Standard (còpia de Reuters) baixat però no usat com a prova.
- Dubtes de metodologia per a Doctorat (no decidits): (1) L'any 2016 queda provat amb premsa (B) i un comunicat d'Investor AB, no amb cap document de l'emissor: ericsson.com (Cloudflare) i els arxius de la SEC (20-F 2016 i 6-K) no es poden obrir des d'aquí. Convindria que Doctorat verifiqui l'informe anual 2016 o els 6-K (accessions 0001193125-16-655851, 0001193125-16-747233, 0001193125-17-010438). · (2) El comunicat d'Investor AB s'ha classificat com a nivell A (comunicat regulatori d'una societat cotitzada a la seva web oficial), però Investor és accionista, no l'emissor ni la seva successora: cal decidir si compta com a A o com a B. · (3) TechCrunch i RCR Wireless són premsa tecnològica/sectorial: cal decidir si entren a 'premsa econòmica de qualitat' (B). Sense elles, la prova es basa en c1 (Fortune/Reuters) i c2. · (4) Totes les cites són anteriors al 31/10/2016 (l'última, del 28/10) i descriuen el relleu del 16/01/2017 com a previst; no s'ha pogut obrir cap document posterior que el confirmi com a fet. · (5) Frykhammar era CEO interí (acting/interim President and CEO); segons la regla, l'interí compta.
- Cites:

1. [`L2|SE0000108656|c1`] [V] «He will take over at Ericsson on January 16 from acting CEO Jan Frykhammar.»
   Anys: 2016 · Nivell B · prova: El 26/10/2016 Frykhammar era CEO en funcions i Ekholm no assumia fins al 16 de gener · URL: https://fortune.com/2016/10/26/ericsson-new-ceo-borje-ekholm · Wayback: https://web.archive.org/web/20241217090637/https://fortune.com/2016/10/26/ericsson-new-ceo-borje-ekholm/ (existent; cita no verificada a la captura)

2. [`L2|SE0000108656|c2`] [V] «Ericsson’s Board of Directors has appointed Börje Ekholm as new CEO, effective January 16, 2017.»
   Anys: 2016 · Nivell A · prova: Data efectiva del nomenament d'Ekholm: 16/01/2017 (posterior al 31/10/2016) · URL: https://www.investorab.com/press/borje-ekholm-appointed-new-ceo-ericsson-steps-down-ceo-patricia-industries-1439281 · Wayback: `pendent_verificacio_externa`

3. [`L2|SE0000108656|c3`] [V] «Jan Frykhammar, who has been working for the company since 1991 will be stepping in as interim CEO»
   Anys: 2016 · Nivell B · prova: Inici del mandat interí de Frykhammar el 25/07/2016, quan Vestberg plega amb efecte immediat · URL: https://techcrunch.com/2016/07/25/ericsson-ceo · Wayback: https://web.archive.org/web/20261003101954/https://techcrunch.com/2016/07/25/ericsson-ceo/ (existent; cita no verificada a la captura)

4. [`L2|SE0000108656|c4`] [V] «Frykhammar will remain interim CEO until Jan. 16, 2017.»
   Anys: 2016 · Nivell B · prova: Frykhammar continua com a CEO interí fins al 16/01/2017 · URL: https://www.rcrwireless.com/20161028/5g/ericsson-new-ceo-tag31-2 · Wayback: `pendent_verificacio_externa`

### L2.28 Boliden AB Namn-Aktier SK 2 (`SE0000869646`)

- isin i anys: `SE0000869646`, 2016-2017 (n=2). Camp: CEO a 31/10 (`ceos`). Valor actual → proposat: **Lennart Evrell → Lennart Evrell (sense canvi)**. FounderCEO: sense canvi.
- Regla aplicada: R1. Nivell de font: A.
- Efecte esperat: `certificada_ceo_pendent` → `certificada` si el flux valida les cites; no s'autodeclara.
- Cerca feta: Web oficial de l'emissor: https://www.boliden.com/investor-relations/reports-and-presentations/annual-reports redirigeix (200) a https://investors.boliden.com/en/reports-and-presentations/financial-reports, d'on s'han extret els enllaços PDF. Baixats amb 200 de investors.boliden.com/sites/boliden-ir/files/pr/: 201703089998-1.pdf (Annual Report 2016), 201703089998-2.pdf (GRI Report 2016, no citat), 201803060710-1.pdf (Annual Report 2017), 201803060710-2.pdf (GRI 2017, no citat), 201610206170-1.pdf (informe Q3 2016), 201610206172-1.pdf (comunicat Q3 2016), 201710247984-1.pdf (informe Q3 2017). Dues URL endevinades a www.boliden.com/globalassets/... (boliden_ar16_eng.pdf, boliden_ar17_eng.pdf) van donar 404 i no s'han fet servir. No ha calgut premsa ni registres.
- Dubtes de metodologia per a Doctorat (no decidits): (1) Cap document únic afirma literalment el càrrec en la data exacta del 31/10; la prova és per acotament (signatura com a President & CEO el 20/10/2016 i el 24/10/2017, més l'informe anual de cada exercici i la data d'efecte del successor, 1/6/2018). Doctorat ha de confirmar que aquest acotament és suficient. · (2) El títol literal és 'President & CEO' (verkställande direktör i koncernchef); es tracta com a CEO.
- Cites:

1. [`L2|SE0000869646|C1`] [V] «Stockholm, 20 October 2016 Lennart Evrell President & CEO»
   Anys: 2016 · Nivell A · prova: Evrell signa com a President & CEO l'informe intermedi el 20/10/2016 · URL: https://investors.boliden.com/sites/boliden-ir/files/pr/201610206170-1.pdf · Wayback: https://web.archive.org/web/20241208120618/https://investors.boliden.com/sites/boliden-ir/files/pr/201610206170-1.pdf (existent; cita no verificada a la captura)

2. [`L2|SE0000869646|C2`] [V] «Evrell, President & CEO of Boliden, summarising the past quarter.»
   Anys: 2016 · Nivell A · prova: Evrell és President & CEO de Boliden el 20/10/2016 · URL: https://investors.boliden.com/sites/boliden-ir/files/pr/201610206172-1.pdf · Wayback: https://web.archive.org/web/20241208123757/https://investors.boliden.com/sites/boliden-ir/files/pr/201610206172-1.pdf (existent; cita no verificada a la captura)

3. [`L2|SE0000869646|C3`] [V] «Boliden has posted one of its strongest years ever. Lennart Evrell President & CEO»
   Anys: 2016 · Nivell A · prova: Evrell signa com a President & CEO la carta de l'informe anual de l'exercici 2016 (exercici natural, inclou el 31/10/2016) · URL: https://investors.boliden.com/sites/boliden-ir/files/pr/201703089998-1.pdf · Wayback: https://web.archive.org/web/20260512121320/https://investors.boliden.com/sites/boliden-ir/files/pr/201703089998-1.pdf (existent; cita no verificada a la captura)

4. [`L2|SE0000869646|C4`] [V] «Stockholm, 24 October 2017 Lennart Evrell President & CEO»
   Anys: 2017 · Nivell A · prova: Evrell signa com a President & CEO l'informe intermedi el 24/10/2017 · URL: https://investors.boliden.com/sites/boliden-ir/files/pr/201710247984-1.pdf · Wayback: https://web.archive.org/web/20260512121618/https://investors.boliden.com/sites/boliden-ir/files/pr/201710247984-1.pdf (existent; cita no verificada a la captura)

5. [`L2|SE0000869646|C5`] [V] «Mikael Staffas has been appointed as the new President and CEO of Boliden. He will take up the position on 1 June 2018.»
   Anys: 2017 · Nivell A · prova: El successor no pren el càrrec fins a l'1/6/2018; per tant no hi ha canvi de CEO abans d'aquesta data · URL: https://investors.boliden.com/sites/boliden-ir/files/pr/201803060710-1.pdf · Wayback: https://web.archive.org/web/20241208132648/https://investors.boliden.com/sites/boliden-ir/files/pr/201803060710-1.pdf (existent; cita no verificada a la captura)

6. [`L2|SE0000869646|C6`] [V] «take over the leadership of Boliden. I will miss you all. Lennart Evrell President & CEO»
   Anys: 2017 · Nivell A · prova: Evrell signa com a President & CEO la carta de l'informe anual de l'exercici 2017 (inclou el 31/10/2017) · URL: https://investors.boliden.com/sites/boliden-ir/files/pr/201803060710-1.pdf · Wayback: https://web.archive.org/web/20241208132648/https://investors.boliden.com/sites/boliden-ir/files/pr/201803060710-1.pdf (existent; cita no verificada a la captura)


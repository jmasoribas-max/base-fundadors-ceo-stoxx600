# Registre de canvis

Data d'aquest arbre: 19/11/2026 10:12 (CET, Europe/Madrid). Base: `dades/base_isin_any_v8r3.csv` SHA `1b7df913b31300857cbc77332a9aa03626edc0013f3bbb1e8625aa456ee38d4c` [V].

La v8 r3 **no afegeix canvis d'etiqueta FounderCEO**. El registre que segueix és el de la v8 r1 (cites amb URL original i Wayback). La v8 r3 aplica l'extensió del supersector de juny 2023 als anys 2024-2025 per als ISIN que ja el tenien (`sector_estes_des_2023=1`) i afegeix `supersector_fix`; no canvia cap etiqueta FounderCEO. Qualsevol canvi futur de dades s'ha d'afegir aquí amb cita literal, URL i Wayback, en una branca i via PR.

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

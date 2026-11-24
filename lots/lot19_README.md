# Lot 19 · Tancament de dubtes oberts amb l'evidència del registre (24/11/2026)

Un triatge de dos agents (anàlisi i verificació contrària) va classificar els 113 grups de dubtes oberts de `PENDENTS.md`. Aquest lot tanca els grups marcats com a «tancables amb l'evidència del registre», després d'una segona verificació independent.

## Què fa

- **78 files** passen a `estat/dubtes_tancats.csv` (dubtes tancats), amb la regla i els id del registre que ho sostenen.
- **10 entrades noves** al registre (`L19-…`). Totes són [V]: reprenen cites [V] del registre per a un altre any o una altra funció, o s'han tornat a comprovar al document original:
  - Aedifica 2019: CEO, exercici allargat que inclou el 31/10/2019;
  - Inditex 2017-2018: revisió de la marca de R1 a R3;
  - Unipol 2024: CEO per R3;
  - KPN i PKO: origen estatal, prova e;
  - STMicroelectronics: prova d;
  - PZU 2024: CEO.
- **No es canvia cap etiqueta (FounderCEO) ni cap CEO (`ceos`).** Els canvis de traçabilitat que proposa el triatge (per exemple, `regles` FT → D37) van al lot de correcció, que ha d'aprovar Jordi.
- `lots/lot19_pendents.csv`: els 9 grups que la verificació va treure dels tancables, amb el motiu.

## Files tancades

| ISIN | Dubte | Anys | Com es tanca |
|---|---|---|---|
| `BE0003851681` | lot17 | 2019 | D21 i criteri b del PR #3 (proxy_tancament): l'informe 2019/2020 cobreix l'exercici allargat de l'1/7/2019 al 31/12/2020, que inclou el 31/10/2019, i la cita [V] de L17-BE0003851681-C01 («Mr. Stefaan Gielens, CEO of Aedifica NV/SA», p. 261) passa al 2019 amb u |
| `CH0012142631` | lot17 | 2016 | Regla 28 (ceo_interval): la condició de data és la del nomenament i no la del document, de manera que l'inici L17-CH0012142631-C02 (B, CEO des de l'1/10/2008) i el final L17-CH0012142631-C01 (A, comunicat del 31/10/2017) valen, i L4/CH0012142631/1 (A) dona el  |
| `CH0013841017` | lot17 | 2019 | Regla 28 (ceo_interval) i criteri c del PR #3 (D4b): inici A L17-CH0013841017-C02 (nomenament del 30/1/2019) i final B L17-CH0013841017-C01 (CEO el 12/11/2019), i L5-CH0013841017-C11 (A, verificada a la captura) fixa el mandat de març al 12/11/2019, de manera  |
| `CH1243598427` | lot9 | 2023, 2024, 2025 | R1 (regla 25 P5) i CLAUDE.md §3: les cites [V] de l'emissor del mateix exercici (L2/CH1243598427/C2023a, C2023c i C2023g; C2024a i C2024c) donen Richard Saynor com a Chief Executive Officer, i l'informe de remuneracions és de Sandoz Group AG (C2023e, C2024d),  |
| `DE0006632003` | lot10 | 2018 | D37 amb l'equivalència de la P6 i criteri a del PR #3: L11-DE0006632003-F01 (anunci ad hoc de l'emissor, «Simon Moroney, CEO and co-founder of MorphoSys AG») substitueix les candidatures del lot 10, i el CEO el cobreix L12-DE0006632003-C01 (R1, informe anual 2 |
| `ES0113307021` | lot9 | 2016 | Regla 25 P5: primer R1 i «consejero delegado» és equivalent legal del CEO, i el president executiu només compta per R3 si el càrrec és vacant, cosa que no passa perquè L9-ES0113307021-C01, L2/ES0113307021/c2 i c3 (A) i c5 (B, 26/10/2016) acrediten Sevilla com  |
| `ES0148396007` | regla29 | 2017, 2018 | R3 (secció 2.1 i regla 25 P5, precedent ITV 2017): el càrrec de CEO era vacant (L6-ES0148396007-X08, Cinco Días) i els ACGR de l'exercici atribueixen a Pablo Isla tots els poders del primer executiu (L17-ES0148396007-C02 per al 2017 i L17-ES0148396007-C01 per  |
| `FR0000051807` | lot10 | 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | D37 amb la P6: L11-FR0000051807-F01 (URD 2024, «Mr. Daniel Julien is the historical founder of the Group») substitueix les candidatures del lot 10, L7-FR0000051807-X01 (entrada de l'any 2016; el fet no depèn de l'any) el situa a la fundació del 1978 (no és D37 |
| `FR0014000MR3` | lot10 | 2021, 2022, 2023, 2024, 2025 | D37 amb la P6 i P1: L11-FR0014000MR3-F01 (informe anual 2024 de l'emissor, «Since founding the original Eurofins Scientific Nantes ... laboratory in 1987, Dr Martin») substitueix la pàgina d'història que donava 403, la SE redomiciliada no és fundació nova, i c |
| `GB0002652740` | lot10 | 2016, 2017, 2018 | D37 (regla 24) amb la P6 i D37d: L16-GB0002652740-F01 (informe anual 2016, «founder of Derwent Valley Holdings in 1984», nom anterior de la cotitzada) respon el dubte sobre «Our History», i el CEO de cada any té cita R1 [V] (L12-GB0002652740-C03, C02 i C01) |
| `GB00B3MBS747` | lot10 | 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | D37 (regla 24) amb la P6: L11-GB00B3MBS747-F01 (web de l'emissor, «Ocado, which he established with two former colleagues from Goldman Sachs in 2000») substitueix la font C del lot 10, i cada any té cita de CEO R1 [V] (L12-GB00B3MBS747-C01 a C10); la cita no é |
| `GB00BNTJ3546` | lot10 | 2021, 2022, 2023, 2024 | D37 (regla 24) amb la P6 i criteri a del PR #3: L11-GB00BNTJ3546-F01 (fullet de l'IPO del 16/4/2021, «Juan Alcaraz is the CEO and Founder of Allfunds», contemporani per a la D37a) substitueix la candidatura del lot 10 que redirigia a una pàgina 404, i cada any |
| `IT0004810054` | regla29 | 2024 | Regla 25 P5 i R3 (secció 2.1): el càrrec de CEO era vacant i l'informe de govern 2024 de l'emissor confia la gestió operativa al director general Matteo Laterza (L7-IT0004810054-C01, p. 50) i el descriu com a «the main person responsible for company management |
| `JE00B3CGFD43` | lot10 | 2016 | D37 amb la P6 i P1: L11-JE00B3CGFD43-F01 (prospectus d'IWG plc del 3/11/2016, «The Regus business ... was founded in 1989 by Mark Dixon, the Chief Executive») substitueix la pàgina bloquejada del lot 10, la holding nova no és fundació nova, i el CEO el cobreix |
| `JE00BN574F90` | lot10 | 2021 | D37 amb la P6 i criteri a del PR #3: L11-JE00BN574F90-F01 (informe anual 2015 de l'emissor, còpia a annualreports.com, «Wizz Air was founded in 2003 by its current Chief Executive Officer József Váradi and five other individuals») substitueix la pàgina bloquej |
| `NL0000009082` | regla29 | 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | Prova e (regles 14 i 21, decisió de Jordi del 24/11/2026): l'empresa estatal PTT es va convertir el 1989 en la cotitzada (L7-NL0000009082-F01, A) i l'Estat n'era l'únic accionista (L7-NL0000009082-X01, A), sense cap fundador persona física, i els CEO tenen cit |
| `NL0000226223` | regla29 | 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | Regla 26 (D1 estricta: combinació del 1987 al 50%, L7-NL0000226223-F02 i X01) i J1 (regla 21b): la fundació que compta és la de Thomson Semiconducteurs, on era Chery, i la prova d hi tanca amb cites A de l'emissor, perquè el negoci ja funcionava el 1981 (L7-NL |
| `NO0010310956` | lot10 | 2019, 2020, 2021 | D37 (regla 24): L11-NO0010310956-F01 (fullet base de l'emissor del 15/7/2021, «CEO Gustav Witzøe is the company’s founder») substitueix les cites no_valida del lot 10, i el CEO el cobreix L11-NO0010310956-C01 (R1, nomenament efectiu el 21/10/2019); la marca D3 |
| `PLPKO0000016` | regla29 | 2022, 2023 | Prova e (regles 14 i 21, decisió de Jordi del 24/11/2026): el banc es va crear per decret estatal el 1919 (L7-PLPKO0000016-X01, A) i la conversió del 2000 també va ser per decret (L3/PLPKO0000016/PKO-08, entrada dels anys 2024-2025; el fet no depèn de l'any),  |
| `PLPZU0000011` | regla29 | 2024 | R1 i CLAUDE.md §3: L7-PLPZU0000011-C03 (informe anual 2024 de l'emissor, «Artur Olech President of the PZU Management Board from 19 July 2024 to 27 January 2025») anomena la persona i el càrrec en un interval que inclou el 31/10/2024, i com que estava registra |
| `SE0000455057` | lot10 | 2016, 2017, 2018, 2019, 2020, 2021 | D37 (regla 24) amb la P6, precedent B&M (regla 27): L11-SE0000455057-F01 (comunicat de l'emissor del 18/8/2025, «Erik Selin, founder and outgoing CEO») substitueix la cita no_valida del lot 10 i preval sobre l'FT, i cada any té cita de CEO R1 [V] (L12-SE000045 |
| `SE0017832488` | lot10 | 2022, 2023, 2024, 2025 | D37 (regla 24) amb la P6: L11-SE0017832488-F01 (comunicat del 18/8/2025, «Erik Selin, founder and outgoing CEO») i L12-SE0017832488-C04 (informe anual 2025, «Balders grundare och vd Erik Selin») substitueixen la cita no_valida del lot 10 i prevalen sobre l'FT, |

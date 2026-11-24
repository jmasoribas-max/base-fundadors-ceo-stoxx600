# Lot 17: cerca nova de cites de CEO per a totes les files que no en tenien

- **Fet per:** Claude, 23/11/2026. Cerca amb dotze agents (grups de 67 files i 18-19 empreses), i verificació i importació amb [`traspas/importa_cerca.py`](../traspas/importa_cerca.py), amb els mateixos criteris que el [lot 12](lot12_README.md).
- **Abast:** les 804 files (P i F) que, després del lot 15, no tenien cita de CEO de l'exercici ([`lot15_pendents.csv`](lot15_pendents.csv)), de 220 empreses. Només s'hi afegeixen proves; **cap canvi de FounderCEO ni de `ceos`**.

## Normes de la cerca

- **Document de l'exercici que inclou el 31/10 de l'any**, o l'interval de la regla 28. Per ordre de preferència: informe anual, còpies dels reguladors (ESEF, FCA NSM, AMF/DILA, CNMV, eMarket Storage), comunicats de l'emissor o d'un canal oficial.
- **Cita literal i curta**, amb el nom i un títol de primer executiu o el seu equivalent legal. Sense agregadors, Wayback, frases de sortida ni càrrecs futurs.
- **Discrepàncies i files no trobades,** declarades.
- **Agents:** no han fet servir cap mètode per saltar bloquejos. Un agent va provar una capçalera de procedència (Referer) en un servidor de Bakkafrost. El control de seguretat ho va aturar, i l'agent va esborrar el fitxer i va fer servir la còpia oficial d'Oslo Børs. Als agents següents se'ls va prohibir expressament.

## Verificació independent (Claude)

1. La cita ha d'anomenar el CEO de la fila (per persona, als co-CEO) i contenir un títol de primer executiu. La llista de títols equivalents s'ha ampliat amb els que han sortit:
   - «Chairman of the Executive Board» i «Executive Board … (Chairman)» (RWE, Fraport, Munich Re);
   - «President of the Executive Committee» (KBC);
   - «Spokesman of the Executive Board» (Nemetschek);
   - «Chairman of the Board of Executive Directors» (K+S);
   - «máximo responsable ejecutivo» (Mapfre).
2. El document ha de ser de l'exercici. En un interval, el document final ha de ser posterior al 31/10.
3. Claude torna a baixar el document i hi busca la cita literal (amb `pdftotext` normal i `-raw`, i dins el zip als ESEF). Si un servidor refusa l'agent de navegador, es torna a provar amb el de curl. Si la re-descàrrega falla, la cita es comprova al fitxer que va baixar la cerca.

## Resultats

| Recompte | Valor |
|---|---:|
| Files del lot | 804 (220 empreses) |
| Files amb cita de CEO (C1) | 791 |
| Files fetes (cita de CEO i de fundador) | 313 |
| … de les quals amb `ceo_interval` | 3 (AB InBev 2017, Clariant 2016, Lonza 2019) |
| Files en dubte enviades a `PENDENTS.md` | 12 (secció «Dubtes del lot 17») |
| Entrades noves `[V]` | 794 (12 comprovades al fitxer de la cerca). Allotjament de les 798 entrades: 501 emissor, 145 regulador, 150 plataforma oficial, 2 premsa B |
| Entrades noves `[NV]` | 4 |
| … amb nota `no_valida` | 4 (la cita no s'ha trobat al document tornat a baixar: Sunrise 2017-2018, Mapfre 2018 i Vivendi 2017) |
| Fonts antigues revisades | 0 |
| Canvis proposats a FounderCEO o `ceos` | 0 (la discrepància de BME va a dubtes) |

**Després del lot:**
- **Cita de CEO:** 5.995 de 6.012 files (99,7 %).
- **Grup F:** 349 de 349 files amb cita de CEO.

**Dubtes** (detall a `PENDENTS.md`):
- **CEO de la base diferent del de la font:** BME 2017-2018. La base té Zoido, però el consejero delegado era Hernani.
- **Criteri del CEO:** Vifor 2017-2019 (R3), Pandora 2018 (R2b) i Mapfre 2025 (R1/R3).
- **Sense document de l'exercici:** Inditex 2016.
- **Data o exercici a confirmar:** Aedifica 2019 (exercici de 18 mesos) i Lundberg 2016.
- **Interval amb un extrem de font B:** Clariant 2016 i Lonza 2019.

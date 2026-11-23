# Lot 15: cites de CEO dels informes anuals oficials (ESEF i FCA NSM)

- **Fet per:** Claude, 23/11/2026.
- **Abast:** les 1.306 files (P i F) que no tenien cita de CEO de l'exercici després dels lots 13 i 14, incloses les 18 del lot 11 que han quedat sense cita en revisar-ne l'exercici ([`lot15.csv`](lot15.csv)). Només s'hi afegeixen proves; **cap canvi de FounderCEO ni de `ceos`**.

## Mètode

1. **Informe de l'exercici.** Per a cada fila es busca l'informe anual oficial de l'exercici que inclou el 31/10 de l'any, és a dir, l'exercici que tanca entre el 31/10/*t* i el 30/10/*t+1*. Fonts:
   - **ESEF** (exercicis 2020-2025): l'informe financer anual que l'emissor diposita al dipòsit oficial del seu país, recollit a filings.xbrl.org. La data de tancament surt de les metadades del dipòsit. La correspondència ISIN → LEI es fa amb l'API pública de GLEIF ([`traspas/troba_esef.py`](../traspas/troba_esef.py); taula a [`traspas/isin_lei.csv`](../traspas/isin_lei.csv)).
   - **FCA NSM** (emissors britànics, qualsevol any): l'«Annual Financial Report» del National Storage Mechanism de l'FCA. La data de tancament de l'exercici es llegeix al mateix informe («for the year ended 30 April 2017»), perquè moltes empreses britàniques no tanquen el 31 de desembre ([`traspas/troba_nsm.py`](../traspas/troba_nsm.py)).

   Llista de documents per fila: [`lot15_documents.csv`](lot15_documents.csv). Hi ha informe per a 567 files.
2. **Cita.** [`traspas/extreu_ceo_documents.py`](../traspas/extreu_ceo_documents.py) busca al text de l'informe un fragment curt, literal, que anomeni el CEO de la fila amb un títol de primer executiu (o l'equivalent legal: Vorstandsvorsitzender, Président du Directoire, VD, Consejero Delegado…). Es descarten els fragments:
   - amb mots de sortida, de càrrec anterior o futur, o amb un títol adjunt (deputy, délégué…);
   - amb el càrrec en una altra entitat («CEO of …», «Administrador-Delegado da …»);
   - de taules (xifres amb separador de milers, percentatges) o amb el nom d'una altra persona entre el nom i el títol;
   - de text amb les lletres separades (passa en alguns ESEF);
   - on el cognom no surt com a nom propi (per exemple, «does» en lloc de «Does»), o on només surt un dels cognoms d'un nom compost.
3. **Verificació.** El fragment es comprova literalment al document baixat. Les cites són `[V]`, i la nota diu l'exercici, la font de la data de tancament i la mida del text.

Per afinar els filtres s'han revisat tres mostres a mà. Els casos dolents trobats i corregits abans d'escriure: el cognom «dos Santos» dins el nom d'una altra societat; una taula d'accionistes on el títol era d'una altra persona; i «does» com a verb.

## Resultats

| Recompte | Valor |
|---|---:|
| Files del lot | 1.306 |
| Files amb cita de CEO nova (C1) | 502 |
| Files fetes (cita de CEO i de fundador) | 147 (la resta de les 502 encara no tenen una prova de fundador completa) |
| … de les quals amb `ceo_interval` | 0 |
| Files en dubte enviades a `PENDENTS.md` | 0 (les files sense cita són a [`lot15_pendents.csv`](lot15_pendents.csv)) |
| Entrades noves `[V]` | 508: 350 d'ESEF (`plataforma`) i 158 de l'FCA NSM (`regulador`) |
| Entrades noves `[NV]` | 0 |
| Fonts antigues revisades | 0 |
| Canvis proposats a FounderCEO o `ceos` | 0 |

**Després del lot:**
- Cita de CEO: 5.204 de 6.012 files (86,6 %).
- Grup F: 338 de 349.
- Queden 804 files sense cita de CEO: 411 del 2016-2019 (abans del 2020 no hi ha ESEF; les britàniques no tenen informe a l'NSM o no hi ha cap frase que passi els filtres) i 393 del 2020-2025 (sense ESEF o sense frase que passi els filtres). Necessiten una cerca nova.

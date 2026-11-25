# Lot 25 · Casos oberts de la prova de no fundador i contradiccions revisades (25/11/2026)

## 1. Contradiccions revisades (3 entrades `revisio_font`)

Tres files P tenien una etiqueta `[ceo_fundador=…]`, que vol dir que una cita fa el CEO fundador. Se n'ha revisat la font. Les entrades noves porten `[ceo_fundador_descartat=…]` o `[ceo_fundador_resolt=…]`. No s'esborra res.

- **WPP 2018-2024:** error de codificació. La cita anomena fundadors Martin Sorrell i Preston Rabl, no Mark Read.
- **CD Projekt 2023:** homònim. Els fundadors són Michał Kiciński i Marcin Iwiński, i Adam Kiciński és una altra persona.
- **Steinhoff 2016-2017:** decisió vigent (regla 25). Es manté el 0, amb `conflicte_fonts` i robustesa a 1.

## 2. Cerca sense límit d'intents (A.4) per a les 15 empreses obertes

Brief a `lot25_brief_cerca.md`; resultat per empresa a `lot25_resum_cerca.csv`. Les entrades s'han importat amb `traspas/importa_entrades.py --lot 25 --origen casos_oberts`. Hi ha 22 cites d'aquesta cerca més 1 anul·lació:
- les 22 cites: 20 `[V]` i 2 cites de context de CD Projekt `[NV]`, que són fitxes en taula;
- l'anul·lació: QT Group 2016, l'any de l'escissió parcial de Digia, que no és un negoci nou (P1/P2, P4).

| Empresa | Resultat |
|---|---|
| Fresnillo | **Tancada:** naixement d'Octavio Alvídrez (Companies House, juliol del 1965) i P3 per la prova b sobre Peñoles (1887) |
| Valmet | **Tancada:** prova b contra el negoci operatiu de Valmet («Valmet was created in 1951», P1/P2) i prova d de Hinnerskov (entra el 2024 des de Mediq). Lectura per a Jordi: la J1 amb el 1951 (Laine era a Valmet des del 1988) |
| QT Group | **Tancada:** prova d contra la fusió de Digia del 2005, amb l'escissió del 2016 anul·lada |
| CD Projekt | Comprovació dels CEO a 31/10: Adam Kiciński (2016-2023) i Badowski i Nowakowski (2024-2025). Marcin Iwiński (cofundador) consta com a «Joint CEO» a les fitxes de l'emissor del 2016 al 2022, i la base ja el compta com a co-CEO el 2018-2021 (Q14). El 2016, el 2017 i el 2022 no són al panell. Cap canvi |
| Les altres 12 | **Sense font A/B:** Elia, Aedifica, Fresenius Medical Care, Scout24, BME, Vidrala, Metso, Haleon, Azimut, UBI, Swedbank i Millicom. El que s'ha mirat és a `lot25_resum_cerca.csv` |

## Efecte

- **Files P amb prova completa per parts:** 5.586 de 5.621 (**99,4 %**). Abans, 5.563.
- **Contradiccions obertes:** 0.
- **Files P sense prova completa:** 35, de 12 empreses. Després de la cerca sense límit, queden com a 0 sense prova completa. A la base final es declararan com a limitació (A.4), i es farà una robustesa que les tracti com a ND.
- **Canvis de FounderCEO o de `ceos`:** cap.

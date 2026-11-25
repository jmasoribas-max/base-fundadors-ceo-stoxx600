# Lot 26 · Segona font per als fundadors-CEO (25/11/2026)

Segueix la decisió de Jordi del 25/11/2026. La robustesa de dues fonts (Q6, `n_A + n_B ≥ 2`, criteri de Villalonga i Amit, 2006) deixava a ND 220 files F de 57 empreses en què el fundador només constava en un document. Per a cada una s'ha buscat un **segon document diferent**, A o B, que anomeni el CEO fundador o cofundador de la cotitzada o d'una predecessora, amb la redacció de la P6 o de la Q2.

- **Abast:** 2 tandes (brief a `lot26_brief_cerca.md`).
- **Resultat per empresa:** `lot26_resum_cerca.csv`.
- **Importació:** `traspas/importa_entrades.py --lot 26 --origen segona_font`. Són 76 entrades: 61 de fundador (54 `D37` i 7 `cita_fundador` de font B) i 15 de context. 75 són `[V]`. L'única `[NV]` és una cita de Derwent London que no surt literalment al document tornat a baixar.
- **Correcció de la robustesa:** `estat/robusteses.py` ara també compta com a document la cita de fundador de la columna antiga de la base (`font_classificacio_*`). Abans no la comptava, i algunes files semblaven tenir una sola font quan en tenien dues.

| | Abans | Després |
|---|---:|---:|
| Files F amb una sola font (`founderceo_rob_dues_fonts` = ND) | 220 (57 empreses) | **14 (5 empreses)** |
| % F a la robustesa de dues fonts | 2,30 % | **5,67 %** |

Les 14 files que queden amb una sola font:
- **Merlin Entertainments 2016-2019:** l'AR 2018 diu «led the management buy-out from Vardon Attractions to form Merlin in 1999». No és redacció de fundador de la P6, i un MBO no és una fundació nova (P1).
- **Tritax Big Box 2021-2025:** l'emissor diu «Having launched Tritax Big Box in 2013», i «launched» no és a la llista de la P6. L'empresa porta, a més, la marca `gestio_externa`.
- **Bridgepoint 2021-2022:** només el comunicat del 2024 l'anomena «Bridgepoint's Founder».
- **Derwent London 2016-2018:** la segona cita no s'ha pogut comprovar.

## Evidència contrària trobada (per a Jordi)

La cerca també ha trobat documents A que situen l'entrada del CEO a l'empresa després de la fundació. Són casos en què la cita de fundador de l'emissor (D37) preval, perquè la D37c es va rebutjar: la cita preval també davant de dades factuals contràries. El risc el cobreix la robustesa D37b, sense `fundador_transformador`.

| Empresa | Cita de fundador (D37 o Q2) | Dada contrària (A) |
|---|---|---|
| Investec (Koseff) | RNS 06/02/2018: «part of the "founding members" of Investec» | AR 2017, p. 118: «Stephen joined Investec in 1980» (fundació el 1974) |
| Bridgepoint (Jackson) | RNS 06/06/2024: «Bridgepoint's Founder» | Fullet de l'OPV del 2021: «employed by the group since 6 October 1986»; «Founded in 1984» |
| Petrofac (Asfari) | Comunicats del 2020 i el 2024: cofundador | AR 2016, p. 72: «Joined the Group in 1991 to establish Petrofac International» (negoci des del 1981) |
| Darktrace (Gustafsson) | City A.M. (B), 06/09/2024: cofundadora | Fullet de l'OPV del 2021: empleada des del novembre del 2014 (fundació el 2013). No exclou un paper fundacional |
| Paysafe (Leonoff) | Cita del grup successor (Q5) | El fullet regulat del 2015 diu que la cotitzada va comprar el negoci d'Optimal Payments el 2011. Leonoff va fundar SureFire el 1998 (Q1: fundador d'un negoci comprat) |

**Proposta:**
- A Investec, Bridgepoint i Petrofac, posar `fundador_transformador`=1 (D37b), com a Dassault: la persona no era a la fundació. Així entren a la robustesa sense `fundador_transformador`.
- Paysafe toca la Q1 i cal que Jordi decideixi: mantenir l'1 (D37 i Q5, amb D37b) o passar-lo a 0 (Q1, amb robustesa D1 àmplia = 1).

## Altres observacions de la cerca

- **Segons documents febles:** Eurofins i Neoen (la mateixa biografia, en un altre any de l'informe) i HelloFresh (un títol en una pàgina sense data). Compten com a documents diferents, però no són fonts independents.
- **Segona font d'una entitat relacionada:**
  - LondonMetric: fundador de Metric, predecessora per la fusió del 2013 (`dubte_D1`).
  - Zur Rose: fundador de Zur Rose Switzerland, el negoci original.
  - Idorsia: fundador d'Actelion, la mare (`d10_fundador_mare`).
  - MorphoSys: la font és Novartis, adquirent i successora (Q5).
- **Adyen 2023-:** Uytdehaage, el co-CEO, no és fundador (hi va entrar com a CFO el 2011). La segona font és de Van der Does.
- **Sagax:** conflicte de data de fundació (P7): 2004 al web, 2000 als fullets.

Cap canvi de FounderCEO ni de `ceos`.

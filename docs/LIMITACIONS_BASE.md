# Limitacions declarades de la base (esborrany viu)

**Estat:** esborrany de Claude, 25/11/2026. Les xifres són de la branca del lot 27, que inclou el lot 28 i el lot de correcció 5. Es tornaran a calcular quan es congeli la versió 1.0.0. Les robusteses surten de `estat/robusteses.py` (`estat/ROBUSTESES.md`) i l'estat per fila, de `estat/estat_files.py` (`estat/RESUM_ESTAT.md`).

Aquest document recull, en un sol lloc, el que la base **no** garanteix i com es mesura l'efecte de cada limitació. Ha de servir per a la secció de limitacions de la tesi i de l'article.

## 1. Cobertura de l'evidència

Panell: 6.012 files ISIN-any (350 F, 5.623 P, 31 NA i 8 ND).

| Condició | Files que la compleixen |
|---|---:|
| C1: cita del CEO a 31/10 (document de l'exercici o interval) | 5.994 (99,7 %) |
| C2: prova de fundador (F) o prova de no fundador completa per parts (P) | 5.974 (99,4 %) |
| C4: coherència i cap dubte obert | 6.000 (99,8 %) |
| C3: cites de CEO i de fundador verificades a la captura del Wayback | 287 (4,8 %), **en curs** |

La C3 és la condició que falta. Cada cita s'ha comprovat literalment al document original en baixar-lo (`[V]`). La còpia independent i permanent a l'arxiu la fa el flux automàtic de Wayback, que encara arxiva unes 4.700 URL.

## 2. Identificació del CEO

- **Interval (regla 28).** A 38 files el CEO s'acredita només per un interval, i a 71 més per un document i un interval. No s'ha comprovat que no hi hagi hagut cap canvi de CEO entre els dos extrems. Robustesa: `founderceo_rob_sense_interval` (5,76 % F).
- **Exercici de la cita (lot 27).** L'auditoria per mostra de 80 cites antigues no va trobar **cap CEO equivocat**. En canvi, un 24 % de les cites marcades pel script eren només un extrem del mandat (nomenament o sortida). Ja s'ha posat una cita de l'exercici a 198 de les 714 files afectades. Les altres 516 conserven la cita antiga: el CEO és correcte, però la prova del 31/10 és més feble.
- **President executiu, R3 i gestió externa.** Són regles úniques documentades: Q8b/Q9, Q12 i Q14. Robusteses: `founderceo_rob_sense_r3`, `founderceo_rob_sense_gestio_externa` (5,73 %) i `founderceo_rob_sense_titol_funcional` (5,79 %).

## 3. Fundadors (F)

- **Cita retrospectiva (D37a).** A 38 files la cita de fundador de l'emissor és posterior a l'any. Robustesa: `founderceo_rob_cita_contemporania`.
- **Fundador que no era a la fundació (D37b).** 27 files porten `fundador_transformador`=1 (p. ex. Dassault, Bridgepoint, Petrofac, Paysafe, B&M i Investec). La D37 preval i no s'admet l'excepció per dades contràries (D37c). Robustesa: sense `fundador_transformador`.
- **Fundador transformador (Q7, FT).** És 1 a l'anàlisi principal. Robustesa: `founderceo_rob_sense_ft`.
- **Una sola font (Q6).** Només 14 files F (Merlin, Tritax, Bridgepoint i Derwent London) tenen un únic document que anomeni el CEO fundador. Robustesa de dues fonts: 5,63 % F.
- **Conflicte de fonts (P6).** 7 files: Wirecard, Just Eat i Steinhoff. Robustesa amb el valor alternatiu: 5,97 % F.

## 4. No fundadors (P)

- **Prova completa per parts** (opció b, 24/11/2026): 5.588 de 5.623 files P (99,4 %).
- **Sense prova completa:** 35 files (12 empreses), després d'una cerca sense límit d'intents (A.4). Es mantenen a 0 i es declaren. Robustesa: `founderceo_rob_0_documentat`.
- **Dependència de criteris interpretatius (regla 25).** Segons `estat_files.py`, 943 files P només es tanquen gràcies a algun criteri de la regla 25:
  - P8 (llista d'un sol fundador): 651;
  - P3 (matriu corporativa): 152;
  - P1/P2 (fundació no nova): 87.

  Robustesa principal per al tribunal: `founderceo_rob_regla25_nd` (6,32 % F).
- **Llista d'una predecessora.** 127 files P es tanquen només amb la llista de fundadors d'una predecessora. En una fusió D1, aquesta llista pot no cobrir totes les parts. Robustesa: `founderceo_rob_llista_predecessora_nd` (5,98 % F).
- **Control de literalitat.** Una part de la prova només compta si el valor surt a la mateixa cita (any de fundació, naixement o edat, entrada).

## 5. Taxes d'error per mostra

| Revisió | Mostra | Resultat |
|---|---:|---|
| Lot 22: tancaments de la prova de no fundador | 40 | 1 prova incorrecta (P3 no comprovada), corregida al script; cap etiqueta 0 errònia en el fons |
| Lot 23: tancaments nous (P3 i anul·lacions) | 15 | 0 etiquetes errònies; 2 proves amb un defecte formal (una de corregida al script) |
| Wayback: `cita_ok` del flux, amb un codi independent | 60 | 60 correctes |
| Exercici de les cites de CEO antigues | 80 | 0 CEO equivocats; 24 % de les marcades sense prova del 31/10 |

## 6. Arxiu i accés a les fonts

- **Fonts que no s'obren amb curl pla.** A la mostra de l'auditoria, una part de les fonts antigues no es pot obrir amb curl pla: SEC, Akamai, Cloudflare i alguns llocs d'emissors. Per a aquestes, la comprovació independent depèn de la captura del Wayback.
- **Captures de pàgines d'error o d'una altra versió.** El flux torna a buscar les captures que són pàgines d'error. Quan la cita no és a la captura vigent, en busca altres captures de la mateixa URL i aplica la comparació flexible (`si_flexible`), que es compta a part.

## 7. Altres

- **Sector:** 150 files sense sector. Són les empreses presents només el 2024-2025 i les que no es van poder aparellar. No s'inventa cap sector.
- **Abast:** fora de la base queden els hereus, els episodis de CEO amb dates i altres variables (decisió de Jordi del 23/11/2026).

## 8. Resum de robusteses (mostra principal: 5.961 files, 5,85 % F)

| Robustesa | % F |
|---|---:|
| Regla 25 com a ND | 6,32 % |
| P8 com a ND | 6,57 % |
| Llista d'una predecessora com a ND | 5,98 % |
| Sense interval | 5,76 % |
| Dues fonts | 5,63 % |
| Conflicte de fonts (valor alternatiu) | 5,97 % |
| Sense gestió externa | 5,73 % |
| 0 sense prova completa com a ND | 5,89 % |

La proporció de fundadors-CEO es manté entre el 5,5 % i el 6,6 % en totes les robusteses. El resultat principal no depèn d'un criteri concret.

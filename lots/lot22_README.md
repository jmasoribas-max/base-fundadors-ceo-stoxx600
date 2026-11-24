# Lot 22 · Pas 3: cerca per tancar la prova de no fundador (24/11/2026)

Tercer pas per a les files P (FounderCEO = 0) que, després dels lots 18 i 21, encara no tenien la prova completa per parts. Segueix la decisió de Jordi del 24/11/2026, opció b: un 0 només compta com a documentat si la prova té totes les parts i cada part té la seva cita A/B. Jordi va aprovar el pas 3 el mateix dia.

## Què s'ha fet

- **Abast:** 498 empreses amb alguna fila P sense prova completa, repartides en 25 tandes d'unes 20 empreses. Cada tanda l'ha feta un agent de cerca amb el mateix brief (`lot22_brief_cerca.md`).
- **Ordre de cerca per empresa:**
  1. drecera per la prova a (llista tancada de fundadors) o la prova e (creada per l'Estat o per una altra empresa, amb la P3);
  2. any de fundació de l'entitat que compta (P1, D1 estricta de la regla 26, regla 21b);
  3. any de naixement de cada CEO;
  4. només si el naixement no surt, ocupador anterior i any d'entrada (prova d).
- **Format de les parts:** cada cita porta una etiqueta estructurada a `notes` (`[part any_fundacio=…]`, `[part naixement_ceo=…]`…). L'aritmètica de la regla 21 la fa `estat/estat_files.py`.
- **Anys de fundació descartats:** quan una font registrada dona un any que no és una fundació (holding nova, redomiciliació, any d'una fusió que no és D1), l'agent ho ha indicat i s'ha afegit l'etiqueta `[anula any_fundacio=YYYY; motiu=…]`. Afecta 18 empreses.
- **Importació:** `traspas/importa_entrades.py --lot 22 --origen pas3_cerca`. Cada cita s'ha tornat a baixar de la URL original i s'ha comprovat que hi surt literalment.

| Resultat de la cerca (per empresa, segons l'agent) | Empreses |
|---|---:|
| Tancada: prova completa per a tots els anys oberts | 469 |
| Parcial | 28 |
| No trobada | 1 |

| Entrades noves al registre | |
|---|---:|
| Total (`evidencia_fundador`) | 1.754 |
| `[V]`: cita literal comprovada al document tornat a baixar | 1.743 |
| `[NV]` `no_valida`: cita de taula que no surt literalment (11; 7 són taules de noms anteriors de Companies House) | 11 |

## Control de literalitat de les parts (nou a `estat/estat_files.py`)

La revisió de les etiquetes ha trobat cites en què el valor de l'etiqueta no surt a la cita mateixa. Per exemple, un any de fundació que només surt al títol de la secció, o un any de naixement deduït d'una taula. Des d'ara, una part només compta si la cita mateixa la documenta. El control s'aplica a tots els lots, no només al 22:

- **any de fundació, entrada i inici del mandat:** l'any ha de sortir a la cita (o la dècada, «1930s», si l'etiqueta en dona l'últim any);
- **naixement:** l'any o una edat;
- **ocupador anterior:** l'any d'entrada que porta només s'usa per a la prova d si surt a la cita.

Efecte: 108 files P menys amb prova completa (del 97,3 % al 95,4 %). Als lots anteriors, 9 menys.

## Efecte a la C2 de les files P

Mateix criteri (amb el control de literalitat) abans i després del lot:

| | Abans del lot 22 | Després del lot 22 |
|---|---:|---:|
| Files P | 5.629 | 5.629 |
| **Amb prova completa per parts** | 2.912 (51,7 %) | **5.371 (95,4 %)** |
| … prova a | 1.621 | 1.882 |
| … prova e | 593 | 886 |
| … prova b | 481 | 1.848 |
| … prova d | 114 | 649 |
| … prova c | 103 | 106 |
| Amb alguna part però sense prova completa | 2.521 | 248 (61 empreses) |
| Sense cap part | 186 | 0 |
| Cita que diu que el CEO és fundador (a revisar, ja venia del lot 18: WPP, Steinhoff, CD Projekt) | 10 | 10 |

Cap canvi de FounderCEO ni de `ceos`.

## Dubtes per a Jordi (`lot22_dubtes.csv`)

`lot22_dubtes.csv` recull les 38 empreses parcials, no trobades o amb un dubte de fundador o de contradicció. Les que demanen una decisió són aquestes:

| Empresa | Dubte | Proposta |
|---|---|---|
| Dassault Systèmes FR0014003TT8 2021-2023 (Charlès) | L'emissor l'anomena «Co-Founder». La correcció C3 (0 → 1, D37) ja està aprovada per al 2016-2020 sota l'ISIN antic | Aplicar-hi el mateix criteri quan es registri la cita amb el nom complet (pendent de la C3) |
| BillerudKorsnäs SE0000862997 2017 | L'informe de sostenibilitat del 2017 diu que Petra Einarsson va substituir Per Lindberg a l'inici del 2017; la base diu Lindberg | Revisar el CEO del 2017 (possible error E2) en un lot de correcció |
| Foncière des Régions / Covivio FR0000064578 | L'emissor diu que Kullmann és al capdavant «depuis sa création en 2001», però l'històric de l'emissor dona el 1963 | Principal 1963, amb `data_fundacio_conflicte` i robustesa com a ND (P7) |
| FinecoBank IT0000072170 | Pista B (Forbes Italia, inaccessible) que podria descriure Foti com a creador de Fineco | Cerca sense límit (A.4); sense cita, es manté 0 sense prova completa |
| Wirecard DE0007472060 | Una font B registrada diu «founded by Markus Braun». El Bundestag i l'emissor diuen que Braun hi va entrar el 2002 des de KPMG (prova d, just 3 anys) | 0 amb `conflicte_fonts` (P6: preval la prova A) i robustesa 1 |
| Wise GB00BL9YR756 2023 | El CEO titular (Käärmann, cofundador) era de sabbàtic; la base dona Sinha | Confirmar que Sinha és CEO interí (R2) el 31/10/2023 |
| Steinhoff NL0011375019 | `conflicte_fonts` (TimesLIVE) i cerca de «founder» als informes del 2015 incompleta | Es manté la decisió vigent (regla 25) |
| Acciona Energía ES0105563003 | Una notícia de l'emissor diu que Mateo és «one of its creators» | La P6 exclou «creator»: 0, informat |
| Safestore GB00B1N7Z094 i JLT GB0005203376 | El CEO va fundar un negoci que després la cotitzada va comprar | Q1: 0, amb `dubte_D1` i robustesa D1 àmplia = 1 |

La pregunta de la tanda 24 sobre les fusions (Vopak, Glanbia, Vonovia, Sobi) no és un dubte nou: la regla 21b ja diu que, en una fusió entre iguals (D1), la prova es fa contra la part on era la persona, i no contra l'any de la fusió.

## Verificació per mostra

Un verificador independent revisa una mostra aleatòria de 40 files tancades pel lot 22 (llavor 20261124). El resultat s'afegirà a aquest fitxer i al PR abans de fusionar.

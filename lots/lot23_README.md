# Lot 23 · Pas 3b: última passada per tancar la prova de no fundador (25/11/2026)

Última passada per a les files P (FounderCEO = 0) que, després del lot 22, encara no tenien la prova completa per parts (decisió de Jordi del 24/11/2026, opció b). Jordi va donar l'OK el 25/11/2026 («Ja pots seguir amb la feina»).

## Què s'ha fet

- **Abast:** 121 empreses (535 files P), en 5 tandes d'unes 24 empreses. Brief: `lot23_brief_cerca.md`.
- **Prioritats:**
  1. la P3 de la prova e: l'any de fundació de la matriu, la llista dels seus fundadors o el seu origen estatal, amb l'etiqueta `entitat=matriu`, i el naixement del CEO;
  2. si no, les proves b o d sobre l'emissor;
  3. substituir les parts que el control de literalitat havia rebutjat.

  Cada tanda tenia, per a cada empresa, el que ja hi havia registrat i el que la cerca del lot 22 ja havia mirat.
- **Descàrregues:** només amb curl pla (sense agent de navegador ni capçaleres afegides). L'eina de descàrrega dels agents s'ha corregit perquè no enviï un agent d'usuari de navegador.
- **Importació:** `traspas/importa_entrades.py --lot 23 --origen pas3b_cerca`. Cada cita s'ha tornat a baixar de la URL original i s'ha comprovat que hi surt literalment.

| Resultat de la cerca (per empresa, segons l'agent) | Empreses |
|---|---:|
| Tancada | 108 |
| Parcial | 4 |
| No trobada | 9 |

| Entrades noves al registre | |
|---|---:|
| `evidencia_fundador` | 185 |
| `revisio_font` (anul·lació d'un any de fundació que no és una fundació, amb la cita de l'entrada original) | 3 |
| **Total, totes `[V]`** | **188** |

## Anys de fundació anul·lats

Els agents han proposat anul·lar 26 anys de fundació registrats que no són una fundació nova. Se n'apliquen 24, amb l'etiqueta `[anula any_fundacio=…]`:

- **P1/P2:** holding nova, vehicle d'una compra (LBO), reorganització dins el grup o escissió. Casos: UBS 2014, Allegro 2017, Aareal 2001, Unicaja 2011, ABN AMRO 2009, Harbour Energy 2014, Linde 1992, Suez 2000, SFR 2013, Legrand 1998, Acciona Energía 2008, Technip Energies 2019 i Acciona 1997.
- **Fusió (regla 26 i regla 21b):** la prova es fa contra la part on era el CEO, o contra la més recent de totes les parts. Casos: ThyssenKrupp 1999, Vopak 1999, Glanbia 1997, Metso 1999, EssilorLuxottica 1972, Travis Perkins 1988, BPER 1984, Diageo 1997, AB InBev 1987, DNB 2003, Carnival 2000.

No s'apliquen dues anul·lacions, perquè no tanquen cap prova i la J1 no es podria aplicar bé: Fresenius Medical Care 1996 (no hi ha cap altre any registrat) i BME 2002 (falta saber si el 2002 és una D1 o una holding).

**Limitació:** quan s'anul·la l'any d'una fusió, el script pren l'any més recent de les parts registrades. Si la part on era el CEO no és la més recent i falta l'any d'una altra part, el resultat pot no seguir exactament la J1. En els casos d'aquest lot, l'agent ha comprovat a quina part era el CEO.

## Correcció de `estat/estat_files.py`

Hi havia files que no es tancaven perquè el script no llegia la data del document quan la descripció del document porta una coma (per exemple, «comunicat de l'emissor (EQS-News, Hannover Rück SE)»). Ara busca la data a tot el segment «Document: …».

## Efecte a la C2 de les files P

Mateix criteri abans i després del lot:

| | Abans del lot 23 | Després del lot 23 |
|---|---:|---:|
| Files P | 5.629 | 5.629 |
| **Amb prova completa per parts** | 5.089 (90,4 %) | **5.587 (99,3 %)** |
| … prova a | 1.892 | 1.929 |
| … prova e | 494 | 665 |
| … prova b | 1.885 | 2.087 |
| … prova d | 704 | 793 |
| … prova c | 114 | 116 |
| Amb alguna part però sense prova completa | 530 (120 empreses) | 29 (12 empreses) |
| Amb una cita que diu que el CEO és fundador | 10 | 13 (+ Dassault 2021-2023) |

Cap canvi de FounderCEO ni de `ceos`. Dassault Systèmes 2021-2023 passa a «contradicció», perquè s'hi ha afegit la cita del Document d'enregistrement universel 2025 («cofondateur de Dassault Systèmes»). Jordi ja ha decidit que és 1 (25/11/2026), i s'aplicarà en un lot de correcció juntament amb la C3.

## Què queda obert (29 files P, 12 empreses; `lot23_dubtes.csv`)

| Empresa | Anys | Què falta |
|---|---|---|
| Fresenius Medical Care | 2016-2021 | Any de fundació de National Medical Care amb cita A/B (fusió D1 del 1996) |
| BME | 2016-2019 | Naixement de Zoido i d'Hernani; decidir si el 2002 és una D1 o una holding |
| UBI Banca | 2016-2019 | Any de fundació de Banca Lombarda o de San Paolo di Brescia (J1) amb font A/B |
| Swedbank | 2016-2018 | On va entrar Bonnesen el 1987 (J1) |
| Fresnillo | 2016, 2017, 2020, 2025 | Naixement d'Octavio Alvídrez amb font A/B |
| Elia | 2023-2024 | Vandenborre hi va començar el 1999: cal la prova e de l'Elia del 2001 (la font fa 403). Diu «I was present at the inception of Elia», que no és una expressió de fundador (P6, Q2) |
| Azimut | 2016 | Entrada o ocupador anterior de Malcontenti i Mungo; fundadors d'Akros Finanziaria |
| Metso | 2025 | A quina part (Valmet o Rauma) va entrar Takaluoma el 1997 |
| QT Group | 2021 | P3 sobre Digia: no hi ha llista de fundadors A/B |
| Scout24 | 2025 | Ocupador anterior de Weitz; P3 sobre Beisheim Holding |
| Vidrala | 2023 | Naixement o ocupador anterior de Gorka Schmitt |
| Millicom | 2024 | Naixement de Benítez (Tigo és la seva primera feina) |

Aquestes files van a la cerca sense límit d'intents (A.4). Si no s'hi troba cap font A/B, la fila queda com a 0 sense prova completa: es declara com a limitació i es fa la robustesa corresponent.

## Lectures de la P3 que convé que Jordi conegui

- **Matriu formada per una fusió:** a Sandoz, Novozymes, Valmet i Haleon s'ha pres com a any o fundadors de la matriu el de les parts de la fusió (Ciba-Geigy i Sandoz; Novo i Nordisk; Valmet i Rauma; Glaxo Wellcome i SmithKline Beecham), seguint la regla 21b. Els CEO van néixer molt després de la fundació d'aquestes parts.
- **Telefónica Deutschland:** VIAG consta com a «reichseigene» (propietat de l'Estat alemany), i BT, com a successora per llei (Telecommunications Act 1984).

## Verificació per mostra

Un verificador independent revisa una mostra estratificada de 15 files tancades pel lot: 6 per la P3, 5 que depenen d'una anul·lació i 4 més. El resultat s'afegirà aquí i al PR.

# Paquet de criteris v2 (24/11/2026)

> **Estat:** Q2, Q3, Q8, Q9 (Telefónica) i Q11 decidides per Jordi el 24/11/2026 (vegeu la secció «Decisions ja preses»). La resta, oberta.

Preparat per Claude perquè Jordi decideixi. Substitueix els punts 2-10 de `docs/PAQUET_CRITERIS_20261123.md`. El punt 1 ja està decidit (24/11/2026, opció b) i aquí no es torna a obrir.

D'on surt: un triatge de dos agents (anàlisi i verificació contrària) sobre els **113 grups de dubtes oberts (266 files)** de `PENDENTS.md`. Classificació final (`cl_final`):

| Classe | Grups | Files (ISIN-any, sense repetir) | Què cal fer |
|---|---:|---:|---|
| `cal_cerca` | 41 | 114 | Buscar fonts. Ho fa Claude; no cal decisió |
| `tancable_amb_evidencia` | 34 | 94 | Es poden tancar amb el registre actual. Alguns porten canvis de dades sense canvi d'etiqueta (vegeu la secció «Canvis de dades dels tancaments») |
| `criteri_jordi` | 33 | 72 | **Preguntes Q1-Q14 d'aquest paquet** |
| `correccio_proposada` | 5 | 10 | **Correccions C1-C4 d'aquest paquet** |

Una fila pot tenir dubtes en més d'una secció de `PENDENTS.md`; per això la suma de la columna de files (290) passa de 266.

Mentre no hi hagi decisió, no es toca cap etiqueta: les files continuen en dubte. Res d'aquest paquet canvia `dades/` sense un lot de correcció aprovat per Jordi.

Aquesta versió incorpora les correccions de la verificació independent del 24/11 (`verif_paquet.md`, secció «Resposta»).

---

## Decisions ja preses (Jordi, 24/11/2026, tarda)

| Q | Decisió | Efecte |
|---|---|---|
| Q2 | **Compten com a fundador** (opció b, contra la recomanació). S'estén a «founding partner», «founding director» i «part of the founding group» | alstria 2019-2021 i Rightmove 2016 es mantenen a 1 per D37 (alstria, quan es registri la cita de l'emissor); Reply 2021-2025 té la cita «part of the founding group» / «one of the founding members» per a Rizzante; Aberdeen 2016 i SoftwareONE 2020 no canvien |
| Q3 | **No compta sola** (opció a), després de comprovar Cellnex, Ocado, B&M i Metro Bank | Cellnex 2016-2022: d'1 a ND, o a 0 si es documenta la prova (lot de correcció); Ocado i B&M no canvien; Metro Bank 2017-2018 es queda a 0 |
| Q8 | **Co-CEO per R1** (opció a) | Ferrovial: s'afegeix Rafael del Pino y Calvo-Sotelo a `ceos` (9 files); FounderCEO no canvia |
| Q9 | **Telefónica: només el president** per R1 amb `ceo_president_exec` (opció a); la Q9b continua oberta | `ceos` no canvia a Telefónica |
| Q11 | **El Gérant és CEO per R1** (opció a): un representant d'una societat Gérante compta si l'emissor l'anomena Gérant | Rubis: `marca_prova` R3 → R1 i fora `de_facto`; FounderCEO no canvia |

Text normatiu: secció «Decisions de Jordi del 24/11/2026 (tarda)» de `CLAUDE.md` i `AGENTS.md`.

---

## Resum (una pantalla)

**15 preguntes de criteri i 4 correccions de dades.** Les preguntes Q1-Q14 cobreixen les 72 files dels grups `criteri_jordi`; Q15 no en té de pròpies. Quatre preguntes porten una subpregunta (Q5b, Q8b, Q9b i Q12b), perquè la resposta principal no la decideix. Algunes preguntes també afecten files de grups de cerca: s'indica a la columna «Files». Es pot respondre «d'acord amb totes» o triar-ne alguna (p. ex. «Q3 no, la resta sí»).

| Q | Pregunta curta | Files | Recomanació |
|---|---|---:|---|
| Q1 | Fundador d'una part adquirida en una fusió amb `dubte_D1` (Standard Life Aberdeen) | 2 (+3 d'EssilorLuxottica i +3 d'ICAP/NEX si la cerca hi troba `dubte_D1`) | La cita de fundador de la part adquirida no compta: 0 amb `dubte_D1` i robustesa D1 ampla = 1. **(sí/no)** |
| Q2 | «founding member» i «co-founding executives» (alstria, Rightmove) | 4 | No compten com a fundador. **(sí/no)** |
| Q3 | «CEO fundador» (Cellnex). Reobre la decisió C0220 de Doctorat, que Jordi va fer aplicar el 23/11 | 8 | No compta: equival a «founding CEO». **(sí/no)** |
| Q4 | «Prior to setting up Energean, Mathios…» (Energean) | 1 | Compta (D37, «set up» amb la persona com a subjecte). **(sí/no)** |
| Q5 | «Leonoff founded Paysafe», que per l'any remet al negoci comprat el 2011 (Paysafe) | 2 | Compta (D37), amb `fundador_transformador`=1. **(sí/no)** |
| Q5b | Cita de l'emissor publicada pel grup successor després de la descotització (Paysafe; Merlin, grup de cerca) | 2 (+4 de Merlin) | Compta com a font de l'emissor, amb `allotjament=successor` i sense cita contemporània (D37a). **(sí/no)** |
| Q6 | «Cofundador» només en font B, davant d'un fet A que no tanca cap prova (Evraz) | 3 | 1 per la P6 amb `si_font_B`. **(sí/no)** |
| Q7 | Comprador que transforma una empresa existent: FT o no (ACS, Florentino Pérez) | 2 | Primer buscar D37; si no n'hi ha, Jordi decideix si és FT (el criteri FT del PROTOCOL no és al repositori); si no ho és, 0 per la d. **(sí/no)** |
| Q8 | Dues persones amb el títol de consejero delegado (Ferrovial) | 9 | Co-CEO per R1. **(sí/no)** |
| Q8b | EssilorLuxottica 2020: Président-Directeur Général i Vice-Président-Directeur Général Délégué (antic punt 7) | 1 (fora del triatge) | Un sol CEO per R1 (Del Vecchio), com el 23/11. **(sí/no)** |
| Q9 | President executiu amb el títol de CEO al document de l'emissor (Telefónica, Mapfre) | 10 | Mana el títol: qui té el títol de CEO al document de l'exercici és el CEO per R1, amb `ceo_president_exec`. **(sí/no)** |
| Q9b | El títol de CEO només surt a la traducció anglesa de l'emissor i l'original diu «Presidente» (Mapfre, Inditex; cal comprovar Telefónica) | Mapfre 2025 (dins Q9) +3 de Mapfre i +2 d'Inditex; condiciona Telefónica | Mana el càrrec de l'original: R3 amb `ceo_president_exec`. **(sí/no)** |
| Q10 | Dos CEO amb una plaça vacant que assumeix el president fundador (Luxottica) | 2 | Només Vian per R1 (0); Del Vecchio = 1 només a la robustesa R3. **(sí/no)** |
| Q11 | Gérant d'una SCA (Rubis) | 10 | R1 per als Gérants; un representant d'un Gérant societat només si l'emissor l'anomena Gérant. **(sí/no)** |
| Q12 | Vehicles gestionats externament (Tritax, Primary Health) | 6 | Mana el que diu l'informe de l'emissor de cada any (R1, R3 o R-SC, en aquest ordre). **(sí/no)** |
| Q12b | Font A de l'emissor («sense direcció pròpia») contra font B («CEO») sobre qui és el CEO (BB Biotech). **És un criteri nou** | 4 | Preval la font A de l'emissor: NA (R-SC). **(sí/no)** |
| Q13 | CEO titular impedit o de baixa (Hexagon, Uniper) | 2 | El titular continua sent el CEO (R1). **(sí/no)** |
| Q14 | Títol funcional «Joint CEO» (CD Projekt) | 4 (+1 del 2023) | Compta per R1 (co-CEO), amb robustesa sense ell. **(sí/no)** |
| Q15 | Document de l'any *t* anterior al 31/10 (antic punt 8) | 3* | S'accepta com a document del mateix exercici, amb nota. **(sí/no)** |

\* Q15 no afegeix files noves: CD Projekt 2020-2021 ja és a Q14, i Wizz Air 2021 és un grup tancable que en depèn.

| C | Correcció de dades | Files | Recomanació |
|---|---|---:|---|
| C1 | BME 2017-2018: `ceos` Zoido → Hernani (R1, P5) | 2 | Aprovar **(sí/no)** |
| C2 | Sopra Steria 2025: FounderCEO ND → 0 (prova a) | 1 | Aprovar **(sí/no)** |
| C3 | Dassault Systèmes 2016-2020: FounderCEO 0 → 1 (D37) | 5 | Aprovar **(sí/no)** |
| C4 | Bridgepoint 2021-2022: FounderCEO 0 → 1 (D37) | 2 | Aprovar **(sí/no)** |

**Efecte si s'accepten totes les recomanacions:**
- **Etiqueta FounderCEO:** canvien **22 files segures**: 14 per les preguntes (Q1: 2 d'1 a 0, Standard Life Aberdeen, amb la condició de la cita de Skeoch; Q2: 4 d'1 a ND; Q3: 7 d'1 a ND i 1 de 0 a ND) i 8 per les correccions (C2: 1 de ND a 0; C3: 5 de 0 a 1; C4: 2 de 0 a 1). **Condicionades a una cerca:** EssilorLuxottica 2018-2020 (3 files, 1 → 0, Q1) i ICAP/NEX 2016-2018 (3 files, 1 → 0 o ND, Q1) si s'hi documenta `dubte_D1`; Tritax 2021 (1 fila, 1 → NA en el pitjor cas, Q12); CD Projekt 2023 (1 fila, 0 → 1 si hi ha cita, Q14); Merlin 2016-2019 (4 files: es mantenen a 1 si Q5b és «sí» i es verifica C0306; si no, depenen de la cerca de la prova d).
- **Mostra principal (`a_mostra_principal`):** en surten 11 files (Q2: 4; Q3: 7; la segona línia de Cellnex del 2019 ja n'és fora, perquè és `dret_temporal`) i n'hi entra 1 (C2). Les files de Q1, C3 i C4 hi continuen (passen de 1 a 0 o de 0 a 1).
- **CEO (`ceos`):** canvien 11 files: 9 de Ferrovial (Q8, s'hi afegeix un co-CEO) i 2 de BME (C1). A Rubis (Q11) en poden canviar fins a 8 més: Clarisse Gobin-Swiecznik el 2023-2025 (3) i Jacques Riou el 2021-2025 (5), si no es troben cites que els anomenin Gérant. A Telefónica 2025 (Q9) en pot canviar 1 (co-CEO amb Gayo, si es confirma la p. 232). Amb Q9b, si l'original castellà de Telefónica no dona a Álvarez-Pallete el títol de CEO, en canvien 8 més (Vilá el 2017-2024). Fora dels grups del triatge, el criteri de Q8 s'hauria de comprovar a NL0015001FS8 2023-2025 i a ACS 2017-2020 (fins a 7 files).
- La resta són marques, robusteses o la regla anotada, sense canvi d'etiqueta ni de CEO. Les opcions no recomanades també poden canviar files: s'indica a l'«Efecte» de cada pregunta (p. ex. Q12b, opció b: 4 files de NA a 0).

---

## Què ha passat amb els punts 2-10 del paquet del 23/11

| Punt del 23/11 | Cas | Ara |
|---|---|---|
| 2 | ICAP / NEX (Spencer) | **Cerca, i després Q1 si cal.** Cal el repartiment del capital i el mètode comptable de la combinació Garban-Intercapital del 1999. Si cap dada no contradiu la «merger» de l'emissor, s'aplica la D1 i l'1 es manté (regla 26, D37d). Si la cerca troba que Garban va adquirir Intercapital, hi ha `dubte_D1` i la resposta de **Q1** s'hi aplica (3 files) |
| 2 | Standard Life Aberdeen (Gilbert) | **Q1** |
| 2 | Petrofac (Asfari) | **No cal decisió.** La regla 24 i la P1 («La D37 preval») ja ho resolen. Falta registrar la cita del comunicat del 12/10/2020 amb el nom d'Asfari (cerca) |
| 3 | Cellnex (Martínez) | **Q3** |
| 3 | Merlin (Varney) | **Cerca, i depèn de Q5b.** Al repositori hi ha una candidata (`traspas/candidates_evidencia.csv`, C0306, backstage.merlinentertainments.biz, 18/06/2023, «their founder», Wayback 20240713022455). És posterior a la descotització i, segons el verificador, l'allotjament és `successor`; «their founder» ho diu la plantilla. Si Q5b és «sí» i es verifica, és D37 i l'1 es manté. Ja no es proposa 1 → 0 |
| 4 | Rightmove, «founding member/partner…» | **Q2** |
| 4 | Energean | **Q4** |
| 5 | alstria (Elamine) | **Q2** (expressió) + cerca de la prova e i la P3 |
| 5 | Sagax (Mindus) | **Cerca.** Primer el prospecte del 2007 i la pàgina about-sagax (ja amb captura); després premsa B (si n'hi ha, 1 amb `si_font_B`) |
| 6 | Primary Health, Tritax | **Q12** (la recomanació canvia: ja no R-SC per coherència, sinó el que diu l'emissor cada any) |
| 6 | BB Biotech (gestor extern) | **Q12b** (pregunta nova: font A de l'emissor contra font B sobre el CEO) |
| 6 | CD Projekt | **Q14** |
| 6 | Zalando | **Cerca.** Els comunicats C04-C06 només anomenen co-CEO Rubin Ritter. Cal un document de l'exercici que anomeni Gentz i Schneider co-CEO; si no n'hi ha, torna com a pregunta sobre documents retrospectius |
| 6 | Rubis | **Q11** |
| 7 | EssilorLuxottica 2020 (CEO) | **Q8b** (mateixa recomanació que el 23/11) |
| 8 | Documents del mateix exercici | **Q15** |
| 9 | Cites del lot 11 d'un altre exercici | Informatiu, sense canvis |
| 10 | Resta de dubtes | Substituït pel triatge (taula de dalt) |

---

## A. Preguntes sobre el fundador

### Q1. Fundador d'una part adquirida en una fusió amb `dubte_D1`

**Pregunta.** Si una fusió és `dubte_D1` (es diu «merger», però es comptabilitza com a adquisició) i el CEO és fundador de la part **adquirida**, la cita de fundador d'aquesta part el fa fundador de la cotitzada?

**Casos.**

| ISIN | Empresa | Anys | Files | Base ara | Dubte a PENDENTS | Estat del `dubte_D1` |
|---|---|---|---:|---|---|---|
| GB00BVFD7Q58 | Standard Life Aberdeen | 2017 | 1 | 1 (co-CEO Skeoch i Gilbert) | lot10, lot16 | Documentat (X03, X04) |
| GB00BF8Q6K64 | Standard Life Aberdeen | 2018 | 1 | 1 (co-CEO Skeoch i Gilbert) | lot10, lot16 | Documentat (X03, X04) |
| FR0000121667 | EssilorLuxottica | 2018-2020 | 3 | 1 (Del Vecchio) | lot10 | **No documentat: pendent de cerca** |
| GB0033872168 / GB00BZ02MH16 | ICAP / NEX | 2016 / 2017-2018 | 3 | 1 (Spencer) | lot10, lot16 (grups de cerca) | **No documentat: pendent de cerca** |

Les 8 files són certificades a la base. Només les 2 files de Standard Life Aberdeen compleixen avui la premissa de la pregunta.

Fets del registre:
- Standard Life Aberdeen: «He is co-founder (and former chief executive) of Aberdeen Asset Management PLC» (L16-…-F01, AR 2017 p. 64 i AR 2018 p. 52). L'operació es va comptabilitzar «as an acquisition of Aberdeen by Standard Life plc» (L7-GB00BF8Q6K64-X03) i els accionistes de Standard Life en tenien el 66,7 % (X04). **Atenció:** X02, X03 i X04 estan registrades per als anys 2019-2025, i X01 (Standard Life del 1825) per al 2016; cap no cobreix el 2017 ni el 2018. Cal ampliar-ne els anys abans d'aplicar-ho.
- EssilorLuxottica: «Leonardo Del Vecchio is the founder of the Group's operations and has been Chairman of the Board since the Group was formed in 1961» (L11-FR0000121667-F01): és el grup Luxottica, no l'antiga Essilor (1972, L9-X01), que és la persona jurídica cotitzada. Al registre no hi ha cap cita sobre l'OPE, la nota IFRS 3 ni el repartiment del capital del 2018. Per tant, avui no es pot dir si hi ha `dubte_D1` ni si cap part superava el 60 %.
- ICAP/NEX: L16-F01 (fullet de NEX) anomena Spencer fundador d'Intercapital («He founded Intercapital in 1986»), no d'ICAP. L'emissor parla de «merger». Al registre no hi ha el repartiment del capital ni el mètode comptable de la combinació Garban-Intercapital del 1999.

**Metodologia.**
- Regla 26: «Una adquisició, o la compra d'una start-up, no fa fundadors els seus fundadors. Si no queda clar, no s'aplica la D1 (`dubte_D1`).» Lectura: «hi ha `dubte_D1`, no s'aplica la D1 i la fundació rellevant és la de la part absorbent o la de la part on era la persona (J1)».
- Regla 24 (D37): la cita ha de ser de la «cotitzada, grup o predecessora legal o econòmica documentada, D37d».
- Regla 25, P6: no compten «les cites de fundador d'una altra entitat».
- Secció 2.3, punt 9: «si un dels co-CEO és fundador, FounderCEO val 1».

**El buit.** La lectura de la regla 26 dona dues fundacions possibles («la part absorbent o la de la part on era la persona»). Aquí no coincideixen: per a Gilbert, Standard Life (1825) porta a 0 i Aberdeen (que va cofundar) porta a 1.

**Opcions.**
- a) Es prova contra la part absorbent: la cita de la part adquirida no compta → 0, amb `dubte_D1` i robustesa D1 ampla = 1.
- b) Es prova contra la part on era la persona (J1) → 1.
- c) ND fins que es decideixi cas per cas.

**Recomanació: a.** La regla 26 diu «Una adquisició, o la compra d'una start-up, no fa fundadors els seus fundadors», la P6 i la D37d exclouen la cita d'una altra entitat, i el precedent de Drillisch (regla 27: «Alphatel i E.I.C. no són predecessores (adquisició, no D1 estricta; D37d)») va en aquest sentit. La J1 serveix per triar l'any de les proves de no fundador, no per donar la condició de fundador. Els dos agents del triatge hi coincideixen.

**Efecte.**
- Standard Life Aberdeen 2017 i 2018: 1 → 0 (2 files), amb `dubte_D1` i robustesa D1 ampla = 1. **Condicions abans d'aplicar-ho:** 1) ampliar als anys 2017 i 2018 les entrades X01-X04 (o registrar-ne de noves); 2) registrar la cita de l'any d'entrada de Skeoch a Standard Life (1999), que ara només és a les notes. La prova d de Gilbert es completa amb L16-F01 (entrada el 14/8/2017 des d'Aberdeen) i la fundació de Standard Life (1825), un cop ampliats els anys. Aberdeen 2016 (GB0000031285) es manté a 1.
- EssilorLuxottica 2018-2020 (3 files): **no s'aplica Q1 fins que la cerca documenti l'operació** (Document de référence 2018 o document de l'OPE a l'AMF). Si hi ha `dubte_D1`, s'hi aplica la resposta de Q1 (amb a: 1 → 0, prova d contra Essilor, 1972; Del Vecchio hi entra l'1/10/2018). Si l'operació compleix la D1 (descrita com a combinació i cap part per sobre del 60 %), es manté l'1 per D37 sobre una predecessora D1.
- ICAP/NEX 2016-2018 (3 files): el mateix. Si la cerca no troba res que contradigui la «merger» de l'emissor, s'aplica la D1 i l'1 es manté. Si troba que Garban va adquirir Intercapital, hi ha `dubte_D1` i, amb a, la fila passa a 0 si es completa una prova de no fundador contra Garban, o a ND si no.

---

### Q2. «founding member» i «co-founding executives»

> **Decidit (Jordi, 24/11/2026): compten (opció b)**, també «founding partner», «founding director» i «part of the founding group».


**Pregunta.** Una font de l'emissor que diu que la persona és «one of the founding members» o «one of the co-founding executives» la fa fundadora (D37)?

**Casos.**

| ISIN | Empresa | Anys | Files | Base ara | Dubte |
|---|---|---|---:|---|---|
| DE000A0LD2U1 | alstria office REIT | 2019-2021 | 3 | 1 (Elamine) | lot10 |
| GB00B2987V85 | Rightmove | 2016 | 1 | 1 (McKittrick) | lot16, lot10 |

Fets: Rightmove, AR 2016 (L16-GB00B2987V85-F01 [V]): «Nick is one of the co-founding executives of Rightmove». L'emissor diu que Rightmove.co.uk «was formed in 2000 by the top four corporate estate agencies» (L7-X01). alstria: «one of the founding members of alstria» surt en un perfil d'EQS i en una pàgina antiga d'alstria.com (candidates del traspàs, no al registre). *No registrat:* que l'informe del 2006 digui que Elamine en va ser el primer gerent, pagat per NATIXIS Capital Partners, només consta a `lots/lot16_dubtes.csv`.

**Metodologia.**
- Regla 25, P6: «No compten: «founder-led», «founding CEO», «founding shareholder» […]».
- Regla 25, P4: «“Founding CEO” o “first CEO” volen dir primer CEO, no fundador.»
- D37 (changelog v0.10): «No compten […] les expressions ambigües».
- La P6 no esmenta «founding member» ni «co-founding executive»: per això cal decisió.

**Opcions.** a) No compten (com «founding CEO»). b) Compten com a «cofundador».

**Recomanació: a.** Descriuen el primer equip o el primer càrrec, no qui va fundar l'empresa. Un matís del verificador: que Rightmove la formessin quatre empreses ajuda a llegir l'expressió, però no desfà una D37 (D37c); el motiu és l'ambigüitat de l'expressió.

**Efecte.** 4 files d'1 → ND, que surten de la mostra principal. Passen a 0 només si es documenta la prova e amb la P3: les matrius (Countrywide, Connells, Halifax i Royal and Sun Alliance; el vehicle de Captiva a alstria) i que el CEO no n'és fundador. Si Jordi tria b, es mantenen a 1 per D37 (Rightmove amb L16-F01; alstria cal trobar la frase en una captura d'alstria.com o al perfil d'EQS).

---

### Q3. «CEO fundador» (Cellnex)

> **Decidit (Jordi, 24/11/2026), després de comprovar Cellnex, Ocado, B&M i Metro Bank: l'expressió sola no compta (opció a).** A Cellnex i Metro Bank designa el primer CEO; Ocado i B&M són fundadors per altres cites (D37, regla 27).


**Pregunta.** «Tobias Martinez, CEO fundador de Cellnex» en un comunicat de l'emissor compta com a «fundador» (D37) o com a «founding CEO» (exclòs)?

**Casos.**

| ISIN | Empresa | Anys | Files | Base ara | Dubte |
|---|---|---|---:|---|---|
| ES0105066007 | Cellnex | 2016-2022 | 7 | 1 (D37, decisió C0220 de Doctorat) | lot16 |
| ES0105066023 | Cellnex (2a línia) | 2019 | 1 | 0 (regla b, sense cap part citada) | regla29 |

Cita (D0543 i L6-ES0105066023-X01, comunicat del 28/4/2023): «Tobias Martinez, CEO fundador de Cellnex, dejará su cargo el 3 de junio tras liderar la empresa durante ocho años». Cellnex es va constituir el 2008 (L6-ES0105066007-X01, «incorporated in Barcelona on 25 June 2008») i la nota de la mateixa entrada data el canvi de nom d'Abertis Telecom Terrestre a Cellnex Telecom l'1/4/2015. *No registrat:* que el 2015 es va escindir d'Abertis i va sortir a borsa (només a `lots/lot16_dubtes.csv`) i que Forbes 2023 (B) en digui «fundador» a seques citant el fons Antin.

**Decisió que es reobre.** L'1 actual ve de la decisió C0220 de Doctorat, que la base anota com «ja tancada». El 23/11, Jordi va aprovar aplicar-la al lot de correcció 1 (CO1-028 a CO1-034: «Jordi 23/11/2026: sí a corregir regles amb les decisions de Doctorat»). L'opció a la desfà.

**Metodologia.**
- Regla 25, P6: compten «fundador, cofundador […] i similars»; no compta «founding CEO».
- Regla 25, P4: «El primer CEO d'una escissió no és fundador per defecte […]. És 1 només si una font A de l'empresa l'anomena fundador (D10b, D37) […]. “Founding CEO” o “first CEO” volen dir primer CEO, no fundador.»
- Regla 27, Arkema: «es manté a 1 (cas de referència de la D10b, 14/11/2026)». La cita d'Arkema (L10-FR0010313833-F03) diu: «Président-directeur général d'Arkema depuis sa création en 2006, et en conséquence, « fondateur » d'Arkema».

**Opcions.**
- a) No compta (és la traducció de «founding CEO»): 1 → ND; 0 només amb la prova e i la P3 sobre Abertis documentades.
- b) Compta (D37/D10b, com Arkema): es manté 1, amb `fundador_escissio` i `conflicte_fonts`, i robustesa com a ND (P4).

**Recomanació: a.** «CEO fundador» és, paraula per paraula, «founding CEO», i el context («liderar la empresa durante ocho años») parla del primer CEO. A Arkema l'emissor fa servir el substantiu «fondateur» sol, entre cometes, i en dedueix la condició. **Avís:** el verificador del triatge recomanava b, per coherència amb Arkema i amb la decisió C0220, que Jordi va fer aplicar el 23/11. Per això és la pregunta més oberta del paquet: dir «sí» a la a vol dir desfer aquella aplicació.

**Efecte.**
- Opció a: 8 files a ND (7 d'1 → ND i ES0105066023 2019 de 0 → ND). Les 7 primeres surten de la mostra principal; ES0105066023 2019 ja n'és fora (`dret_temporal`). Passen a 0 si es documenten l'escissió (no registrada), la P3 sobre Abertis (la fitxa d'Abertis ja té la constitució del 1967 [V]) i l'entrada de Martínez el 2000 com a directiu de Tradia (avui només a `lots/lot16_dubtes.csv`, cal registrar-la).
- Opció b: es manten les 7 files a 1 i ES0105066023 2019 passa de 0 a 1 (1 fila).
- En totes dues, les dues línies del 2019 han de tenir el mateix valor.

---

### Q4. «Prior to setting up Energean, Mathios…»

**Pregunta.** Un gerundi amb el subjecte implícit («Prior to setting up Energean, Mathios had…») compta com a «set up» amb la persona com a subjecte?

**Cas.** GB00BG12Y042 Energean, 2023, 1 fila. Base: 1 (Rigas). Dubtes lot10 i lot16. Cita A [V], AR 2023 p. 101 (L16-GB00BG12Y042-F01). Al registre, «founding shareholder» (que la P6 exclou) només surt a la biografia d'un tercer (L10-GB00BG12Y042-F01, Energy Council 2017, [NV] `no_valida`, font C), no a la de l'AR 2023.

**Metodologia.** P6: compten «“founded”, “set up”, “established” o “started” la companyia amb la persona com a subjecte». P1: «La D37 preval.»

**Opcions.** a) Compta (D37). b) No compta.

**Recomanació: a.** En anglès el subjecte del gerundi és el de l'oració principal (Mathios). «Founding shareholder», a la biografia del tercer, no compta, però tampoc no contradiu la cita. Els dos agents hi coincideixen.

**Efecte.** Cap canvi d'etiqueta (1). Marques: D37a, la cita és del 20/03/2024, no contemporània (cal buscar-la a l'AR 2022); `fundacio_no_nova` i `fundador_transformador` només si una cita documenta la compra de Prinos (2007) i la holding del 2017.

---

### Q5. «Leonoff founded Paysafe», dit pel grup successor

**Pregunta.** Una atribució «X founded [nom de la cotitzada]» feta pel grup successor després de la descotització, que per l'any (1997) i pel nom («originally Optimal Payments») remet al negoci que la cotitzada va comprar el 2011, compta com a D37?

**Cas.** GB0034264548 Paysafe, 2016-2017, 2 files. Base: 1 (Leonoff), marca `origen_intern`. Dubte lot9.
- F01 (comunicat del 2019, allotjament successor): «Leonoff founded Paysafe, originally Optimal Payments, in 1997 and has held the position of President and CEO since 2008.»
- X01 (AR 2016, regulador): «In 1997, Joel founded SureFire Commerce Inc., which merged with the Optimal Group in 2003 to form Optimal Payments, now known as Paysafe Group plc.»
- D01: «In 2011, Neovia acquired substantially all of the assets of 7012985 Canada Inc. and changed its name to Optimal Payments plc».

**Metodologia.** Regla 24: la D37 preval «sobre les proves a-e de la regla 21, l'FT, D1, D10 i qualsevol “joined”, també davant de dades factuals contràries (D37c)». D37d: «l'“empresa de procedència” ha de ser una predecessora legal o econòmica documentada». Precedent B&M (regla 27): 1 per D37 amb `fundador_transformador`=1.

**Opcions.** a) Compta (D37): 1 amb `fundador_transformador`=1 i `founderceo_rob_cita_contemporania`=0. b) No compta (D37d, com Drillisch): ND.

**Recomanació: a.** La cita anomena «Paysafe», no una altra entitat, i ve del grup que inclou l'antiga plc. La diferència amb Q1 és aquesta: aquí la cita anomena la cotitzada; a Q1 anomena una altra entitat. Els dos agents hi coincideixen.

**Efecte.** Cap canvi d'etiqueta (2 files a 1), sempre que Q5b també sigui «sí». Marques: `fundador_transformador`=1 (va entrar a la cotitzada el 2011) i `founderceo_rob_cita_contemporania`=0 als dos anys. Amb l'opció b, 2 files d'1 → ND.

### Q5b. Cita de l'emissor publicada pel grup successor després de la descotització

**Pregunta.** Una cita de fundador que publica el grup successor (la mateixa societat o el grup que la inclou) després que la cotitzada deixi de cotitzar compta com a font de l'emissor per a la D37?

**Casos.**

| ISIN | Empresa | Anys | Files | Base ara | Grup del triatge |
|---|---|---|---:|---|---|
| GB0034264548 | Paysafe | 2016-2017 | 2 | 1 (Leonoff) | `criteri_jordi` (lot9), el de Q5 |
| GB00BDZT6P94 | Merlin | 2016-2019 | 4 | 1 (Varney), certificades | `cal_cerca` (lot10 i lot16) |

Fets:
- Paysafe: F01 és un comunicat del 2019, amb `allotjament=successor`.
- Merlin: no hi ha cap entrada de fundador al registre (F01 només documenta l'MBO). La candidata C0306 (`traspas/candidates_evidencia.csv`) és un article de backstage.merlinentertainments.biz del 18/06/2023, posterior a la descotització: «Merlin’s family of 30,000 staff around the world feel proud that their founder has been recognised for his amazing achievement»; el mateix article identifica «Sir Nick Varney, our former Chief Executive». Segons el verificador del triatge, l'allotjament seria `successor` (Merlin Entertainments Ltd, l'antiga plc), i «their founder» ho diu la plantilla. Captura de Wayback 20240713022455.

**Metodologia.** Regla 24: la D37 val amb una cita «en una font primària de l'emissor (cotitzada, grup o predecessora legal o econòmica documentada, D37d)»; no esmenta el successor. CLAUDE.md, criteri a del PR #3: «un document de l'emissor allotjat fora del seu domini (CDN, regulador, plataforma de comunicats) és font A si la cita és literal: compta qui l'ha escrit, no on està allotjat». CLAUDE.md §6 ja preveu `allotjament=successor`. Segons el verificador de Paysafe, la nota (4) del lot 2 ho va deixar sense decidir.

**Opcions.**
- a) Compta, si el document identifica la persona i el successor és la mateixa societat o el grup que la inclou; `founderceo_rob_cita_contemporania`=0 si no hi ha cap cita anterior.
- b) No compta: cal una cita publicada per l'emissor mentre cotitzava.

**Recomanació: a.** Compta qui ha escrit el document (criteri a del PR #3), el registre ja preveu `allotjament=successor` i la robustesa D37a recull que la cita és posterior.

**Efecte.** Paysafe: amb a, cap canvi (depèn també de Q5); amb b, 2 files d'1 → ND. Merlin: amb a, quan es registri i es verifiqui C0306, l'1 es manté per D37 (4 files), amb `fundador_transformador` i `fundacio_no_nova` si es documenten, i `founderceo_rob_cita_contemporania`=0 si no es troba cap cita als informes 2013-2019 ni al fullet de l'OPV del 2013. Amb b, Merlin depèn de la resta de la cerca (font B de PA amb `si_font_B`, o prova d sobre Vardon) i pot quedar a 1, a 0 o a ND.

---

### Q6. «Cofundador» només en font B davant d'un fet A que no tanca cap prova

**Pregunta.** Si només la premsa (B) diu que el CEO és cofundador, i l'emissor (A) diu que «joined» dos anys després de la fundació, però això no completa cap prova de no fundador, la fila és 1 per la P6 (`si_font_B`) o ND?

**Cas.** GB00B71N6K86 Evraz, 2018-2020, 3 files. Base: 1 (Frolov), sense marca. Dubte lot9.
- Kommersant (B, L9-D01 [V]): «…два других ее основателя — Александр Абрамов (24,29%) и Александр Фролов (12,15%)…».
- Emissor: «Evraz was founded in 1992 as limited liability company EvroazMetall» (L9-X01) i «Mr. Frolov joined the Original Group in 1994» (L9-X02).
- AR 2021, perfil d'Abramov: «He founded EvrazMetall in 1992.» (L7-GB00B71N6K86-X01 [V], en singular). Però la nota de L9-X01 diu que el fullet del 2011 atribueix la fundació a un grup de científics i enginyers encapçalat per Abramov, sense una llista exhaustiva.
- Altres fonts B: «co-founder of Evraz, Alexander Frolov» (L11-GB00B71N6K86-F01) i «Evraz CEO and co-founder Alexander Frolov» (Interfax, L2|GB00B71N6K86|C7).
- La prova d no tanca (2 anys, en calen 3). La P8 no s'aplica: hi ha fonts B que anomenen cofundadors, i la frase en singular d'X01 no és una llista tancada davant la nota de L9-X01.

**Metodologia.** P6: «Un “sí” de font B sense D37 compta com a 1 si cap font A/B no el contradiu […]; marca `si_font_B` i robustesa com a ND. Si el contradiu una prova de no basada en fonts A, preval la prova A (`conflicte_fonts`).» CLAUDE.md §4: «Si no hi ha proves que sigui fundador, és indeterminat, no 0».

**Opcions.** a) 1 amb `si_font_B` (el fet A no és una «prova de no»). b) ND (el fet A xoca amb la font B).

**Recomanació: a,** amb una condició. La P6 només fa prevaler la font A quan és una «prova de no», i aquí no n'hi ha cap de completa (decisió del 24/11). El conflicte s'anota a les notes. **Condició (reserva del verificador):** la P6 exigeix que el «sí» de font B «es refereixi a la cotitzada o a una predecessora D1/D10», i per la P1 compta el negoci operatiu. «Co-founder of Evraz Group» pot voler dir la holding Evraz Group SA. Cal documentar que la font B parla del negoci operatiu (EvrazMetall, 1992) o d'una predecessora de la cotitzada; si només parla de la holding, la cita no compta i la fila queda ND. Abans, una cerca curta de D37 a l'emissor (biografies 2018-2020, RNS del 2021, fullet de l'IPO del 2005).

**Efecte.** Cap canvi d'etiqueta (3 files a 1). S'afegeix `si_font_B` i la robustesa com a ND. Cal registrar Kommersant com a entrada de fundador. Amb l'opció b, 3 files d'1 → ND.

---

### Q7. Comprador que transforma una empresa existent (FT o no)

**Pregunta.** Florentino Pérez va passar el 1983 a ser «máximo ejecutivo» i un dels principals accionistes de Construcciones Padrós, que ja existia, i en va fer ACS amb fusions. És fundador transformador (FT de tipus c, com Arnault a LVMH) o un 0 per la prova d?

**Cas.** ES0167050915 ACS, 2016 i 2021, 2 files. Base: 0 (prova d, sense cap part citada). Dubte regla29. Cita (L6-ES0167050915-X02, IAGC 2021): «En 1983 regresa a la iniciativa privada y desde ese año pasó a ser el máximo ejecutivo de Construcciones Padrós, S.A., siendo, además, uno de sus principales accionistas.»

**Metodologia.** Secció 2.3, punt 6 (resolt P5): «Els fundadors transformadors que compleixen el criteri del PROTOCOL són 1 a l'anàlisi principal i 0 a la robustesa `founderceo_rob_sense_ft`». Ampliació de la regla 27 (v0.10.10): «LVMH 2016-2025: l'1 ve d'un FT validat de tipus c (decisió de Jordi X9-3, 15/11/2026), no de D37 ni de D1». El criteri del PROTOCOL no és al repositori, i CLAUDE.md diu que la metodologia vigent «és només la del repositori». Cada FT s'ha validat per decisió de Jordi.

**Opcions.** a) Buscar primer una D37; si no n'hi ha, Jordi decideix si és FT, cas per cas com a LVMH (Claude no pot aplicar el test FT perquè el criteri no és al repositori; Jordi pot donar-ne el text perquè s'hi incorpori); si no ho és, 0 per la d contra Padrós. b) 0 directament per la d (comprador = no fundador).

**Recomanació: a.** És el mateix camí que LVMH, i deixa la decisió FT a qui l'ha presa fins ara. X02 no diu que comprés Padrós, i cal citar-ho abans de decidir.

**Efecte.** Avui cap. Si Jordi el considera FT: 2 files de 0 → 1 (amb `ft`, `tipus_ft`=c i robustesa sense FT = 0). Per al 0 per la d falten l'any de fundació de Padrós i l'ocupador anterior al 1983. Per al 2021 cal citar la sortida de Marcelino Fernández Verdes i el retorn de Pérez com a consejero delegado abans del 31/10/2021.

---

## B. Preguntes sobre qui és el CEO

### Q8. Dues persones amb el títol de consejero delegado (Ferrovial)

> **Decidit (Jordi, 24/11/2026): co-CEO per R1 (opció a).**


**Pregunta.** Si l'informe de govern del mateix exercici dona el càrrec de consejero delegado al president («Presidente y Consejero Delegado») i a un altre conseller, compten tots dos com a co-CEO per R1?

**Casos.**

| ISIN | Empresa | Anys | Files | Base ara | Dubte |
|---|---|---|---:|---|---|
| ES0118900010 | Ferrovial | 2016-2018 | 3 | Meirás sol, regla b | regla29 |
| ES0118900010 | Ferrovial | 2019-2022 | 4 | Madridejos sol, regla b, `nota_del_pino_president_exec` | regla29 |
| ES0618900981 | Ferrovial (drets) | 2016 | 1 | Meirás sol | regla29 |
| ES06189009A2 | Ferrovial (drets) | 2017 | 1 | Meirás sol | regla29 |

Cites: «DON ÍÑIGO MEIRÁS AMUSCO Consejero Delegado» (L6-ES0118900010-C01); «DON RAFAEL DEL PINO Y CALVO-SOTELO Presidente y Consejero Delegado» (X01, IAGC 2016); el 20-F del successor: «Rafael del Pino has served as our Chief Executive Officer since 1992 (co-Chief Executive Officer with Mr. Ignacio Madridejos since September 2019) until the Merger» (X12).

**Metodologia.**
- Secció 2.1, R1: «el títol de CEO o el càrrec legal equivalent […] identifica el CEO». P5: equivalent legal, entre d'altres, «consejero delegado».
- Secció 2.1, R3: «Un president executiu només compta per R3 i porta la marca `ceo_president_exec`.» P5: «el president executiu només si el càrrec de CEO és vacant».
- Secció 2.3, punt 9 (co-CEO). La regla no diu qui és co-CEO.

**Opcions.** a) Co-CEO per R1 (tots dos tenen el càrrec legal). b) Només el consejero delegado; el president és president executiu (R3, no compta perquè el càrrec no és vacant).

**Recomanació: a.** És la lectura literal de R1 i P5: del Pino té el càrrec legal de consejero delegado, no només el de president. El 20-F del successor (X12) hi és coherent per al 2019-2022, però no és un document del mateix exercici i, segons el verificador, descriu l'estructura amb poca precisió (passa per alt Meirás, 2009-2019). Dos dels quatre analistes (ES0618900981 i ES06189009A2) preferien b; el verificador, a, en tots quatre grups. Les files ES0618900981 i ES06189009A2 són drets de subscripció (`no_us_article`=1), i la decisió hi té poc efecte.

**Efecte.**
- `ceos` canvia a 9 files: s'hi afegeix Rafael del Pino y Calvo-Sotelo (`n_ceos` 1 → 2, marca `co_ceo`; a 2019-2022 substitueix `nota_del_pino_president_exec`).
- FounderCEO es manté a 0 per la prova a (F01: «En 1952, Rafael del Pino funda Ferrovial», en singular, P8). **Condició:** cal registrar la cita literal de l'annex III que identifica el fundador com a Rafael del Pino y Moreno, perquè el fill porta el mateix nom. La columna `regles` passa de b a a (9 files).
- Fora del recompte (no són grups `criteri_jordi`): cal **comprovar**, no aplicar directament, NL0015001FS8 2023-2025 (3 files, mateixa marca `nota_del_pino_president_exec`), perquè X12 diu que del Pino va ser co-CEO «until the Merger»; i cal comprovar si a ACS 2017-2020 (4 files, grup de cerca) Florentino Pérez tenia també el càrrec de consejero delegado. Si n'hi ha, el criteri de Q8 s'hi aplicaria i `ceos` podria canviar a fins a 7 files més.

### Q8b. EssilorLuxottica 2020 (antic punt 7)

**Pregunta.** El 31/10/2020, amb Del Vecchio com a Président-Directeur Général i Sagnières com a Vice-Président-Directeur Général Délégué, hi ha un CEO o dos?

**Cas.** FR0000121667 2020, 1 fila. No és cap grup del triatge. Base: Del Vecchio sol (`n_ceos`=1), però amb la marca `co_ceo`, igual que el 2018 i el 2019.

**Fets.** Els títols i la precisió «amb poders iguals» surten del paquet del 23/11 (punt 7). Al registre no hi ha cap cita amb el títol de Sagnières del 2020. Per tant, cal registrar-la abans d'aplicar res.

**Metodologia.** P5: R1 és el «títol de CEO o equivalent legal: […] PDG, directeur général […] o similars». El directeur général délégué no hi és.

**Opcions.** a) Un sol CEO per R1 (Del Vecchio, PDG). b) Co-CEO, pels poders iguals.

**Recomanació: a,** la del 23/11: el títol de CEO (PDG) és només de Del Vecchio. Respondre «sí» a Q8 no decideix aquest cas: a Ferrovial tots dos tenen el càrrec legal de consejero delegado, i aquí Sagnières té un càrrec de «délégué».

**Efecte.** Amb a, cap canvi de CEO ni d'etiqueta; la marca `co_ceo` de 2018-2020 no quadra amb `n_ceos`=1 i s'ha de treure o justificar (com a Luxottica, Q10). Amb b, `ceos` canvia a 1 fila (s'hi afegeix Sagnières). En totes dues, l'etiqueta depèn de Q1 i de la cerca de l'operació del 2018.

---

### Q9. President executiu amb el títol de CEO al document de l'emissor

> **Decidit per a Telefónica (Jordi, 24/11/2026): només el president, per R1 (opció a).** La Q9b continua oberta.


**Pregunta.** Quan el document de l'exercici dona el títol de CEO al president executiu, és el CEO per R1, encara que hi hagi un consejero delegado? I si no té el títol, què passa? (Quan el títol només surt a la traducció anglesa, vegeu Q9b.)

**Casos.**

| ISIN | Empresa | Anys | Files | Base ara | Dubte |
|---|---|---|---:|---|---|
| ES0178430E18 | Telefónica | 2017-2024 | 8 | Álvarez-Pallete, regla b | regla29 |
| ES0178430E18 | Telefónica | 2025 | 1 | Murtra, regla b | regla29 |
| ES0124244E34 | Mapfre | 2025 | 1 | Huertas, regla b | lot17 |

Cites:
- Telefónica 2017-2018: «Mr. José María Álvarez-Pallete López – Executive Chairman (Chief Executive Officer)» (C02 i C03, IAGC). 2019-2023: «Chief Executive Officer - Mr. José María Álvarez-Pallete López» (C04-C08, apartat «Allocation of positions and duties»). 2024: «José María Álvarez-Pallete Chairman & CEO — Telefónica S.A.» (C09, fragment de resultats del 3T). Totes són de la versió anglesa. Vilá, de la versió castellana: «Nombrar a D. Ángel Vilá Boix Consejero Delegado (Chief Operating Officer -C.O.O.-) y Vocal de la Comisión Delegada de Telefónica, S.A.» (X02).
- Telefónica 2025: «Marc Murtra Chairman & CEO of Telefónica, S.A.» (C10, p. 5). Segons el triatge, la p. 232 del mateix document nomena Emilio Gayo «Chief Executive Officer» el 06/03/2025; no hi ha cap entrada al registre amb aquesta cita, i l'IAGC 2025 (X03) és [NV].
- Mapfre 2025: «La presidencia del Consejo de Administración corresponde a D. Antonio Huertas Mejías, quien tiene la condición de máximo responsable ejecutivo y de presidente de la Sociedad» (C01, original castellà, sense títol de CEO ni de consejero delegado).

**Metodologia.** Secció 2.1, R1: «el títol de CEO o el càrrec legal equivalent […] identifica el CEO». P5: R1 inclou com a equivalents legals el «consejero delegado» i el «PDG» (president i director general). Secció 2.1, R3 i regla 22: «Un president executiu només compta per R3 i porta la marca `ceo_president_exec`.» P5: «el president executiu només si el càrrec de CEO és vacant, criteri 4 del PR #3».

**Opcions.**
- a) Mana el títol: qui té el títol de CEO al document de l'exercici és el CEO per R1, amb `ceo_president_exec` si també és president. Sense títol de CEO ni de consejero delegado, el president només compta per R3 i amb el càrrec vacant.
- b) Mana el càrrec legal: el president executiu sempre és R3. Si hi ha un consejero delegado (Vilá el 2017-2024), el CEO és ell.
- c) Co-CEO quan el president té el títol de CEO i hi ha un consejero delegado (la P5 també fa del consejero delegado un equivalent legal).

**Recomanació: a.** El criteri és el títol: R1 parla del «títol de CEO», i la P5 admet com a equivalent legal el PDG, és a dir, un president que també té el càrrec de primer executiu. L'emissor mateix tradueix el càrrec de Vilá per COO. És coherent amb C1 per la mateixa raó: a BME, Zoido no tenia el títol de CEO, encara que X04 l'anomeni «primer ejecutivo», i Hernani era consejero delegado. I és coherent amb Q8, on tots dos tenen el càrrec legal. Amb la marca `ceo_president_exec` a totes les files, la robustesa sense presidents executius els recull. **Matís:** amb el criteri del títol, Vilá també té un títol equivalent (consejero delegado), i per això l'opció c és una alternativa coherent amb Q8; la recomanació a es basa que l'emissor el qualifica de COO.

**Efecte.**
- Opció a: `ceos` no canvia el 2017-2024. S'afegeix `ceo_president_exec` a Telefónica 2017-2025 i Mapfre 2025 (10 files), i per coherència a Mapfre 2016, 2017 i 2019 i a Inditex 2017-2018 (vegeu Q9b). Mapfre 2025 passa a R3: abans cal una cita de l'IAGC 2025 (C.1.3 o C.1.10) que mostri que no hi havia consejero delegado.
- **Telefónica 2025, cas obert:** amb el criteri del títol, Murtra (C10) i Gayo (p. 232, no registrat) tindrien tots dos el títol de CEO. Si es confirma i l'emissor no distingeix funcions, s'aplica la regla de co-CEO i `ceos` canvia a 1 fila (s'hi afegeix Gayo). Que la secció 4.4 qualifiqui Gayo de COO no és al registre: cal recuperar l'IAGC 2025 (X03, pendent d'arxiu) i registrar la p. 232.
- Opció b: `ceos` canvia a 8 files de Telefónica (Vilá el 2017-2024) i a la del 2025 (Gayo), 9 en total.
- Opció c: `ceos` canvia a 8 files de Telefónica (s'hi afegeix Vilá com a co-CEO; `n_ceos` 1 → 2).
- FounderCEO = 0 en totes les opcions (Álvarez-Pallete: prova b completa, 1963 i 1924; Vilá i Gayo: prova c amb la fundació del 1924, X01; per a Gayo cal registrar la cita del nomenament).

### Q9b. Títol de CEO que només surt a la traducció anglesa de l'emissor

**Pregunta.** Si la traducció anglesa de l'emissor diu «Chairman and CEO» i l'original castellà només diu «Presidente», val el títol de la traducció per a R1?

**Casos.**
- Mapfre (ES0124244E34) 2016, 2017 i 2019: avui R1 amb C02, C04 i C05 («… MR. ANTONIO HUERTAS MEJÍAS CHAIRMAN AND CEO»). La nota de L17-ES0124244E34-C02 diu: «Spanish original (...) says only 'PRESIDENTE'». C04 i C05 són també «English issuer translation». Mapfre 2025 (Q9) és de l'original castellà i no té títol de CEO. No són grups del triatge, llevat del 2025.
- Inditex (ES0148396007) 2017-2018, grup tancable: L17-C01 («Chairman and CEO of Inditex since 2011», ACGR FY2018) i L17-C02 (C.1.10, poders delegats al «chief executive officer(s)»), de la versió anglesa. El tancament proposat pels dos agents les passa de R1 a R3 amb `ceo_president_exec`; la vacant la dona L6-X08 (Cinco Días, B): «no tenía CEO desde 2011».
- Telefónica 2017-2024 (Q9): les cites de CEO d'Álvarez-Pallete són de la versió anglesa. El verificador del triatge demanava veure quin títol li dona l'IAGC original en castellà abans de decidir.

**Posicions del triatge.** El verificador de Mapfre recomana R3 amb `ceo_president_exec` a tots els anys de Huertas (2016-2019 i 2025), perquè el càrrec legal original no és equivalent a CEO; altrament, el mateix càrrec queda codificat diferent segons la llengua (R1 el 2016, el 2017 i el 2019; R3 el 2025). El tancament d'Inditex va en el mateix sentit. A favor de la traducció: és un document de l'emissor, i la P5 admet el PDG com a equivalent legal.

**Opcions.**
- a) Val la traducció: R1 amb `ceo_president_exec`.
- b) Mana el càrrec de l'original: R3 amb `ceo_president_exec`, només si el càrrec de CEO és vacant; si l'original dona el càrrec de consejero delegado a una altra persona, aquesta és el CEO per R1.

**Recomanació: b.** El mateix càrrec ha de quedar codificat igual sigui quina sigui la llengua del document, R1 parla del «càrrec legal equivalent» (que és el de l'original), i és el que recomana el verificador de Mapfre i el que ja fa el tancament d'Inditex. **Atenció: va en sentit contrari de l'opció a de Q9 si l'original de Telefónica no dona a Álvarez-Pallete el títol de CEO.** Per això, abans d'aplicar Q9 a Telefónica, cal llegir l'IAGC original en castellà.

**Efecte.**
- Opció b: `ceos` no canvia a Mapfre ni a Inditex (no hi havia consejero delegado; a Mapfre cal citar-ho). Mapfre 2016, 2017, 2019 i 2025 i Inditex 2017-2018 passen a R3 amb `ceo_president_exec` (6 files), i entren a les robusteses sense R3 i sense presidents executius. Telefónica 2017-2024: si l'original castellà només diu «Presidente Ejecutivo», el CEO passa a ser Vilá per R1 i `ceos` canvia a 8 files; si l'original també li dona el títol de CEO o de consejero delegado, s'aplica Q9.
- Opció a: Mapfre 2016, 2017 i 2019 es mantenen per R1 i el tancament d'Inditex s'ha de corregir (C01 i C02 es mantenen a R1, amb `ceo_president_exec`).
- FounderCEO no canvia en cap opció.

---

### Q10. Dos CEO amb una plaça vacant que assumeix el president fundador (Luxottica)

**Pregunta.** En un model de dos CEO, si una plaça queda vacant i en fa les funcions el president executiu fundador, sense el títol, compta com a co-CEO?

**Cas.** IT0001479374 Luxottica, 2016-2017, 2 files. Base: 0, Vian sol, però amb la marca `co_ceo`. Dubte regla29.
- «Mr. Massimo Vian continued in his role as CEO for Product and Operations.» (C01)
- «The Chairman Leonardo Del Vecchio, founder and inspirer of the Group culture and strategic vision, will assume the executive responsibilities for Markets» (X04).
- Del Vecchio signa com a «principal executive officer» al 20-F del 2016 (X01, X02), al costat de Vian (X03); el 2017 l'F-6 només en designa Vian (X07).
- **Prova en contra de la recomanació:** carta a la SEC (L7-IT0001479374-X05 [V], anys 2016-2017): «the Company’s Executive Chairman was determined to be the sole CODM because he has the principal authority to make strategic decisions». És la prova més forta que Del Vecchio era el primer executiu.

**Metodologia.** P5 i secció 2.1, R3 (president executiu només amb el càrrec vacant). Regla 27, Richemont 2017: «NA per R-SC a l'anàlisi principal; Rupert=1 només a la robustesa R3».

**Opcions.** a) Vian sol per R1 (0). b) Co-CEO Vian i Del Vecchio (1).

**Recomanació: a.** Hi ha un CEO amb títol, i per tant el càrrec de CEO no és vacant. X05 diu qui tenia l'autoritat estratègica, però no li dona el títol de CEO; la P5 aplica R1 abans que R3. Del Vecchio entra a la robustesa R3, com Rupert a Richemont. Els dos agents hi coincideixen. El verificador avisa que els precedents no són uniformes (Galenica 2016 va quedar NA; Micro Focus 2016, co-CEO per R1).

**Efecte.** Cap canvi d'etiqueta ni de CEO (2 files a 0). `founderceo_rob_r3_president_exec_com_1` passa a 1 als dos anys, i es treu la marca `co_ceo`, que no quadra amb un sol CEO. Amb l'opció b, 2 files de 0 → 1.

---

### Q11. Gérant d'una SCA (Rubis)

> **Decidit (Jordi, 24/11/2026): el Gérant és CEO per R1 (opció a).**


**Pregunta.** El Gérant d'una societat en commandite per accions és CEO per R1? I la persona que ho és com a representant d'un Gérant societat (Riou per Agena, Clarisse Gobin-Swiecznik per Sorgema)?

**Casos.**

| ISIN | Empresa | Anys | Files | Base ara | Dubte |
|---|---|---|---:|---|---|
| FR0000121253 | Rubis | 2016 | 1 | 1; Gobin i Riou; marques `co_ceo;de_facto` | lot12 |
| FR0013269123 | Rubis | 2017-2025 | 9 | 1; 2 CEO (2017-2022), 3 (2023-2024), 5 (2025); `co_ceo;de_facto` | lot12 |

Cites: «Gilles Gobin et Jacques Riou Associés-Gérants» (L12-FR0000121253-C02, 2016); «Sont Gérants de Rubis : Monsieur Gilles Gobin – Sorgema – GR Partenaires – Agena.» (L12-FR0013269123-C04, 2017); «M. Gilles Gobin et, depuis le 1er juillet 2023, Mme Clarisse Gobin-Swiecznik sont les représentants légaux de Sorgema.» (C15); 2025: «Jean-Christian Bergeron et Marc Jacquot sont Gérants non statutaires» (C08).

**Metodologia.** P5: R1 = «títol de CEO o equivalent legal: […] PDG, directeur général, […] o similars». No esmenta el Gérant d'una SCA ni els representants legals.

**Opcions.**
- a) R1 per als Gérants persona física; un representant d'un Gérant societat compta només si l'emissor l'anomena literalment Gérant.
- b) R1 per a tots, també els representants.
- c) R3 (com ara), amb `de_facto`.

**Recomanació: a.** El Gérant és l'òrgan de direcció legal d'una SCA, com a Hermès o Michelin. Per als representants, la regla a evita afegir persones sense títol i és coherent amb Hermès, on la base només té Axel Dumas.

**Efecte.**
- FounderCEO = 1 no canvia (10 files): Gobin és Gérant a títol personal i fundador tots els anys (regla 9).
- Marques: `marca_prova` de R3 a R1 al registre i fora `de_facto` (10 files). `founderceo_rob_sense_r3` ja val 1.
- `ceos`, Riou: el 2016 l'emissor l'anomena «Associés-Gérants» amb Gobin (C02), i els anys 2017-2020 ja tenen cites registrades on figura com a Gérant (C05, C03, C01, C06 i C07). Del 2021 al 2025, en canvi, el registre només l'anomena «représentant légal d'Agena» (C12, C14, C17, C20 i C10); per al 2021 hi ha un indici («Managing Partners», nota de L10-FR0013269123-F08). Amb l'opció a, Riou sortiria de `ceos` el 2021-2025 (fins a 5 files) si no es troben cites que l'anomenin Gérant.
- `ceos`, Clarisse Gobin-Swiecznik: només surt com a representant de Sorgema. Amb l'opció a sortiria de `ceos` el 2023-2025 (fins a 3 files), llevat que es trobi una cita que l'anomeni Gérante.
- En total, amb l'opció a, `ceos` pot canviar a fins a 8 files (2021-2025). FounderCEO no canvia, perquè Gobin és Gérant a títol personal i fundador tots els anys.

---

### Q12. Vehicles gestionats externament (Tritax, Primary Health)

**Pregunta.** En una societat gestionada per un gestor extern, qui és el CEO: el soci del gestor que l'emissor anomena CEO de la cotitzada (R1), el directiu de l'assessor que porta el dia a dia (R3) o ningú (R-SC)?

**Casos.**

| ISIN | Empresa | Anys | Files | Base ara | Dubte |
|---|---|---|---:|---|---|
| GB00BG49KP99 | Tritax Big Box REIT | 2021-2025 | 5 | 1 (Godfrey) | lot12 |
| GB00BYRJ5J14 | Primary Health Properties | 2020 | 1 | 1 (Hyman, `de_facto`, `r3_managing_director`) | lot12 |

Cites:
- Tritax: «Colin Godfrey as CEO for Tritax Big Box REIT plc» (C03, 2022; C04, C05 i C01 semblants fins al 2025). El 2021 només hi ha «Chief Executive Officer» a la Q&A del gestor i «CEO – Fund Management» (C02).
- PHP 2020: «Harry Hyman was accountable to the Board, in his capacity as the Managing Director of the Adviser, for the day-to-day management of the Group» (C03, AR 2020 p. 64). La nota de C03 recull també la p. 63: «Managing Director Harry Hyman - Manages the day-to-day running of the business through the Advis[er]». Nomenat CEO el 5/1/2021 (C01; és posterior al 31/10/2020 i no serveix d'interval).

**Metodologia.** Regla 22: «Primer s'apliquen R1, R2 i R3. […] BB Biotech i Tritax s'anoten com a vehicles d'inversió gestionats externament, per a la robustesa sense financeres.» P5: «R-SC (NA) només després d'una cerca exhaustiva i documentada». Secció 2.1, R3: «un CEO de facto amb el càrrec vacant compta si la font atribueix de manera literal l'exercici de primer executiu».

**Opcions.**
- a) Mana el que diu l'informe de l'emissor de cada any, en l'ordre de la P5: títol de CEO de la cotitzada (o equivalent, com un Managing Director del consell de la cotitzada) → R1; gestió diària atribuïda literalment a una persona, sense CEO → R3; l'emissor declara que no té direcció pròpia → R-SC (NA).
- b) R-SC a tots els vehicles gestionats externament, per coherència (recomanació del 23/11).

**Recomanació: a.** Segueix l'ordre de la P5 (R1, R3 i només després R-SC) i fa servir el que diu l'emissor. Canvia la recomanació del 23/11, que era b. Afegir una marca de gestió externa i una robustesa amb aquestes files com a NA (columna nova; cal l'OK de Jordi).

**Efecte.**
- Opció a: Tritax 2022-2025 es manté amb Godfrey per R1 (4 files); el seu 1 depèn, a més, d'una cerca del lot 10 (comprovar que «Co-Founder» de L11-F01 va amb la plc i no amb la gestora). Tritax 2021: la cita és feble; si no se'n troba una de més clara, passa a R3 o a R-SC (1 fila, 1 → NA en el pitjor cas, i sortiria de la mostra principal). Tritax 2018-2020 continua NA mentre es busquen les cites d'R-SC (cerca).
- PHP 2020 (1 fila): amb a, hi ha tres sortides possibles, i cap no canvia l'etiqueta llevat de l'última. **R1** si «Managing Director» (p. 63) era un càrrec del consell de PHP i no només de l'assessor (cal comprovar-ho al document); **R3** si només és el directiu de l'assessor amb la gestió diària atribuïda (es manté a 1, amb `de_facto` i `r3_managing_director`); **R-SC** si cap de les dues no es pot citar (1 → NA). El verificador recomana R3 i demana decidir-ho juntament amb Tritax 2021-2025.
- Opció b: Tritax 2021-2025 i PHP 2020 passen d'1 a NA (6 files) i surten de la mostra principal.

### Q12b. Font A de l'emissor contra font B sobre qui és el CEO (BB Biotech)

**Pregunta.** Si l'emissor (A) declara que no té direcció pròpia i la premsa (B) anomena CEO el cap de l'equip del gestor, qui preval?

**Casos.**

| ISIN | Empresa | Anys | Files | Base ara | Dubte |
|---|---|---|---:|---|---|
| CH0038389992 | BB Biotech | 2016 | 1 | NA (R-SC), certificada | lot10 |
| CH0038389992 | BB Biotech | 2017-2019 | 3 | NA (R-SC), no certificada | lot10 |

Cites:
- Font A, AR 2016: «does not have a management of its own within the meaning of article 716b CO» (BBB16-1); «The members of the Board of Directors have no executive functions» (BBB16-2). Per al 2017-2019 hi ha les cites equivalents de cada exercici (BBB17-3, BBB18-3 i BBB19-3). Les del 2016 estan registrades amb anys=2017 (el lot 3 les va fer servir com a extrem de l'interval del 2017): cal registrar-les també per al 2016.
- Font B: «Daniel Koller, CEO BB Biotech» (moneycab, R2-1, 14/02/2017) i «Seit 2010 ist er Leiter der börsenkotierten Beteiligungsgesellschaft» (R2-24); R2-4 (metadades d'un article de l'11/10/2018 amb «CEO BB Biotech»); R2-7 («Leiter des Management Teams»).

**Metodologia.** **Cap regla aprovada no diu quina font preval, A o B, sobre la identitat del CEO**: la P6 i la P7 només regulen el fundador i la data de fundació. CLAUDE.md, decisions del 23/11, criteri c del PR #3: «una cita de CEO només de font B és vàlida (D4b), i s'anota». Criteri d: la llista de mitjans de nivell B la proposa Claude i la valida Doctorat; encara no està validada, i no se sap si moneycab i payoff són B o C. Regla 28: interval amb el nomenament (o l'inici) abans del 31/10/t i un document que anomeni la persona CEO en una data igual o posterior. Regla 22: BB Biotech s'anota com a vehicle gestionat externament, per a la robustesa sense financeres.

**Opcions.**
- a) Preval la font A de l'emissor: NA (R-SC). **És un criteri nou**: no el diu cap regla aprovada.
- b) Koller CEO per R1 amb font B (criteri c del PR #3): el 2017-2019 amb les cites B de cada any; el 2016 per la regla 28 (inici el 2010, R2-24, i R2-1 del 14/02/2017 com a extrem final). El lot 3 ja va calcular aquesta alternativa: FounderCEO=0 per la prova d. Cal, abans, que Doctorat validi moneycab i payoff com a font B.
- c) NA provisional fins que es validi la llista de mitjans B, i després decidir entre a i b.

**Recomanació: a,** perquè és la recomanació dels dos verificadors del triatge i segueix l'ordre de fonts de CLAUDE.md §4 (primer l'emissor). Però com que és un criteri nou, només s'aplica si Jordi l'aprova expressament; si no, l'opció que segueix les regles vigents és b (o c mentre la llista B no estigui validada).

**Efecte.** Opció a: cap canvi (4 files a NA, fora de la mostra principal); cal registrar les cites de l'AR 2016 amb anys=2016. Opció b: 4 files de NA → 0, que entren a la mostra principal, i `ceos` passa a Daniel Koller a 4 files. Opció c: cap canvi ara.

---

### Q13. CEO titular impedit o de baixa

**Pregunta.** Si el CEO titular conserva el càrrec però està impedit uns dies (detingut) o de baixa, i l'emissor nomena un CEO en funcions o reparteix les funcions, qui és el CEO a 31/10: el titular (R1) o l'interí (R2/R2b)?

**Casos.**

| ISIN | Empresa | Any | Files | Base ara | Dubte |
|---|---|---|---:|---|---|
| SE0000103699 | Hexagon | 2016 | 1 | Rollén, 0 (prova d) | regla29 |
| DE000UNSE018 | Uniper | 2018 | 1 | Schäfer, 0 (prova e) | regla29 |

Cites: Hexagon (comunicat del 31/10/2016, C05): «During the time period that Ola Rollén is detained, Hexagon's CFO and Executive Vice President Robert Belkic will be acting CEO for Hexagon.» Uniper (AR 2018): «Klaus Schäfer, the Chairman of the Management Board and Chief Executive Officer (“CEO”)» (C03) i «Mr. Schäfer's duties were temporarily assigned to the other members of the Management Board by the Executive Committee of the Supervisory Board» (X02).

**Metodologia.** Secció 2.1, R2: «un interí compta com a CEO». Taula «CEO interí» (secció 3.2): a l'especificació principal, Interim=1; com a robustesa, assignar-li el CEO definitiu «si l'interinatge dura menys de 6 mesos». D35/R2b: «direcció interina col·legiada sense CEO». Cap regla no tracta un titular impedit sense vacant.

**Opcions.** a) El titular per R1; l'interí s'anota a les notes. b) L'interí per R2 (Hexagon) o R2b (Uniper).

**Recomanació: a.** El càrrec no era vacant i la P5 aplica R1 abans que R2. La taula de l'interí està pensada per a vacants. Robustesa amb l'interí a Hexagon.

**Efecte.** Cap canvi de CEO ni d'etiqueta (FounderCEO = 0 en totes dues opcions). Falta: a Hexagon, una cita R1 del 2016 de l'original de l'emissor (X01 és de companiesmarketcap, agregador); a Uniper, la data d'inici de la baixa (AR 2018, p. 8). Amb l'opció b, `ceos` canvia a Hexagon 2016 (Belkic) i Uniper 2018 (R2b, `founderceo_rob_r2b_com_na`).

---

### Q14. Títol funcional «Joint CEO» (CD Projekt)

**Pregunta.** Si les fitxes per a inversors de l'emissor del mateix exercici diuen «Co-founder, Joint CEO» i l'informe anual en diu «Vice President of the Board», la persona és co-CEO per R1?

**Casos.** PLOPTTC00011 CD Projekt, 2018-2019 i 2020-2021, 4 files. Base: 1, co-CEO Adam Kiciński i Marcin Iwiński, marca `co_ceo_titol_funcional`. Dubtes lot12.
- «Adam Kiciński […] Marcin Iwiński […] President, Joint CEO Co-founder, Joint CEO» (C05, fitxa del 23/11/2018; C06, 28/11/2019; C03, 01/06/2020).
- Fundadors: «Back when Michał Kiciński and myself were establishing the company…» (L10-PLOPTTC00011-F01, Iwiński).

**Metodologia.** Secció 2.1, R1: «el títol de CEO o el càrrec legal equivalent […] identifica el CEO». Regla 9 (co-CEO). CLAUDE.md §3: document de l'emissor «del mateix exercici».

**Opcions.** a) Compta (co-CEO, 1), amb robustesa amb Kiciński com a CEO únic. b) No compta: CEO únic Adam Kiciński → 0 per la prova a (els fundadors són Iwiński i Michał Kiciński).

**Recomanació: a.** És el títol de CEO literal en un document de l'emissor del mateix exercici. El títol funcional i el càrrec estatutari no es contradiuen. Els dos agents hi coincideixen.

**Efecte.** Cap canvi d'etiqueta (4 files a 1). Robustesa nova «sense títol funcional» (4 files a 0; columna nova, cal l'OK de Jordi). Per al 2020-2021 depèn també de Q15. Cal registrar la línia d'Iwiński de la composició del Management Board als informes anuals. Amb l'opció b, 4 files d'1 → 0.
- **CD Projekt 2023 (fora del grup):** la fila té FounderCEO=0, un sol CEO (Adam Kiciński) i la mateixa marca `co_ceo_titol_funcional`. Amb l'opció a, si es troba una fitxa de l'emissor del 2023 que doni Iwiński com a «Joint CEO», la fila passa de 0 a 1 i `ceos` canvia (s'hi afegeix Iwiński). Sense aquesta cita, no canvia.

---

### Q15. Document de l'any *t* anterior al 31/10 (antic punt 8)

**Pregunta.** Un document de l'emissor datat l'any *t*, però anterior al 31/10, que anomena el CEO amb el càrrec, compta com a «document del mateix exercici» (CLAUDE.md §3)?

**Casos.** CD Projekt 2020-2021 (2 files, ja a Q14: C03 de l'1/6/2020 i C04 del 7/10/2021 no són el nomenament i, per tant, no fan d'interval). Wizz Air JE00BN574F90 2021 (1 fila, grup tancable): l'exercici tanca el 31 de març i C01 és de l'informe F21, del 7/6/2021, que no inclou el 31/10/2021.

**Metodologia.** CLAUDE.md §3: «d'un document de l'emissor o d'un regulador **del mateix exercici**». D21: «Si l'informe no documenta cap canvi entre el 31/10 i el tancament de l'exercici, el CEO de final d'exercici serveix com a proxy». Regla 28: l'extrem final de l'interval ha d'anomenar la persona «en una data igual o posterior al 31/10/t».

**Opcions.** a) S'accepta, amb una nota de «document anterior al 31/10», si l'informe de l'exercici no documenta cap canvi fins al tancament. b) Només documents posteriors al 31/10 o l'informe de l'exercici.

**Recomanació: a.** És un document del mateix exercici i la condició del proxy de tancament evita acceptar-lo si hi ha hagut un canvi. A la pràctica ja s'aplica (p. ex. SEB 2017); falta la decisió.

**Efecte.** Cap canvi d'etiqueta. CD Projekt C03 i C04 passen de `ceo_interval` a R1 amb nota. Wizz Air 2021 queda cobert, amb una reserva: les cites [V] de Wizz Air (L11-JE00BN574F90-F01 i C01) són de la còpia d'annualreports.com, un agregador. CLAUDE.md §4 diu que els agregadors «no són l'original: busca l'original de l'emissor». El tancament val pel criteri a del PR #3 (compta qui ha escrit el document) i porta la marca `agregador=true`, però cal substituir la còpia per l'original de l'emissor (wizzair.com o National Storage Mechanism). Amb l'opció b, cal buscar documents posteriors al 31/10 (per a CD Projekt, les fitxes de novembre-desembre del 2020 i el 2021).

---

## Correccions de dades que cal aprovar

Les cinc línies del triatge són quatre correccions: BME apareix dues vegades (dubtes de la regla 29 i del lot 17). Totes van en un lot de correcció aprovat per Jordi, i abans el flux de Wayback ha de verificar les cites a la captura. El detall camp per camp és a `correccions_dades.csv` (`origen=correccio_proposada`).

**Columnes derivades.** Quan canvia FounderCEO, també han de canviar `a_mostra_principal` i les robusteses que en copien el valor. El repositori no té cap script que les recalculi (les fórmules de la r1 les va aplicar DF), i a la base hi ha files de lots anteriors que van canviar d'etiqueta sense recalcular-les. Per això el CSV hi posa una línia per a cada columna derivada que canvia:
- Les robusteses que copien FounderCEO quan la fila no té el tret que tracten (p. ex. `founderceo_rob_nd_com_0` en una fila que no és ND) porten el valor nou.
- Les que depenen d'un fet que no és al registre porten `a_recalcular` (p. ex. si la fundació de Dassault Systèmes del 1981 va ser corporativa) o `a_documentar` (dates de cita que no consten). S'han de resoldre abans d'aplicar el lot.
- Les columnes històriques (`*_v8`, `*_v75r2`) i les de la simulació (`sim_*`) no es toquen, com al lot de correcció 1.
- Les robusteses noves de les regles 25-28 (`founderceo_rob_regla25_nd`, D1 ampla, `founderceo_rob_sense_interval`) encara no existeixen a la base (tasca T6.1 de l'auditoria del 23/11); quan es creïn, s'hi aplicaran les marques d'aquestes files.

### C1. BME (ES0115056139), 2017-2018: canvi de CEO

- **`ceos`: Antonio Zoido Martínez → Javier Hernani Burzako** (2 files). FounderCEO es manté a 0 (prova e, F01).
- **Regla:** P5 (R1: consejero delegado; president executiu només per R3 amb el càrrec de CEO vacant, criteri 4 del PR #3).
- **Cites literals:**
  - L6-ES0115056139-X02 (IAGC 2017, p. PDF 59, H.1.1): «En esta cifra se incluye la remuneración percibida por D. Javier Hernani Burzako desde su nombramiento como Consejero Delegado el 27 de abril de 2017». URL: https://www.cnmv.es/webservices/verdocumento/ver?e=GPsUSqtXoOk8PqxtO1BuJ2U6lyp6K9C6l937F9nEOaMDAeVNxCRAwLPil3Xzyzk3
  - L6-ES0115056139-X03 (IAGC 2018, p. PDF 22, C.1.9): «JAVIER HERNANI BURZAKO En virtud del acuerdo adoptado por el Consejo de Administración el 27 de abril de 2017 el Consejero Delegado tiene delegadas la totalidad de las facultades del Consejo de Administración, excepto las indelegables por ley.» URL: https://www.cnmv.es/webservices/verdocumento/ver?e=7LHu%2f2adYaYMU%2bEo%2fnH6ziHsyw07%2fg9RxrvZrWy77RoDAeVNxCRAwLPil3Xzyzk3
- **Ids:** L6-ES0115056139-X02, -X03 (passen a entrades `ceo` R1), -X04 (context: Zoido «primer ejecutivo», R3 que no s'aplica), -F01 (prova e).
- Coherent amb Santander, BBVA, Inditex 2019-2021 i Iberdrola 2022-2024, i amb Q9. Es tanquen alhora les dues línies de PENDENTS (regla 29 i lot 17).

### C2. Sopra Steria (FR0000050809), 2025: de ND a 0

- **FounderCEO: no_determinat → 0** (1 fila). `regles`: cap → a. Marques: es manté `dubte_D1` i s'afegeix `llista_exhaustiva=implicita` (P8; sense `a_fundador_unic`, perquè són tres fundadors), amb robustesa com a ND.
- **Columnes derivades:** `a_mostra_principal` 0 → 1 (la fila **entra a la mostra principal**); `motiu_nd`, `detall_motiu_nd`, `motiu_nd_article` i `tancament_nd` es buiden (precedent CO1-002); 17 robusteses passen a 0 (16 des de `no_determinat` i `founderceo_rob_nd_com_1` des d'1); `a_mostra_nomes_verificats` queda `a_recalcular` fins que el flux verifiqui la cita.
- **Regla:** prova a (decisió de Jordi del 24/11/2026) + regla 26 (`dubte_D1`: la fusió del 2014 es va fer per OPE de Sopra, amb el 90,52 %, i es comptabilitza com a adquisició) + regla 27 (Sopra Steria 2025: es prova contra Sopra 1968, «prova a per P8 si l'emissor dona la llista de fundadors del 1968»).
- **Cites literals:**
  - L3|FR0000050809|L3SS-17 (Document de référence 2011 de Sopra Group): «Founded in January 1968 by Pierre Pasquier, François Odin and Léo Gantelet, Sopra Group is one of Europe's longest established IT services companies.» URL: https://www.soprasteria.com/docs/librariesprovider2/sopra-steria-corporate/finance/rapports-financiers/sopra2011_drf_en.pdf?sfvrsn=e9f6ddb6_2
  - L3|FR0000050809|L3SS-25 (URD 2025, §3.2.2): «The position of Chief Executive Officer was held by Vincent Paris until 1 March 2022, then by Cyril Malargé until October 8, 2025, and by Xavier Pecquet for the remainder of financial year 2025.» URL: https://www.soprasteria.com/docs/librariesprovider2/sopra-steria-corporate/finance/rapports-financiers/sopra_steria_urd_2025_en_assemblage_opti.pdf
- **Ids:** L3SS-17, L3SS-25, L3SS-26, R2-01 a R2-04, R2-11 (operació del 2014), R2-09 i DF-PR6-SS2 (Pecquet a Sopra Group Holding Ltd des del 2005).
- Matisos: la llista de fundadors del 2007 en donava només dos (el risc el cobreix `llista_exhaustiva=implicita`). La prova b no tanca per anys sencers (1968-1950 = 18) i només és un reforç. Al registre, `marques_fundador` diu `fundacio_no_nova`, i s'ha d'harmonitzar a `dubte_D1`. Cal que el flux verifiqui L3SS-17 a la captura (ara `cita_verificada_a_captura=no` per manca d'accés, no per fallada).

### C3. Dassault Systèmes (FR0000130650), 2016-2020: de 0 a 1

- **FounderCEO: 0 → 1** (5 files). `regles`: a → D37. `d37_data_cita` = 2026-02-21; `founderceo_rob_cita_contemporania` = 0 (ja ho és); `fundador_transformador` = 1 (entrada el 1983, fundació el 1981); `founderceo_rob_pre_d37` i `founderceo_rob_sense_fundador_transformador` (i la còpia `sense_fundador_transformador`) = ND fins que es documenti la prova e amb la P3 (la d no tanca: 2 anys, en calen 3).
- **Columnes derivades:** les 5 files continuen a la mostra principal. 13 robusteses que copien FounderCEO passen de 0 a 1; `founderceo_rob_fundacio_corporativa_com_0` i `founderceo_rob_sense_origen_intern` queden `a_recalcular` (depenen de si la fundació del 1981 va ser corporativa o interna); `d37_cita_contemporania` = no; `a_mostra_nomes_verificats` queda `a_recalcular`.
- **Regla:** D37 (regla 24) amb D37c; P6 («Co-Founder»); precedent B&M (regla 27).
- **Cita literal:** L7-FR0000130650-X03 (comunicat de l'emissor del 21/02/2026, p. 1): «As Co-Founder and CEO, Bernard guided our company from a startup to a world leader.» URL: https://investor.3ds.com/static-files/9cbbc05a-51e9-427a-bbab-e469b9bbfcd4
- **Ids:** L7-FR0000130650-X03 (cal tornar-la a registrar com a `fundador`, D37), -X01 («Founded in 1981», URL https://investor.3ds.com/static-files/68cd64f7-27b6-4441-be4d-84398eab14e1), -X02 («He joined the company in 1983…»), -C01 a -C05 (CEO R1, sense canvis).
- Condicions: X03 només diu «Bernard»; cal afegir la frase del mateix comunicat amb el nom complet (com a B&M). El 0 actual (regla a) no té cap cita de fundador.

### C4. Bridgepoint (GB00BND88V85), 2021-2022: de 0 a 1

- **FounderCEO: 0 → 1** (2 files). `regles`: e → D37. `d37_data_cita` = 2024-06-06; `founderceo_rob_cita_contemporania` = 0 (ja ho és) llevat que surti «founder» a l'AR 2021, a l'AR 2022 o al fullet de l'IPO; `founderceo_rob_pre_d37` = 0 (prova e i P1); marca `fundacio_no_nova` (l'MBO del 2000). `fundador_transformador` = 1 només si es cita que Jackson no hi era el 1984.
- **Columnes derivades:** les 2 files continuen a la mostra principal. 13 robusteses que copien FounderCEO passen de 0 a 1, i també `founderceo_rob_sense_fundador_transformador` (i la còpia) mentre `fundador_transformador`=0; `founderceo_rob_fundacio_corporativa_com_0` es queda a 0 (filial de NatWest des del 1984, X02); `founderceo_rob_sense_origen_intern` = no_determinat (MBO del 2000, segons la metodologia v0.10.10: «sense origen intern (divisió interna o MBO a no_determinat)»); `d37_cita_contemporania` = no; `a_mostra_nomes_verificats` queda `a_recalcular`.
- **Regla:** D37 (regla 24) amb D37a; P6 (aposició «Founder»); P1 i regla 5 («La D37 preval», també en un MBO); precedent B&M (regla 27); criteri a del PR #3 (comunicat de l'emissor en una plataforma).
- **Cita literal:** L7-GB00BND88V85-X01 (RNS de l'emissor del 06/06/2024): «William Jackson, Bridgepoint's Founder». URL: https://www.investegate.co.uk/index.php/announcement/rns/bridgepoint-group-reg-s---bpt/directorate-change/8245113
- **Ids:** L7-GB00BND88V85-X01 (cal una entrada nova `fundador`, D37), -X02 («From its establishment in 1984 to 2000, Bridgepoint operated as a subsidiary of NatWest Group», fullet de l'adquisició d'ECP del 2023, p. 78), -X03, -C01 i -C02 (CEO R1).
- Convé localitzar l'RNS original a londonstockexchange.com o a bridgepointgroup.com (investegate el reprodueix).

---

## Canvis de dades dels tancaments (sense canvi d'etiqueta ni de CEO)

Són els grups `tancable_amb_evidencia` que, a més de tancar el dubte, proposen tocar `dades/`. Cap no canvia FounderCEO ni `ceos`. Detall a `correccions_dades.csv` (`origen=tancament`, 39 línies).

| ISIN | Empresa | Anys | Canvi | Regla |
|---|---|---|---|---|
| ES0148396007 | Inditex | 2017-2018 | `marques` + `ceo_president_exec`. La reclassificació de C01 i C02 de R1 a R3 depèn de Q9b | 2.1 R3 i regla 22 (vegeu Q9 i Q9b) |
| NL0000009082 | KPN | 2016-2025 | `regles` c_AAF64_reserva → c_AAF64_reserva;e; `founderceo_rob_c_com_nd` ND → 0 | Regla 14 (D22) i regla 21 (totes les proves) |
| NL0000226223 | STMicroelectronics | 2018-2025 | `regles` b → d | Prova d contra la part on era el CEO (J1); la b no té el naixement en cita |
| NL0010558797 | OCI | 2016 | `regles` b → b;a; `marques` + `conflicte_fonts`, `fundacio_no_nova`, `llista_exhaustiva=implicita`, `a_fundador_unic` | P6 (última frase), P1, P8 |
| PLPKO0000016 | PKO BP | 2022, 2023 | `regles` c_AAF64_reserva → e;b; `founderceo_rob_c_com_nd` ND → 0 | Regles 14 i 21 |
| IT0003487029 | UBI Banca | 2016-2019 | `regles` b → d | Prova d contra Banca Lombarda (J1, regla 26) |
| SE0000455057 | Balder | 2016-2021 | `regles` cap;FT → D37; `founderceo_rob_sense_ft` ND → 1; `founderceo_rob_cita_contemporania` 1 → 0*; `d37_cita_contemporania` = no; `d37_data_cita` a documentar (vegeu la nota) | Regla 24 (D37 preval sobre l'FT), D37a |
| SE0017832488 | Balder | 2022-2025 | `regles` cap;FT → D37; `founderceo_rob_sense_ft` ND → 1; `founderceo_rob_cita_contemporania` 1 → 0* (2022-2024); `d37_data_cita` = 2025-08-18; `d37_cita_contemporania` no (2022-2024) i sí (2025) | Ídem |
| GB00B3MBS747 | Ocado | 2016-2025 | `founderceo_rob_cita_contemporania` 1 → 0*; `d37_data_cita` a documentar | D37a |
| GB00BNYK8G86 | Darktrace | 2021-2022 | `d37_data_cita` = 2024-09-06; `founderceo_rob_cita_contemporania` 1 → 0*; `d37_cita_contemporania` = no | D37a |
| FR0000051807 | Teleperformance | 2017-2025 | `founderceo_rob_cita_contemporania` 1 → 0* (2017-2024); `d37_data_cita` = 2025-03-06; `d37_cita_contemporania` no (2017-2024) i sí (2025) | D37a |
| FR0014000MR3 | Eurofins | 2021-2024 | `founderceo_rob_cita_contemporania` 1 → 0*; `d37_cita_contemporania` = no; `d37_data_cita` a documentar | D37a |
| NO0010310956 | SalMar | 2019-2021 | `founderceo_rob_cita_contemporania` 1 → 0* (2019 i 2020); `d37_data_cita` = 2021-07-15; `d37_cita_contemporania` no (2019-2020) i sí (2021) | D37a |

\* Llevat que una cerca trobi una cita contemporània de l'emissor (precedent B&M, regla 27). Només afecta la robustesa.

Notes:
- **Balder, `ft`:** la base té `ft`=1, `tipus_ft`=a i `ft_rob_3anys`=1 a totes dues línies. El diccionari de camps no defineix si `ft` marca la via de l'etiqueta o només el fet; per això no es proposa cap canvi d'aquestes columnes. Si Jordi vol que `ft`=1 només marqui files on l'1 ve de l'FT, passarien a 0.
- **Unipol 2024:** es retira el canvi opcional `R-SC;b` → `R3;b`. La base fa servir `R-SC;b` a 12 files resoltes per R3 (UnipolSai 2016-2017, Atlantia 2019, Vifor…); canviar-ne només una la faria incoherent. Si es vol homogeneïtzar, ha de ser un canvi de totes alhora.
- **Rubis 2018-2020 (D37a):** el verificador del triatge diu que la cita de L16-FR0013269123-F01 és del 2025 i no és contemporània. Però el registre té cites [V] de l'emissor anteriors: L16-FR0000121253-F01 (document de référence 2015, dipositat el 28/04/2016: «Il quitte la banque en 1989 pour fonder Rubis en 1990») i L10-FR0013269123-F01 (document de registre del 2017: «Creation of Rubis by Gilles Gobin in tandem with Jacques Riou»). La D37a compta les «cites de data fins al 31/10/t», i per tant `founderceo_rob_cita_contemporania`=1 es pot mantenir. Cal ampliar als anys 2018-2020 (i 2021-2024) els anys d'una d'aquestes entrades. No es proposa cap canvi a `dades/`.

## Punts informatius (sense decisió)

- **Cites del lot 11 d'un altre exercici (antic punt 9):** 18 entrades marcades `no_valida` o amb menys anys (PR #29). Les files es tornen a buscar.
- **Cerques (41 grups, 114 files):** Claude les fa sense límit d'intents (A.4). Entre elles: ICAP/NEX (que pot acabar a Q1), Petrofac, Merlin (que depèn de Q5b), Sagax, Zalando, alstria (prova e), Tritax 2018-2020 (R-SC), Cellnex 2016-2022 (cita contemporània a l'informe anual 2015 o 2016 o al fullet de l'OPV del 2015), CTS Eventim (font de l'FT), Inditex 2016, Vifor 2017-2019 i ACS 2017-2020 i 2022-2025.
- **Tancaments sense canvi de dades:** la resta dels 34 grups tancables (p. ex. Aedifica 2019, Allreal 2022, Clariant 2016, Lonza 2019, Sandoz 2023-2025, Bankia 2016, MorphoSys 2018, Allfunds, Regus, Wizz Air, Derwent, Rubis per la cita de fundador, PZU 2024) només necessiten ajustos al registre (marca D37 en lloc de `cita_fundador`, anys d'una entrada, tipus d'entrada) i la verificació de Wayback. **Reserva per a Wizz Air 2021:** les cites són de la còpia d'annualreports.com (agregador, CLAUDE.md §4); el tancament val pel criteri a del PR #3, però cal substituir-la per l'original de l'emissor.

---

## Fonts d'aquest paquet

- Triatge: `triatge.csv` i `triatge_resultats.json` (columna `cl_final`), i `ctx/<ISIN>.md`.
- `docs/PAQUET_CRITERIS_20261123.md`, `CLAUDE.md`, `docs/METODOLOGIA_3_Articles_v0.10.10.md` (regles 5, 6, 9, 21, 22, 24-29; seccions 2.1 i 3.2).
- `lots/correccio1_canvis.csv` (CO1-028 a CO1-034), `traspas/candidates_evidencia.csv` (C0306), `lots/lot16_dubtes.csv` (fets que encara no són al registre, marcats «no registrat»), `docs/DICCIONARI_CAMPS.md` i `docs/LIMITACIONS.md` (columnes derivades).
- `docs/REGISTRE_CANVIS.csv` (cites i URL), `dades/base_isin_any_v8r3.csv` (valors actuals), `PENDENTS.md`, `estat/estat_files.py` (referències de dubte: regla29, lot9, lot10, lot12, lot16, lot17).

# Decisions de criteri pendents (23/11/2026)

Preparat per Claude perquè Jordi decideixi, amb Doctorat si cal. Cada punt té:
- el problema, amb dades del repositori;
- les opcions;
- la recomanació de Claude;
- l'efecte sobre la base.

Mentre no hi hagi decisió, no es toca cap etiqueta: les files afectades queden en dubte a `PENDENTS.md`.

N'hi ha deu, per ordre d'importància. **El punt 1 és el que més afecta el resultat final.**

---

## 1. Què compta com a «prova de no fundador documentada» (C2 de les files P)

**Problema.** Ara, l'estat (`estat/`) dona per bona la C2 d'una fila P si hi ha **alguna** cita de fundador vàlida. Però les proves de la metodologia (regla 21) tenen parts:

| Prova | Parts |
|---|---|
| a | llista tancada de fundadors |
| b | any de fundació + naixement del CEO |
| c | any de fundació, 64 anys o més abans |
| d | ocupador anterior + any de fundació |
| e | origen corporatiu o estatal |

Un control automàtic estricte sobre les cites del registre de les 4.224 files P que avui tenen C2 per registre dona aquest resultat:
- només unes **420** tenen cites que contenen **totes** les parts;
- unes 900 en tenen una part;
- la resta no en tenen cap que el control reconegui. Per exemple, «Andreas Treichl (Chairman) 1952» com a única cita de la prova b.

El control té falsos negatius, i per tant la xifra real és més alta. Tot i així, n'hi ha prou per veure que **la C2 actual sobreestima la documentació de les proves de no fundador**.

**Observació clau.** Les parts no són per fila:
- l'any de fundació és de l'**empresa**: una cita serveix per a tots els anys;
- el naixement i l'ocupador anterior són de la **persona**: una cita serveix per a tots els anys que és CEO.

Per tant, completar-ho costa molt menys del que sembla: unes 1.000 empreses i uns 1.500 CEO, no 5.600 files.

**Opcions.**
- a) Mantenir la C2 com ara: qualsevol cita de fundador vàlida.
- b) Exigir totes les parts, combinant les cites de l'empresa (fundació, origen, llista) i de la persona (naixement, ocupador). Les parts que falten es busquen per empresa i per persona.
- c) Com la b, però només per a la mostra principal, i deixar la resta per a una robustesa.

**Recomanació: b.** Davant del tribunal, un 0 ha de ser tan auditable com un 1 (secció 2.3 de la metodologia).

**Efecte i pla si es tria la b:**
1. Canviar `estat/estat_files.py` perquè la C2 de les P es calculi per parts.
2. Fer un lot de «fitxa d'empresa» (any de fundació, origen, llista de fundadors) i un de «fitxa de persona» (naixement, carrera), a partir de les candidates de l'auditoria i de cerques noves.

El lot 14 ja aplica aquest criteri a les cites noves.

---

## 2. Grup F: entitat fundada que no és la cotitzada (regla 26, D1 estricta)

| Empresa | Anys | Què diu la font A | Pregunta |
|---|---|---|---|
| ICAP / NEX (Spencer) | 2016; 2017-2018 | «Intercapital plc was founded by Michael Spencer in 1986». El 1999, Intercapital i Garban es van combinar en ICAP. NEX és una holding nova del 2016 | La combinació del 1999 compleix la D1 estricta (sense que cap part tingui més del 60 %)? Si no, ICAP compta com a fundació d'Intercapital? NEX: P1 (holding nova) |
| Standard Life Aberdeen (Gilbert) | 2017-2018 | «He is co-founder (and former chief executive) of Aberdeen Asset Management PLC». L'emissor comptabilitza la fusió del 2017 com a **adquisició** d'Aberdeen per Standard Life (66,7 % per als accionistes de Standard Life) | Tot apunta a `dubte_D1`: no s'aplica la D1 i, per tant, Gilbert no seria fundador de la cotitzada. La fila és F perquè Gilbert era co-CEO; l'altre co-CEO, Skeoch, no és fundador (prova d) |
| Petrofac (Asfari) | 2016 | «as both its co-founder and Group Chief Executive» (comunicat del 2020). L'emissor també diu que Petrofac Inc és del 1981 i que Asfari s'hi va incorporar el 1991 a través d'AMcorp | D37 (l'emissor l'anomena cofundador, i la D37 preval) o P1/D1 (la incorporació del 1991)? |

**Recomanació:**
- **Standard Life Aberdeen:** `dubte_D1`. Valor de la fila segons la regla de co-CEO vigent: si n'hi ha prou que un co-CEO sigui fundador, la fila queda en dubte; si no, 0.
- **Petrofac:** 1 per D37, perquè l'emissor l'anomena cofundador i la D37 preval sobre les proves. Cal una cita que l'anomeni pel nom: la capçalera del comunicat ho fa, i es pot ampliar.
- **ICAP/NEX:** cal la participació de cada part a la combinació del 1999. Ho puc buscar, si cal.

---

## 3. Grup F: contradiccions amb font A (possible 1 → 0)

| Empresa | Anys | Base | Què diuen les fonts |
|---|---|---|---|
| Cellnex (Tobías Martínez) | 2016-2022 | 1 | IAGC 2018 (CNMV): va entrar a Tradia/Retevisió (grup Abertis) com a directiu el 2000. Cellnex és l'escissió d'Abertis del 2015. L'emissor en diu «CEO fundador», que la P6 no admet. Forbes (2023) en diu «fundador» citant el fons Antin (font B; preval la A) |
| Merlin Entertainments (Varney) | 2016-2019 | 1 | Informe anual 2016: era director general de Vardon Attractions abans de l'**MBO** del 1999, i la P1 diu que un MBO no és fundació nova. Un portaveu citat per PA en diu «our founder» (B; `conflicte_fonts`) |

**Recomanació:**
- **Cellnex:** 1 → 0. Prova e, amb la comprovació de la P3: cal documentar amb la prova a, b o d que el CEO no és fundador d'Abertis (hi va entrar l'any 2000, com a directiu d'una filial). Es pot aplicar també la P4 (primer CEO d'una escissió). Marques `fundador_escissio` i `conflicte_fonts`. Si no es pot documentar la P3, ND.
- **Merlin:** 1 → 0 per la P1, si es documenta l'any de fundació de Vardon i que Varney hi va entrar més tard (prova d). Si no es documenta, ND.

Totes dues anirien en un lot de correcció a part, amb cita i registre.

---

## 4. Grup F: expressions dubtoses segons la P6

| Empresa | Expressió | Recomanació |
|---|---|---|
| Rightmove (McKittrick, 2016) | «one of the co-founding executives of Rightmove». A més, l'emissor diu que Rightmove la van formar quatre agències el 2000 | No compta: és un «founding executive», equivalent a «founding CEO». Prova e (creada per quatre empreses) i P3 → possible 1 → 0 |
| Energean (Rigas, 2023) | «Prior to setting up Energean, Mathios…», i la mateixa biografia diu «founding shareholder» | «Set up» amb la persona com a subjecte implícit compta (P6). Però la P1 s'hi aplica: Energean es va crear el 2007 i va comprar el negoci de Prinos (1981), i la holding cotitzada és del 2017. Recomano 1 per D37, amb la marca de la P1 |
| Extensió analògica de les exclusions | «founding member/partner/chairman/director» i «part of the founding group» (Tatiana Rizzante, Reply) | Confirmar que tampoc no compten, igual que «founding shareholder» |

---

## 5. Grup F sense cap font A/B de fundador

- **alstria (Elamine, 2019-2021):** només en diuen fundador els agregadors. L'informe del 2006 diu que alstria la va crear un vehicle d'un fons de Captiva i que Elamine en va ser el primer gerent, aportat per NATIXIS Capital Partners. Recomanació: prova e amb la P3 → possible 1 → 0, o ND.
- **Sagax (Mindus, 2021-2025):** l'emissor només diu «CEO since 2004». Hi ha dos articles d'Affärsvärlden (B) que no s'han pogut obrir. Recomanació: ND fins que es trobi una font, o bé buscar l'informe de la fundació del 2004.

---

## 6. Criteri del CEO (dubtes del lot 12)

| Empresa | Anys | Pregunta |
|---|---|---|
| Primary Health Properties | 2020 | Harry Hyman era Managing Director de l'assessor extern (Nexus), no CEO de la cotitzada. Va ser nomenat CEO el 5/1/2021. R3 o R-SC? |
| Tritax Big Box | 2021-2025 | REIT gestionada externament: Colin Godfrey és soci de la gestora. Els anys 2018-2020 de la mateixa empresa són NA (R-SC). Coherència: NA també el 2021-2025? |
| CD Projekt | 2018-2021 | Iwiński: els informes en diuen «Vice President of the Board»; «Joint CEO» només surt a les fitxes per a inversors |
| Zalando | 2016-2018 | Gentz i Schneider: els informes en diuen «member of the Management Board» (el consell no té president); el títol de co-CEO surt més tard |
| Rubis (SCA) | 2016-2025 | Compten els Gérants com a CEO (R1), també quan ho són a través de societats (Agena, Sorgema)? |

**Recomanació:**
- **Rubis:** R1. El Gérant és l'equivalent legal del CEO en una SCA, com a Hermès o Michelin.
- **PHP 2020 i Tritax:** R-SC (NA), per coherència amb els anys 2018-2020 de Tritax.
- **CD Projekt i Zalando:** co-CEO per R1 amb fonts de l'emissor posteriors, amb la marca de document retrospectiu. Si no s'accepta, R2b (direcció col·legiada).

---

## 7. EssilorLuxottica 2020 (lot 13)

Al 31/10/2020, Del Vecchio era Président-Directeur Général, i Sagnières Vice-Président-Directeur Général Délégué, **amb poders iguals**. La base té un CEO únic per R1. **Recomanació:** mantenir R1, perquè el títol de CEO és només de Del Vecchio. Cal confirmar-ho.

---

## 8. Documents del mateix exercici: abast (CLAUDE.md §3)

Ara s'accepten per a la fila *t*:
- l'informe anual de l'exercici que inclou el 31/10/*t*;
- els comunicats o documents de l'emissor datats a l'any *t* que anomenen el CEO amb el càrrec, també si són d'abans del 31/10. Per exemple, «appoints Johan Torgeby new President and CEO» (SEB, 2017).

**Pregunta:** n'hi ha prou amb un comunicat de nomenament de l'any *t* anterior al 31/10, o cal que el document sigui posterior al 31/10, o l'informe anual? **Recomanació:** acceptar-ho, perquè és un document del mateix exercici, i marcar-ho a les notes.

---

## 9. Cites de CEO del lot 11 d'un altre exercici

18 entrades del lot 11 (traspàs de l'auditoria IA) usaven l'informe de l'any anterior o del següent. S'han marcat `no_valida` o se n'han reduït els anys (PR #29), i les files es tornen a buscar. Només cal estar-ne informat; no cal decidir res.

---

## 10. Resta de dubtes oberts (257 files)

| Origen | Files | Naturalesa |
|---|---:|---|
| Lot 10 (traspàs) | 122 | La majoria són fonts que no s'obrien o proves no tancades: es poden resoldre cercant. Uns quants són de criteri (P1, P3, P6, D37d) |
| Regla 29 (lots fora de mostra) | 111 | La majoria són P sense font a la primera passada: cal cercar-ne. Uns quants són de criteri: R2b (Uniper 2018), «CEO fundador» (Cellnex), CEO de la base diferent del de la font (BME 2017-2018, Ferrovial 2016) |
| Lot 16 | 27 | Punts 2-5 d'aquest document |
| Lot 12 | 23 | Punt 6 |
| Lot 9 | 13 | Cerca |
| ND | 1 | Sopra Steria 2025 |

**Pla:** Claude resol per cerca els dubtes de cerca. Els de criteri van en paquets com aquest.

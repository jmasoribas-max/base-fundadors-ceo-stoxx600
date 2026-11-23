# Instruccions per a Claude Code

Aquest fitxer té el mateix contingut normatiu que `AGENTS.md`. **Si discrepen, mana aquest fitxer (`CLAUDE.md`).** Historial d'aprovacions: final del fitxer.

## 1. Missió

Base de fundadors-CEO de l'STOXX Europe 600 (2016-2025, 1.040 empreses, 6.012 files ISIN-any). Base oficial: `dades/base_isin_any_v8r3.csv`. Per a cada fila: el CEO a 31/10 i si és fundador (1/0/ND/NA), cadascun amb una font A/B, una cita literal i una URL estable que qualsevol pugui comprovar.

## 2. Qui fa què

| Feina | Qui |
|---|---|
| Cercar fonts A/B, llegir-les i proposar cita, URL, pàgina i prova (a-e, D37, R1-R3) | Agent (Codex o Claude) |
| Comprovar que la cita surt literalment al document sencer, buscar i verificar la captura Wayback (`id_`), omplir els camps `wayback_v8r1_*` i `cita_verificada_a_captura`, generar els recomptes | DF, per script, des del seu ordinador |
| Revisar dubtes de metodologia | Doctorat |
| Aprovar i fusionar | Jordi |

L'agent **no** ha de reintentar Wayback, ni demanar desades (Save Page Now), ni repetir descàrregues que el seu entorn talla. Ho fa DF.

## 3. Quan una fila està feta

Una fila del lot està **feta** quan té:

1. **CEO:** almenys una entrada `funcio_cita=ceo` amb una cita que anomena la persona i el càrrec, d'un document de l'emissor o d'un regulador **del mateix exercici** (informe anual, document de registre, comunicat). Si no n'hi ha, val un **interval** (regla 28 de l'annex): dues entrades A/B, el nomenament amb data igual o anterior al 31/10 de l'any i un document que anomeni la persona CEO en una data igual o posterior al 31/10 de l'any (no n'hi ha prou que el document sigui posterior). Totes dues porten `marca_prova` = `ceo_interval` i a `notes` diuen `inici` o `final`. Si trobes una sortida o successió entre els dos extrems, l'interval no val i s'aplica R1-R3.
2. **Fundador:** almenys una entrada `funcio_cita=fundador` amb la prova positiva que justifica l'etiqueta (`marca_prova` = a, b, c, d o e per a un 0; D37 o la regla que correspongui per a un 1).
Si no hi ha font A/B (regla 29 de l'annex), la fila **no** està feta ni verificada: surt a la taula de dubtes del PR amb què s'ha buscat i on, i s'afegeix a la secció «Dubtes dels lots `fora_mostra_auditoria` (regla 29)» de `PENDENTS.md` (només afegint línies). No s'hi canvia l'etiqueta. Després s'hi aplica la cerca sense límit d'intents (A.4).

Cobrir la fila és el que compta. No cal aportar més d'una cita per fet si la primera és bona.

## 4. Fonts

- Només fonts de nivell **A** (documents de la mateixa empresa o registres oficials) i **B** (premsa econòmica de qualitat, llibres, articles acadèmics).
- Wikipedia, LinkedIn, Crunchbase, pàgines d'alumni, biografies no corporatives i textos d'IA són fonts **C**: serveixen de pista, mai de prova. Una font C mai no verifica, ni sola ni amb altres fonts C.
- Ordre de preferència: (1) informe anual o document de registre de l'emissor de l'exercici; (2) comunicat de l'emissor o canal regulat (p. ex. EQS); (3) regulador o registre; (4) font B.
- Agregadors (annualreports.com, companiesmarketcap.com, zonebourse, marketscreener) no són l'original: busca l'original de l'emissor.
- Un `0` (no fundador) necessita una **prova positiva amb cita**. Si no hi ha proves que sigui fundador, és **indeterminat**, no `0`. No forcis un 0 ni un 1.
- La data de referència del CEO és el **31/10 de cada any** i no es pot canviar.
- No inventis dades, hashes, dates, càrrecs ni classificacions.
- La cita ha de ser al document obert, no a un resum ni de memòria. Copia-la tal com surt (sense traduir ni reescriure), d'una a tres frases.

## 5. Estats d'una entrada (definició operativa)

Aquesta secció i la verificació Wayback per DF (secció 2) són de procediment i no formen part de la metodologia (METODOLOGIA v0.10.10, changelog).

| Situació | `marca_veritat` | Què hi poses |
|---|---|---|
| Has obert el document **sencer** i hi has trobat la cita literalment | `[V]` | `notes`: on és (pàgina o secció) |
| No has pogut obrir el document sencer: 403, 429, 503, temps esgotat, captcha, pàgina de bloqueig, **descàrrega tallada** (mida exacta 1.048.576 o 5.242.880 bytes, o PDF que no s'obre) | `[NV]` | `notes`: `pendent_DF: <motiu i mida>`. **No vol dir que la font sigui dolenta** |
| Has obert el document sencer i la cita **no hi és**, o és d'un altre any, o la font és C | `[NV]` | `notes`: `no_valida: <motiu>`, i busca'n una alternativa A/B |

- Un error d'accés no és mai prova que la cita no hi sigui. Només `no_valida` rebaixa una font.
- Les fonts que ja hi ha al registre per a les files del lot es revisen amb la mateixa taula. No s'esborren mai: si canvia l'estat, s'afegeix la nota nova a continuació de l'antiga.
- `[V]` de l'agent és provisional fins que DF el confirma per script.

## 6. Format de sortida (exacte)

Cada entrada nova és una fila a `docs/REGISTRE_CANVIS.csv` amb les mateixes columnes que el fitxer, i omple com a mínim:

| Camp | Valor |
|---|---|
| `tipus` | `evidencia_ceo`, `evidencia_fundador`, `evidencia_context`, `revisio_font` o `dubte_metodologic` |
| `grup_id` | `L{n}-{ISIN}` |
| `isin`, `nom`, `anys`, `n_files` | de la fila o de l'interval |
| `origen` | `proposta_{agent}_lot{n}` (p. ex. `proposta_codex_lot6`) |
| `estat_certificacio` | `fora_mostra_auditoria` (o el valor de la fila a la base) |
| `cita_literal`, `url_font` | obligatoris si `funcio_cita` és `ceo` o `fundador` |
| `id_document_o_font` | `L{n}-{ISIN}-C01`, `-F01`… (C = CEO, F = fundador), únic |
| `model_verificacio` | nom de l'agent |
| `marca_veritat` | segons la secció 5 |
| `notes` | pàgina o secció; `pendent_DF:` o `no_valida:` si escau |
| `url_wayback`, `wayback_v8r1_*`, `cita_verificada_a_captura` | **buits**: els omple DF |
| `allotjament` | `emissor`, `regulador`, `grup`, `successor`, `plataforma` o `mitja` |
| `funcio_cita` | `ceo`, `fundador`, `context` o `revisio_font` |
| `marca_prova` | per a `fundador`: `a`, `b`, `c`, `d`, `e` o `D37`; per a `ceo`: `R1`, `R2`, `R2b`, `R3` o `ceo_interval` |

A cada fitxa `empreses/{ISIN}.md` del lot, afegeix (sense esborrar res) les cites amb el seu `id_document_o_font` i la URL original.

El cos del PR té **una sola** secció de resultats, amb aquests recomptes i cap altra xifra: files del lot; files fetes (secció 3); de les quals, files amb `ceo_interval`; files en dubte i enviades a `PENDENTS.md`; entrades noves per `marca_veritat` i per tipus de nota (`pendent_DF`, `no_valida`); fonts antigues revisades i quantes són `no_valida`; canvis proposats a FounderCEO o `ceos` (han de ser 0 en un lot `fora_mostra_auditoria`; si en veus un, va a dubtes). Si refàs el PR, substitueix la secció; les versions anteriors van a `docs/REGISTRE_CANVIS.md` marcades com a «v1», «v2».

## 7. Mida del lot i quan aturar-se

- Un lot = la llista d'ISIN que DF posa a `lots/lot{n}.csv` (ISIN, any). Normalment unes 50 empreses i unes 250-300 files. No l'ampliïs ni el retallis.
- Per fila: si després de mirar l'informe anual de l'any, el de l'any següent i el web d'inversors de l'emissor no trobes la font, passa la fila a dubtes amb el que has mirat i continua. No hi dediquis més temps en aquest lot. És només un triatge de primera passada (regla 29): la fila va a `PENDENTS.md` i després s'hi aplica la cerca sense límit d'intents (A.4). Als casos oberts (ND, `ceo_pendent`, `no_certificada`) no hi ha límit.
- Si l'entorn falla (feina que no acaba, xarxa), fes commit del que tinguis a la branca i explica-ho al PR. No deixis feina només a la conversa.

## 8. Branques i PR

1. Crea la branca `cas/fora-mostra-lot{n}` a partir de `main`.
2. Llegeix `lots/lot{n}.csv`, les fitxes del lot, les seves files a `dades/base_isin_any_v8r3.csv` i les entrades que ja tenen a `docs/REGISTRE_CANVIS.csv`.
3. Escriu les entrades (secció 6), les cites a les fitxes i, si n'hi ha, els dubtes a `PENDENTS.md` (secció 3).
4. Executa en local, **sense `--live`**, `python3 scripts/valida_pr.py` i `python3 scripts/comprova_enllacos_cites.py`. Han de donar 0 problemes. Recalcula `MANIFEST_SHA256.csv`.
5. Obre **un** PR per lot amb el cos de la secció 6. No el fusionis.

**No toquis mai** `main`, `dades/`, `scripts/`, `docs/METODOLOGIA.md`, `CLAUDE.md`, `AGENTS.md`, les regles, `.github/` ni `.claude/`. Excepció (decisió de Jordi del 23/11/2026): Claude, com a coordinador de la base, pot modificar scripts/ i .github/, i pot aplicar a dades/ els lots de correcció que Jordi hagi aprovat explícitament, amb el registre i les fitxes corresponents; sempre en una branca i per PR, que DF valida i Jordi aprova i fusiona. Aquesta excepció no s'aplica a cap altre agent. No pots fer commit ni push a `main`, ni fusionar un PR, ni esmenar, rebasejar o forçar `main`. No s'usa `curl -k` ni s'omet la verificació del certificat TLS. Sense logins ni salts d'antibots.

El flux, un cop obert el PR, és aquest i no un altre: 1) **DF** valida (format, comptes, scripts, verificació de cites i Wayback); 2) **Doctorat** revisa la metodologia; 3) **Jordi** aprova. Protecció de `main`: `docs/PROTECCIO_BRANCA_MAIN.md`.

Si un PR torna amb correccions, DF dona la llista exacta d'ID. Corregeix només aquests ID, a la mateixa branca. Hi ha **una sola ronda** de correccions per lot.

## 9. Format de les propostes de canvi d'etiqueta o de CEO (fora dels lots `fora_mostra_auditoria`)

Cada proposta (al registre i, si cal, al cos del PR) ha de portar com a mínim:

- `isin` i `any` (o interval d'anys)
- valor actual i valor proposat de FounderCEO (o del camp que es modifica)
- regla aplicada (un sol valor, el més fort que s'aplica; vegeu `docs/METODOLOGIA.md` i, per als criteris del PR #6, la regla 25 més avall)
- nivell de font (A o B)
- cita literal
- URL original
- URL Wayback (o declaració de pendent; la pot completar DF)
- justificació breu, sense afegir fets que no siguin a la cita
- efecte esperat sobre la certificació (N1, N2, doctorat, ceo_pendent, no_certificada), sense autodeclarar-la tancada: la certificació queda dins el flux (DF, Doctorat, Jordi)

No proposis un canvi sense cita literal i URL.

## 10. Altres feines (ordre de `PENDENTS.md`)

1. **Casos oberts:** 6 ND (les que queden després del lot ND-1: Drillisch 2017, Sopra Steria 2025 i Aroundtown 2017-2020), 108 `certificada_ceo_pendent`, 241 `no_certificada`, i els casos clau (LVMH, BE Semiconductor, Aberdeen 2016, Anders Dam). Busca fins que trobis la font. Si després d'una cerca exhaustiva i documentada no hi ha cap font A/B, la fila queda indeterminada i a la fitxa s'explica què s'ha buscat i on. Cap límit d'intents.
2. **Les files sense auditar** (`sim_estat_certificacio=fora_mostra_auditoria`: 3.890 a la base v8 r3 [V]; després dels lots 4 i 5, en queden 2.888 a 625 ISIN [V, càlcul de DF del 20/11/2026]). Es fan per lots de DF (secció 7).
3. **Fitxes completes:** el CEO de cada any amb cita, la prova de fundador o de no fundador, el sector i les fonts amb Wayback.
4. **Errors:** si una dada contradiu la base, encara que estigui certificada, proposa'n la correcció amb la cita (secció 9). En un lot `fora_mostra_auditoria` la proposta va a la taula de dubtes i no es canvia `dades/`.

Nota sobre Wayback per a qui la verifiqui (DF): per verificar una cita en un **PDF** arxivat a Wayback Machine, cal obrir el document de la captura, no l'embolcall HTML. Si la URL de la forma `https://web.archive.org/web/{timestamp}/{url}` retorna una pàgina HTML (barra de Wayback) i no el PDF, s'ha d'usar el modificador públic `id_`: `https://web.archive.org/web/{timestamp}id_/{url}`, que serveix els bytes originals de la captura. Això no és un bypass d'accés: és la forma de recuperar el fitxer arxivat. La cita s'ha de rellegir al document (per exemple amb `pdftotext`). Si, també amb `id_`, la captura no és el document, es declara `pendent_verificacio_externa` i no s'inventa.

# Annex normatiu (text vigent; les regles es copien literalment de la metodologia)

## Criteris aprovats de la regla 25 (METODOLOGIA v0.10.8)

Font: `METODOLOGIA_3_Articles_v0.10.8.md` (secció 2.3, regla 25), SHA-256 `e8dfa212b2be5c90cda94919f1326396c4025387a03e5dd7ece3c2a353dc802d`, comprovat el 20/11/2026. Criteris de treball del PR #6, proposats per Doctorat i aprovats per Jordi el 20/11/2026 a les 09:29 Europe/Madrid (segons DF). Desenvolupen normes ja vigents (proves a-e, D1 estricte, D10/D10b, D36, D37, regla 5) amb criteris generals; no creen cap principi nou. Totes les files afectades porten marca i robustesa. El text que segueix és el de la regla 25, sense afegir-hi normes noves:

- **P1.** Holding nova, redomiciliació o vehicle d'LBO no són fundació nova. Només hi ha fundació nova si es crea un negoci nou o es combinen negocis independents que compleixen la D1 estricta. Per a b, c i d, la fundació rellevant és la del negoci operatiu. Base: D36, prova d i regla 5; coherent amb Adams, Almeida i Ferreira (2009) [V], llevat que ells compten l'LBO com a fundació. La D37 preval. Marca `fundacio_no_nova`; robustesa amb aquestes files com a ND.
- **P2.** Fusions i reorganitzacions dins el mateix grup no són fundació nova (no hi ha parts independents i la D1 no s'hi aplica). Mateix tractament, marca i robustesa que la P1.
- **P3.** La prova e es compleix si la cotitzada la va crear una altra empresa. Si la matriu té fundadors persona física, cal comprovar també (amb a, b o d sobre la matriu) que el CEO no n'és un; si no es pot comprovar, la fila queda ND. Marca `e_matriu_personal`.
- **P4.** El primer CEO d'una escissió no és fundador per defecte (prova e amb la comprovació de la P3). És 1 només si una font A de l'empresa l'anomena fundador (D10b, D37) o si és fundador de la mare (v0.10.6). «Founding CEO» o «first CEO» volen dir primer CEO, no fundador. Es manté la robustesa `fundador_escissio` a 0 i s'afegeix la robustesa amb aquestes files com a ND.
- **P5.** Identificació del CEO sense títol, en ordre: R1 (títol de CEO o equivalent legal: Vorstandsvorsitzender, consejero delegado, PDG, directeur général, verkställande direktör, administrateur délégué o similars); R2 (interins) i R2b (direcció col·legiada transitòria); R3 (persona descrita literalment com a primer executiu en font A/B; el president executiu només si el càrrec de CEO és vacant, criteri 4 del PR #3); R-SC (NA) només després d'una cerca exhaustiva i documentada. Els co-CEO segueixen la regla vigent. Marques i robusteses existents (`ceo_president_exec`, R2b com a NA).
- **P6.** Equivalències de la D37 en font de l'emissor: fundador, cofundador, oprichter, Gründer, fondateur, grundare i similars; «founded», «set up», «established» o «started» la companyia amb la persona com a subjecte; aposicions com «tevens founder». Les actes de junta publicades per l'emissor són font A de l'emissor (BE Semiconductor, Blickman, actes de la junta del 2021 a besi.com, segons DF). No compten: «founder-led», «founding CEO», «founding shareholder», ni «architect» o «creator» del grup (aquests dos, només per la via FT), ni les cites de fundador d'una altra entitat. Un «sí» de font B sense D37 compta com a 1 si cap font A/B no el contradiu i es refereix a la cotitzada o a una predecessora D1/D10; marca `si_font_B` i robustesa com a ND. Si el contradiu una prova de no basada en fonts A, preval la prova A (`conflicte_fonts`).
- **P7.** Contradiccions sobre la data de fundació: preval l'emissor sobre la seva pròpia fundació, després un registre o regulador i després una font B. La prova b usa la data més recent entre les plausibles de nivell A/B. Si la classificació canvia segons la data, es manté la principal amb marca `data_fundacio_conflicte` i robustesa com a ND.
- **P8.** Una atribució concreta en singular («founded in [any] by X») en font A, sense cap font A/B que anomeni cofundadors, val com a llista tancada per a la prova a. Marques `llista_exhaustiva=implicita` i `a_fundador_unic`; robustesa com a ND.
- **P9.** El primer accionista compta com a ocupador anterior per a la prova d si és una entitat jurídica diferent i hi ha cita que el CEO hi treballava abans d'incorporar-se a la cotitzada (cas Abertis). Qui funda a través d'un vehicle personal o familiar és fundador persona física, i la prova e no s'aplica a aquella entitat (cas Ryanair). Els altres detalls es resolen amb P1-P8; només s'eleven els que no hi encaixin.
- **Steinhoff 2016-2017 (Jooste):** FounderCEO=0 a l'anàlisi principal per la regla b del lot ND-1, amb marca `conflicte_fonts` (TimesLIVE, font B, «the company he founded») i robustesa a 1. Es fa una cerca exhaustiva de «founder» als informes anuals de l'emissor del 2015-2017 i al fullet de llistat a Frankfurt del 2015; si l'emissor l'anomena fundador, o una font A acredita que el 1998 compleix la D1 estricta i Jooste n'era fundador de la seva part, passa a 1 per D37.

Aquest text no autoritza a canviar `dades/` ni les robusteses en el mateix PR que només documenta les instruccions. Qualsevol aplicació a la base va en un lot a part, amb cita, registre i el flux DF → Doctorat → Jordi.

## Regles 26 i 27 (METODOLOGIA v0.10.9)

Font: `METODOLOGIA_3_Articles_v0.10.9.md` (secció 2.3, regles 26 i 27), SHA-256 `ce4188360905deca13508fc0df45dd249c4090fa5051b3993da555f86ab68991`, comprovat el 20/11/2026. Incorporades a aquestes instruccions amb l'aprovació de Jordi del 20/11/2026 a les 17:18 Europe/Madrid (segons DF).

### Regla 26. D1 estricta [PROTOCOL v1.2.9, Jordi, 11/11/2026 12:43; incorporada a la metodologia per Jordi el 20/11/2026 14:25, segons DF]

Text literal: «Només són fusions entre iguals (AAF 2009) si la font les descriu com a "merger of equals", fusió o combinació (no adquisició), o si cap de les parts no té més del 60% del capital de l'entitat resultant. Una adquisició, o la compra d'una start-up, no fa fundadors els seus fundadors. Si no queda clar, no s'aplica la D1 (`dubte_D1`). Robustesa amb la definició ampla per als casos marcats.» Lectura: si la descripció i l'estructura de l'operació es contradiuen (p. ex. «between equals» però OPE i comptabilització com a adquisició), hi ha `dubte_D1`, no s'aplica la D1 i la fundació rellevant és la de la part absorbent o la de la part on era la persona (J1). Si s'aplica la D1, una persona que no era a cap de les parts no n'esdevé fundadora per la D1.

### Regla 27. Decisions del PR #6, segona ronda [Jordi, 20/11/2026 14:25, segons DF]

- B&M LU1072616219 2016-2021 (Arora): FounderCEO=1 per D37, després d'una cerca de cita contemporània de l'emissor (informes 2016-2021 i fullet IPO 2014). Cita A de l'informe anual 2024 («an entrepreneurial founder»), amb la persona identificada al mateix document com a predecessor de Russo (p. 88 i 95). D37b: `fundador_transformador`=1 (no era a la fundació del 1978). D37a: si no hi ha cita contemporània, les files queden a 0 a `founderceo_rob_cita_contemporania`.
- Aroundtown LU1673108939 2017-2020: de ND a 0 per la prova a. L'aposició A «Founder of the Group in 2004» (Gabay) val com a atribució de fundador únic (P6, P8); la redomiciliació del 2017 no és fundació nova (P1). Marques `llista_exhaustiva=implicita`, `a_fundador_unic` i `fundacio_no_nova`; robustesa com a ND.
- 1&1 Drillisch DE0005545503 2017 (Choulidis): de ND a 0, substitueix la decisió J5 del 15/11/2026. Dues proves independents: a) l'emissor enumera els fundadors de l'entitat del 1997 sense Choulidis (`llista_exhaustiva=implicita`); d) entrada el 1998/1999 respecte del negoci operatiu del 1983 (P1), amb ocupador anterior documentat (Honeywell 1987-1991). Alphatel i E.I.C. no són predecessores (adquisició, no D1 estricta; D37d). Marca `data_fundacio_conflicte` sense robustesa com a ND, perquè la classificació no canvia amb cap de les dues dates.
- ITV GB0033986497 2017: el CEO a 31/10/2017 és Peter Bazalgette per R3 (càrrec de CEO vacant del 30/6/2017 al 8/1/2018; l'emissor declara que no es va respectar la separació Chairman/CEO i l'inclou a la taula de remuneració del Chief Executive). No s'aplica R2 (una sola font B, Variety). Ian Griffiths no era CEO. Marca `ceo_president_exec`, robustesa sense R3. FounderCEO=0 (prova d).
- Richemont CH0210483332 2017: no es reobre la decisió del 12/11/2026. NA per R-SC a l'anàlisi principal; Rupert=1 només a la robustesa R3.
- Abast de les marques de la regla 25: cada marca va a les files on la classificació depèn d'aquell criteri, a la columna multivalor `marques_fundador`, i s'aplica a tota la base. Robusteses calculades per script a partir de les marques: `founderceo_rob_regla25_nd` (totes les files marcades per la regla 25 com a ND, la principal per al tribunal) i, on hi hagi prou files, les separades per criteri (P1/P2, P3, P4, P6, P7, P8). `conflicte_fonts`: robustesa amb el valor alternatiu de la font en conflicte. D37a, D37b i R2b: columnes existents (`founderceo_rob_cita_contemporania`, sense `fundador_transformador`, `founderceo_rob_r2b_com_na`).
- Arkema FR0010313833: es manté a 1 (cas de referència de la D10b, 14/11/2026); la P4 hi és coherent. Només es comprova a la passada de la regla 25 que la cita A està arxivada; porta `fundador_escissio`.
- LVMH FR0000121014 2016-2025 i Sopra Steria FR0000050809 2025 (a la v0.10.9 constaven com a «pendents de comprovació de DF»): **resolts al PR #10** (merge `410b9a4bd16b2efe3f6df702524593d8d847c6b9`). LVMH: FounderCEO=1 per FT tipus c (decisió de Jordi X9-3); l'1 no ve de la D37, i per tant no s'hi aplica la regla 26. Sopra Steria 2025: es manté ND amb la marca `dubte_D1`, perquè ni la b ni la d tanquen contra la part on era el CEO.

Aquest text no autoritza a canviar `dades/` ni les robusteses en el mateix PR que només documenta les instruccions. Qualsevol aplicació a la base va en un lot a part, amb cita, registre i el flux DF → Doctorat → Jordi.

Ampliació de la regla 27 a la METODOLOGIA v0.10.10 (text literal; l'ITV 2017 ja és aplicada a `main`, `ceos`=Peter Bazalgette [V]):

- Resultats de DF (21/11/2026, `INFORME_PR_pas3_v3.md`, segons DF; cites marcades [V] per DF, no rellegides per Doctorat):
  - B&M 2016-2021: no hi ha cap cita contemporània que anomeni Arora fundador (AR 2016-2021 i fullet IPO del 12/6/2014). «founder-led… since the Group was acquired by the Aroras in December 2004» (fullet, p. 51) no compta (P6). Queda 1 per D37 (cita del 2024), `fundador_transformador`=1 i `founderceo_rob_cita_contemporania`=0 als anys 2016-2021.
  - LVMH 2016-2025: l'1 ve d'un FT validat de tipus c (decisió de Jordi X9-3, 15/11/2026), no de D37 ni de D1. Es manté a 1 i es retira la proposta 1→0. La regla 26 no hi aplica (Arnault no era a cap de les parts del 1987).
  - Sopra Steria 2025: CEO a 31/10/2025 Xavier Pecquet (nomenat el 8/10/2025), director de Sopra Group Holding Ltd des del 7/7/2005, sense vincle amb Steria. Amb `dubte_D1`, es prova contra Sopra (fundada el 1968). ND provisional: abans de tancar-la, prova b amb el mes i l'any de naixement de Companies House i prova a per P8 si l'emissor dona la llista de fundadors del 1968. ND només després d'una cerca exhaustiva i documentada.
  - ITV 2017: Bazalgette per R3 amb cites A de l'AR 2017 (p. 61, Executive Chairman fins al nou Chief Executive i incompliment de la A.2.1; p. 93, taula del Chief Executive). Pendent d'aplicar al PR.

## Regles 28 i 29 (METODOLOGIA v0.10.10)

Font: `METODOLOGIA_3_Articles_v0.10.10.md` (secció 2.3, regles 28 i 29, i annex A.4 corregit), SHA-256 `61112829dce1cbcebafc5ebcf9e04eb738566934369931cec597aeac2e14ec07`, comprovat el 21/11/2026. Decisions de Jordi del 21/11/2026 a les 10:23 Europe/Madrid (segons DF). Text literal:

- Regla 28. **Cobertura del CEO per interval [Jordi, 21/11/2026 10:23, segons DF].** Si no hi ha cap document de l'emissor o del regulador del mateix exercici que anomeni el CEO, la identitat del CEO a 31/10/t es pot acreditar amb un interval de dos extrems documentats amb font A/B: el nomenament (data igual o anterior al 31/10/t) i un document posterior que anomeni la persona com a CEO en una data igual o posterior al 31/10/t (no n'hi ha prou que el document sigui posterior). Marca `ceo_interval`, recompte al PR i robustesa `founderceo_rob_sense_interval` (les files amb `ceo_interval` com a ND). No s'exigeix comprovar l'absència de sortides o successions entre els dos extrems (Jordi: l'evidència no es trobarà); queda com a limitació declarada de la base: «a les files amb `ceo_interval` no s'ha verificat l'absència de canvis de CEO entre els dos extrems». Si es troba una sortida o successió entremig, l'interval no val i s'aplica R1-R3.

- Regla 29. **Límit de cerca com a triatge als lots `fora_mostra_auditoria` [Jordi, 21/11/2026 10:23, segons DF].** En aquests lots l'agent mira, per fila, l'informe anual de l'any, el de l'any següent i el web d'inversors de l'emissor. Si no hi troba font A/B, la fila va a la taula de dubtes amb el que s'ha mirat i no se'n canvia l'etiqueta. El límit és només de primera passada: una fila en dubte no compta com a feta ni com a verificada, i passa a la cua de casos oberts (`PENDENTS.md`), on s'aplica la cerca sense límit d'intents (A.4) abans de la base final. Als casos oberts (ND, `ceo_pendent`, `no_certificada`) no hi ha límit.

- A.4 Regla d'exclusió per manca de documentació (Jordi, 17/11, segons DF; corregida a la v0.10.10 amb la decisió de Jordi del 19/11, segons DF, que rebutja el límit de tres intents). Les files que, després d'una cerca exhaustiva i documentada (script, IA i manual), sense límit d'intents, no tinguin ni font de CEO ni font de prova surten de la mostra principal. El límit de la regla 29 és només de triatge i no és motiu d'exclusió. Queden registrades amb motiu, es desglossen per F/P, any i sector i es fa una robustesa que les inclou. Justificació [C]: evita una exclusió cas a cas i permet avaluar el biaix de selecció si les mancances es concentren en un grup.

La robustesa `founderceo_rob_sense_interval` és una columna de `dades/`: la calcula DF per script a partir de la marca `ceo_interval`; l'agent no la toca.

## Metodologia vigent

La metodologia vigent per a aquest treball és només la del repositori: aquestes instruccions (`AGENTS.md` / `CLAUDE.md`, amb el mateix contingut normatiu) i els documents del repositori als quals remeten. No la busquis a Google Drive, Gmail, Slack ni cap altra font. Si hi trobes versions antigues de la metodologia (per exemple, al Drive), no s'apliquen.

## Nota sobre la certificació

Les propostes de Claude no compten com a tercer model a cegues. El que certifica és la cita A/B verificada per script, dins el flux.

## El que aquestes instruccions no autoritzen

No pots canviar la metodologia, ni tocar els fitxers protegits (llevat de l'excepció de la secció 8), ni fusionar a `main`. L'extensió del sector del juny 2023 als anys 2024-2025 ja està aplicada a la v8 r3 per als ISIN que tenien aquesta font; les 48 empreses només presents el 2024-2025 i les 24 no casades queden pendents (font A, per exemple un informe anual amb la classificació ICB) i no s'inventa cap sector.

## Historial

El contingut normatiu d'aquest fitxer coincideix amb el de `CLAUDE.md` (aprovat per Jordi el 19/11/2026 i actualitzat el 20/11/2026 a les 11:56 Europe/Madrid amb la regla 25 de la METODOLOGIA v0.10.8, els 6 ND i la regla de Wayback amb `id_`, i el 20/11/2026 a les 13:10 Europe/Madrid amb la revisió de les fonts antigues del lot, i el 20/11/2026 a les 17:18 Europe/Madrid amb les regles 26 i 27 de la METODOLOGIA v0.10.9 i la norma de metodologia vigent), adaptat a qualsevol agent (Codex, Claude Code o un altre).

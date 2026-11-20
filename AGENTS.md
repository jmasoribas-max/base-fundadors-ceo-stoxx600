# Instruccions per a l'agent

El contingut normatiu d'aquest fitxer coincideix amb el de `CLAUDE.md` (aprovat per Jordi el 19/11/2026 i actualitzat el 20/11/2026 a les 11:56 Europe/Madrid amb la regla 25 de la METODOLOGIA v0.10.8, els 6 ND i la regla de Wayback amb `id_`, i el 20/11/2026 a les 13:10 Europe/Madrid amb la revisió de les fonts antigues del lot, i el 20/11/2026 a les 17:18 Europe/Madrid amb les regles 26 i 27 de la METODOLOGIA v0.10.9 i la norma de metodologia vigent), adaptat a qualsevol agent (Codex, Claude Code o un altre).

**Si `AGENTS.md` i `CLAUDE.md` discrepen, mana `CLAUDE.md`. L'agent ho ha d'anotar al PR.**

## Missió

Acabar la base de fundadors-CEO de l'STOXX Europe 600 (2016-2025, 1.040 empreses) i deixar-la correcta, amb una font que corrobori cada dada. No n'hi ha prou de revisar: s'ha de buscar la informació que falta, corregir errors i resoldre els casos oberts. Per a cada empresa i any: el CEO i si és fundador (1/0), amb una cita literal d'una font fiable.

La base oficial d'aquest repositori és `dades/base_isin_any_v8r3.csv`.

## Ordre de treball

Segueix aquest ordre (detall a `PENDENTS.md`):

1. **Casos oberts:** 6 ND (les que queden després del lot ND-1: Drillisch 2017, Sopra Steria 2025 i Aroundtown 2017-2020), 108 `certificada_ceo_pendent`, 241 `no_certificada`, i els casos clau (LVMH, BE Semiconductor, Aberdeen 2016, Anders Dam). Busca fins que trobis la font. Si després d'una cerca exhaustiva i documentada no hi ha cap font A/B, la fila queda indeterminada i a la fitxa s'explica què s'ha buscat i on. Cap límit d'intents.
2. **Les 3.890 files sense auditar** (`sim_estat_certificacio=fora_mostra_auditoria`; recompte comprovat a la base v8 r3 del `main` actual: **3.890** [V]). Verifica el CEO i l'etiqueta empresa per empresa i afegeix les cites que faltin. Si el recompte no quadrés en una versió futura, posa-hi la xifra real.
3. **Fitxes completes:** el CEO de cada any amb cita, la prova de fundador o de no fundador, el sector i les fonts amb Wayback.
4. **Errors:** si una dada contradiu la base, encara que estigui certificada, proposa'n la correcció amb la cita.

## Com treballar

- Només fonts de nivell **A** (documents de la mateixa empresa o registres oficials) i **B** (premsa econòmica de qualitat, llibres, articles acadèmics).
- Wikipedia, LinkedIn, Crunchbase, pàgines d'alumni, biografies no corporatives i textos d'IA són fonts **C**: serveixen de pista, mai de prova. Una font C mai no verifica, ni sola ni amb altres fonts C.
- Un `0` (no fundador) necessita una **prova positiva amb cita**. Si no hi ha proves que sigui fundador, és **indeterminat**, no `0`. No forcis un 0 ni un 1.
- Cada evidència porta una **cita literal**, l'**URL original** i el **Wayback**. Si no hi ha Wayback, declara-ho (`pendent_verificacio_externa` o equivalent) i no l'inventis.
- Per verificar una cita en un **PDF** arxivat a Wayback Machine, cal obrir el document de la captura, no l'embolcall HTML. Si la URL de la forma `https://web.archive.org/web/{timestamp}/{url}` retorna una pàgina HTML (barra de Wayback) i no el PDF, s'ha d'usar el modificador públic `id_`: `https://web.archive.org/web/{timestamp}id_/{url}`, que serveix els bytes originals de la captura. Això no és un bypass d'accés: és la forma de recuperar el fitxer arxivat. La cita s'ha de rellegir al document (per exemple amb `pdftotext`). Si, també amb `id_`, la captura no és el document, es declara `pendent_verificacio_externa` i no s'inventa. No s'usa `curl -k` ni s'omet la verificació del certificat TLS.
- Les fonts i cites que ja hi ha a la fitxa o al registre per a les files del lot no es donen per bones: s'han d'obrir i comprovar que la cita hi és literalment, que la font és A/B i que cobreix l'any. Si una no és vàlida (enllaç mort, font C, cita que no hi surt o d'un altre any), es marca com a no vàlida al registre, s'explica per què i se'n busca una alternativa A/B. No s'esborra mai la font antiga: es deixa marcada.
- No inventis dades, hashes, dates, càrrecs ni classificacions.
- La data de referència del CEO és el **31/10 de cada any** i no es pot canviar.
- Un 403, un temps d'espera esgotat, un captcha o una pàgina de bloqueig no són evidència. La cita ha de ser al document obert, no a un resum ni de memòria.

### Branques, lots i PR

Treballa per **lots d'empreses en branques** i obre **un PR per lot**.

**No toquis mai** `main`, `scripts/`, `docs/METODOLOGIA.md`, `CLAUDE.md`, `AGENTS.md`, les regles, `.github/` ni `.claude/`.

No pots fer commit ni push a `main`, ni fusionar un PR, ni esmenar, rebasejar o forçar `main`.

El flux, un cop obert el PR, és aquest i no un altre:

1. **DF** valida (format, comptes, `scripts/valida_pr.py`, coherència).
2. **Doctorat** revisa la metodologia.
3. **Jordi** aprova.

La configuració de la protecció de `main` (PR obligatori, aprovació de Jordi, cap push directe, CODEOWNERS) és a `docs/PROTECCIO_BRANCA_MAIN.md`.

### Com començar un lot

1. Crea una branca amb un nom descriptiu a partir de `main` (`fix/...`, `cas/...`, `sector/...`).
2. Agafa la primera tasca oberta seguint l'ordre de `PENDENTS.md`.
3. Llegeix la fitxa (`empreses/{ISIN}.md`), les files a `dades/base_isin_any_v8r3.csv`, `docs/REGISTRE_CANVIS.md` i `docs/METODOLOGIA.md`.
4. Cada canvi de dades ha de deixar, a la fitxa i al `docs/REGISTRE_CANVIS`, la cita literal, l'URL i el Wayback.
5. A la branca, qualsevol canvi a `dades/` ha d'anar acompanyat del canvi a les fitxes afectades i al registre. No toquis les dades a `main`.
6. Executa en local, **sense `--live`**:
   - `python3 scripts/valida_pr.py`
   - `python3 scripts/comprova_enllacos_cites.py`
7. **Cal que `scripts/valida_pr.py` passi abans d'obrir el PR.** Si falla, corregeix-ho abans.
8. Obre el PR amb un resum (què canvia, quins ISIN-any, quina regla, quines cites). No el fusionis.

### Format de les propostes de canvi

Cada proposta (al registre i, si cal, al cos del PR) ha de portar com a mínim:

- `isin` i `any` (o interval d'anys)
- valor actual i valor proposat de FounderCEO (o del camp que es modifica)
- regla aplicada (un sol valor, el més fort que s'aplica; vegeu `docs/METODOLOGIA.md` i, per als criteris del PR #6, la regla 25 més avall)
- nivell de font (A o B)
- cita literal
- URL original
- URL Wayback (o declaració de pendent)
- justificació breu, sense afegir fets que no siguin a la cita
- efecte esperat sobre la certificació (N1, N2, doctorat, ceo_pendent, no_certificada), sense autodeclarar-la tancada: la certificació queda dins el flux (DF, Doctorat, Jordi)

No proposis un canvi sense cita literal i URL.

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

## Metodologia vigent

La metodologia vigent per a aquest treball és només la del repositori: aquestes instruccions (`AGENTS.md` / `CLAUDE.md`, amb el mateix contingut normatiu) i els documents del repositori als quals remeten. No la busquis a Google Drive, Gmail, Slack ni cap altra font. Si hi trobes versions antigues de la metodologia (per exemple, al Drive), no s'apliquen.

## Nota sobre la certificació

Les propostes de l'agent no compten com a tercer model a cegues. El que certifica és la cita A/B verificada per script, dins el flux.

## El que aquestes instruccions no autoritzen

No pots canviar la metodologia, ni tocar els fitxers protegits, ni fusionar a `main`. L'extensió del sector del juny 2023 als anys 2024-2025 ja està aplicada a la v8 r3 per als ISIN que tenien aquesta font; les 48 empreses només presents el 2024-2025 i les 24 no casades queden pendents (font A, per exemple un informe anual amb la classificació ICB) i no s'inventa cap sector.

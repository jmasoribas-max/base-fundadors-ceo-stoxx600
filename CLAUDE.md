# Instruccions per a Claude Code

**Aprovat per Jordi el 19/11/2026.**

## Missió

Acabar la base de fundadors-CEO de l'STOXX Europe 600 (2016-2025, 1.040 empreses) i deixar-la correcta, amb una font que corrobori cada dada. No n'hi ha prou de revisar: has de buscar la informació que falta, corregir errors i resoldre els casos oberts. Per a cada empresa i any: el CEO i si és fundador (1/0), amb una cita literal d'una font fiable.

La base oficial d'aquest repositori és `dades/base_isin_any_v8r3.csv`.

## Ordre de treball

Segueix aquest ordre (detall a `PENDENTS.md`):

1. **Casos oberts:** 14 ND, 108 `ceo_pendent`, 241 `no_certificada`, i els casos clau (LVMH, BE Semiconductor, Aberdeen 2016, Anders Dam). Busca fins que trobis la font. Si després d'una cerca exhaustiva i documentada no hi ha cap font A/B, la fila queda indeterminada i a la fitxa s'explica què s'ha buscat i on. Cap límit d'intents.
2. **Les 3.890 files sense auditar** (`sim_estat_certificacio=fora_mostra_auditoria`; recompte comprovat a la base v8 r3: **3.890** [V]). Verifica el CEO i l'etiqueta empresa per empresa i afegeix les cites que faltin. Si el recompte no quadrés en una versió futura, posa-hi la xifra real.
3. **Fitxes completes:** el CEO de cada any amb cita, la prova de fundador o de no fundador, el sector i les fonts amb Wayback.
4. **Errors:** si una dada contradiu la base, encara que estigui certificada, proposa'n la correcció amb la cita.

## Com treballar

- Només fonts de nivell **A** (documents de la mateixa empresa o registres oficials) i **B** (premsa econòmica de qualitat, llibres, articles acadèmics).
- Wikipedia, LinkedIn, Crunchbase, pàgines d'alumni, biografies no corporatives i textos d'IA són fonts **C**: serveixen de pista, mai de prova. Una font C mai no verifica, ni sola ni amb altres fonts C.
- Un `0` (no fundador) necessita una **prova positiva amb cita**. Si no hi ha proves que sigui fundador, és **indeterminat**, no `0`. No forcis un 0 ni un 1.
- Cada evidència porta una **cita literal**, l'**URL original** i el **Wayback**. Si no hi ha Wayback, declara-ho (`pendent_verificacio_externa` o equivalent) i no l'inventis.
- No inventis dades, hashes, dates, càrrecs ni classificacions.
- La data de referència del CEO és el **31/10 de cada any** i no es pot canviar.
- Un 403, un temps d'espera esgotat, un captcha o una pàgina de bloqueig no són evidència. La cita ha de ser al document obert, no a un resum ni de memòria.

### Branques, lots i PR

Treballa per **lots d'empreses en branques** i obre **un PR per lot**.

**No toquis mai** `main`, `scripts/`, `docs/METODOLOGIA.md`, `CLAUDE.md`, les regles ni `.github/`.

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
- regla aplicada (un sol valor, el més fort que s'aplica; vegeu `docs/METODOLOGIA.md`)
- nivell de font (A o B)
- cita literal
- URL original
- URL Wayback (o declaració de pendent)
- justificació breu, sense afegir fets que no siguin a la cita
- efecte esperat sobre la certificació (N1, N2, doctorat, ceo_pendent, no_certificada), sense autodeclarar-la tancada: la certificació queda dins el flux (DF, Doctorat, Jordi)

No proposis un canvi sense cita literal i URL.

## Nota sobre la certificació

Les propostes de Claude no compten com a tercer model a cegues. El que certifica és la cita A/B verificada per script, dins el flux.

## El que aquestes instruccions no autoritzen

No pots canviar la metodologia, ni tocar els fitxers protegits, ni fusionar a `main`. L'extensió del sector del juny 2023 als anys 2024-2025 ja està aplicada a la v8 r3 per als ISIN que tenien aquesta font; les 48 empreses només presents el 2024-2025 i les 24 no casades queden pendents (font A, per exemple un informe anual amb la classificació ICB) i no s'inventa cap sector.

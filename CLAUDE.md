# Instruccions per a Claude Code

> **Esborrany pendent de la revisió de Doctorat.** Aquest fitxer és una instrucció de treball. No el prenguis com a metodologia tancada fins que Doctorat l'hagi revisat.

Aquest repositori el farà servir Claude Code, amb accés al GitHub del titular. Pots llegir les fonts que ja hi ha al repositori (i les que un PR aporti), executar els scripts d'aquest arbre i fer commits **només en branques**.

## Regla absoluta: no toquis mai `main`

La branca `main` està protegida. **Claude no la pot tocar mai.**

No pots:

- fer commit a `main`
- fer push a `main`
- fusionar un pull request
- esmenar, rebasejar o forçar `main`
- editar fitxers directament a la branca principal

Només pots:

- crear una branca a partir de `main`
- treballar i fer-hi commits
- executar els scripts en local
- obrir un pull request amb un resum

El flux, un cop obert el PR, és aquest i no un altre:

1. **DF** valida (format, comptes, `scripts/valida_pr.py`, coherència amb la base i les fitxes).
2. **Doctorat** revisa la metodologia.
3. **Jordi** aprova i fusiona.

No avancis un PR a «fusionable» ni demanis a ningú que el fusioni en nom teu. Les instruccions per configurar la protecció de `main` (PR obligatori, aprovació de Jordi i cap push directe) són a `docs/PROTECCIO_BRANCA_MAIN.md`.

## Com començar a treballar

1. Crea una branca amb un nom descriptiu (`fix/...`, `sector/...`, `cita/...`). No treballis mai a `main`.
2. Agafa la primera tasca oberta seguint l'**ordre de prioritats** de `PENDENTS.md` (secció «Ordre de treball»). No comencis una tasca de prioritat inferior si n'hi ha de superiors encara obertes, tret que el PR o Jordi ho indiquin.
3. Llegeix la fitxa de l'empresa (`empreses/{ISIN}.md`), les files corresponents a `dades/base_isin_any_v8r2.csv`, el `docs/REGISTRE_CANVIS.md` i `docs/METODOLOGIA.md`.
4. Treballa només amb fonts de nivell A o B (vegeu més avall).
5. Cada canvi de dades ha de deixar, a la fitxa i al `docs/REGISTRE_CANVIS`, la **cita literal**, l'**URL original** i el **Wayback**. Si no hi ha Wayback, declara-ho (`pendent_verificacio_externa` o equivalent) i no l'inventis.
6. No toquis les dades a `main`. A la branca, qualsevol canvi a `dades/` ha d'anar acompanyat del canvi a les fitxes afectades i al registre.
7. Executa en local, **sense `--live`**:
   - `python3 scripts/valida_pr.py`
   - `python3 scripts/comprova_enllacos_cites.py`
8. Si el validador falla, corregeix-ho abans d'obrir el PR. **Cal que `scripts/valida_pr.py` passi abans d'obrir el PR.**
9. Obre el PR amb un resum (què canvia, quins ISIN-any, quina regla, quines cites). No el fusionis.

## Fonts i cites

- Només fonts de nivell **A** (documents de la mateixa empresa o registres oficials) o **B** (tercers fiables: premsa econòmica de qualitat, obres de referència, llibres, articles acadèmics).
- Una font de nivell C (agregadors, blogs, premsa local sense font, enciclopèdies obertes) **mai no verifica**. Només pot servir de pista.
- La cita ha de ser **literal** i ha de ser al document obert, no a un resum ni de memòria. Un 403, un temps d'espera esgotat, un captcha o una pàgina de bloqueig no són evidència.
- Cada cita porta l'URL original i l'URL de Wayback. Si no hi ha captura, queda pendent; no n'inventis cap.
- No inventis dades, hashes, dates, càrrecs ni classificacions.
- Si no es pot determinar, deixa-ho **indeterminat** i explica el dubte. No forcis un 0 ni un 1.

## Format de les propostes de canvi

Cada proposta (al registre i, si cal, al cos del PR) ha de portar com a mínim:

- `isin` i `any` (o interval d'anys)
- valor actual i valor proposat de FounderCEO (o del camp que es modifica)
- regla aplicada (un sol valor, el més fort que s'aplica; vegeu `docs/METODOLOGIA.md`)
- nivell de font (A o B)
- cita literal
- URL original
- URL Wayback (o declaració de pendent)
- justificació breu, sense afegir fets que no siguin a la cita
- efecte esperat sobre la certificació (N1, N2, doctorat, ceo_pendent, no_certificada), sense autodeclarar-la tancada: la certificació la tanquen DF, Doctorat i Jordi segons el flux

No proposis un canvi sense cita literal i URL.

## Scripts

- `scripts/valida_pr.py`: format de les fitxes i de l'índex, valors permesos, cites literals, coherència amb la base, enllaços interns, i (en un PR) que els canvis a `dades/` portin registre i fitxes. S'ha d'executar abans d'obrir el PR. Sense `--live` per defecte.
- `scripts/comprova_enllacos_cites.py`: forma de les URL i de les cites del registre i de les fitxes. Sense `--live` per defecte. No executis `--live` si no t'ho demanen explícitament.

## El que aquest fitxer no fa

Aquestes instruccions no autoritzen a canviar la metodologia, a estendre el sector de 2023 a 2024-2025, ni a tancar casos que `PENDENTS.md` reserva a Doctorat.

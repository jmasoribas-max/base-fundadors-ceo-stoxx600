# Diari de treball de Claude

Registre de tot el que fa Claude a la base de fundadors-CEO, perquè no es perdi res. Les entrades no s'esborren: només s'hi afegeixen línies. Cada entrada diu què s'ha fet, amb quins fitxers i commits, quins resultats, què queda obert i quin és el pas següent. Les dates són Europe/Madrid.

- **Branca de treball de Claude:** `claude/charming-mayer-ejb9ek` (no és `main`; cap PR obert encara).
- **Estat de la base:** el comptador és a [`estat/RESUM_ESTAT.md`](../estat/RESUM_ESTAT.md) (`python3 estat/estat_files.py`).

## Estat ràpid (s'actualitza a cada sessió)

| | Valor |
|---|---|
| Última actualització | 23/11/2026 |
| `main` de referència | `17b03df` (PR #20) |
| Files acabades (4 condicions) | 278 de 6.012 (4,6 %) |
| Files amb evidència de CEO i de fundador (C1 i C2) | 4.162 de 6.012 (69,2 %) |
| Files F amb C1 i C2 | 99 de 349 (lot 11) |
| Fase del pla | Fase 0 feta. Lot de correcció 1 preparat (no aplicat). Fase 1 en curs: lot 11 (F) aplicat a la branca; queda la cerca nova de CEO per a 232 files F |
| Pendent de Jordi | Fusionar el PR #21 (accés; revisat per Claude, correcte); decisions 4-10 de DF (sessió 5); OK per obrir el PR de la branca |
| Flux nou | Claude prepara, valida (scripts i comprovació independent per mostra) i obre els PR; Jordi aprova i fusiona. DF queda fora (document final per a DF quan s'acabi) |

## Decisions i indicacions de Jordi rebudes

| Data | Indicació (paraules de Jordi, resumides) |
|---|---|
| 23/11/2026 | Claude es fa càrrec de la base. Primer, auditoria de l'estat i llista de tasques pendents. |
| 23/11/2026 | Abast: només cal l'evidència de **qui era el CEO** cada any i de **si era el fundador** (amb el fundador quan l'empresa en té, o les proves de la metodologia per descartar-ho), guardada i arxivada. Hereus, episodis de CEO i altres variables són extres i queden fora. La validació humana la farà Jordi quan la base estigui ben feta. |
| 23/11/2026 | Les preguntes sobre on és cada cosa (Wayback, sortides de l'auditoria, etc.) les farà Jordi a Grok i passarà la resposta. |
| 23/11/2026 | OK per començar l'script d'estat per fila. |
| 23/11/2026 | Cal deixar anotat tot el que es fa en un document per tenir-ho controlat (aquest diari). |
| 23/11/2026 | Nom del fundador: **sí** a la proposta. Es desa quan l'evidència el dona (totes les F i les P resoltes per la prova a); no es fa cap cerca específica a les P resoltes per b, c, d o e. |
| 23/11/2026 | Claude porta la batuta de la base i ha de poder escriure a `scripts/` i `.github/`. Jordi farà el canvi de permisos i d'instruccions (vegeu la sessió 4). |
| 23/11/2026 | Sí a les decisions 1, 2 i 3 (CEO oficial, `regles`, criteris del PR #3). Detall a la sessió 6. DF pot configurar l'accés de Claude. |
| 23/11/2026 | Accés: Claude també ha de poder aplicar a `dades/` els lots de correcció que Jordi aprovi (s'inclou a la petició a DF). |
| 23/11/2026 | Claude té llibertat per vigilar els PR, crear una branca per lot i fer la feina proposada, sempre que tingui el control de tot i sigui correcte per a la base final amb evidència vàlida per al doctorat. |
| 23/11/2026 | **DF ja no porta res de la base: ho porta tot Claude.** En acabar, es passarà a DF un document amb tots els passos seguits fins a la base final, perquè n'estigui al cas. |
| 23/11/2026 | Punt 1 (permisos per editar `CLAUDE.md`, `AGENTS.md` i `docs/METODOLOGIA.md`): ho executarà Grok amb un prompt. Punt 3: sí a l'última entrega de DF (verificació Wayback). Punt 2: endavant amb el procés automàtic a GitHub per a Wayback. |
| 23/11/2026 | Fonts de LSEG, Bloomberg, LexisNexis i similars: tot el que és públic al web es pot fer servir, encara que provingui d'aquestes fonts. Mai no s'ha fet servir cap base de dades privada seva. Deixa sense efecte l'avís de la sessió 7. |

## Entrades

### 23/11/2026 · Sessió 1 · Auditoria de l'estat de la base

- **Què s'ha fet:** lectura del document de traspàs i de la metodologia v0.10.10; recomptes propis sobre `main` `17b03df` (CSV oficial, registre de 11.582 entrades, `PENDENTS.md`, fitxes, lots, scripts); comprovació independent per mostra de 87 cites del registre (re-descàrrega del document original i cerca literal).
- **Fitxers:** [`docs/AUDITORIA_ESTAT_BASE_20261123.md`](AUDITORIA_ESTAT_BASE_20261123.md); scripts i resultat de la mostra a `docs/auditoria_20261123/`.
- **Commit:** `ef33f28`.
- **Resultats principals:**
  - Panell 6.012 files / 1.040 ISIN; F 349, P 5.631, NA 31, ND 1. SHA del CSV i del registre iguals que al traspàs.
  - Mostra: de 72 documents oberts, 71 contenen la cita (68 literals, 1 gairebé, 2 de cel·les de taula) i 1 no és concloent; cap cita inventada. 15 documents no es van poder obrir des de l'entorn.
  - F completes: 44 de 349. Les 1.773 files «certificades» no tenen cap cita de CEO al registre (la prova és a les sortides de l'auditoria IA, fora del repositori).
  - Wayback: només 744 entrades amb la cita verificada a la captura.
  - Incoherències al CSV: Enagás 2016-2021, Bellway 2017, BME 2017-2018, Cellnex 2016-2022, AB InBev, Harbour, P sense prova a `regles`.
- **Correcció al traspàs:** `main` ja no és `fa8f90d` sinó `17b03df` (PR #20, dashboard, fusionat el 23/11 a les 14:00); les dades no han canviat.

### 23/11/2026 · Sessió 2 · Pla per finalitzar i preguntes per a Grok

- **Què s'ha fet:** definició de «fila acabada» amb l'abast fixat per Jordi; pla en sis fases; 19 preguntes per a Grok (sortides r3e/r4, inventari antic de fonts, Wayback, decisions no aplicades, organització).
- **Fitxers:** [`docs/PLA_FINALITZACIO_20261123.md`](PLA_FINALITZACIO_20261123.md).
- **Commit:** `0d1c59c`.
- **Obert:** respostes de Grok; decisió de Jordi sobre desar el nom del fundador quan l'evidència el dona (F i prova a) i no fer-ne una cerca específica a les P resoltes per b, c, d o e.

### 23/11/2026 · Sessió 3 · Script d'estat per fila (tasca 0.2 del pla)

- **Què s'ha fet:** script que comprova les quatre condicions (CEO, fundador, arxiu, coherència) per a cada fila i genera el resum. Mode `--comprova` per al CI. Fitxer `dubtes_tancats.csv` (buit) per anar tancant dubtes de `PENDENTS.md` sense esborrar-los.
- **Fitxers:** [`estat/estat_files.py`](../estat/estat_files.py), [`estat/estat_files.csv`](../estat/estat_files.csv), [`estat/RESUM_ESTAT.md`](../estat/RESUM_ESTAT.md), [`estat/dubtes_tancats.csv`](../estat/dubtes_tancats.csv), [`estat/README.md`](../estat/README.md).
- **Commit:** `0d2573a`.
- **Per què a `estat/` i no a `scripts/`:** `.claude/settings.json` no permet a l'agent escriure a `scripts/` ni a `.github/`. No s'ha saltat aquesta protecció. Jordi pot moure l'script o afegir-lo al CI.
- **Resultats (línia de base):** 278 files acabades (4,6 %); 4.107 amb evidència de CEO i de fundador; 1.856 sense cita de CEO (302 F); 1.283 sense cita de fundador (138 F); 51 files incoherents; 264 amb dubte obert; 5.733 sense arxiu verificat. Empreses F completes en evidència: 9 de 88.
- **Diferències amb l'auditoria:** C1 dona 4.129 `ok` (l'auditoria en donava 4.097) perquè ara es reconeixen els cognoms compostos (p. ex. «Jaime García-Legaz»); s'han revisat 15 exemples i són correctes. Les NA amb documentació són 27 (l'auditoria només comptava cites de CEO o fundador; ara també compten les de context).
- **Troballa nova:** les 37 P sense prova de «no» a `regles` són gairebé totes antigues ND que Doctorat va passar a 0; la regla aplicada és a `sim_nota` (p. ex. «AB InBev: ND passa a 0, regla b») però `regles` no es va actualitzar. Va al lot de coherència (tasca 1.3).
- **Pendent de Jordi:** afegir al CI (`.github/workflows/valida_pr.yml`) el pas:

  ```yaml
        - name: Estat per fila al dia (sense xarxa)
          run: python3 estat/estat_files.py --comprova
  ```

- **Pas següent:** quan arribin les respostes de Grok, fase 1 (recuperar les cites de l'auditoria r3e/r4 i de l'inventari antic). Mentrestant es pot preparar la tasca 0.3 (camps mínims del registre) o el lot de coherència 1.3, si Jordi ho vol.

### 23/11/2026 · Sessió 4 · Accés a `scripts/` i `.github/`

- **Què s'ha demanat:** Jordi vol que Claude pugui escriure a `scripts/` i `.github/`.
- **Per què Claude no ho pot fer sol:** el bloqueig és a `.claude/settings.json` (regles `deny`) i a `CLAUDE.md` / `AGENTS.md` (§8, «No toquis mai…»). Aquests fitxers també estan protegits contra l'agent, i Claude no se salta aquesta protecció. El canvi l'ha de fer Jordi a GitHub, amb un PR que ell mateix fusiona.
- **Canvi proposat (mínim):**
  - `.claude/settings.json`: treure només `Edit(/scripts/**)` i `Edit(/.github/**)`. Es mantenen els bloquejos de push a `main`, de fusió i d'edició de `docs/METODOLOGIA.md`, `CLAUDE.md`, `docs/REGLES*` i `.claude/`.
  - `CLAUDE.md` i `AGENTS.md`, línia 94: treure `scripts/` i `.github/` de la llista «No toquis mai» i afegir que Claude, com a coordinador de la base, els pot modificar en una branca i per PR que Jordi aprova i fusiona.
- **Quan Jordi ho hagi fusionat:** Claude fusiona `main` a la seva branca, afegeix el pas de l'script d'estat al CI, actualitza les frases de `README.md` i `docs/PROTECCIO_BRANCA_MAIN.md` que diuen que Claude no toca `scripts/` ni `.github/`, i ho anota aquí. Pot caldre obrir una sessió nova perquè el canvi de permisos tingui efecte.

### 23/11/2026 · Sessió 5 · Respostes de DF a les 19 preguntes

- **Què s'ha rebut:** `RESPOSTES_19_PREGUNTES_CLAUDE.md`, de DF (via Jordi). No s'ha copiat al repositori; aquí en queda el resum operatiu.
- **On és cada cosa (resum):**
  - Sortides r3e (Drive `1jwCn3Eev6Ni5McBp1jEpQnEjpBQj8j61`): `SORTIDA_chatgpt_COMPLET.jsonl` (`1cMhGnfZlw3EcaTic-agFu5Ntrd_oD-Fs`) i `SORTIDA_claude_COMPLET.jsonl` (`1iOkn2Hz08Yq_7Dboxgkh2teiVZYRvrew`). Una cita de classificació per fila; el CEO només a `justificacio`.
  - Sortides r4 (Drive `1ic68PNoqKOXURIpE7-MzQES4Zaj0BP2o`): `SORTIDA_chatgpt_COMPLETACIO.jsonl` (`12PYpFI4UPkNWQoFACsKjBwtyyM4GokhP`) i `SORTIDA_claude_COMPLETACIO.jsonl` (`1snomzCW0Ar8nYYfXnc2fgpud6289v19A`). Cites del CEO a `ceo_31_10.evidencies[]`; lligam per `id_fila` = `sim_id_fila_r4` de la base.
  - Registres de verificació de la certificació (només al box): `CERTIFICACIO_parella_any_r3e.csv` i `MANIFEST_evidencies_web_r4.csv` (Claude 3.768 evidències, 2.708 verificades; ChatGPT 2.481, 946 verificades).
  - Inventari antic: `fonts_v75r2.csv` (box i Drive `1Ze-INmZqhA07lp7y-PjaCZ9kI4QT8kE1`, 8.310 fonts). Extractes al Drive, carpeta `15zme4Bygi5mCC5SqZWbTyN4VM8_XHR9A` (8.472 fitxers).
  - Wayback: arxivament acabat el 22/11 (`wayback_resultats_20261122.csv`, 4.550 URL); verificació en curs al box (`verificacio_cites_20261122.csv`). Lots 9 i 10 fora; lots 6-8 gairebé sense captura.
- **Comprovacions de Claude:**
  - Accés de lectura al Drive confirmat (metadades de 3 fitxers; 3-6,5 MB cadascun). No es poden llegir sencers pel connector (el contingut arribaria íntegre a la conversa), per això es demanen a DF en una branca.
  - **GitHub Pages és actiu** (https://jmasoribas-max.github.io/base-fundadors-ceo-stoxx600/, HTTP 200). La branca `gh-pages` la va publicar el compte de Jordi el 23/11 a les 14:00 (commit `64ce9cc`). `dashboard/README.md` encara diu que no està publicat: cal corregir-ho.
  - **«Proves de LSEG i Bloomberg»:** són 47 entrades amb URL de comunicats regulats RNS (`rns-pdf.londonstockexchange.com`), informes anuals de la mateixa LSEG (que és a la mostra, `GB00B0SWJX34`) i `assets.lsegissuerservices.com`, més articles de premsa de Bloomberg. Són documents públics, no dades amb llicència (Datastream, Workspace o el terminal de Bloomberg). Lectura de Claude [C]: no afecta l'A.5.
- **Fet en aquesta sessió:** `estat/llista_urls_arxiu.py` i `estat/urls_per_arxivar.csv`: 6.579 URL del registre sense la cita verificada a la captura (5.559 sense `url_wayback`). Pla actualitzat (secció 7). Commit: vegeu `git log` d'aquesta data.
- **Fitxers que cal demanar a DF** (a una branca del repositori, p. ex. `df/fitxers-per-claude`, carpeta `entrada_claude/`):
  1. Les 4 sortides JSONL (r3e i r4, ChatGPT i Claude).
  2. `CERTIFICACIO_parella_any_r3e.csv` i els dos `MANIFEST_evidencies_web_r4.csv`.
  3. `fonts_v75r2.csv`.
  4. `wayback_resultats_20261122.csv` i, quan acabi, `verificacio_cites_20261122.csv`.
  5. Opcional, més endavant: els extractes X6 en un zip.
  - No cal `MAPA_FILES_r4_NO_PER_A_IA.csv` (la base ja té `sim_id_fila_r4`) ni les evidències web en brut (9,7 GB).
- **Decisions pendents de Jordi:** les 10 de DF, amb la recomanació de Claude al missatge del 23/11 (resumides a l'estat ràpid quan es resolguin).

### 23/11/2026 · Sessió 6 · Decisions 1-3 i lot de correcció 1 (preparat, no aplicat)

- **Decisions de Jordi (23/11/2026):** sí a les tres recomanacions:
  1. Copiar `sim_ceo_aplicat` a `ceos` a les 7 files (Enagás 2016-2021, Bellway 2017).
  2. Corregir `regles` amb les decisions de Doctorat i revisar les P amb `cap`.
  3. Criteris del PR #3: (a) un document de l'emissor allotjat fora del seu domini (CDN, regulador, plataforma de comunicats) és font A si la cita és literal; (b) l'informe de l'exercici com a aproximació del 31/10 (D21); (c) una cita de CEO només de font B és vàlida (D4b); (d) la llista de mitjans B la proposa Claude i la valida Doctorat.
- Jordi ha enviat a DF el missatge per pujar els fitxers a una branca. També proposa que DF configuri l'accés de Claude a `scripts/` i `.github/`.
- **Fet:** lot de correcció 1 preparat (no aplicat): [`lots/correccio1_canvis.csv`](../lots/correccio1_canvis.csv) i [`lots/correccio1_README.md`](../lots/correccio1_README.md). 171 cel·les a 59 files: 7 `ceos`, 41 `regles`, 123 camps de motiu de ND en files que ja no són ND. Cap canvi de FounderCEO. Script reutilitzable [`estat/aplica_canvis.py`](../estat/aplica_canvis.py) (prova en sec per defecte; amb `--aplica` escriu CSV, xlsx, registre i fitxes).
- **Prova en una còpia separada (worktree, esborrada després):** l'aplicació canvia exactament 59 files del CSV, afegeix 59 entrades al registre i una secció a 19 fitxes; les incoherències passen de 51 a 3 (Knorr-Bremse 2019-2020 i Pandora 2018); `valida_pr.py` dona 0 problemes; si es torna a executar, l'script detecta que ja està aplicat.
- **Queden fora del lot:** Knorr-Bremse 2019-2020 i Pandora 2018 (R2b sense proves per a cada membre de la direcció interina) → dubte per a Doctorat i cerca.
- **Conseqüències dels criteris del PR #3:**
  - S'han d'incorporar a la metodologia (Doctorat, nova versió) i a `CLAUDE.md` / `AGENTS.md` (Jordi).
  - Dels 13 pendents del lot 9, Allreal 2019-2022 (4 files) es pot tancar amb el criteri (a); Sandoz, Bankia, Paysafe i EVRAZ continuen depenent d'altres criteris (cotització doble, P5, D37d, P6).
- **Troballa per a la tasca 0.3:** les 46 entrades `decisio_doctorat` i `decisio_doctorat_r4` del registre no tenen `funcio_cita`, i per això l'script d'estat no les compta com a evidència de fundador (p. ex. AB InBev). Cal normalitzar-les.
- **Pendent:** qui aplica els lots que toquen `dades/` (Claude o DF), segons el que decideixi Jordi sobre l'accés.

### 23/11/2026 · Sessió 7 · Fitxers de DF rebuts i primera anàlisi de la fase 1

- **Fitxers:** branca `df/fitxers-per-claude`, carpeta `entrada_claude/`, commit `34cff60` (main intacte, cap PR). Els 9 SHA-256 coincideixen amb el README de DF: 4 JSONL (r3e i r4, ChatGPT i Claude), `CERTIFICACIO_parella_any_r3e.csv`, els dos `MANIFEST_evidencies_web_r4.csv`, `fonts_v75r2.csv` i `wayback_resultats_20261122.csv`. `verificacio_cites_20261122.csv` arribarà quan acabi (DF ho revisa a partir de les 16:00).
- **Avís de DF sobre fonts de pagament:** 11 URL a `fonts_v75r2.csv` (LSEG, Bloomberg, LexisNexis; cites de 114 caràcters com a màxim) i 3 de Bloomberg al JSONL de Claude r4. En importar cites al registre s'han de revisar aquestes URL: no s'hi ha de copiar contingut de pagament més enllà d'una cita curta, i cal preferir una font oberta si n'hi ha.
- **Comprovació d'estructura:** cada evidència web de r4 lliga 1 a 1 amb el manifest de DF (3.768 de 3.768 a Claude); les evidències `paquet` porten URL; r3e té una cita de classificació per fila i model.
- **Fet:** [`traspas/candidates_auditoria.py`](../traspas/candidates_auditoria.py) genera les evidències candidates per fila (`traspas/candidates_evidencia.csv`, 15.425 cites per a 3.246 files; no es puja al repositori perquè es regenera) i el resum [`traspas/RESUM_CANDIDATES.md`](../traspas/RESUM_CANDIDATES.md). No modifica el registre.
- **Resultat:** de les 1.905 files que avui no tenen cita de CEO o de fundador, **839** quedarien amb totes dues només amb cites que els scripts de DF ja van trobar literalment al document. Per condició:
  - Sense CEO: 1.856 files; 1.307 amb candidata, 985 amb candidata ja verificada (F: 146 de 302).
  - Sense fundador: 1.283 files; 1.160 amb candidata, 978 amb candidata ja verificada (F: 134 de 138).
- **Límits d'aquesta anàlisi:** per al fundador encara no es comprova que la prova sigui completa per a la regla (p. ex. la b necessita any de fundació i any de naixement) en el cas de les cites de r3e i de l'inventari antic; per al CEO, encara no es comprova que el document sigui de l'exercici. Es farà en el pas d'importació.
- **Decisió de Jordi:** incloure a la petició d'accés l'opció que Claude pugui aplicar a `dades/` els lots de correcció que Jordi aprovi.
- **Pas següent:** lot d'importació F (les 88 empreses F), amb les cites verificades i, per a la resta, re-descàrrega i verificació pròpia.

### 23/11/2026 · Sessió 8 · Lot 11: importació del grup F

- **Lot 11** = les 349 files F (88 empreses): [`lots/lot11.csv`](../lots/lot11.csv).
- **Script:** [`traspas/importa_lot.py`](../traspas/importa_lot.py). Per a cada fila sense C1 o C2, tria la millor cita candidata:
  - CEO: la cita anomena el CEO i conté un títol de primer executiu.
  - Fundador (F): la cita anomena el CEO i conté un mot de fundació.
  - Prioritat: ja verificada per DF; després document de l'exercici; no agregador; nivell A.
  - Si no n'hi ha cap de verificada, Claude baixa l'original i hi busca la cita literal.
  - Escriu entrades al registre amb el format de `CLAUDE.md` §6 (`origen=proposta_claude_lot11`, identificadors `L11-{ISIN}-C01`/`F01`) i les afegeix a les fitxes.
- **Agregadors:** `annualreports.com` és la font més freqüent de les candidates. Només s'usa si no n'hi ha cap altra, amb la nota `agregador=true` per substituir-la per la còpia de l'emissor.
- **Prova en sec (sense baixades):** CEO 132 files amb cita ja verificada (170 sense); fundador 106 (32 sense).
- **En curs:** execució amb verificació pròpia en una còpia separada (worktree) per revisar-ne el resultat abans d'escriure al registre de la branca.
- **PR #21 (DF, branca `config/claude-coordinador`):** revisat per Claude. Fa exactament els canvis demanats: `.claude/settings.json` només treu `Edit(/scripts/**)` i `Edit(/.github/**)`; `CLAUDE.md` i `AGENTS.md` afegeixen l'excepció per a Claude (`scripts/`, `.github/` i els lots de correcció aprovats a `dades/`) i la referència a la línia 195. CI `valida` correcte. Detall cosmètic: `scripts/`, `.github/` i `dades/` dins l'excepció van sense accents greus. **Claude no el fusiona**: és decisió de Jordi (i `CLAUDE.md` i els permisos li ho impedeixen).
- **Refinament de l'importador abans d'escriure al registre** (després de revisar a mà dues proves en una còpia separada):
  - Les cites es retallen a la frase rellevant.
  - S'exclouen les expressions que la P6 no admet.
  - Per al CEO, només documents de l'exercici (CLAUDE.md §3) i cap frase de sortida.
  - Es rebutgen les cites on el cognom correspon a una altra persona (Aditya / Lakshmi Mittal) i les de fundador d'una altra entitat (fons de Rigas).
  - La marca de la regla ve del token que correspon a l'etiqueta.
- **Lot 11 aplicat a la branca:** 74 entrades noves al registre (66 [V], 8 [NV] `pendent_DF`; 17 amb `agregador=true`), cites afegides a 47 fitxes, cap canvi de FounderCEO ni de `ceos`. Grup F: cita de CEO 47 → 105 files; cita de fundador 211 → 292; totes dues 44 → 99. Resum a [`lots/lot11_README.md`](../lots/lot11_README.md).
- **Queda al grup F:** 232 files sense cita de CEO (66 empreses) i 57 sense cita de fundador (22 empreses): [`lots/lot11_pendents.csv`](../lots/lot11_pendents.csv). Cal una cerca nova amb l'informe anual de cada exercici.
- **Nota sobre els filtres de la P6 (pregunta de Jordi, 23/11/2026):** la P6 (regla 25) exclou literalment «founder-led», «founding CEO», «founding shareholder», «architect» i «creator» (aquests dos només per la via FT), i les cites de fundador d'una altra entitat. L'importador també exclou «founding member(s)», «founding partner», «founding chairman» i «founding director» **per analogia**: això no és al text de la P6 i ho ha de confirmar Doctorat o Jordi. Files F on el filtre va deixar fora la cita candidata: Cellnex 2016-2022 («CEO fundador»; ja és un dubte obert del lot 6), Energean 2023 («founding shareholder») i alstria 2019-2021 («founding members»). L'etiqueta no canvia; aquestes files queden pendents d'una altra font o del criteri de Doctorat.

### 23/11/2026 · Sessió 9 · PR #21 fusionat i primer PR de la branca de Claude

- **PR #21 fusionat per Jordi** (`main` `242fff0`). Claude ja pot modificar `scripts/` i `.github/` i aplicar a `dades/` els lots de correcció que Jordi aprovi (sempre per PR). Comprovat: l'edició de `.github/workflows/valida_pr.yml` ja és permesa en aquesta sessió.
- **Fet:**
  - `main` fusionat a la branca de Claude (sense conflictes).
  - CI: nou pas `python3 estat/estat_files.py --comprova`.
  - `README.md` i `docs/PROTECCIO_BRANCA_MAIN.md` actualitzats amb el nou rol de Claude.
  - `dashboard/README.md`: ara diu que el dashboard està publicat a GitHub Pages.
  - Dashboard regenerat amb les cites del lot 11.
  - Manifest recalculat.
- **Jordi vol que Claude obri el PR de la branca:** Claude és l'encarregat d'acabar la base. El PR recull tot el que hi ha a la branca des del 23/11 (auditoria, pla, diari, eines d'estat i de traspàs, lot 11 i lot de correcció 1 preparat però no aplicat).
- **PR obert:** [jmasoribas-max/base-fundadors-ceo-stoxx600#22](https://github.com/jmasoribas-max/base-fundadors-ceo-stoxx600/pull/22) (de `claude/charming-mayer-ejb9ek` a `main`). No fusionat. Flux: DF valida → Doctorat (si toca metodologia) → Jordi fusiona.

### 23/11/2026 · Sessió 10 · Nou flux sense DF i lot de correcció 1 aplicat

- **Decisió de Jordi:** DF ja no porta la base. Claude ho fa tot: prepara, valida i obre els PR. Jordi aprova i fusiona. Al final, document per a DF amb tots els passos.
- **Conseqüències que cal resoldre:**
  1. `CLAUDE.md` i `AGENTS.md` encara diuen que DF valida els PR i fa el Wayback; s'han d'actualitzar (Claude no pot editar `CLAUDE.md`).
  2. Wayback: l'arxivament amb claus només es podia fer a l'ordinador de casa, i la verificació de cites a la captura la feia DF al seu ordinador. Cal decidir on es farà ara.
  3. `verificacio_cites_20261122.csv` (11.709 cites ja verificades a la captura, segons DF a les 14:53) encara no s'ha lliurat.
- **PR #22:** vigilat per Claude (subscripció a l'activitat del PR); CI `valida` correcte.
- **Lot de correcció 1 aplicat** a la branca `cas/correccio1` (creada a partir de la branca de Claude):
  - 171 cel·les a 59 files; 59 entrades `correccio_coherencia` al registre i una secció a 19 fitxes.
  - Les entrades de correcció porten `[NV]`, perquè el registre exigeix `[NV]` a les entrades sense cita; el fonament és la decisió citada a `notes`.
  - Files incoherents: de 51 a 3 (Knorr-Bremse 2019-2020 i Pandora 2018).
  - Nous SHA: CSV `d55dd688…0034`, xlsx `8ffdf24f…acbfac`.
  - Validadors: 0 problemes. Dashboard i manifest regenerats.

### 23/11/2026 · Sessió 11 · Cerca de CEO del grup F (en curs) i Wayback a GitHub

- **Branca:** `cas/cerca-ceo-f`, a partir de `cas/correccio1`.
- **Intervals amb cites existents:** amb les cites candidates ja verificades, només 11 de les 232 files F sense CEO es poden cobrir per interval (regla 28); a la majoria els falta la cita del nomenament. Cal una cerca nova.
- **ESEF:** els informes electrònics ESEF de filings.xbrl.org no cobreixen prou (en una empresa de prova, només el 2025). No serveixen com a via general.
- **Prova pilot (Galapagos 2017-2021):** cita literal del CEO trobada per a 4 dels 5 anys als informes anuals del web de l'emissor, en pocs minuts.
- **Cerca en paral·lel:** sis agents, uns 11 per empresa cadascun ([`traspas/cerca_ceo_f_llista.csv`](../traspas/cerca_ceo_f_llista.csv)), amb normes estrictes:
  - document de l'exercici o interval de la regla 28;
  - cita literal del document baixat;
  - fonts A/B, sense agregadors ni Wayback;
  - discrepàncies i files no trobades declarades.
  - Els resultats s'escriuen fora del repositori; **Claude els verificarà per script (re-descàrrega i cerca literal) abans d'escriure res al registre.**
- **Decisions de Jordi:**
  - Grok farà el canvi de permisos (punt 1).
  - Sí a l'última entrega de DF (punt 3).
  - Endavant amb el procés automàtic de Wayback a GitHub (punt 2).

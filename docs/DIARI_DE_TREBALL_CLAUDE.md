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
| Files amb evidència de CEO i de fundador (C1 i C2) | 4.107 de 6.012 (68,3 %) |
| Files F amb C1 i C2 | 44 de 349 |
| Fase del pla | Fase 0 (preparació): tasca 0.2 feta; esperant respostes de Grok (0.1) |
| Pendent de Jordi | Respostes de Grok; afegir l'script al CI; decisió sobre el nom del fundador; OK per obrir el PR de la branca |

## Decisions i indicacions de Jordi rebudes

| Data | Indicació (paraules de Jordi, resumides) |
|---|---|
| 23/11/2026 | Claude es fa càrrec de la base. Primer, auditoria de l'estat i llista de tasques pendents. |
| 23/11/2026 | Abast: només cal l'evidència de **qui era el CEO** cada any i de **si era el fundador** (amb el fundador quan l'empresa en té, o les proves de la metodologia per descartar-ho), guardada i arxivada. Hereus, episodis de CEO i altres variables són extres i queden fora. La validació humana la farà Jordi quan la base estigui ben feta. |
| 23/11/2026 | Les preguntes sobre on és cada cosa (Wayback, sortides de l'auditoria, etc.) les farà Jordi a Grok i passarà la resposta. |
| 23/11/2026 | OK per començar l'script d'estat per fila. |
| 23/11/2026 | Cal deixar anotat tot el que es fa en un document per tenir-ho controlat (aquest diari). |

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

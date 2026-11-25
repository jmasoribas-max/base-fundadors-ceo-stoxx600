# Wayback a GitHub Actions

Procés automàtic que arxiva a la Wayback Machine (Internet Archive) els documents citats a la base i comprova que la cita literal és a la còpia arxivada. Substitueix l'execució a l'ordinador de casa i al de DF; **les còpies continuen a web.archive.org**, que és l'arxiu independent que demana la metodologia (D29).

## Fitxers

| Fitxer | Origen | Què fa |
|---|---|---|
| [`wayback_arxiva.py`](wayback_arxiva.py) | Script de DF (SHA-256 original `c26f0dd045d76cd4b36cc49c402fdaf505ea04d93798503fc2154f8a353bf55c`; branca `df/fitxers-per-claude`, commit `529f1d0`), **adaptat per Claude el 24/11/2026**: només accepta una captura existent si Wayback la va desar amb resposta 200, i amb `--refes` torna a buscar (primer de tot) les URL la captura de les quals no és el document, sense tornar a triar els timestamps dolents | Per a cada URL, busca una captura existent (API `available` i CDX) i, si no n'hi ha, en demana una de nova amb Save Page Now. Les claus només es llegeixen de l'entorn i només s'envien a web.archive.org; no s'imprimeixen enlloc |
| [`refes_captures.py`](refes_captures.py) | Claude | Abans d'arxivar: treu dels resultats les URL la captura de les quals no és el document (`http_404`, `http_410`, `pdftotext_error`, `binari_no_llegible`, `html_sense_text`) i els seus parells de la verificació, perquè es tornin a buscar i a verificar. Com a molt dues vegades per URL; historial a `wayback/captures_refetes.csv` |
| [`verifica_flexible.py`](verifica_flexible.py) | Claude | Segona comprovació dels parells `cita_no_trobada` i `cita_parcial`: busca la cita en altres captures de la mateixa URL (índex CDX, resposta 200) i amb la comparació flexible (mateixes paraules i ordre; sense tenir en compte espais, guions de final de línia ni talls «[…]»). `porta_al_registre.py --flexible` en porta el resultat al registre: `si` si la cita és exacta en una altra captura i `si_flexible` si només hi és amb la comparació flexible |
| [`mostra_control.py`](mostra_control.py) | Claude | Mostra de control: torna a comprovar una mostra aleatòria de parells `cita_ok` amb un codi independent (baixada, extracció de text i normalització pròpies). S'activa amb l'entrada `mostra_control` del flux |
| [`verifica_cites.py`](verifica_cites.py) | Script de DF (SHA-256 original `0f45779681bf30a3284efc7df3977fd012a5896298da8d0a6cdfc824d9db3d5a`), **adaptat per Claude**: camins com a opcions; no processa parells sense cita; no escriu els parells sense captura (queden pendents); torna a verificar els parells que havien fallat per un error intern de l'script | Baixa la captura `id_` de cada URL, n'extreu el text (`pdftotext` o HTML) i comprova si hi és la cita. No fa servir claus |
| [`prepara_entrada.py`](prepara_entrada.py) | Claude | Llista les URL de les fonts amb cita (registre i base) en el format de `wayback_arxiva.py` |
| [`resum.py`](resum.py) | Claude | Resum de l'estat (s'escriu a la branca de resultats) |
| [`../../.github/workflows/wayback.yml`](../../.github/workflows/wayback.yml) | Claude | El flux de GitHub Actions |
| [`../../wayback/resultats_arxiu_inicial.csv`](../../wayback/resultats_arxiu_inicial.csv) | Resultat de l'arxivament de DF a l'ordinador de casa (22/11/2026; SHA-256 `fa0ee9c025457d0bea20a4981c4aaa51c1a7e0d4c7efb66206a4c9822345d2e5`) | Punt de partida: 4.550 URL que ja tenen captura |

## Com funciona

- S'executa sol cada 6 hores i també es pot llançar a mà (pestanya **Actions** → **wayback** → **Run workflow**).
- Cada execució continua on ho va deixar l'anterior i desa els resultats a la branca **`wayback-dades`** (carpeta `wayback/`), sense tocar `main`: `resultats_arxiu.csv`, `verificacio_cites.csv` i `RESUM.md`.
- Una execució dura com a màxim unes 6 hores: per defecte tracta fins a 700 URL a arxivar i 400 a verificar.
- Si no hi ha les claus, només verifica les URL que ja tenen captura.
- Els resultats es porten al registre (`url_wayback`, `cita_verificada_a_captura`) en un PR a part, sense tocar FounderCEO.

## Configuració de les claus (una sola vegada, la fa Jordi)

1. A GitHub, al repositori: **Settings** → **Secrets and variables** → **Actions** → **New repository secret**.
2. Nom `IA_S3_ACCESS`, valor: la clau d'accés d'Internet Archive. Desa.
3. Torna a **New repository secret**. Nom `IA_S3_SECRET`, valor: la clau secreta. Desa.

Les claus són a https://archive.org/account/s3.php (amb el compte d'Internet Archive). GitHub les guarda xifrades i les amaga dels registres; ningú, tampoc Claude, no les pot llegir.

## Cost

GitHub Actions és gratuït als repositoris públics. En un de privat, el pla gratuït en dona 2.000 minuts al mes.

## Primera execució (23/11/2026, run 45204845355)

- **Arxivament:** 993 captures noves. En total, 3.893 de les 7.287 URL amb cita ja tenen captura. El pas va arribar al límit de 200 minuts; els resultats es desen URL a URL i la propera execució continua.
- **Verificació:** 2.545 parells. 733 `cita_ok`, 140 `cita_no_trobada`, 10 `cita_parcial` i 1.662 `captura_no_llegible`.
- **Error del flux:** 1.537 dels 1.662 `captura_no_llegible` eren `excepció_interna:FeatureNotFound`, perquè el flux no instal·lava `lxml`, l'analitzador HTML que fa servir l'script. Corregit: el flux instal·la `lxml==5.3.0`, i l'script retira aquests parells dels resultats perquè es tornin a verificar. Els altres 125 són PDF de captura malmesos (`pdftotext`) i es mantenen.


## Captures que no eren el document (revisió del 24/11/2026)

Revisió dels resultats fins a l'execució 45420730928 (6.880 parells; 5.009 `cita_ok`):

- **166 URL (860 parells) amb captura `http_404`.** Quasi totes (157) són captures de Save Page Now en què el servidor de l'emissor va respondre a Internet Archive amb una pàgina d'error; la resta, captures existents triades per l'API `available`, que no mirava el codi de la captura.
- **61 URL (unes 430 parells) amb un PDF arxivat que no s'obre** (`pdftotext_error`), sobretot captures indicades a la base antiga.
- **6 URL** amb una captura binària o un HTML sense text.

Correcció: `wayback_arxiva.py` només accepta captures desades amb resposta 200, i `refes_captures.py` fa que aquestes 233 URL es tornin a buscar a la propera execució (una altra captura bona o una de nova). Si després de dos intents no n'hi ha cap de bona, la URL queda pendent: la cita no es dona per verificada a la captura i cal una font alternativa.

Mostra de control: llançar el flux a mà amb `mostra_control` = 60 (llavor 20261124). El resultat es desa a `wayback/mostra_control_<run>.csv` de la branca `wayback-dades`.

## Segona comprovació (25/11/2026)

Mostra aleatòria de 150 de les 1.629 entrades del registre amb `cita_verificada_a_captura=no`. La cita era al document original en 127 casos (85 %), i hi era fins i tot amb la comparació estricta. Per tant, el problema gairebé sempre és que la captura vigent és **una altra versió** de la pàgina o del document. En 13 casos (9 %), la cita no era literal a l'original: cites de taula o amb «[…]», que van al lot de revisió de fonts. En 10 casos (7 %), l'original no era a la còpia local.

Per això, `verifica_flexible.py` fa dues coses:

1. Busca la cita en **altres captures de la mateixa URL**. Una coincidència exacta en una altra captura és un `si` normal, amb la URL d'aquella captura.
2. Aplica la **comparació flexible** que va aprovar Jordi el 25/11/2026. El resultat es marca a part (`si_flexible`) i el dashboard el mostra com a «Cita comprovada a la còpia (flexible)». `estat/estat_files.py` el compta com a verificat a la captura (C3).

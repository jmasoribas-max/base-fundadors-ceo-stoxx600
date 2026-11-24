# Wayback a GitHub Actions

Procés automàtic que arxiva a la Wayback Machine (Internet Archive) els documents citats a la base i comprova que la cita literal és a la còpia arxivada. Substitueix l'execució a l'ordinador de casa i al de DF; **les còpies continuen a web.archive.org**, que és l'arxiu independent que demana la metodologia (D29).

## Fitxers

| Fitxer | Origen | Què fa |
|---|---|---|
| [`wayback_arxiva.py`](wayback_arxiva.py) | Script de DF, **sense canvis** (SHA-256 `c26f0dd045d76cd4b36cc49c402fdaf505ea04d93798503fc2154f8a353bf55c`; branca `df/fitxers-per-claude`, commit `529f1d0`) | Per a cada URL, busca una captura existent (API `available` i CDX) i, si no n'hi ha, en demana una de nova amb Save Page Now. Les claus només es llegeixen de l'entorn i només s'envien a web.archive.org; no s'imprimeixen enlloc |
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


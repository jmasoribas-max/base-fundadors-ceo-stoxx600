# Notes per repetir el procés a GitHub

Aquest fitxer és nou (no formava part del paquet original). El `LLEGEIX-ME.md` explica només com executar `wayback_arxiva.py` en un ordinador local amb PowerShell, i no s'ha modificat.

Els dos scripts s'han copiat sense canvis des del box (`/workspace/dashboard-fundadors/wayback/`). `verifica_cites.py` és la versió que s'està executant al box (PID 30762). `wayback_arxiva.py` és la còpia que hi ha al box del paquet executat a l'ordinador de casa el 21-22/11/2026 (mateix directori que `urls_main.csv`, `LLEGEIX-ME.md` i `wayback_resultats_20261122.csv`).

## wayback_arxiva.py

Arxiva a la Wayback Machine les URL de font de la base. Per cada URL única, consulta si ja n'hi ha una captura (API available i CDX). Si n'hi ha, la reutilitza (`ja_existia`). Si no, en demana una de nova amb l'API de desament (`capturada`). Si falla, marca `error` (amb el missatge `pendent_verificacio_externa` quan escau) i continua. És reprenible: les URL ja marcades `ja_existia` o `capturada` se salten.

Entrada:
- CSV d'URL (per defecte `urls_main.csv` al mateix directori; opció `--input`).
- Variables d'entorn `IA_S3_ACCESS` i `IA_S3_SECRET` (obligatòries per desar captures noves). El codi les llegeix de l'entorn; no porten cap valor literal.

Sortida:
- CSV incremental (per defecte `wayback_resultats.csv`; opció `--output`), una fila per URL, amb camps `url`, `estat`, `timestamp_captura`, `url_wayback`, `http_codi`, `missatge`. El fitxer ja pujat a `entrada_claude/wayback_resultats_20261122.csv` és el resultat del run del 22/11.

Opcions útils: `--totes` (consulta també les URL que ja tenen captura indicada al CSV), `--limit N` (prova), `--pausa` (defecte 8 s), `--max-reintents` (defecte 5).

Dependències: Python 3 i la llibreria `requests`. `verify=True` (sense `-k`). No fa servir archive.today.

## verifica_cites.py

Comprova si la cita literal de cada parell (ISIN-any, URL, cita) apareix a la captura Wayback corresponent. No fa servir claus d'archive.org. És reprenible (cache de captures i CSV incremental). Pausa mínima de 2 s, amb backoff si Wayback respon 429.

Entrada (camins per defecte, relatius al lloc on és l'script):
- `../repo_main_lectura/dades/base_isin_any_v8r3.csv`
- `../repo_main_lectura/docs/REGISTRE_CANVIS.csv`
- `wayback_resultats_20261122.csv` (al mateix directori que l'script)
- cache de captures a `cache/` (opció `--cache`)

Sortida:
- `verificacio_cites_20261122.csv` (opció `--out`)
- `INFORME_VERIFICACIO_CITES.md` (opció `--informe`), generat quan el recorregut s'ha completat (o amb `--nomes-informe`)
- registre a `verifica_cites.log`

Els noms amb data `20261122` estan fixats al codi. Per a un run nou caldria ajustar-los (aquest paquet no modifica l'script). També cal que existeixi el directori germà `repo_main_lectura` amb la base i el registre, o passar uns `--out`/`--informe`/`--cache` i adaptar els camins de la base.

Opcions útils: `--limit-urls N` (prova), `--nomes-informe`.

Dependències: Python 3, `requests`, `beautifulsoup4` i `pdftotext` (Poppler) per als PDF.

## Claus a GitHub

Per executar `wayback_arxiva.py` a GitHub Actions, `IA_S3_ACCESS` i `IA_S3_SECRET` han d'anar com a secrets del repositori, amb aquests mateixos noms, i injectar-se com a variables d'entorn del pas. No s'han d'escriure al flux, ni al codi, ni als logs. `verifica_cites.py` no les necessita.

## Proxy

Els scripts no configuren cap intermediari: fan servir `requests` amb la configuració per defecte (variables d'entorn estàndard, si n'hi ha). El run de `verifica_cites.py` al box de DF va sortir a través del proxy de sortida del box. El run de `wayback_arxiva.py` es va fer a l'ordinador de casa, seguint el `LLEGEIX-ME.md`. En un flux de GitHub Actions el trànsit sortiria des de l'executor de GitHub, no des d'aquell proxy del box.

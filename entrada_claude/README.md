# entrada_claude

Fitxers de DF per a Claude, a la branca `df/fitxers-per-claude` (creada des de `main` `17b03dfa4075f145fdddb56040b1b695d2b9359d`). El contingut s'ha copiat sense modificar. Aquesta carpeta no forma part de `main`.

Els dos `MANIFEST_evidencies_web_r4.csv` tenen el mateix nom i s'han posat a subcarpetes (`r4_claude/` i `r4_chatgpt/`).

`verificacio_cites_20261122.csv` i `INFORME_VERIFICACIO_CITES.md` s'han afegit un cop acabada la verificació de cites (informe del 24/11/2026 a les 07:34 CET, Europe/Madrid).

Els scripts de Wayback són a `scripts_wayback/`, copiats sense modificar des de `/workspace/dashboard-fundadors/wayback/`. El `LLEGEIX-ME.md` original no explica com repetir el procés a GitHub Actions; les notes corresponents són a `scripts_wayback/NOTES_GITHUB.md` (fitxer nou, el LLEGEIX-ME no s'ha editat).

## Fitxers

- `SORTIDA_chatgpt_COMPLET.jsonl` — origen box `/workspace/dashboard-fundadors/auditoria_v75r2/paquet_ia/r3e/sortides_complet/SORTIDA_chatgpt_COMPLET.jsonl` (còpies idèntiques al Drive, carpeta `1jwCn3Eev6Ni5McBp1jEpQnEjpBQj8j61`, fitxer `1cMhGnfZlw3EcaTic-agFu5Ntrd_oD-Fs`, i a `/workspace/doctorat/auditoria_r3e_sortides_complet/` i `verificacio_r3e_drive/`). Format JSONL. 3.757 registres (1 `control_entrades`, 2.122 `classificacio`, 1.633 `incidencia`, 1 `informe`). SHA-256 `e65627e2a855a3b38df4fb3be4e3807e252227c39bf2aa27b49c3014708a2e7f`. Coincideix amb el `SHA256SUMS` oficial de la carpeta de sortides r3e.

- `SORTIDA_claude_COMPLET.jsonl` — origen box `/workspace/dashboard-fundadors/auditoria_v75r2/paquet_ia/r3e/sortides_complet/SORTIDA_claude_COMPLET.jsonl` (còpies idèntiques al Drive, mateix carpeta, fitxer `1iOkn2Hz08Yq_7Dboxgkh2teiVZYRvrew`, i a les còpies de l'Arquitecta citades amunt). Format JSONL. 2.675 registres (1 `control_entrades`, 2.122 `classificacio`, 551 `incidencia`, 1 `informe`). SHA-256 `711564ce30186d87e0649ec14c1cd8abf24f4e223fa57476152acbb0e4f1adb0`. Coincideix amb el `SHA256SUMS` oficial.

- `SORTIDA_chatgpt_COMPLETACIO.jsonl` — origen box `/workspace/dashboard-fundadors/auditoria_v75r2/paquet_ia/r4_completacio/sortides/chatgpt/SORTIDA_chatgpt_COMPLETACIO.jsonl` (còpies idèntiques al Drive, carpeta `1IVt1Q6LWfG0wG25B4vxc0qbkufcfJPXy`, fitxer `12PYpFI4UPkNWQoFACsKjBwtyyM4GokhP`, i a `/workspace/doctorat/completacio_r4_sortides/chatgpt/` i `verificacio_r4_drive/`). Format JSONL. 1.668 registres (1 `control_entrades`, 1.666 `resposta`, 1 `informe`). SHA-256 `edb00bc23af03909adcf8ddf2d0d06dacbd354403209dfb830813f9ccab56295`. Coincideix amb el `SHA256SUMS` oficial.

- `SORTIDA_claude_COMPLETACIO.jsonl` — origen box `/workspace/dashboard-fundadors/auditoria_v75r2/paquet_ia/r4_completacio/sortides/claude/SORTIDA_claude_COMPLETACIO.jsonl` (còpies idèntiques al Drive, carpeta `1h_WhaP9wrepgnBPn0INttwjzTodvOJam`, fitxer `1snomzCW0Ar8nYYfXnc2fgpud6289v19A`, i a `/workspace/doctorat/completacio_r4_sortides/claude/` i `verificacio_r4_drive/`). Format JSONL. 1.668 registres (1 `control_entrades`, 1.666 `resposta`, 1 `informe`). SHA-256 `ba4124dc8605b22599c6f8a79493790063913a6ee4a18e96c9c785f679dcbf3f`. Coincideix amb el `SHA256SUMS` oficial.

- `CERTIFICACIO_parella_any_r3e.csv` — origen box `/workspace/dashboard-fundadors/auditoria_v75r2/paquet_ia/r4_completacio/_intern/CERTIFICACIO_parella_any_r3e.csv` (només al box, no és al Drive). Format CSV. 2.122 files de dades + capçalera. SHA-256 `31c24add3a0ad981ccdbd04e07b0c72566a2319841f27f4d606180836698ccab`.

- `r4_claude/MANIFEST_evidencies_web_r4.csv` — origen box `/workspace/dashboard-fundadors/auditoria_v75r2/paquet_ia/r4_completacio/sortides/claude/evidencies_web/MANIFEST_evidencies_web_r4.csv` (només al box, no és al Drive; no s'han pujat les evidències web en brut). Format CSV. 3.768 files de dades + capçalera. SHA-256 `523dbedf5fdbf590080e4185bbc929f42d567e2f3506c07bae063e1589e49fb9`.

- `r4_chatgpt/MANIFEST_evidencies_web_r4.csv` — origen box `/workspace/dashboard-fundadors/auditoria_v75r2/paquet_ia/r4_completacio/sortides/chatgpt/evidencies_web/MANIFEST_evidencies_web_r4.csv` (només al box, no és al Drive; no s'han pujat les evidències web en brut). Format CSV. 2.481 files de dades + capçalera. SHA-256 `4aa3828424ea29d6577e3bb69b6674dd44c8496f6e7f3d49f944323351b8239b`.

- `fonts_v75r2.csv` — origen canònic box `/workspace/dashboard-fundadors/integracio_20261117_v75/fonts_v75r2.csv` (còpies idèntiques a `/workspace/dashboard-fundadors/vigent_upload_20261117_v75r2/fonts_v75r2.csv`, `/workspace/dashboard-fundadors/vigent_verify_20261117_v75r2/fonts_v75r2.csv`, i al Drive fitxer `1Ze-INmZqhA07lp7y-PjaCZ9kI4QT8kE1`). Format CSV. 8.310 files de dades + capçalera (8.606 línies físiques, per salts de línia dins de camps). SHA-256 `fb25b45b60cbf047d764aa7760cb3de0fd0c7c02020d82183c1ca9b6a2845afb`. Coincideix amb el `SHA256SUMS` de la carpeta d'integració.

- `wayback_resultats_20261122.csv` — origen box `/workspace/dashboard-fundadors/wayback/wayback_resultats_20261122.csv` (només al box, no és al Drive). Format CSV. 4.555 files de dades + capçalera. SHA-256 `fa0ee9c025457d0bea20a4981c4aaa51c1a7e0d4c7efb66206a4c9822345d2e5`.

- `verificacio_cites_20261122.csv` — origen box `/workspace/dashboard-fundadors/wayback/verificacio_cites_20261122.csv` (només al box, no és al Drive). Format CSV. 39.453 files de dades + capçalera (42.645 línies físiques, per salts de línia dins de camps). SHA-256 `cf5b167c49eaa371ed8d1eeaa65bff821638aacba6457c598c643f9c57be4e12`.

- `INFORME_VERIFICACIO_CITES.md` — origen box `/workspace/dashboard-fundadors/wayback/INFORME_VERIFICACIO_CITES.md` (només al box, no és al Drive). Format Markdown. 739 línies. SHA-256 `7976d90c3ceca0dedbe57b95bb4cf20a805831f0b74d5ed570673725ee7f508c`.

- `scripts_wayback/wayback_arxiva.py` — origen box `/workspace/dashboard-fundadors/wayback/wayback_arxiva.py` (còpia al box del paquet executat a l'ordinador de casa el 21-22/11/2026). Script Python. SHA-256 `c26f0dd045d76cd4b36cc49c402fdaf505ea04d93798503fc2154f8a353bf55c`.

- `scripts_wayback/verifica_cites.py` — origen box `/workspace/dashboard-fundadors/wayback/verifica_cites.py` (versió en execució al box, PID 30762). Script Python. SHA-256 `0f45779681bf30a3284efc7df3977fd012a5896298da8d0a6cdfc824d9db3d5a`.

- `scripts_wayback/LLEGEIX-ME.md` — origen box `/workspace/dashboard-fundadors/wayback/LLEGEIX-ME.md` (instruccions originals per executar `wayback_arxiva.py` en local, sense modificar). Format Markdown. SHA-256 `9664817acf77ca0d487ee95536585c2d237e919e6f43b591d5fff47107e41cfd`.

- `scripts_wayback/NOTES_GITHUB.md` — fitxer nou de DF (no hi era al paquet original). Explica per a què serveix cada script, les entrades i sortides, que les claus han d'anar com a secrets del repositori (`IA_S3_ACCESS`, `IA_S3_SECRET`) i que el run del box va fer servir el proxy de sortida. Format Markdown. SHA-256 `1e898823e4be2c5a97fefc3f80541072b764950b1fbdb1ebf03f9cc3b65c4196`.

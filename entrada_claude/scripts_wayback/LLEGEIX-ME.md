# Arxivar les fonts de main a Wayback

Aquest directori es pot copiar al teu ordinador. L'script no modifica el repositori. Les claus d'archive.org no s'han d'enganxar a cap fitxer, ni al xat, ni a un correu.

Les 4.550 URL úniques venen del CSV de la base (`font_classificacio_url`, `d37_cita_contemp_url`, `url_font` de sector i `v75_urls_arxivades`) i del registre de canvis de main (`docs/REGISTRE_CANVIS.csv`, on hi ha les fonts de CEO i de fundador dels lots). D'aquestes, 3.288 ja tenen una captura indicada al CSV; per defecte l'script les dona per fetes sense tornar-les a desar. En queden 1.262 per consultar i, si cal, desar.

L'script no comprova les cites. Això es farà després.

Temps estimat (només les 1.262 pendents, amb 8 segons de pausa): unes 3-4 hores si la majoria ja són a Wayback; unes 8-12 hores si se n'han de desar moltes de noves. Es pot aturar i reprendre.

## Passos

1. Copia tot aquest directori al teu ordinador (cal que hi siguin `wayback_arxiva.py` i `urls_main.csv`).

2. Obre PowerShell i entra al directori copiat. Exemple, si l'has deixat a Documents:

   ```powershell
   Set-Location $env:USERPROFILE\Documents\wayback
   ```

3. Comprova que tens Python 3. Si `python --version` falla, instal·la'l des de https://www.python.org/downloads/ i torna a obrir PowerShell. En instal·lar-lo, marca l'opció d'afegir Python al PATH.

4. Instal·la `requests` si encara no el tens:

   ```powershell
   python -m pip install requests
   ```

5. Defineix les claus com a variables d'entorn d'aquesta sessió, sense deixar-les en un fitxer. Abans, desactiva l'historial per no guardar-les:

   ```powershell
   Set-PSReadLineOption -HistorySaveStyle SaveNothing
   $acc = Read-Host "IA_S3_ACCESS" -AsSecureString
   $ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($acc)
   $env:IA_S3_ACCESS = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr)
   [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr)
   $sec = Read-Host "IA_S3_SECRET" -AsSecureString
   $ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($sec)
   $env:IA_S3_SECRET = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr)
   [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr)
   Remove-Variable acc, sec, ptr
   ```

   Si prefereixes escriure-les a mà a la mateixa finestra (`$env:IA_S3_ACCESS = '...'`), no les enganxis a cap document i esborra la línia de l'historial després.

6. Executa l'script:

   ```powershell
   python wayback_arxiva.py
   ```

   El resultat va creixent a `wayback_resultats.csv` (una línia per URL: `ja_existia`, `capturada` o `error`). Si una URL falla, queda marcada `pendent_verificacio_externa` al missatge i l'script continua.

7. Per reprendre després d'aturar-lo o d'un error, torna a definir les variables d'entorn (pas 5) si has tancat la finestra, i executa de nou la mateixa ordre del pas 6. Les URL ja marcades `ja_existia` o `capturada` se salten. Les que havien quedat en error es tornen a provar.

8. Quan acabi, esborra les claus d'aquesta sessió:

   ```powershell
   Remove-Item Env:IA_S3_ACCESS -ErrorAction SilentlyContinue
   Remove-Item Env:IA_S3_SECRET -ErrorAction SilentlyContinue
   ```

   Envia `wayback_resultats.csv` (no cal que hi posis les claus). No cal tornar a executar res si no t'ho demanen.

## Notes

- Per defecte no es tornen a consultar les 3.288 URL que ja tenen captura al CSV. Si alguna vegada cal revisitar-les: `python wayback_arxiva.py --totes`.
- Per una prova curta: `python wayback_arxiva.py --limit 3`.
- La pausa per defecte és de 8 segons. No la abaixis sense motiu (Wayback limita la cadència; un 429 fa que l'script esperi i reintenti).
- Una desada nova és sempre una captura d'ara, no d'un any passat. Si ja n'hi ha una de l'any objectiu, es reutilitza. Si només n'hi ha d'un altre any, també es reutilitza i no se'n demana una de nova.
- L'script no desactiva la verificació SSL, no salta intermediaris i no fa servir archive.today.

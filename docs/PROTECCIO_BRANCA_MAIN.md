# Protecció de la branca `main`

Aquest document descriu la protecció efectiva del repositori públic `jmasoribas-max/base-fundadors-ceo-stoxx600` (CET, Europe/Madrid).

## Per què no hi ha aprovacions obligatòries

Claude Code farà servir el compte de Jordi (`jmasoribas-max`). Els pull requests s'obriran, doncs, **en nom de Jordi**. GitHub no deixa que un compte aprovi un PR propi. Si es deixés `enforce_admins=true` amb 1 aprovació obligatòria (o amb CODEOWNERS obligatori), **ningú no podria fusionar res**.

Per això la protecció de `main` (decisió de Jordi, 19/11/2026 10:22) és:

- PR obligatori (no es pot fer push directe a `main`, tampoc els administradors: `enforce_admins=true`)
- Aprovacions obligatòries: **0**
- `require_code_owner_reviews` **desactivat** (amb un sol compte no es pot complir)
- Cap force push i cap esborrat de `main`
- El fitxer `.github/CODEOWNERS` es **conserva com a documentació** de quins camins no ha de tocar Claude; no s'usa com a requisit de revisió a GitHub

## Quina és la barrera real

Com que Claude i Jordi comparteixen el mateix compte de GitHub, la protecció de branques no pot servir d'aprovació d'un segon revisor. La barrera real és la combinació de:

1. **La protecció contra el push directe a `main`** (`enforce_admins=true`, PR obligatori, sense force push ni esborrat). Claude no pot empènyer ni forçar `main`; només pot obrir un PR.
2. **Els permisos de Claude Code** a `.claude/settings.json` (regles `deny`): bloqueja `git push` (incloent-hi cap a `main` / `origin main` i `--force`), `gh pr merge`, i `gh api` quan l'ordre conté `merge` o `protection`; i bloqueja les eines d'edició (`Edit`/`Write`) sobre `scripts/`, `docs/METODOLOGIA.md`, `CLAUDE.md`, `docs/REGLES*`, `.github/` i `.claude/`.
3. **`CLAUDE.md`**, que li prohibeix tocar `main`, fusionar i modificar aquests mateixos camins.

**Jordi és qui fusiona**, amb el botó de fusió del PR a GitHub, després que DF validi i Doctorat revisi la metodologia. Claude no ha de fusionar.

## 1. Qui pot fer què

| Actor | Permès | Prohibit |
|---|---|---|
| Claude Code | Crear branques, fer-hi commits, executar scripts en local, obrir un PR amb resum | Push directe a `main`, force push, fusionar un PR, esborrar `main`, editar els camins protegits |
| DF | Validar el PR (format, comptes, `scripts/valida_pr.py`, coherència) | Fusionar a `main` |
| Doctorat | Revisar la metodologia del PR | Fusionar a `main` |
| Jordi | Fusionar el PR a `main` amb el botó de GitHub | Push directe a `main` (la protecció també s'aplica als administradors) |

## 2. Configuració aplicada a GitHub (protecció clàssica de `main`)

Valors efectius:

- Require a pull request before merging: sí
- Required approvals: **0**
- Require review from Code Owners: **no**
- Dismiss stale reviews: sí (resta activat; no hi ha aprovacions obligatòries)
- Enforce for administrators: **sí**
- Allow force pushes: **no**
- Allow deletions: **no**

## 3. Permisos de Claude Code (`.claude/settings.json`)

Fitxer de projecte compartit (documentació oficial: [Configure permissions](https://code.claude.com/docs/en/permissions) i [Settings files](https://code.claude.com/docs/en/settings), consultades el 19/11/2026). Sintaxi verificada [V]:

- Les regles van a `permissions.deny`. Les deny tenen prioritat i un `allow` no les pot anul·lar.
- `Bash(git push *)` és l'exemple oficial per refusiar ordres que comencen per `git push` (inclou `git push origin main` i `git push --force`). S'hi afeixen `Bash(git * push *)` i `Bash(*git push *)` per cobrir variants com `git -C . push`, seguint les comodines documentades.
- Per als fitxers s'usa `Edit(/ruta)` i no `Write(/ruta)`: la documentació oficial diu que `Write(path)` no emparella cap crida i que `Edit` regeix també l'eina Write. El patró `/ruta` en un `.claude/settings.json` de projecte s'ancora a l'arrel del repositori.

Limitació documentada oficialment [V]: una regla `Bash` emparella el text de l'ordre tal com la escriu Claude, no totes les formes equivalents del mateix programa. Per exemple, `Bash(git push *)` no atura per si sola `git -C . push origin main` (per això hi ha la regla addicional). Tampoc no és una frontera de seguretat del sistema operatiu: un script que obri fitxers pel seu compte o una invocació no emparellada pot saltar-se la regla. La protecció de `main` a GitHub sí que rebutja el push directe, també si ve d'una ordre no emparellada.

## 4. CODEOWNERS (documentació)

`.github/CODEOWNERS` llista els camins que Claude no ha de modificar i els assigna a `@jmasoribas-max`. **No és un requisit de revisió a GitHub**, perquè amb un sol compte no es pot complir. Serveix de documentació i de guia, juntament amb les regles `Edit` de `.claude/settings.json`.

Camins documentats: `scripts/`, `docs/METODOLOGIA.md`, `CLAUDE.md`, `docs/REGLES*.md`, `.github/` i `.claude/`.

## 5. Comprovació

1. Un push directe a `main` (també fet per l'administrador) és rebutjat.
2. Un canvi entra a `main` només si Jordi el fusiona amb el botó del PR.
3. Claude no ha d'executar `git push` cap a `main`, ni `git push --force`, ni `gh pr merge`, ni crides `gh api` de fusió o de protecció de branques.

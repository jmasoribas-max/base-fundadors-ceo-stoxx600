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

1. **La protecció contra el push directe a `main`** (`enforce_admins=true`, PR obligatori, sense force push ni esborrat). GitHub ja rebutja qualsevol push directe a `main`, també si ve d'una ordre no emparellada pels permisos. Claude pot empènyer les seves branques i obrir un PR; no pot empènyer ni forçar `main`.
2. **Els permisos de Claude Code** a `.claude/settings.json` (regles `deny`): bloqueja només el `git push` cap a `main` (p. ex. `origin main` o `:main`) i el force push (`--force` / `-f`); no bloqueja el push de les branques de Claude, necessari per obrir un PR. També bloqueja `gh pr merge` i `gh api` quan l'ordre conté `merge` o `protection`, i les eines d'edició (`Edit`/`Write`) sobre `docs/METODOLOGIA.md`, `CLAUDE.md`, `docs/REGLES*` i `.claude/`. Des del 23/11/2026 (PR #21, decisió de Jordi) ja no bloqueja `scripts/` ni `.github/`: Claude, com a coordinador de la base, els pot modificar en una branca i per PR.
3. **`CLAUDE.md`**, que li prohibeix tocar `main`, fusionar i modificar aquests mateixos camins (amb l'excepció de `scripts/`, `.github/` i els lots de correcció aprovats a `dades/`, secció 8).

**Jordi és qui fusiona**, amb el botó de fusió del PR a GitHub, després que DF validi i Doctorat revisi la metodologia. Claude no ha de fusionar.

## 1. Qui pot fer què

| Actor | Permès | Prohibit |
|---|---|---|
| Claude Code | Crear branques, fer-hi commits, empènyer les seves branques, executar scripts en local, obrir un PR amb resum; com a coordinador de la base (des del 23/11/2026), modificar `scripts/` i `.github/` i aplicar a `dades/` els lots de correcció aprovats per Jordi | Push directe a `main`, force push, fusionar un PR, esborrar `main`, editar `docs/METODOLOGIA.md`, `CLAUDE.md`, `AGENTS.md`, les regles i `.claude/` |
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
- No s'usa `Bash(git push *)` (ni `Bash(git * push *)` ni `Bash(*git push *)`): aquestes regles bloquegen també el push de les branques de Claude i l'impedirien obrir un PR. Es bloqueja només el push a `main` i el force push, amb la mateixa sintaxi oficial `Bash(eina arguments*)`:
  - `Bash(git push origin main*)`
  - `Bash(git push * main)`
  - `Bash(git push *:main*)`
  - `Bash(git push --force*)`
  - `Bash(git push -f*)`
  - `Bash(git push * --force*)`
  - `Bash(git push * -f*)`
- Per als fitxers s'usa `Edit(/ruta)` i no `Write(/ruta)`: la documentació oficial diu que `Write(path)` no emparella cap crida i que `Edit` regeix també l'eina Write. El patró `/ruta` en un `.claude/settings.json` de projecte s'ancora a l'arrel del repositori.

Limitació documentada oficialment [V]: una regla `Bash` emparella el text de l'ordre tal com la escriu Claude, no totes les formes equivalents del mateix programa. Tampoc no és una frontera de seguretat del sistema operatiu: un script que obri fitxers pel seu compte o una invocació no emparellada (p. ex. `git -C . push origin main`) pot saltar-se la regla. Això no obre `main`: GitHub ja rebutja qualsevol push directe a `main`.

## 4. CODEOWNERS (documentació)

`.github/CODEOWNERS` llista els camins protegits i els assigna a `@jmasoribas-max` (des del 23/11/2026, Claude pot modificar `scripts/` i `.github/` per PR; la resta, no). **No és un requisit de revisió a GitHub**, perquè amb un sol compte no es pot complir. Serveix de documentació i de guia, juntament amb les regles `Edit` de `.claude/settings.json`.

Camins documentats: `scripts/`, `docs/METODOLOGIA.md`, `CLAUDE.md`, `docs/REGLES*.md`, `.github/` i `.claude/`.

## 5. Comprovació

1. Un push directe a `main` (també fet per l'administrador) és rebutjat.
2. Un canvi entra a `main` només si Jordi el fusiona amb el botó del PR.
3. Claude pot fer `git push` de les seves branques. No ha d'executar `git push` cap a `main`, ni `git push --force` / `-f`, ni `gh pr merge`, ni crides `gh api` de fusió o de protecció de branques.

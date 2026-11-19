# Protecció de la branca `main`

Aquest document són **instruccions de configuració**, no una recomanació opcional. La branca `main` ha d'estar protegida abans que el repositori s'usi a GitHub i abans que Claude Code hi treballi amb accés al repositori.

Regla de govern (decisió de Jordi, 19/11/2026 9:42, CET, Europe/Madrid):

- Claude no pot tocar mai `main` (ni push, ni commit, ni fusió, ni esmena directa).
- Claude només treballa en branques i obre pull requests.
- **DF** valida.
- **Doctorat** revisa la metodologia.
- **Jordi** aprova i fusiona.

## 1. Qui pot fer què

| Actor | Permès | Prohibit |
|---|---|---|
| Claude Code | Crear branques, fer-hi commits, executar scripts en local, obrir un PR amb resum | Qualsevol escriptura a `main`, fusionar un PR, fer push directe, forçar o esborrar `main` |
| DF | Validar el PR (format, comptes, `scripts/valida_pr.py`, coherència) | Fusionar a `main` |
| Doctorat | Revisar la metodologia del PR | Fusionar a `main` |
| Jordi | Aprovar el PR i fusionar-lo a `main` | — |

Ningú no fa push directe a `main`. L'únic camí d'entrada és un PR aprovat per Jordi.

## 2. Configuració a GitHub (ruleset)

Al repositori: **Settings → Rules → Rulesets → New branch ruleset**.

1. **Ruleset name:** `proteccio-main`.
2. **Enforcement status:** Active.
3. **Target branches:** Include `main` (o el patró `refs/heads/main`).
4. Activeu aquestes regles:
   - **Restrict deletions** (ningú no pot esborrar `main`).
   - **Block force pushes**.
   - **Restrict updates** / impedir push directe a la branca (si el ruleset ho ofereix com a regla a part).
   - **Require a pull request before merging**:
     - Required approvals: **1**.
     - El revisor que compta per a la fusió és el compte GitHub de **Jordi** (no s'hi posa aquí un nom d'usuari inventat: cal el compte real de Jordi).
     - Dismiss stale pull request approvals when new commits are pushed.
     - Do not allow bypassing the above settings (cap excepció per a administradors pel que fa al push directe).
   - **Require status checks to pass**: afegiu la comprovació que executa `scripts/valida_pr.py` (flux `.github/workflows/valida_pr.yml`), un cop el repositori sigui a GitHub i el flux s'hagi executat almenys un cop (GitHub només deixa exigir un check que ja existeixi).
5. **Bypass list:** buida, tret que Jordi hi posi explícitament el seu compte només per a emergències documentades. Claude, DF i Doctorat no hi han de figurar.
6. Deseu el ruleset.

Si el repositori encara usa les **Branch protection rules** clàssiques (Settings → Branches → Add branch protection rule):

- Branch name pattern: `main`.
- Require a pull request before merging, 1 aprovació (Jordi).
- Require status checks to pass (`valida_pr`).
- Do not allow bypassing the above settings.
- Restrict who can push to matching branches: cap compte, cap equip, cap integració amb permís de push directe.
- Allow force pushes: no. Allow deletions: no.

## 3. Permisos del repositori

- El repositori és **privat**.
- Claude Code pot tenir accés de redacció **només per crear branques i obrir PR**, no per fusionar a `main`. Si el producte ho permet, desactiveu-li el permís de fusió.
- DF i Doctorat: accés de lectura (i comentaris / revisió al PR). No han de poder fusionar.
- Només el compte de Jordi pot fusionar PRs a `main`.
- No hi ha d'haver cap clau, token ni secret al repositori. Els secrets de GitHub Actions, si calen, van a Settings → Secrets, no al codi.

## 4. Comprovació un cop configurat

Després d'activar la protecció, verifiqueu:

1. Un push directe a `main` és rebutjat.
2. Un PR sense l'aprovació de Jordi no es pot fusionar.
3. Un PR amb `scripts/valida_pr.py` en fallida no es pot fusionar (un cop el status check sigui obligatori).
4. Claude no pot fusionar ni empènyer a `main`.

Aquestes instruccions s'han d'aplicar en el moment de crear el repositori remot. Aquest arbre és encara un repositori **git local**; no s'ha creat cap remot ni s'ha fet cap push.

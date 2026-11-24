# Dashboard Fundadors (lloc estàtic)

Lloc HTML estàtic per consultar la base Fundadors (STOXX Europe 600, 2016-2025). Té tres seccions:

- **Estat** (`index.html`): en quin punt és la base. Files acabades, embut de les quatre condicions (C1-C4), estat per etiqueta i per any, mancances i què s'hi fa, origen dels dubtes oberts, controls de qualitat, resultats provisionals i «Sobre aquestes dades» (`#versio`). Es pot imprimir en dues pàgines A4.
- **Empreses** (`empreses.html`): cercador i filtres (etiqueta, estat, país d'emissió de l'ISIN) i una taula amb la sèrie FounderCEO 2016-2025 i l'estat de les files de cada empresa. Llegeix `?q=` i el hash (`q`, `e`, `t`, `p`, `m`).
- **Mètode** (`metodologia.html`): la pregunta, la llegenda (`#llegenda`), quan una fila està acabada, fonts A/B/C, marques de prova (`#regla-…`), l'estat antic de l'auditoria i els criteris de la part pública.
- Una **fitxa** per ISIN (`empreses/{ISIN}.html`): estat de l'empresa, dubtes oberts, línia de temps (etiqueta i estat per any), «Any per any» amb «Per què?» (la cita de CEO i la de fundador de l'any, amb la font original, la còpia Wayback i si la cita s'ha comprovat a la còpia), totes les proves plegades per grup i l'historial de l'auditoria IA.

**Publicat a GitHub Pages** (https://jmasoribas-max.github.io/base-fundadors-ceo-stoxx600/), des de la branca `gh-pages`. La primera publicació la va fer el compte de Jordi el 23/11/2026 a les 14:00 (commit `64ce9cc`, `main` `17b03df`). Des del 24/11/2026, la publicació és automàtica: cada cop que un PR que canvia `dashboard/` es fusiona a `main`, el flux [`publica_dashboard`](../.github/workflows/publica_dashboard.yml) en copia el contingut a `gh-pages`. També es pot llançar a mà des de la pestanya Actions.

## Com es regenera

Des de l'arrel del repositori:

```bash
python3 dashboard/genera_dashboard.py
```

L'script només fa servir la biblioteca estàndard de Python (3.11 o posterior). No fa cap petició de xarxa. El resultat és determinista: amb les mateixes dades, els mateixos fitxers. Quan canviïn les dades de `main` (i el `MANIFEST_SHA256.csv`), n'hi ha prou de tornar-lo a executar.

Per veure'l en local, obre `dashboard/index.html` al navegador (funciona amb `file://`). No cal cap servidor: la cerca i els filtres funcionen amb JavaScript al navegador, sense dependències externes.

Opcions:

- `--sha-esperat <sha256>`: s'atura si `dades/base_isin_any_v8r3.csv` no té aquest SHA-256.
- `--commit <sha>`: commit de referència que es mostra a les pàgines (per defecte, el `merge-base` amb `main`).

## Què llegeix i què no

Llegeix només, per programa:

- [`dades/base_isin_any_v8r3.csv`](../dades/base_isin_any_v8r3.csv): base oficial (clau `isin` + `any`). D'aquí surten el nom, `ceos`, `FounderCEO`, les cites `font_classificacio_*` i `d37_*`, `sim_estat_certificacio` i `sim_nivell` (només a l'«Historial de l'auditoria IA» de la fitxa) i, com a rastre secundari, `v75_urls_arxivades`.
- [`estat/estat_files.csv`](../estat/estat_files.csv): **l'únic comptador de progrés**. Totes les xifres de l'Estat, els filtres d'estat d'Empreses i l'estat de cada any a la fitxa surten d'aquí (`estat`, `c1_ceo`, `c1_ids`, `c1_tipus`, `c2_fundador`, `c2_ids`, `c3_arxiu`, `c4_coherencia`, `dubtes_oberts`, `avisos`, `regles`). Cada fila té un sol estat, en l'ordre de l'embut: falta evidència (`falta_ceo` o `falta_fundador`) → amb dubte o incoherència (`dubte_obert` o `incoherent`) → només falta l'arxiu (`falta_arxiu`) → acabada.
- [`estat/RESUM_ESTAT.md`](../estat/RESUM_ESTAT.md): només les quatre línies SHA-256 de la capçalera (per comprovar que l'estat és de les dades actuals) i, per comprovar-les, les xifres de l'embut, la fila Total i les mancances.
- [`estat/dubtes_tancats.csv`](../estat/dubtes_tancats.csv) i [`estat/urls_per_arxivar.csv`](../estat/urls_per_arxivar.csv): només el nombre de files («Dubtes tancats» i «URL a la cua d'arxiu»).
- [`docs/REGISTRE_CANVIS.csv`](../docs/REGISTRE_CANVIS.csv): font de les proves de cada fitxa (clau `id_document_o_font`; el camp `anys` s'expandeix) i dels recomptes d'entrades del pas «Com es controla la qualitat?» (`marca_veritat`, `url_wayback`, `cita_verificada_a_captura`).
- [`PENDENTS.md`](../PENDENTS.md): només els encapçalaments `## …` i les àncores `<a id="…">`, per enllaçar-hi. **Mai no se'n mostra el text.**
- [`MANIFEST_SHA256.csv`](../MANIFEST_SHA256.csv): abans d'escriure res, l'script comprova que el SHA-256 de la base, el registre, `estat/estat_files.csv`, `PENDENTS.md` i `estat/dubtes_tancats.csv` coincideix amb el del manifest.
- `dashboard/fonts_wayback_extra.csv`, **només si existeix** (ara no existeix). Columnes: `id_document_o_font`, `url_wayback` (ha de començar per `https://web.archive.org/web/`) i, opcionalment, `timestamp`. Només s'usa per a proves sense cap URL Wayback al registre, i es marca com a «fitxer extra».

No llegeix l'`.xlsx`, `empreses/*.md`, `INDEX.md`, `index.csv`, `docs/REGISTRE_CANVIS.md`, cap còpia antiga de la base ni cap fitxer de fora del repositori (resultats locals de Wayback o de verificació de cites inclosos).

## Quan s'atura

L'script s'atura sense escriure res si:

- algun dels cinc fitxers no coincideix amb `MANIFEST_SHA256.csv`;
- `estat/RESUM_ESTAT.md` no correspon a la base, el registre, `PENDENTS.md` i `estat/dubtes_tancats.csv` actuals (cal executar `python3 estat/estat_files.py`);
- `estat/estat_files.csv` no té exactament les mateixes claus (isin, any) que la base, o hi apareix un estat desconegut;
- la barra de quatre estats no quadra amb l'embut (C1∧C2 = total − falta evidència; C1∧C2∧C4 = C1∧C2 − dubte), o l'embut, la fila Total o les mancances no coincideixen amb `estat/RESUM_ESTAT.md`.

## Versió congelada

La constant `VERSIO_CONGELADA` de l'script és buida: el lloc diu «en revisió fins a la versió congelada», sense número, fins que Jordi en confirmi el nom.

## Què escriu

Només dins de `dashboard/`: `index.html`, `empreses.html`, `metodologia.html`, `empreses/{ISIN}.html` (una per ISIN; esborra les fitxes d'ISIN que ja no són a la base) i `assets/` (`style.css`, `cerca.js`, `fitxa.js`). No modifica cap altre fitxer del repositori.

## Criteris de la part pública

- **Sector ICB**: no es mostra ni es fa servir als filtres (`MOSTRA_SECTOR = False` a l'script) fins que Jordi aclareixi la llicència. Les proves del registre que són de la classificació sectorial (PDF de components STOXX) també queden ocultes.
- No es mostren mai: `pes_pct`, les columnes `founderceo_rob_*`, les propostes brutes de cada revisor de l'auditoria (columnes `sim_*` de propostes), les notes de decisió (`sim_nota`, `sim_decisio_doctorat`, `v75_decisio_jordi`, `ids_decisio`, `model_verificacio`), `FounderCEO_v75r2`, ni referències a fitxers o informes interns. Si la cita o l'URL d'una prova contenen un terme de la llista restringida, la prova es mostra com a «no mostrada», amb el seu identificador. Si una nota del registre conté noms de models o referències internes, es mostra un avís en lloc de la nota.
- Per decisió de Jordi (23/11/2026), sí que es mostren les proves de LSEG (inclosa Refinitiv), les proves amb fonts Bloomberg i les cites que contenen dates de naixement publicades per l'emissor.
- Sí que es mostren: FounderCEO oficial, CEO per any, l'estat de cada fila, marques de prova, `[V]` / `[NV]`, fonts no vàlides o sense còpia arxivada, `cita_verificada_a_captura` i, com a historial, `sim_estat_certificacio` i `sim_nivell`.
- Del fitxer `PENDENTS.md` només es compten files i s'enllacen les seccions: no se'n mostra cap text (conté notes internes).
- Les cites de més de 600 caràcters es mostren com a fragment, marcat amb […], i s'indica que el text complet és al registre.
- No s'inventa cap camp: no hi ha noms de fundadors de l'empresa, ni any de fundació, ni país com a camp de la base. El filtre «país d'emissió de l'ISIN» es deriva del prefix de l'ISIN i es marca com a derivat.

## Colors

Els tokens són a `:root` de `assets/style.css` i es redefineixen per al mode fosc. Etiquetes (text blanc ≥ 4,5:1): F `#c2521f`, P `#1f66c1`, ND `#9b2f8f` (fosc `#a8399c`), NA `#6e6d68`. L'ND és pruna i no violeta perquè el violeta `#6b4fd8` quedava massa a prop del blau de P (ΔE 10,3 en visió normal i 3,5 en deuteranopia, per sota dels llindars del validador de paleta); amb la pruna, tots els parells passen (CVD ≥ 8,5, visió normal ≥ 15,8). Estats: acabada `#1f7a3d`, només falta l'arxiu `#cfe8d6`, amb dubte `#e9a93a` (més ambre que `#f1c75b`, perquè el groc clar i el verd clar quedaven a ΔE 13,8), falta evidència `#e7e5df` amb trama. Els estats clars tenen poc contrast amb el fons: per això porten sempre icona i text, vora i separadors, i el número a la llegenda.

La metodologia que mana és la del repositori ([`AGENTS.md`](../AGENTS.md) i [`docs/METODOLOGIA.md`](../docs/METODOLOGIA.md)). La pàgina de llegenda del dashboard no la substitueix.

# Dashboard Fundadors (lloc estàtic)

Lloc HTML estàtic per consultar la base Fundadors (STOXX Europe 600, 2016-2025). Estil editorial (paper càlid, tinta, xifres i cites en serif), amb mode clar i fosc. Té tres seccions i un marc comú:

- **Marc comú** (la capçalera, el contingut i el peu fan servir el mateix contenidor d'1.240 px, alineats a la mateixa vora): capçalera amb la marca, el menú Estat / Empreses / Mètode, el **cercador amb suggeriments** (a totes les pàgines), la píndola «En revisió · dades del …» i el **botó de mode clar/fosc**. Al mòbil (≤ 760 px), el menú passa a **pestanyes inferiors fixes** i el cercador ocupa tota l'amplada a dalt.
- **Estat** (`index.html`): en quin punt és la base, amb cada secció com una pregunta numerada i la resposta en una frase. Xifra protagonista de files acabades i, just a sota, **dreceres amb recompte** (acabades, només falta l'arxiu, amb dubte, falta evidència i fundadors-CEO): cada targeta diu les files (i el % del total) i el nombre d'empreses que obre el filtre d'Empreses (`#t=…` o `#e=F`). Sota la barra apilada, la llegenda només diu què vol dir cada estat (les xifres ja són a les targetes; a la impressió, on no hi ha targetes, la llegenda les porta). Després, embut de les quatre condicions (C1-C4), estat per etiqueta i per any, mancances i què s'hi fa, origen dels dubtes oberts, controls de qualitat, resultats provisionals i «Sobre aquestes dades» (`#versio`). Es pot imprimir en dues pàgines A4.
- **Empreses** (`empreses.html`): cercador gran (també amb suggeriments; filtra la llista mentre escrius) i filtres (etiqueta, estat, país d'emissió de l'ISIN) i una taula amb la sèrie FounderCEO 2016-2025 i l'estat de les files de cada empresa. A l'escriptori, cada casella de la sèrie obre l'evidència d'aquell any a la fitxa (`#any-AAAA`, per delegació a `cerca.js`). Llegeix `?q=` i el hash (`q`, `e`, `t`, `p`, `m`).
- **Mètode** (`metodologia.html`): la pregunta, la llegenda (`#llegenda`), quan una fila està acabada, fonts A/B/C, marques de prova (`#regla-…`), l'estat antic de l'auditoria i els criteris de la part pública.
- Nom de les empreses: la columna `nom_panell` és la descripció del valor («Nestlé S.A. Namens-Aktien SF -,10»). Per mostrar-lo, `nom_visible()` en treu el sufix de classe d'acció i el nominal; el nom original surt al `title`, a la fitxa («Nom del valor a la base») i a la cerca. No es modifica `dades/`.
- Una **fitxa** per ISIN (`empreses/{ISIN}.html`):
  - Capçalera: nom, ISIN amb botó de copiar, país (prefix ISIN), anys, etiqueta dominant («x de N anys · CEO») i minibarra d'estat amb «x de N files acabades · …». Caixa de dubte si n'hi ha.
  - **Franja d'anys**: deu targetes 2016-2025 amb l'any, la lletra de l'etiqueta, la icona d'estat (a l'escriptori) i una línia de color d'estat a sota; l'any obert, remarcat. Els anys en què l'empresa no era a l'índex són targetes buides i no clicables (explicat a «Com es llegeix»). Amb el focus a la franja, les fletxes ←/→ (i Inici/Fi) passen d'any (una sola parada de tabulació; un avís visible ho diu quan el focus hi és). La franja queda enganxada a dalt en desplaçar-se (al mòbil, compacta: dues files de 40 px amb l'any i la lletra) i, quan el títol ja no es veu, mostra el nom i l'ISIN de l'empresa. La targeta remarcada segueix el desplaçament i l'any que s'obre. Sota, el CEO a 31/10 per períodes.
  - **Línia del temps vertical**, del més recent al més antic (l'any obert per defecte queda just sota la franja): un bloc per any amb l'any gran i un punt d'estat. Capçalera: «CEO a 31/10/AAAA» i el nom, l'etiqueta, «Prova: …» (enllaçada al Mètode; sense codis repetits, i els codis sense resum aprovat com «FT · vegeu el Mètode») i l'estat. Plegable «Evidència de AAAA» amb insígnies («CEO [V]», «Fundador [V]» o «Prova [V]») i la còpia arxivada de cada prova (la data només si totes dues en tenen; si no, de quina és). Obert, **dues columnes**: «Qui era el CEO» (amb la frase de la regla R2, R2b, R3 o de l'interval quan no és R1) i «Per què és fundador (F)» / «Per què no és fundador» (P) / «Per què no hi ha CEO» (NA) / «Què falta» (ND). Sota el títol de la columna 2, la frase de la prova de la cita que es mostra; si la cita és d'una altra prova que la de la columna `regles` de la base, es diu en una línia («La base classifica la fila per la regla b; aquesta cita és de la prova d») i el generador llista aquestes files a la consola. A les F, només les regles de fundador; una prova de no fundador de la mateixa fila (co-CEO) va en una línia a part. Cada columna mostra si la cita s'ha trobat al document ([V]), el nivell («Font (nivell no declarat)» si l'entrada no el diu) i l'allotjament, la cita en serif (amb l'atribut `lang` de l'idioma quan es detecta clarament), el document i la localització (de la primera nota pública, sense els fragments tècnics), «Font original ↗ · domini», «Còpia arxivada · data ↗» (o «Còpia arxivada: pendent / encara no / no n'hi ha», desactivat), «Cita comprovada a la còpia: sí / no / pendent», l'ID, «Veure la prova» i «Copia la cita» (copia la cita sencera encara que se'n mostri un fragment). Si la prova té més cites a `c2_ids` per a l'any (les altres parts d'una prova b o d), surten sota la principal en format compacte. Els intervals de CEO mostren els dos extrems i la limitació declarada (regla 28). Al peu, «Totes les proves d'aquest any (n) →» i la frase de l'estat de la fila.
  - Per defecte s'obre l'últim any amb dades; `#any-AAAA` obre i porta a aquell any. Triar un any a la franja l'obre i tanca els altres (acordió). `#p-…` obre la prova. Sense JavaScript, l'últim any queda obert i els enllaços de la franja funcionen.
  - Sota: totes les proves plegades per grup, l'historial de l'auditoria IA i Anterior / Següent.

### Cercador amb suggeriments

Patró *combobox* de l'ARIA APG: `role="combobox"`, `listbox`, `aria-activedescendant`, fletxes ↑/↓, Retorn i Esc; la drecera «/» porta al cercador (a Empreses, al de la llista) i es pot desactivar amb el botó del peu (es desa a `localStorage`, clau `fc-drecera`); Ctrl+K (⌘K) també hi porta. Ordre dels suggeriments: el nom comença així, una paraula del nom, dins del nom, ISIN, una paraula d'un CEO, dins d'un nom de CEO; en empat, el CEO actual, les empreses amb algun any F i l'ordre alfabètic. Al mòbil hi ha un sol cercador per pantalla (a Empreses, el de la llista; a l'Estat, el de la capçalera); entre 761 i 1.100 px, el de la capçalera ocupa una fila sencera. Busca per nom (sense accents ni majúscules), altres noms de la base, ISIN i nom de CEO. Cada suggeriment mostra el nom, l'ISIN, els CEO que coincideixen (o el de l'últim any) i la sèrie F/P de deu anys amb la línia d'estat. Retorn sense cap suggeriment triat porta a `empreses.html?q=…`. L'índex és a `assets/index_cerca.js` (≈ 160 kB, compartit per totes les pàgines i carregat només quan s'enfoca un cercador; és JS i no JSON perquè funcioni amb `file://`). Només conté dades que ja són a `empreses.html`, i el generador s'atura si hi troba un terme restringit.

### Mode clar i fosc

El botó de la capçalera canvia entre clar i fosc i desa l'opció a `localStorage` (clau `fc-tema`, dins un `try/catch`). Si no n'hi ha cap de desada, mana `prefers-color-scheme`. Un script petit al `<head>` aplica l'opció abans de pintar (atribut `data-theme` a `<html>`). Els tokens foscos són propis (no una inversió) i només s'apliquen a la pantalla: la impressió de l'Estat surt sempre en clar, en dues pàgines A4.

**Publicat a GitHub Pages** (https://jmasoribas-max.github.io/base-fundadors-ceo-stoxx600/), des de la branca `gh-pages`. La primera publicació la va fer el compte de Jordi el 23/11/2026 a les 14:00 (commit `64ce9cc`, `main` `17b03df`). Des del 24/11/2026, la publicació és automàtica: cada cop que un PR que canvia `dashboard/` es fusiona a `main`, el flux [`publica_dashboard`](../.github/workflows/publica_dashboard.yml) en copia el contingut a `gh-pages`. També es pot llançar a mà des de la pestanya Actions.

## Com es regenera

Des de l'arrel del repositori:

```bash
python3 dashboard/genera_dashboard.py
```

L'script només fa servir la biblioteca estàndard de Python (3.11 o posterior). No fa cap petició de xarxa. El resultat és determinista: amb les mateixes dades, els mateixos fitxers. Quan canviïn les dades de `main` (i el `MANIFEST_SHA256.csv`), n'hi ha prou de tornar-lo a executar.

Per veure'l en local, obre `dashboard/index.html` al navegador (funciona amb `file://`). No cal cap servidor: la cerca, els suggeriments, els filtres i el mode fosc funcionen amb JavaScript al navegador, sense dependències externes ni fonts web (les serifs són les del sistema: Iowan Old Style, Palatino, Charter, Georgia…).

Opcions:

- `--sha-esperat <sha256>`: s'atura si `dades/base_isin_any_v8r3.csv` no té aquest SHA-256.
- `--commit <sha>`: commit de referència que es mostra a les pàgines (per defecte, el `merge-base` amb `main`).

## Què llegeix i què no

Llegeix només, per programa:

- [`dades/base_isin_any_v8r3.csv`](../dades/base_isin_any_v8r3.csv): base oficial (clau `isin` + `any`). D'aquí surten el nom, `ceos`, `FounderCEO`, les cites `font_classificacio_*` i `d37_*`, `sim_estat_certificacio` i `sim_nivell` (només a l'«Historial de l'auditoria IA» de la fitxa) i, com a rastre secundari, `v75_urls_arxivades`.
- [`estat/estat_files.csv`](../estat/estat_files.csv): **l'únic comptador de progrés**. Totes les xifres de l'Estat, els filtres d'estat d'Empreses i l'estat de cada any a la fitxa surten d'aquí (`estat`, `c1_ceo`, `c1_ids`, `c1_tipus`, `c2_fundador`, `c2_ids`, `c3_arxiu`, `c4_coherencia`, `dubtes_oberts`, `avisos`, `regles`). Cada fila té un sol estat, en l'ordre de l'embut: falta evidència (`falta_ceo` o `falta_fundador`) → amb dubte o incoherència (`dubte_obert` o `incoherent`) → només falta l'arxiu (`falta_arxiu`) → acabada.
- [`estat/RESUM_ESTAT.md`](../estat/RESUM_ESTAT.md): només les quatre línies SHA-256 de la capçalera (per comprovar que l'estat és de les dades actuals) i, per comprovar-les, les xifres de l'embut, la fila Total i les mancances.
- [`estat/dubtes_tancats.csv`](../estat/dubtes_tancats.csv): només el nombre de files («Dubtes tancats»).
- «URL a la cua d'arxiu» **es calcula del registre actual**, amb la mateixa regla que [`estat/llista_urls_arxiu.py`](../estat/llista_urls_arxiu.py): una URL hi entra si té `url_font` http(s), cita i `funcio_cita` `ceo`, `fundador`, `context` o `datacio`, i cap entrada amb aquella URL no té `cita_verificada_a_captura=si`. De [`estat/urls_per_arxivar.csv`](../estat/urls_per_arxivar.csv) només se'n compta el nombre de files per avisar a la consola si està desfasat (no es publica).
- [`estat/estat_files.py`](../estat/estat_files.py): se n'importa la funció que decideix si una cita anomena el CEO (sense escriure bytecode), per triar a l'evidència de l'any de la fitxa la mateixa prova que fa complir la condició quan la llista `c1_ids` o `c2_ids` és truncada («(+n)»).
- [`docs/METODOLOGIA_3_Articles_v0.10.10.md`](../docs/METODOLOGIA_3_Articles_v0.10.10.md): només per trobar el número de línia de les regles sense resum aprovat (FT, D10, D10b_prelacio, d_per_part, b_per_part, holding_interposada) i enllaçar-hi (`?plain=1#L…`). Si no troba la línia, enllaça el fitxer sencer.
- [`docs/REGISTRE_CANVIS.csv`](../docs/REGISTRE_CANVIS.csv): font de les proves de cada fitxa (clau `id_document_o_font`; el camp `anys` s'expandeix) i dels recomptes d'entrades del pas «Com es controla la qualitat?» (`marca_veritat`, `url_wayback`, `cita_verificada_a_captura`).
- [`PENDENTS.md`](../PENDENTS.md): només els encapçalaments `## …` i les àncores `<a id="…">`, per enllaçar-hi. **Mai no se'n mostra el text.**
- [`MANIFEST_SHA256.csv`](../MANIFEST_SHA256.csv): abans d'escriure res, l'script comprova que el SHA-256 de la base, el registre, `estat/estat_files.csv`, `PENDENTS.md` i `estat/dubtes_tancats.csv` coincideix amb el del manifest.
- `dashboard/fonts_wayback_extra.csv`, **només si existeix** (ara no existeix). Columnes: `id_document_o_font`, `url_wayback` (ha de començar per `https://web.archive.org/web/`) i, opcionalment, `timestamp`. Només s'usa per a proves sense cap URL Wayback al registre, i es marca com a «fitxer extra».

No llegeix l'`.xlsx`, `empreses/*.md`, `INDEX.md`, `index.csv`, `docs/REGISTRE_CANVIS.md`, cap còpia antiga de la base ni cap fitxer de fora del repositori (resultats locals de Wayback o de verificació de cites inclosos).

## Quan s'atura

L'script s'atura sense escriure res si:

- algun dels cinc fitxers no coincideix amb `MANIFEST_SHA256.csv`;
- alguna fila acabada no mostra, a l'«Evidència de l'any» de la fitxa, una cita de CEO i una de fundador amb «Cita comprovada a la còpia: sí»;
- l'índex del cercador conté un terme de la llista restringida, o un dels exemples del cercador de l'Estat (LVMH, Nestlé) no és a la base;
- `estat/RESUM_ESTAT.md` no correspon a la base, el registre, `PENDENTS.md` i `estat/dubtes_tancats.csv` actuals (cal executar `python3 estat/estat_files.py`);
- `estat/estat_files.csv` no té exactament les mateixes claus (isin, any) que la base, o hi apareix un estat desconegut;
- la barra de quatre estats no quadra amb l'embut (C1∧C2 = total − falta evidència; C1∧C2∧C4 = C1∧C2 − dubte), o l'embut, la fila Total o les mancances no coincideixen amb `estat/RESUM_ESTAT.md`.

## Versió congelada

La constant `VERSIO_CONGELADA` de l'script és buida: el lloc diu «en revisió fins a la versió congelada», sense número, fins que Jordi en confirmi el nom.

## Què escriu

Només dins de `dashboard/`: `index.html`, `empreses.html`, `metodologia.html`, `empreses/{ISIN}.html` (una per ISIN; esborra les fitxes d'ISIN que ja no són a la base) i `assets/` (`style.css`; `comu.js`: mode clar/fosc, cercador amb suggeriments i botons de copiar; `index_cerca.js`: índex del cercador; `cerca.js`: filtres d'Empreses; `fitxa.js`: franja d'anys, obertura per hash i filtre de proves). No modifica cap altre fitxer del repositori.

## Criteris de la part pública

- **Sector ICB**: no es mostra ni es fa servir als filtres (`MOSTRA_SECTOR = False` a l'script) fins que Jordi aclareixi la llicència. Les proves del registre que són de la classificació sectorial (PDF de components STOXX) també queden ocultes.
- No es mostren mai: `pes_pct`, les columnes `founderceo_rob_*`, les propostes brutes de cada revisor de l'auditoria (columnes `sim_*` de propostes), les notes de decisió (`sim_nota`, `sim_decisio_doctorat`, `v75_decisio_jordi`, `ids_decisio`, `model_verificacio`), `FounderCEO_v75r2`, ni referències a fitxers o informes interns. Si la cita o l'URL d'una prova contenen un terme de la llista restringida, la prova es mostra com a «no mostrada», amb el seu identificador. Si una nota del registre conté noms de models o referències internes, es mostra un avís en lloc de la nota.
- Per decisió de Jordi (23/11/2026), sí que es mostren les proves de LSEG (inclosa Refinitiv), les proves amb fonts Bloomberg i les cites que contenen dates de naixement publicades per l'emissor.
- Sí que es mostren: FounderCEO oficial, CEO per any, l'estat de cada fila, marques de prova, `[V]` / `[NV]`, fonts no vàlides o sense còpia arxivada, `cita_verificada_a_captura` i, com a historial, `sim_estat_certificacio` i `sim_nivell`.
- Del fitxer `PENDENTS.md` només es compten files i s'enllacen les seccions: no se'n mostra cap text (conté notes internes).
- Les notes del registre es mostren (a «Detalls tècnics» de cada prova) amb els filtres de termes restringits i de noms de models, però **sense** filtrar les mencions a DF (p. ex. «correcció de DF»): hi ha 28 fitxes amb notes d'aquest tipus. Si Jordi vol el mateix criteri que per a `PENDENTS.md`, cal afegir `\bDF\b` al filtre de notes de `prepara_prova()`.
- A l'«Evidència de l'any», la línia del document surt de la primera nota **pública** de l'entrada (el text que segueix «Document:», o la nota marcada «Nota:»), retallada a 230 caràcters; el nivell A/B/C, del camp d'origen o d'aquesta nota. Les notes ocultes pels filtres no s'hi fan servir mai.
- Les cites de més de 600 caràcters es mostren com a fragment, marcat amb […], i s'indica que el text complet és al registre.
- No s'inventa cap camp: no hi ha noms de fundadors de l'empresa, ni any de fundació, ni país com a camp de la base. El filtre «país d'emissió de l'ISIN» es deriva del prefix de l'ISIN i es marca com a derivat.

## Colors

Els tokens són a `:root` de `assets/style.css` i es redefineixen per al mode fosc **només a la pantalla**: sota `@media screen and (prefers-color-scheme: dark)` amb `:root:not([data-theme="light"])` i sota `@media screen` amb `:root[data-theme="dark"]`. La impressió surt sempre en clar. Neutres (estil editorial): paper `#f7f4ec`, full `#fffdf8`, tinta `#1d1b16` (fosc: `#151411`, `#1c1a17`, `#efebe1`). Etiquetes (text blanc ≥ 4,5:1): F `#c2521f`, P `#1f66c1`, ND `#9b2f8f` (fosc `#a8399c`), NA `#6e6d68`. L'ND és pruna i no violeta perquè el violeta `#6b4fd8` quedava massa a prop del blau de P (ΔE 10,3 en visió normal i 3,5 en deuteranopia); amb la pruna, tots els parells passen.

Estats, en dos jocs:

- **Marques** (`--mk-*`: barra de quatre estats, franja de la sèrie d'Empreses, minibarres, embut, barres de la taula per any, mostres de llegenda): clar acabada `#1f7a3d`, només falta l'arxiu `#86c9a0`, amb dubte `#e9a93a`, falta evidència `#8a8882` (amb trama a les barres); fosc `#9be3b5`, `#3b9a6b`, `#d9a93a`, `#5a5954`. Validades amb `validate_palette.js --pairs all` (qualsevol estat pot quedar al costat de qualsevol altre): en clar, CVD ≥ 10,8 i visió normal ≥ 15,5; en fosc, CVD ≥ 11,9 i visió normal ≥ 16,9. Amb el paper nou es van tornar a validar sobre `#fffdf8` i `#f7f4ec` (clar) i `#1c1a17` i `#151411` (fosc), amb el mateix resultat. Els tons clars d'arxiu i dubte queden per sota de 3:1 contra el paper (1,8-2,0:1) i el gris fosc de «falta» a 2,5:1: per això les barres porten vora i separadors, cada marca porta icona o lletra i els números són a la llegenda (la regla de *relief* del validador). **Vora de contrast (24/11/2026):** sense canviar els farciments validats, totes les marques d'estat (barra apilada, minibarres, línies de la franja i de la sèrie, punts de la línia del temps, mostres de llegenda) porten una vora interior d'1 px del mateix to que arriba a 3:1 contra el paper (`--mk-*-vora`): clar `#1f7a3d` (5,3:1), `#3d8c5c` (3,7-4,1:1), `#9a6a12` (4,3-4,7:1), `#8a8882` (3,2-3,5:1); fosc `#9be3b5`, `#3b9a6b` (5,0-5,3:1), `#d9a93a` (8,0:1), `#8e8c86` (5,2-5,5:1). `validate_palette.js` dona «Contrast vs surface: PASS» a tots quatre en clar (`#fffdf8`, `#f7f4ec`) i en fosc (`#1c1a17`, `#151411`); les altres comprovacions del validador (croma del gris, distància entre les vores verdes) no s'hi apliquen perquè les vores no són una paleta categòrica: la categoria la porten els farciments ja validats i la icona. El gris de «falta» és un neutre volgut (no passa el llindar de croma, que és per a sèries categòriques). Els verds proposats a la revisió (`#3d8f63` per a l'arxiu) quedaven a ΔE 7,9 de l'acabada i no passaven. La franja de la sèrie fa 5 px i va separada de la lletra per una línia de 2 px del color de la superfície.
- **Insígnies amb text** (`--st-*`, to suau): acabada `#1f7a3d` (text blanc), arxiu `#cfe8d6`, dubte `#e9a93a`, falta `#e7e5df` amb trama (text `#1a1a19`). Porten sempre icona i text.

La taula «Com va cada any?» no fa servir intensitat de fons: cada cel·la porta el número, el % de l'any i una barra de longitud en el color de l'estat. Amb una escala de 5 graons, el validador (`--ordinal`) no podia separar els graons i alhora mantenir el text ≥ 4,5:1, i els talls de 20 en 20 punts creaven salts falsos (21 % vs 20 %).

La metodologia que mana és la del repositori ([`AGENTS.md`](../AGENTS.md) i [`docs/METODOLOGIA.md`](../docs/METODOLOGIA.md)). La pàgina de llegenda del dashboard no la substitueix.

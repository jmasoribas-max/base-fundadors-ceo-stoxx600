# Dashboard Fundadors (prototip estàtic)

Lloc HTML estàtic per consultar la base Fundadors (STOXX Europe 600, 2016-2025): una pàgina d'inici amb cercador i taula filtrable, una fitxa per cada ISIN (CEO a 31/10 de cada any, etiqueta FounderCEO, certificació i proves amb cita literal, font original i còpia Wayback quan consta) i una pàgina de metodologia i llegenda.

**No està publicat a GitHub Pages i Pages no està activat.** Això només es farà amb l'OK explícit de Jordi.

## Com es regenera

Des de l'arrel del repositori:

```bash
python3 dashboard/genera_dashboard.py
```

L'script només fa servir la biblioteca estàndard de Python (3.10 o posterior). No fa cap petició de xarxa. El resultat és determinista: amb les mateixes dades, els mateixos fitxers. Quan canviïn les dades de `main` (i el `MANIFEST_SHA256.csv`), n'hi ha prou de tornar-lo a executar.

Per veure'l en local, obre `dashboard/index.html` al navegador. No cal cap servidor: la cerca i els filtres funcionen amb JavaScript al navegador, sense dependències externes.

Opcions:

- `--sha-esperat <sha256>`: s'atura si `dades/base_isin_any_v8r3.csv` no té aquest SHA-256.
- `--commit <sha>`: commit de referència que es mostra a les pàgines (per defecte, el `merge-base` amb `main`).

## Què llegeix i què no

Llegeix només, per programa:

- [`dades/base_isin_any_v8r3.csv`](../dades/base_isin_any_v8r3.csv): base oficial (clau `isin` + `any`). D'aquí surten el nom, `ceos`, `FounderCEO`, `sim_estat_certificacio`, `sim_nivell`, `sim_ceo_aplicat`, les cites `font_classificacio_*` i `d37_*` i, com a rastre secundari, `v75_urls_arxivades`.
- [`docs/REGISTRE_CANVIS.csv`](../docs/REGISTRE_CANVIS.csv): font principal de les proves. El camp `anys` s'expandeix i cada entrada s'enllaça amb les files `isin` + `any` que cobreix. La clau de cada prova és `id_document_o_font`.
- [`MANIFEST_SHA256.csv`](../MANIFEST_SHA256.csv): abans d'escriure res, l'script comprova que el SHA-256 de la base i del registre coincideix amb el del manifest. Si no coincideix, s'atura.
- `dashboard/fonts_wayback_extra.csv`, **només si existeix** (ara no existeix). Columnes: `id_document_o_font`, `url_wayback` (ha de començar per `https://web.archive.org/web/`) i, opcionalment, `timestamp`. Només s'usa per a proves sense cap URL Wayback al registre, i es marca com a «fitxer extra».

No llegeix l'`.xlsx`, `empreses/*.md`, `INDEX.md`, `index.csv`, `docs/REGISTRE_CANVIS.md`, cap còpia antiga de la base ni cap fitxer de fora del repositori (resultats locals de Wayback o de verificació de cites inclosos).

## Què escriu

Només dins de `dashboard/`: `index.html`, `metodologia.html`, `empreses/{ISIN}.html` (una per ISIN; esborra les fitxes d'ISIN que ja no són a la base) i `assets/` (`style.css`, `cerca.js`, `fitxa.js`). No modifica cap altre fitxer del repositori.

## Criteris de la part pública

- **Sector ICB**: no es mostra ni es fa servir als filtres (`MOSTRA_SECTOR = False` a l'script) fins que Jordi aclareixi la llicència. Les proves del registre que són de la classificació sectorial (PDF de components STOXX) també queden ocultes.
- No es mostren mai: `pes_pct`, les columnes `founderceo_rob_*`, les propostes brutes dels models (`sim_*_chatgpt`, `sim_*_claude`), les notes de decisió (`sim_nota`, `sim_decisio_doctorat`, `v75_decisio_jordi`, `ids_decisio`, `model_verificacio`), `FounderCEO_v75r2`, ni res de proveïdors de dades amb llicència. Si la cita o l'URL d'una prova contenen un terme de la llista restringida, la prova es mostra com a «no mostrada», amb el seu identificador. Si una nota del registre conté noms de models o referències internes, es mostra un avís en lloc de la nota.
- Sí que es mostren: FounderCEO oficial, CEO per any, `sim_estat_certificacio` i `sim_nivell`, marques de prova, `[V]` / `[NV]`, fonts no vàlides o sense còpia arxivada, i `cita_verificada_a_captura`.
- Les cites de més de 600 caràcters es mostren com a fragment, marcat amb […], i s'indica que el text complet és al registre.
- No s'inventa cap camp: no hi ha noms de fundadors de l'empresa, ni any de fundació, ni país com a camp de la base. El filtre «país d'emissió de l'ISIN» es deriva del prefix de l'ISIN i es marca com a derivat.

La metodologia que mana és la del repositori ([`AGENTS.md`](../AGENTS.md) / [`CLAUDE.md`](../CLAUDE.md) i [`docs/METODOLOGIA.md`](../docs/METODOLOGIA.md)). La pàgina de llegenda del dashboard no la substitueix.

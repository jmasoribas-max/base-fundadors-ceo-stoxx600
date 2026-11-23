# Auditoria de l'estat de la base de fundadors-CEO (23/11/2026)

- **Autor:** Claude (agent), per encàrrec de Jordi. Proposta de treball: no és una decisió ni modifica cap dada.
- **Objecte:** repositori `jmasoribas-max/base-fundadors-ceo-stoxx600`, `main` a `17b03df` (fusió del PR #20, dashboard, 23/11/2026 14:00 Europe/Madrid).
- **Metodologia de referència:** `METODOLOGIA_3_Articles_v0.10.10.md` (fitxer adjunt pel traspàs; no és al repositori) i `CLAUDE.md`.
- **Convenció:** [V] = calculat o comprovat en aquesta auditoria sobre els fitxers de `main`; [NV] = no comprovat aquí; [C] = criteri o opinió de l'auditor.
- **Reproduïbilitat:** els recomptes surten de `docs/auditoria_20261123/cobertura.py`; la comprovació per mostra, de `docs/auditoria_20261123/mostra_verificacio.py` (llavor 20261123), amb el resultat a `docs/auditoria_20261123/mostra_resultat.csv`.

## 0. Resum en deu punts

1. **El panell és sòlid i està congelat** [V]: 6.012 files ISIN-any, 1.040 ISIN, 2016-2025. FounderCEO: F 349 (88 ISIN), P 5.631, NA 31, ND 1 (Sopra Steria 2025). Mostra principal J14: 5.967 (F 348, P 5.619). Els SHA del CSV, l'xlsx, el sector i el registre coincideixen amb els del traspàs.
2. **L'enfocament metodològic és correcte i defensable** [C]: CEO-primer com Fahlenbrach (2009) i Adams, Almeida i Ferreira (2009), i amb un estàndard més exigent que la literatura (un 0 necessita prova positiva). El risc és la proliferació de regles i decisions cas per cas, no el fons.
3. **Les cites que hi ha són fiables** [V]: en una mostra independent de 87 cites del registre, de les 72 que s'han pogut obrir, 71 hi són (68 literals, 1 gairebé literal i 2 reconstruïdes de cel·les d'una taula) i 1 no és concloent (pàgina amb JavaScript). No s'ha trobat cap cita inventada.
4. **Però la cobertura d'evidència dins el repositori és del 67,7 %** [V]: de les 5.980 files F+P, 4.048 tenen alhora cita de CEO (que anomena la persona) i cita de classificació. En falten **1.932**.
5. **El problema greu és el grup F, que és el tractament de la tesi** [V]: només **44 de 349 files F** (12,6 %) estan completes, i només **9 de 88 empreses F** ho estan en tots els seus anys F. Hi ha 302 files F sense cita de CEO al registre.
6. **Paradoxa de la certificació** [V]: les 1.773 files «certificades» (N1/N2/doctorat) són les que tenen menys evidència al repositori: **0 cites de CEO** al registre i 1.247 sense cap cita estructurada. La certificació es va fer amb l'acord de dos models d'IA amb cites que no s'han traspassat al repositori. Un tercer (el tribunal) no la pot comprovar.
7. **La durabilitat (Wayback) està gairebé per fer** [V]: només 744 de les 11.582 entrades del registre (6,4 %) tenen la cita verificada a la captura. Les files amb les dues cites verificades a Wayback són 302 (5,1 %). Els lots 6-10 (5.862 entrades) no s'han passat mai per l'script. La metodologia (D29) exigeix captura per a cada document.
8. **El CSV oficial té incoherències conegudes i no aplicades** [V]: p. ex. Enagás 2016-2021 i Bellway 2017 tenen a `ceos` un CEO diferent del que va decidir Doctorat (`sim_ceo_aplicat`); Cellnex 2016-2022 és F amb regla `b` (prova de no fundador); 37 files P no tenen cap prova de «no» a `regles`. L'estat de certificació no s'ha actualitzat després dels lots 4-10.
9. **Falten peces que la metodologia demana i que la base no té** [V]: la taula d'episodis de CEO amb dates (la «peça central dels tres articles», §1.3), la categoria H (hereu) i FounderChair, i els camps estructurats de la prova b (any de fundació i any de naixement). Tampoc no s'ha començat la doble codificació humana amb kappa (regla 12), que és la validació que més pesarà davant el tribunal.
10. **La sensació de no avançar té causes concretes** [C]: no hi ha una definició mecànica i única de «fila acabada»; conviuen tres sistemes d'evidència (paquets antics, auditoria IA r3e/r4 i registre nou); els lots s'han centrat en les files `fora_mostra` (ara cobertes al 96 %) mentre les F i les certificades quedaven enrere; i la verificació Wayback depèn d'un script a l'ordinador de casa.

## 1. Què he revisat i com

- Tots els fitxers de `main`: `dades/` (CSV de 158 columnes, xlsx i sector), `docs/REGISTRE_CANVIS.csv` (11.582 entrades), `PENDENTS.md`, les 1.040 fitxes, `lots/`, `scripts/`, CI, `README.md`, `docs/*`.
- Recomptes propis, sense copiar xifres d'informes anteriors. Definició **estricta** de cita vàlida: entrada del registre amb cita literal i URL, `marca_veritat=[V]`, sense `no_valida` a les notes. Per al CEO, a més, la cita ha d'anomenar la persona (cognom de `ceos`) i `funcio_cita=ceo`. Per a la classificació, `funcio_cita=fundador` al registre o la columna antiga `font_classificacio_cita` del CSV.
- Comprovació independent per mostra: 87 entrades `ceo`/`fundador` [V], estratificades per origen (lots 2-10 i ajustos DF), re-descarregades del web original (Wayback no és accessible des del meu entorn) i cercades literalment al text extret (`pdftotext` o HTML).
- Validadors del repositori sense `--live`: `valida_pr.py` i `comprova_enllacos_cites.py` donen **0 problemes** [V]. Atenció: són validadors de format (fitxes, valors permesos, forma de les URL). No comproven que la cita sigui al document, que la prova lligui amb l'etiqueta ni la coherència entre columnes.

Límits d'aquesta auditoria: no he obert el box ni el Drive (sortides r3e/r4, inventari de fonts antic); no he comprovat el contingut semàntic de les cites (si diuen el que se n'afirma, error E4) més enllà de la mostra; no he pogut provar Wayback.

## 2. Fotografia de l'estat actual [V]

### 2.1 Cobertura d'evidència per fila

| Etiqueta | Files | Cita de CEO que anomena la persona | Cita de classificació | Totes dues | Cap de les dues | Totes dues verificades a Wayback |
|---|---:|---:|---:|---:|---:|---:|
| F (`1`) | 349 | 47 (13,5 %) | 211 (60,5 %) | **44 (12,6 %)** | 135 | 0 |
| P (`0`) | 5.631 | 4.049 (71,9 %) | 4.490 (79,7 %) | 4.004 (71,1 %) | 1.095 | 302 |
| NA | 31 | 0 | 2 | 0 | 29 | 0 |
| ND | 1 | 1 | 1 | 1 | 0 | 0 |
| **Total** | **6.012** | **4.097 (68,1 %)** | **4.704 (78,2 %)** | | **1.259** | |

- Files F+P sense alguna de les dues cites: **1.932** (1.884 sense cita de CEO; 1.279 sense cita de classificació).
- 122 files (120 P, 40 ISIN) tenen cita de CEO però la cita no anomena la persona (p. ex. «CEO since October 1, 2019», extret d'un CV). `CLAUDE.md` §3 demana que la cita anomeni persona i càrrec.
- 547 cites de CEO usen fórmules de tinença («since», «from… until», «seit»…): són vàlides per D21, però la metodologia (D27) demana etiquetar aquests anys com a `reculada_per_tinenca`, i el registre no té aquest camp.
- 754 files P es basen només en la prova c (64 anys), que la metodologia qualifica de «criteri, no evidència». Ja hi ha la robustesa `founderceo_rob_c_com_nd`.

### 2.2 Cobertura segons l'estat de certificació

| Estat a la base | Files | Totes dues cites al repositori | Cap cita estructurada |
|---|---:|---:|---:|
| `certificada` (N1/N2/doctorat) | 1.773 | **0** | **1.247** |
| `certificada_ceo_pendent` | 108 | 105 | 0 |
| `no_certificada` | 241 | 208 | 11 |
| `fora_mostra_auditoria` | 3.890 | 3.736 (96,0 %) | 1 |

- Les 3.890 files `fora_mostra` ja han passat totes pels lots 4-8 (3.883) i pel lot 3 (Jyske, 7), però el CSV encara les diu `fora_mostra_auditoria`.
- 302 de les 349 F són `certificada`: per això el grup F és el pitjor documentat.

### 2.3 Grup F (88 empreses)

| | Empreses |
|---|---:|
| Amb cita de classificació a tots els anys F | 48 |
| Amb cita de CEO a tots els anys F | 10 |
| Completes (CEO i classificació) a tots els anys F | **9** |

Falten: 302 files F sense cita de CEO (78 empreses) i 138 files F sense cita de classificació (40 empreses).

### 2.4 Durabilitat (Wayback)

- Entrades del registre amb `cita_verificada_a_captura=si`: **744** (6,4 %). Amb `no`: 4.934 (sobretot perquè l'script no va poder accedir a la captura o no n'hi havia). Buides: 5.904 (els lots 6-10 no s'han passat mai).
- URL distintes citades com a prova de CEO o de fundador: **5.805**; amb la cita verificada a la captura: **394**.
- La verificació depèn d'un script a l'ordinador de casa de Jordi; l'últim estat escrit és d'un run del 21/11 en curs [NV].

### 2.5 Comprovació independent per mostra

| Resultat | Entrades |
|---|---:|
| Cita trobada literalment | 68 |
| Cita gairebé literal (salt de línia d'un PDF) | 1 |
| Contingut present, però la «cita» ajunta cel·les d'una taula (BME 2019, Generali 2024) | 2 |
| No concloent (pàgina que es construeix amb JavaScript; Kinnevik) | 1 |
| No accessible des d'aquí (403, SEC, servidor que talla) | 15 |
| **Cita no trobada en un document llegit** | **0** |

Lectura [C]: quan el document s'obre, les cites del registre hi són. El risc no és la invenció, sinó (a) que no s'hagin traspassat al repositori, (b) que no estiguin arxivades i (c) l'adequació semàntica (si la cita prova el que diu la regla), que aquesta mostra no avalua.

### 2.6 Coherència interna del CSV oficial

| Problema | Files | Exemples |
|---|---:|---|
| `ceos` ≠ `sim_ceo_aplicat` (decisió de Doctorat no aplicada a `ceos`) | 7 | Enagás 2016-2021 (`ceos` Llardén, president executiu; Doctorat: Oreja, consejero delegado, R1); Bellway 2017 (`ceos` John Watson; Doctorat: Ted Ayres) |
| CEO probablement incorrecte per la P5 (president executiu amb consejero delegado) | 2 | BME 2017-2018 (`ceos` Zoido; l'IAGC 2017 dona Hernani consejero delegado des del 27/4/2017). Ja és a `PENDENTS.md` (regla 29) |
| F amb una regla de «no» a `regles` | 7 | Cellnex 2016-2022 (`regles=b`; la nota diu «P passa a 1, D37») |
| P sense cap prova de «no» a `regles` | 37 | AB InBev 2021-2025 (`cap`, però la nota diu «regla b»), Stora Enso 2020-2022, Unicaja 2025, Vantage Towers 2022, Mandatum 2025, Knorr-Bremse 2019-2020 i Pandora 2018 (`R-SC;R2b`) |
| P amb regla de «sí» | 2 | Harbour 2022-2023 (`cita_fundador`; la decisió és 0 per e) |
| `motiu_nd` ple en files que ja no són ND | 28 | antics ND passats a P |
| `sim_estat_certificacio` no actualitzat després dels lots 4-10 | 4.239 | les 3.890 `fora_mostra` i les 349 dels lots 2, 3 i 9 |

Risc sistemàtic [C]: els casos Enagás i BME apunten a un patró (empreses espanyoles i italianes amb president executiu i consejero delegado). Convé una revisió dirigida d'aquest patró a tota la base.

### 2.7 Documentació i estructura

- La metodologia vigent (v0.10.10) no és al repositori; `docs/METODOLOGIA.md` és un resum de la v0.10.7.
- `PENDENTS.md` és un registre acumulatiu, no un estat: la secció 1 conserva 366 files de llistes del 19/11, moltes ja treballades als lots 2, 3 i 9.
- El CSV té 158 columnes; unes 100 són de procés (x5_*, v75_*, sim_*, packs) i el diccionari les descriu només com a «camp heretat». No hi ha definida la base final neta.
- L'inventari de fonts antic (identificadors `WBF…`, paquets X2-X14 a `ids_fonts`, 5.655 files) i les sortides de l'auditoria r3e/r4 no són al repositori.
- El registre no té els camps que la metodologia exigeix per a cada font (D23, D27-D29): nivell A/B, extracte amb context, data del document, `http_status`, SHA-256 del document, `arxiu_durable`, `verificada_A`/`reculada_per_tinenca`. Hi són en text lliure a `notes`, o no hi són. `marca_prova` té més de cent formats diferents i, al lot 3, les entrades de fundador porten marques de CEO.
- Aspectes de procés: el lot 7 va tenir 2.391 files i 500 ISIN en un dia (la norma és de 250-300 files); la validació de DF del lot 10 va ser per una mostra de 6 files.

## 3. Què està bé i s'ha de mantenir

- Univers reproduïble (informes de l'ETF), panell congelat i una línia per empresa i any.
- Enfocament CEO-primer, data de referència 31/10 i regles R1-R3/R-SC explícites.
- Estàndard d'evidència exigent: només fonts A/B, cita literal, URL; un 0 necessita prova positiva; sense prova, ND.
- Robusteses previstes per a cada decisió discutible (c, FT, D37a/b, escissions, R3, etc.).
- Govern amb Git: `main` protegida, PR, registre on no s'esborra res, SHA de cada fitxer, distinció [V]/[NV]. És una bona base per al paquet de replicació i per a Zenodo.
- Unes 4.000 files ja tenen cita de CEO i de classificació, i la mostra indica que aquestes cites són correctes.

## 4. És adequat l'enfocament? [C]

**Metodologia: sí, amb una condició.** El fons és correcte i és més rigorós que el dels papers de referència. Però el text acumula 29 regles, D1-D37, dos jocs de P1-P9 amb significats diferents, J, K, L i X, i moltes decisions per empresa («decisió de Jordi»). Davant el tribunal això es pot llegir com a decisions ad hoc. Recomano un **codi de codificació consolidat** (codebook v1.0): una taula de regles amb identificadors únics, el criteri general de cadascuna i un **registre de casos decidits** a part (qui, quan, per què, quina robustesa els treu).

**Organització del treball: cal un canvi.**

1. **Una sola mètrica d'«acabat».** Ara cada agent compta diferent (certificada, feta, [V], N1/N2). Proposo un script que calculi, per a cadascuna de les 6.012 files, si compleix els requisits de fila acabada (secció 5) i en tregui un resum. Cada lot ha de fer moure aquest comptador; és la manera de veure el progrés.
2. **Un sol sistema d'evidència: el registre.** La certificació per acord de models d'IA (N1/N2) és una eina interna i la metodologia ja ho diu. El que valida davant el tribunal és la cita A/B arxivada per fila i la doble codificació humana amb kappa.
3. **Prioritzar el grup F**, que és el tractament de l'article 1 i on hi ha menys evidència.
4. **Treure el coll d'ampolla de Wayback** de l'ordinador de casa i fer-lo reproduïble.
5. **Menys capes de coordinació.** Hi ha molta feina en traspassos, recàlculs i redocumentació de decisions «segons DF». Proposo que les decisions es registrin una sola vegada (registre de casos) i que la feina de producció es faci en lots petits verificats automàticament.

## 5. Definició proposada de «base acabada»

Per a cada fila de la mostra principal (F o P):

1. **CEO:** almenys una cita A/B [V], d'un document del mateix exercici, que anomeni la persona i el càrrec; o un interval de la regla 28 (dues entrades `ceo_interval`).
2. **Classificació:** almenys una cita A/B [V] amb la prova coherent amb l'etiqueta (a-e per a un 0; D37, cita directa, FT o D10 per a un 1) i, per a la prova b, l'any de fundació i l'any de naixement estructurats.
3. **Durabilitat:** cada document citat té captura Wayback i la cita s'ha verificat a la captura per script (o consta com a limitació `arxiu_durable=false`, amb motiu).
4. **Coherència:** `ceos`, `regles`, marques i robusteses coherents amb l'evidència; cap dubte obert a la fila.

Per a NA: cerca R-SC exhaustiva documentada. Per a ND: cerca exhaustiva documentada (A.4).

A nivell de base: metodologia vigent al repositori; marques i robusteses de les regles 25-29 calculades; doble codificació humana feta i kappa reportat; congelació (FounderCEO v1.0.0) amb SHA i DOI de Zenodo.

## 6. Què falta per acabar (mida de cada forat) [V]

| Forat | Files | Empreses |
|---|---:|---:|
| F sense cita de CEO | 302 | 78 |
| F sense cita de classificació | 138 | 40 |
| P sense cita de CEO | 1.582 | 299 |
| P sense cita de classificació | 1.141 | 209 |
| NA sense evidència R-SC al registre | 29 | 6 |
| Cites de CEO que no anomenen la persona | 122 | 40 |
| Dubtes oberts a `PENDENTS.md` (regla 29, lots 9 i 10) | 111 + 13 + 139 | |
| URL citades sense cita verificada a Wayback | 5.411 | |
| Incoherències del CSV (secció 2.6) | ~83 + estat de certificació | |
| Sector no tancat | 187 | 127 ISIN |
| Doble codificació humana | tots els F + 10-20 % de P | |

Ordre de magnitud [C]: les 1.932 files F+P incompletes equivalen a uns 7 lots de 250-300 files si es fan de cop (CEO i classificació per fila). Una part es pot recuperar per script si es localitzen les sortides r3e/r4 (tasca T2.1), i això reduiria molt la feina de cerca.

## 7. Tasques concretes proposades

Columna «Perfil»: qui ho pot fer, no una assignació. **Agent** = Claude, Codex o un altre agent de cerca; **Script** = feina automàtica; **DF**, **Doctorat**, **Jordi** = rols actuals; **Persona** = codificador humà.

### Fase 0. Fonaments (bloquejant, curta)

| ID | Tasca | Abast | Perfil | Depèn de |
|---|---|---|---|---|
| T0.1 | Posar la metodologia v0.10.10 al repositori i preparar un codebook consolidat (regles amb identificadors únics) i un registre de casos decidits | 1 PR | Agent prepara; Doctorat revisa; Jordi aprova | — |
| T0.2 | Definir l'esquema final: columnes de la base final i camps obligatoris del registre (nivell A/B, data del document, extracte, SHA, `verificada_A`/`reculada_per_tinenca`, any de fundació, any de naixement, regla normalitzada) | 1 document | Agent proposa; Doctorat valida; Jordi aprova | — |
| T0.3 | Script d'estat per fila (`estat_files.csv` + resum) segons la secció 5, executat al CI a cada PR. Substitueix `PENDENTS.md` com a font d'estat | 1 script | Agent escriu; DF valida; Jordi aprova (toca `scripts/`) | T0.2 |
| T0.4 | Normalitzar per script el registre existent (`marca_prova`, `funcio_cita`, `estat_certificacio`) en columnes noves, sense esborrar res | 11.582 entrades | Agent o script; DF valida | T0.2 |
| T0.5 | Decisions de Jordi (secció 8) | — | Jordi | — |

### Fase 1. Correccions i grup F

| ID | Tasca | Abast | Perfil | Depèn de |
|---|---|---|---|---|
| T1.1 | Lot de coherència del CSV: Enagás 2016-2021, Bellway 2017, BME 2017-2018, `regles` de Cellnex, AB InBev i Harbour, 37 P sense prova de «no» (si no tenen prova, passen a ND segons la metodologia), `motiu_nd` residual | ~83 files | Agent documenta; DF aplica; Doctorat; Jordi | T0.5 |
| T1.2 | Revisió dirigida del patró president executiu + consejero delegado (ES, IT, PT i similars) | per determinar | Agent | — |
| T2.1 | Localitzar les sortides r3e/r4 i l'inventari de fonts antic (box/Drive) i extreure'n per script les cites de CEO i de classificació de les 1.773 certificades | 1.773 files | DF o Arquitecta (accés al box); Agent pot processar els fitxers | T0.5 |
| T2.2 | Verificar al document les cites recuperades i entrar-les al registre | el que surti de T2.1 | Agent, per lots | T2.1 |
| T3.1 | **Lot F**: cita de CEO per a les 302 files F i cita de classificació per a les 138 F que no en tenen; objectiu 349/349 | 2 lots | Agent | T0.2 |
| T4.1 | Wayback dels lots 6-10 i de tot el grup F (captura + verificació de la cita a la còpia `id_`) | ~5.400 URL | DF per script; Jordi decideix on s'executa | T0.5 |

### Fase 2. Completar les P i els pendents

| ID | Tasca | Abast | Perfil | Depèn de |
|---|---|---|---|---|
| T3.2 | Lots de CEO per a P (el que quedi després de T2) | fins a 1.582 files, ~6 lots | Agent | T2.2 |
| T3.3 | Lots de classificació per a P; a les 754 P només amb prova c, intentar pujar a b amb l'any de naixement | fins a 1.141 files, ~4-5 lots | Agent | T2.2 |
| T3.4 | NA: documentar la cerca R-SC exhaustiva | 29 files | Agent; Doctorat si hi ha dubte | — |
| T3.5 | Pendents de `PENDENTS.md` amb cerca sense límit (A.4): 111 de la regla 29, 139 del lot 10, 154 `fora_mostra` incompletes, Jyske, Sopra Steria 2025 | ~300 files | Agent; Doctorat per als dubtes de criteri | — |
| T3.6 | Criteris pendents del PR #3 (13 files del lot 9: Allreal, Sandoz, Bankia, Paysafe, EVRAZ) | 13 files | Doctorat proposa; Jordi decideix | — |
| T3.7 | Segona cita per a les 122 files amb una cita de CEO que no anomena la persona | 122 files | Agent | — |

### Fase 3. Verificació i validació

| ID | Tasca | Abast | Perfil | Depèn de |
|---|---|---|---|---|
| T4.2 | Verificació independent automàtica de cada lot (re-descàrrega i cerca literal per mostra, com en aquesta auditoria), amb un llindar d'acceptació (p. ex. ≥ 95 % dels documents oberts) | cada PR | Script; DF | T0.3 |
| T4.3 | Wayback de la resta de documents i verificació de les cites a la captura | la resta de les 5.805 URL | DF per script | T4.1 |
| T4.4 | Desar extractes amb SHA-256 (D23, D29) com a còpia pròpia (repositori o Zenodo, revisant drets) | totes les fonts | Script; Jordi decideix on | T0.2 |
| T5.1 | Decidir qui fa la doble codificació (D13) | — | Jordi amb la directora | — |
| T5.2 | Paquet cec de doble codificació: tots els F (349 files, 88 empreses) i una mostra estratificada del 10-20 % de P; càlcul de kappa per script | ~1.000 files | Persona codifica; Agent prepara el paquet i l'script | T5.1, T3.1 |
| T5.3 | Revisió de Jordi d'una mostra estratificada per regla i de tots els dubtosos (regla 12) | mostra | Jordi | T5.2 |

### Fase 4. Variables, robusteses i congelació

| ID | Tasca | Abast | Perfil | Depèn de |
|---|---|---|---|---|
| T6.1 | Columnes de marques i robusteses de les regles 25-29 (`marques_fundador`, `founderceo_rob_regla25_nd` i per criteri, `founderceo_rob_sense_interval`, `conflicte_fonts`, `dubte_D1` ampla, `si_font_B`) | tota la base | DF per script; Doctorat revisa; Jordi | T0.4 |
| T6.2 | Taula d'episodis de CEO (inici, fi, interí, co-CEO, motiu de sortida) a partir de les cites, que sovint ja porten dates | ~1.600 persones [NV] | Agent i script | T0.5 (abast) |
| T6.3 | Categoria H (hereu), FounderChair, Returning_founder; any de fundació, any de naixement, any d'IPO, nom dels fundadors, si són vius, si l'empresa porta el seu nom (variables instrumentals de l'A1) | per decidir | Agent | T0.5 (abast) |
| T7.1 | Sector: 127 ISIN amb font A i decisió sobre la llicència ICB | 187 files | Agent; Jordi | — |
| T7.2 | Actualitzar `LIMITACIONS.md`, `DICCIONARI_CAMPS.md` i `README.md`; separar base final i columnes de procés | — | Agent; DF | T0.2 |
| T7.3 | Congelació FounderCEO v1.0.0 i CEO_spells v1.0.0, SHA, DOI de Zenodo, repositori públic net i publicació del dashboard | — | DF; Jordi aprova | tot l'anterior |
| T7.4 | Esborrar la branca `df/lot8-llista` | — | Jordi | — |

## 8. Decisions que calen de Jordi

1. **Definició de «base acabada»** (secció 5). En particular: una fila «certificada» sense cita al repositori, compta com a feta? Recomanació [C]: no; la cita ha de ser al repositori.
2. **Sortides de l'auditoria r3e/r4 i inventari de fonts antic:** on són i qui les pot traspassar (T2.1). És la manera més ràpida de reduir el forat de les certificades.
3. **Wayback:** on s'executa la captura i la verificació (ordinador de casa, ordinador de DF o un procés automàtic de GitHub amb les claus com a secrets), i amb quin calendari.
4. **Abast de les variables addicionals** (T6.2 i T6.3): si s'inclouen ara a la base o en una fase posterior. La metodologia les demana per als tres articles.
5. **Doble codificació (D13):** qui la fa i quan.
6. **Lot de coherència T1.1:** autoritzar-lo (toca `dades/`).
7. **Criteris del PR #3** (13 files del lot 9) i **Sopra Steria 2025**.
8. **Llicència ICB** abans de mostrar el sector.
9. **Simplificació del flux:** lots de 250-300 files amb verificació automàtica per mostra, un estat per fila calculat per script i decisions registrades una sola vegada.

## 9. Correcció al document de traspàs

El traspàs pren com a referència `main` `fa8f90d`. Ara `main` és `17b03df`: el PR #20 (dashboard) es va fusionar el 23/11/2026 a les 14:00 Europe/Madrid. El CSV, l'xlsx, el sector, el registre i `PENDENTS.md` no han canviat (mateixos SHA); només han canviat `dashboard/` i `MANIFEST_SHA256.csv`. El dashboard no està publicat a GitHub Pages (segons `dashboard/README.md`).

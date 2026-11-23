# Pla per finalitzar la base de fundadors-CEO (proposta, 23/11/2026)

- **Autor:** Claude (agent), per encàrrec de Jordi. És una proposta de treball: no modifica cap dada ni la metodologia.
- **Punt de partida:** `docs/AUDITORIA_ESTAT_BASE_20261123.md` (`main` a `17b03df`).
- **Abast (definit per Jordi el 23/11/2026):** per a cada empresa i any, l'evidència de **qui era el CEO** el 31/10 i l'evidència de **si aquell CEO era el fundador** (amb el fundador identificat quan l'empresa en té i l'evidència el dona, o amb les proves a-e de la metodologia per descartar-ho). Tota l'evidència guardada i arxivada. La resta (hereus, episodis de CEO amb dates, variables instrumentals, etc.) queda fora. La validació humana la farà Jordi al final.

## 1. Què vol dir «fila acabada»

Una fila (ISIN-any) està acabada quan compleix les quatre condicions:

1. **CEO.** Almenys una cita A/B [V] que anomena la persona i el càrrec, d'un document de l'exercici que inclou el 31/10 (informe anual, document de registre, comunicat, regulador), o bé un interval de la regla 28 (dues entrades `ceo_interval`).
2. **Fundador.**
   - Si FounderCEO = 1: una cita A/B que anomena el CEO fundador o cofundador (D37 o cita directa), o les cites de la via FT o D10 que corresponguin.
   - Si FounderCEO = 0: una prova a-e amb cita A/B. Si la prova anomena els fundadors (prova a, P8), se'n desen els noms.
   - Si és NA: la cerca R-SC documentada. Si és ND: la cerca exhaustiva documentada (A.4).
3. **Arxiu.** Cada document citat té captura Wayback, i la cita s'ha verificat per script a la captura (`id_`). Si no es pot arxivar, consta com a limitació amb el motiu (`arxiu_durable=false`).
4. **Coherència.** El CSV oficial (`ceos`, `FounderCEO`, `regles`) diu el mateix que l'evidència, i la fila no té cap dubte obert.

Una fila «certificada» per l'auditoria IA r3e/r4 compta com a acabada **només** si la seva evidència és al repositori i compleix aquestes quatre condicions.

## 2. Situació de partida [V]

| | Files |
|---|---:|
| Files del panell | 6.012 |
| F+P amb cita de CEO i cita de classificació al repositori | 4.048 de 5.980 |
| F completes | 44 de 349 (9 de 88 empreses) |
| Sense cita de CEO | 1.884 (302 F, 1.582 P) |
| Sense cita de classificació | 1.279 F+P (138 F, 1.141 P), més 29 NA |
| Certificades sense cap cita al repositori | 1.247 (però 963 tenen enllaç Wayback a la base i 1.189 remeten a fonts de l'inventari antic, que no és al repositori) |
| Cites ja verificades a la captura Wayback | 744 entrades de 11.582 |

## 3. Normes per a tots els lots nous

Per evitar els problemes vistos a l'auditoria:

- Màxim 250-300 files per lot, agrupades **per empresa** (tots els anys d'una empresa al mateix lot), i CEO i fundador alhora.
- Cada PR porta el recompte de files acabades abans i després (script d'estat, tasca 0.2).
- Abans de fusionar, verificació independent automàtica per mostra (re-descàrrega i cerca literal). Llindar proposat: ≥ 95 % dels documents oberts.
- Cap canvi a `FounderCEO` ni a `ceos` dins un lot de proves. Si l'evidència contradiu la base, la fila va a la llista de dubtes i es corregeix en un lot de correcció a part, amb l'OK de Jordi.
- Els dubtes de criteri s'agrupen en un sol paquet periòdic per a Doctorat i Jordi, no un per lot.
- Es mantenen el flux i les prohibicions de `CLAUDE.md` (branques, PR, no tocar `main`).

## 4. Fases i tasques

### Fase 0. Preparació (abans de cap lot nou)

| ID | Tasca | Resultat | Qui aprova |
|---|---|---|---|
| 0.1 | Respostes de Grok a les preguntes de la secció 6 | Saber on és cada fitxer i qui fa què | — |
| 0.2 | Script d'estat per fila: comprova les quatre condicions de la secció 1 per a les 6.012 files i genera `estat_files.csv` i un resum. S'executa al CI a cada PR | Un sol comptador de progrés, que substitueix `PENDENTS.md` com a estat | Jordi (toca `scripts/` i `.github/`) |
| 0.3 | Camps mínims al registre: nivell de font (A/B), any o data del document, tipus de prova del CEO (informe de l'exercici, tinença o interval), noms dels fundadors quan la font els dona, i any de fundació i any de naixement quan la prova és b. Les entrades antigues es normalitzen per script en columnes noves, sense esborrar res | La prova es pot comprovar per script (per exemple, la resta de la prova b) | Doctorat revisa; Jordi aprova |
| 0.4 | Posar la metodologia v0.10.10 al repositori | La norma vigent, dins el repositori | Jordi (toca `docs/METODOLOGIA.md`) |

### Fase 1. Recuperar l'evidència que ja existeix fora del repositori

És la fase més rendible: moltes cites ja es van trobar i només cal portar-les al repositori i comprovar-les.

| ID | Tasca | Abast | Resultat |
|---|---|---|---|
| 1.1 | Script que porta al registre les cites de les sortides de l'auditoria r3e/r4 i de l'inventari de fonts antic (`ids_fonts`, paquets X2-X14), marcades [NV] fins que es comprovin | 1.773 certificades, i les altres que en tinguin | Entrades noves al registre amb URL i cita |
| 1.2 | Verificació d'aquestes cites al document i compleció del que falti (per lots) | El que surti de 1.1 | Entrades [V] |
| 1.3 | Lot de coherència del CSV: Enagás 2016-2021, Bellway 2017, BME 2017-2018, `regles` de Cellnex, AB InBev i Harbour, 37 P sense prova de «no», `motiu_nd` residual | ~83 files | Proposta documentada; DF aplica; Jordi aprova |

### Fase 2. Grup F complet (prioritat màxima)

| ID | Tasca | Abast | Resultat |
|---|---|---|---|
| 2.1 | Lot F-1 | ~44 empreses F | CEO de cada any i cita de fundador, amb el fundador identificat |
| 2.2 | Lot F-2 | ~44 empreses F | Ídem |
| 2.3 | Wayback de tots els documents del grup F, tot seguit | ~400-600 URL [NV] | Les 349 F acabades |

### Fase 3. Completar les P

| ID | Tasca | Abast | Resultat |
|---|---|---|---|
| 3.x | Lots de P per empresa, començant per les certificades que no s'hagin recuperat a la fase 1 | Avui 1.582 P sense CEO i 1.141 sense prova (moltes coincideixen); entre 4 i 7 lots segons el que doni la fase 1 | CEO i prova a-e per fila |

### Fase 4. Pendents i casos difícils (en paral·lel a les fases 2 i 3)

| ID | Tasca | Abast |
|---|---|---|
| 4.1 | Cerca sense límit (A.4) dels dubtes de `PENDENTS.md`: regla 29 (111), lot 10 (139) i la resta de files `fora_mostra` incompletes | ~300 files |
| 4.2 | NA: documentar la cerca R-SC | 29 files, 6 empreses |
| 4.3 | Casos de criteri: lot 9 (13 files, criteris del PR #3) i Sopra Steria 2025 | Paquet per a Doctorat i Jordi |

### Fase 5. Arxiu i verificació (contínua)

| ID | Tasca | Abast |
|---|---|---|
| 5.1 | Captura Wayback de cada document citat i verificació de la cita a la captura | ~5.800 URL actuals i les noves |
| 5.2 | Verificació independent per mostra de cada lot abans de fusionar | Cada PR |
| 5.3 | Còpia pròpia de l'extracte amb SHA-256 (D29), on decideixi Jordi | Totes les fonts |

### Fase 6. Tancament

| ID | Tasca |
|---|---|
| 6.1 | Script d'estat: 100 % de files acabades o amb limitació documentada (A.4) |
| 6.2 | CSV coherent; columnes d'estat d'evidència en lloc de la certificació IA; columnes de robustesa de les regles 25-28 calculades per script a partir de les marques |
| 6.3 | Base final neta (una fila per ISIN-any amb CEO, FounderCEO, regla, fundadors quan consti i identificadors d'evidència) i taula d'evidències (URL, Wayback, cita, nivell, data). Diccionari i limitacions al dia |
| 6.4 | Congelació v1.0.0 amb SHA → validació humana de Jordi → correccions → dipòsit a Zenodo |

## 5. Què pot fer Claude des d'aquest entorn

- **Sí:** cercar i llegir fonts originals (a la mostra de l'auditoria, el 83 % dels documents s'obren) i verificar-ne les cites; escriure els scripts (estat, importació, normalització, verificació per mostra); preparar els lots i els PR.
- **No:** Wayback (està bloquejat des de l'entorn al núvol); fusionar a `main`; accedir al box. Al Drive hi pot accedir amb el connector si Jordi l'autoritza i li diu la carpeta.

## 6. Preguntes per a Grok

Context per a Grok: Claude es fa càrrec de la base al repositori `jmasoribas-max/base-fundadors-ceo-stoxx600` (`main` `17b03df`). Cal saber on és cada cosa per acabar-la. Si us plau, per a cada resposta doneu la ruta exacta (box o Drive, amb l'identificador de carpeta) i el format del fitxer.

**A. Evidència de l'auditoria IA (r3e del 17/11 i r4 del 18/11)**

1. On són les sortides de l'auditoria r3e i de la completació r4 (carpetes del Drive `1jwCn3Eev6Ni5McBp1jEpQnEjpBQj8j61` i `1ic68PNoqKOXURIpE7-MzQES4Zaj0BP2o`, o al box)? Quin fitxer conté, per a cada fila, la URL i la cita literal que va fer servir cada model (ChatGPT i Claude) per al CEO i per a la classificació?
2. Com es lliguen aquestes sortides amb la base? La base té `sim_id_fila_r4` (p. ex. `R1298`): hi ha una taula que relacioni aquest identificador amb les cites?
3. A `sim_cert_detall` diu «cita A/B verificada». Qui ho va verificar i com (script contra el document?), i on és el registre d'aquesta verificació?

**B. Inventari de fonts antic**

4. On és l'inventari al qual remet `ids_fonts` (identificadors com `X6|WBF06094`) i els paquets X2-X14 (`pack_origen`, `font_classificacio_pack`)? Per a cada font, conté URL, cita literal i SHA?
5. On són els documents o extractes amb el SHA de `v75_sha256_documents` i `font_classificacio_sha_extracte`? Se'n va desar el text?
6. Les URL de `v75_urls_arxivades` (captures Wayback) són de documents de CEO, de fundador o de tots dos? Què vol dir `v75_cita_trobada` buit?

**C. Wayback**

7. El run de verificació Wayback que es va començar el 21/11 a l'ordinador de casa: ha acabat? On és el resultat i quines entrades del registre cobreix (lots 2-5 o també 6-10)?
8. On és l'script (`/workspace/dashboard-fundadors/wayback/`?), què fa exactament (captura amb les claus IA S3 i verificació amb `id_` i `pdftotext`?) i qui el pot executar? Es podria executar fora de l'ordinador de casa (ordinador de DF o un procés automàtic de GitHub amb les claus com a secrets)?
9. Les 2.509 entrades amb `cita_verificada_a_captura=no` i la nota «captura existent… connexió tallada pel proxy»: s'han tornat a intentar?
10. Les 6 cites de la secció «Cites amb Wayback pendent» de `PENDENTS.md` (Mandatum, emeis/Orpea): estan resoltes?

**D. Estat de la base i decisions**

11. Quina columna és el CEO oficial: `ceos` o `sim_ceo_aplicat`? A Enagás 2016-2021 i Bellway 2017 no coincideixen (Doctorat va decidir Oreja i Ayres). S'havia d'aplicar a `ceos`?
12. Cellnex 2016-2022 és F amb `regles=b`; AB InBev 2021-2025 és P amb `regles=cap`; Harbour 2022-2023 és P amb `regles=cita_fundador`. Hi ha un recàlcul de DF pendent? Quina és la regla correcta de cada cas?
13. Hi ha decisions de Jordi ja preses però encara no aplicades al CSV (p. ex. Inditex 2016-2018, canvis de CEO trobats als lots)? On és la llista?
14. Jordi va aprovar els criteris generals del PR #3 (19/11): un document de l'emissor penjat fora del seu domini compta com a A, cotitzacions dobles, premsa B contemporània, què és un mitjà B? D'això depenen 13 files del lot 9.
15. Els «300 dubtes residuals que mantenen la cobertura» del lot 7 i els 20 dubtes metodològics del lot 5: on són llistats i cal fer-hi res?

**E. Organització**

16. DF, Doctorat i l'Arquitecta continuen actius? Els PR de Claude han de passar per la validació de DF abans de l'OK de Jordi, o van directament a Jordi?
17. Codex continuarà fent lots en paral·lel? Si és així, qui els assigna, per evitar que dos agents treballin les mateixes files?
18. On s'han de desar les còpies de les evidències (extractes o PDF): al repositori, a Zenodo o al Drive? Hi ha cap limitació de drets acordada?
19. Continua vigent el pla de fer privat el repositori de treball i obrir-ne un de públic i net al final?

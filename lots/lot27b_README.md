# Lot 27b · Cerca amb agents de la cita de CEO de l'exercici (26/11/2026)

## Per què

És la segona part del lot 27 (`lot27_README.md`). Les 516 files de `lot27_pendents.csv` (176 empreses) només tenien una cita de CEO que, segons l'script de revisió de l'exercici, podia ser d'un altre any, i per script no s'hi havia trobat cap informe oficial de l'exercici. Jordi va demanar la cerca amb agents el 26/11/2026.

## Què s'ha fet

Set agents, d'unes 74 files cadascun, han aplicat a cada fila aquest ordre:

1. **Jutjar la cita actual.** És bona (`ok_actual`) si és:
   - un document de l'exercici que conté el 31/10;
   - un document de l'emissor de l'any *t* anterior al 31/10 sense cap canvi (Q15);
   - un document posterior que cobreix la data literalment («CEO since 2012»).
2. **Si no ho és, buscar una cita millor:**
   - l'informe de l'exercici (preferentment font A);
   - un document posterior amb el mandat explícit;
   - o bé un interval de la regla 28.
3. **Informar de qualsevol CEO diferent del de la base.**

Les cites noves s'han importat amb `traspas/importa_entrades.py` (lot 27, origen `cerca_ceo_exercici_agents`). L'script torna a baixar cada document i hi busca la cita literal. Les sis cites que ja eren al registre hereten la verificació de l'entrada `[V]` original.

## Resultats

| Resultat (per fila, `lot27b_resum.csv`) | Files |
|---|---:|
| `ok_actual`: la cita actual ja acredita el 31/10 | 303 |
| `nova_cita`: cita nova de l'exercici, o posterior amb el mandat explícit | 198 |
| `interval`: dos extrems documentats (regla 28) | 15 |
| `no_trobat` | 0 |
| **`ceo_diferent`** | **0** |
| **Total** | **516** |

- **Cap CEO equivocat.** En les 516 files, la persona de la base era el CEO el 31/10.
- **Entrades noves al registre:** 145, totes `[V]`.
  - 143 són de CEO: 130 R1, 2 R2 i 11 `ceo_interval`.
  - 2 són de context: Luxottica 2016-2017, vegeu més avall.
  - Afecten 83 empreses.
  - 1 entrada s'ha rebutjat: una línia de Sartorius sense el nom del CEO. La mateixa font en té una altra amb el nom, que sí que s'ha importat.
- **Fonts:** 141 entrades de nivell A i 2 de nivell B (premsa). Les dues de premsa són LafargeHolcim 2016 (swissinfo) i Clariant 2018 (Moneycab). El 2016 de LafargeHolcim queda només amb font B (D4b), perquè holcim.com respon 403 a curl.
- **Còpies descarregables:** a 7 files amb `ok_actual`, l'agent hi ha afegit la mateixa cita en una còpia que es pot baixar. Les notes comencen amb `url_alternativa:`.

## Intervals: les cites antigues que només són un extrem

A les 15 files `interval`, les cites antigues eren només el nomenament o la sortida, i comptaven com a «document». S'hi ha fet:

- **Notes:** s'ha afegit a les notes de cadascuna, sense esborrar res (secció 5), una nota amb l'etiqueta `[extrem_mandat anys=…]`. N'hi ha nou:
  - SGS: `L4|CH0002497458|1` i `|4`.
  - Carl Zeiss Meditec: `L5-DE0005313704-R13-C01` i `-C02`.
  - Siemens Energy: `L5-DE000ENER6Y0-C2`, `-R13-C01` i `-R13-C02`.
  - Worldpay: `L7-GB00BYYK2V80-C02`.
  - Elekta: `L7-SE0000163628-C01`.
- **Script:** `estat/estat_files.py` llegeix aquesta etiqueta. Per a aquells anys, l'entrada compta com a extrem d'un interval i no com a document.
- **Efecte:** les files amb `c1_tipus=interval` passen de 38 a 53, i la robustesa `founderceo_rob_sense_interval` les tracta com a ND.

## Punts per a Jordi

1. **KBC Ancora 2025.** La persona és correcta: Vandepitte, CEO de l'1/2/2024 al 16-17/6/2026. Però l'informe anual 2025/26 (p. 38) diu: «The company is not led by a CEO in the sense of a sole operational and responsible representative of the enterprise». Podria ser un cas de la Q12 (gestió externa) o de l'R2b (direcció col·legiada). No es canvia res fins que es decideixi.
2. **Michelin 2018-2025 (Q11, el Gérant d'una SCA és CEO).**
   - 2018: Menegaux ja era Managing General Partner al costat de Senard.
   - Des del 2019, Yves Chapot consta com a «General Manager» (Gérant non commandité).

   Si l'emissor els anomena Gérant, serien co-CEO. Hi ha una comprovació en curs, que també mira Hermès, Lagardère i Elior. L'etiqueta (0) no canviaria.
3. **Hexagon 2016.** El 31/10/2016, Rollén estava detingut i el CFO Belkic feia de CEO en funcions. Per la Q13, Rollén continua sent el CEO, i la robustesa R2 ha de fer servir Belkic.
4. **MAN 2017.** La cita és de l'informe anual 2017 de MAN SE, allotjat a ShipServ. Pel criteri a) del PR #3, compta qui ha escrit el document, no on està allotjat. Si no s'accepta, les notes descriuen un interval alternatiu: informe 2016, p. 133, i informe 2018, p. 152.
5. **Resultats anuals com a document de l'exercici.** Cinc files `ok_actual` es basen en el comunicat de resultats anuals de l'exercici i no en l'informe anual. Coherent amb la D21. Són Faurecia 2017 i 2020, BPER 2017, Experian 2021 i IDS 2024.

## Luxottica 2016-2017 (sense canvi)

Al document original en italià de govern corporatiu del 2016 (Relazione sul governo societario):
- l'únic amb el càrrec legal d'«Amministratore Delegato» és Vian;
- Del Vecchio hi és «Presidente Esecutivo», encarregat de l'àrea de Mercats;
- l'emissor distingeix el «Presidente Esecutivo» del «Chief Executive Officer (“CEO”)».

La traducció anglesa del 20-F diu «the other CEO», però per la Q8b la traducció només serveix de suport. Per tant, el CEO és Vian (R1) i la base no canvia. Les dues cites són al registre com a context.

## Accés

Moltes cites `ok_actual` són a webs que no responen a curl pla: sec.gov, sgs.com, holcim.com, gea.com, aegon.com, zeiss.com, unilever.com, infineon.com i d'altres. Les comprovarà el flux de Wayback, com sempre.

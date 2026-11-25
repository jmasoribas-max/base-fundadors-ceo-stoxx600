# Lot de correcció 3: Dassault Systèmes, Covivio i Wirecard (25/11/2026)

- **Proposta:** Claude, 25/11/2026. **Estat:** aplicat en aquesta branca. Jordi l'aprova en fusionar el PR.
- **Aprovació:** decisions de Jordi del 25/11/2026 sobre els dubtes del lot 22. La columna `aprovacio` de cada fila del fitxer de canvis porta la cita literal.
  - Dassault: «Per mi aquest és molt clar que ha de ser 1. L'empresa és la mateixa, no ha cambiat, l'única cosa que ha cambiat ha sigut l'ISIN».
  - Covivio i Wirecard: «confirmo covivo i wirecard».

  Dassault 2016-2020 també segueix la correcció C3 aprovada el 24/11/2026 (vespre).
- **Canvis:** [`correccio3_canvis.csv`](correccio3_canvis.csv), **178 cel·les a 22 files** (`CO3-001` a `CO3-178`). **8 files canvien de `FounderCEO`.**
- **Evidència:** 38 entrades del lot 24 al registre (`L24-…`, totes `[V]`, origen `dubtes_lot22`).
- **Com s'ha aplicat:** `python3 estat/aplica_canvis.py lots/correccio3_canvis.csv --aplica --origen correccio3_claude`. Abans, la prova en sec no va trobar cap discrepància entre `valor_actual` i el CSV o l'xlsx de la base. L'script ha escrit el CSV, l'xlsx, 43 entrades `correccio_coherencia` al registre i les fitxes. Després s'han regenerat l'estat, el dashboard i el manifest.

## Què canvia

| Bloc | Cel·les | Files | Què |
|---|---:|---:|---|
| Dassault Systèmes `FR0000130650` 2016-2020 (C3) | 100 | 5 | FounderCEO 0 → 1 per D37 (P6, «Co-Founder»). Els mateixos camps que la C3 preparada al lot de correcció 2 (`correccio2_c3_dassault_pendent.csv`, que aquest lot substitueix): `regles` → D37; marca D37; D37a (`d37_data_cita` 2026-02-21, no contemporània); D37b (`fundador_transformador`=1: fundació el 1981, entrada el 1983); `pre_d37` i les columnes sense transformador → ND; les robusteses que copien FounderCEO → 1 |
| Dassault Systèmes `FR0014003TT8` 2021-2023 | 60 | 3 | El mateix, perquè és la mateixa empresa amb un ISIN nou (decisió de Jordi del 25/11/2026) |
| Covivio `FR0000064578` 2016-2025 | 10 | 10 | Marca `data_fundacio_conflicte` (P7). Es manté el 0: fundació el 2/12/1963 (estatuts, L24-F04), naixement el 1965 (L24-F01) i entrada el 2001 des de Gecina (L24-F02, L24-F03). La biografia que diu «depuis sa création en 2001» (L24-X01) no correspon a cap fundació: l'historial de l'emissor només hi registra adquisicions |
| Wirecard `DE0007472060` 2016-2019 | 8 | 4 | `regles` d → a. Els fundadors són Paul Bauer-Schlichtegroll (EBS, predecessora) i Detlev Hoppenrath (Wire Card AG), segons el Bundestag i «Die Wirecard-Story» (L24-F01, -F02, -F05). Marques `conflicte_fonts` (l'RTÉ, font B, diu «founded by Markus Braun») i `llista_exhaustiva=implicita` (P8) |

## Dassault: la cita amb el nom complet

Al lot de correcció 2, la C3 va quedar pendent perquè la cita registrada només deia «Bernard» i el web de l'emissor retornava 403. Ara hi ha tres cites de l'emissor amb el nom complet. Totes es poden baixar amb curl pla.

- **L24-…-F03:** comunicat del 21/02/2026, p. 2: «Bernard Charlès commented : “… As Co-Founder of our company, alongside Charles Edelstenne, I am truly pleased that Pascal Daloz succeeds me in this role.»
- **L24-…-F02:** el mateix comunicat en francès: «J'ai co-fondé notre entreprise avec Charles Edelstenne…».
- **L24-…-F01:** Document d'enregistrement universel 2025, dipositat a l'AMF el 31/3/2026, p. 7: «Bernard Charlès, cofondateur de Dassault Systèmes, …».

No s'ha trobat cap cita contemporània (D37a). Els documents de registre del 2016 al 2024 diuen «He joined Dassault Systèmes in 1983». Per la D37 (regla 24), la cita de l'emissor preval igualment. La D37c rebutjada vol dir que no hi ha excepció per dades contràries. El risc el cobreixen les robusteses `founderceo_rob_cita_contemporania` i sense `fundador_transformador`.

## Covivio i Wirecard: fundador transformador (Q7)

Jordi va demanar que es comprovés si Kullmann o Braun podien ser fundadors transformadors. Cap dels dos compleix el criteri 1 de la Q7, que és prendre el control de l'empresa com a primer accionista individual:

- **Kullmann** tenia 50.399 accions a 31/12/2016, prop del 0,07 % (L24-X03). L'empresa la controlava Batipart (1999-2010) i després el primer accionista va ser Delfin, amb el 27,77 % (L24-X04, L24-X06).
- **Braun** tenia entre el 7 i el 8 % de les accions, i ningú no superava el 10 % (L24-X03, X07 a X09). Cap font A/B no li atribueix la transformació del negoci (L24-X04, X05).

## BillerudKorsnäs 2017: sense canvi

El dubte del lot 22 era si la base s'equivocava de CEO el 2017. No s'equivoca: el CEO a 31/10/2017 és Per Lindberg. Les cites són al registre:

- **L24-SE0000862997-C01 i C02:** l'informe del tercer trimestre (16-17/10/2017) el signa Lindberg com a CEO. El comunicat del 30/10/2017 diu que Petra Einarsson «will assume her new position at the turn of the year 2017-2018» i que Lindberg deixa el càrrec quan ella el pren.
- **L24-SE0000862997-X01 i X02:** l'informe anual 2017, publicat l'abril del 2018, diu «at the beginning of the year», però es refereix al 2018. D'aquí venia la confusió.

## Efecte

- **Panell:** 352 F i 5.621 P (abans 344 F i 5.629 P). La mostra principal no canvia de mida.
- **Files P amb prova completa per parts:** 5.563 de 5.621 (99,0 %).
- **Dubtes del lot 7 de Dassault 2016-2020:** es donen per tancats a `estat/dubtes_tancats.csv`.

**Robusteses que falten.** Les robusteses de les marques noves es calcularan al lot de robusteses: `data_fundacio_conflicte` com a ND, i `conflicte_fonts` amb el valor alternatiu (1). Avui les columnes de la regla 25 encara no existeixen.

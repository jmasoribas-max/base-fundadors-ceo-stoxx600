# Lot de correcció 6: les quatre decisions del lot 28 (26/11/2026)

- **Proposta:** Claude, 26/11/2026. **Estat:** aplicat en aquesta branca. Jordi l'aprova en fusionar el PR.
- **Aprovació:** Jordi, 26/11/2026, després de l'explicació de cada cas a la sessió de Claude: «estic d'acord amb totes les teves recomanacions». La columna `aprovacio` de cada fila del fitxer de canvis porta aquesta cita.
- **Canvis:** [`correccio6_canvis.csv`](correccio6_canvis.csv), **79 cel·les a 8 files** (`CO6-001` a `CO6-079`). **3 files canvien de `FounderCEO`.**
- **Evidència:** les entrades del lot 28 al registre (`L28-…`), ja a `main` (PR #56). Aquest lot no afegeix cap cita nova.
- **Com s'ha aplicat:**
  - Ordre: `python3 estat/aplica_canvis.py lots/correccio6_canvis.csv --aplica --origen correccio6_claude`.
  - Comprovació prèvia: la prova en sec no va trobar cap discrepància entre `valor_actual` i el CSV o l'xlsx de la base.
  - Resultat: l'script ha escrit el CSV, l'xlsx, 56 entrades `correccio_coherencia` al registre i 4 fitxes.
  - Després s'han regenerat l'estat, les robusteses, el dashboard i el manifest.

## Què canvia

| Decisió | Files | Cel·les | Canvi |
|---|---|---:|---|
| 1. EssilorLuxottica `FR0000121667` | 2018-2020 | 3 | Marca `dubte_D1`. FounderCEO es manté a 1 (Del Vecchio) |
| 2. ACS `ES0167050915` | 2016, 2021 | 44 | FounderCEO 0 → 1 per FT de tipus c (Q7): `regles` d → cap;FT, `ft`=1, `tipus_ft`=c, `founderceo_rob_sense_ft`=0. Les robusteses que copien FounderCEO passen a 1 |
| 3. Rubis `FR0013269123` | 2024-2025 | 6 | Jacques Riou surt de `ceos` i de `sim_ceo_aplicat` (Q11). `n_ceos` passa de 3 a 2 (2024) i de 5 a 4 (2025). FounderCEO es manté a 1 (Gilles Gobin) |
| 4. Tritax Big Box `GB00BG49KP99` | 2021 | 26 | R-SC per la Q12, com el 2018-2020: `ceos` buit, FounderCEO 1 → NA_sense_ceo, `regles` R-SC, marques `R_SC_confirmat;gestio_externa`, `motiu_na`, `a_mostra_principal`=0. Les robusteses prenen els valors del 2020 |

### 1. EssilorLuxottica 2018-2020

Font: document de référence 2018 (AMF), entrades L28-FR0000121667-X01 a -X05 i -F01. L'emissor descriu l'operació del 2018 com a «rapprochement», i cap part no passa del 60 %: Delfin té el 38,93 % després de l'aportació i el 32,05 % després de l'OPE, amb els vots limitats al 31 %.

Però hi ha dues lectures de qui adquireix:
- jurídicament, l'adquirent és Essilor;
- sota l'IFRS 3, l'adquirent comptable és Luxottica (el document en diu «acquisition inversée»).

La descripció i l'estructura no lliguen amb la comptabilitat, i per això s'hi aplica `dubte_D1` (regla 26). Per la J1, la part on era Del Vecchio és Luxottica, que ell va fundar: el document en dona una cita contemporània, a la p. 140. La Q1 no s'hi aplica, perquè Luxottica no és la part absorbida en substància.

### 2. ACS 2016 i 2021 (Florentino Pérez)

**D37:** cap document de l'emissor no l'anomena fundador. S'han revisat l'IAGC 2016 i 2021, l'informe anual 2021, el fullet de la CNMV del 1999 i el currículum del web d'ACS.

**Q7, criteri per criteri:**
1. **Control.** Va comprar Construcciones Padrós el 1983 (elDiario.es, B), i l'emissor el fa «uno de sus principales accionistas» (A). A ACS és el primer accionista: 12,52 % el 2016 i 12,93 % el 2021 (IAGC).
2. **Primer executiu.** És «máximo ejecutivo» de Padrós des del 1984 i president executiu d'ACS des del 1997 (A).
3. **Transformació documentada.** L'emissor diu de Padrós: «tras su adquisición se reconvierte y relanza. Es germen del Grupo ACS hoy» (A). L'elDiario.es diu que OCP «se transformó en ACS» (B).

**Llacuna anotada:** cap font no diu literalment que fos el *primer* accionista individual de Padrós quan en va prendre el control. La Q7 cita ACS expressament entre els casos FT.

**Altres columnes:**
- `ft_rob_3anys` no s'ha tocat. És una columna heretada de la v75r2 i el diccionari no en defineix la regla.
- `founderceo_rob_ft_nomes_ab` passa a 1, perquè l'FT té fonts A i B.

### 3. Rubis 2024-2025

Fonts: documents d'enregistrement universel 2024 i 2025, entrades L28-FR0013269123-C04 a -C07 i -X02 a -X05.

- Clarisse Gobin-Swiecznik hi és «Gérante». El 2025 també ho són Bergeron i Jacquot.
- Jacques Riou només signa sota «La Gérance» i consta com a «Président d’Agena, société co-Gérante». Cap frase no l'anomena «Gérant».

Per la Q11, el representant d'una societat Gérante només compta com a CEO si l'emissor l'anomena Gérant. Del 2021 al 2023 l'emissor sí que el diu «Gérant» (L28-…-C01 a -C03), i aquells anys no canvien.

### 4. Tritax Big Box 2021

Font: informe anual 2021, entrades L28-GB00BG49KP99-X01 a -X05.

- Godfrey hi és «CEO – Fund Management», un càrrec de la gestora.
- L'informe diu que el Consell no té consellers executius i que la societat no té empleats.

La designació «CEO for Tritax Big Box REIT plc» només hi és des de l'informe 2022. Per la Q12, el 2021 és R-SC, com el 2018-2020. El 2022-2025 no canvia.

## Efecte

- **Panell:** 351 F, 5.621 P, 32 NA i 8 ND. Abans hi havia 350 F, 5.623 P i 31 NA.
- **Mostra principal:** 350 F i 5.610 P.
- **Nota sobre Luxottica 2016-2017 (lot 27b, sense canvi):** el document de govern corporatiu original del 2016, en italià, dona el càrrec legal d'«Amministratore Delegato» només a Vian, i Del Vecchio hi és «Presidente Esecutivo». Per la Q8b, el CEO és Vian (R1). El «the other CEO» de la traducció anglesa només serveix de suport. La base no canvia, i les cites entren al registre amb el lot 27b.

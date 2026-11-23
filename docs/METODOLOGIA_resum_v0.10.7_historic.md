# Metodologia (resum)

Aquest document és un **resum** de les regles i dels criteris de certificació a partir dels fitxers ja existents. No n'afegeix cap de nova. El que no està documentat a les fonts citades es marca **[NV]**.

Fonts d'aquest resum:

- Regles de classificació FounderCEO v0.10.7 (document de regles de l'auditoria IA). [V]
- Criteri de certificació de Doctorat, recollit a l'informe intern de comparació r4 (18/11/2026). [V]
- Tipologia d'errors E1-E8 de l'auditoria. [V]

La metodologia completa de les regles no es reprodueix aquí literalment; se'n resumeix el que cal per treballar al repositori. En cas de dubte, preval el text de les fonts i, si el dubte persisteix, el cas queda indeterminat.

## 1. Qui és el CEO de l'any t (R1-R3 i R-SC)

Data de referència: el CEO de l'any t és qui ocupava el càrrec el **31/10/t**. La font preferent és l'informe anual de l'exercici que inclou el 31/10/t. Si aquest informe no documenta cap canvi entre el 31/10/t i el tancament, el CEO del tancament serveix com a aproximació; si hi ha un canvi, val qui ocupava el càrrec el 31/10/t. [V]

Qui compta com a CEO:

- **R1.** Compta des del dia en què comença a exercir. Identifiquen el CEO el títol de CEO o el càrrec legal equivalent: president del consell de direcció en models de dos consells (per exemple, Vorstandsvorsitzender o Prezes Zarządu), Président-Directeur Général o Directeur Général, Administrateur Délégué, i equivalents. [V]
- **R2.** Un CEO interí compta com a CEO. [V]
- **R3.** Si el càrrec és vacant, compta qui la font descriu literalment com a primer executiu de facto. Un president executiu només compta per aquesta via. [V]
- El portaveu únic d'un consell de direcció col·legiat compta com a CEO. [V]

**R-SC.** Si, un cop aplicats R1, R2 i R3, el 31/10/t no hi ha cap CEO individual, la classificació és `sense_ceo`. [V]

**Co-CEO.** Si hi ha co-CEO i almenys un és fundador, la classificació és `1`. [V]

Les dates d'inici i de fi del mandat han de sortir d'un document. No s'estima cap data. [V]

## 2. És fundador? (resum)

L'objecte és la parella CEO-empresa. Es prova si el CEO és fundador o cofundador de l'empresa cotitzada o d'una entitat rellevant (fusió entre iguals, escissió o refundació, predecessora documentada). [V]

Ordre de les proves de «sí»:

- **D37.** Cita de l'emissor (informe anual, fullet, comunicat, web oficial, document regulador) que anomena la persona founder, co-founder, fundador o equivalent, referit a la cotitzada, al grup o a la predecessora documentada. Aquesta cita preval sobre les proves de «no», sobre la regla FT i sobre altres fonts que diguin «joined». No compten com a D37 les cites de fundador d'una altra entitat, les expressions ambigües com «founder-led» ni les fonts que no són de l'empresa. [V]
- **Cita directa.** Si no hi ha D37: cita literal en font A o B on el CEO consta com a fundador o cofundador de la cotitzada o d'una entitat rellevant. Compten tots els membres de l'equip fundador. Un fundador que torna com a CEO és `1` durant el nou mandat. [V]
- **Fundador transformador (FT).** Si no hi ha D37 ni cita directa, calen les quatre condicions, cadascuna amb cita literal: control propi i no heretat (primer accionista amb almenys el 20% dels vots, o majoria); és CEO (o president executiu i CEO) dins dels 5 anys posteriors a la presa de control i continua l'any t; transformació (canvi del negoci principal, fusió inversa amb la seva empresa com a adquirent comptable, o vendes almenys 10 vegades més grans per adquisicions, amb les dues xifres citades); i una font fiable el presenta com a fundador, creador o arquitecte del grup actual, sense contradicció d'una altra font fiable. [V]

Proves de «no» (`0`): exigeixen almenys una prova positiva amb cita. L'ordre de força, de més a menys, és **b, a, e, d, c**. [V]

- **a)** Llista tancada de fundadors on el CEO no hi és (la font ha de presentar la llista com a completa). [V]
- **b)** Edat: l'any de fundació rellevant més recent menys l'any de naixement més antic possible del CEO és inferior a 18 (amb un any de marge si l'any de naixement es dedueix d'una edat declarada). [V]
- **c)** 64 anys o més entre la fundació rellevant més recent i l'inici del mandat, només si no hi ha dada d'edat. És un criteri, no una prova d'edat. [V]
- **d)** Incorporació tardana: el CEO entra 3 anys o més després de la fundació rellevant més recent i hi ha cita de l'ocupador anterior. Un LBO, un MBO, la sortida a borsa o un canvi de denominació no són una fundació nova. [V]
- **e)** Origen no personal: una cita indica que l'entitat (i les rellevants) la va crear l'Estat o una altra empresa, sense cap persona fundadora. [V]

No són fundadors (tret que hi hagi D37): qui arriba per MBO o LBO i els socis de fons; els executius que s'han convertit en primers accionistes per la retribució; els hereus i familiars del fundador. Si el fundador és president i el CEO és una altra persona, la classificació és `0`. [V]

**Indeterminat.** Si hi ha un CEO identificat però cap prova de sí ni de no, la classificació és `indeterminat`. No es força un `0`. Si hi ha alhora una prova de sí i una de no, i D37 no resol el conflicte, també és `indeterminat`. Si dues fonts A o B es contradiuen sobre la fundació, també. [V]

Ser fundador depèn de la fundació, no de la IPO. [V]

## 3. Nivells de font

- **A:** documents de la mateixa empresa o registres oficials (informe anual, fullet o document d'IPO, pàgina oficial d'història, comunicat, document a un regulador o a la borsa). [V]
- **B:** tercers fiables (premsa econòmica de qualitat, obres de referència d'història empresarial, llibres, articles acadèmics). [V]
- **C:** agregadors, blogs, premsa local sense font, enciclopèdies obertes. Una font C **mai no verifica**, ni sola ni amb altres fonts C. Només serveix de pista. [V]

Una font només és evidència si el document s'obre i la cita literal hi és. [V] La URL de referència és la captura arxivada (Wayback); si no n'hi ha, val la URL oficial i el document es considera no durable. [V]

## 4. Criteris de certificació N1 / N2 (Doctorat)

Text del criteri de certificació (Doctorat), recollit a l'informe intern de comparació r4 (18/11/2026) [V]:

> N1, els dos models coincideixen amb la base, amb cita A/B (paquet ja verificada literalment, o web, aquesta darrera pot ser [NV] si encara no s'ha comprovat per script) i sense E2, E4 ni E6; N2, un model coincideix amb la base i l'altre ho deixa indeterminat, sense incidència greu; «certificada, CEO pendent», l'etiqueta és certificable però el CEO queda [NV] als dos models; la resta no es certifica. Un ND que només tanca un model no canvia l'etiqueta ni es certifica.

A la base, els estats són: `certificada` (amb nivell `N1`, `N2` o `doctorat`), `certificada_ceo_pendent`, `no_certificada` i `fora_mostra_auditoria`. [V]

Definicions de la tipologia d'errors, en la part que el criteri cita [V]:

- **E2** (crítica): el CEO del 31/10/t és una altra persona.
- **E4** (major): la font no diu el que se n'afirma.
- **E6** (menor, a la tipologia): dates de mandat, naixement o fundació errònies, sense efecte en l'estat.

**Decisió de Doctorat (19/11/2026):** E2, E4 i E6 impedeixen certificar a N1 i a N2. [V] Aquesta decisió tanca el matís entre l'adjectiu «greu» del criteri i la classificació d'E6 com a menor a la tipologia: als efectes de la certificació N1/N2, E2, E4 i E6 impedeixen certificar.

A la base v8 r3, les files amb incidència E4 a `sim_cert_detall` són **15 files / 7 ISIN** [V]: Covestro (`DE0006062144`), TAG Immobilien (`DE0008303504`), A.P. Møller-Mærsk (`DK0010244508`), Mandatum (`FI4000552526`), SFR Group (`FR0011594233`), Meggitt (`GB0005758098`) i Heineken Holding (`NL0000008977`). La llista detallada és a `PENDENTS.md`.

El detall operatiu de cada etiqueta `sim_cert_detall` (redacció exacta per fila) es llegeix a la base; no es reinterpreta aquí. [V] com a camp; no se'n fa una casuística nova.

## 5. Sector ICB a la v8 r3

El sector s'afegeix **per ISIN**, a partir de la taula `dades/sector_icb_v8r3.csv` (SHA `ddc3d037d796c4053700ce374148f134b09e071579875befe89e664e816899af` [V], idèntica a la font v75r2), construïda amb els PDF públics de components 2015-juny 2023.

**Decisió de Jordi (19/11/2026 10:06):** s'estén el supersector del PDF de juny 2023 als anys 2024-2025, **només** per als ISIN que ja tenen aquesta font (`any_font=2023`). Les files esteses porten `sector_estes_des_2023=1` i `any_font=2023`. Per a una robustesa que les exclogui, es filtra `sector_estes_des_2023!=1`. El sector fix per empresa és la columna `supersector_fix` (el mateix valor a totes les files de l'ISIN que tenen sector a la taula font). [V]

Supòsit, **[NV]**: no hi ha hagut cap reclassificació ICB entre el 2023 i el 2025 (declarat a `docs/LIMITACIONS.md`).

No s'estén el sector quan l'ISIN no té font de juny 2023 (33 ISIN, 52 files 2024-2025: queden `pendent_extensio_2024_2025` o `revisar_pendent_extensio_2024_2025`). Les 72 empreses sense sector (48 només presents el 2024-2025 i 24 no casades) queden pendents per a Claude, amb una font A (per exemple un informe anual amb la classificació ICB). Les 25 empreses casades per la via `nom_stoxx_via_llista_seleccio` queden marcades `revisar`. [V]

## 6. El que no s'ha documentat aquí [NV]

- Qualsevol regla, excepció o criteri que no figuri a les fonts citades més amunt. [NV]
- La llista nominativa de les 13 parelles sense documents (el recompte 10 P + 3 NA figura a l'informe de recuperació de 440 documents, 17/11/2026). [NV] per als noms; [V] per al recompte. Si la llista no apareix als fitxers, es regenerarà per script.
- El supòsit de no reclassificació ICB entre 2023 i 2025. [NV] (vegeu `docs/LIMITACIONS.md`).

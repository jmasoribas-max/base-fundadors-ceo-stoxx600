# Anàlisi de les preguntes obertes del paquet de criteris v2 (24/11/2026)

> **Decidit per Jordi el 24/11/2026: d'acord amb totes les recomanacions**, amb la regla única de la designació de l'emissor per al president executiu i el consejero delegado (C1 no s'aplica) i amb el criteri FT escrit tal com es proposa. Text normatiu: secció «Decisions de Jordi del 24/11/2026 (vespre)» de `CLAUDE.md` i `AGENTS.md`.

Preparat per Claude a petició de Jordi. L'objectiu és decidir cada criteri amb tres bases: el que ja diu la metodologia de la base (v0.10.10 i CLAUDE.md), el que fa la literatura empírica sobre founder-CEO, i l'impacte sobre la mostra i l'evidència.

- **Literatura:** dues revisions independents. El text complet i les cites literals són a [`docs/literatura/fundador_20261124.md`](literatura/fundador_20261124.md) (qui és el fundador) i [`docs/literatura/ceo_20261124.md`](literatura/ceo_20261124.md) (qui és el CEO).
- **Limitació:** de 8 dels 12 papers clàssics no s'ha pogut llegir el text complet, perquè estan darrere de murs de pagament: Anderson i Reeb, Miller et al., Palia-Ravid-Wang, Jayaraman et al., Nelson, Wasserman, He, i Gao i Jain. Les cites literals són d'Adams, Almeida i Ferreira (2009), Fahlenbrach (2009), Villalonga i Amit (2006), Sraer i Thesmar (2007), Barontini i Caprio (2006), Andres (2008, WP), Kramarz i Thesmar, Fernandes et al. (2013), Crespí i Pascual (2009) i Stein i Gallego (2012). **Abans de citar-les a la tesi, cal comprovar les pàgines a la versió publicada.**
- **Mostra principal actual:** 5.967 files, de les quals 348 F (5,832 %).

## Resum

| Q | Ja cobert per la metodologia? | Literatura | Recomanació | Efecte a la mostra principal |
|---|---|---|---|---|
| Q1 Fundador de l'empresa absorbida | **Sí**, regla 26 («una adquisició … no fa fundadors els seus fundadors») | AAF, Andres i SDC/Wulf: no compta. Villalonga i Amit: sí, però per a l'estatus familiar | **No compta (0)**, robustesa D1 àmplia = 1 | Standard Life Aberdeen: −2 F. EssilorLuxottica i ICAP/NEX (−6 F): només si la cerca confirma que van ser adquisicions |
| Q4 «Prior to setting up Energean» | **Sí**, P6 («set up» amb la persona com a subjecte) | S'accepta la inferència per la biografia (Fahlenbrach) | **Compta (1)** | Cap |
| Q5 i Q5b Cita publicada pel grup successor | **En part**: criteri a del PR #3 i D37a | Cap paper no exigeix cita contemporània; les fonts retrospectives s'accepten | **Compta (1)**, `allotjament=successor`, robustesa D37a = 0 | Cap (Paysafe i Merlin es mantenen a 1) |
| Q6 «Cofundador» només en premsa (B) | **Sí**, P6 (`si_font_B`, robustesa ND) | AAF i Fahlenbrach accepten una font de premsa; Villalonga i Amit en demanen dues | **Compta (1)** amb `si_font_B`, robustesa ND i robustesa de dues fonts | Cap (Evraz es manté a 1) |
| Q7 Refundador (ACS, Florentino Pérez) | **En part**: regla 6 i P5 (FT), però el criteri FT no és escrit al repositori | Tradició europea (Sraer-Thesmar, Barontini-Caprio, Andres): el *raider* compta. Tradició nord-americana (Fahlenbrach, VA): no, llevat de pocs casos | **Escriure el criteri FT** i aplicar-lo igual a LVMH, CTS Eventim, ACS…; per a ACS, primer buscar si l'emissor l'anomena fundador | ACS 2016 i 2021: +2 F si compleix el criteri FT |
| Q8b EssilorLuxottica 2020 (PDG i DGD) | **Sí**, R1 (PDG) | Kramarz i Thesmar: el CEO és el PDG o el DG; el DGD no | **Només Del Vecchio** | Cap |
| Q9 i Q9b President executiu i consejero delegado; traducció | **No del tot**: R3 diu que el president executiu només compta si el càrrec és vacant, però R1 admet el títol de CEO | ExecuComp i SEC: la persona que l'emissor designa com a CEO. A Espanya no hi ha consens (Crespí i Pascual: autodeclaració de l'IAGC; Stein i Gallego: poders). Cap paper no prioritza la traducció | **Regla única (vegeu més avall):** mana la designació del primer executiu al document regulat **original**; robustesa amb l'altra persona | Cap a FounderCEO; només canvia `ceos` (a cap fila, si s'aplica la regla) |
| C1 BME 2017-2018 | (és un cas de Q9) | — | **No s'aplica la correcció**: l'IAGC original diu que Zoido era el «primer ejecutivo» fins a l'abril del 2019 (X04). Robustesa amb Hernani | Cap |
| Q10 Luxottica | **Sí**, R1 (hi ha CEO amb títol) | Una cobertura informal no fa co-CEO | **Només Vian (0)**; Del Vecchio, a la robustesa R3 | Cap |
| Q12 Gestió externa (Tritax, Primary Health) | **En part**: R1, R3 i R-SC | El més habitual és excloure les financeres i immobiliàries; als REIT amb gestor extern no es codifica cap CEO persona | **Mana el document de l'emissor de cada any** (R1, R3 o R-SC), amb marca `gestio_externa` i **robustesa que exclou aquestes empreses** | Cap a l'anàlisi principal; a la robustesa en surten unes 6 files F |
| Q12b BB Biotech | **Sí**, ordre de fonts (§4: primer l'emissor) | L'emissor és la referència | **NA (R-SC)** | Cap (fora de la mostra) |
| Q13 CEO impedit o de baixa | **En part**: R2 (interí) | El titular continua sent el CEO mentre el càrrec no quedi vacant | **El titular (R1)**; robustesa amb l'interí si es nomena formalment | Cap |
| Q14 «Joint CEO» funcional (CD Projekt) | **En part**: R1 | Els co-CEO s'identifiquen pel títol; per al títol funcional no hi ha precedent | **Co-CEO (R1)**, perquè és designació de l'emissor de l'exercici, amb marca i **robustesa sense ell** | Cap a l'anàlisi principal; a la robustesa, 4 files d'1 a 0 |
| Q15 Document de l'any anterior al 31/10 | **Sí**, D21 (`proxy_tancament`) | La literatura data el CEO per exercici; el 31/10 és més exigent | **S'accepta** si no consta cap canvi | Cap |
| C2 Sopra Steria 2025 | prova a i regla 27 | — | **Aprovar: ND → 0** | +1 fila P a la mostra |
| C3 Dassault Systèmes 2016-2020 | D37 i P4 (escissió: 1 si l'emissor l'anomena fundador) | AAF compten el «main executive at the time the company began» | **Aprovar: 0 → 1**, robustesa D37a = 0 i `fundador_escissio` | +5 F |
| C4 Bridgepoint 2021-2022 | Regla 5 (MBO = 0, llevat de D37) | Fahlenbrach i VA: MBO no; AAF: sí, si transforma l'empresa | **Aprovar: 0 → 1** per D37, robustesa sense origen intern = ND | +2 F |

**Efecte conjunt** (amb les decisions ja preses de Q2, Q3, Q8 i Q11): la mostra principal passa de 5.967 a 5.961 files i els F, de 348 a 346 (**5,832 % → 5,804 %**). Si ACS compleix el criteri FT, en surten 348 (5,838 %). Si EssilorLuxottica i ICAP/NEX resulten adquisicions, 6 F menys.

## Q1. Fundador de l'empresa absorbida en una «fusió» que és una adquisició

**Metodologia.** La regla 26 ja ho diu: «Una adquisició, o la compra d'una start-up, no fa fundadors els seus fundadors.» El dubte venia de la lectura de la J1 («la part on era la persona»), que serveix per triar la data de les proves de no fundador, no per donar la condició de fundador.

**Literatura.**
- Adams, Almeida i Ferreira (2009, p. 138-139) compten els fundadors de totes dues parts **només** en una *merger of equals*.
- Andres (2008, p. 7): si una empresa familiar és absorbida, la família no fa familiar l'absorbent.
- La definició de SDC (Wulf 2004) demana aproximadament un 50/50. A Standard Life Aberdeen va ser un 66,7/33,3.
- Villalonga i Amit (2006, p. 391) admeten el fundador d'una predecessora en adquisicions (Turner a Time Warner), però per a l'estatus familiar.

**Recomanació:** 0, amb `dubte_D1` i robustesa D1 àmplia = 1 (la regla 26 ja la preveu).

**Impacte:**
- Standard Life Aberdeen 2017 i 2018: d'1 a 0 (2 files).
- Abans d'aplicar-ho cal ampliar els anys de les entrades X01-X04 i registrar l'entrada de Skeoch el 1999.
- EssilorLuxottica (3 files) i ICAP/NEX (3 files) només si la cerca documenta que va ser una adquisició.

## Q4, Q5 i Q5b. Redacció de la cita i qui la publica

**Metodologia.**
- La P6 ja admet «set up» amb la persona com a subjecte.
- Pel criteri a del PR #3, compta qui ha escrit el document.
- La D37a té una robustesa per a les cites no contemporànies.

**Literatura.** Cap paper fa una llista d'equivalències: n'hi ha prou amb l'etiqueta «founder» o la inferència per la biografia (Fahlenbrach, p. 442). Les fonts retrospectives (Hoover's, històries corporatives, publicacions d'aniversari) s'accepten. Cap paper no tracta el grup successor.

**Recomanació:**
- Energean: compta.
- Paysafe i Merlin: compten, amb `allotjament=successor` i `founderceo_rob_cita_contemporania` = 0.

**Impacte:** cap canvi d'etiqueta.

## Q6. «Cofundador» només en premsa

**Metodologia.** La P6 ja ho regula: un «sí» de font B compta si cap font A/B no el contradiu, amb `si_font_B` i robustesa com a ND.

**Literatura.**
- Fahlenbrach i AAF accepten una font de premsa.
- Villalonga i Amit (p. 392) en demanen dues, i que cap n'anomeni una altra persona.

**Recomanació:** Evraz 2018-2020 a 1, amb `si_font_B`, la robustesa ND i, a més, una robustesa de dues fonts (`n_A + n_B ≥ 2`), que reprodueix VA. Cal comprovar que «co-founder of Evraz» es refereix a la cotitzada o a una predecessora (P1).

## Q7. Refundadors (criteri FT)

**Metodologia.** La regla 6 (resolta per la P5 el 16/11) diu que els fundadors transformadors que compleixen el criteri del PROTOCOL són 1 a l'anàlisi principal i 0 a `founderceo_rob_sense_ft`. **El criteri del PROTOCOL no és al repositori**, i el tribunal el demanarà.

**Literatura.** Hi ha dues tradicions:
- La **europea** compta el *raider* o qui pren el control d'una empresa i la transforma:
  - Sraer i Thesmar (2007, p. 714 i 743): Pinault, Bolloré;
  - Barontini i Caprio (2006, p. 700): Arnault, «the founder of a new family dynasty»;
  - Andres (2008, p. 7): participació majoritària + CEO + canvi del negoci.
- La **nord-americana** exclou MBO i LBO (Fahlenbrach, p. 442; Villalonga i Amit, p. 392), però admet uns quants transformadors amb robustesa (Buffett i Tisch a Fahlenbrach; Galvin, Graham i Walter a VA).
- AAF (p. 138-139) compten una adquisició «that leads to a major change in the development of the company».

**Recomanació:**
1. Escriure el criteri FT a la metodologia. Proposta, a partir d'Andres i Barontini-Caprio: la persona pren el control (primer accionista individual) d'una empresa existent, n'és CEO o president executiu i en transforma el negoci de manera documentada en una font A/B. Es manté la marca `ft`/`tipus_ft` i la robustesa `founderceo_rob_sense_ft`.
2. Aplicar-lo igual a tots els FT actuals (LVMH, CTS Eventim i els que n'hi hagi) i a ACS.
3. Per a ACS, buscar primer si l'emissor o la premsa l'anomenen fundador (D37 / `si_font_B`).

**Impacte:** ACS 2016 i 2021, +2 F si compleix el criteri. Els FT actuals no canvien si ja el compleixen.

## Q8b, Q9, Q9b i C1. President executiu i consejero delegado (regla única proposada)

**Metodologia.** Hi ha una tensió interna:
- R1 identifica el CEO pel «títol de CEO o equivalent legal», i la P5 inclou el consejero delegado.
- R3 diu que un president executiu només compta si el càrrec de CEO és vacant.
- A Telefónica, el president té el títol de «CEO» (a la versió anglesa) i el consejero delegado és qualificat de «COO».
- A BME, l'IAGC diu que Zoido (president) era el «primer ejecutivo» mentre Hernani era consejero delegado.

**Literatura.**
- La regla dominant és **la persona que l'emissor designa com a CEO** al document regulat: ExecuComp CEOANN, la SEC («or acting in a similar capacity») i Fernandes et al. (2013, «the highest-ranking executive»).
- A França, el CEO és el PDG o el DG, i el DGD no (Kramarz i Thesmar).
- A Espanya no hi ha consens:
  - Crespí i Pascual (Banco de España 2009, p. 93-94) segueixen l'autodeclaració de l'IAGC;
  - Stein i Gallego (IESE 2012) segueixen els poders delegats.
- Cap paper no dona prioritat a una traducció: tots dos fan servir l'IAGC original.

**Recomanació (regla única):**
1. Si dues persones tenen el càrrec legal de consejero delegado, són co-CEO. És la Q8, ja decidida (Ferrovial).
2. Si hi ha un president executiu i un consejero delegado, el CEO és **qui el document regulat original de l'emissor designa com a primer executiu** («primer ejecutivo», «máximo responsable ejecutivo», CEO), amb la marca `ceo_president_exec` si és el president. Si l'emissor no designa ningú, mana el càrrec legal (el consejero delegado, R1). Es fa una robustesa amb l'altra persona.
3. Es llegeix el document original. La traducció anglesa de l'emissor només serveix de suport.

**Aplicació:**
- Telefónica 2017-2025: el president (com vas decidir), si l'IAGC original el designa primer executiu. Cal comprovar-ho al text castellà.
- BME 2017-2018: **Zoido** (X04: «tenía atribuidas como primer ejecutivo de la Sociedad»). Per tant, **la correcció C1 no s'aplica**, i Hernani va a la robustesa.
- Mapfre i Inditex: el president (no hi ha consejero delegado), amb `ceo_president_exec`.
- EssilorLuxottica 2020: Del Vecchio (PDG).

**Impacte:** cap a FounderCEO, perquè totes aquestes persones són no fundadores per qualsevol via. La columna `ceos` no canvia si es confirma la designació a Telefónica.

## Q10, Q13, Q14 i Q15. Altres criteris de CEO

- **Q10, Luxottica.** Hi ha un CEO amb títol (Vian), i per tant el càrrec no és vacant: R1. Del Vecchio entra a la robustesa R3. La literatura no considera co-CEO qui cobreix una plaça de manera informal. Cap canvi.
- **Q13, impedit o de baixa.** El titular continua sent el CEO mentre el càrrec no quedi vacant: Ballinger i Marcel (2010) defineixen l'interí amb vacant. Si l'emissor nomena formalment algú «en funcions», va a la robustesa R2. Cap canvi.
- **Q14, CD Projekt.** «Joint CEO» és el títol que l'emissor dona a Iwiński en documents de l'exercici. La literatura identifica els co-CEO pel títol, i no hi ha precedent per al títol funcional. Recomanació: co-CEO (R1), amb la marca `co_ceo_titol_funcional` i **robustesa sense ell**, on 4 files passen d'1 a 0, perquè Adam Kiciński no és fundador.
- **Q15.** D21 ja ho permet (`proxy_tancament`). La literatura data el CEO per exercici, i el nostre 31/10 és més exigent. Gabaix, Landier i Sauvagnat (2014) fan servir una regla d'interval equivalent a la nostra regla 28.

## Q12 i Q12b. Gestió externa

**Literatura.** El més habitual és **excloure** les financeres i immobiliàries (AAF, VA, Sraer i Thesmar, Barontini i Caprio, Andres). Als REIT amb gestor extern no es codifica cap CEO persona (Cannon i Vogt 1995).

**Recomanació:**
- Cada any mana el document de l'emissor: R1 si designa un CEO de la cotitzada; R3 si atribueix literalment la direcció a una persona; R-SC si declara que no té direcció pròpia.
- Marca nova `gestio_externa` i **robustesa que exclou aquestes empreses**, la més propera a la pràctica de la literatura.
- BB Biotech: NA, perquè preval l'emissor.

**Impacte:**
- Anàlisi principal: cap canvi. Tritax 2021-2025 es manté a 1 si l'informe de cada any anomena Godfrey CEO de la plc. Primary Health 2020 depèn de la redacció.
- Robustesa: n'hi surten unes 6 files F.

## C2, C3 i C4. Correccions de dades

- **C2, Sopra Steria 2025: ND → 0.** Prova a: «Founded in January 1968 by Pierre Pasquier, François Odin and Léo Gantelet». Pecquet no hi és. La fila entra a la mostra.
- **C3, Dassault Systèmes 2016-2020: 0 → 1.** «As Co-Founder and CEO, Bernard guided our company…» (emissor, 2026). Va ser una escissió de Dassault Aviation (1981), i per la P4 compta perquè l'emissor l'anomena cofundador. AAF hi donen suport: compten el «main executive at the time the company began». Marques: `fundador_escissio`, D37a = 0 (cita no contemporània). Abans d'aplicar-ho, cal afegir la frase del mateix comunicat que porta el nom complet.
- **C4, Bridgepoint 2021-2022: 0 → 1.** «William Jackson, Bridgepoint's Founder» (emissor, 2024). L'empresa va néixer d'un MBO de NatWest el 2000. La regla 5 diu que els MBO són 0, llevat que l'emissor els anomeni fundadors (D37). Marques: D37a = 0, `founderceo_rob_sense_origen_intern` = ND.

## Casos nous que ha tret la fitxa de fundació (per a una propera ronda)

- **Drillisch 2018.** Adquisició inversa: comptablement, el comprador és 1&1. Si l'entitat que compta és 1&1, Dommermuth en seria fundador i el 0 no se sosté.
- **Danone i Pernod Ricard.** Totes dues parlen de «fusió» i de «fundador del Grup» en singular, però avui es classifiquen diferent. Cal una sola regla.
- **Wirecard.** Una font B diu que Braun és fundador, i el Bundestag i l'emissor ho contradiuen (`conflicte_fonts`).
- **Covivio.** Kullmann dirigeix l'empresa «depuis sa création en 2001»: podria ser cofundador.
- **Sonova.** L'emissor anomena fundadors els que la van comprar el 1965.

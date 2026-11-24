# Lot 18 · Fitxa de fundació per empresa i prova de no fundador per parts (24/11/2026)

Aplica la decisió de Jordi del 24/11/2026 (opció b): un 0 només compta com a documentat si la prova té **totes les parts**, cadascuna amb la seva cita A/B. Tres peces:

1. **Fitxa de fundació per empresa.** Per a les 970 empreses amb files P, agents de cerca (grups de 10 empreses) van buscar qui la va fundar (o quin Estat o empresa la va crear) i quan, amb cites literals. Un **verificador independent per grup** va intentar refutar cada fitxa. Només s'importen les empreses amb veredicte «ok», sense les cites que el verificador treu.
   - 1.665 entrades noves (1.642 [V], 23 [NV] `pendent_arxiu`);
   - 361 empreses amb prova a o e verificada, que cobreixen 2.079 files P;
   - 638 empreses (correccions o dubtes del verificador) a `lot18_dubtes.csv`, per a una segona passada.
2. **Etiquetes de les parts (doble codificació).** Les 2.688 cites de fundador anteriors de les empreses amb files P les han llegit **dos codificadors independents a cegues** amb el codebook `lot18_codebook_parts.md`, i un tercer ha resolt els desacords. Acord: **88,4 %** (2.375 de 2.688). Cada entrada porta a les notes etiquetes `[part …]` amb el valor (any de fundació, naixement, ocupador anterior…). Script: `traspas/escriu_etiquetes_parts.py`.
3. **Càlcul de la C2 de les files P per parts** (`estat/estat_files.py`). Llegeix les etiquetes i fa l'aritmètica de la regla 21: b (menys de 18 anys a la fundació), d (entrada 3 o més anys després, amb ocupador anterior), c (64 anys o més fins a l'inici del mandat, només sense edat). La C3 de les P demana una cita verificada a Wayback per a cada part.

## Efecte

| | Abans (criteri antic) | Ara (per parts) |
|---|---:|---:|
| Files P amb prova de no fundador | 5.005 (88,9 %) | **2.339 (41,6 %)** |
| … prova a / e / b / d / c | — | 1.475 / 549 / 218 / 85 / 12 |
| Files P amb alguna part, però sense prova completa | — | 2.603 |
| Files acabades (total) | 356 | **55** |

La caiguda de les files acabades és temporal: la C3 per parts demana que **cada part** estigui verificada a la còpia de Wayback, i les 1.665 cites noves encara no s'han arxivat. El flux de Wayback les processarà a les properes execucions.

## Pendent

- Les 638 empreses de `lot18_dubtes.csv` (correccions del verificador i dubtes de criteri).
- Dades de persona (naixement, ocupador anterior, inici del mandat) per a les 2.603 files P amb prova incompleta.
- 10 files on una cita diu que el CEO és fundador (`contradiccio`): revisió cas per cas.

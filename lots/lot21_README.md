# Lot 21 · Correccions de la fitxa de fundació i dades de persona (24/11/2026)

Segona passada per a les files P amb la prova de no fundador incompleta després del lot 18. Dues vies que no necessiten cerca web nova:

1. **Correccions del verificador (pas 1).** Les 181 empreses del lot 18 que el verificador independent havia marcat «corregir». Quatre agents hi han aplicat les correccions que no demanen cap cerca: treure les cites dolentes, reclassificar parts, corregir anys o fundadors i afegir cites que ja eren als fitxers baixats (instruccions a `lot21_brief_correccions.md`).
   - 155 empreses corregides; 26 pendents d'una cerca o d'una decisió (`lot21_pendents_correccio.csv`).
   - Importades amb `traspas/importa_fitxa_fundacio.py`: **590 entrades** (569 [V]); 109 empreses amb algun dubte de l'importador (`lot21_dubtes.csv`).
2. **Dades de persona dels documents que ja teníem (pas 2).** `traspas/extreu_dades_persona.py` busca, als informes ja baixats, frases amb el cognom del CEO i el naixement, l'edat o l'inici del mandat, i frases amb l'any de fundació. `traspas/etiqueta_dades_persona.py` les etiqueta amb patrons estrictes. Cinc agents han revisat **cada** etiqueta i cada frase de fundació (`lot21_brief_revisio_persona.md`): de 932 etiquetes, 743 bones, 33 corregides i 156 rebutjades; de 1.348 frases de fundació, 226 bones.
   - Importades amb `traspas/importa_entrades.py`: **954 entrades** (948 [V], cita literal comprovada al document); 28 rebutjades per l'importador.

L'edat es converteix en any de naixement amb el criteri de la metodologia: l'any més antic possible (any del document − edat − 1).

## Efecte a la C2 de les files P

| | Després del lot 18 | Després del lot 21 |
|---|---:|---:|
| Files P amb prova completa per parts | 2.339 (41,6 %) | **2.921 (51,9 %)** |
| … prova a / e / b / d / c | 1.475 / 549 / 218 / 85 / 12 | 1.621 / 593 / 481 / 121 / 105 |
| Amb alguna part però sense prova completa | 2.603 | 2.512 |
| Sense cap part documentada | 677 | 186 |

Cap canvi d'etiqueta ni de CEO.

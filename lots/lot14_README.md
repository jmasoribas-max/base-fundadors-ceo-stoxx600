# Lot 14: files P, traspàs de les cites de l'auditoria

- **Fet per:** Claude, 23/11/2026, amb [`traspas/importa_lot.py`](../traspas/importa_lot.py) a partir de les candidates de [`traspas/candidates_auditoria.py`](../traspas/candidates_auditoria.py), com el [lot 11](lot11_README.md).
- **Abast:** les 1.590 files P (FounderCEO=0) de 297 empreses que, abans del lot, no tenien cita de CEO, de prova de no fundador o de cap de les dues ([`lot14.csv`](lot14.csv)). Només s'hi afegeixen proves; **cap canvi de FounderCEO ni de `ceos`**.

## Criteris nous respecte del lot 11

### Cita de CEO: document de l'exercici

El document ha de ser de l'exercici que inclou el 31/10 de la fila (CLAUDE.md §3). Abans, l'importador acceptava qualsevol document publicat l'any de la fila o el següent. Per això podia agafar l'informe de l'exercici anterior, publicat a principis d'any. Ara es comprova així:
- **Informe llarg:** l'any que més hi surt ha de ser el de la fila (o el següent si l'exercici és partit, com 2019/20).
- **Comunicat curt:** la data ha de ser de l'any de la fila.
- **Document que no s'obre:** l'any del nom del fitxer o la data.

Aquest canvi treu 126 files que abans s'haurien cobert.

### Prova de no fundador: totes les parts, cadascuna amb la seva cita

Cada prova necessita totes les seves parts, cadascuna amb una cita que la contingui:

| Prova | Parts |
|---|---|
| a | llista de fundadors que no inclou el CEO i que anomena algú |
| b | any de fundació i naixement del CEO |
| c | any de fundació, com a mínim 64 anys abans de l'any de la fila |
| d | ocupador anterior del CEO i any de fundació |
| e | origen en una altra entitat o en l'Estat |

- De cada cita candidata se'n retalla la frase que conté la part.
- Les parts de l'empresa (fundació, origen, llista) han de tenir l'empresa com a subjecte o anomenar-la.
- Les parts del CEO (naixement, ocupador anterior) han d'anomenar-lo, sense cap altra persona com a subjecte.
- Es descarten els fragments de taules o de text barrejat.

Una mostra de la primera versió tenia proves febles, com «Born in 1970, Dutch nationality» sol per a la b, o fragments de biografia d'una altra empresa. Amb aquest filtre, el lot cobreix menys files (102 en lloc de 697), però les cites són netes.

## Resultats

| Recompte | Valor |
|---|---:|
| Files del lot | 1.590 (297 empreses) |
| Files fetes (cita de CEO i de fundador) | 101 |
| … de les quals amb `ceo_interval` | 0 |
| Files amb cita de CEO nova `[V]` | 256 |
| Files amb prova de no fundador completa nova `[V]` | 102 |
| Files en dubte enviades a `PENDENTS.md` | 0 (és un traspàs; les files sense cita són a [`lot14_pendents.csv`](lot14_pendents.csv)) |
| Entrades noves `[V]` | 278 (250 de CEO, 28 de parts de prova) |
| Entrades noves `[NV]` | 28 (de CEO; `pendent_arxiu`: el document original no s'obre) |
| … amb nota `no_valida` | 0 |
| Fonts antigues revisades | 18 (lot 11; vegeu més avall) |
| … `no_valida` | 8 |
| Canvis proposats a FounderCEO o `ceos` | 0 |

Detall de les files pendents ([`lot14_pendents.csv`](lot14_pendents.csv)):
- **1.260** sense cita de CEO de l'exercici. Les de 2020-2025 es busquen al lot 15 als informes ESEF; les altres necessiten una cerca nova.
- **1.039** sense prova completa de no fundador. En 375 hi ha una part de la prova, però en falta una altra: per exemple, a la b hi ha el naixement però no l'any de fundació (150 files) o al revés (90).

## Revisió de les cites de CEO del lot 11 (fonts antigues)

Les cites de CEO dels lots 11 a 13 s'han revisat amb el criteri nou de l'exercici. Els lots 12 i 13 (cerca nova) no tenen cap problema; les alertes que hi surten són falses alarmes, perquè són empreses amb un exercici que no coincideix amb l'any natural i el document és el correcte. Al lot 11 (traspàs de l'auditoria IA), 18 entrades usaven un document d'un altre exercici per a un o més anys:

- **8 entrades queden `[NV]` amb `no_valida`:** el document no és de l'exercici de cap dels anys de l'entrada. Són zooplus 2021, Netcompany 2022, Teleperformance 2025, Arkema 2024 i 2025, Neoen 2024 i InPost 2024 i 2025.
- **10 entrades redueixen els anys** als que sí que són de l'exercici del document; la nota diu de quins anys a quins. Són CTS Eventim, HelloFresh, Eurofins (dues), Ubisoft, EssilorLuxottica, Arkema i Adyen (dues).

Cap entrada no s'esborra: el canvi i el motiu consten a les `notes`. Les files afectades tornen a no tenir cita de CEO i es busquen de nou. 18 són files F: el grup F passa de 349 a 331 files amb cita de CEO, fins que es trobin les noves.

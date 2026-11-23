# Lot 11: grup F, traspàs de cites de l'auditoria IA i de l'inventari antic

- **Fet per:** Claude, 23/11/2026, amb [`traspas/importa_lot.py`](../traspas/importa_lot.py) a partir de les candidates de [`traspas/candidates_auditoria.py`](../traspas/candidates_auditoria.py) (fitxers de DF a `df/fitxers-per-claude`, commit `34cff60`).
- **Abast:** les 349 files F (88 empreses), [`lot11.csv`](lot11.csv). Només s'hi afegeixen proves; **cap canvi de FounderCEO ni de `ceos`**.
- **Criteris:**
  - Cita de CEO: anomena el CEO de la fila, conté un títol de primer executiu i és d'un document de l'exercici (any de la fila o el següent); no es fan servir frases de sortida («stepped down», «resign»…) ni cites on el cognom correspon a una altra persona.
  - Cita de fundador: anomena el CEO, conté un mot de fundació admès per la P6 (no «founding CEO», «CEO fundador», «founding shareholder» ni «founding member») i esmenta l'empresa o hi fa referència.
  - Les cites es retallen a la frase rellevant, que és un fragment literal del text verificat.
  - Si una cita és d'un agregador (`annualreports.com`), porta la nota `agregador=true` per substituir-la per la còpia de l'emissor.
- **Verificació:** les cites ja trobades literalment per scripts de DF (manifest r4, certificació r3e) entren com a [V], amb el nom de l'script a `model_verificacio`. Les altres les ha baixat Claude del web original: [V] si hi ha la cita, [NV] amb `pendent_DF` si el document no s'obre.

## Resultats

| Recompte | Valor |
|---|---:|
| Files del lot | 349 |
| Files fetes (cita de CEO i de fundador, segons `estat/`) | 99 (abans del lot: 44) |
| … de les quals amb `ceo_interval` | 0 |
| Files amb cita de CEO | 105 (abans: 47) |
| Files amb cita de fundador | 292 (abans: 211) |
| Entrades noves al registre | 74 (55 de CEO, 19 de fundador) |
| … `[V]` | 66 |
| … `[NV]` (`pendent_DF`) | 8 |
| … `no_valida` | 0 |
| … amb `agregador=true` | 17 |
| Fonts antigues revisades | 0 |
| Canvis proposats a FounderCEO o `ceos` | 0 |

Files que continuen sense cita: [`lot11_pendents.csv`](lot11_pendents.csv), 232 sense cita de CEO (66 empreses) i 57 sense cita de fundador (22 empreses). La majoria eren files «certificades» per l'auditoria r3e, que no tenia cita de CEO. Cal una cerca nova (informe anual de cada exercici); no hi ha límit d'intents.

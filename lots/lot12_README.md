# Lot 12: grup F, cerca nova de cites de CEO

- **Fet per:** Claude, 23/11/2026. Cerca en paral·lel amb sis agents (66 empreses; llista [`traspas/cerca_ceo_f_llista.csv`](../traspas/cerca_ceo_f_llista.csv)), i verificació i importació amb [`traspas/importa_cerca.py`](../traspas/importa_cerca.py).
- **Abast:** les 232 files F que, després del lot 11, no tenien cita de CEO ([`lot11_pendents.csv`](lot11_pendents.csv), `falta=ceo`). Només s'hi afegeixen proves; **cap canvi de FounderCEO ni de `ceos`**.
- **Normes de la cerca:**
  - Document de l'exercici que inclou el 31/10, o interval de la regla 28.
  - Cita literal del document baixat, de fonts A/B, sense agregadors ni Wayback.
  - Discrepàncies i files no trobades, declarades.
- **Verificació independent (Claude):** per a cada cita:
  1. La cita ha d'anomenar el CEO de la fila i contenir un títol de primer executiu o el seu equivalent legal (Gérant a les SCA, President of the Management Board a Polònia…).
  2. El document ha de ser de l'exercici; el document final d'un interval, posterior al 31/10.
  3. Claude torna a baixar el document de la URL i hi busca la cita literal; als PDF a columnes, també amb `pdftotext -raw`; als ESEF, dins el zip.
  - L'evidència es decideix per persona: a les files de co-CEO, cada CEO necessita la seva.

## Resultats

| Recompte | Valor |
|---|---:|
| Files del lot | 232 (66 empreses) |
| Files amb cita de CEO (C1) | 232 |
| Files fetes (cita de CEO i de fundador) | 183 |
| … de les quals amb `ceo_interval` | 8 (Actelion 2016, Zalando 2016-2018, CD Projekt 2020-2021, Rubis 2016 i 2018) |
| Files en dubte enviades a `PENDENTS.md` | 23 (secció «Dubtes del lot 12»: Primary Health Properties 2020, Tritax Big Box 2021-2025, CD Projekt 2018-2021, Zalando 2016-2018, Rubis 2016-2025) |
| Entrades noves `[V]` | 262 (184 de l'emissor, 57 de reguladors, 21 de plataformes de comunicats oficials; cap agregador) |
| Entrades noves `[NV]` | 0 |
| … amb nota `no_valida` | 0 |
| Fonts antigues revisades | 0 |
| Canvis proposats a FounderCEO o `ceos` | 0 |

Detalls:
- Una cita (Adyen 2024, Ingo Uytdehaage) s'ha rebutjat perquè només l'anomena pel nom de pila; la fila queda coberta per una altra cita que anomena tots dos co-CEO.
- Una cita s'ha verificat al fitxer que va baixar la cerca, perquè la re-descàrrega no ha funcionat; ho diu a `model_verificacio`.

**Grup F després del lot:** 337 de 349 files amb cita de CEO (abans 105) i 282 completes (abans 99).

Les 12 files F que encara no compleixen la condició del CEO tenen dues causes, i es reprenen en un lot posterior:
- 10 tenien al lot 11 una cita `[NV]` (document que no s'obria).
- 2 són co-CEO on la cita del lot 11 només anomena un dels dos (Zalando 2023, Adyen 2023).

# Lot 27 · Cita de CEO de l'exercici per a les files amb una cita d'un altre any (25/11/2026)

## Per què

La revisió de l'exercici de les cites de CEO antigues (lots anteriors al 12) va marcar 1.095 files-any: segons un script heurístic, el document de la cita podia ser d'un altre exercici. Un auditor independent n'ha revisat una mostra de 80 (60 marcades i 20 de control). El resultat és a `lot27_auditoria_mostra.csv`.

- **Cap CEO equivocat.** En tots els documents que s'han pogut obrir, la persona és el CEO de la base.
- **Un 24 % de les files marcades** (9 de 37 obribles) tenen un problema real de data. La cita és només un extrem del mandat: o el nomenament en un document d'abans del 31/10, o la sortida en un document posterior. No té el segon extrem que demana la regla 28 (interval), i per tant no acredita el 31/10 de l'any. Exemples: Nestlé 2019 («CEO until August 31, 2024») i Solvay 2021 (informe del 2018).
- **La resta són falses alarmes:** exercicis no naturals, documents posteriors que diuen explícitament «since 2012», o seccions web de l'informe.
- **Accés:** 26 de les 80 fonts no es poden obrir amb curl pla (SEC, Akamai, Cloudflare). A aquestes els caldrà la captura del Wayback.

Dels 1.095 avisos, 328 files ja tenien una altra cita de CEO bona. En queden **714 files (234 empreses)** que només depenen de la cita avisada (`lot27.csv`).

## Què s'ha fet

Mateix mètode que el lot 15:
- **Informes:** `traspas/troba_esef.py` (ESEF, exercicis 2020-2025) i `traspas/troba_nsm.py` (FCA NSM, emissors britànics) busquen l'informe anual oficial de l'exercici que conté el 31/10.
- **Cites:** `traspas/extreu_ceo_documents.py --totes` n'extreu un fragment literal que anomena el CEO amb el títol.

Canvis als scripts:
- **`--totes`:** també tracta files que ja compleixen C1.
- **Filtre nou de capçaleres de taula:** descarta els fragments amb tres anys o més (p. ex. «Chief Executive 2025 20 24 2023…») i els de menys de tres paraules. S'han revisat 30 cites a mà abans d'escriure.

| | Files |
|---|---:|
| Files del lot | 714 |
| Amb informe oficial de l'exercici trobat | ~275 (132 ESEF, 143 NSM) |
| **Amb cita de CEO nova de l'exercici** | **198** (199 entrades `[V]`) |
| Sense cita nova (`lot27_pendents.csv`) | 516 |

Cap canvi de FounderCEO ni de `ceos`. Les cites antigues no s'esborren: la cita nova de l'exercici passa a ser la principal.

## Què queda

A les 516 files restants no hi ha informe oficial per script: són de Suïssa, del 2016-2019 fora del Regne Unit, o de documents sense cap frase que passi els filtres. Si s'hi aplica la taxa de la mostra, unes 125 tindrien el problema de data de debò. Per trobar-les i corregir-les cal una cerca amb agents, com al lot 17. Per a cada fila, l'agent ha de mirar si la cita actual acredita el 31/10 i, si no, ha de buscar el document de l'exercici o el segon extrem de l'interval. Pendent de l'OK de Jordi.

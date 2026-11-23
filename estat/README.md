# Estat per fila de la base

Aquesta carpeta conté el comptador únic de progrés de la base. Respon, per a cadascuna de les 6.012 files (ISIN-any), si la fila està **acabada** segons la definició del pla ([`docs/PLA_FINALITZACIO_20261123.md`](../docs/PLA_FINALITZACIO_20261123.md), secció 1) i, si no ho està, què li falta.

| Fitxer | Què és |
|---|---|
| [`estat_files.py`](estat_files.py) | L'script. Només llegeix fitxers locals; no fa cap petició de xarxa ni modifica `dades/` |
| [`estat_files.csv`](estat_files.csv) | Una fila per ISIN-any amb l'estat de cada condició (generat) |
| [`RESUM_ESTAT.md`](RESUM_ESTAT.md) | Resum per etiqueta, embut, mancances, empreses i llista d'incoherències (generat) |
| [`dubtes_tancats.csv`](dubtes_tancats.csv) | Files amb un dubte de `PENDENTS.md` ja tancat (s'hi afegeixen línies quan un PR tanca un dubte) |
| [`llista_urls_arxiu.py`](llista_urls_arxiu.py) | Genera [`urls_per_arxivar.csv`](urls_per_arxivar.csv): les URL del registre amb cita que encara no tenen la cita verificada a una captura Wayback. És l'entrada de la passada d'arxivament (`wayback_arxiva.py`, a l'ordinador amb les claus) |

## Com s'executa

```bash
python3 estat/estat_files.py
```

```bash
python3 estat/estat_files.py --comprova
```

La primera ordre regenera `estat_files.csv` i `RESUM_ESTAT.md`. La segona no escriu res i falla si aquests dos fitxers no corresponen a les dades actuals; serveix per al CI. Cada PR que canviï el registre, la base, `PENDENTS.md` o `dubtes_tancats.csv` ha de tornar a executar la primera ordre i incloure'n el resultat.

## Les quatre condicions

Una cita és **vàlida** si l'entrada de `docs/REGISTRE_CANVIS.csv` té `cita_literal`, `url_font` http(s), `marca_veritat=[V]` i les notes no contenen `no_valida`. El camp `anys` s'expandeix (accepta llistes i intervals).

| Condició | Columna | Valors |
|---|---|---|
| **C1 CEO** | `c1_ceo` | `ok`: hi ha cites vàlides amb `funcio_cita=ceo` que anomenen cadascun dels CEO de `ceos`. `co_ceo_parcial`: només n'anomenen algun. `cita_sense_nom`: hi ha cita de CEO però no anomena la persona. `falta`: no hi ha cita de CEO. Per a NA: `rsc_documentat` / `falta_rsc` |
| | `c1_tipus` | `document` o `interval` (si `marca_prova` esmenta un interval) |
| **C2 Fundador** | `c2_fundador` | `ok_registre`: cita vàlida amb `funcio_cita=fundador`. `ok_columna_antiga`: només hi ha la cita antiga del CSV (`font_classificacio_cita` amb URL). `falta`. Per a NA i ND: `rsc_documentat` / `cerca_documentada` si hi ha alguna entrada vàlida (CEO, fundador o context) |
| **C3 Arxiu** | `c3_arxiu` | `ok`: almenys una cita de C1 i una de C2 tenen `cita_verificada_a_captura=si`. Si no, `falta_ceo`, `falta_fundador`, `falta_ceo+fundador`, `falta_fundador_columna_antiga` o `sense_evidencia` |
| **C4 Coherència** | `c4_coherencia` | `ok` o la llista de problemes: `ceos_diferent_de_sim_ceo_aplicat`, `F_sense_regla_de_si`, `P_sense_prova_de_no`, `P_amb_regla_de_si`, `motiu_nd_residual`, `NA_sense_motiu_na` |
| | `dubtes_oberts` | Dubtes oberts a `PENDENTS.md` (seccions de dubtes de la regla 29 i dels lots 9 i 10) que no són a `dubtes_tancats.csv`. Un ND porta sempre `ND_obert` fins que no consti tancat |

`estat` val `acabada` si es compleixen les quatre condicions i no hi ha dubtes oberts. Si no, enumera el que falta: `falta_ceo`, `falta_fundador`, `incoherent`, `dubte_obert`, `falta_arxiu`.

Regles que identifiquen una prova a `regles`: de «sí», `cita_fundador`, `D37`, `FT`, `D10b_prelacio`, `D10`; de «no», `a`, `b`, `c_AAF64_reserva`, `d`, `e`, `d_per_part`, `b_per_part`.

## Limitacions conegudes

- **Nom a la cita.** Es comprova que la cita contingui algun dels cognoms del CEO (els mots del nom, tret del nom de pila i de partícules com «de» o «van», sense accents). No detecta el nom en un altre alfabet (p. ex. ciríl·lic).
- **Càrrec a la cita.** Només es comprova com a avís (`carrec_no_detectat_a_la_cita`), amb una llista de títols en diverses llengües; no bloqueja.
- **Exercici del document.** L'script no pot saber si el document és de l'exercici que inclou el 31/10; ho ha de garantir qui escriu l'entrada (`CLAUDE.md` §3). Quan el registre tingui el camp de data del document (tasca 0.3 del pla), s'hi afegirà.
- **Prova coherent amb l'etiqueta.** La regla es llegeix de `regles` del CSV, perquè `marca_prova` del registre no té un format uniforme (tasca 0.3).
- **Cita antiga del CSV.** `font_classificacio_cita` compta per a C2, però no per a C3, perquè no té la verificació a la captura.
- **NA i ND.** Qualsevol entrada vàlida que cobreixi la fila es pren com a cerca documentada; no se'n valora si la cerca és exhaustiva. Un ND no es dona per acabat fins que no consta a `dubtes_tancats.csv`.
- **Dubtes del registre.** Les entrades `tipus=dubte_metodologic` del registre no es compten com a dubte obert (n'hi ha dels lots 5 i 7 que eren residuals; pendent d'aclarir, pregunta 15 a Grok).

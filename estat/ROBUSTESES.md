# Robusteses calculades per script

Generat per `estat/robusteses.py` a partir de la base, del registre i de `estat/estat_files.py`. No toca `dades/`: les columnes es copiaran a la base en congelar-la. Les regles de cada columna són a la capçalera de l'script.

Mostra principal (`a_mostra_principal`=1): 5.960 files. 350 F (5.87 %).

| Columna | Files que canvien (tota la base) | F a la mostra | P a la mostra | ND a la mostra | Altres a la mostra | % F (F / (F + P)) |
|---|---:|---:|---:|---:|---:|---:|
| `founderceo_rob_regla25_nd` | 943 | 318 | 4699 | 943 | 0 | 6.34 % |
| `founderceo_rob_r25_p1p2` | 87 | 344 | 5529 | 87 | 0 | 5.86 % |
| `founderceo_rob_r25_p3` | 152 | 350 | 5458 | 152 | 0 | 6.03 % |
| `founderceo_rob_r25_p4` | 23 | 327 | 5610 | 23 | 0 | 5.51 % |
| `founderceo_rob_r25_p6` | 3 | 347 | 5610 | 3 | 0 | 5.83 % |
| `founderceo_rob_r25_p7` | 10 | 350 | 5600 | 10 | 0 | 5.88 % |
| `founderceo_rob_r25_p8` | 651 | 350 | 4959 | 651 | 0 | 6.59 % |
| `founderceo_rob_sense_interval` | 53 | 342 | 5565 | 53 | 0 | 5.79 % |
| `founderceo_rob_conflicte_fonts` | 7 | 357 | 5603 | 0 | 0 | 5.99 % |
| `founderceo_rob_dues_fonts` | 13 | 337 | 5610 | 13 | 0 | 5.67 % |
| `founderceo_rob_sense_gestio_externa` | 12 | 343 | 5609 | 0 | 8 | 5.76 % |
| `founderceo_rob_sense_titol_funcional` | 11 | 346 | 5607 | 0 | 7 | 5.81 % |
| `founderceo_rob_c_com_nd` | 125 | 344 | 5491 | 125 | 0 | 5.90 % |
| `founderceo_rob_llista_predecessora_nd` | 127 | 350 | 5483 | 127 | 0 | 6.00 % |
| `founderceo_rob_0_documentat` | 35 | 350 | 5576 | 34 | 0 | 5.91 % |

`founderceo_rob_llista_predecessora_nd` i la cerca d'una segona font per a les files F amb una sola font: decisió de Jordi del 25/11/2026.

# Robusteses calculades per script

Generat per `estat/robusteses.py` a partir de la base, del registre i de `estat/estat_files.py`. No toca `dades/`: les columnes es copiaran a la base en congelar-la. Les regles de cada columna són a la capçalera de l'script.

Mostra principal (`a_mostra_principal`=1): 5.961 files. 351 F (5.89 %).

| Columna | Files que canvien (tota la base) | F a la mostra | P a la mostra | ND a la mostra | Altres a la mostra | % F (F / (F + P)) |
|---|---:|---:|---:|---:|---:|---:|
| `founderceo_rob_regla25_nd` | 938 | 319 | 4704 | 938 | 0 | 6.35 % |
| `founderceo_rob_r25_p1p2` | 86 | 345 | 5530 | 86 | 0 | 5.87 % |
| `founderceo_rob_r25_p3` | 148 | 351 | 5462 | 148 | 0 | 6.04 % |
| `founderceo_rob_r25_p4` | 23 | 328 | 5610 | 23 | 0 | 5.52 % |
| `founderceo_rob_r25_p6` | 3 | 348 | 5610 | 3 | 0 | 5.84 % |
| `founderceo_rob_r25_p7` | 10 | 351 | 5600 | 10 | 0 | 5.90 % |
| `founderceo_rob_r25_p8` | 651 | 351 | 4959 | 651 | 0 | 6.61 % |
| `founderceo_rob_sense_interval` | 38 | 343 | 5580 | 38 | 0 | 5.79 % |
| `founderceo_rob_conflicte_fonts` | 7 | 358 | 5603 | 0 | 0 | 6.01 % |
| `founderceo_rob_dues_fonts` | 220 | 132 | 5610 | 219 | 0 | 2.30 % |
| `founderceo_rob_sense_gestio_externa` | 12 | 343 | 5609 | 0 | 9 | 5.76 % |
| `founderceo_rob_sense_titol_funcional` | 11 | 347 | 5607 | 0 | 7 | 5.83 % |
| `founderceo_rob_c_com_nd` | 127 | 345 | 5489 | 127 | 0 | 5.91 % |
| `founderceo_rob_llista_predecessora_nd` | 127 | 351 | 5483 | 127 | 0 | 6.02 % |

`founderceo_rob_llista_predecessora_nd` i la cerca d'una segona font per a les files F amb una sola font: decisió de Jordi del 25/11/2026.

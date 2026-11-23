# Lot 13: les 12 últimes files F sense cita de CEO

- **Fet per:** Claude, 23/11/2026. Cerca amb dos agents i verificació i importació amb [`traspas/importa_cerca.py`](../traspas/importa_cerca.py), amb els mateixos criteris que el [lot 12](lot12_README.md).
- **Abast:** les 12 files F que després del lot 12 encara no complien la condició del CEO:
  - 10 tenien al lot 11 una cita `[NV]`, perquè el document original no s'obria (alstria 2020, Genmab 2024, Cellnex 2022, Alten 2025, EssilorLuxottica 2020, Tullow 2016, Allfunds 2023-2024, LPP 2024-2025);
  - 2 són de co-CEO on la cita del lot 11 només anomenava un dels dos (Zalando 2023, Adyen 2023).
- Només s'hi afegeixen proves; **cap canvi de FounderCEO ni de `ceos`**. Les entrades `[NV]` del lot 11 es mantenen tal com eren.

## Resultats

| Recompte | Valor |
|---|---:|
| Files del lot | 12 (10 empreses) |
| Files amb cita de CEO (C1) | 12 |
| Files fetes (cita de CEO i de fundador) | 10 (alstria 2020 i Cellnex 2022 encara no tenen cita de fundador) |
| … de les quals amb `ceo_interval` | 0 |
| Files en dubte enviades a `PENDENTS.md` | 0 |
| Entrades noves `[V]` | 15 (9 de l'emissor, 4 de reguladors, 2 de plataformes de comunicats oficials) |
| Entrades noves `[NV]` | 0 |
| Fonts antigues revisades | 0 |
| Canvis proposats a FounderCEO o `ceos` | 0 |

**Grup F després del lot:** totes les 349 files tenen cita de CEO. 292 també tenen cita de fundador; les 57 restants (22 empreses) són la feina següent del grup F.

## Notes per a la revisió

- **Cellnex 2022 i Alten 2025 (BALO del 2026):** la re-descàrrega de Claude ha rebut un error (403 i temps esgotat). La cita s'ha comprovat literalment al fitxer que la cerca va baixar de la mateixa URL, i ho diu a `model_verificacio`.
- **Alten 2025:** al 31/10/2025, Simon Azoulay era Président-Directeur Général. El BALO de la junta del 2026 diu «Président-Directeur Général jusqu'au 17 novembre 2025», data en què Cyril Malargé va passar a ser Directeur Général. No hi ha discrepància amb `ceos`.
- **EssilorLuxottica 2020:** al 31/10/2020, Leonardo Del Vecchio era Président-Directeur Général (fins al 17/12/2020), segons el document d'enregistrement universel del 2020 (còpia de l'AMF, p. 78). Fins a aquella data, Hubert Sagnières era Vice-Président-Directeur Général Délégué, amb poders iguals als del PDG (p. 107). La base el té com a CEO únic per R1, perquè el títol de CEO és només de Del Vecchio. Ho anoto perquè Jordi decideixi si cal tractar-ho com a co-CEO.
- **Correcció d'allotjament al lot 12:** 18 entrades del lot 12 (`echanges.dila.gouv.fr`) tenien `allotjament=emissor`. Ara diuen `regulador`, perquè és la còpia oficial (DILA) dels documents dipositats a l'AMF. La correcció consta a les `notes` de cada entrada.
- **Canvis a l'importador** ([`traspas/importa_lot.py`](../traspas/importa_lot.py)), que es fan servir als lots següents:
  - Els documents que no s'obren es marquen `pendent_arxiu` (abans `pendent_DF`).
  - Les baixades de filings.xbrl.org es fan amb l'agent de curl, perquè aquest dipòsit refusa els agents de navegador.
  - Llista d'allotjaments ampliada: DILA, Journal officiel (BALO) i info-financiere.fr com a reguladors; Ritzau i pressetext com a plataformes de comunicats.
  - Comprovació de l'exercici del document a les cites de CEO que es traspassen de l'auditoria. L'informe ha de ser de l'exercici que inclou el 31/10 de la fila, no el de l'any anterior publicat a principis d'any. Es fa servir a partir del lot 14. Les cites dels lots 11 i 12 es revisaran amb el mateix criteri.

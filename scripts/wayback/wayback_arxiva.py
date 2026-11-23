#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arxiva a Wayback Machine les URL de font de la base (main).

Claus nomes via variables d'entorn IA_S3_ACCESS i IA_S3_SECRET.
Mai s'imprimeixen, ni s'escriuen a fitxers ni als logs (ni parcialment).
Nomes llibreria estandard + requests. verify=True (sense -k).
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
import time
from collections import OrderedDict
from pathlib import Path

try:
    import requests
except ImportError:
    sys.stderr.write(
        "Falta la llibreria 'requests'. Instal·la-la amb:\n"
        "  python -m pip install requests\n"
    )
    sys.exit(1)

SAVE_URL = "https://web.archive.org/save"
STATUS_URL = "https://web.archive.org/save/status/"
AVAILABLE_URL = "https://archive.org/wayback/available"
CDX_URL = "https://web.archive.org/cdx/search/cdx"
USER_AGENT = (
    "base-fundadors-ceo-stoxx600 wayback_arxiva "
    "(recerca academica; github.com/jmasoribas-max/base-fundadors-ceo-stoxx600)"
)
RESULT_FIELDS = [
    "url",
    "estat",
    "timestamp_captura",
    "url_wayback",
    "http_codi",
    "missatge",
]
FETS = {"ja_existia", "capturada"}
PAUSA_DEFECTE = 8
MAX_REINTENTS_DEFECTE = 5
POLLING_SEGONS = 5
POLLING_MAX = 60  # 5 minuts


class ClausFalten(Exception):
    pass


def _dir_script() -> Path:
    return Path(__file__).resolve().parent


def _llegeix_claus():
    access = os.environ.get("IA_S3_ACCESS") or ""
    secret = os.environ.get("IA_S3_SECRET") or ""
    # No retinguem ni comprovem el contingut mes enlla de si son buides.
    if not access.strip() or not secret.strip():
        raise ClausFalten(
            "Falten les variables d'entorn IA_S3_ACCESS i/o IA_S3_SECRET. "
            "Defineix-les a la sessio (vegeu LLEGEIX-ME.md) i torna-ho a executar."
        )
    return access.strip(), secret.strip()


def _capcaleres_auth(access: str, secret: str) -> dict:
    # Aquesta capcalera no s'ha d'imprimir ni registrar mai.
    return {
        "Authorization": "LOW %s:%s" % (access, secret),
        "Accept": "application/json",
        "User-Agent": USER_AGENT,
    }


def _capcaleres_publiques() -> dict:
    return {"User-Agent": USER_AGENT, "Accept": "application/json"}


def _wayback_url(timestamp: str, original: str) -> str:
    ts = (timestamp or "").strip()
    orig = (original or "").strip()
    if not ts or not orig:
        return ""
    if orig.startswith("http://") or orig.startswith("https://"):
        return "https://web.archive.org/web/%s/%s" % (ts, orig)
    return ""


def _any_de_timestamp(ts: str) -> str:
    ts = (ts or "").strip()
    return ts[:4] if len(ts) >= 4 and ts[:4].isdigit() else ""


def _carrega_input(path: Path) -> "OrderedDict[str, dict]":
    """Agrupa per URL unica, en ordre de primera aparicio."""
    agrupat = OrderedDict()
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            url = (row.get("url") or "").strip()
            if not url:
                continue
            any_obj = (row.get("any_objectiu") or "").strip()
            cap = (row.get("captura_indicada") or "").strip() == "1"
            wb = (row.get("url_wayback_indicada") or "").strip()
            if url not in agrupat:
                agrupat[url] = {
                    "anys": [],
                    "captura_indicada": False,
                    "url_wayback_indicada": "",
                }
            info = agrupat[url]
            if any_obj and any_obj not in info["anys"]:
                info["anys"].append(any_obj)
            if cap:
                info["captura_indicada"] = True
                if wb and not info["url_wayback_indicada"]:
                    info["url_wayback_indicada"] = wb
    return agrupat


def _carrega_fets(path: Path) -> set:
    fets = set()
    if not path.is_file():
        return fets
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return fets
        for row in reader:
            url = (row.get("url") or "").strip()
            estat = (row.get("estat") or "").strip()
            if url and estat in FETS:
                fets.add(url)
    return fets


def _obre_sortida(path: Path):
    nou = (not path.is_file()) or path.stat().st_size == 0
    f = path.open("a", newline="", encoding="utf-8")
    writer = csv.DictWriter(f, fieldnames=RESULT_FIELDS, extrasaction="ignore")
    if nou:
        writer.writeheader()
        f.flush()
    return f, writer


def _escriu(f, writer, fila: dict) -> None:
    writer.writerow({k: fila.get(k, "") for k in RESULT_FIELDS})
    f.flush()


def _pausa(segons: float) -> None:
    if segons > 0:
        time.sleep(segons)


def _backoff(intent: int) -> float:
    # 30, 60, 120, 240, 300 (sostre)
    return min(300, 30 * (2 ** max(0, intent - 1)))


def _demana(sessio: requests.Session, metode: str, url: str, **kwargs):
    """requests sense verificar=False. No registra capcaleres."""
    kwargs.setdefault("timeout", 60)
    kwargs.setdefault("allow_redirects", True)
    return sessio.request(metode, url, **kwargs)


def _consulta_available(sessio, url: str, timestamp: str = ""):
    params = {"url": url}
    if timestamp:
        params["timestamp"] = timestamp
    r = _demana(sessio, "GET", AVAILABLE_URL, params=params, headers=_capcaleres_publiques())
    return r


def _consulta_cdx(sessio, url: str):
    params = {
        "url": url,
        "output": "json",
        "fl": "timestamp,statuscode,original",
        "filter": "statuscode:200",
        "limit": "100",
    }
    r = _demana(sessio, "GET", CDX_URL, params=params, headers=_capcaleres_publiques())
    return r


def _extreu_available(data: dict):
    try:
        closest = (data or {}).get("archived_snapshots", {}).get("closest") or {}
    except AttributeError:
        return "", ""
    if not closest or not closest.get("available"):
        return "", ""
    ts = str(closest.get("timestamp") or "").strip()
    wb = str(closest.get("url") or "").strip()
    if wb.startswith("http://web.archive.org/"):
        wb = "https://" + wb[len("http://"):]
    if not wb and ts:
        orig = str(closest.get("url") or "")
        wb = _wayback_url(ts, orig) if orig.startswith("http") and "web.archive.org" not in orig else wb
    return ts, wb


def _escull_cdx(files, anys_objectiu):
    """files: llista de [timestamp, status, original] (sense capcalera)."""
    candidats = []
    for row in files:
        if not row or len(row) < 1:
            continue
        ts = str(row[0]).strip()
        if not ts.isdigit():
            continue
        orig = str(row[2]).strip() if len(row) > 2 else ""
        candidats.append((ts, orig))
    if not candidats:
        return "", ""
    objectius = {a for a in anys_objectiu if a and a.isdigit()}
    preferits = [c for c in candidats if _any_de_timestamp(c[0]) in objectius]
    tria = preferits[0] if preferits else candidats[0]
    ts, orig = tria
    return ts, _wayback_url(ts, orig) if orig else _wayback_url(ts, orig)


def _busca_captura_existent(sessio, url: str, anys_objectiu, pausa: float, max_reintents: int):
    """Retorna (timestamp, url_wayback, http_codi, nota) o error via excepcio/tupla."""
    anys = [a for a in anys_objectiu if a and a.isdigit()]
    ts_pref = (anys[0] + "1231") if anys else ""
    ultim_codi = ""
    errors_transitori = {429, 500, 502, 503, 504}

    def amb_reintents(fn, etiqueta):
        nonlocal ultim_codi
        darrer_err = None
        for intent in range(1, max_reintents + 1):
            try:
                r = fn()
            except requests.RequestException as exc:
                darrer_err = "excepció de xarxa (%s)" % exc.__class__.__name__
                ultim_codi = ""
                if intent < max_reintents:
                    _pausa(_backoff(intent))
                    continue
                return None, darrer_err
            ultim_codi = str(r.status_code)
            if r.status_code in errors_transitori:
                darrer_err = "%s HTTP %s" % (etiqueta, r.status_code)
                if intent < max_reintents:
                    retry_after = r.headers.get("Retry-After")
                    espera = None
                    if retry_after and retry_after.isdigit():
                        espera = min(300, int(retry_after))
                    _pausa(espera if espera is not None else _backoff(intent))
                    continue
                return r, darrer_err
            return r, None
        return None, darrer_err or ("%s ha fallat" % etiqueta)

    r, err = amb_reintents(
        lambda: _consulta_available(sessio, url, ts_pref),
        "available",
    )
    ts, wb = "", ""
    nota = ""
    if r is not None and r.status_code == 200:
        try:
            ts, wb = _extreu_available(r.json())
        except ValueError:
            nota = "available: resposta no JSON"
    elif err:
        nota = err

    any_ok = _any_de_timestamp(ts) in set(anys) if anys and ts else bool(ts)
    if ts and wb and any_ok:
        return ts, wb, ultim_codi, "available (any objectiu)" if anys else "available"

    # CDX: mira totes les captures i prefereix l'any objectiu
    r2, err2 = amb_reintents(lambda: _consulta_cdx(sessio, url), "cdx")
    if r2 is not None and r2.status_code == 200:
        try:
            data = r2.json()
        except ValueError:
            data = None
            if not nota:
                nota = "cdx: resposta no JSON"
        if isinstance(data, list) and len(data) > 1:
            ts2, wb2 = _escull_cdx(data[1:], anys)
            if ts2 and wb2:
                any_c = _any_de_timestamp(ts2)
                tag = "cdx (any objectiu)" if (anys and any_c in set(anys)) else "cdx (altra data)"
                return ts2, wb2, str(r2.status_code), tag
    elif err2:
        nota = (nota + "; " if nota else "") + err2

    if ts and wb:
        return ts, wb, ultim_codi, "available (altra data)"

    return "", "", ultim_codi, nota or "sense captura"


def _spn_desa(sessio, url: str, access: str, secret: str, pausa: float, max_reintents: int):
    errors_transitori = {429, 500, 502, 503, 504}
    darrer_codi = ""
    for intent in range(1, max_reintents + 1):
        try:
            r = _demana(
                sessio,
                "POST",
                SAVE_URL,
                headers=_capcaleres_auth(access, secret),
                data={"url": url, "capture_all": "1"},
                timeout=90,
            )
        except requests.RequestException as exc:
            darrer_codi = ""
            if intent < max_reintents:
                _pausa(_backoff(intent))
                continue
            return {
                "estat": "error",
                "timestamp_captura": "",
                "url_wayback": "",
                "http_codi": darrer_codi,
                "missatge": "pendent_verificacio_externa: excepció de xarxa al Save Page Now (%s)"
                % exc.__class__.__name__,
            }
        darrer_codi = str(r.status_code)
        if r.status_code in errors_transitori:
            if intent < max_reintents:
                retry_after = r.headers.get("Retry-After")
                espera = min(300, int(retry_after)) if retry_after and retry_after.isdigit() else _backoff(intent)
                _pausa(espera)
                continue
            return {
                "estat": "error",
                "timestamp_captura": "",
                "url_wayback": "",
                "http_codi": darrer_codi,
                "missatge": "pendent_verificacio_externa: Save Page Now HTTP %s després de reintents"
                % r.status_code,
            }
        if r.status_code not in (200, 201):
            return {
                "estat": "error",
                "timestamp_captura": "",
                "url_wayback": "",
                "http_codi": darrer_codi,
                "missatge": "pendent_verificacio_externa: Save Page Now HTTP %s" % r.status_code,
            }
        try:
            payload = r.json()
        except ValueError:
            return {
                "estat": "error",
                "timestamp_captura": "",
                "url_wayback": "",
                "http_codi": darrer_codi,
                "missatge": "pendent_verificacio_externa: Save Page Now no ha tornat JSON",
            }
        job_id = str(payload.get("job_id") or "").strip()
        if not job_id:
            # de vegades la resposta ja porta timestamp
            ts = str(payload.get("timestamp") or "").strip()
            if ts:
                return {
                    "estat": "capturada",
                    "timestamp_captura": ts,
                    "url_wayback": _wayback_url(ts, url),
                    "http_codi": darrer_codi,
                    "missatge": "Save Page Now sense job_id, amb timestamp",
                }
            return {
                "estat": "error",
                "timestamp_captura": "",
                "url_wayback": "",
                "http_codi": darrer_codi,
                "missatge": "pendent_verificacio_externa: Save Page Now sense job_id",
            }
        return _spn_polling(sessio, job_id, url, access, secret, darrer_codi)
    return {
        "estat": "error",
        "timestamp_captura": "",
        "url_wayback": "",
        "http_codi": darrer_codi,
        "missatge": "pendent_verificacio_externa: Save Page Now ha esgotat els reintents",
    }


def _spn_polling(sessio, job_id: str, url: str, access: str, secret: str, http_alta: str):
    # job_id ve de l'API; no el tractem com a secret, pero no hi afegim les claus.
    for _ in range(POLLING_MAX):
        _pausa(POLLING_SEGONS)
        try:
            r = _demana(
                sessio,
                "GET",
                STATUS_URL + job_id,
                headers=_capcaleres_auth(access, secret),
                timeout=60,
            )
        except requests.RequestException:
            continue
        if r.status_code in (429, 500, 502, 503, 504):
            _pausa(_backoff(1))
            continue
        if r.status_code != 200:
            continue
        try:
            data = r.json()
        except ValueError:
            continue
        estat = str(data.get("status") or "").lower()
        if estat == "success":
            ts = str(data.get("timestamp") or "").strip()
            orig = str(data.get("original_url") or data.get("original") or url).strip()
            wb = str(data.get("original_url") and data.get("timestamp") and _wayback_url(ts, orig) or "")
            if not wb:
                wb = _wayback_url(ts, url)
            return {
                "estat": "capturada",
                "timestamp_captura": ts,
                "url_wayback": wb,
                "http_codi": http_alta,
                "missatge": "Save Page Now 2",
            }
        if estat == "error":
            msg = str(data.get("message") or data.get("status_ext") or "error de job")
            # no reenviem cossos llargs per si de cas
            if len(msg) > 200:
                msg = msg[:200]
            return {
                "estat": "error",
                "timestamp_captura": "",
                "url_wayback": "",
                "http_codi": http_alta,
                "missatge": "pendent_verificacio_externa: job Save Page Now: %s" % msg,
            }
        # pending / other: continua el polling
    return {
        "estat": "error",
        "timestamp_captura": "",
        "url_wayback": "",
        "http_codi": http_alta,
        "missatge": "pendent_verificacio_externa: el job Save Page Now no ha acabat a temps (es pot reprendre)",
    }


def processa(args) -> int:
    try:
        access, secret = _llegeix_claus()
    except ClausFalten as exc:
        sys.stderr.write(str(exc) + "\n")
        return 2

    entrada = Path(args.input)
    sortida = Path(args.output)
    if not entrada.is_file():
        sys.stderr.write("No trobo el fitxer d'entrada: %s\n" % entrada)
        return 2

    agrupat = _carrega_input(entrada)
    fets = _carrega_fets(sortida)
    pendents = []
    indicades = []
    for url, info in agrupat.items():
        if url in fets:
            continue
        if info["captura_indicada"] and not args.totes:
            indicades.append((url, info))
        else:
            pendents.append((url, info))

    if args.limit is not None:
        pendents = pendents[: max(0, args.limit)]

    total_net = len(pendents)
    print(
        "URL uniques al fitxer: %d. Ja fetes (reprendre): %d. "
        "Amb captura indicada (sense xarxa): %d. A consultar/desar: %d."
        % (len(agrupat), len(fets), len(indicades), total_net)
    )

    sessio = requests.Session()
    f, writer = _obre_sortida(sortida)
    n_ja = n_cap = n_err = 0
    try:
        for url, info in indicades:
            wb = info.get("url_wayback_indicada") or ""
            ts = ""
            if "/web/" in wb:
                try:
                    despres = wb.split("/web/", 1)[1]
                    ts = despres.split("/", 1)[0].replace("id_", "").replace("if_", "").replace("oe_", "")
                except IndexError:
                    ts = ""
            _escriu(
                f,
                writer,
                {
                    "url": url,
                    "estat": "ja_existia",
                    "timestamp_captura": ts,
                    "url_wayback": wb,
                    "http_codi": "",
                    "missatge": "captura ja indicada al CSV de main",
                },
            )
            n_ja += 1

        for i, (url, info) in enumerate(pendents, start=1):
            print("Consulta %d/%d" % (i, total_net))
            try:
                ts, wb, codi, nota = _busca_captura_existent(
                    sessio, url, info["anys"], args.pausa, args.max_reintents
                )
            except requests.RequestException:
                ts, wb, codi, nota = "", "", "", "excepció de xarxa en la consulta"
            if ts and wb:
                _escriu(
                    f,
                    writer,
                    {
                        "url": url,
                        "estat": "ja_existia",
                        "timestamp_captura": ts,
                        "url_wayback": wb,
                        "http_codi": codi,
                        "missatge": nota,
                    },
                )
                n_ja += 1
                _pausa(args.pausa)
                continue

            resultat = _spn_desa(
                sessio, url, access, secret, args.pausa, args.max_reintents
            )
            resultat["url"] = url
            if nota and resultat.get("estat") == "error":
                resultat["missatge"] = (
                    resultat.get("missatge") or ""
                ) + ((" | consulta prèvia: " + nota) if nota else "")
            elif nota and resultat.get("estat") == "capturada":
                resultat["missatge"] = (resultat.get("missatge") or "") + " (no n'hi havia cap d'existent)"
            _escriu(f, writer, resultat)
            if resultat["estat"] == "capturada":
                n_cap += 1
            else:
                n_err += 1
            _pausa(args.pausa)
    finally:
        f.close()
        # No deixem les claus a cap estructura que es pugui imprimir en un error final.
        access = secret = None
        del access, secret

    print(
        "Acabat. ja_existia=%d capturada=%d error=%d. Resultat: %s"
        % (n_ja, n_cap, n_err, sortida)
    )
    return 0


def main(argv=None) -> int:
    base = _dir_script()
    parser = argparse.ArgumentParser(
        description="Arxiva a Wayback les URL de font de urls_main.csv (reprenible)."
    )
    parser.add_argument(
        "--input",
        default=str(base / "urls_main.csv"),
        help="CSV d'entrada (defecte: urls_main.csv al mateix directori)",
    )
    parser.add_argument(
        "--output",
        default=str(base / "wayback_resultats.csv"),
        help="CSV de resultats incremental (defecte: wayback_resultats.csv)",
    )
    parser.add_argument(
        "--pausa",
        type=float,
        default=PAUSA_DEFECTE,
        help="Segons de pausa entre URL (defecte: %s)" % PAUSA_DEFECTE,
    )
    parser.add_argument(
        "--max-reintents",
        type=int,
        default=MAX_REINTENTS_DEFECTE,
        help="Reintents si Wayback respon 429 o 5xx (defecte: %s)" % MAX_REINTENTS_DEFECTE,
    )
    parser.add_argument(
        "--totes",
        action="store_true",
        help="Consulta també les URL que ja tenen captura indicada al CSV de main",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Processa com a molt N URL pendents (prova). No afecta les ja indicades.",
    )
    args = parser.parse_args(argv)
    if args.pausa < 0:
        sys.stderr.write("La pausa no pot ser negativa.\n")
        return 2
    if args.max_reintents < 1:
        sys.stderr.write("Cal almenys 1 intent.\n")
        return 2
    return processa(args)


if __name__ == "__main__":
    sys.exit(main())

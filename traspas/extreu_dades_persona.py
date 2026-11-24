"""Pas 2 (24/11/2026): candidats de dades de persona (naixement, inici del mandat, entrada i
ocupador anterior) i d'any de fundació per a les files P sense prova completa, a partir dels
documents que ja tenim baixats (memòria cau de text). Sense descàrregues noves."""
import csv, re, sys, json, hashlib, collections, importlib.util, glob
from pathlib import Path
ROOT = Path('/home/user/base-fundadors-ceo-stoxx600'); S = Path(sys.argv[1])
sys.path.insert(0, str(ROOT/'estat')); import estat_files as E
spec = importlib.util.spec_from_file_location('IL', ROOT/'traspas/importa_lot.py'); IL = importlib.util.module_from_spec(spec); spec.loader.exec_module(IL)
C = S/'baixades'
B = list(csv.DictReader(open(ROOT/'dades/base_isin_any_v8r3.csv', encoding='utf-8')))
est = {(r['isin'], r['any']): r for r in csv.DictReader(open(ROOT/'estat/estat_files.csv', encoding='utf-8'))}
reg = list(csv.DictReader(open(ROOT/'docs/REGISTRE_CANVIS.csv', encoding='utf-8')))
inc = [r for r in B if r['FounderCEO'] == '0' and not est[(r['isin'], r['any'])]['c2_fundador'].startswith('ok_prova_')]
ceos = collections.defaultdict(set); nom = {}
for r in inc:
    nom[r['isin']] = r['nom_panell']
    for n in (r['ceos'] or '').split('|'):
        if n: ceos[r['isin']].add(n)
urls = collections.defaultdict(dict)
for e in reg:
    if e['isin'] in ceos and (e['url_font'] or '').startswith('http'):
        urls[e['isin']].setdefault(e['url_font'], e['anys'])
ANY = r'(19[2-9]\d|20[0-2]\d)'
NAIX = re.compile(r'\b(born|née?|geboren|geb\.|nacid[oa]|nat[oa] (?:a|il|nel)|født|född|syntynyt|urodzon[ya]|year of birth|date of birth|birth year|jahrgang|geburtsjahr|année de naissance|date de naissance|año de nacimiento)\b[^.;]{0,60}?' + ANY, re.I)
EDAT = re.compile(r'\b(aged?|âgée?|age:|alter:?|edad:?)\s*(\d{2})\b|\b(\d{2})\s*(years old|ans\b|jahre\b|años\b)', re.I)
INICI = re.compile(r'\b(since|seit|depuis|desde|dal|sedan|siden|from|appointed|nommée?|ernannt|bestellt|nombrad[oa]|named|became)\b[^.;]{0,80}?' + ANY, re.I)
CARREC = re.compile(r'\b(ceo|chief executive|vorstandsvorsitz|vorsitzende[rn]? des vorstand|directeur général|directrice générale|président-directeur|consejer[oa] delegad[oa]|amministratore delegato|verkställande direktör|administrerende direktør|toimitusjohtaja|prezes zarządu|group chief|managing director)', re.I)
ANT = re.compile(r'\b(prior to joining|before joining|previously|joined[^.;]{0,60}\bfrom\b|vor seinem eintritt|zuvor|auparavant|avant de rejoindre|anteriormente|tidigare|tidligere)\b', re.I)
FUND = re.compile(r'\b(founded|established|incorporated|gegründet|fondée?|fundad[ao]|costituit[ao]|opgericht|grundad|stiftet|perustettu)\b[^.;]{0,60}?' + r'(1[5-9]\d\d|20[0-2]\d)|\b(1[5-9]\d\d|20[0-2]\d)\b[^.;]{0,40}\b(founded|established|incorporated|gegründet|fondée?|fundad[ao])\b', re.I)
def frases(t):
    t = re.sub(r'[ \t]+', ' ', t)
    return [f.strip() for f in re.split(r'(?<=[.;])\s+|\n\s*\n', t) if 20 <= len(f.strip()) <= 450]
def cognom(n):
    p = [x for x in re.split(r'\s+', n) if x.lower() not in E.PARTICULES and len(x) > 2]
    return p[-1] if p else n
out = []; stats = collections.Counter()
for isin, us in urls.items():
    vistos = set()
    for url, anys in us.items():
        t = C/(hashlib.sha256(url.encode()).hexdigest() + '.txt')
        if not t.exists(): stats['sense_cache'] += 1; continue
        txt = t.read_text(encoding='utf-8', errors='ignore')
        if txt.startswith('#ERROR') or len(txt) < 200: continue
        stats['docs'] += 1
        for f in frases(txt):
            fn = E.norm(f); tipus = []
            persones = [n for n in ceos[isin] if E.norm(cognom(n)) in fn]
            if persones:
                if NAIX.search(f): tipus.append('naixement')
                elif EDAT.search(f): tipus.append('edat')
                if INICI.search(f) and CARREC.search(f): tipus.append('inici_mandat')
                if ANT.search(f): tipus.append('ocupador_anterior')
            if FUND.search(f) and not persones: tipus.append('any_fundacio')
            if not tipus: continue
            k = (E.norm(f)[:120])
            if k in vistos: continue
            vistos.add(k)
            out.append(dict(isin=isin, empresa=nom[isin], ceos=sorted(ceos[isin]), persones=persones, tipus=tipus, url=url, anys_doc=anys, frase=f))
            for x in tipus: stats[x] += 1
# limita any_fundacio a 6 per ISIN (prioritat a frases curtes)
per = collections.defaultdict(list)
for o in out: per[o['isin']].append(o)
final = []
for isin, os_ in per.items():
    af = sorted([o for o in os_ if o['tipus'] == ['any_fundacio']], key=lambda o: len(o['frase']))[:6]
    final += [o for o in os_ if o['tipus'] != ['any_fundacio']] + af
json.dump(final, open(S/'persona/candidats.json', 'w'), ensure_ascii=False)
print(dict(stats), 'candidats', len(final), 'isin', len(per))

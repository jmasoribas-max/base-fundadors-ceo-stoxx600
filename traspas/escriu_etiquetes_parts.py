"""Afegeix al registre les etiquetes [part …] de la doble codificació independent (24/11/2026)."""
import csv, io, json, re, sys, glob, collections
from pathlib import Path
S = Path(sys.argv[1]); REG = Path('docs/REGISTRE_CANVIS.csv')
fin = json.load(open(S / 'etiquetes/finals.json', encoding='utf-8'))
ceos = {}
for f in glob.glob(str(S / 'etiquetes/lots/*.json')):
    for e in json.load(open(f, encoding='utf-8')):
        ceos[e['id']] = e['ceos_anys_entrada'] + e['altres_ceos_isin']
def net(v): return re.sub(r'[\];\[]', ',', v or '').strip()
def etiq(p):
    part, val, et = p['part'], net(p.get('valor')), p.get('entitat_tipus') or 'incert'
    if part == 'any_altre' or not val: return ''
    if part in ('naixement_ceo', 'entrada', 'inici_mandat', 'ocupador_anterior'):
        nom = val.split(':')[0].strip()
        if not nom or nom == '?': return ''
        if part == 'naixement_ceo':
            m = re.search(r'age\s*(\d{2})\s*in\s*(\d{4})', val)
            if m: val = f"{nom}:{int(m.group(2)) - int(m.group(1)) - 1}"
            elif not re.search(r':\s*(1[89]\d\d|20[0-2]\d)\b', val): return ''
        return f"[part {part}={val}]"
    if part == 'any_fundacio':
        m = re.search(r'\b(1[5-9]\d\d|20[0-2]\d)\b', val)
        if not m: return ''
        val = m.group(1)
    t = f"[part {part}={val}; entitat={et}"
    if part == 'llista_fundadors': t += f"; tancada={p.get('tancada') or 'no'}"
    return t + ']'
rows = list(csv.reader(open(REG, encoding='utf-8', newline='')))
cap = rows[0]; ci = {c: i for i, c in enumerate(cap)}
n = 0; c = collections.Counter()
for r in rows[1:]:
    e = fin.get(r[ci['id_document_o_font']])
    if not e: continue
    tags = [t for t in (etiq(p) for p in e['parts']) if t]
    if e.get('ceo_fundador') == 'si':
        noms = [x for x in ceos.get(e['id'], []) if x.split()[-1].lower() in (e.get('nota_entrada') or '').lower()]
        if noms: tags.append(f"[ceo_fundador={noms[0]}]")
        else: tags.append("[ceo_fundador=?]")
    font = 'acord dels dos codificadors' if e.get('font') == 'acord' else 'adjudicació d\'un tercer codificador'
    nota = f" Parts de la prova (doble codificació independent, 24/11/2026; {font}): " + (' '.join(tags) if tags else 'cap part.')
    if 'Parts de la prova (doble codificació' in r[ci['notes']]: continue
    r[ci['notes']] = (r[ci['notes']] + nota).strip(); n += 1
    for t in tags: c[t.split('=')[0]] += 1
buf = io.StringIO(); csv.writer(buf, lineterminator='\r\n').writerows(rows)
REG.write_bytes(buf.getvalue().encode('utf-8'))
print('entrades etiquetades', n, dict(c))

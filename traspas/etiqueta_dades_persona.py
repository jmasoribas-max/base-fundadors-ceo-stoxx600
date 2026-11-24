"""Etiquetes per script (patrons estrictes) dels candidats de persona: naixement, edat i inici del
mandat de CEO. L'any de fundació el revisa un agent (és massa sorollós per a un patró)."""
import json, re, sys, csv, collections
S = sys.argv[1]
c = json.load(open(S + '/persona/candidats.json'))
ANY = r'(19[2-9]\d|20[0-2]\d)'
def cognom(n):
    return [x for x in n.split() if len(x) > 2][-1]
NAIX = [re.compile(p, re.I) for p in [
    r'\b(?:born|née?|geboren|geb\.|nacid[oa]|født|född|syntynyt|urodzon[ya])\b(?: (?:in|on|en|le|am|el|i|w|à|a)\b)?[^.;\d]{0,40}?(?:\d{1,2}[./ ]\s?\w*\.?\s?)?' + ANY,
    r'\b(?:year of birth|date of birth|birth year|jahrgang|geburtsjahr|année de naissance|date de naissance|año de nacimiento)\b\s*:?\s*(?:\d{1,2}[./ ]\s?\w*\.?\s?)?' + ANY]]
EDAT = re.compile(r'\b(?:aged?|âgée? de|age:|alter:?|edad:?)\s*(\d{2})\b|\b(\d{2})\s*(?:years old|ans\b|jahre alt|años\b)', re.I)
INICI = re.compile(r'\b(?:(?:chief executive officer|ceo|group ceo|president and ceo|vorstandsvorsitzende[rn]?|directeur général|consejero delegado|amministratore delegato|verkställande direktör|toimitusjohtaja|prezes zarządu)\b[^.;]{0,25}?\b(?:since|seit|depuis|desde|dal|sedan|siden)\s+(?:\w+\s+){0,2}?' + ANY
                   + r'|(?:appointed|nommée?|ernannt|nombrad[oa]|named|became)\s+(?:as\s+)?(?:group\s+)?(?:chief executive officer|ceo|directeur général|vorstandsvorsitzende[rn]?|consejero delegado)\b[^.;]{0,30}?(?:in|on|en|le|am|with effect from|effective)\s+(?:\w+\s+){0,3}?' + ANY + r')', re.I)
out = []; st = collections.Counter()
for o in c:
    for p in o['persones']:
        cg = cognom(p)
        # la persona ha d'aparèixer abans del patró, a menys de 160 caràcters
        f = o['frase']; i = f.lower().find(cg.lower())
        if i < 0: continue
        cola = f[i:i + 220]
        tags = []
        if 'naixement' in o['tipus']:
            for rx in NAIX:
                m = rx.search(cola)
                if m: tags.append(('naixement_ceo', f'{p}:{m.group(m.lastindex)}')); break
        if 'edat' in o['tipus'] and not tags:
            m = EDAT.search(cola)
            if m:
                edat = int(m.group(1) or m.group(2)); t = min(int(x) for x in re.findall(r'\d{4}', o['anys_doc'])[:1] or [0])
                if t and 25 <= edat <= 85: tags.append(('naixement_ceo', f'{p}:{t - edat - 1}')); st['edat_convertida'] += 1
        if 'inici_mandat' in o['tipus']:
            m = INICI.search(cola)
            if m: tags.append(('inici_mandat', f'{p}:{[g for g in m.groups() if g][-1]}'))
        if len(o['persones']) > 1 and tags:
            # dues persones a la frase: només si el patró segueix el cognom d'aquesta persona sense l'altra entremig
            altres = [cognom(q).lower() for q in o['persones'] if q != p]
            if any(a in cola[:120].lower() for a in altres): continue
        for part, val in tags:
            out.append(dict(isin=o['isin'], anys=o['anys_doc'], funcio_cita='fundador', marca_prova={'naixement_ceo': 'b', 'inici_mandat': 'c'}[part],
                            part=part, persona=p, url=o['url'], cita_literal=f.strip(), nivell='A',
                            notes=f'Part de la prova: {part} (etiqueta per patró estricte, 24/11/2026). [part {part}={val}]'))
            st[part] += 1
json.dump(out, open(S + '/persona/etiquetes_script.json', 'w'), ensure_ascii=False)
w = csv.DictWriter(open(S + '/persona/entrades_persona.csv', 'w', newline='', encoding='utf-8'), fieldnames=list(out[0]))
w.writeheader(); w.writerows(out)
print(dict(st), 'entrades', len(out), 'isin', len({o["isin"] for o in out}))

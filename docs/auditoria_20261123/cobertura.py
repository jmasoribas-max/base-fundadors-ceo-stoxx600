import csv, re, collections, unicodedata, json, sys
import os
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
b=list(csv.DictReader(open(f'{ROOT}/dades/base_isin_any_v8r3.csv',encoding='utf-8')))
r=list(csv.DictReader(open(f'{ROOT}/docs/REGISTRE_CANVIS.csv',encoding='utf-8')))
def years(s):
    out=set()
    for part in re.split(r'[,;\s]+', s.strip()):
        if not part: continue
        m=re.match(r'^(\d{4})-(\d{4})$',part)
        if m:
            a,z=int(m.group(1)),int(m.group(2)); out|=set(str(y) for y in range(a,z+1))
        elif re.match(r'^\d{4}$',part): out.add(part)
    return out
def norm(s):
    s=unicodedata.normalize('NFKD',s); s=''.join(c for c in s if not unicodedata.combining(c))
    return s.lower()
FUND_OK0={'a','b','c','d','e'}
def fund_rules(mp):
    toks=set(t.strip().lower() for t in re.split(r'[,;/ ]+',mp) if t.strip())
    return toks
idx=collections.defaultdict(list)
orphan=collections.Counter()
keys={(x['isin'],x['any']) for x in b}
for e in r:
    ys=years(e['anys'])
    for y in ys:
        if (e['isin'],y) in keys: idx[(e['isin'],y)].append(e)
        else: orphan[e['origen']]+=1
res=[]
for row in b:
    k=(row['isin'],row['any']); es=idx.get(k,[])
    lab=row['FounderCEO']
    names=[n for n in row['ceos'].split('|') if n.strip()]
    surn=[norm(n.split()[-1]) for n in names]
    def ok(e): return bool(e['cita_literal'].strip()) and bool(e['url_font'].strip())
    def V(e): return ok(e) and e['marca_veritat']=='[V]' and 'no_valida' not in e['notes']
    ceo=[e for e in es if e['funcio_cita']=='ceo' and ok(e)]
    ceoV=[e for e in ceo if V(e)]
    ceoVname=[e for e in ceoV if any(s and s in norm(e['cita_literal']) for s in surn)]
    ceocap=[e for e in ceoV if e['cita_verificada_a_captura']=='si']
    fun=[e for e in es if e['funcio_cita']=='fundador' and ok(e)]
    funV=[e for e in fun if V(e)]
    funVcap=[e for e in funV if e['cita_verificada_a_captura']=='si']
    # consistency of founder proof with label
    rules=set()
    for e in funV: rules|=fund_rules(e['marca_prova'])
    cons0 = bool(rules & FUND_OK0)
    old_cls = bool(row['font_classificacio_cita'].strip())
    res.append(dict(isin=row['isin'],any=row['any'],lab=lab,cert=row['sim_estat_certificacio'],regles=row['regles'],
        ceo=len(ceo)>0, ceoV=len(ceoV)>0, ceoVname=len(ceoVname)>0, ceocap=len(ceocap)>0,
        fun=len(fun)>0, funV=len(funV)>0, funVcap=len(funVcap)>0, cons0=cons0, old_cls=old_cls,
        verif_doc=row['verificacio_documental'], v75=row['v75_marca'], v75_cita=row['v75_cita_trobada']))
json.dump(res,open(sys.argv[1],'w'))
print('orphan registry year-refs (ISIN-any not in panel):',sum(orphan.values()),dict(orphan))
def pct(n,d): return f'{n} ({100*n/d:.1f}%)' if d else '0'
labs=['1','0','NA_sense_ceo','no_determinat']
print('\n=== Cobertura per etiqueta ===')
for L in labs+['TOTAL']:
    S=[x for x in res if L=='TOTAL' or x['lab']==L]; n=len(S)
    print(f"{L}: n={n} | ceo_any={pct(sum(x['ceo'] for x in S),n)} ceoV={pct(sum(x['ceoV'] for x in S),n)} ceoV+nom={pct(sum(x['ceoVname'] for x in S),n)} ceo_captura={pct(sum(x['ceocap'] for x in S),n)}")
    print(f"     fund_any={pct(sum(x['fun'] for x in S),n)} fundV={pct(sum(x['funV'] for x in S),n)} fund_captura={pct(sum(x['funVcap'] for x in S),n)} classif_antiga(col)={pct(sum(x['old_cls'] for x in S),n)} fundV_o_antiga={pct(sum(x['funV'] or x['old_cls'] for x in S),n)}")
print('\n=== Cobertura per estat certificacio ===')
for C in ['certificada','certificada_ceo_pendent','no_certificada','fora_mostra_auditoria']:
    S=[x for x in res if x['cert']==C]; n=len(S)
    both=sum(x['ceoVname'] and (x['funV'] or x['old_cls']) for x in S)
    print(f"{C}: n={n} ceoV+nom={pct(sum(x['ceoVname'] for x in S),n)} fundV={pct(sum(x['funV'] for x in S),n)} antiga={pct(sum(x['old_cls'] for x in S),n)} totes_dues(ceoV+nom & (fundV|antiga))={pct(both,n)} captura_ambdues={pct(sum(x['ceocap'] and x['funVcap'] for x in S),n)}")
print('\n=== Files completes (estricte) ===')
S=[x for x in res if x['lab'] in ('0','1')]; n=len(S)
comp=sum(x['ceoVname'] and (x['funV'] or x['old_cls']) for x in S)
comp_reg=sum(x['ceoVname'] and x['funV'] for x in S)
cap=sum(x['ceocap'] and x['funVcap'] for x in S)
print('F+P n=',n,'CEO[V]+nom i classificacio (registre o antiga)=',pct(comp,n),'| nomes registre=',pct(comp_reg,n),'| verificades a captura Wayback (les dues)=',pct(cap,n))
print('Zero evidencia estructurada (ni CEO ni classif):',pct(sum(not x['ceo'] and not x['fun'] and not x['old_cls'] for x in res),len(res)))
# P rows: founder entries V but no a-e rule tag
S0=[x for x in res if x['lab']=='0' and x['funV']]
print('P amb fundV pero cap marca a-e a marca_prova:',sum(not x['cons0'] for x in S0),'de',len(S0))
print('\n=== P per regla principal (regles) ===')
c=collections.Counter(x['regles'] for x in res if x['lab']=='0')
for k,v in c.most_common(8):
    S=[x for x in res if x['lab']=='0' and x['regles']==k]
    print(f"  {k}: {v} | fundV={sum(x['funV'] for x in S)} antiga={sum(x['old_cls'] for x in S)} cap={sum(not x['funV'] and not x['old_cls'] for x in S)}")
# by company
byi=collections.defaultdict(list)
for x in res: byi[x['isin']].append(x)
full=sum(all(x['ceoVname'] and (x['funV'] or x['old_cls']) for x in v if x['lab'] in('0','1')) for v in byi.values())
print('\nISIN amb totes les files F/P completes (estricte):',full,'de',len(byi))

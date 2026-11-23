import csv, random, re, subprocess, json, os, sys, unicodedata, hashlib, html
import os
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
SP=sys.argv[1]; DOCS=os.path.join(SP,'mostra_docs')
r=list(csv.DictReader(open(f'{ROOT}/docs/REGISTRE_CANVIS.csv',encoding='utf-8')))
pool=[e for e in r if e['funcio_cita'] in('ceo','fundador') and e['marca_veritat']=='[V]' and e['cita_literal'].strip() and e['url_font'].startswith('http') and 'no_valida' not in e['notes'] and 'web.archive.org' not in e['url_font']]
random.seed(20261123)
strata={}
for e in pool: strata.setdefault(e['origen'],[]).append(e)
sample=[]
for o,es in sorted(strata.items()):
    k=min(len(es), 9 if len(es)>200 else 5)
    sample+=random.sample(es,k)
def norm(s):
    s=html.unescape(s)
    s=unicodedata.normalize('NFKC',s)
    s=s.replace('­','')
    s=re.sub(r'[‘’‚‛′`´]',"'",s); s=re.sub(r'[“”„«»]','"',s)
    s=re.sub(r'[‐-―−]','-',s)
    s=re.sub(r'-\s*\n\s*','',s)
    s=re.sub(r'\s+',' ',s).lower()
    return s
def words(s): return re.findall(r'\w+',norm(s))
out=[]
for i,e in enumerate(sample):
    url=e['url_font'].strip(); fn=os.path.join(DOCS,f'd{i:03d}')
    rec=dict(i=i,origen=e['origen'],isin=e['isin'],anys=e['anys'],funcio=e['funcio_cita'],id=e['id_document_o_font'],url=url,cita=e['cita_literal'][:300])
    try:
        p=subprocess.run(['curl','-sSL','--max-time','60','--max-filesize','60000000','-A','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36','-o',fn,'-w','%{http_code} %{content_type} %{size_download}',url],capture_output=True,text=True,timeout=90)
        rec['http']=p.stdout.strip(); rec['err']=p.stderr.strip()[-150:]
    except Exception as ex:
        rec['http']='timeout'; rec['err']=str(ex)[:100]
    text=''
    if os.path.exists(fn) and os.path.getsize(fn)>0:
        head=open(fn,'rb').read(5)
        if head.startswith(b'%PDF'):
            t=subprocess.run(['pdftotext','-q',fn,'-'],capture_output=True,timeout=120); text=t.stdout.decode('utf-8','ignore')
            rec['tipus']='pdf'
        else:
            raw=open(fn,'rb').read().decode('utf-8','ignore')
            raw=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>',' ',raw)
            text=re.sub(r'<[^>]+>',' ',raw); rec['tipus']='html'
    rec['len_text']=len(text)
    nt=norm(text); nc=norm(e['cita_literal'])
    rec['exacta']= nc[:250] in nt if nc else False
    if not rec['exacta'] and nt:
        cw=words(e['cita_literal']); tw=set(words(text))
        rec['frac_paraules']=round(sum(w in tw for w in cw)/max(1,len(cw)),2)
        # longest run check: 8-word windows
        ntw=' '.join(words(text)); hits=0; wins=0
        for j in range(0,max(1,len(cw)-7),4):
            wins+=1; hits+= (' '.join(cw[j:j+8]) in ntw)
        rec['finestres8']=f'{hits}/{wins}'
    out.append(rec)
    print(json.dumps(rec,ensure_ascii=False)[:400],flush=True)
json.dump(out,open(os.path.join(SP,'mostra_resultat.json'),'w'),ensure_ascii=False,indent=1)

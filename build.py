#!/usr/bin/env python3
"""Genera il sito statico in docs/ da data/articles.json."""
import json, html, os, shutil
M=["gennaio","febbraio","marzo","aprile","maggio","giugno","luglio","agosto","settembre","ottobre","novembre","dicembre"]
def d(s): y,m,g=s.split("-"); return f"{int(g)} {M[int(m)-1]} {y}"
e=html.escape
A=sorted(json.load(open("data/articles.json")),key=lambda a:a["date"],reverse=True)
SEC=[("cachyos","CachyOS"),("linux","Linux &amp; Sicurezza")]
CSS="""*{box-sizing:border-box}body{margin:0;background:#000;color:#ddd;font:17px/1.6 Georgia,serif}
a{color:inherit;text-decoration:none}header{border-bottom:3px solid #1fd1a0;padding:18px 24px;background:#050505}
.logo{font:800 32px/1 Arial,sans-serif;color:#fff;letter-spacing:-1px}.logo span{color:#1fd1a0}
.tagline{color:#888;font:13px Arial,sans-serif;margin-top:6px}nav{font:600 14px Arial,sans-serif;margin-top:12px}
nav a{margin-right:18px;color:#bbb;text-transform:uppercase}nav a:hover{color:#1fd1a0}
main{max-width:1150px;margin:auto;padding:24px}h2.sec{font:800 22px Arial,sans-serif;color:#fff;border-left:5px solid #1fd1a0;padding-left:10px;text-transform:uppercase}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px;margin-bottom:40px}
.card{background:#0d0d0d;border:1px solid #222;padding:18px;border-radius:4px;transition:.2s}.card:hover{border-color:#1fd1a0}
.card.lead{grid-column:1/-1;padding:28px}.card.lead h3{font-size:30px}
.card h3{color:#fff;margin:6px 0 8px;font:700 21px/1.25 Arial,sans-serif}.meta{font:12px Arial,sans-serif;color:#888;text-transform:uppercase}
.tag{background:#1fd1a0;color:#000;padding:2px 7px;font-weight:700;margin-right:8px;border-radius:2px}.tag.Sicurezza,.tag.Malware,.tag.Vulnerabilità,.tag.Allerta{background:#e0303b;color:#fff}
article{max-width:760px;margin:auto}article h1{color:#fff;font:800 36px/1.2 Arial,sans-serif}.lede{font-size:20px;color:#aaa;font-style:italic}
.src{margin-top:40px;border-top:1px solid #333;padding-top:12px;font:13px Arial,sans-serif;color:#777}
footer{text-align:center;color:#555;font:12px Arial,sans-serif;padding:30px;border-top:1px solid #222}"""
def page(t,body,root=""):
    return f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{t}</title><link rel="stylesheet" href="{root}style.css"></head><body>
<header><a href="{root}index.html"><div class="logo">Cachy<span>Sec</span> News</div></a><div class="tagline">Sicurezza, vulnerabilità e malware su CachyOS e Linux — notizie dal mondo riscritte in italiano</div>
<nav><a href="{root}index.html">Home</a><a href="{root}index.html#cachyos">CachyOS</a><a href="{root}index.html#linux">Linux</a></nav></header><main>{body}</main>
<footer>Aggiornato automaticamente ogni 24 ore solo in presenza di novità · Articoli riassunti e rielaborati in italiano · Fonti citate in calce</footer></body></html>"""
def card(a,lead=False):
    return f"""<a class="card{' lead' if lead else ''}" href="articoli/{a['id']}.html"><div class="meta"><span class="tag {a['tag']}">{e(a['tag'])}</span>{d(a['date'])}</div><h3>{e(a['title'])}</h3><p>{e(a['summary'])}</p></a>"""
shutil.rmtree("docs",ignore_errors=True); os.makedirs("docs/articoli")
open("docs/style.css","w").write(CSS); open("docs/.nojekyll","w").close()
b=""
for k,n in SEC:
    L=[a for a in A if a["section"]==k]
    b+=f'<h2 class="sec" id="{k}">{n}</h2><div class="grid">'+"".join(card(a,i==0) for i,a in enumerate(L))+"</div>"
open("docs/index.html","w").write(page("CachySec News – Sicurezza CachyOS e Linux",b))
for a in A:
    p="".join(f"<p>{e(x)}</p>" for x in a["body"])
    open(f"docs/articoli/{a['id']}.html","w").write(page(e(a["title"]),f"""<article><div class="meta"><span class="tag {a['tag']}">{e(a['tag'])}</span>{dict(SEC)[a['section']]} · {d(a['date'])}</div><h1>{e(a['title'])}</h1><p class="lede">{e(a['summary'])}</p>{p}<div class="src">Fonte: {e(a['source'])} · Data originale: {d(a['date'])}<br>Articolo riassunto e riscritto in italiano dalla redazione.</div></article>""","../"))
print(len(A),"articoli")

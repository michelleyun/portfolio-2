#!/usr/bin/env python3
"""Builds the static site from content.py and visuals.py. Run: python3 build.py <out_dir>"""
import sys, os
from html import escape as e
from PIL import Image
from content import *
from visuals import SOLUTIONS

OUT = sys.argv[1] if len(sys.argv) > 1 else '../site'


def head(title, desc, P, path):
    full = 'Michelle Yun' if title == 'Michelle Yun' else f'{title} · Michelle Yun'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:title" content="{e(full)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE}og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Michelle Yun, written in characters">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#fafaf8">
<link rel="icon" href="{P}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&amp;family=Geist+Mono:wght@400&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{P}assets/css/site.css">
</head>
'''


def top(P, cur):
    sw = lambda href, lab, key: f'<a href="{P}{href}"{" aria-current=\"page\"" if cur == key else ""}>{lab}</a>'
    return f'''<div class="top">
  <a class="brand" href="{P}index.html">Michelle Yun</a>
  <nav class="switch" aria-label="Work or photography">{sw("index.html", "Work", "work")}{sw("photography.html", "Photography", "photo")}</nav>
  <button class="pill menu-btn" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
</div>
<nav class="menu" id="menu" aria-label="Site">
  <a href="{P}index.html">Work</a><a href="{P}photography.html">Photography</a><a href="{P}about.html#about">About</a><a href="{P}about.html#toolkit">Toolkit</a><a href="{P}about.html#contact">Contact</a>
</nav>'''


def mswitch(P, cur):
    sw = lambda href, lab, key: f'<a href="{P}{href}"{" aria-current=\"page\"" if cur == key else ""}>{lab}</a>'
    return f'<nav class="switch m-switch" aria-label="Work or photography, phone">{sw("index.html", "Work", "work")}{sw("photography.html", "Photography", "photo")}</nav>'


def side_foot(P):
    return f'''<div class="side-foot">
  <nav class="links" aria-label="More"><a class="pill" href="{P}about.html#about">About</a><a class="pill" href="{P}about.html#toolkit">Toolkit</a><a class="pill" href="{P}about.html#contact">Contact</a></nav>
  <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
  <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a>
</div>'''


def foot(P):
    return f'''<footer class="foot">
  <div class="kj" aria-hidden="true"><img src="{P}assets/kj/kj-footer.webp" alt="" width="670" height="531" loading="lazy"></div>
  <div class="foot-row"><span>© 2026 Michelle Yun</span><a href="#top">Back to top ↑</a></div>
</footer>'''


def page(name, html):
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(html)


def cvars(i):
    k = f'{i + 1:02d}'
    return f'--c:var(--c{k});--t:var(--t{k});--d:var(--d{k})'


def end(P):
    return f'<script src="{P}assets/js/site.js" defer></script>\n</body>\n</html>\n'


# ---------- Home ----------
def home():
    P = ''
    rows = ''.join(
        f'''<li><a href="{c["slug"]}.html" data-i="{i}" data-n="{c["n"]}" data-tag="{e(c["tag"])}" data-title="{e(c["title"])}" data-line="{e(c["line"])}" style="{cvars(i)}">
<span class="n">{c["n"]}</span><span><span class="t">{e(c["title"])}</span><span class="s">{e(c["tag"])}</span><span class="tag">{e(c["tag"])}</span></span><span class="dot"></span></a></li>'''
        for i, c in enumerate(CASES))
    html = head('Michelle Yun', LINE, P, '') + f'''<body class="home" id="top">
<script>(function(){{var h=location.hash.slice(1),m={{about:'about.html#about',toolkit:'about.html#toolkit',contact:'about.html#contact',background:'about.html#background',photography:'photography.html'}};if(/^case-0[1-6]$/.test(h))location.replace(h+'.html');else if(m[h])location.replace(m[h]);}})();</script>
<div class="intro" id="intro" aria-hidden="true">
  <div class="r"><b>Michelle Yun</b><button class="pill" type="button" id="intro-skip">Skip intro</button></div>
  <img src="assets/kj/kj-intro.gif" alt="" width="724" height="724">
  <div class="r"><span>Portfolio</span><span class="mono" id="intro-n">000</span></div>
</div>
<a class="skip" href="#work">Skip to selected work</a>
<div class="shell">
<aside class="side">
{top(P, "work")}
{mswitch(P, "work")}
<div class="who">
  <img src="assets/portrait/michelle-yun.jpg" alt="Michelle Yun in a black blazer" width="300" height="452">
  <div><p>Solutions Engineer<br><span class="mute">Chicago, Illinois</span></p><span class="clock"><i></i><span data-clock>Chicago</span></span></div>
</div>
<p class="lead">{LINE}</p>
<div class="mpanel" aria-hidden="true"><canvas class="art"></canvas></div>
<section id="work" aria-labelledby="work-h">
  <div class="list-label"><h2 id="work-h" style="font-size:15px;letter-spacing:0">Selected work</h2><span class="mono mute">06</span></div>
  <p class="mute" style="font-size:14px;margin-bottom:12px"><span class="dk">Hover to preview, click to read the full case study.</span><span class="mb">Tap a project to read the full case study.</span></p>
  <ol class="rows">{rows}</ol>
</section>
{side_foot(P)}
</aside>
<main class="main">
  <div class="meta-line" id="meta"><span>Michelle Yun · Portfolio</span><span>6 selected case studies</span></div>
  <div class="pane" id="pane"><h1 class="sr">Michelle Yun</h1><canvas class="art" aria-hidden="true"></canvas></div>
  <div class="pane-cap fade" id="cap">
    <div><span class="tag" id="cap-tag" hidden></span><h2 id="cap-title" style="margin-top:10px">6 selected case studies</h2><p id="cap-line">Hover to preview, click to read the full case study.</p></div>
    <a class="pill solid" id="cap-link" href="{CASES[0]["slug"]}.html">Start with 01 →</a>
  </div>
  {foot(P)}
</main>
</div>
''' + end(P)
    page('index.html', html)


# ---------- Photography ----------
def photography():
    P = ''
    items, stack = '', ''
    for i, (f, name, place, lens, alt) in enumerate(PHOTOS):
        w, h = Image.open(os.path.join(OUT, 'assets/photos', f)).size
        src = f'assets/photos/{f}'
        items += (f'<li><a href="{src}" data-i="{i}" data-src="{src}" data-ratio="{w} / {h}" data-name="{e(name)}" data-place="{e(place)}" data-lens="{lens}" data-alt="{e(alt)}"{" aria-current=\"true\"" if i == 0 else ""}>'
                  f'<span class="n">{i + 1:02d}</span><span><span class="t">{e(name)}</span><span class="s">{e(place)}</span></span><span class="mono mute">{lens}</span></a></li>')
        stack += (f'<figure><div class="frame" tabindex="0" role="button" aria-label="Show {e(name)} in color" style="aspect-ratio:{w} / {h}"><canvas aria-hidden="true"></canvas>'
                  f'<img src="{src}" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy"></div>'
                  f'<figcaption><b>{e(name)}</b> <span class="mute">· {e(place)} · {lens}</span></figcaption></figure>')
    w0, h0 = Image.open(os.path.join(OUT, 'assets/photos', PHOTOS[0][0])).size
    html = head('Photography', 'Portraits of some very good dogs, by Michelle Yun.', P, 'photography.html') + f'''<body class="photo" id="top">
<div class="shell">
<aside class="side">
{top(P, "photo")}
{mswitch(P, "photo")}
<div>
  <h1 class="lead">Portraits of some very good dogs.</h1>
  <p class="mute" style="margin-top:12px"><span class="dk">Hover to bring them out in color.</span><span class="mb">Tap to bring them out in color.</span></p>
</div>
<ol class="rows plist" style="--c:var(--c01)">{items}</ol>
{side_foot(P)}
</aside>
<main class="main">
  <div class="meta-line"><span id="ph-n">01 / 10</span><span id="ph-where">{e(PHOTOS[0][2])} · {PHOTOS[0][3]}</span></div>
  <div class="stage" id="stage">
    <div class="frame" tabindex="0" role="button" aria-label="Show in color" style="aspect-ratio:{w0} / {h0}"><canvas aria-hidden="true"></canvas><img src="assets/photos/{PHOTOS[0][0]}" alt="{e(PHOTOS[0][4])}"></div>
  </div>
  <div class="ph-cap">
    <h2 id="ph-name" style="font-size:40px;letter-spacing:-.035em">{e(PHOTOS[0][1])}</h2>
    <p class="mute" id="ph-desc">{e(PHOTOS[0][4])}</p>
    <div class="nav"><button class="pill round" type="button" id="ph-prev" aria-label="Previous photo">←</button><button class="pill round" type="button" id="ph-next" aria-label="Next photo">→</button></div>
  </div>
  <div class="stack">{stack}</div>
  {foot(P)}
</main>
</div>
''' + end(P)
    page('photography.html', html)


# ---------- About ----------
def about():
    P = ''
    groups = ''
    for g, ents in BACKGROUND:
        es = ''
        for org, role, dates, now, link in ents:
            r = f'<span class="r">{e(role)}</span>' if role else ''
            l = f'<a class="pill" href="{link[1]}">{e(link[0])}</a>' if link else '<span></span>'
            es += f'<div class="ent"><span><b>{e(org)}</b>{r}</span><span class="d{" now" if now else ""}">{e(dates)}</span>{l}</div>'
        groups += f'<div class="grp"><span class="mono">{e(g)}</span><div class="ents">{es}</div></div>'
    kits = ''
    for name, items in TOOLKIT:
        lis = ''
        for t, c in items:
            if c:
                slug = next(x['slug'] for x in CASES if x['n'] == c)
                lis += f'<li><a href="{slug}.html"><span>{e(t)}</span><small>↗{c}</small></a></li>'
            else:
                lis += f'<li><span>{e(t)}</span></li>'
        kits += f'<div><h3>{e(name)}</h3><ul>{lis}</ul></div>'
    paras = ''.join(f'<p>{e(p)}</p>' for p in ABOUT)
    nav = ''.join(f'<a href="#{i}">{l}</a>' for i, l in [('about', 'About'), ('background', 'Background'), ('toolkit', 'Toolkit'), ('contact', 'Contact')])
    html = head('About', ABOUT_LEAD, P, 'about.html') + f'''<body class="about-page" id="top">
<div class="shell">
<aside class="side about-side">
{top(P, "")}
<p class="lead">{LINE}</p>
<nav class="side-nav" aria-label="On this page">{nav}</nav>
{side_foot(P)}
</aside>
<main class="main">
<div class="page">
  <section id="about" class="csec" style="margin-top:0">
    <div class="band"><canvas class="art" data-band="-1" aria-hidden="true"></canvas></div>
    <div class="about">
      <figure style="margin:0"><img src="assets/portrait/about.jpg" alt="Michelle Yun" width="672" height="720"></figure>
      <div><h1 class="mono mute" style="font-weight:400">About</h1><p class="big">{e(ABOUT_LEAD)}</p><div class="cols">{paras}</div></div>
    </div>
  </section>
  <section id="background" class="csec" style="margin-top:0">
    <div class="sec-h"><h2>Background</h2></div>
    {groups}
  </section>
  <section id="toolkit" class="csec" style="margin-top:0">
    <div class="sec-h"><h2>Toolkit</h2><span class="mute" style="font-size:14px">↗ See the skill in practice in a case study.</span></div>
    <div class="kit">{kits}</div>
  </section>
  <section id="contact" class="csec contact" style="margin-top:0">
    <h2 class="sr">Contact</h2>
    <p class="q">Questions about my work, or just want to talk shop?</p>
    <div class="m"><a href="mailto:{EMAIL}">{EMAIL}</a><button class="pill" type="button" data-copy="{EMAIL}">Copy</button></div>
    <p class="sub"><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a> · Chicago, Illinois</p>
  </section>
</div>
{foot(P)}
</main>
</div>
''' + end(P)
    page('about.html', html)


# ---------- Case studies ----------
def cases():
    P = ''
    for i, c in enumerate(CASES):
        prv, nxt = CASES[i - 1], CASES[(i + 1) % 6]
        nav = ''.join(f'<a href="#{k.lower()}">{k}</a>' for k in ['Context', 'Approach', 'Solution', 'Impact'])
        imp = ''.join(f'<div><small>{k + 1:02d}</small><b>{e(t)}</b><p>{e(d)}</p></div>' for k, (t, d) in enumerate(c['impact']))
        html = head(c['title'], c['line'], P, f'{c["slug"]}.html') + f'''<body class="case-page" id="top" style="{cvars(i)}">
<div class="shell">
<aside class="side case-side">
{top(P, "work")}
<a class="pill" href="{P}index.html#work" style="align-self:flex-start">← Back to all work</a>
<nav class="side-nav" aria-label="Case study sections">{nav}</nav>
<div class="case-nav">
  <a class="pill round" href="{prv["slug"]}.html" aria-label="Previous case study: {e(prv["title"])}">←</a>
  <a class="pill round" href="{nxt["slug"]}.html" aria-label="Next case study: {e(nxt["title"])}">→</a>
  <span class="mono mute" style="margin-left:6px">{c["n"]} / 06</span>
</div>
{side_foot(P)}
</aside>
<main class="main">
<article class="case">
  <div class="band"><canvas class="art" data-band="{i}" aria-hidden="true"></canvas></div>
  <header class="case-h">
    <div class="k"><span class="mono mute">{c["n"]}</span><span class="tag">{e(c["tag"])}</span></div>
    <h1>{e(c["title"])}</h1>
    <div class="facts"><div><small>Company</small>{e(c["company"])}</div><div><small>Role</small>{e(c["role"])}</div><div><small>Deliverable</small>{e(c["deliverable"])}</div></div>
  </header>
  <div class="summary"><div><b>Challenge</b><p>{e(c["challenge"])}</p></div><div><b>What I did</b><p>{e(c["did"])}</p></div><div><b>Outcome</b><p>{e(c["outcome"])}</p></div></div>
  <div class="prose">
    <section class="csec" id="context"><h2>Context</h2><p>{e(c["context"])}</p></section>
    <section class="csec" id="approach"><h2>Approach</h2><p>{e(c["approach"])}</p></section>
    <section class="csec" id="solution"><h2>Solution</h2>{SOLUTIONS[i]()}</section>
  </div>
  <section class="csec" id="impact"><h2>Impact</h2><div class="impact">{imp}</div></section>
  <a class="next" href="{nxt["slug"]}.html"><span><small>Next · {nxt["n"]}</small><b>{e(nxt["title"])}</b></span><span class="pill solid">Read →</span></a>
</article>
{foot(P)}
</main>
</div>
''' + end(P)
        page(f'{c["slug"]}.html', html)


if __name__ == '__main__':
    home(); photography(); about(); cases()
    print('built', OUT)

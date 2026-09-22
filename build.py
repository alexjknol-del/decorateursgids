# -*- coding: utf-8 -*-
"""Generator voor decorateursgids.be. Geen dependencies. Bouwt dist/."""
import os, shutil, html, datetime
from content import SITE, THEMES, OVER

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
TODAY = datetime.date.today().isoformat()

CSS = r"""
:root{--paper:#f6f1e8;--paper2:#efe7d9;--ink:#2b2520;--muted:#6f655b;--line:#d9cdbb;--acc:#b5532c;--acc2:#8a3d1f;--sage:#6e7d5f}
@media (prefers-color-scheme:dark){:root{--paper:#1d1a17;--paper2:#26221e;--ink:#eee6da;--muted:#a79c8e;--line:#3d362f;--acc:#e07a4d;--acc2:#f0a07a;--sage:#9aab8a}}
*{box-sizing:border-box}
html{background:var(--paper);color:var(--ink);font:17px/1.65 Georgia,"Iowan Old Style",Palatino,"Times New Roman",serif;-webkit-text-size-adjust:100%}
body{margin:0}
a{color:var(--acc2);text-decoration-thickness:1px;text-underline-offset:3px}
a:hover{color:var(--acc)}
img{max-width:100%}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
header.top{border-bottom:3px double var(--line);padding:22px 0 18px}
header.top .wrap{display:flex;align-items:baseline;justify-content:space-between;flex-wrap:wrap;gap:10px 28px}
.brand{font-size:26px;letter-spacing:.02em;text-decoration:none;color:var(--ink);font-weight:400}
.brand b{color:var(--acc);font-weight:400;font-style:italic}
.brand small{display:block;font:italic 13px/1.3 Georgia,serif;color:var(--muted);margin-top:2px}
nav.main{display:flex;gap:22px;flex-wrap:wrap;font-family:"Helvetica Neue",Arial,sans-serif;font-size:13px;letter-spacing:.14em;text-transform:uppercase}
nav.main a{color:var(--ink);text-decoration:none;padding-bottom:4px;border-bottom:2px solid transparent}
nav.main a:hover,nav.main a.on{border-color:var(--acc);color:var(--acc2)}
.hero{padding:64px 0 40px;display:grid;grid-template-columns:1.2fr .8fr;gap:48px;align-items:end}
.hero h1{font-size:clamp(34px,5vw,58px);line-height:1.05;font-weight:400;margin:0 0 20px;letter-spacing:-.01em}
.hero h1 em{color:var(--acc);font-style:italic}
.hero p{font-size:19px;margin:0;max-width:34em;color:var(--muted)}
.swatches{display:grid;grid-template-columns:repeat(5,1fr);gap:8px}
.swatches span{display:block;aspect-ratio:1/1.35;border-radius:2px 2px 14px 2px}
.kicker{font-family:"Helvetica Neue",Arial,sans-serif;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--acc);margin:0 0 10px}
.themes{margin:36px 0 64px}
.themes h2{font-weight:400;font-size:30px;margin:0 0 6px}
.themes p.lead{color:var(--muted);margin:0 0 30px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px}
.card{background:var(--paper2);border:1px solid var(--line);border-radius:3px 3px 26px 3px;padding:26px 26px 22px;text-decoration:none;color:var(--ink);display:flex;flex-direction:column;gap:12px;min-height:220px;position:relative;transition:transform .15s}
.card:hover{transform:translateY(-3px);border-color:var(--acc)}
.card .nr{font-family:"Helvetica Neue",Arial,sans-serif;font-size:12px;letter-spacing:.18em;color:var(--acc)}
.card h3{margin:0;font-weight:400;font-size:24px;line-height:1.2}
.card p{margin:0;color:var(--muted);font-size:15.5px;flex:1}
.card .go{font-family:"Helvetica Neue",Arial,sans-serif;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--acc2)}
.card i.chip{position:absolute;right:22px;top:22px;width:18px;height:18px;border-radius:50%}
.strip{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:34px 0;margin:0 0 64px;display:grid;grid-template-columns:repeat(3,1fr);gap:32px}
.strip h4{margin:0 0 8px;font-weight:400;font-size:20px}
.strip p{margin:0;color:var(--muted);font-size:15.5px}
article.post{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:56px;padding:48px 0 64px}
article.post .body{max-width:40em}
.crumbs{font-family:"Helvetica Neue",Arial,sans-serif;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:0 0 22px}
.crumbs a{color:var(--muted);text-decoration:none}
.crumbs a:hover{color:var(--acc)}
h1.title{font-size:clamp(32px,4.4vw,48px);line-height:1.08;font-weight:400;margin:0 0 22px;letter-spacing:-.01em}
p.intro{font-size:20px;line-height:1.55;color:var(--muted);margin:0 0 30px;border-left:3px solid var(--acc);padding-left:18px}
.body h2{font-weight:400;font-size:27px;margin:38px 0 12px;line-height:1.2}
.body p{margin:0 0 16px}
.body p:first-of-type{}
aside.side{position:sticky;top:24px;align-self:start;display:flex;flex-direction:column;gap:22px}
.box{background:var(--paper2);border:1px solid var(--line);border-radius:3px 3px 22px 3px;padding:22px 22px 18px}
.box h3{margin:0 0 12px;font-weight:400;font-size:13px;letter-spacing:.16em;text-transform:uppercase;font-family:"Helvetica Neue",Arial,sans-serif;color:var(--acc)}
.box ul{margin:0;padding:0 0 0 18px;font-size:15.5px}
.box li{margin:0 0 9px}
.box p{margin:0 0 8px;font-size:15.5px}
.box a.btn{display:inline-block;margin-top:6px;font-family:"Helvetica Neue",Arial,sans-serif;font-size:13px;letter-spacing:.04em;word-break:break-all;text-decoration:none;border:1px solid var(--acc);color:var(--acc2);padding:9px 14px;border-radius:2px}
.box a.btn:hover{background:var(--acc);color:#fff}
.box.toc ol{margin:0;padding:0 0 0 20px;font-size:15px}
.box.toc li{margin:0 0 6px}
.box.toc a{text-decoration:none;color:var(--ink)}
.box.toc a:hover{color:var(--acc)}
.prevnext{border-top:1px solid var(--line);margin-top:40px;padding-top:22px;display:flex;justify-content:space-between;gap:20px;font-size:15.5px}
.prevnext a{text-decoration:none}
.prevnext span{display:block;font-family:"Helvetica Neue",Arial,sans-serif;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin-bottom:4px}
.page{max-width:40em;padding:48px 0 64px}
.page h1{font-size:clamp(32px,4.4vw,46px);font-weight:400;line-height:1.1;margin:0 0 24px}
.page h2{font-weight:400;font-size:25px;margin:34px 0 10px}
.page p,.page li{margin:0 0 16px}
footer.foot{border-top:3px double var(--line);padding:34px 0 44px;color:var(--muted);font-size:14.5px}
footer.foot .wrap{display:flex;justify-content:space-between;flex-wrap:wrap;gap:14px 30px}
footer.foot a{color:var(--muted);text-decoration:none;margin-right:18px}
footer.foot a:hover{color:var(--acc)}
@media (max-width:900px){.hero{grid-template-columns:1fr;gap:28px;padding:44px 0 28px}.swatches{grid-template-columns:repeat(10,1fr)}.swatches span{aspect-ratio:1/1}article.post{grid-template-columns:1fr;gap:34px}aside.side{position:static}.strip{grid-template-columns:1fr;gap:22px}}
@media (max-width:600px){html{font-size:16px}nav.main{gap:14px}.card{min-height:0}}
"""

SWATCH_COLORS = ["#b5532c","#d8a072","#e8d5b7","#6e7d5f","#3d4a3a","#8b6f4e","#c9b99a","#5b6b7a","#a4562f","#2b2520"]

def esc(s): return html.escape(s, quote=True)

def nav(active=""):
    items = [("/", "Home"), ("/gids/", "Thema's"), ("/over/", "Over"), ("/contact/", "Contact")]
    return "".join('<a href="%s"%s>%s</a>' % (h, ' class="on"' if h == active else "", t) for h, t in items)

def layout(title, meta, body, path, active="", extra_head=""):
    canonical = SITE["url"] + path
    return """<!DOCTYPE html>
<html lang="nl-BE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_BE">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>%s</style>
%s
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="/">Decorateurs<b>gids</b>.be<small>%s</small></a>
<nav class="main">%s</nav>
</div></header>
<main>%s</main>
<footer class="foot"><div class="wrap">
<div>&copy; %s Decorateursgids.be. Onafhankelijke gids over het afwerken en aankleden van een woning.</div>
<div><a href="/over/">Over</a><a href="/contact/">Contact</a><a href="/partners/">Partners</a><a href="/privacybeleid/">Privacybeleid</a><a href="/cookiebeleid/">Cookiebeleid</a><a href="/sitemap.xml">Sitemap</a></div>
</div></footer>
</body>
</html>""" % (esc(title), esc(meta), canonical, esc(title), esc(meta), canonical, CSS, extra_head,
              esc(SITE["tagline"]), nav(active), body, datetime.date.today().year)

def write(path, content):
    full = os.path.join(OUT, path.strip("/"), "index.html") if path != "/" else os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def ext(url, anchor):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (url, esc(anchor))

def linkify(text):
    """Vervang volledige URL's in lopende tekst door links met de URL als ankertekst."""
    import re
    def rep(m):
        u = m.group(0)
        return ext(u, u)
    return re.sub(r"https?://[^\s<>\"')]+(?<![.,])", rep, esc(text))

def theme_cards():
    out = []
    for i, t in enumerate(THEMES):
        out.append('<a class="card" href="/gids/%s/"><i class="chip" style="background:%s"></i><span class="nr">%s</span><h3>%s</h3><p>%s</p><span class="go">Lees het artikel</span></a>'
                   % (t["slug"], SWATCH_COLORS[i], t["nr"], esc(t["title"]), esc(t["meta"].split(". ")[0] + ".")))
    return "".join(out)

def home():
    sw = "".join('<span style="background:%s"></span>' % c for c in SWATCH_COLORS)
    body = """<div class="wrap">
<section class="hero">
<div><p class="kicker">Gids voor wie een ruimte afwerkt</p>
<h1>Van kale muur tot <em>bewoonde</em> kamer.</h1>
<p>Tien thema's over het werk van de decorateur: verf, vloeren, raamdecoratie, meubels, woonaccessoires en alles wat daarbij opgehangen en geplaatst wordt. Vuistregels uit de praktijk, zonder omhaal.</p></div>
<div class="swatches" aria-hidden="true">%s</div>
</section>
<section class="strip">
<div><h4>Eerst het grote vlak</h4><p>Vloer, muren en raamdecoratie bepalen negentig procent van de sfeer. Die keuzes komen eerst.</p></div>
<div><h4>Dan de lagen</h4><p>Meubels, verlichting, textiel en accessoires komen in die volgorde, van groot naar klein.</p></div>
<div><h4>Netjes opgehangen</h4><p>Elke laag hangt aan een schroef. Het juiste boortje en de juiste plug maken het verschil tussen strak en slordig.</p></div>
</section>
<section class="themes">
<p class="kicker">De tien thema's</p>
<h2>Waar deze gids over gaat</h2>
<p class="lead">Elk thema is een artikel met de vuistregels uit de praktijk, een samenvatting en een verwijzing naar een winkel of merk waar het materiaal te vinden is.</p>
<div class="grid">%s</div>
</section>
</div>""" % (sw, theme_cards())
    write("/", layout("Decorateursgids.be | Gids voor wie een ruimte afwerkt", SITE["description"], body, "/", "/"))

def gids_index():
    body = """<div class="wrap"><section class="themes" style="padding-top:48px">
<p class="crumbs"><a href="/">Home</a> / Thema's</p>
<h1 style="font-size:40px;font-weight:400;margin:0 0 6px">De tien thema's</h1>
<p class="lead">Van de vloer tot de laatste plant: alle onderdelen van het afwerken en aankleden van een woning, in de volgorde waarin een decorateur ze aanpakt.</p>
<div class="grid">%s</div></section></div>""" % theme_cards()
    write("/gids/", layout("Alle thema's | Decorateursgids.be", "Overzicht van de tien thema's op Decorateursgids.be: woonaccessoires, klokken, boren en ophangen, verf, raamdecoratie, vloeren, tegels, meubels, keuken en planten.", body, "/gids/", "/gids/"))

def slug_id(s):
    import re
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def theme_page(i, t):
    prev = THEMES[i - 1] if i > 0 else None
    nxt = THEMES[i + 1] if i < len(THEMES) - 1 else None
    secs = []
    toc = []
    for h, paras in t["sections"]:
        sid = slug_id(h)
        toc.append('<li><a href="#%s">%s</a></li>' % (sid, esc(h)))
        secs.append('<h2 id="%s">%s</h2>' % (sid, esc(h)) + "".join("<p>%s</p>" % linkify(p) for p in paras))
    p = t["partner"]
    pn = ""
    if prev or nxt:
        pn = '<div class="prevnext"><div>%s</div><div style="text-align:right">%s</div></div>' % (
            ('<a href="/gids/%s/"><span>Vorige</span>%s</a>' % (prev["slug"], esc(prev["title"]))) if prev else "",
            ('<a href="/gids/%s/"><span>Volgende</span>%s</a>' % (nxt["slug"], esc(nxt["title"]))) if nxt else "")
    body = """<div class="wrap"><article class="post">
<div class="body">
<p class="crumbs"><a href="/">Home</a> / <a href="/gids/">Thema's</a> / %s</p>
<p class="kicker">Thema %s</p>
<h1 class="title">%s</h1>
<p class="intro">%s</p>
%s
%s
</div>
<aside class="side">
<div class="box"><h3>In het kort</h3><ul>%s</ul></div>
<div class="box toc"><h3>In dit artikel</h3><ol>%s</ol></div>
<div class="box"><h3>Waar te vinden</h3><p><strong>%s</strong></p><p>%s</p>%s</div>
</aside>
</article></div>""" % (esc(t["title"]), t["nr"], esc(t["h1"]), esc(t["intro"]), "".join(secs), pn,
                       "".join("<li>%s</li>" % esc(k) for k in t["kort"]), "".join(toc),
                       esc(p["name"]), esc(p["blurb"]), ext(p["url"], p["anchor"]).replace('<a ', '<a class="btn" '))
    schema = """<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":%s,"description":%s,"inLanguage":"nl-BE","datePublished":"%s","mainEntityOfPage":"%s","publisher":{"@type":"Organization","name":"Decorateursgids.be","url":"%s"}}</script>""" % (
        _j(t["h1"]), _j(t["meta"]), "2026-09-06", SITE["url"] + "/gids/%s/" % t["slug"], SITE["url"])
    ttl = "%s | Decorateursgids.be" % t["h1"]
    if len(ttl) > 70: ttl = t["h1"]
    write("/gids/%s/" % t["slug"], layout(ttl, t["meta"], body, "/gids/%s/" % t["slug"], "/gids/", schema))

def _j(s):
    import json
    return json.dumps(s, ensure_ascii=False)

def simple(path, title, meta, h1, paragraphs_html, active=""):
    body = '<div class="wrap"><div class="page"><p class="crumbs"><a href="/">Home</a> / %s</p><h1>%s</h1>%s</div></div>' % (esc(h1), esc(h1), paragraphs_html)
    write(path, layout(title, meta, body, path, active))

def over():
    simple("/over/", OVER["title"] + " | Decorateursgids.be", OVER["meta"], OVER["title"],
           "".join("<p>%s</p>" % linkify(p) for p in OVER["paragraphs"]), "/over/")

def contact():
    ph = """<p>Decorateursgids.be is per e-mail bereikbaar op <a href="mailto:info@decorateursgids.be">info@decorateursgids.be</a>.</p>
<p>Dat adres is bedoeld voor vragen en opmerkingen over de inhoud van de gids, voor het melden van onjuistheden en voor voorstellen voor nieuwe thema's. Berichten worden gelezen en waar nodig beantwoord.</p>
<p>De gids verkoopt zelf niets en voert geen decoratiewerk uit. Vragen over een bestelling of een levering horen thuis bij de winkel of het merk waar die bestelling is geplaatst.</p>"""
    simple("/contact/", "Contact | Decorateursgids.be", "Contact opnemen met Decorateursgids.be kan per e-mail via info@decorateursgids.be.", "Contact", ph, "/contact/")

def privacy():
    ph = """<p>Decorateursgids.be verwerkt zo weinig mogelijk persoonsgegevens. Deze pagina beschrijft wat er wel en niet gebeurt.</p>
<h2>Bezoek aan de site</h2>
<p>De site bestaat uit statische pagina's. Er is geen accountsysteem, geen contactformulier en geen nieuwsbrief. Bij een bezoek worden geen persoonsgegevens verzameld door de site zelf. De hostingpartij die de pagina's aflevert, kan technische gegevens zoals IP-adres en tijdstip tijdelijk in logbestanden bewaren om de dienst te beveiligen en te laten werken.</p>
<h2>E-mail</h2>
<p>Wie een e-mail stuurt naar info@decorateursgids.be, deelt daarmee een e-mailadres en de inhoud van het bericht. Die gegevens worden alleen gebruikt om het bericht te beantwoorden en worden niet doorgegeven aan derden. Berichten worden verwijderd zodra ze niet meer nodig zijn.</p>
<h2>Links naar andere sites</h2>
<p>De gids verwijst naar winkels en merken. Op die sites geldt het privacybeleid van de betrokken partij. Decorateursgids.be heeft geen invloed op wat daar met gegevens gebeurt.</p>
<h2>Rechten</h2>
<p>Iedereen heeft het recht op inzage, verbetering en verwijdering van persoonsgegevens die Decorateursgids.be zou bewaren. Een verzoek daartoe kan naar info@decorateursgids.be. Wie meent dat gegevens onjuist verwerkt worden, kan een klacht indienen bij de Gegevensbeschermingsautoriteit, https://www.gegevensbeschermingsautoriteit.be/.</p>"""
    simple("/privacybeleid/", "Privacybeleid | Decorateursgids.be", "Hoe Decorateursgids.be omgaat met persoonsgegevens van bezoekers en van wie een e-mail stuurt.", "Privacybeleid", ph.replace("https://www.gegevensbeschermingsautoriteit.be/", ext("https://www.gegevensbeschermingsautoriteit.be/", "https://www.gegevensbeschermingsautoriteit.be/")))

def cookies():
    ph = """<p>Decorateursgids.be plaatst zelf geen cookies. Er draaien geen statistiekprogramma's, geen advertentiescripts en geen ingesloten inhoud van sociale media op deze site.</p>
<h2>Wat wel kan gebeuren</h2>
<p>De hostingpartij die de pagina's aflevert, kan een technisch noodzakelijke cookie plaatsen om de verbinding te beveiligen. Zo'n cookie bevat geen persoonsgegevens en wordt niet gebruikt om bezoekers te volgen.</p>
<h2>Links naar andere sites</h2>
<p>Wie doorklikt naar een winkel of merk, komt op een site met een eigen cookiebeleid. Daar kunnen wel cookies geplaatst worden. Decorateursgids.be heeft daar geen zeggenschap over.</p>
<h2>Cookies beheren</h2>
<p>Cookies zijn in elke browser te bekijken en te verwijderen via de instellingen onder privacy of sitegegevens.</p>"""
    simple("/cookiebeleid/", "Cookiebeleid | Decorateursgids.be", "Decorateursgids.be plaatst zelf geen cookies. Wat er wel kan gebeuren en hoe cookies beheerd worden.", "Cookiebeleid", ph)

PARTNERS = [
    ('Sleutelhangers.be', 'Sleutelhangers.be bedrukt sleutelhangers en vouwmeters met eigen logo.', 'https://www.sleutelhangers.be/vouwmeters-bedrukken', 'vouwmeter bedrukken'),
    ('Huissteden', 'Huissteden levert naaimachines, garen en toebehoren.', 'https://www.huissteden.nl/garen-vlies/naaigaren', 'naaimachine garen'),
    ('Het Schippertje', 'Het Schippertje verkoopt sierlijsten en ornamenten voor wand en plafond.', 'https://www.het-schippertje.nl/sierlijsten/', 'sierlijsten muur'),
    ('Aluwdoors', 'Aluwdoors maakt stalen binnendeuren in uiteenlopende afwerkingen.', 'https://www.aluwdoors.com/stalen-deuren/gouden-deuren/', 'een gouden deur'),
    ('Dakraam.nl', 'Dakraam.nl levert dakramen en bijbehorende raamdecoratie.', 'https://dakraam.nl/producten/raamdecoraties/', 'raamdecoraties'),
    ('De Bloemist', 'De Bloemist bezorgt bloemen en ballonnen aan huis.', 'https://debloemist.nl/ballon-bezorgen', 'Ballon versturen'),
    ('Bouwbeslag.nl', 'Bouwbeslag.nl levert deurbeslag, waaronder deurklinken in brons.', 'https://bouwbeslag.nl/deurklink/brons', 'deurbeslag brons'),
    ('Goedkope Slotenmaker', 'Goedkope Slotenmaker is een Nederlandse wegwijzer naar slotenmakers, geordend per provincie en gemeente.', 'https://www.goedkopeslotenmaker.nl/', 'goedkopeslotenmaker.nl'),
    ('ProductenHuren.nl', 'ProductenHuren.nl vergelijkt huuraanbod van huishoudelijke apparaten, waaronder koelkasten voor tijdelijk gebruik.', 'https://productenhuren.nl/koelkasten/', 'Koelkast huren'),
]

def partners():
    cards = "".join(
        '<div class="card"><h3>%s</h3><p>%s</p><span class="go">%s</span></div>' % (esc(n), esc(d), ext(u, a))
        for n, d, u, a in PARTNERS)
    body = ('<div class="wrap"><div class="page"><p class="crumbs"><a href="/">Home</a> / Partners</p>'
            '<h1>Partners en bronnen</h1>'
            '<p>Decorateursgids.be verwijst hier naar externe partners en bronnen.</p></div>'
            '<div class="grid" style="margin:0 0 64px">%s</div></div>' % cards)
    write("/partners/", layout("Partners en bronnen | Decorateursgids.be",
          "Externe partners en bronnen waar Decorateursgids.be naar verwijst.", body, "/partners/", "/partners/"))

def notfound():
    body = '<div class="wrap"><div class="page"><h1>Pagina niet gevonden</h1><p>Deze pagina bestaat niet of is verplaatst. Alle thema\'s staan op <a href="/gids/">de themapagina</a>.</p></div></div>'
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(layout("Pagina niet gevonden | Decorateursgids.be", "Deze pagina bestaat niet.", body, "/404.html"))

def sitemap():
    urls = ["/", "/gids/", "/over/", "/contact/", "/partners/", "/privacybeleid/", "/cookiebeleid/"] + ["/gids/%s/" % t["slug"] for t in THEMES]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        "<url><loc>%s%s</loc><lastmod>%s</lastmod></url>\n" % (SITE["url"], u, TODAY) for u in urls) + "</urlset>\n"
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % SITE["url"])
    with open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="4" fill="#f6f1e8"/><path d="M6 24 L6 8 L14 8 Q22 8 22 16 Q22 24 14 24 Z" fill="#b5532c"/><circle cx="26" cy="22" r="3" fill="#6e7d5f"/></svg>')
    with open(os.path.join(OUT, "_headers"), "w", encoding="utf-8") as f:
        f.write("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: DENY\n")

def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    home(); gids_index()
    for i, t in enumerate(THEMES):
        theme_page(i, t)
    over(); contact(); partners(); privacy(); cookies(); notfound(); sitemap()
    n = sum(len(f) for _, _, f in os.walk(OUT))
    print("gebouwd:", n, "bestanden in", OUT)

if __name__ == "__main__":
    main()

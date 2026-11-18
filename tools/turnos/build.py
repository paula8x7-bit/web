# Fabrica las páginas de trabajo a turnos a partir de la cabecera y el pie de la web.
# Uso: python3 tools/turnos/build.py  (desde la raíz del repositorio)
import json, re, html, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).parent))
from content import SRC, COMER, DORMIR, HUB  # noqa: E402
from content_en import SRC_EN, EAT_EN, SLEEP_EN
from content_viajes import SRC_VIAJES, JETLAG, JETLAG_EN  # noqa: E402

for extra in (SRC_EN, SRC_VIAJES):
    repes = SRC.keys() & extra.keys()
    assert not repes, f"Fuentes con el mismo nombre en dos ficheros: {repes}"
    SRC.update(extra)
# Página gemela en el otro idioma (para hreflang y el selector ES / EN)
COMER["alt"] = EAT_EN["path"]
DORMIR["alt"] = SLEEP_EN["path"]

# Textos fijos de la plantilla, por idioma
L = {
    "es": {"locale": "es_ES", "crumbs": "Migas de pan", "home": ("Inicio", "/"), "src": "Fuente", "src_h": "Fuentes",
           "faq_h": "Preguntas frecuentes", "by": "Por Paula Rubio, nutricionista integrativa · Noviembre de 2026",
           "cta_h": "¿Lo adaptamos a tu cuadrante?",
           "cta_p": "En consulta preparamos pautas para cada tipo de turno, con tu horario, tus síntomas y tus analíticas delante. Online, en castellano o en inglés.",
           "cta_b1": "Reserva tu cita", "cta_b2": ("Trabajo a turnos", "/turnos/"),
           "cta_note": '¿Eres TCP o piloto? Tienes una <a href="/tripulaciones/" style="color:#5e1a24;border-bottom:1px solid #c9b578">guía gratuita para tripulaciones de largo radio</a>.'},
    "en": {"locale": "en_GB", "crumbs": "Breadcrumb", "home": ("Home", "/en/"), "src": "Source", "src_h": "Sources",
           "faq_h": "Frequently asked questions", "by": "By Paula Rubio, integrative nutritionist · November 2026",
           "cta_h": "Shall we fit this around your rota?",
           "cta_p": "In my consultations we build guidelines for each type of shift, with your schedule, your symptoms and your blood tests in front of us. Online, in English or Spanish.",
           "cta_b1": "Book an appointment", "cta_b2": ("Email me", "mailto:hola@paularubionutricionista.com"),
           "cta_note": 'Cabin crew or pilot? There is a <a href="/en/cabin-crew/" style="color:#5e1a24;border-bottom:1px solid #c9b578">free guide for long haul crew</a>.'
                       '<br><br>Living in Spain? You can get your blood tests done at <a href="https://diagnoseum.com/?utm_source=web-night-shift-en&amp;utm_medium=referral" target="_blank" rel="noopener" data-umami-event="diagnoseum-night-shift-en" style="color:#5e1a24;border-bottom:1px solid #c9b578">Diagnoseum</a>: you choose exactly what you want to test, no doctor\'s referral needed, backed by Eurofins.'},
}

SITE = "https://paularubionutricionista.com"
NUTRIA = "https://nutriaplans.com/marketplace/paufly"
PUBLISHED = "2026-11-17"

glow = (ROOT / "planes/glow/index.html").read_text()
STYLE = re.search(r"<style>\s*\*\{box-sizing.*?</style>", glow, re.S).group(0)
EXTRA = """<style>
@media(max-width:900px){[data-cards]{grid-template-columns:1fr 1fr!important}[data-rules]{grid-template-columns:1fr!important}}
@media(max-width:640px){[data-cards]{grid-template-columns:1fr!important}}
details summary{cursor:pointer;list-style:none}
details summary::-webkit-details-marker{display:none}
details[open] summary span:last-child{transform:rotate(45deg)}
[data-body] a{color:#5e1a24;border-bottom:1px solid #c9b578}
[data-body] sup a{border:0;font-size:12px;padding-left:1px}
</style>"""
UMAMI = """<script>try{if(/[?&]soy-paula/.test(location.search))localStorage.setItem("umami.disabled","1")}catch(e){}</script>
<script defer src="https://cloud.umami.is/script.js" data-website-id="21a20c4a-cd36-44e3-bc6b-2af2bde813e7"></script>"""


def block(src, start, end):
    return src[src.index(start): src.index(end) + len(end)]


HEADER = block(glow, "<header", "</header>")
FOOTER = block(glow, "<footer", "</footer>")

# Cabecera y pie en inglés (los de la home EN), con anclas absolutas
en_home = (ROOT / "en/index.html").read_text()
EN_HEADER = block(en_home, "<header", "</header>")
EN_FOOTER = block(en_home, "<footer", "</footer>")
for frag in ("inicio", "sobre-mi", "servicios", "planes", "contacto"):
    EN_HEADER = EN_HEADER.replace(f'href="#{frag}"', f'href="/en/#{frag}"')
    EN_FOOTER = EN_FOOTER.replace(f'href="#{frag}"', f'href="/en/#{frag}"')


def chrome(t):
    """Cabecera y pie según el idioma, con el selector ES / EN apuntando a la página gemela."""
    alt = t.get("alt")
    if t.get("lang") == "en":
        h = EN_HEADER.replace('href="/"', f'href="{alt}"') if alt else EN_HEADER
        return h, EN_FOOTER
    h = HEADER.replace('href="/en/"', f'href="{alt}"') if alt else HEADER
    return h, FOOTER

F_JOST = "font-family:'Jost',sans-serif"
F_COR = "font-family:'Cormorant Garamond',serif"
F_EB = "font-family:'EB Garamond',serif"
BTN = (f"display:inline-flex;align-items:center;justify-content:center;background:#5e1a24;color:#f7f1e6;{F_JOST};"
       "font-size:13px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;padding:16px 32px;border-radius:2px;transition:background .25s")
BTN2 = (f"display:inline-flex;align-items:center;justify-content:center;background:transparent;color:#3c3b34;border:1px solid #b7a882;{F_JOST};"
        "font-size:13px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;padding:15px 31px;border-radius:2px;transition:all .25s")
EYEBROW = f"{F_JOST};font-size:13px;letter-spacing:.32em;text-transform:uppercase;color:#a98a4a"
H2 = f"{F_COR};font-weight:500;font-size:clamp(30px,3.4vw,44px);line-height:1.1;color:#3c3b34"
BODY = f"{F_JOST};font-weight:300;font-size:clamp(16px,1.25vw,18px);line-height:1.8;color:#4f4d43"
CARD = "background:#faf6ec;border:1px solid #e7dfc9;border-radius:5px;padding:24px 22px 26px;display:flex;flex-direction:column;gap:10px"
SEC_A = "background:#faf6ec;padding:clamp(54px,7vw,98px) clamp(22px,5vw,72px)"
SEC_B = "background:#f5efe2;padding:clamp(54px,7vw,98px) clamp(22px,5vw,72px)"


class Cites:
    """Convierte [clave] en superíndices numerados por orden de aparición."""

    def __init__(self, label="Fuente"):
        self.order = []
        self.label = label

    def __call__(self, text):
        def rep(m):
            k = m.group(1)
            if k not in SRC:
                return m.group(0)
            if k not in self.order:
                self.order.append(k)
            n = self.order.index(k) + 1
            return f'<sup><a href="#fuentes" aria-label="{self.label} {n}">{n}</a></sup>'
        return re.sub(r"\[([a-z]+)\]", rep, text)

    def plain(self, text):
        return re.sub(r"\[[a-z]+\]", "", re.sub(r"<[^>]+>", "", text))


def head(t, ld):
    url = SITE + t["path"]
    lang = t.get("lang", "es")
    alts = ""
    if t.get("alt"):
        es_url, en_url = (url, SITE + t["alt"]) if lang == "es" else (SITE + t["alt"], url)
        alts = (f'<link rel="alternate" hreflang="es" href="{es_url}">\n'
                f'<link rel="alternate" hreflang="en" href="{en_url}">\n'
                f'<link rel="alternate" hreflang="x-default" href="{es_url}">\n')
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t['title'])}</title>
<meta name="description" content="{html.escape(t['desc'])}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="canonical" href="{url}">
{alts}<meta property="og:type" content="{'article' if t is not HUB else 'website'}">
<meta property="og:site_name" content="Paula Rubio Nutricionista">
<meta property="og:locale" content="{L[lang]['locale']}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(t['title'])}">
<meta property="og:description" content="{html.escape(t['desc'])}">
<meta property="og:image" content="{SITE}/assets/hero.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
{STYLE}
{EXTRA}
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
</script>
{UMAMI}
</head>
<body>
"""


def person():
    return {"@type": "Person", "@id": SITE + "/#paula", "name": "Paula Rubio",
            "jobTitle": "Nutricionista integrativa y sobrecargo de largo radio", "url": SITE + "/",
            "sameAs": ["https://www.instagram.com/yummy_rainbows/", NUTRIA]}


def crumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}


def crumbs_html(items, label="Migas de pan"):
    parts = []
    for i, (n, u) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f'<span aria-current="page">{n}</span>')
        else:
            parts.append(f'<a href="{u}" style="color:#8a8470">{n}</a>')
    return (f'<nav aria-label="{label}" style="{F_JOST};font-size:13px;color:#8a8470;margin-bottom:22px">'
            + ' <span aria-hidden="true">›</span> '.join(parts) + '</nav>')


def faq_html(faq):
    return "".join(
        f'<details style="border-bottom:1px solid #e4dcc7;padding:20px 0"><summary style="display:flex;justify-content:space-between;gap:20px;align-items:center">'
        f'<span style="{F_COR};font-weight:500;font-size:clamp(21px,1.9vw,26px);color:#3c3b34">{q}</span>'
        f'<span aria-hidden="true" style="{F_JOST};font-size:24px;color:#a98a4a;transition:transform .2s">+</span></summary>'
        f'<p style="{BODY};margin-top:12px">{a}</p></details>'
        for q, a in faq)


def sources_html(c, title="Fuentes", en=False):
    if not c.order:
        return ""
    items = "".join(
        f'<li style="margin-bottom:8px"><a href="{SRC[k][1]}" target="_blank" rel="noopener" style="color:#5c5a4f;border-bottom:1px solid #d9cfb4">{html.escape(SRC[k][0].replace(" y cols.", " et al.").replace("(revisión sistemática)", "(systematic review)") if en else SRC[k][0])}</a></li>'
        for k in c.order)
    return (f'<div id="fuentes" style="max-width:760px;margin:0 auto;padding-top:clamp(30px,4vw,48px)">'
            f'<h2 style="{F_JOST};font-size:13px;letter-spacing:.24em;text-transform:uppercase;color:#a98a4a;margin-bottom:14px">{title}</h2>'
            f'<ol style="{F_JOST};font-weight:300;font-size:14px;line-height:1.6;color:#5c5a4f;padding-left:20px">{items}</ol></div>')


def cta_box(x):
    b2_text, b2_url = x["cta_b2"]
    return f"""<div style="max-width:760px;margin:clamp(30px,4vw,48px) auto 0;background:#f5efe2;border:1px solid #e7dfc9;border-radius:6px;padding:clamp(26px,3vw,38px)">
  <h2 style="{F_COR};font-weight:500;font-size:clamp(26px,2.6vw,34px);line-height:1.15;color:#5e1a24">{x['cta_h']}</h2>
  <p style="{BODY};margin-top:12px">{x['cta_p']}</p>
  <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:22px">
    <a href="{NUTRIA}" data-umami-event="perfil-nutria" target="_blank" rel="noopener" data-hover="background:#6f7a4d;color:#f7f1e6" style="{BTN}">{x['cta_b1']}</a>
    <a href="{b2_url}" data-hover="border-color:#5e1a24;color:#5e1a24" style="{BTN2}">{b2_text}</a>
  </div>
  <p style="{F_JOST};font-weight:300;font-size:15px;line-height:1.6;color:#5c5a4f;margin-top:18px">{x['cta_note']}</p>
</div>"""


def article(t):
    lang = t.get("lang", "es")
    x = {**L[lang], **t.get("cta", {})}  # una página puede cambiar los textos del recuadro final
    c = Cites(x["src"])
    url = SITE + t["path"]
    if "trail" in t:
        trail = [x["home"], *t["trail"], (t["h1"], t["path"])]
    elif lang == "es":
        trail = [x["home"], ("Trabajo a turnos", "/turnos/"), (t["h1"], t["path"])]
    else:
        trail = [x["home"], (t["h1"], t["path"])]
    intro = "".join(f'<p style="{BODY};margin-top:16px">{c(p)}</p>' for p in t["intro"])
    secs = []
    for s in t["sections"]:
        ps = "".join(f'<p style="{BODY};margin-top:14px">{c(p)}</p>' for p in s["ps"])
        lst = ""
        if s.get("list"):
            lis = "".join(f'<li style="margin-bottom:6px">{c(x)}</li>' for x in s["list"])
            lst = (f'<div style="background:#f5efe2;border-left:3px solid #c9b578;border-radius:3px;padding:18px 22px;margin-top:18px">'
                   f'<p style="{F_JOST};font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:#a98a4a;margin-bottom:10px">{s["list_h"]}</p>'
                   f'<ul style="{BODY};padding-left:20px">{lis}</ul></div>')
        after = f'<p style="{BODY};margin-top:16px">{c(s["after"])}</p>' if s.get("after") else ""
        secs.append(f'<section style="margin-top:clamp(34px,4vw,50px)"><h2 style="{H2}">{s["h2"]}</h2>{ps}{lst}{after}</section>')
    faq_ld = {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "@id": url + "#articulo", "headline": t["h1"], "description": t["desc"], "inLanguage": lang,
         "datePublished": PUBLISHED, "dateModified": PUBLISHED, "mainEntityOfPage": url, "image": SITE + "/assets/hero.jpg",
         "author": {"@id": SITE + "/#paula"}, "publisher": {"@id": SITE + "/#negocio"},
         "citation": [SRC[k][1] for k in t["sources"]]},
        person(), crumbs(trail), faq_ld]}
    main = f"""<main>
<section data-sec style="{SEC_A}">
  <div style="max-width:760px;margin:0 auto">
    {crumbs_html(trail, x["crumbs"])}
    <span style="{EYEBROW}">{t['eyebrow']}</span>
    <h1 style="{F_COR};font-weight:600;line-height:1.05;font-size:clamp(40px,4.6vw,64px);color:#5e1a24;margin-top:16px">{t['h1']}</h1>
    <div style="width:90px;height:1px;background:#c9b578;margin:24px 0"></div>
    <p style="{F_EB};font-size:clamp(19px,1.6vw,24px);line-height:1.5;color:#4c4a40">{t['lead']}</p>
    {intro}
    <p style="{F_JOST};font-size:13px;color:#8a8470;margin-top:20px">{x['by']}</p>
  </div>
</section>
<section data-sec data-body style="{SEC_B}">
  <div style="max-width:760px;margin:0 auto">
    {''.join(secs)}
  </div>
  {cta_box(x)}
  <div style="max-width:760px;margin:clamp(40px,5vw,60px) auto 0">
    <h2 style="{H2};margin-bottom:clamp(14px,2vw,24px)">{x['faq_h']}</h2>
    {faq_html(t['faq'])}
  </div>
  {sources_html(c, x["src_h"], lang == "en")}
</section>
</main>
"""
    header, footer = chrome(t)
    return head(t, ld) + header + "\n\n" + main + "\n" + footer + '\n\n<script src="/script.js"></script>\n</body>\n</html>\n'


def hub(t):
    c = Cites()
    url = SITE + t["path"]
    trail = [("Inicio", "/"), ("Trabajo a turnos", "/turnos/")]
    intro = "".join(f'<p style="{BODY};margin-top:16px">{c(p)}</p>' for p in t["intro"])
    who = "".join(
        f'<div style="{CARD}"><h3 style="{F_COR};font-weight:500;font-size:26px;line-height:1.12;color:#5e1a24">{h}</h3>'
        f'<p style="{F_JOST};font-weight:300;font-size:15px;line-height:1.65;color:#5c5a4f">{p}</p></div>' for h, p in t["who"])
    arts = "".join(
        f'<a href="{u}" data-hover="border-color:#5e1a24" style="{CARD};background:#faf6ec;transition:border-color .2s">'
        f'<span style="{F_JOST};font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:#a98a4a">Leer</span>'
        f'<h3 style="{F_COR};font-weight:500;font-size:27px;line-height:1.12;color:#5e1a24">{h}</h3>'
        f'<p style="{F_JOST};font-weight:300;font-size:15px;line-height:1.65;color:#5c5a4f">{p}</p></a>' for h, p, u in t["articles"])
    steps = "".join(
        f'<div style="{CARD}"><span style="{F_JOST};font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:#a98a4a">{i+1}</span>'
        f'<h3 style="{F_COR};font-weight:500;font-size:28px;line-height:1.1;color:#5e1a24">{h}</h3>'
        f'<p style="{F_JOST};font-weight:300;font-size:15px;line-height:1.65;color:#5c5a4f">{p}</p></div>' for i, (h, p) in enumerate(t["steps"]))
    faq_ld = {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": url + "#pagina", "url": url, "name": t["title"], "description": t["desc"], "inLanguage": "es",
         "isPartOf": {"@id": SITE + "/#negocio"}, "author": {"@id": SITE + "/#paula"},
         "audience": {"@type": "Audience", "audienceType": "Trabajadores a turnos y de noche"}},
        person(), crumbs(trail), faq_ld]}
    main = f"""<main>
<section data-sec style="{SEC_A}">
  <div data-about style="max-width:1240px;margin:0 auto;display:grid;grid-template-columns:1.2fr 0.8fr;gap:clamp(34px,5vw,72px);align-items:center">
    <div>
      {crumbs_html(trail)}
      <span style="{EYEBROW}">{t['eyebrow']}</span>
      <h1 style="{F_COR};font-weight:600;line-height:1.04;font-size:clamp(40px,4.6vw,66px);color:#5e1a24;margin-top:16px">{t['h1']}</h1>
      <div style="width:90px;height:1px;background:#c9b578;margin:24px 0"></div>
      <p style="{F_EB};font-size:clamp(19px,1.6vw,24px);line-height:1.5;color:#4c4a40">{t['lead']}</p>
      <div data-body>{intro}</div>
      <div style="display:flex;flex-wrap:wrap;gap:16px;margin-top:30px">
        <a href="{NUTRIA}" data-umami-event="perfil-nutria" target="_blank" rel="noopener" data-hover="background:#6f7a4d;color:#f7f1e6" style="{BTN}">Reserva tu cita</a>
        <a href="mailto:hola@paularubionutricionista.com" data-hover="border-color:#5e1a24;color:#5e1a24" style="{BTN2}">Escríbeme</a>
      </div>
    </div>
    <img src="/assets/paula-sitting.webp" alt="Paula Rubio, nutricionista integrativa y sobrecargo de largo radio" style="width:100%;max-width:420px;justify-self:center;aspect-ratio:4/5;object-fit:cover;border-radius:6px;box-shadow:0 12px 28px rgba(60,50,30,.14)">
  </div>
</section>

<section data-sec style="{SEC_B}">
  <div style="max-width:1240px;margin:0 auto">
    <h2 style="{H2};text-align:center;margin-bottom:clamp(26px,3vw,40px)">{t['who_h2']}</h2>
    <div data-cards style="display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(16px,2vw,24px)">{who}</div>
  </div>
</section>

<section data-sec style="{SEC_A}">
  <div style="max-width:1240px;margin:0 auto">
    <h2 style="{H2};text-align:center;margin-bottom:clamp(26px,3vw,40px)">{t['articles_h2']}</h2>
    <div data-cards style="display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(16px,2vw,24px)">{arts}</div>
  </div>
</section>

<section data-sec style="{SEC_B}">
  <div style="max-width:1240px;margin:0 auto">
    <h2 style="{H2};text-align:center;margin-bottom:clamp(26px,3vw,40px)">{t['steps_h2']}</h2>
    <div data-rules style="display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(16px,2vw,24px)">{steps}</div>
    <p style="{BODY};text-align:center;max-width:60ch;margin:34px auto 0">Si vives en España, puedes hacerte las analíticas en <a href="https://diagnoseum.com/?utm_source=web-turnos&amp;utm_medium=referral" target="_blank" rel="noopener" data-umami-event="diagnoseum-turnos" style="color:#5e1a24;border-bottom:1px solid #c9b578">Diagnoseum</a>: eliges a la carta lo que quieres medir, sin volante y con el respaldo de Eurofins.</p>
  </div>
</section>

<section data-sec style="{SEC_A}">
  <div style="max-width:860px;margin:0 auto">
    <h2 style="{H2};text-align:center;margin-bottom:clamp(20px,3vw,34px)">Preguntas frecuentes</h2>
    {faq_html(t['faq'])}
    {sources_html(c)}
  </div>
</section>
</main>
"""
    return head(t, ld) + HEADER + "\n\n" + main + "\n" + FOOTER + '\n\n<script src="/script.js"></script>\n</body>\n</html>\n'


for t, fn in ((HUB, hub), (COMER, article), (DORMIR, article), (EAT_EN, article), (SLEEP_EN, article), (JETLAG, article), (JETLAG_EN, article)):
    dest = ROOT / t["path"].strip("/") / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(fn(t))
    print("ok", dest.relative_to(ROOT))

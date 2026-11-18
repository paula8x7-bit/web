# Fabrica las páginas de consulta online por ciudad, en castellano y en inglés.
# Uso: python3 tools/ciudades/build.py  (desde la raíz del repositorio)
# Para añadir una ciudad, añade una entrada a CIUDADES y vuelve a ejecutarlo
# (y añádela al índice de guías y al sitemap).
# En la web no se ponen direcciones concretas de centros: cambian y no se pueden comprobar.
import json, re, html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = "https://paularubionutricionista.com"
NUTRIA = "https://nutriaplans.com/marketplace/paufly"

# slug, nombre, centros (es, en), línea de tripulación (o None)
CIUDADES = [
    ("madrid", "Madrid", ("los centros Eurofins y Abolab de Madrid", "any Eurofins or Abolab centre in Madrid"), True),
    ("barcelona", "Barcelona", ("cualquier centro Eurofins de Barcelona", "any Eurofins centre in Barcelona"), True),
    ("vigo", "Vigo", ("cualquier centro Eurofins de Vigo", "any Eurofins centre in Vigo"), False),
    ("santander", "Santander", ("cualquier centro Eurofins de Santander", "any Eurofins centre in Santander"), False),
]

glow = (ROOT / "planes/glow/index.html").read_text()
en_home = (ROOT / "en/index.html").read_text()
STYLE = re.search(r"<style>\s*\*\{box-sizing.*?</style>", glow, re.S).group(0)
EXTRA = """<style>
@media(max-width:900px){[data-cards]{grid-template-columns:1fr 1fr!important}[data-rules]{grid-template-columns:1fr!important}}
@media(max-width:640px){[data-cards]{grid-template-columns:1fr!important}}
details summary{cursor:pointer;list-style:none}
details summary::-webkit-details-marker{display:none}
details[open] summary span:last-child{transform:rotate(45deg)}
[data-body] a{color:#5e1a24;border-bottom:1px solid #c9b578}
</style>"""
UMAMI = """<script>try{if(/[?&]soy-paula/.test(location.search))localStorage.setItem("umami.disabled","1")}catch(e){}</script>
<script defer src="https://cloud.umami.is/script.js" data-website-id="21a20c4a-cd36-44e3-bc6b-2af2bde813e7"></script>"""


def block(src, start, end):
    return src[src.index(start): src.index(end) + len(end)]


ES_HEADER = block(glow, "<header", "</header>")
ES_FOOTER = block(glow, "<footer", "</footer>")
EN_HEADER = block(en_home, "<header", "</header>")
EN_FOOTER = block(en_home, "<footer", "</footer>")
for frag in ("inicio", "sobre-mi", "servicios", "planes", "contacto"):
    EN_HEADER = EN_HEADER.replace(f'href="#{frag}"', f'href="/en/#{frag}"')
    EN_FOOTER = EN_FOOTER.replace(f'href="#{frag}"', f'href="/en/#{frag}"')

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


def texts(lang, slug, city, centros, crew):
    dg = f"https://diagnoseum.com/?utm_source=web-ciudad-{slug}{'-en' if lang == 'en' else ''}&amp;utm_medium=referral"
    ev = f"diagnoseum-ciudad-{slug}{'-en' if lang == 'en' else ''}"
    dlink = f'<a href="{dg}" target="_blank" rel="noopener" data-umami-event="{ev}">Diagnoseum</a>'
    if lang == "es":
        t = {
            "path": f"/nutricionista-online/{slug}/",
            "title": f"Nutricionista integrativa online en {city} | Paula Rubio",
            "desc": f"Nutricionista integrativa online para {city}: consulta por videollamada o plan sin videollamada, y analíticas sin volante en {centros[0]}.",
            "eyebrow": f"Consulta online · {city}",
            "h1": f"Nutricionista integrativa online en {city}",
            "lead": f"Consulta desde casa, por videollamada, y la analítica en un centro de {city}.",
            "intro": [
                f"Soy Paula Rubio, dietista-nutricionista con enfoque clínico e integrativo, y sobrecargo de largo radio. Paso consulta online, así que da igual que vivas en {city}: trabajamos por videollamada o con un plan en la app, y si hace falta una analítica, te la haces cerca de casa.",
                "Trabajo con dietoterapia personalizada en composición corporal, salud digestiva, autoinmunidad, alteraciones hormonales, fatiga y otros casos que requieren mirar más allá de una pauta alimentaria aislada.",
            ],
            "lab_h2": f"Tu analítica en {city}",
            "lab": [
                f"Si vives en {city}, puedes hacerte las analíticas con {dlink}, el proyecto de análisis clínicos que he cofundado: eliges a la carta lo que quieres medir, sin volante y con el respaldo de Eurofins.",
                f"Compras online lo que quieres medir y te sacas la sangre en {centros[0]}. Después la leemos juntos y la uso para tu plan.",
            ],
            "who_h2": "Con quién trabajo",
            "who": [
                ("Salud digestiva y hormonas", "Digestiones pesadas, hinchazón, ciclo, piel, autoinmunidad y fatiga.", "/guias/"),
                ("Trabajo a turnos", "Enfermería, medicina, policía, emergencias e industria: comida y sueño con tu cuadrante.", "/turnos/"),
                ("Tripulaciones y viajeros", "Jet lag, comida a bordo y escalas. Tienes una guía gratuita.", "/tripulaciones/" if crew else "/jet-lag/"),
            ],
            "srv_h2": "Cómo trabajar conmigo",
            "srv": [
                ("Planes ya hechos", "Desde 39,99 €", "Eliges uno de mis planes de 4 semanas y empiezas hoy. Lo sigues en Nutria, que ajusta las cantidades a ti."),
                ("Plan personalizado", "Desde 69 €", "Tu plan hecho a partir de mi cuestionario, tus gustos y tu analítica. Sin videollamada."),
                ("Con videollamada", "Desde 75 €", "Consulta inicial, seguimiento mensual y seguimiento clínico para casos complejos."),
            ],
            "crew": (f"¿Eres TCP o piloto con base en {city}? Tienes una <a href=\"/tripulaciones/\">guía gratuita para tripulaciones de largo radio</a> y, si vuelas en corto radio, <a href=\"/tcp-corto-radio-que-comer/\">qué comer con madrugones y varios saltos</a>." if crew else ""),
            "cta": "Reserva tu cita", "cta2": ("Ver guías y artículos", "/guias/"),
            "faq_h": "Preguntas frecuentes",
            "faq": [
                (f"¿Puedo hacer la consulta si vivo en {city}?", f"Sí. La consulta es online, por videollamada, en castellano o en inglés. También puedes trabajar conmigo sin videollamada, con un plan ya hecho o un plan personalizado en la app."),
                (f"¿Dónde me hago la analítica en {city}?", f"Con Diagnoseum te la haces en {centros[0]}. Compras online lo que quieres medir y vas al centro."),
                ("¿Necesito volante del médico?", "No. Con Diagnoseum eliges a la carta lo que quieres medir, sin volante y con el respaldo de Eurofins."),
                ("¿Cuánto cuesta?", "Los planes ya hechos, desde 39,99 €; el plan personalizado, desde 69 €; y la consulta con videollamada, desde 75 €."),
            ],
            "home": ("Inicio", "/"), "crumbs": "Migas de pan", "locale": "es_ES",
            "alt": f"/en/nutritionist/{slug}/",
        }
    else:
        t = {
            "path": f"/en/nutritionist/{slug}/",
            "title": f"English speaking nutritionist in {city} (online) | Paula Rubio",
            "desc": f"English speaking integrative nutritionist for {city}: online consultations or plans without a video call, and blood tests with no doctor's referral at {centros[1]}.",
            "eyebrow": f"Online consultations · {city}",
            "h1": f"English speaking nutritionist in {city}",
            "lead": f"Consultations from home, by video call, and your blood test at a centre in {city}.",
            "intro": [
                f"I'm Paula Rubio, a registered dietitian-nutritionist with a clinical and integrative approach, and a long haul Inflight Manager. I consult online in English and Spanish, so it doesn't matter that you live in {city}: we work by video call or with a plan in the app, and if you need a blood test, you can have it done near home.",
                "I work with personalized diet therapy for body composition, digestive health, autoimmunity, hormonal imbalances, fatigue and other cases that call for looking beyond an isolated meal plan.",
            ],
            "lab_h2": f"Your blood test in {city}",
            "lab": [
                f"If you live in {city}, you can get your blood tests done with {dlink}, the clinical testing project I co-founded: you choose exactly what you want to test, no doctor's referral needed, backed by Eurofins.",
                f"You buy online what you want to test and have your blood drawn at {centros[1]}. Then we go through the results together and I use them for your plan.",
            ],
            "who_h2": "Who I work with",
            "who": [
                ("Digestive and hormonal health", "Heavy digestion, bloating, your cycle, skin, autoimmunity and fatigue.", "/en/"),
                ("Shift workers", "Nurses, doctors, police, emergency services and industry: food and sleep around your rota.", "/en/what-to-eat-on-night-shift/"),
                ("Cabin crew and travellers", "Jet lag, food on board and layovers. There's a free guide for crew.", "/en/cabin-crew/" if crew else "/en/jet-lag/"),
            ],
            "srv_h2": "How to work with me",
            "srv": [
                ("Ready-made plans", "From €39.99", "Pick one of my 4-week plans and start today. You follow it in Nutria, which adjusts the amounts to you."),
                ("Personalized plan", "From €69", "Your plan built from my questionnaire, your tastes and your blood work. No video call."),
                ("With video call", "From €75", "Initial consultation, monthly follow-up and clinical follow-up for complex cases."),
            ],
            "crew": (f"Cabin crew or pilot based in {city}? There's a <a href=\"/en/cabin-crew/\">free guide for long haul crew</a> and, if you fly short haul, <a href=\"/en/short-haul-cabin-crew-food/\">what to eat on earlies and multi sector days</a>." if crew else ""),
            "cta": "Book an appointment", "cta2": ("Guides and articles", "/en/guides/"),
            "faq_h": "Frequently asked questions",
            "faq": [
                (f"Can I book a consultation if I live in {city}?", "Yes. Consultations are online, by video call, in English or Spanish. You can also work with me without a video call, with a ready-made or personalized plan in the app."),
                (f"Where can I get a blood test in {city}?", f"With Diagnoseum, at {centros[1]}. You buy online what you want to test and go to the centre."),
                ("Do I need a doctor's referral?", "No. With Diagnoseum you choose exactly what you want to test, no doctor's referral needed, backed by Eurofins."),
                ("How much does it cost?", "Ready-made plans from €39.99, a personalized plan from €69 and a consultation with video call from €75."),
            ],
            "home": ("Home", "/en/"), "crumbs": "Breadcrumb", "locale": "en_GB",
            "alt": f"/nutricionista-online/{slug}/",
        }
    t["lang"], t["city"] = lang, city
    return t


def faq_html(faq):
    return "".join(
        f'<details style="border-bottom:1px solid #e4dcc7;padding:20px 0"><summary style="display:flex;justify-content:space-between;gap:20px;align-items:center">'
        f'<span style="{F_COR};font-weight:500;font-size:clamp(21px,1.9vw,26px);color:#3c3b34">{q}</span>'
        f'<span aria-hidden="true" style="{F_JOST};font-size:24px;color:#a98a4a;transition:transform .2s">+</span></summary>'
        f'<p style="{BODY};margin-top:12px">{a}</p></details>' for q, a in faq)


def page(t):
    lang = t["lang"]
    url = SITE + t["path"]
    es_url, en_url = (url, SITE + t["alt"]) if lang == "es" else (SITE + t["alt"], url)
    header, footer = (ES_HEADER, ES_FOOTER) if lang == "es" else (EN_HEADER, EN_FOOTER)
    # Selector ES / EN a la página gemela
    header = header.replace('href="/en/"', f'href="{t["alt"]}"') if lang == "es" else header.replace('href="/"', f'href="{t["alt"]}"')
    home = t["home"]
    crumbs = (f'<nav aria-label="{t["crumbs"]}" style="{F_JOST};font-size:13px;color:#8a8470;margin-bottom:22px">'
              f'<a href="{home[1]}" style="color:#8a8470">{home[0]}</a> <span aria-hidden="true">›</span> <span aria-current="page">{t["h1"]}</span></nav>')
    intro = "".join(f'<p style="{BODY};margin-top:16px">{p}</p>' for p in t["intro"])
    lab = "".join(f'<p style="{BODY};margin-top:14px">{p}</p>' for p in t["lab"])
    who = "".join(
        f'<a href="{u}" data-hover="border-color:#5e1a24" style="{CARD};color:inherit;transition:border-color .2s">'
        f'<h3 style="{F_COR};font-weight:500;font-size:26px;line-height:1.12;color:#5e1a24">{h}</h3>'
        f'<p style="{F_JOST};font-weight:300;font-size:15px;line-height:1.65;color:#5c5a4f">{p}</p></a>' for h, p, u in t["who"])
    srv = "".join(
        f'<div style="{CARD}"><span style="{F_JOST};font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:#a98a4a">{price}</span>'
        f'<h3 style="{F_COR};font-weight:500;font-size:28px;line-height:1.1;color:#5e1a24">{h}</h3>'
        f'<p style="{F_JOST};font-weight:300;font-size:15px;line-height:1.65;color:#5c5a4f">{p}</p></div>' for h, price, p in t["srv"])
    crew = f'<p style="{BODY};text-align:center;max-width:60ch;margin:30px auto 0">{t["crew"]}</p>' if t["crew"] else ""
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": url + "#pagina", "url": url, "name": t["title"], "description": t["desc"], "inLanguage": lang,
         "author": {"@id": SITE + "/#paula"}},
        {"@type": "Service", "name": t["h1"], "serviceType": "Nutrition consultation", "url": url,
         "provider": {"@type": "Person", "@id": SITE + "/#paula", "name": "Paula Rubio"},
         "areaServed": {"@type": "City", "name": t["city"]}, "availableLanguage": ["es", "en"]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": home[0], "item": SITE + home[1]},
            {"@type": "ListItem", "position": 2, "name": t["h1"], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in t["faq"]]}]}
    cta2_text, cta2_url = t["cta2"]
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
<link rel="alternate" hreflang="es" href="{es_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{es_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Paula Rubio Nutricionista">
<meta property="og:locale" content="{t['locale']}">
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
{header}

<main>
<section data-sec style="{SEC_A}">
  <div data-about style="max-width:1240px;margin:0 auto;display:grid;grid-template-columns:1.2fr 0.8fr;gap:clamp(34px,5vw,72px);align-items:center">
    <div>
      {crumbs}
      <span style="{EYEBROW}">{t['eyebrow']}</span>
      <h1 style="{F_COR};font-weight:600;line-height:1.04;font-size:clamp(40px,4.6vw,64px);color:#5e1a24;margin-top:16px">{t['h1']}</h1>
      <div style="width:90px;height:1px;background:#c9b578;margin:24px 0"></div>
      <p style="{F_EB};font-size:clamp(19px,1.6vw,24px);line-height:1.5;color:#4c4a40">{t['lead']}</p>
      <div data-body>{intro}</div>
      <div style="display:flex;flex-wrap:wrap;gap:16px;margin-top:30px">
        <a href="{NUTRIA}" data-umami-event="perfil-nutria" target="_blank" rel="noopener" data-hover="background:#6f7a4d;color:#f7f1e6" style="{BTN}">{t['cta']}</a>
        <a href="{cta2_url}" data-hover="border-color:#5e1a24;color:#5e1a24" style="{BTN2}">{cta2_text}</a>
      </div>
    </div>
    <img src="/assets/paula-sitting.webp" alt="Paula Rubio" style="width:100%;max-width:420px;justify-self:center;aspect-ratio:4/5;object-fit:cover;border-radius:6px;box-shadow:0 12px 28px rgba(60,50,30,.14)">
  </div>
</section>

<section data-sec data-body style="{SEC_B}">
  <div style="max-width:760px;margin:0 auto">
    <h2 style="{H2}">{t['lab_h2']}</h2>
    {lab}
  </div>
</section>

<section data-sec style="{SEC_A}">
  <div style="max-width:1240px;margin:0 auto">
    <h2 style="{H2};text-align:center;margin-bottom:clamp(26px,3vw,40px)">{t['who_h2']}</h2>
    <div data-cards style="display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(16px,2vw,24px)">{who}</div>
    <div data-body>{crew}</div>
  </div>
</section>

<section data-sec style="{SEC_B}">
  <div style="max-width:1240px;margin:0 auto">
    <h2 style="{H2};text-align:center;margin-bottom:clamp(26px,3vw,40px)">{t['srv_h2']}</h2>
    <div data-rules style="display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(16px,2vw,24px)">{srv}</div>
    <div style="text-align:center;margin-top:34px">
      <a href="{NUTRIA}" data-umami-event="perfil-nutria" target="_blank" rel="noopener" data-hover="background:#6f7a4d;color:#f7f1e6" style="{BTN}">{t['cta']}</a>
    </div>
  </div>
</section>

<section data-sec style="{SEC_A}">
  <div style="max-width:860px;margin:0 auto">
    <h2 style="{H2};text-align:center;margin-bottom:clamp(20px,3vw,34px)">{t['faq_h']}</h2>
    {faq_html(t['faq'])}
  </div>
</section>
</main>

{footer}

<script src="/script.js"></script>
</body>
</html>
"""


for slug, city, centros, crew in CIUDADES:
    for lang in ("es", "en"):
        t = texts(lang, slug, city, centros, crew)
        dest = ROOT / t["path"].strip("/") / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page(t))
        print("ok", dest.relative_to(ROOT))

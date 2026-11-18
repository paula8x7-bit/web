# Fabrica el índice de guías y recursos (/guias/ y /en/guides/), al que lleva «Guías» del menú y el botón de la portada.
# Uso: python3 tools/guias/build.py  (desde la raíz del repositorio)
# Cuando publiques una página nueva (artículo, receta, plan), añádela aquí a su sección y vuelve a ejecutarlo.
import json, re, html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = "https://paularubionutricionista.com"
ES_PATH, EN_PATH = "/guias/", "/en/guides/"

# (etiqueta, título, texto, enlace, imagen o None)
ES = {
    "title": "Guías, artículos y recetas | Paula Rubio",
    "desc": "Todo lo que he publicado, ordenado por tema: trabajo a turnos, tripulaciones, planes de 4 semanas y recetas.",
    "h1": "Guías y recursos",
    "lead": "Todo lo que he ido publicando, ordenado por tema.",
    "sections": [
        ("Trabajo a turnos", [
            ("Artículo", "Qué comer en el turno de noche", "Antes, durante y al salir, con ideas para el táper.", "/turnos/que-comer-en-el-turno-de-noche/", None),
            ("Artículo", "Cómo dormir después de un turno de noche", "Luz, oscuridad, horarios y café para dormir de día.", "/turnos/como-dormir-despues-del-turno-de-noche/", None),
            ("Consulta", "Nutricionista para trabajo a turnos", "Cómo trabajo con quien come a deshora y duerme de día.", "/turnos/", None),
        ]),
        ("Viajes y tripulaciones", [
            ("Artículo", "Jet lag: cómo recuperarte", "Síntomas, por qué cuesta más volar al este y qué hacer con la luz, la comida y el café.", "/jet-lag/", None),
            ("Artículo", "Qué comer antes de un vuelo largo", "Qué llevar al avión y cómo evitar la hinchazón, las piernas pesadas y el estreñimiento.", "/que-comer-antes-de-un-vuelo-largo/", None),
            ("Guía gratuita", "Guía para tripulaciones de largo radio", "Jet lag, comida a bordo, sueño y analíticas para escalas de 24 a 72 horas.", "/tripulaciones/", "/assets/guias/portada-guia-tripulaciones.webp|contain"),
        ]),
        ("Planes de 4 semanas", [
            ("Plan", "Come según tu ciclo", "La comida ordenada por el día de tu ciclo: regla, folicular, ovulación y lútea.", "/planes/come-segun-tu-ciclo/", "/assets/planes/46efbd82-da71-467f-8074-0579563f8faa.webp"),
            ("Plan", "Glow, piel luminosa desde dentro", "Cuatro semanas de comida para la piel: colágeno, barrera, minerales y color.", "/planes/glow/", "/assets/planes/37793bec-6f56-455e-ad92-1e6d8d0a0fdc.webp"),
            ("Planes", "¿Qué quieres trabajar?", "Todos los planes, para elegir según lo que quieres conseguir.", "/planes/", None),
        ]),
        ("Recetas", [
            ("Receta", "Golden milk con azafrán", "Una bebida caliente con cúrcuma, jengibre y canela para los días de regla.", "/recetas/golden-milk-con-azafran/", "/assets/planes/f5805796-536b-491d-9c7d-edeea8f7e9b6.webp"),
            ("Receta", "Mousse de cacao y aguacate con nueces", "Un postre sin azúcar añadido, con plátano, para los días de regla.", "/recetas/mousse-de-cacao-y-aguacate/", "/assets/planes/6fa439da-7d73-41cd-94e5-f35b0a4ed0e0.webp"),
            ("Receta", "Mousse de cacao y aguacate con frambuesa", "Sin azúcar añadido y sin nata, con frambuesas.", "/recetas/mousse-de-cacao-aguacate-y-frambuesa/", "/assets/planes/0b7d6d7d-2e46-4f87-8754-98da44e7ac47.webp"),
            ("Receta", "Shot rubí de pimiento, naranja y lima", "Vitamina C para fabricar colágeno, en un vasito.", "/recetas/shot-de-pimiento-rojo-naranja-y-lima/", "/assets/planes/1aab1d12-95bb-4e7e-9d86-c0004e370813.webp"),
        ]),
    ],
    "note": "",
}

EN = {
    "title": "Guides and resources | Paula Rubio",
    "desc": "Everything I've published in English, sorted by topic: night shift eating and a free guide for long haul cabin crew.",
    "h1": "Guides and resources",
    "lead": "Everything I've published, sorted by topic.",
    "sections": [
        ("Night shift", [
            ("Article", "What to eat on night shift", "Before, during and after, with an eating schedule and meal prep ideas.", "/en/what-to-eat-on-night-shift/", None),
            ("Article", "How to sleep after a night shift", "Light, darkness, a fixed bedtime and caffeine to sleep during the day.", "/en/how-to-sleep-after-night-shift/", None),
        ]),
        ("Travel and cabin crew", [
            ("Article", "How to beat jet lag", "Going east or west, from the UK to the USA or Australia, with a jet lag eating schedule.", "/en/jet-lag/", None),
            ("Article", "Cabin crew meal prep", "What to cook before a trip, what to pack and what to eat on a night flight.", "/en/cabin-crew-meal-prep/", None),
            ("Free guide", "Guide for long haul cabin crew", "Jet lag, food on board, sleep and blood tests for 24 to 72 hour layovers.", "/en/cabin-crew/", "/assets/guias/cabin-crew-guide-cover.webp|contain"),
        ]),
    ],
    "note": 'My plans and recipes are in Spanish for now. If you read Spanish, you\'ll find them <a href="/guias/" hreflang="es" style="color:#5e1a24;border-bottom:1px solid #c9b578">here</a>.',
}

glow = (ROOT / "planes/glow/index.html").read_text()
en_home = (ROOT / "en/index.html").read_text()
STYLE = re.search(r"<style>\s*\*\{box-sizing.*?</style>", glow, re.S).group(0)
EXTRA = """<style>
@media(max-width:900px){[data-cards]{grid-template-columns:1fr 1fr!important}}
@media(max-width:600px){[data-cards]{grid-template-columns:1fr!important}}
[data-card]:hover{border-color:#c9b578!important}
</style>"""
UMAMI = """<script>try{if(/[?&]soy-paula/.test(location.search))localStorage.setItem("umami.disabled","1")}catch(e){}</script>
<script defer src="https://cloud.umami.is/script.js" data-website-id="21a20c4a-cd36-44e3-bc6b-2af2bde813e7"></script>"""


def block(src, start, end):
    return src[src.index(start): src.index(end) + len(end)]


ES_HEADER = block(glow, "<header", "</header>").replace('href="/en/"', f'href="{EN_PATH}"')
ES_FOOTER = block(glow, "<footer", "</footer>")
EN_HEADER = block(en_home, "<header", "</header>")
EN_FOOTER = block(en_home, "<footer", "</footer>")
for frag in ("inicio", "sobre-mi", "servicios", "planes", "contacto"):
    EN_HEADER = EN_HEADER.replace(f'href="#{frag}"', f'href="/en/#{frag}"')
    EN_FOOTER = EN_FOOTER.replace(f'href="#{frag}"', f'href="/en/#{frag}"')
EN_HEADER = EN_HEADER.replace('href="/"', f'href="{ES_PATH}"')

F_JOST = "font-family:'Jost',sans-serif"
F_COR = "font-family:'Cormorant Garamond',serif"
F_EB = "font-family:'EB Garamond',serif"
EYEBROW = f"{F_JOST};font-size:13px;letter-spacing:.32em;text-transform:uppercase;color:#a98a4a"
H2 = f"{F_COR};font-weight:500;font-size:clamp(30px,3.2vw,42px);line-height:1.1;color:#3c3b34"
SEC_A = "background:#faf6ec;padding:clamp(54px,7vw,98px) clamp(22px,5vw,72px) clamp(30px,4vw,50px)"
SEC_B = "background:#f5efe2;padding:clamp(40px,5vw,70px) clamp(22px,5vw,72px) clamp(54px,7vw,98px)"


def card(label, title, text, url, img):
    # «ruta|contain» muestra la imagen entera (portadas), sin recortarla
    src, _, fit = (img or "").partition("|")
    pic = (f'<img src="{src}" alt="" loading="lazy" style="width:100%;aspect-ratio:4/3;object-fit:{fit or "cover"};display:block;background:#efe7d5">'
           if img else "")
    return (f'<a href="{url}" data-card style="display:flex;flex-direction:column;background:#faf6ec;border:1px solid #e7dfc9;'
            f'border-radius:5px;overflow:hidden;color:inherit;transition:border-color .2s">{pic}'
            f'<div style="padding:22px 22px 24px;display:flex;flex-direction:column;gap:10px;flex:1">'
            f'<span style="{F_JOST};font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:#a98a4a">{label}</span>'
            f'<h3 style="{F_COR};font-weight:500;font-size:clamp(24px,2vw,28px);line-height:1.12;color:#5e1a24">{title}</h3>'
            f'<p style="{F_JOST};font-weight:300;font-size:15px;line-height:1.65;color:#5c5a4f">{text}</p></div></a>')


def page(t, lang):
    path, alt = (ES_PATH, EN_PATH) if lang == "es" else (EN_PATH, ES_PATH)
    url, es_url, en_url = SITE + path, SITE + ES_PATH, SITE + EN_PATH
    home = ("Inicio", "/") if lang == "es" else ("Home", "/en/")
    secs = "".join(
        f'<div style="max-width:1240px;margin:0 auto clamp(40px,5vw,64px)">'
        f'<h2 style="{H2};margin-bottom:clamp(18px,2.4vw,28px)">{name}</h2>'
        f'<div data-cards style="display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(16px,2vw,24px);align-items:start">'
        + "".join(card(*c) for c in cards) + "</div></div>"
        for name, cards in t["sections"])
    note = (f'<p style="{F_JOST};font-weight:300;font-size:16px;line-height:1.7;color:#5c5a4f;max-width:1240px;margin:0 auto">{t["note"]}</p>'
            if t["note"] else "")
    items = [c for _, cards in t["sections"] for c in cards]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "@id": url + "#pagina", "url": url, "name": t["h1"], "description": t["desc"],
         "inLanguage": lang, "author": {"@id": SITE + "/#paula"},
         "mainEntity": {"@type": "ItemList", "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "name": c[1], "url": SITE + c[3]} for i, c in enumerate(items)]}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": home[0], "item": SITE + home[1]},
            {"@type": "ListItem", "position": 2, "name": t["h1"], "item": url}]}]}
    header, footer = (ES_HEADER, ES_FOOTER) if lang == "es" else (EN_HEADER, EN_FOOTER)
    crumbs = (f'<nav aria-label="{"Migas de pan" if lang == "es" else "Breadcrumb"}" style="{F_JOST};font-size:13px;color:#8a8470;margin-bottom:22px">'
              f'<a href="{home[1]}" style="color:#8a8470">{home[0]}</a> <span aria-hidden="true">›</span> <span aria-current="page">{t["h1"]}</span></nav>')
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
<meta property="og:locale" content="{'es_ES' if lang == 'es' else 'en_GB'}">
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
  <div style="max-width:1240px;margin:0 auto">
    {crumbs}
    <span style="{EYEBROW}">Paula Rubio</span>
    <h1 style="{F_COR};font-weight:600;line-height:1.05;font-size:clamp(40px,4.6vw,64px);color:#5e1a24;margin-top:16px">{t['h1']}</h1>
    <div style="width:90px;height:1px;background:#c9b578;margin:24px 0"></div>
    <p style="{F_EB};font-size:clamp(19px,1.6vw,24px);line-height:1.5;color:#4c4a40">{t['lead']}</p>
  </div>
</section>
<section data-sec style="{SEC_B}">
  {secs}
  {note}
</section>
</main>

{footer}

<script src="/script.js"></script>
</body>
</html>
"""


for t, lang, path in ((ES, "es", ES_PATH), (EN, "en", EN_PATH)):
    dest = ROOT / path.strip("/") / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page(t, lang))
    print("ok", dest.relative_to(ROOT))

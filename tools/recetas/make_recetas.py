"""Genera las páginas de receta en /recetas/<slug>/ a partir de la plantilla de la página del plan.

Uso: python3 tools/recetas/make_recetas.py
Reutiliza los estilos, la cabecera y el pie de planes/come-segun-tu-ciclo/index.html.
"""
import html
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SITE = "https://paularubionutricionista.com"
UMAMI = '<script defer src="https://cloud.umami.is/script.js" data-website-id="21a20c4a-cd36-44e3-bc6b-2af2bde813e7"></script>'

PLANES = {
    "ciclo": {
        "nombre": "Come según tu ciclo",
        "pagina": "/planes/come-segun-tu-ciclo/",
        "tienda": "https://nutriaplans.com/plan-store/come-segun-tu-ciclo",
        "evento": "comprar-ciclo",
        "resumen": "Cuatro semanas de comida ordenadas por el día de tu ciclo: guisos y cosas calientes en la regla, crudo y verde en la fase folicular y postre real todos los días en la lútea. Con sus recetas, sus alternativas y la lista de la compra, en la app de Nutria.",
    },
    "glow": {
        "nombre": "Glow, piel luminosa desde dentro",
        "pagina": "/planes/glow/",
        "tienda": "https://nutriaplans.com/plan-store/glow-piel-luminosa-desde-dentro",
        "evento": "comprar-glow",
        "resumen": "Cuatro semanas de comida para la piel, una por cada cosa que necesita: colágeno, barrera, minerales y color. Con sus recetas, sus alternativas y el porqué de cada plato, en la app de Nutria.",
    },
}

RECETAS = [
    {
        "slug": "mousse-de-cacao-y-aguacate",
        "plan": "ciclo",
        "foto": "6fa439da-7d73-41cd-94e5-f35b0a4ed0e0",
        "titulo": "Mousse de cacao y aguacate con nueces",
        "seo_titulo": "Mousse de cacao y aguacate sin azúcar para los días de regla",
        "descripcion": "Receta de mousse de cacao y aguacate con plátano y nueces, sin azúcar añadido. Un postre que abriga en los días de regla.",
        "momento": "Días de regla · Merienda",
        "intro": "Cremosa, de cuchara y sin azúcar añadido. El dulce lo pone el plátano maduro, y el aguacate hace de nata sin que se note. Para cuando baja la energía y apetece algo que abrigue.",
        "raciones": "1 ración",
        "tiempo": "PT10M",
        "tiempo_texto": "10 minutos y un rato de nevera",
        "ingredientes": [
            ("Aguacate", "60 g", "medio aguacate pequeño"),
            ("Plátano bien maduro", "60 g", "medio plátano"),
            ("Cacao puro en polvo", "8 g", "1 cucharada generosa"),
            ("Canela de Ceilán", "2 g", "1 cucharadita"),
            ("Nueces", "8 g", "3 o 4 mitades"),
            ("Lino molido", "12 g", "1 cucharada colmada"),
            ("Pipas de calabaza", "8 g", "1 cucharada rasa"),
        ],
        "pasos": [
            "Tritura el aguacate con el plátano y el cacao hasta que quede sedoso, sin grumos.",
            "Pásalo a un bol o a una copa y déjalo en la nevera para que coja textura de mousse.",
            "Al servir, pon por encima la canela, las nueces picadas y las semillas: lino molido y pipas de calabaza.",
        ],
        "nota": "El lino y la pipa de calabaza son las semillas de la primera mitad del ciclo, del día 1 al 14. En la segunda mitad cambian a sésamo y girasol.",
        "en_el_plan": "Es la merienda del día 1, el primer día de regla.",
    },
    {
        "slug": "golden-milk-con-azafran",
        "plan": "ciclo",
        "foto": "f5805796-536b-491d-9c7d-edeea8f7e9b6",
        "titulo": "Golden milk con azafrán",
        "seo_titulo": "Golden milk con azafrán y cúrcuma para los días de regla",
        "descripcion": "Receta de golden milk con cúrcuma, jengibre, canela y azafrán. Una bebida caliente para la media tarde en los días de regla.",
        "momento": "Días de regla · Media tarde",
        "intro": "Algo caliente entre las manos a media tarde. Cúrcuma, jengibre, canela y unas hebras de azafrán, a fuego lento y sin prisa.",
        "raciones": "1 taza",
        "tiempo": "PT10M",
        "tiempo_texto": "10 minutos",
        "ingredientes": [
            ("Bebida de almendra sin azúcar, enriquecida en calcio", "200 ml", "1 vaso"),
            ("Azafrán", "unas 15 hebras", ""),
            ("Cúrcuma molida", "2 g", "1 cucharadita rasa"),
            ("Jengibre fresco", "5 g", "un trocito rallado"),
            ("Canela de Ceilán", "1 g", "media cucharadita"),
            ("Crema de almendra", "5 g", "1 cucharadita rasa"),
            ("Pimienta negra", "", "una vuelta de molinillo"),
        ],
        "pasos": [
            "Machaca el azafrán en el mortero y déjalo cinco minutos en una cucharada de agua caliente.",
            "Calienta la bebida de almendra con la cúrcuma, el jengibre rallado y la canela, cinco minutos a fuego bajo y sin que llegue a hervir.",
            "Añade el azafrán con su agua y la crema de almendra, y bate.",
            "Termina con una vuelta de pimienta negra, que ayuda a que la curcumina se absorba.",
        ],
        "nota": "Mira la etiqueta de la bebida de almendra: muchas, sobre todo las ecológicas, no llevan calcio añadido. Y el azafrán, si lo echas entero y directo, suelta color pero poco sabor; por eso se machaca y se remoja antes.",
        "en_el_plan": "Es una de las bebidas de media tarde de los días 1 a 5.",
    },
    {
        "slug": "shot-de-pimiento-rojo-naranja-y-lima",
        "plan": "glow",
        "foto": "1aab1d12-95bb-4e7e-9d86-c0004e370813",
        "titulo": "Shot rubí de pimiento, naranja y lima",
        "seo_titulo": "Shot de pimiento rojo, naranja y lima: vitamina C para la piel",
        "descripcion": "Receta de shot de pimiento rojo crudo, naranja y lima, rico en vitamina C para fabricar colágeno. Se toma recién hecho y en ayunas.",
        "momento": "Semana del colágeno · En ayunas",
        "intro": "Pimiento rojo crudo, naranja y lima, recién hecho. Abre cada mañana de la semana del colágeno, porque la vitamina C es la pieza sin la que tu cuerpo no puede fabricarlo bien.",
        "raciones": "1 shot",
        "tiempo": "PT5M",
        "tiempo_texto": "5 minutos",
        "ingredientes": [
            ("Pimiento rojo crudo", "60 g", "medio pimiento pequeño"),
            ("Naranja pelada", "80 g", "media naranja"),
            ("Lima", "10 g", "un chorrito"),
        ],
        "pasos": [
            "Tritura el pimiento rojo crudo con la naranja y el chorrito de lima.",
            "Tómalo recién hecho, en ayunas y antes del desayuno.",
            "Después, enjuágate la boca con agua.",
        ],
        "nota": "Lo de crudo y al momento tiene su porqué: la vitamina C se pierde con el calor, pero también con el tiempo y con el aire, así que un shot hecho la víspera llega a medias. El pimiento rojo crudo tiene más vitamina C que la naranja. Y como es ácido, no te laves los dientes en la media hora siguiente: el esmalte queda un rato más blando.",
        "en_el_plan": "Se toma los siete días de la primera semana, la del colágeno.",
    },
    {
        "slug": "mousse-de-cacao-aguacate-y-frambuesa",
        "plan": "glow",
        "foto": "0b7d6d7d-2e46-4f87-8754-98da44e7ac47",
        "titulo": "Mousse de cacao y aguacate con frambuesa",
        "seo_titulo": "Mousse de cacao, aguacate y frambuesa sin azúcar añadido",
        "descripcion": "Receta de mousse de cacao y aguacate con gelatina y frambuesas, sin azúcar añadido y sin nata. Un postre pensado para la piel.",
        "momento": "Semana del colágeno · Merienda",
        "intro": "Cremosa, sin nata y sin azúcar añadido. Nadie diría que lleva aguacate. El cacao puro aporta cobre y la gelatina, glicina, dos cosas que la piel usa en la semana del colágeno.",
        "raciones": "1 copa",
        "tiempo": "PT10M",
        "tiempo_texto": "10 minutos y dos horas de nevera",
        "ingredientes": [
            ("Aguacate", "45 g", "un tercio de aguacate"),
            ("Cacao puro en polvo", "10 g", "1 cucharada colmada"),
            ("Gelatina neutra en polvo, sin azúcar", "10 g", ""),
            ("Frambuesas", "100 g", "un puñado grande"),
        ],
        "pasos": [
            "Disuelve la gelatina en un poco de agua caliente.",
            "Tritura el aguacate con el cacao y la gelatina disuelta, y bate hasta que quede completamente liso. Insiste más de lo que crees: la textura lo es todo.",
            "Pásalo a una copa y déjalo un par de horas en la nevera.",
            "Termina con las frambuesas por encima.",
        ],
        "nota": "La gelatina es la forma más sencilla de comer glicina, el aminoácido del que más se gasta al fabricar colágeno. Por eso aparece casi a diario en la primera semana del plan.",
        "en_el_plan": "Es la merienda del día 4 de la primera semana, la del colágeno.",
    },
]

E = html.escape


def plantilla():
    src = open(os.path.join(ROOT, "planes", "come-segun-tu-ciclo", "index.html"), encoding="utf-8").read()
    estilos = re.search(r"<style>\n\*\{box-sizing.*?</style>", src, re.S).group(0)
    cabecera = re.search(r"<header.*?</header>", src, re.S).group(0)
    pie = re.search(r"<footer.*?</html>", src, re.S).group(0)
    return estilos, cabecera, pie


def pagina(r, estilos, cabecera, pie):
    p = PLANES[r["plan"]]
    url = f"{SITE}/recetas/{r['slug']}/"
    img = f"{SITE}/assets/planes/{r['foto']}.jpg"
    ld = {
        "@context": "https://schema.org",
        "@type": "Recipe",
        "name": r["titulo"],
        "description": r["descripcion"],
        "image": img,
        "author": {"@type": "Person", "name": "Paula Rubio"},
        "recipeYield": r["raciones"],
        "totalTime": r["tiempo"],
        "recipeCategory": "Merienda" if "Merienda" in r["momento"] else "Bebida",
        "recipeCuisine": "Española",
        "recipeIngredient": [" ".join(x for x in (c, n) if x) for n, c, _ in r["ingredientes"]],
        "recipeInstructions": [{"@type": "HowToStep", "text": s} for s in r["pasos"]],
    }
    ingr = "".join(
        f'<li style="display:flex;justify-content:space-between;gap:16px;padding:12px 0;border-bottom:1px solid #e7dfc9">'
        f'<span>{E(n)}</span><span style="text-align:right;color:#7a7668;white-space:nowrap">{E(c)}'
        + (f'<br><span style="font-size:13px">{E(h)}</span>' if h else "")
        + "</span></li>"
        for n, c, h in r["ingredientes"]
    )
    pasos = "".join(
        f'<li style="display:grid;grid-template-columns:34px 1fr;gap:12px;padding:12px 0">'
        f'<span style="font-family:\'Cormorant Garamond\',serif;font-size:28px;line-height:1;color:#a98a4a">{i}</span>'
        f"<span>{E(s)}</span></li>"
        for i, s in enumerate(r["pasos"], 1)
    )
    boton = "display:inline-flex;align-items:center;justify-content:center;font-family:'Jost',sans-serif;font-size:13px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;padding:16px 30px;border-radius:2px;transition:all .25s"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(r['seo_titulo'])} | Paula Rubio</title>
<meta name="description" content="{E(r['descripcion'])}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Paula Rubio Nutricionista">
<meta property="og:locale" content="es_ES">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{E(r['titulo'])}">
<meta property="og:description" content="{E(r['descripcion'])}">
<meta property="og:image" content="{img}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
{estilos}
<style>@media(max-width:900px){{[data-receta]{{grid-template-columns:1fr!important}}[data-receta-img]{{aspect-ratio:4/3!important}}}}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{UMAMI}
</head>
<body>

{cabecera}

<main>
<section data-sec style="background:#faf6ec;padding:clamp(36px,6vw,90px) clamp(22px,5vw,72px)">
  <div data-receta style="max-width:1180px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:clamp(28px,5vw,68px);align-items:center">
    <div>
      <span style="font-family:'Jost',sans-serif;font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:#a98a4a">Receta · {E(r['momento'])}</span>
      <h1 style="font-family:'Cormorant Garamond',serif;font-weight:600;line-height:1.05;font-size:clamp(36px,4.4vw,64px);color:#5e1a24;margin-top:14px">{E(r['titulo'])}</h1>
      <div style="width:90px;height:1px;background:#c9b578;margin:22px 0"></div>
      <p style="font-family:'EB Garamond',serif;font-size:clamp(18px,1.5vw,22px);line-height:1.55;color:#4c4a40">{E(r['intro'])}</p>
      <p style="font-family:'Jost',sans-serif;font-weight:300;font-size:14px;letter-spacing:.06em;color:#7a7668;margin-top:18px">{E(r['raciones'])} · {E(r['tiempo_texto'])}</p>
    </div>
    <img src="/assets/planes/{r['foto']}.webp" alt="{E(r['titulo'])}" data-receta-img style="width:100%;height:auto;aspect-ratio:1/1;object-fit:cover;border-radius:6px;box-shadow:0 12px 28px rgba(60,50,30,.14)">
  </div>
</section>

<section data-sec style="background:#f5efe2;padding:clamp(44px,6vw,90px) clamp(22px,5vw,72px)">
  <div data-receta style="max-width:1080px;margin:0 auto;display:grid;grid-template-columns:0.85fr 1.15fr;gap:clamp(30px,5vw,64px);align-items:start;font-family:'Jost',sans-serif;font-weight:300;font-size:16px;line-height:1.65;color:#4c4a40">
    <div>
      <h2 style="font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(28px,3vw,38px);color:#3c3b34;margin-bottom:10px">Ingredientes</h2>
      <ul style="list-style:none">{ingr}</ul>
    </div>
    <div>
      <h2 style="font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(28px,3vw,38px);color:#3c3b34;margin-bottom:10px">Cómo se hace</h2>
      <ol style="list-style:none">{pasos}</ol>
      <p style="margin-top:18px;padding:18px 20px;background:#faf6ec;border-left:2px solid #c9b578;border-radius:2px">{E(r['nota'])}</p>
    </div>
  </div>
</section>

<section data-sec style="background:#5e1a24;padding:clamp(48px,6vw,88px) clamp(22px,5vw,72px)">
  <div style="max-width:760px;margin:0 auto;text-align:center;color:#f7f1e6">
    <span style="font-family:'Jost',sans-serif;font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:#d9c48f">Esta receta es de mi plan</span>
    <h2 style="font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(32px,3.6vw,48px);line-height:1.1;margin-top:14px">{E(p['nombre'])}</h2>
    <p style="font-family:'EB Garamond',serif;font-size:clamp(18px,1.5vw,21px);line-height:1.55;margin-top:18px;color:#efe6d3">{E(r['en_el_plan'])} {E(p['resumen'])}</p>
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin-top:30px">
      <a href="{p['tienda']}" data-umami-event="{p['evento']}" data-umami-event-origen="receta-{r['slug']}" target="_blank" rel="noopener" data-hover="background:#f7f1e6;color:#5e1a24" style="{boton};background:#d9c48f;color:#3c2a12">Comprar el plan · 39,99 €</a>
      <a href="{p['pagina']}" data-hover="border-color:#f7f1e6" style="{boton};border:1px solid #b9937a;color:#f7f1e6">Ver qué incluye</a>
    </div>
  </div>
</section>
</main>

{pie}
"""


def main():
    estilos, cabecera, pie = plantilla()
    for r in RECETAS:
        d = os.path.join(ROOT, "recetas", r["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(pagina(r, estilos, cabecera, pie))
        print("ok", r["slug"])


if __name__ == "__main__":
    main()

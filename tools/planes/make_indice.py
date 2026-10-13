"""Genera /planes/index.html: la página para elegir plan según lo que quieres conseguir.

Uso: python3 tools/planes/make_indice.py
Reutiliza los estilos, la cabecera y el pie de la página del plan del ciclo, como las recetas.
Para añadir un plan nuevo, añade una entrada a PLANES y vuelve a ejecutarlo.
"""
import html
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "recetas"))
from make_recetas import ROOT, SITE, UMAMI, plantilla  # noqa: E402

E = html.escape

PLANES = [
    {
        "para": "Quiero comer según mi ciclo",
        "nombre": "Come según tu ciclo",
        "pagina": "/planes/come-segun-tu-ciclo/",
        "tienda": "https://nutriaplans.com/plan-store/come-segun-tu-ciclo",
        "evento": "comprar-ciclo",
        "foto": "46efbd82-da71-467f-8074-0579563f8faa",
        "alt": "Estofado de ternera con boniato y remolacha",
        "texto": "La comida ordenada por el día de tu ciclo. Cuchara y cosas calientes en la regla, crudo y verde en la fase folicular, y postre real todos los días en la lútea.",
        "puntos": ["Con la guía completa del plan", "Te sirve también para perder peso"],
    },
    {
        "para": "Quiero cuidar mi piel",
        "nombre": "Glow, piel luminosa desde dentro",
        "pagina": "/planes/glow/",
        "tienda": "https://nutriaplans.com/plan-store/glow-piel-luminosa-desde-dentro",
        "evento": "comprar-glow",
        "foto": "37793bec-6f56-455e-ad92-1e6d8d0a0fdc",
        "alt": "Tartar de salmón y aguacate con mango",
        "texto": "Una semana para cada cosa que necesita tu piel: colágeno, barrera, minerales y color. Cada receta lleva su porqué.",
        "puntos": ["Shots y meriendas pensados para la piel", "Con el porqué de cada receta"],
    },
]

INCLUYEN = [
    ("Tres comidas y merienda", "Cada día, con una opción recomendada y alternativas para cambiar."),
    ("La lista de la compra", "Semana a semana, para ir al súper una vez."),
    ("Recetas paso a paso", "Cada plato con su receta y sus pasos, dentro de la app."),
    ("Un asistente en la app", "Te ajusta las cantidades a ti y te ayuda si un día no encuentras algo."),
]

BOTON = "display:inline-flex;align-items:center;justify-content:center;font-family:'Jost',sans-serif;font-size:12.5px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;padding:15px 22px;border-radius:2px;transition:all .25s"


def tarjeta(p):
    puntos = "".join(
        f'<li style="padding-left:18px;position:relative"><span style="position:absolute;left:0;color:#a98a4a">·</span>{E(x)}</li>'
        for x in p["puntos"]
    )
    return f"""
      <article style="background:#faf6ec;border:1px solid #e7dfc9;border-radius:5px;overflow:hidden;display:flex;flex-direction:column">
        <a href="{p['pagina']}" style="display:block"><img src="/assets/planes/{p['foto']}.webp" alt="{E(p['alt'])}" loading="lazy" style="width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;display:block"></a>
        <div style="padding:26px 26px 28px;display:flex;flex-direction:column;gap:12px;flex:1">
          <span style="font-family:'Jost',sans-serif;font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:#a98a4a">{E(p['para'])}</span>
          <h2 style="font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(26px,2.4vw,32px);line-height:1.1;color:#5e1a24">{E(p['nombre'])}</h2>
          <p style="font-family:'Jost',sans-serif;font-weight:300;font-size:15.5px;line-height:1.65;color:#5c5a4f">{E(p['texto'])}</p>
          <ul style="list-style:none;font-family:'Jost',sans-serif;font-weight:300;font-size:14.5px;line-height:1.7;color:#5c5a4f">{puntos}</ul>
          <p style="font-family:'Cormorant Garamond',serif;font-weight:500;font-size:26px;color:#6f7a4d;margin-top:auto;padding-top:8px">39,99 € <span style="font-family:'Jost',sans-serif;font-weight:300;font-size:13px;letter-spacing:.06em;color:#7a7668">· 4 semanas</span></p>
          <div style="display:flex;flex-wrap:wrap;gap:10px">
            <a href="{p['tienda']}" data-umami-event="{p['evento']}" data-umami-event-origen="pagina-planes" target="_blank" rel="noopener" data-hover="background:#6f7a4d" style="{BOTON};background:#5e1a24;color:#f7f1e6">Comprar</a>
            <a href="{p['pagina']}" data-hover="border-color:#5e1a24" style="{BOTON};border:1px solid #c9b578;color:#5e1a24">Ver qué incluye</a>
          </div>
        </div>
      </article>"""


def pagina(estilos, cabecera, pie):
    url = f"{SITE}/planes/"
    img = f"{SITE}/assets/planes/{PLANES[0]['foto']}.jpg"
    titulo = "Planes de nutrición de 4 semanas"
    desc = "Planes de 4 semanas ya hechos, con recetas, lista de la compra y un asistente que te ajusta las cantidades. Elige por lo que quieres conseguir."
    tarjetas = "".join(tarjeta(p) for p in PLANES)
    incluyen = "".join(
        f'<div style="background:#faf6ec;border:1px solid #e7dfc9;border-radius:5px;padding:22px 22px 24px">'
        f'<h3 style="font-family:\'Cormorant Garamond\',serif;font-weight:500;font-size:22px;line-height:1.15;color:#3c3b34">{E(t)}</h3>'
        f'<p style="font-family:\'Jost\',sans-serif;font-weight:300;font-size:14.5px;line-height:1.65;color:#5c5a4f;margin-top:8px">{E(d)}</p></div>'
        for t, d in INCLUYEN
    )
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(titulo)} | Paula Rubio</title>
<meta name="description" content="{E(desc)}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Paula Rubio Nutricionista">
<meta property="og:locale" content="es_ES">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{E(titulo)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{img}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
{estilos}
<style>@media(max-width:900px){{[data-elige]{{grid-template-columns:1fr!important}}[data-incluyen]{{grid-template-columns:1fr 1fr!important}}}}@media(max-width:560px){{[data-incluyen]{{grid-template-columns:1fr!important}}}}</style>
{UMAMI}
</head>
<body>

{cabecera}

<main>
<section data-sec style="background:#faf6ec;padding:clamp(40px,6vw,88px) clamp(22px,5vw,72px) clamp(30px,4vw,52px)">
  <div style="max-width:780px;margin:0 auto;text-align:center">
    <span style="font-family:'Jost',sans-serif;font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:#a98a4a">Planes de 4 semanas</span>
    <h1 style="font-family:'Cormorant Garamond',serif;font-weight:600;line-height:1.05;font-size:clamp(36px,4.4vw,60px);color:#5e1a24;margin-top:14px">¿Qué quieres trabajar?</h1>
    <div style="width:90px;height:1px;background:#c9b578;margin:22px auto"></div>
    <p style="font-family:'EB Garamond',serif;font-size:clamp(18px,1.5vw,22px);line-height:1.55;color:#4c4a40">Elige por lo que quieres conseguir. Lo compras, te instalas Nutria y empiezas hoy. El asistente te ajusta las cantidades a ti, y si quieres perder peso, también las calorías.</p>
  </div>
</section>

<section data-sec style="background:#faf6ec;padding:0 clamp(22px,5vw,72px) clamp(48px,6vw,90px)">
  <div data-elige style="max-width:1080px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:clamp(18px,2.4vw,30px)">{tarjetas}
  </div>
</section>

<section data-sec style="background:#f5efe2;padding:clamp(44px,6vw,86px) clamp(22px,5vw,72px)">
  <div style="max-width:1080px;margin:0 auto">
    <h2 style="font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(30px,3.2vw,42px);line-height:1.1;color:#3c3b34;text-align:center;margin-bottom:clamp(24px,3vw,38px)">Todos los planes llevan</h2>
    <div data-incluyen style="display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(14px,2vw,22px)">{incluyen}</div>
  </div>
</section>

<section data-sec style="background:#5e1a24;padding:clamp(48px,6vw,88px) clamp(22px,5vw,72px)">
  <div style="max-width:720px;margin:0 auto;text-align:center;color:#f7f1e6">
    <span style="font-family:'Jost',sans-serif;font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:#d9c48f">Si prefieres uno hecho para ti</span>
    <h2 style="font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(32px,3.6vw,46px);line-height:1.1;margin-top:14px">Plan a medida, desde 69 €</h2>
    <p style="font-family:'EB Garamond',serif;font-size:clamp(18px,1.5vw,21px);line-height:1.55;margin-top:18px;color:#efe6d3">Rellenas mi cuestionario con tu historia, tus horarios, lo que te gusta y tu analítica si la tienes, y en 5 días tienes tu plan de 4 semanas en la app. Sin videollamada.</p>
    <a href="mailto:hola@paularubionutricionista.com?subject=Plan%20a%20medida" data-umami-event="contacto-plan-medida" data-hover="background:#f7f1e6;color:#5e1a24" style="{BOTON};margin-top:28px;background:#d9c48f;color:#3c2a12;padding:16px 30px">Escríbeme</a>
  </div>
</section>
</main>

{pie}
"""


def main():
    estilos, cabecera, pie = plantilla()
    d = os.path.join(ROOT, "planes")
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(pagina(estilos, cabecera, pie))
    print("ok planes/index.html")


if __name__ == "__main__":
    main()

# Fabrica las páginas de tripulaciones (ES y EN) a partir de la cabecera y el pie de la web.
# Uso: python3 tools/crew/build.py  (desde la raíz del repositorio)
import json, re, html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = "https://paularubionutricionista.com"
NUTRIA = "https://nutriaplans.com/marketplace/paufly"

glow = (ROOT / "planes/glow/index.html").read_text()
en_home = (ROOT / "en/index.html").read_text()

STYLE = re.search(r"<style>\s*\*\{box-sizing.*?</style>", glow, re.S).group(0)
EXTRA = """<style>
@media(max-width:900px){[data-topics]{grid-template-columns:1fr 1fr!important}[data-rules]{grid-template-columns:1fr!important}}
@media(max-width:640px){[data-topics]{grid-template-columns:1fr!important}[data-cover]{max-width:250px!important}}
details summary{cursor:pointer;list-style:none}
details summary::-webkit-details-marker{display:none}
details[open] summary span:last-child{transform:rotate(45deg)}
</style>"""
UMAMI = """<script>try{if(/[?&]soy-paula/.test(location.search))localStorage.setItem("umami.disabled","1")}catch(e){}</script>
<script defer src="https://cloud.umami.is/script.js" data-website-id="21a20c4a-cd36-44e3-bc6b-2af2bde813e7"></script>"""
FORM_JS = """<script>
document.querySelectorAll("[data-guide-form]").forEach(function(f){
  var msg=f.querySelector("[data-msg]"),btn=f.querySelector("button"),label=btn.textContent;
  function say(t,bad){msg.textContent=t;msg.style.color=bad?"#a3402f":"#5e1a24"}
  f.addEventListener("submit",function(e){
    e.preventDefault();
    var email=f.querySelector("[name=EMAIL]");
    if(!email.value||!email.checkValidity()){say(f.dataset.errEmail,1);email.focus();return}
    if(!f.querySelector("[data-consent]").checked){say(f.dataset.errConsent,1);return}
    if(f.querySelector("[name=email_address_check]").value)return;
    btn.disabled=true;btn.textContent=f.dataset.sending;say("");
    fetch(f.action+"?isAjax=1",{method:"POST",body:new FormData(f)})
      .then(function(r){return r.json().catch(function(){return{}})})
      .then(function(d){
        if(d&&d.success){f.querySelector("div").style.display="none";f.querySelector("[data-consent]").closest("label").style.display="none";say(f.dataset.ok);try{window.umami&&umami.track(f.dataset.umami)}catch(x){}}
        else if(d&&d.errors&&d.errors.EMAIL){say(f.dataset.errEmail,1)}
        else{say(f.dataset.err,1)}
      })
      .catch(function(){say(f.dataset.err,1)})
      .finally(function(){btn.disabled=false;btn.textContent=label});
  });
});
</script>"""


def block(src, start, end):
    return src[src.index(start): src.index(end) + len(end)]

# Cabecera y pie en castellano (los de las páginas de plan), con el EN apuntando a la página gemela
ES_HEADER = block(glow, "<header", "</header>").replace('href="/en/"', 'href="/en/cabin-crew/"')
ES_FOOTER = block(glow, "<footer", "</footer>")

# Cabecera y pie en inglés (los de la home EN), con anclas absolutas y el ES apuntando a la gemela
EN_HEADER = block(en_home, "<header", "</header>")
EN_FOOTER = block(en_home, "<footer", "</footer>")
for frag in ("inicio", "sobre-mi", "servicios", "planes", "contacto"):
    EN_HEADER = EN_HEADER.replace(f'href="#{frag}"', f'href="/en/#{frag}"')
    EN_FOOTER = EN_FOOTER.replace(f'href="#{frag}"', f'href="/en/#{frag}"')
EN_HEADER = EN_HEADER.replace('href="/"', 'href="/tripulaciones/"')

F_JOST = "font-family:'Jost',sans-serif"
F_COR = "font-family:'Cormorant Garamond',serif"
F_EB = "font-family:'EB Garamond',serif"
BTN = (f"display:inline-flex;align-items:center;justify-content:center;background:#5e1a24;color:#f7f1e6;{F_JOST};"
       "font-size:13px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;padding:16px 32px;border-radius:2px;transition:background .25s")
BTN2 = (f"display:inline-flex;align-items:center;justify-content:center;background:transparent;color:#3c3b34;border:1px solid #b7a882;{F_JOST};"
        "font-size:13px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;padding:15px 31px;border-radius:2px;transition:all .25s")
EYEBROW = f"{F_JOST};font-size:13px;letter-spacing:.32em;text-transform:uppercase;color:#a98a4a"
H2 = f"{F_COR};font-weight:500;font-size:clamp(30px,3.4vw,46px);line-height:1.1;color:#3c3b34"
BODY = f"{F_JOST};font-weight:300;font-size:clamp(15px,1.2vw,17px);line-height:1.75;color:#5c5a4f"
CARD = "background:#faf6ec;border:1px solid #e7dfc9;border-radius:5px;padding:24px 22px 26px;display:flex;flex-direction:column;gap:10px"
SEC_A = "background:#faf6ec;padding:clamp(54px,7vw,98px) clamp(22px,5vw,72px)"
SEC_B = "background:#f5efe2;padding:clamp(54px,7vw,98px) clamp(22px,5vw,72px)"


def page(t):
    url = SITE + t["path"]
    faq_ld = {
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]],
    }
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": url + "#pagina",
                "url": url,
                "name": t["title"],
                "description": t["desc"],
                "inLanguage": t["lang"],
                "isPartOf": {"@id": SITE + "/#negocio"},
                "about": t["about"],
                "audience": {"@type": "Audience", "audienceType": t["audience"]},
                "primaryImageOfPage": SITE + t["cover"],
                "author": {"@id": SITE + "/#paula"},
            },
            {
                "@type": "DigitalDocument",
                "name": t["doc_name"],
                "encodingFormat": "application/pdf",
                "inLanguage": t["lang"],
                "isAccessibleForFree": True,
                "author": {"@id": SITE + "/#paula"},
            },
            {
                "@type": "Person",
                "@id": SITE + "/#paula",
                "name": "Paula Rubio",
                "jobTitle": t["job"],
                "url": SITE + "/",
                "sameAs": ["https://www.instagram.com/yummy_rainbows/", NUTRIA],
            },
            faq_ld,
        ],
    }
    es_url, en_url = SITE + "/tripulaciones/", SITE + "/en/cabin-crew/"
    head = f"""<!DOCTYPE html>
<html lang="{t['lang']}">
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
<meta property="og:title" content="{html.escape(t['og_title'])}">
<meta property="og:description" content="{html.escape(t['desc'])}">
<meta property="og:image" content="{SITE}{t['og_image']}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(t['og_title'])}">
<meta name="twitter:description" content="{html.escape(t['desc'])}">
<meta name="twitter:image" content="{SITE}{t['og_image']}">
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
    topics = "".join(
        f'<div style="{CARD}"><span style="{F_JOST};font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:#a98a4a">{i+1:02d}</span>'
        f'<h3 style="{F_COR};font-weight:500;font-size:27px;line-height:1.12;color:#5e1a24">{h}</h3>'
        f'<p style="{F_JOST};font-weight:300;font-size:15px;line-height:1.65;color:#5c5a4f">{p}</p></div>'
        for i, (h, p) in enumerate(t["topics"])
    )
    rules = "".join(
        f'<div style="{CARD};background:#f5efe2"><h3 style="{F_COR};font-weight:500;font-size:30px;line-height:1.1;color:#5e1a24">{h}</h3>'
        f'<p style="{F_JOST};font-weight:300;font-size:16px;line-height:1.7;color:#5c5a4f">{p}</p></div>'
        for h, p in t["rules"]
    )
    steps = "".join(
        f'<div style="{CARD}"><span style="{F_JOST};font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:#a98a4a">{i+1}</span>'
        f'<h3 style="{F_COR};font-weight:500;font-size:28px;line-height:1.1;color:#5e1a24">{h}</h3>'
        f'<p style="{F_JOST};font-weight:300;font-size:15px;line-height:1.65;color:#5c5a4f">{p}</p></div>'
        for i, (h, p) in enumerate(t["steps"])
    )
    faq = "".join(
        f'<details style="border-bottom:1px solid #e4dcc7;padding:20px 0"><summary style="display:flex;justify-content:space-between;gap:20px;align-items:center">'
        f'<span style="{F_COR};font-weight:500;font-size:clamp(21px,1.9vw,26px);color:#3c3b34">{q}</span>'
        f'<span aria-hidden="true" style="{F_JOST};font-size:24px;color:#a98a4a;transition:transform .2s">+</span></summary>'
        f'<p style="{BODY};margin-top:12px">{a}</p></details>'
        for q, a in t["faq"]
    )
    main = f"""<main>
<section id="guia" data-sec style="{SEC_A}">
  <div data-about style="max-width:1240px;margin:0 auto;display:grid;grid-template-columns:1.15fr 0.85fr;gap:clamp(34px,5vw,72px);align-items:center">
    <div>
      <span style="{EYEBROW}">{t['eyebrow']}</span>
      <h1 style="{F_COR};font-weight:600;line-height:1.04;font-size:clamp(40px,4.6vw,70px);color:#5e1a24;margin-top:18px">{t['h1']}</h1>
      <div style="width:90px;height:1px;background:#c9b578;margin:26px 0"></div>
      <p style="{F_EB};font-size:clamp(19px,1.6vw,24px);line-height:1.5;color:#4c4a40">{t['lead']}</p>
      <p style="{BODY};margin-top:16px">{t['intro']}</p>
      <!-- Formulario: manda el correo a la lista de Brevo y Brevo envía la guía con una automatización -->
      <form id="pedir-guia" data-guide-form action="{t['form_action']}" method="post" novalidate
        data-umami="{t['event']}" data-sending="{html.escape(t['sending'])}" data-ok="{html.escape(t['ok'])}"
        data-err-email="{html.escape(t['err_email'])}" data-err-consent="{html.escape(t['err_consent'])}" data-err="{html.escape(t['err'])}"
        style="margin-top:32px;max-width:560px">
        <label for="guia-email" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">{t['email_label']}</label>
        <div style="display:flex;flex-wrap:wrap;gap:12px">
          <input id="guia-email" type="email" name="EMAIL" required autocomplete="email" placeholder="{t['email_ph']}"
            style="flex:1 1 240px;min-width:0;{F_JOST};font-size:16px;color:#3c3b34;background:#fffdf7;border:1px solid #b7a882;border-radius:2px;padding:15px 16px">
          <button type="submit" data-hover="background:#6f7a4d;color:#f7f1e6" style="{BTN};border:0;cursor:pointer">{t['cta']}</button>
        </div>
        <input type="text" name="email_address_check" value="" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-5000px">
        <input type="hidden" name="locale" value="{t['lang']}">
        <label style="display:flex;gap:10px;align-items:flex-start;margin-top:14px;{F_JOST};font-weight:300;font-size:14px;line-height:1.55;color:#5c5a4f;cursor:pointer">
          <input type="checkbox" data-consent required style="margin-top:3px;accent-color:#5e1a24;width:16px;height:16px;flex:none">
          <span>{t['consent']}</span>
        </label>
        <p data-msg role="status" aria-live="polite" style="{F_JOST};font-size:15px;line-height:1.55;color:#5e1a24;margin-top:12px"></p>
      </form>
      <p style="{F_JOST};font-weight:300;font-size:14px;color:#8a8470;margin-top:10px">{t['note']} <a href="{t['other_url']}" hreflang="{t['other_lang']}" style="color:#5e1a24;border-bottom:1px solid #c9b578">{t['other_cta']}</a></p>
    </div>
    <a data-cover href="#pedir-guia" aria-label="{t['cta']}" style="display:block;max-width:420px;justify-self:center">
      <img src="{t['cover']}" alt="{t['cover_alt']}" width="700" height="989" style="width:100%;height:auto;border-radius:4px;box-shadow:0 16px 36px rgba(60,50,30,.18)">
    </a>
  </div>
</section>

<section data-sec style="{SEC_B}">
  <div style="max-width:1240px;margin:0 auto">
    <h2 style="{H2};text-align:center">{t['topics_h2']}</h2>
    <p style="{BODY};text-align:center;max-width:62ch;margin:16px auto clamp(30px,4vw,48px)">{t['topics_p']}</p>
    <div data-topics style="display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(16px,2vw,24px)">{topics}</div>
  </div>
</section>

<section data-sec style="{SEC_A}">
  <div style="max-width:1240px;margin:0 auto">
    <h2 style="{H2};text-align:center">{t['rules_h2']}</h2>
    <p style="{BODY};text-align:center;max-width:62ch;margin:16px auto clamp(30px,4vw,48px)">{t['rules_p']}</p>
    <div data-rules style="display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(16px,2vw,24px)">{rules}</div>
  </div>
</section>

<section data-sec style="{SEC_B}">
  <div data-about style="max-width:1240px;margin:0 auto;display:grid;grid-template-columns:0.8fr 1.2fr;gap:clamp(34px,5vw,72px);align-items:center">
    <img src="/assets/paula-sitting.webp" alt="{t['photo_alt']}" loading="lazy" style="width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:6px;box-shadow:0 12px 28px rgba(60,50,30,.14)">
    <div>
      <span style="{EYEBROW}">{t['about_eyebrow']}</span>
      <h2 style="{H2};margin-top:16px">{t['about_h2']}</h2>
      <div style="width:90px;height:1px;background:#c9b578;margin:24px 0"></div>
      {''.join(f'<p style="{BODY};margin-top:14px">{p}</p>' for p in t['about_ps'])}
    </div>
  </div>
</section>

<section data-sec style="{SEC_A}">
  <div style="max-width:1240px;margin:0 auto">
    <h2 style="{H2};text-align:center">{t['steps_h2']}</h2>
    <p style="{BODY};text-align:center;max-width:62ch;margin:16px auto clamp(30px,4vw,48px)">{t['steps_p']}</p>
    <div data-rules style="display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(16px,2vw,24px)">{steps}</div>
    <div style="display:flex;flex-wrap:wrap;gap:16px;justify-content:center;margin-top:36px">
      <a href="{NUTRIA}" data-umami-event="perfil-nutria" target="_blank" rel="noopener" data-hover="background:#6f7a4d;color:#f7f1e6" style="{BTN}">{t['book']}</a>
      <a href="mailto:hola@paularubionutricionista.com" data-hover="border-color:#5e1a24;color:#5e1a24" style="{BTN2}">{t['write']}</a>
    </div>
    <p style="{BODY};text-align:center;max-width:60ch;margin:34px auto 0">{t['diagnoseum']}</p>
  </div>
</section>

<section data-sec style="{SEC_B}">
  <div style="max-width:860px;margin:0 auto">
    <h2 style="{H2};text-align:center;margin-bottom:clamp(20px,3vw,34px)">{t['faq_h2']}</h2>
    {faq}
  </div>
</section>
</main>
"""
    header = ES_HEADER if t["lang"] == "es" else EN_HEADER
    footer = ES_FOOTER if t["lang"] == "es" else EN_FOOTER
    out = head + "\n" + header + "\n\n" + main + "\n" + footer + '\n\n<script src="/script.js"></script>\n' + FORM_JS + '\n</body>\n</html>\n'
    dest = ROOT / t["path"].strip("/") / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out)
    print("ok", dest.relative_to(ROOT))


from content import ES, EN  # noqa: E402

page(ES)
page(EN)

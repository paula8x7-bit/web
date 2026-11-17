# Correos de la guía de tripulaciones (Brevo). Genera el HTML de cada uno en tools/crew/emails/.
from pathlib import Path

ES_PDF = "https://drive.google.com/file/d/1AtvnL80xOb6unagv8N3nZI5C-A5iuFeM/view"
EN_PDF = "https://drive.google.com/file/d/1z3mIxF06HfiV-UheMdgpkJjOCa0ow3wR/view"
NUTRIA = "https://nutriaplans.com/marketplace/paufly"

EMAILS = {
    "es-1-guia": {
        "subject": "Tu guía para tripulaciones de largo radio",
        "preheader": "Aquí la tienes, para leerla en la próxima escala.",
        "paras": [
            "Hola:",
            "Aquí tienes la guía para tripulaciones de largo radio.",
            ("btn", "Descargar la guía", ES_PDF),
            "Es la que uso yo. Si vas justo de tiempo, empieza por la página del jet lag según a qué hora aterrices: es la que antes se nota.",
            "Si te surge cualquier duda, contesta a este correo. Lo leo yo.",
            "Buen vuelo, y nos vemos en la sala de firmas.",
            "Paula",
        ],
        "footer": 'Recibes este correo porque te descargaste la guía en paularubionutricionista.com. <a href="{{ unsubscribe }}" style="color:#8a8470">Darme de baja</a>.',
    },
    "es-2-seguimiento": {
        "subject": "¿Qué tal la última rotación?",
        "preheader": "Me encantaría saber qué te ha funcionado.",
        "paras": [
            "Hola:",
            "Hace unos días te mandé la guía para tripulaciones. ¿Te ha dado tiempo a probar algo en tu última rotación?",
            "Me encantaría saber qué te ha funcionado y qué no. Contéstame a este correo, aunque sea con una línea.",
            "Y si quieres que adaptemos todo esto a tu roster, a tu analítica y a cómo te encuentras, lo vemos en consulta. Trabajo online, en castellano y en inglés.",
            ("btn", "Reservar consulta", NUTRIA),
            f'Por si se te perdió, <a href="{ES_PDF}" style="color:#5e1a24">aquí tienes otra vez la guía</a>.',
            "Un abrazo,",
            "Paula",
        ],
        "footer": 'Recibes este correo porque te descargaste la guía en paularubionutricionista.com. <a href="{{ unsubscribe }}" style="color:#8a8470">Darme de baja</a>.',
    },
    "en-1-guide": {
        "subject": "Your long-haul crew guide",
        "preheader": "Here it is, ready for your next layover.",
        "paras": [
            "Hi,",
            "Here's your guide for long-haul crew.",
            ("btn", "Download the guide", EN_PDF),
            "It's the one I use myself. If you're short on time, start with the jet lag page by arrival time. It's the one you'll notice first.",
            "If you have any questions, just reply to this email. I read every reply myself.",
            "Have a good flight, and see you at report.",
            "Paula",
        ],
        "footer": 'You\'re getting this email because you downloaded the guide at paularubionutricionista.com. <a href="{{ unsubscribe }}" style="color:#8a8470">Unsubscribe</a>.',
    },
    "en-2-follow-up": {
        "subject": "How was your last trip?",
        "preheader": "I'd love to hear what worked for you.",
        "paras": [
            "Hi,",
            "A few days ago I sent you the crew guide. Have you had a chance to try anything on your last trip?",
            "I'd love to hear what worked for you and what didn't. Just hit reply, even a line is enough.",
            "And if you'd like to tailor all of this to your roster, your blood tests and how you feel, we can do that in a consultation. I work online, in English and Spanish.",
            ("btn", "Book a consultation", NUTRIA),
            f'In case you lost it, <a href="{EN_PDF}" style="color:#5e1a24">here\'s the guide again</a>.',
            "Speak soon,",
            "Paula",
        ],
        "footer": 'You\'re getting this email because you downloaded the guide at paularubionutricionista.com. <a href="{{ unsubscribe }}" style="color:#8a8470">Unsubscribe</a>.',
    },
}


def render(e, lang):
    rows = []
    for p in e["paras"]:
        if isinstance(p, tuple):
            _, label, url = p
            rows.append(
                f'<tr><td style="padding:8px 0 22px"><a href="{url}" style="display:inline-block;background:#5e1a24;color:#f7f1e6;'
                f'font-family:Arial,Helvetica,sans-serif;font-size:14px;letter-spacing:.12em;text-transform:uppercase;text-decoration:none;'
                f'padding:14px 28px;border-radius:2px">{label}</a></td></tr>'
            )
        else:
            rows.append(f'<tr><td style="padding:0 0 16px;font-family:Georgia,serif;font-size:17px;line-height:1.6;color:#3c3b34">{p}</td></tr>')
    return f"""<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e['subject']}</title></head>
<body style="margin:0;padding:0;background:#f5efe2">
<div style="display:none;max-height:0;overflow:hidden">{e['preheader']}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f5efe2"><tr><td align="center" style="padding:32px 16px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;background:#faf6ec;border:1px solid #e7dfc9;border-radius:6px">
<tr><td style="padding:32px 32px 8px"><img src="https://paularubionutricionista.com/assets/firma-email.png" alt="Paula Rubio" width="140" style="display:block;width:140px;height:auto"></td></tr>
<tr><td style="padding:16px 32px 16px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">{''.join(rows)}</table></td></tr>
</table>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:560px"><tr><td style="padding:18px 32px;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.6;color:#8a8470;text-align:center">
Paula Rubio Nutricionista · hola@paularubionutricionista.com<br>{e['footer']}</td></tr></table>
</td></tr></table>
</body></html>"""


out = Path(__file__).parent / "emails"
out.mkdir(exist_ok=True)
for key, e in EMAILS.items():
    (out / f"{key}.html").write_text(render(e, key[:2]))
    print(key, "|", e["subject"])

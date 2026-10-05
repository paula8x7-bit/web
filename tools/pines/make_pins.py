"""Descarga las fotos de los platos desde Nutria y fabrica los pines de Pinterest.

Lo ejecuta la acción de GitHub "Pines" (.github/workflows/pines.yml).
Salida:
  assets/planes/<foto>.jpg   fotos para las páginas de cada plan (900 px)
  assets/pines/<slug>.jpg     pines verticales 1000 x 1500
  pines/index.html            galería de pines (no indexada) para guardarlos en Pinterest
"""
import io
import json
import os
import sys
import time
import urllib.request

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = json.load(open(os.path.join(os.path.dirname(__file__), "data.json"), encoding="utf-8"))
FONTS = os.environ.get("PIN_FONTS", os.path.join(os.path.dirname(__file__), "fonts"))
SRC = "https://nutriaplans.com/uploads/dish-images/"

CREAM, BURGUNDY, OLIVE, GOLD, GREY = "#f5efe2", "#5e1a24", "#6f7a4d", "#a98a4a", "#8a8470"


def font(name, size, weight):
    f = ImageFont.truetype(os.path.join(FONTS, name), size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


def fetch(file):
    # Nutria limita las descargas seguidas: espera entre fotos y reintenta con calma.
    last = None
    for wait in (2, 10, 30):
        time.sleep(wait)
        try:
            req = urllib.request.Request(SRC + file, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return Image.open(io.BytesIO(r.read())).convert("RGB")
        except Exception as e:
            last = e
    raise last


def square(img, size):
    w, h = img.size
    s = min(w, h)
    img = img.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))
    return img.resize((size, size), Image.LANCZOS)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=fnt) <= width:
            cur = test
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def spaced(draw, xy, text, fnt, fill, tracking):
    x, y = xy
    total = sum(draw.textlength(c, font=fnt) for c in text) + tracking * (len(text) - 1)
    x = x - total / 2
    for c in text:
        draw.text((x, y), c, font=fnt, fill=fill)
        x += draw.textlength(c, font=fnt) + tracking


def make_pin(photo, pin):
    W, H, P = 1000, 1500, 1000
    canvas = Image.new("RGB", (W, H), CREAM)
    canvas.paste(square(photo, P), (0, 0))
    d = ImageDraw.Draw(canvas)
    eb = font("Jost.ttf", 26, 500)
    spaced(d, (W / 2, P + 52), pin["eyebrow"].upper(), eb, GOLD, 6)
    d.line((W / 2 - 40, P + 102, W / 2 + 40, P + 102), fill="#c9b578", width=2)
    size = 78
    while True:
        tf = font("CormorantGaramond.ttf", size, 600)
        lines = wrap(d, pin["title"], tf, W - 140)
        if len(lines) <= 2 or size <= 56:
            break
        size -= 4
    sf = font("EBGaramond-Italic.ttf", 36, 400)
    sub_lines = wrap(d, pin["sub"], sf, W - 160)[:2]
    block = len(lines) * int(size * 1.02) + 14 + len(sub_lines) * 44
    y = P + 120 + max(0, ((H - 100) - (P + 120) - block) // 2)
    for line in lines:
        d.text((W / 2, y), line, font=tf, fill=BURGUNDY, anchor="ma")
        y += int(size * 1.02)
    for line in sub_lines:
        d.text((W / 2, y + 14), line, font=sf, fill=OLIVE, anchor="ma")
        y += 44
    ff = font("Jost.ttf", 22, 400)
    spaced(d, (W / 2, H - 52), "PAULARUBIONUTRICIONISTA.COM", ff, GREY, 4)
    return canvas


def main():
    os.makedirs(os.path.join(ROOT, "assets", "planes"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "assets", "pines"), exist_ok=True)
    planes = lambda f: os.path.join(ROOT, "assets", "planes", os.path.splitext(f)[0] + ".jpg")
    pin_out = lambda p: os.path.join(ROOT, "assets", "pines", p["slug"] + ".jpg")
    # Solo se descarga lo que falta: los pines y fotos ya fabricados no se tocan.
    todo = [p for p in DATA["pins"] if not os.path.exists(pin_out(p)) or os.environ.get("PIN_REBUILD")]
    files = {p["file"] for p in todo} | {g["file"] for gl in DATA["gallery"].values() for g in gl if not os.path.exists(planes(g["file"]))}
    photos, failed = {}, []
    for f in sorted(files):
        try:
            photos[f] = fetch(f)
        except Exception as e:
            print("No se pudo descargar", f, e, file=sys.stderr)
            failed.append(f"{f}: {e}")
            continue
        square(photos[f], 900).save(planes(f), "JPEG", quality=84, optimize=True, progressive=True)
    made = 0
    for pin in todo:
        if pin["file"] not in photos:
            continue
        make_pin(photos[pin["file"]], pin).save(pin_out(pin), "JPEG", quality=86, optimize=True, progressive=True)
        made += 1
    with open(os.path.join(ROOT, "pines", "resultado.txt"), "w", encoding="utf-8") as fh:
        fh.write(f"Pines nuevos: {made} de {len(todo)}\n" + "".join(x + "\n" for x in failed))
    cards = "\n".join(
        f'<figure><img src="/assets/pines/{p["slug"]}.jpg" alt="{p["pin_title"]}" data-pin-description="{p["pin_desc"]}" '
        f'data-pin-url="{p["link"]}" width="500" height="750" loading="lazy"><figcaption>{p["pin_title"]}</figcaption></figure>'
        for p in DATA["pins"] if os.path.exists(pin_out(p)))
    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex"><title>Pines · Paula Rubio Nutricionista</title>
<style>body{{background:#f5efe2;font-family:sans-serif;color:#3c3b34;margin:0;padding:24px}}
main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:20px;max-width:1200px;margin:0 auto}}
img{{width:100%;height:auto;display:block}}figcaption{{font-size:13px;margin-top:6px}}</style></head>
<body><main>
{cards}
</main></body></html>
"""
    os.makedirs(os.path.join(ROOT, "pines"), exist_ok=True)
    open(os.path.join(ROOT, "pines", "index.html"), "w", encoding="utf-8").write(html)
    print(made, "pines nuevos;", len(failed), "fotos sin descargar")


if __name__ == "__main__":
    main()

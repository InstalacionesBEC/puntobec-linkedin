"""Genera la imagen de una publicación de PuntoBEC (PNG 1080x1350, formato 4:5 para el feed de LinkedIn).

Uso:
    python tarjeta.py entrada.json salida.png

entrada.json (UTF-8):
{
  "estilo": "titular" | "lista" | "comparacion" | "dato",
  "etiqueta": "HÁBITOS",                      # categoría corta (máx. ~20 car.)
  "titular": "Frase principal del post",      # 4-14 palabras
  "puntos": ["...", "..."],                   # lista: 2-4 puntos | comparacion: exactamente 2 bloques "Título|texto"
  "dato": "66 días",                          # solo estilo "dato": cifra verificable
  "dato_texto": "mediana para automatizar un hábito (Lally et al., 2010)",
  "pregunta": "Pregunta final del post",      # opcional, aparece en el pie
  "tema": "claro" | "oscuro"                  # opcional (por defecto alterna por día)
}
"""
import json, sys, datetime
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
M = 90  # margen
import os, glob


def _primera(*cands):
    for c in cands:
        hits = glob.glob(c)
        if hits:
            return hits[0]
    return None


# Fuentes: Windows (Segoe UI) o Linux (DejaVu / Liberation / Noto). Sin fuentes del sistema → fuente por defecto de Pillow.
F_BOLD = _primera("C:/Windows/Fonts/segoeuib.ttf", "/usr/share/fonts/**/DejaVuSans-Bold.ttf",
                  "/usr/share/fonts/**/LiberationSans-Bold.ttf", "/usr/share/fonts/**/NotoSans-Bold.ttf")
F_REG = _primera("C:/Windows/Fonts/segoeui.ttf", "/usr/share/fonts/**/DejaVuSans.ttf",
                 "/usr/share/fonts/**/LiberationSans-Regular.ttf", "/usr/share/fonts/**/NotoSans-Regular.ttf")
F_SEMI = _primera("C:/Windows/Fonts/seguisb.ttf", "/usr/share/fonts/**/DejaVuSans-Bold.ttf",
                  "/usr/share/fonts/**/LiberationSans-Bold.ttf") or F_BOLD

LIMA = (184, 214, 52)
NEGRO = (17, 17, 17)
GRIS = (90, 90, 90)
BLANCO = (255, 255, 255)
CREMA = (246, 245, 239)


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except (OSError, TypeError, AttributeError):
        return ImageFont.load_default(size=size)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit(draw, text, path, width, max_h, start, minimum, spacing=1.15):
    size = start
    while size >= minimum:
        f = font(path, size)
        lines = wrap(draw, text, f, width)
        h = len(lines) * size * spacing
        if h <= max_h:
            return f, lines, size
        size -= 4
    f = font(path, minimum)
    return f, wrap(draw, text, f, width), minimum


def draw_lines(draw, lines, fnt, size, x, y, fill, spacing=1.15):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += size * spacing
    return y


def main(inp, out):
    d = json.load(open(inp, encoding="utf-8"))
    estilo = d.get("estilo", "titular")
    tema = d.get("tema") or ("oscuro" if datetime.date.today().toordinal() % 2 else "claro")
    bg, fg, sub = (NEGRO, BLANCO, (200, 200, 200)) if tema == "oscuro" else (CREMA, NEGRO, GRIS)

    img = Image.new("RGB", (W, H), bg)
    dr = ImageDraw.Draw(img)
    cw = W - 2 * M

    # Cabecera: marca + etiqueta
    dr.ellipse((M, M + 12, M + 22, M + 34), fill=LIMA)
    dr.text((M + 34, M), "Punto", font=font(F_BOLD, 40), fill=fg)
    pw = dr.textlength("Punto", font=font(F_BOLD, 40))
    dr.text((M + 34 + pw + 6, M), "BEC", font=font(F_BOLD, 40), fill=LIMA)
    et = d.get("etiqueta", "").upper()
    if et:
        fe = font(F_BOLD, 28)
        tw = dr.textlength(et, font=fe)
        x1 = W - M
        dr.rounded_rectangle((x1 - tw - 40, M + 2, x1, M + 52), radius=26, fill=LIMA)
        dr.text((x1 - tw - 20, M + 8), et, font=fe, fill=NEGRO)

    y = M + 150
    pie_top = H - M - 170

    if estilo == "dato" and d.get("dato"):
        fd, ld, sd = fit(dr, d["dato"], F_BOLD, cw, 260, 230, 120, 1.0)
        y = draw_lines(dr, ld, fd, sd, M, y, LIMA, 1.0) + int(sd * 0.3)
        if d.get("dato_texto"):
            ft, lt, st = fit(dr, d["dato_texto"], F_REG, cw, 150, 40, 30)
            y = draw_lines(dr, lt, ft, st, M, y, sub) + 40
        dr.rectangle((M, y, M + 120, y + 8), fill=LIMA)
        y += 50
        ft, lt, st = fit(dr, d.get("titular", ""), F_BOLD, cw, pie_top - y - 20, 64, 40)
        draw_lines(dr, lt, ft, st, M, y, fg)
    else:
        max_t = 420 if estilo in ("lista", "comparacion") else pie_top - y - 40
        ft, lt, st = fit(dr, d.get("titular", ""), F_BOLD, cw, max_t, 96 if estilo == "titular" else 76, 44, 1.1)
        y = draw_lines(dr, lt, ft, st, M, y, fg, 1.1) + 30
        dr.rectangle((M, y, M + 120, y + 8), fill=LIMA)
        y += 60
        puntos = d.get("puntos", [])
        if estilo == "lista" and puntos:
            avail = pie_top - y - 20
            per = avail / len(puntos)
            for i, p in enumerate(puntos, 1):
                fp, lp, sp = fit(dr, p, F_SEMI, cw - 90, per - 24, 44, 28)
                dr.ellipse((M, y + 2, M + 56, y + 58), fill=LIMA)
                n = str(i)
                fn = font(F_BOLD, 34)
                dr.text((M + 28 - dr.textlength(n, font=fn) / 2, y + 6), n, font=fn, fill=NEGRO)
                yy = draw_lines(dr, lp, fp, sp, M + 84, y + 4, fg)
                y = max(yy, y + 64) + 24
        elif estilo == "comparacion" and len(puntos) >= 2:
            gap = 30
            bw = (cw - gap) / 2
            bh = min(pie_top - y - 30, 400)
            y += (pie_top - y - 30 - bh) / 2
            for i, p in enumerate(puntos[:2]):
                tit, _, txt = p.partition("|")
                x = M + i * (bw + gap)
                fill = LIMA if i == 1 else ((40, 40, 40) if tema == "oscuro" else (230, 229, 220))
                tc = NEGRO if i == 1 else fg
                dr.rounded_rectangle((x, y, x + bw, y + bh), radius=28, fill=fill)
                fh, lh, sh = fit(dr, tit, F_BOLD, bw - 60, 130, 46, 30)
                yy = draw_lines(dr, lh, fh, sh, x + 30, y + 30, tc) + 16
                fb, lb, sb = fit(dr, txt, F_REG, bw - 60, bh - (yy - y) - 30, 36, 24)
                draw_lines(dr, lb, fb, sb, x + 30, yy, tc)
        elif puntos:
            fp, lp, sp = fit(dr, " ".join(puntos), F_REG, cw, pie_top - y - 20, 44, 28)
            draw_lines(dr, lp, fp, sp, M, y, sub)

    # Pie: pregunta
    q = d.get("pregunta")
    dr.line((M, pie_top, W - M, pie_top), fill=LIMA, width=4)
    if q:
        fq, lq, sq = fit(dr, q, F_SEMI, cw, 130, 38, 26)
        draw_lines(dr, lq, fq, sq, M, pie_top + 26, fg)
    img.save(out, "PNG", optimize=True)
    print(out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

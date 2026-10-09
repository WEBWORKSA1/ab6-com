#!/usr/bin/env python3
"""Generate AB6.com raster images (app icons + Open Graph card) with Pillow.
Run: pip install pillow && python3 tools/make_images.py   (also run automatically by GitHub Actions)"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
LIME, LIME2, INK, BG, TXT, MUTED = (196, 255, 61), (123, 212, 0), (10, 12, 15), (10, 12, 15), (238, 242, 246), (154, 166, 178)


def font(size, bold=True):
    names = ["DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf", "LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf"]
    for d in ["/usr/share/fonts/truetype/dejavu", "/usr/share/fonts/truetype/liberation", "/usr/share/fonts/truetype"]:
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def logo(size, bg=None):
    s = size / 40
    im = Image.new("RGBA", (size, size), bg or (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=int(10 * s), fill=LIME)
    for r in range(3):
        for c in range(2):
            x, y = (9 + c * 12) * s, (7 + r * 9.5) * s
            d.rounded_rectangle([x, y, x + 10 * s, y + 7.5 * s], radius=int(2.4 * s), fill=INK)
    return im


def og():
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), BG)
    glow = Image.new("RGB", (W, H), BG)
    ImageDraw.Draw(glow).ellipse([700, -260, 1360, 400], fill=(58, 80, 20))
    im = Image.blend(im, glow.filter(ImageFilter.GaussianBlur(120)), 1.0)
    d = ImageDraw.Draw(im)
    im.paste(logo(84), (80, 120), logo(84))
    d.text((184, 128), "AB6.COM", font=font(60), fill=TXT)
    d.text((80, 240), "SIX-PACK ABS,", font=font(80), fill=TXT)
    d.text((80, 335), "ENGINEERED.", font=font(80), fill=LIME)
    d.text((80, 455), "Free calculators · Workout generator", font=font(30, False), fill=MUTED)
    d.text((80, 495), "6-week challenge · Coaching", font=font(30, False), fill=MUTED)
    for r in range(3):
        for c in range(2):
            x, y = 880 + c * 126, 165 + r * 104
            d.rounded_rectangle([x, y, x + 110, y + 88], radius=18, fill=LIME if (r + c) % 2 == 0 else LIME2)
    im.save(os.path.join(IMG, "og.png"), optimize=True)


if __name__ == "__main__":
    os.makedirs(IMG, exist_ok=True)
    for s in (192, 512):
        logo(s, BG + (255,)).convert("RGB").save(os.path.join(IMG, f"icon-{s}.png"), optimize=True)
    og()
    print("Images written to", IMG)

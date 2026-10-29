#!/usr/bin/env python3
"""Render the original profile nameplate. Dev dependency: Pillow."""

import io
import math
from pathlib import Path
import urllib.request

from PIL import Image, ImageDraw, ImageFont, PngImagePlugin

ROOT = Path(__file__).resolve().parents[1]
SCALE = 2
GROUND = "#d6f1e8"
INK = "#123e3c"
RULE = "#87b6a8"
SIGNAL = "#c44422"
FONT_URL = "https://raw.githubusercontent.com/google/fonts/main/ofl/chakrapetch/ChakraPetch-SemiBold.ttf"


def build():
    with urllib.request.urlopen(FONT_URL, timeout=30) as response:
        font_bytes = response.read()
    image = Image.new("RGB", (900 * SCALE, 360 * SCALE), GROUND)
    draw = ImageDraw.Draw(image)

    def line(points, fill=RULE, width=1):
        draw.line([(x * SCALE, y * SCALE) for x, y in points], fill=fill, width=width * SCALE)

    def text(x, y, value, size, fill=INK, anchor=None):
        font = ImageFont.truetype(io.BytesIO(font_bytes), size * SCALE)
        draw.text((x * SCALE, y * SCALE), value, font=font, fill=fill, anchor=anchor)

    def ellipse(box, fill=None, outline=RULE, width=1):
        draw.ellipse(tuple(v * SCALE for v in box), fill=fill, outline=outline, width=width * SCALE)

    # Oversized lettering and a real routing diagram, not a generic stats card.
    text(36, 8, "NUNO", 108)
    text(36, 112, "SOUSA", 108)
    line([(42, 259), (458, 259)], INK)
    text(42, 273, "AI platforms.", 24)
    text(42, 305, "Cloud & DevOps.", 24)

    cx, cy, radius = 694, 156, 105
    ellipse((cx - radius, cy - radius, cx + radius, cy + radius))
    ellipse((cx - 72, cy - 72, cx + 72, cy + 72))
    line([(cx - 132, cy), (cx - 119, cy)], INK)
    line([(cx + 119, cy), (cx + 132, cy)], INK)
    line([(cx, cy - 132), (cx, cy - 119)], INK)
    line([(cx, cy + 119), (cx, cy + 132)], INK)

    # A finite set of calibration marks follows the instrument's circumference.
    for angle in range(0, 360, 15):
        a = math.radians(angle)
        inner = radius + 8
        outer = radius + (16 if angle % 45 == 0 else 12)
        line([
            (cx + math.cos(a) * inner, cy + math.sin(a) * inner),
            (cx + math.cos(a) * outer, cy + math.sin(a) * outer),
        ])

    nodes = [(603, 103), (785, 103), (694, 261)]
    for x, y in nodes:
        ellipse((x - 7, y - 7, x + 7, y + 7), GROUND, INK, 2)
    ellipse((778, 96, 792, 110), SIGNAL, SIGNAL)
    text(557, 59, "BUILD", 18)
    text(772, 59, "SHIP", 18)
    text(676, 285, "RUN", 18)
    text(cx, 127, "CODE", 27, anchor="mt")
    text(cx, 162, "TO CLOUD", 20, anchor="mt")

    line([(510, 325), (854, 325)])
    text(510, 331, "PERSONAL MISSION CONTROL", 12)
    text(854, 331, "PORTO, PT", 12, anchor="rt")

    metadata = PngImagePlugin.PngInfo()
    metadata.add_text("Title", "Nuno Sousa - personal mission control")
    metadata.add_text("Description", "Original artwork rendered by scripts/build-artwork.py; not an AI-generated image or stock asset.")
    metadata.add_text("Source", f"Original geometric composition. Chakra Petch typeface: {FONT_URL}; SIL Open Font License 1.1.")
    output = ROOT / "assets/mission-control.png"
    output.parent.mkdir(exist_ok=True)
    image.save(output, pnginfo=metadata, optimize=True)
    print(output)


if __name__ == "__main__":
    build()

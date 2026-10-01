"""Generate a link-preview (og:image) card for every Markdown page with a title.

Each card has a small "Jack Skidmore" banner and the page title below it,
wrapped and shrunk to fit. An optional `og_title:` in front matter overrides
the text on the card. Output goes to assets/images/og/<slug>.png, where <slug>
is the source path without ".md" and with "/" replaced by "-" — the same rule
_layouts/default.html uses to find it.

Run from the repo root:  python _og/generate.py
"""

import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "_og" / "InterDisplay-Bold.ttf"
OUT = ROOT / "assets" / "images" / "og"

W, H = 1200, 630
PAD_X = 88
BG = "#ffffff"
TEXT = "#1f2328"
GREEN = "#0D4723"

BANNER_SIZE = 48
BANNER_TOP = 72
TITLE_MAX, TITLE_MIN = 96, 44
TITLE_LINE_HEIGHT = 1.15
TITLE_GAP = 56  # space between banner and the title area
BOTTOM_PAD = 72


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        return {}
    data = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep:
            data[key.strip()] = value.strip().strip("\"'")
    return data


def wrap(draw, text, font, max_width):
    lines, line = [], ""
    for word in text.split():
        candidate = f"{line} {word}".strip()
        if draw.textlength(candidate, font=font) <= max_width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def fit_title(draw, title, max_width, max_height):
    for size in range(TITLE_MAX, TITLE_MIN - 1, -2):
        font = ImageFont.truetype(str(FONT), size)
        lines = wrap(draw, title, font, max_width)
        too_wide = any(draw.textlength(l, font=font) > max_width for l in lines)
        if not too_wide and len(lines) * size * TITLE_LINE_HEIGHT <= max_height:
            return font, lines
    return font, lines


def render(title, dest):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    banner = ImageFont.truetype(str(FONT), BANNER_SIZE)
    draw.text((PAD_X, BANNER_TOP), "Jack ", font=banner, fill=TEXT, anchor="lt")
    jack_width = draw.textlength("Jack ", font=banner)
    draw.text((PAD_X + jack_width, BANNER_TOP), "Skidmore", font=banner, fill=GREEN, anchor="lt")

    area_top = BANNER_TOP + BANNER_SIZE + TITLE_GAP
    area_height = H - BOTTOM_PAD - area_top
    font, lines = fit_title(draw, title, W - 2 * PAD_X, area_height)

    line_height = font.size * TITLE_LINE_HEIGHT
    y = area_top + (area_height - len(lines) * line_height) / 2
    for line in lines:
        draw.text((PAD_X, y + line_height / 2), line, font=font, fill=TEXT, anchor="lm")
        y += line_height

    img.save(dest, optimize=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if any(part.startswith((".", "_")) for part in rel.parts):
            continue
        fm = front_matter(path)
        if not fm.get("title"):
            continue
        slug = str(rel.with_suffix("")).replace("/", "-")
        render(fm.get("og_title") or fm["title"], OUT / f"{slug}.png")
        print(f"{rel} -> assets/images/og/{slug}.png")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build the GTA 6 meme for make.fun bounty gta6-meme-x-01.

Composites the official make.fun ghost mascot onto an AI-generated Vice City
scene and adds bold meme captions (white text, thick black outline).
"""
from PIL import Image, ImageDraw, ImageFont

BASE_IMAGE = "media-generation-gta6-meme-base-0-c4c9a772-5652-4330-889d-1d76ca270f40.webp"
GHOST_IMAGE = "ghost-mark-1024.png"
OUTPUT_IMAGE = "meme-gta6-final.png"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

GHOST_SIZE = 330
GHOST_POS = (640, 190)

TOP_CAPTION = "WAITED 13 YEARS FOR GTA 6"
TOP_FONT_SIZE = 88
TOP_Y = 40

BOTTOM_LINE_1 = "MY AI AGENT GOT PAID"
BOTTOM_LINE_2 = "BEFORE MY DOWNLOAD FINISHED"
BOTTOM_FONT_SIZE = 78
BOTTOM_Y_1 = 1360
BOTTOM_Y_2 = 1455


def draw_centered(draw, canvas_width, y, text, font, stroke_width=6):
    bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    text_width = bbox[2] - bbox[0]
    draw.text(((canvas_width - text_width) / 2, y), text, font=font,
              fill="white", stroke_width=stroke_width, stroke_fill="black")


def main():
    canvas = Image.open(BASE_IMAGE).convert("RGB")
    width, _height = canvas.size

    ghost = Image.open(GHOST_IMAGE).convert("RGBA")
    ghost = ghost.resize((GHOST_SIZE, GHOST_SIZE), Image.LANCZOS)
    canvas.paste(ghost, GHOST_POS, ghost)

    draw = ImageDraw.Draw(canvas)
    top_font = ImageFont.truetype(FONT_PATH, TOP_FONT_SIZE)
    bottom_font = ImageFont.truetype(FONT_PATH, BOTTOM_FONT_SIZE)

    draw_centered(draw, width, TOP_Y, TOP_CAPTION, top_font)
    draw_centered(draw, width, BOTTOM_Y_1, BOTTOM_LINE_1, bottom_font)
    draw_centered(draw, width, BOTTOM_Y_2, BOTTOM_LINE_2, bottom_font)

    canvas.save(OUTPUT_IMAGE)
    print(f"saved {OUTPUT_IMAGE} {canvas.size}")


if __name__ == "__main__":
    main()

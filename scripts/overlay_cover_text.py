#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


FONT_PATH = "/System/Library/Fonts/Hiragino Sans GB.ttc"
MANGA_FONT_PATH = "/System/Library/Fonts/ヒラギノ角ゴシック W8.ttc"


def fit_font(text: str, font_path: str, max_width: int, start_size: int, min_size: int) -> ImageFont.FreeTypeFont:
    size = start_size
    while size >= min_size:
        font = ImageFont.truetype(font_path, size=size)
        bbox = font.getbbox(text)
        width = bbox[2] - bbox[0]
        if width <= max_width:
            return font
        size -= 2
    return ImageFont.truetype(font_path, size=min_size)


def draw_centered_text(draw: ImageDraw.ImageDraw, text: str, y: int, font: ImageFont.FreeTypeFont, fill: str, stroke_fill: str, stroke_width: int, image_width: int) -> None:
    bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    text_width = bbox[2] - bbox[0]
    x = (image_width - text_width) // 2
    draw.text((x, y), text, font=font, fill=fill, stroke_fill=stroke_fill, stroke_width=stroke_width)


def draw_manga_title(draw: ImageDraw.ImageDraw, text: str, width: int, y: int) -> None:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return

    font_path = MANGA_FONT_PATH
    max_width = width - 80
    size = 136 if len(lines) == 1 else 124
    title_font = ImageFont.truetype(font_path, size=size)

    while size >= 40:
        title_font = ImageFont.truetype(font_path, size=size)
        widest = 0
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=title_font, stroke_width=7)
            widest = max(widest, bbox[2] - bbox[0])
        if widest <= max_width:
            break
        size -= 4

    line_height = size + 20
    current_y = y
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=title_font, stroke_width=7)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2

        draw.text(
            (x - 7, current_y + 8),
            line,
            font=title_font,
            fill="#D62828",
            stroke_fill="#D62828",
            stroke_width=2,
        )
        draw.text(
            (x + 7, current_y + 12),
            line,
            font=title_font,
            fill="#2563EB",
            stroke_fill="#2563EB",
            stroke_width=2,
        )
        draw.text(
            (x, current_y),
            line,
            font=title_font,
            fill="#FFF7E8",
            stroke_fill="#111827",
            stroke_width=7,
        )
        current_y += line_height


def draw_sign(draw: ImageDraw.ImageDraw, text: str, x: int, y: int, fill: tuple[int, int, int, int], stroke_fill: str, text_fill: str) -> None:
    sign_width = 206
    sign_height = 68
    shadow_offset = 6

    draw.rounded_rectangle(
        [(x + shadow_offset, y + shadow_offset), (x + sign_width + shadow_offset, y + sign_height + shadow_offset)],
        radius=20,
        fill=(15, 23, 42, 120),
    )
    draw.rounded_rectangle(
        [(x, y), (x + sign_width, y + sign_height)],
        radius=20,
        fill=fill,
        outline=(255, 247, 232, 200),
        width=3,
    )

    label_font = fit_font(text, MANGA_FONT_PATH, sign_width - 28, 34, 18)
    bbox = draw.textbbox((0, 0), text, font=label_font, stroke_width=2)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = x + (sign_width - tw) // 2
    ty = y + (sign_height - th) // 2 - 2
    draw.text(
        (tx, ty),
        text,
        font=label_font,
        fill=text_fill,
        stroke_fill=stroke_fill,
        stroke_width=2,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", type=Path)
    parser.add_argument("output_path", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--left-label", default="")
    parser.add_argument("--right-label", default="")
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--style", choices=["default", "manga"], default="default")
    parser.add_argument("--left-sign", default="")
    parser.add_argument("--right-sign", default="")
    args = parser.parse_args()

    image = Image.open(args.image_path).convert("RGBA")
    overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    width, height = image.size

    if args.style == "manga":
        draw_manga_title(draw, args.title, width, 58)
    else:
        # soft top gradient band for readable title
        draw.rounded_rectangle(
            [(40, 28), (width - 40, 230)],
            radius=28,
            fill=(255, 255, 255, 36),
            outline=(255, 255, 255, 64),
            width=2,
        )

        title_font = fit_font(args.title, FONT_PATH, width - 140, 88, 40)
        draw_centered_text(
            draw,
            args.title,
            58,
            title_font,
            fill="#FFF7E8",
            stroke_fill="#0F172A",
            stroke_width=4,
            image_width=width,
        )

    if args.subtitle:
        subtitle_font = fit_font(args.subtitle, FONT_PATH, width - 160, 34, 20)
        draw_centered_text(
            draw,
            args.subtitle,
            150,
            subtitle_font,
            fill="#E5E7EB",
            stroke_fill="#0F172A",
            stroke_width=2,
            image_width=width,
        )

    if args.left_sign:
        draw_sign(
            draw,
            args.left_sign,
            36,
            840,
            fill=(198, 40, 40, 235),
            stroke_fill="#7F1D1D",
            text_fill="#FFF7E8",
        )

    if args.right_sign:
        draw_sign(
            draw,
            args.right_sign,
            width - 36 - 206,
            820,
            fill=(37, 99, 235, 235),
            stroke_fill="#1E3A8A",
            text_fill="#EFF6FF",
        )

    tag_font = fit_font("NETFLIX", FONT_PATH, 220, 34, 20)
    if args.left_label:
        draw.rounded_rectangle(
            [(56, height - 150), (56 + 220, height - 92)],
            radius=18,
            fill=(180, 26, 26, 220),
        )
        draw_centered_text(
            draw,
            args.left_label,
            height - 140,
            tag_font,
            fill="#FFF7E8",
            stroke_fill="#7F1D1D",
            stroke_width=2,
            image_width=220 + 112,
        )

    if args.right_label:
        x1 = width - 276
        x2 = width - 56
        draw.rounded_rectangle(
            [(x1, height - 150), (x2, height - 92)],
            radius=18,
            fill=(37, 99, 235, 220),
        )
        bbox = draw.textbbox((0, 0), args.right_label, font=tag_font, stroke_width=2)
        tw = bbox[2] - bbox[0]
        tx = x1 + (220 - tw) // 2
        draw.text(
            (tx, height - 140),
            args.right_label,
            font=tag_font,
            fill="#EFF6FF",
            stroke_fill="#1E3A8A",
            stroke_width=2,
        )

    final = Image.alpha_composite(image, overlay).convert("RGB")
    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    final.save(args.output_path)
    print(f"saved {args.output_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


STYLE_SPECS = {
    "anime_cover": {
        "label": "Style 1 - Anime Cover",
        "summary": "Anime key visual built like a famous scene cover: cleaner background, stronger pose, more cover impact.",
        "keywords": [
            "anime key visual",
            "famous-scene conversion",
            "loaded action pose",
            "clean cover composition",
            "two-sided conflict background",
        ],
        "anchor_prefix": (
            "Anime key visual character sheet, cover-worthy sports protagonist, strong facial appeal, "
            "loaded batting stance, visible torso twist, pre-impact tension, clean hero silhouette. "
        ),
        "background_prefix": (
            "Background layer for an anime cover, clean and graphic, only a few symbolic world-building elements, "
            "no main character, no clutter, preserve clear negative space around the center. "
        ),
        "final_prefix": (
            "Anime cover illustration, transformed from a famous sports-anime climax frame, dynamic loaded batting pose, "
            "strong hero angle, clean energetic composition, background supporting the hero rather than competing with the hero. "
        ),
        "style_suffix": (
            "Illustrated anime style only, clean background hierarchy, concentrated motion energy, no dirty paper texture, "
            "no old stains, no photorealism, no readable text, no logos, no watermarks."
        ),
        "mode": "hero",
    },
    "game_cinematic": {
        "label": "Style 2 - Game Cinematic",
        "summary": "Premium game-animation key art with stronger lighting, star aura, and commercial-news hero treatment.",
        "keywords": [
            "premium animated game key art",
            "heroic sports portrait",
            "strong volumetric lighting",
            "high-budget cinematic composition",
            "commercial news cover energy",
        ],
        "anchor_prefix": (
            "Premium animated game character sheet, sports superstar aura, sharp face design, confident hero pose, "
            "cinematic body language, strong shoulder and torso readability. "
        ),
        "background_prefix": (
            "Background layer for a premium animated game sports cover, dramatic light beams, clean arena atmosphere, "
            "only a few symbolic elements, no clutter, preserve clear space around the subject. "
        ),
        "final_prefix": (
            "Premium animated game sports cover illustration, one star protagonist, cinematic lighting, strong emotional readability, "
            "commercial-news hero treatment, background supporting the protagonist. "
        ),
        "style_suffix": (
            "High-end animated game illustration, not photorealistic, not low-budget 3D, strong volumetric lighting, "
            "no readable text, no logos, no watermarks."
        ),
        "mode": "hero",
    },
    "editorial_collage": {
        "label": "Style 3 - Editorial Collage",
        "summary": "Sports-business magazine collage using the protagonist, numbers, screens, and venue symbols to support one conclusion.",
        "keywords": [
            "editorial sports business collage",
            "magazine cover layout",
            "newsroom energy",
            "numbers and screens",
            "clean layered composition",
        ],
        "anchor_prefix": (
            "Editorial sports-business cover subject layer, one main protagonist, headline-ready pose, clean cutout silhouette, "
            "strong central presence for magazine-style collage layout. "
        ),
        "background_prefix": (
            "Background layer for a sports-business editorial collage, large number blocks, screen panels, venue symbols, "
            "clean paper-like layering, no clutter, preserve clear reading hierarchy. "
        ),
        "final_prefix": (
            "Sports-business editorial collage cover, one main protagonist, layered number blocks and screen panels, "
            "magazine-grade composition, one clear commercial-news conclusion. "
        ),
        "style_suffix": (
            "High-end editorial collage illustration, clean layers, structured information feel, not scrapbook mess, "
            "no readable text, no logos, no watermarks."
        ),
        "mode": "editorial",
    },
    "minimal_data_poster": {
        "label": "Style 4 - Minimal Data Poster",
        "summary": "Minimal poster that makes numbers, arrows, and structure the main visual while keeping one clear anchor.",
        "keywords": [
            "minimal data poster",
            "numbers-first sports graphic",
            "clean arrow and block composition",
            "posterized information design",
            "high-contrast editorial graphic",
        ],
        "anchor_prefix": (
            "Minimal poster subject layer, one clear protagonist or symbolic anchor, simplified silhouette, "
            "designed to coexist with large numbers and bold graphic shapes. "
        ),
        "background_prefix": (
            "Background layer for a minimal data poster, bold blocks, arrows, contrast bands, arena or court lines kept very faint, "
            "strong negative space, no clutter. "
        ),
        "final_prefix": (
            "Minimal sports data poster, one clear anchor, large implied numbers, bold arrows and structured blocks, "
            "high-contrast editorial graphic design with poster clarity. "
        ),
        "style_suffix": (
            "Minimal graphic poster, clean information hierarchy, not powerpoint, not techno UI, "
            "no readable text, no logos, no watermarks."
        ),
        "mode": "poster",
    },
    "mascot_q": {
        "label": "Style 5 - Mascot Q",
        "summary": "Power-Pro-like baseball mascot treatment with bean body, cute prompt-derived props, and cleaner panel composition.",
        "keywords": [
            "baseball mascot illustration",
            "rounded bean body",
            "short limbs",
            "thick clean outline",
            "cute panel composition",
        ],
        "anchor_prefix": (
            "Cute baseball mascot character sheet, rounded bean-shaped body, oversized head, very short limbs, "
            "thick clean outline, simple expressive face, sporty charm, collectible Xiaohongshu mascot vibe. "
        ),
        "background_prefix": (
            "Background layer for a cute mascot cover, simple panel-like composition, large cream breathing room, "
            "only a few bold sporty symbols, no clutter, no full scenic illustration. "
        ),
        "final_prefix": (
            "Cute Japanese baseball mascot cover, Power-Pro-like bean body proportions, thick outline, flat clean coloring, "
            "prompt-derived sporty props, simple but memorable panel-like composition. "
        ),
        "style_suffix": (
            "Non-photoreal mascot illustration, no mature body proportions, no glossy anime rendering, no cluttered background, "
            "no readable text, no logos, no watermarks."
        ),
        "mode": "mascot",
    },
}

COMMON_ANCHOR_SUFFIX = (
    "Vertical cover composition, one main subject only, flattering face design, clear silhouette, "
    "clean light background or minimal studio-like environment, no distorted anatomy, no extra fingers."
)

COMMON_BACKGROUND_SUFFIX = (
    "Background only, no main character, preserve center space for subject placement, support the story conflict, "
    "keep it simple and readable as a cover."
)

COMMON_FINAL_SUFFIX = (
    "Vertical cover composition, one clear focal subject, click-worthy Xiaohongshu cover, strong emotional readability, "
    "safe negative space for a title, no distorted anatomy, no extra fingers."
)


@dataclass
class StoryAtoms:
    protagonist: str
    action_moment: str
    emotional_conflict: str
    background_symbols: list[str]


@dataclass
class StylePacket:
    style_id: str
    label: str
    summary: str
    keywords: list[str]
    selection_reason: str
    subject_anchor_prompt: str
    background_prompt: str
    final_prompt: str
    cute_elements: list[str]


def load_env_from_workspace(start: Path) -> None:
    candidates = [start] + list(start.parents)
    for base in candidates:
        env_path = base / ".env"
        if env_path.exists():
            load_dotenv(env_path)
            return
    load_dotenv()


def normalize_prompt(raw_prompt: str) -> str:
    prompt = " ".join(raw_prompt.strip().split())
    if not prompt:
        raise ValueError("Prompt is empty")
    return prompt


def has_any(prompt: str, tokens: list[str]) -> bool:
    return any(token in prompt for token in tokens)


def mentions_negative(prompt: str, token_groups: list[list[str]]) -> bool:
    negatives = ["no ", "without ", "remove ", "exclude ", "不要", "移除", "去掉", "不要有", "no-", "無"]
    for group in token_groups:
        if not any(token in prompt for token in group):
            continue
        for neg in negatives:
            for token in group:
                if f"{neg}{token}" in prompt:
                    return True
    return False


def infer_story_atoms(raw_prompt: str) -> StoryAtoms:
    prompt = raw_prompt.lower()
    protagonist = "the named main protagonist from the brief"
    for candidate in ["shohei ohtani", "ohtani", "大谷翔平"]:
        if candidate in prompt or candidate in raw_prompt:
            protagonist = "Shohei Ohtani"
            break
    for candidate in ["caitlin clark", "clark", "克拉克"]:
        if candidate in prompt or candidate in raw_prompt:
            protagonist = "Caitlin Clark"
            break

    action_moment = "the signature pose or emotional moment described in the brief"
    if has_any(prompt, ["batting", "swing", "挥棒", "揮棒", "left-handed", "左打", "baseball", "棒球"]):
        action_moment = (
            "real left-handed loaded batting stance before contact, back knee flexed, weight on the back leg, "
            "front side natural and balanced, torso fully coiled for the swing"
        )
    elif has_any(prompt, ["basketball", "wnba", "nba", "女篮", "篮球", "籃球"]):
        action_moment = (
            "decisive basketball hero pose with strong ball control, alert shoulders, grounded stance, "
            "and visible competitive tension in the upper body"
        )
    elif has_any(prompt, ["run", "running", "sprint", "冲刺", "跑"]):
        action_moment = "mid-sprint burst with strong forward momentum"
    elif has_any(prompt, ["jump", "扣", "jump shot", "灌篮", "投篮"]):
        action_moment = "pre-jump explosive sports moment"

    if has_any(prompt, ["crouch", "lower stance", "low-angle", "低机位", "压低"]) and has_any(prompt, ["baseball", "棒球", "swing", "挥棒", "揮棒"]):
        action_moment = (
            "deeper low-angle left-handed loaded batting stance before contact, stronger crouch, back knee flexed, "
            "weight on the back leg, natural front-leg action, torso coiled for the explosive swing"
        )
    if has_any(prompt, ["torso twist", "twist", "扭转", "轉體"]) and has_any(prompt, ["baseball", "棒球", "swing", "挥棒", "揮棒"]):
        action_moment = (
            "deeper low-angle left-handed loaded batting stance before contact, natural leg bend, weight on the back leg, "
            "clear torso coil and hip tension right before the explosive swing"
        )
    if has_any(prompt, ["half-body", "upper-body", "半身", "上半身", "cropped above the knees"]) and has_any(prompt, ["baseball", "棒球", "swing", "挥棒", "揮棒"]):
        action_moment = (
            "low-angle half-body left-handed loaded batting pose before contact, hands tight near the rear shoulder, "
            "bat visible, clear torso coil and natural swing tension"
        )

    emotional_conflict = "the core rise, conflict, or business tension described in the brief"
    if "exclusive" in prompt or "独占" in raw_prompt:
        emotional_conflict = "exclusive-rights tension and the fight for audience attention"
    elif has_any(prompt, ["salary", "薪资", "薪水", "加薪", "工资", "工资帽"]):
        emotional_conflict = "salary-growth tension and the question of who is finally getting paid"
    elif has_any(prompt, ["broadcast", "rights", "转播", "版权", "版权费"]):
        emotional_conflict = "media-rights tension and the fight over who controls the audience"
    elif has_any(prompt, ["expansion", "扩军", "加盟费"]):
        emotional_conflict = "league-expansion momentum and the flow of new money into the sport"

    background_symbols = build_background_symbols(raw_prompt)
    return StoryAtoms(
        protagonist=protagonist,
        action_moment=action_moment,
        emotional_conflict=emotional_conflict,
        background_symbols=background_symbols,
    )


def build_background_symbols(raw_prompt: str) -> list[str]:
    prompt = raw_prompt.lower()
    symbols: list[str] = []
    tokyo_tokens = ["tokyo", "東京", "东京", "tokyo tower", "東京塔", "东京铁塔"]
    mascot_tokens = ["mascot", "cute", "q版", "q 版", "chibi", "icon"]
    japan_tokens = ["japan team", "samurai japan", "侍japan", "侍 japan", "wbc", "world baseball classic", "棒球"]
    basketball_tokens = ["basketball", "wnba", "nba", "篮球", "籃球"]

    if has_any(prompt, tokyo_tokens) and not mentions_negative(prompt, [tokyo_tokens]):
        symbols.append("Tokyo skyline silhouette")
    if has_any(prompt, ["netflix", "streaming", "流媒体", "串流"]):
        if has_any(prompt, mascot_tokens):
            symbols.append("cute red streaming mascot icon")
        else:
            symbols.append("minimal red streaming interface panel")
    if has_any(prompt, ["amazon", "e-commerce", "prime", "电商"]):
        if has_any(prompt, mascot_tokens):
            symbols.append("cute blue commerce mascot icon")
        else:
            symbols.append("minimal blue commerce arrow panel")
    if has_any(prompt, ["wbc", "world baseball classic", "棒球"]):
        symbols.append("clean WBC stadium arch and scoreboard light")
    if has_any(prompt, japan_tokens):
        symbols.append("Samurai Japan color-block stadium banner")
    if has_any(prompt, basketball_tokens):
        symbols.append("clean basketball court lines and arena light")
    if has_any(prompt, ["salary", "薪资", "薪水", "工资", "加薪", "工资帽"]):
        symbols.append("bold upward salary blocks and cap-rise bars")
    if has_any(prompt, ["broadcast", "rights", "转播", "版权", "版权费"]):
        symbols.append("large broadcast screen and camera light beam")
    if has_any(prompt, ["expansion", "扩军", "加盟费", "city", "城市"]):
        symbols.append("new arena and city skyline silhouettes")
    if not symbols:
        symbols = ["clean sports-arena light", "simple conflict color field", "bold number block"]
    deduped: list[str] = []
    for item in symbols:
        if item not in deduped:
            deduped.append(item)
    return deduped[:3]


def build_cute_elements(raw_prompt: str) -> list[str]:
    prompt = raw_prompt.lower()
    elements: list[str] = []
    tokyo_tokens = ["tokyo", "東京", "东京", "tokyo tower", "東京塔", "东京铁塔"]
    if has_any(prompt, ["baseball", "wbc", "棒球"]):
        elements.extend(["mini baseball bat", "cute cap", "tiny scoreboard icon"])
    if has_any(prompt, ["basketball", "wnba", "nba", "篮球", "籃球"]):
        elements.extend(["mini basketball", "tiny arena light", "score panel icon"])
    if has_any(prompt, ["netflix", "streaming", "流媒体", "串流"]):
        elements.append("red streaming app tile")
    if has_any(prompt, ["amazon", "prime", "e-commerce", "电商"]):
        elements.append("blue delivery-arrow tile")
    if has_any(prompt, ["salary", "薪资", "薪水", "工资", "加薪"]):
        elements.append("upward salary arrow")
    if has_any(prompt, ["broadcast", "rights", "转播", "版权"]):
        elements.append("tiny screen icon")
    if has_any(prompt, ["tokyo", "japan", "日本", "东京"]) and not mentions_negative(prompt, [tokyo_tokens]):
        elements.append("tiny Tokyo tower silhouette")
    deduped: list[str] = []
    for item in elements:
        if item not in deduped:
            deduped.append(item)
    return deduped[:4] or ["mini sports prop", "cute conflict color ribbon"]


def build_style_packets(raw_prompt: str) -> tuple[StoryAtoms, list[StylePacket]]:
    normalized = normalize_prompt(raw_prompt)
    atoms = infer_story_atoms(normalized)
    symbol_text = ", ".join(atoms.background_symbols)
    cute_elements = build_cute_elements(normalized)
    cute_text = ", ".join(cute_elements)
    story_cues = f"Preserve these story-specific cues from the prompt: {normalized}."

    packets: list[StylePacket] = []
    for style_id, spec in STYLE_SPECS.items():
        mode = spec["mode"]
        if mode == "mascot":
            subject_prompt = (
                f"{spec['anchor_prefix']}Convert {atoms.protagonist} into a cute sports mascot while keeping the story readable. "
                f"Main action should feel like {atoms.action_moment}. {story_cues} {COMMON_ANCHOR_SUFFIX} {spec['style_suffix']}"
            )
            background_prompt = (
                f"{spec['background_prefix']}Use only these symbols: {symbol_text}. "
                f"Translate the story into these cute elements: {cute_text}. "
                f"{story_cues} {COMMON_BACKGROUND_SUFFIX} {spec['style_suffix']}"
            )
            final_prompt = (
                f"{spec['final_prefix']}Turn the story into a cute mascot cover. Main action: {atoms.action_moment}. "
                f"Emotional conflict: {atoms.emotional_conflict}. Include only these cute elements: {cute_text}. "
                f"Background symbols: {symbol_text}. {story_cues} {COMMON_FINAL_SUFFIX} {spec['style_suffix']}"
            )
            packet_cute_elements = cute_elements
        else:
            subject_prompt = (
                f"{spec['anchor_prefix']}{atoms.protagonist}, {atoms.action_moment}. "
                f"Emotional core: {atoms.emotional_conflict}. {story_cues} {COMMON_ANCHOR_SUFFIX} {spec['style_suffix']}"
            )
            background_prompt = (
                f"{spec['background_prefix']}Use only these background symbols: {symbol_text}. "
                f"{story_cues} {COMMON_BACKGROUND_SUFFIX} {spec['style_suffix']}"
            )
            final_prompt = (
                f"{spec['final_prefix']}{atoms.protagonist} in {atoms.action_moment}, with {atoms.emotional_conflict}. "
                f"Background should only use these symbols: {symbol_text}. "
                f"{story_cues} {COMMON_FINAL_SUFFIX} {spec['style_suffix']}"
            )
            packet_cute_elements = []

        packets.append(
            StylePacket(
                style_id=style_id,
                label=spec["label"],
                summary=spec["summary"],
                keywords=spec["keywords"],
                selection_reason="",
                subject_anchor_prompt=subject_prompt,
                background_prompt=background_prompt,
                final_prompt=final_prompt,
                cute_elements=packet_cute_elements,
            )
        )

    return atoms, packets


def recommend_style_ids(raw_prompt: str) -> list[str]:
    prompt = raw_prompt.lower()
    if has_any(prompt, ["mascot", "cute", "q版", "q 版", "chibi", "吉祥物", "可爱", "可愛"]):
        return ["mascot_q", "anime_cover"]
    if has_any(prompt, ["salary", "薪资", "薪水", "工资", "加薪", "broadcast", "rights", "转播", "版权", "版权费", "expansion", "扩军", "加盟费", "platform", "平台", "商业", "商業"]):
        return ["editorial_collage", "minimal_data_poster"]
    if has_any(prompt, ["clark", "克拉克", "ohtani", "大谷", "star", "superstar", "巨星", "人物", "球星"]):
        return ["game_cinematic", "anime_cover"]
    return ["game_cinematic", "editorial_collage"]


def explain_style_selection(style_id: str, raw_prompt: str) -> str:
    prompt = raw_prompt.lower()
    if style_id == "editorial_collage":
        return "这题更像商业新闻，需要人物、数字和机制一起服务一个结论。"
    if style_id == "minimal_data_poster":
        return "这题的数字和结构变化很重要，适合用更简洁的海报结构把信息压清楚。"
    if style_id == "game_cinematic":
        return "这题更依赖主角气场和人物升咖感，适合更有明星感的电影级人物风格。"
    if style_id == "anime_cover":
        if has_any(prompt, ["emotion", "情绪", "冲突", "对峙", "热血", "动作"]):
            return "这题更依赖动作和情绪冲突，适合海报感更强的运动动画风。"
        return "这套风格能提供更强的封面感和动作张力。"
    if style_id == "mascot_q":
        return "这题更适合做得轻一点、可爱一点，用角色化方式提升收藏感和分享感。"
    return "这套风格更适合当前这张图的主任务。"


def write_outputs(
    output_dir: Path,
    raw_prompt: str,
    atoms: StoryAtoms,
    packets: list[StylePacket],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "raw_prompt": raw_prompt,
        "story_atoms": asdict(atoms),
        "styles": [asdict(packet) for packet in packets],
        "generation_order": [
            "subject_anchor_prompt",
            "background_prompt",
            "final_prompt",
        ],
    }
    (output_dir / "style_prompts.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = [
        "# Style Duo",
        "",
        "## Raw Prompt",
        raw_prompt,
        "",
        "## Story Atoms",
        f"- 主角：{atoms.protagonist}",
        f"- 动作瞬间：{atoms.action_moment}",
        f"- 情绪冲突：{atoms.emotional_conflict}",
        f"- 背景符号：{', '.join(atoms.background_symbols)}",
        "",
        "## Generation Order",
        "1. subject_anchor_prompt",
        "2. background_prompt",
        "3. final_prompt",
        "",
    ]
    for packet in packets:
        lines.extend(
            [
                f"## {packet.label}",
                f"- Summary: {packet.summary}",
                f"- Why selected: {packet.selection_reason}",
                f"- Keywords: {', '.join(packet.keywords)}",
            ]
        )
        if packet.cute_elements:
            lines.append(f"- Cute elements: {', '.join(packet.cute_elements)}")
        lines.extend(
            [
                "- Subject anchor prompt:",
                "```text",
                packet.subject_anchor_prompt,
                "```",
                "- Background prompt:",
                "```text",
                packet.background_prompt,
                "```",
                "- Final prompt:",
                "```text",
                packet.final_prompt,
                "```",
                "",
            ]
        )
    (output_dir / "style_prompts.md").write_text("\n".join(lines), encoding="utf-8")


def generate_images(
    output_dir: Path,
    packets: list[StylePacket],
    model: str,
    size: str,
    quality: str,
    output_format: str,
) -> None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required to generate images")

    client = OpenAI(api_key=api_key)
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "provider": "openai",
        "model": model,
        "size": size,
        "quality": quality,
        "output_format": output_format,
        "images": [],
    }

    for packet in packets:
        response = client.images.generate(
            model=model,
            prompt=packet.final_prompt,
            size=size,
            quality=quality,
            output_format=output_format,
        )
        data_item = response.data[0]
        image_path = output_dir / f"{packet.style_id}.{output_format}"
        image_data = getattr(data_item, "b64_json", None)
        image_url = getattr(data_item, "url", None)
        revised_prompt = getattr(data_item, "revised_prompt", None)
        if image_data:
            image_path.write_bytes(base64.b64decode(image_data))
        elif image_url:
            with urllib.request.urlopen(image_url) as remote:
                image_path.write_bytes(remote.read())
        else:
            raise RuntimeError(f"No image data returned for style {packet.style_id}")

        manifest["images"].append(
            {
                "style_id": packet.style_id,
                "file": str(image_path),
                "final_prompt": packet.final_prompt,
                "revised_prompt": revised_prompt,
            }
        )
        print(f"saved {image_path}")

    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"saved {output_dir / 'manifest.json'}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", help="Base prompt text")
    parser.add_argument("--prompt-file", type=Path, help="Path to a text file containing the base prompt")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--generate-images", action="store_true")
    parser.add_argument(
        "--styles",
        help="Comma-separated style ids to keep, e.g. game_cinematic,editorial_collage",
    )
    parser.add_argument("--model", default="gpt-image-1.5")
    parser.add_argument("--size", default="1024x1536")
    parser.add_argument("--quality", default="high")
    parser.add_argument("--output-format", default="png")
    args = parser.parse_args()

    if not args.prompt and not args.prompt_file:
        raise ValueError("Either --prompt or --prompt-file is required")

    raw_prompt = args.prompt
    if args.prompt_file:
        raw_prompt = args.prompt_file.read_text(encoding="utf-8")
    assert raw_prompt is not None

    output_dir = args.output_dir.resolve()
    load_env_from_workspace(output_dir.parent)
    atoms, packets = build_style_packets(raw_prompt)
    if args.styles:
        wanted = {item.strip() for item in args.styles.split(",") if item.strip()}
    else:
        wanted = set(recommend_style_ids(raw_prompt))
    packets = [packet for packet in packets if packet.style_id in wanted]
    if not packets:
        raise ValueError("No matching styles selected")
    for packet in packets:
        packet.selection_reason = explain_style_selection(packet.style_id, raw_prompt)
    write_outputs(output_dir, raw_prompt.strip(), atoms, packets)
    print(f"saved {output_dir / 'style_prompts.md'}")
    print(f"saved {output_dir / 'style_prompts.json'}")

    if args.generate_images:
        generate_images(
            output_dir=output_dir,
            packets=packets,
            model=args.model,
            size=args.size,
            quality=args.quality,
            output_format=args.output_format,
        )


if __name__ == "__main__":
    main()

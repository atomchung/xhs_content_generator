#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def build_readme(title: str, slug: str) -> str:
    return f"""# {title}

This folder is the workspace for one Xiaohongshu post.

## Folder layout

- `research/research.md`
  Topic framing, title options, angle notes, source map.
- `research/fact_pack.md`
  Verified numbers, argument chain, risk notes.
- `research/story_spine.md`
  One-story framing: core question, conflict, why now, why care, and parked side angles.
- `text/post.md`
  Final note copy for publishing.
- `prompts/`
  Prompt drafts and per-style prompt files.
- `images/`
  Generated images and edited deliverables.
- `reviews/`
  Publish reviews, postmortems, and iteration notes.

## Post metadata

- Slug: `{slug}`
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="Post date, for example 2026-03-16")
    parser.add_argument("--slug", required=True, help="Short ASCII slug, for example apple-f1-entry-war")
    parser.add_argument("--title", required=True, help="Working post title")
    parser.add_argument(
        "--base-dir",
        default="demo_posts",
        help="Base directory for post folders",
    )
    args = parser.parse_args()

    root = Path(args.base_dir) / f"{args.date}-{args.slug}"
    research_dir = root / "research"
    text_dir = root / "text"
    prompts_dir = root / "prompts"
    images_dir = root / "images"
    reviews_dir = root / "reviews"

    for path in [research_dir, text_dir, prompts_dir, images_dir, reviews_dir]:
        path.mkdir(parents=True, exist_ok=True)

    files = {
        root / "README.md": build_readme(args.title, args.slug),
        research_dir / "research.md": "# Research\n",
        research_dir / "fact_pack.md": "## Fact Pack\n",
        research_dir / "story_spine.md": """## Story Spine

- One-sentence story:
- This post answers:
- Main character or focal point:
- Central tension or conflict:
- Why now:
- Why the reader should care:
- Evidence ladder:
- Side angles to park:
""",
        text_dir / "post.md": "## 标题候选\n",
    }

    for path, content in files.items():
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    print(root)


if __name__ == "__main__":
    main()

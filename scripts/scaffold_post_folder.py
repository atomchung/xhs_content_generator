#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def build_readme(title: str, slug: str) -> str:
    return f"""# {title}

This folder is the workspace for one Xiaohongshu post.

## Folder layout

- `research/fact_pack.md`
  Main per-post research file: facts, numbers, source map, visual raw material, and open questions.
- `research/story_spine.md`
  Story-line checkpoint: one-sentence story, governing question, chosen angle, and parked side angles.
- `text/post.md`
  Drafting workspace for the final note.
- `prompts/`
  Web-ready prompt drafts and per-page prompt files.
- `images/`
  Manually generated images, curated screenshots, and edited deliverables.
- `reviews/`
  Publish reviews, postmortems, and iteration notes.

## Post metadata

- Slug: `{slug}`
- Status: `draft`
- Public note URL:
- Upstream backlog entry:
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
        research_dir / "fact_pack.md": """## Fact Pack

- Topic candidate:
- Why this is worth researching now:
- Current research status:

## What happened
- ...

## Why now
- ...

## Terms to translate
- ...

## Must-know facts
- ...

## Key numbers and context
- ...

## Source map
- Primary sources:
- Strong secondary sources:
- Open questions:

## Risks and unresolved
- ...

## Visual and story raw material
- Best scenes:
- Strongest protagonist:
- Possible tensions:
- Side angles to park:
""",
        research_dir / "story_spine.md": """## Story Spine

- One-sentence story:
- This post answers:
- Chosen angle:
- Main character or focal point:
- Central tension or conflict:
- Why now:
- Why the reader should care:
- What to keep:
- Side angles to park:
""",
        text_dir / "post.md": """## Working Brief

- One-sentence story:
- Title direction:

## 标题候选

## 正文

## 图组分工

## 来源尾注
""",
    }

    for path, content in files.items():
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    print(root)


if __name__ == "__main__":
    main()

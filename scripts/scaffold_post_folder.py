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
        text_dir / "post.md": """<!--
写正文前必须 Read skills/xhs-note-assembly/SKILL.md。
发布正文和图组分工是物理分开的两个 section，禁止混写。
-->

## Working Brief

- One-sentence story:
- Title direction:
- 目标读者画像（懂 / 半懂 / 完全不懂）:

## 写作前必答（每题一句话）

- [ ] 目标字数（150-300）：
- [ ] 几段（3-5）：
- [ ] 开头用 mystery 还是 number shock：
- [ ] 每段计划塞哪个数字：
- [ ] 收口用 hate_bait / 反转 / A-B-C / 二选一 哪一种：
- [ ] fact_pack.md 是否已经落盘（未落盘不准往下写）：

## 标题候选

1.
2.
3.

## 最终标题

-

## 发布正文（直接复制到小红书）

> 绝对禁区：本 section 禁止出现 `Page X / 第 X 图 / P1-P8 / 图组 / 图上文案`。
> 这一块就是读者看到的正文，其他字一律搬去下面的「图组分工」。

```
（贴小红书的正文放这里，150-300 字，3-5 段）
```

### 自检 checklist（发前必过）

- [ ] 字数 150-300
- [ ] 3-5 段，每段只回答一个问题
- [ ] 开头是 mystery 或 number shock，不是 contrast / in_media_res
- [ ] 每段至少 1 个数字
- [ ] 开场模块有一句可视化场景细节
- [ ] 收口不是「你怎么看」，而是 hate_bait / 反转 / A-B-C / 二选一
- [ ] 没有出现 `Page X / 第 X 图 / P1-P8`
- [ ] 没有英文黑话 / 术语堆叠
- [ ] 繁体已转简体（专有名词除外）

## 图组分工（读者看不到，是工作稿）

### 图 1（生图封面）
- 任务：
- 画面说明：

### 图 2
- 任务：
- 素材类型（真人 / 截图 / 生图）：
- 图上文案：

### 图 3
- 任务：
- 素材类型：
- 图上文案：

### 图 4
- 任务：
- 素材类型：
- 图上文案：

## 话题标签

-

## 来源尾注

-
""",
    }

    for path, content in files.items():
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    print(root)


if __name__ == "__main__":
    main()

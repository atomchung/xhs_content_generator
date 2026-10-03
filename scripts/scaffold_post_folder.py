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
按本轮任务读取共用 xhs-story / xhs-content；不要重跑已完成的选题。
发布正文和图组分工是物理分开的两个 section，禁止混写。
-->

## Working Brief

- One-sentence story:
- Title direction:
- 目标读者画像（懂 / 半懂 / 完全不懂）:

## 本轮需要解决的内容问题

- 观众为什么愿意继续读：
- 看完应该记住什么：
- 实际用到的事实与核对缺口：
- 还需要用户决定什么（已拍板的不重复问）：

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
（贴小红书的正文放这里，长度与结构服务故事）
```

### 自检 checklist（发前必过）

- [ ] 标题、封面和正文兑现同一个故事承诺
- [ ] 推进能让目标读者理解，不为凑段落或数字重复信息
- [ ] 用到的事实可追到来源，推论和待核明确
- [ ] 独立观众 review 的覆盖范围、结果与当版作品对应
- [ ] 没有出现 `Page X / 第 X 图 / P1-P8`
- [ ] 没有英文黑话 / 术语堆叠
- [ ] 繁体已转简体（专有名词除外）

## 图组分工（读者看不到，是工作稿）

### 图 1（封面；素材类型按故事选择）
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

按故事增减图数，不需要的页直接删除；不要为了模板凑四张。

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

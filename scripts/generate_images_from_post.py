#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


PROMPT_BLOCK_RE = re.compile(
    r"### 图(?P<index>\d+)\n.*?- prompt[:：]\n```text\n(?P<prompt>.*?)\n```",
    re.S,
)


@dataclass
class PromptBlock:
    index: int
    prompt: str


def parse_prompt_blocks(markdown: str) -> list[PromptBlock]:
    blocks: list[PromptBlock] = []
    for match in PROMPT_BLOCK_RE.finditer(markdown):
        blocks.append(
            PromptBlock(
                index=int(match.group("index")),
                prompt=match.group("prompt").strip(),
            )
        )
    if not blocks:
        raise ValueError("No image prompt blocks found in post.md")
    return sorted(blocks, key=lambda block: block.index)


def infer_output_dir(post_path: Path) -> Path:
    if post_path.parent.name == "text":
        return post_path.parent.parent / "prompts"
    return post_path.parent / "prompts"


def export_prompts(post_path: Path, output_dir: Path) -> None:
    markdown = post_path.read_text(encoding="utf-8")
    blocks = parse_prompt_blocks(markdown)

    output_dir.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Web-Ready Prompts From Post",
        "",
        "These prompts are exported for direct use in ChatGPT / Gemini style web UIs.",
        "This script does not call any image-generation API.",
        "",
        f"Source post: `{post_path}`",
        "",
    ]

    for block in blocks:
        prompt_path = output_dir / f"image_{block.index}_prompt.txt"
        prompt_path.write_text(block.prompt, encoding="utf-8")
        lines.extend(
            [
                f"## 图{block.index}",
                "```text",
                block.prompt,
                "```",
                "",
            ]
        )
        print(f"saved {prompt_path}")

    markdown_path = output_dir / "web_prompts.md"
    markdown_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"saved {markdown_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("post_path", type=Path)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()

    post_path = args.post_path.resolve()
    output_dir = (args.output_dir or infer_output_dir(post_path)).resolve()
    export_prompts(post_path=post_path, output_dir=output_dir)


if __name__ == "__main__":
    main()

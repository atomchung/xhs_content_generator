#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import re
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
import httpx
from openai import OpenAI


PROMPT_BLOCK_RE = re.compile(
    r"### 图(?P<index>\d+)\n.*?- prompt[:：]\n```text\n(?P<prompt>.*?)\n```",
    re.S,
)


@dataclass
class PromptBlock:
    index: int
    prompt: str


def load_env_from_workspace(start: Path) -> None:
    candidates = [start] + list(start.parents)
    for base in candidates:
        env_path = base / ".env"
        if env_path.exists():
            load_dotenv(env_path)
            return
    load_dotenv()


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


def generate_images(
    post_path: Path,
    output_dir: Path,
    provider: str,
    model: str,
    size: str,
    quality: str,
    output_format: str,
    consistency_mode: str,
    reference_image: Path | None,
) -> None:
    load_env_from_workspace(post_path.parent)
    markdown = post_path.read_text(encoding="utf-8")
    blocks = parse_prompt_blocks(markdown)

    output_dir.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, object] = {
        "post_path": str(post_path),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "provider": provider,
        "model": model,
        "size": size,
        "quality": quality,
        "output_format": output_format,
        "consistency_mode": consistency_mode,
        "images": [],
    }

    if provider != "openai":
        raise ValueError(f"Unsupported provider: {provider}")

    client = OpenAI()
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required for provider=openai")

    reference_image_path: Path | None = reference_image

    for block in blocks:
        image_path = output_dir / f"image_{block.index}.{output_format}"
        revised_prompt = None

        use_reference_edit = (
            consistency_mode == "first_image_edit"
            and block.index > 1
            and reference_image_path is not None
        )

        if use_reference_edit:
            edit_prompt = build_consistency_edit_prompt(block.prompt)
            payload = openai_edit_image(
                api_key=api_key,
                model=model,
                prompt=edit_prompt,
                reference_images=[reference_image_path],
                size=size,
                quality=quality,
                output_format=output_format,
            )
            image_data = payload["data"][0].get("b64_json")
            image_url = payload["data"][0].get("url")
            revised_prompt = payload["data"][0].get("revised_prompt")
        else:
            response = client.images.generate(
                model=model,
                prompt=block.prompt,
                size=size,
                quality=quality,
                output_format=output_format,
            )
            data_item = response.data[0]
            image_data = getattr(data_item, "b64_json", None)
            image_url = getattr(data_item, "url", None)
            if hasattr(data_item, "revised_prompt"):
                revised_prompt = data_item.revised_prompt

        if image_data:
            image_path.write_bytes(base64.b64decode(image_data))
        elif image_url:
            with urllib.request.urlopen(image_url) as remote:
                image_path.write_bytes(remote.read())
        else:
            raise RuntimeError(
                f"Image {block.index} returned neither b64 data nor url"
            )

        if reference_image_path is None:
            reference_image_path = image_path

        manifest["images"].append(
            {
                "index": block.index,
                "file": str(image_path),
                "prompt": block.prompt,
                "revised_prompt": revised_prompt,
                "used_reference_edit": use_reference_edit,
                "reference_image": str(reference_image_path) if use_reference_edit else None,
            }
        )
        print(f"saved {image_path}")

    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"saved {manifest_path}")


def build_consistency_edit_prompt(prompt: str) -> str:
    return (
        "Use the attached reference image only as a strict style and character anchor. "
        "Keep the same Japanese anime sports movie poster look, the same protagonist face design, "
        "the same palette, linework, lighting, jersey silhouette, emotional tone, and overall poster system. "
        "Do not reuse the exact pose or composition unless the new prompt asks for it. "
        "Avoid photorealism, uncanny faces, random English text, logos, watermarks, and mismatched styles. "
        f"{prompt}"
    )


def openai_edit_image(
    *,
    api_key: str,
    model: str,
    prompt: str,
    reference_images: list[Path],
    size: str,
    quality: str,
    output_format: str,
) -> dict:
    files = []
    handles = []
    try:
        for path in reference_images:
            handle = path.open("rb")
            handles.append(handle)
            files.append(
                (
                    "image",
                    (
                        path.name,
                        handle,
                        mimetypes.guess_type(path.name)[0] or "application/octet-stream",
                    ),
                )
            )

        data = {
            "model": model,
            "prompt": prompt,
            "input_fidelity": "high",
            "size": size,
            "quality": quality,
            "output_format": output_format,
        }
        with httpx.Client(timeout=600.0) as client:
            response = client.post(
                "https://api.openai.com/v1/images/edits",
                headers={"Authorization": f"Bearer {api_key}"},
                data=data,
                files=files,
            )
            response.raise_for_status()
            return response.json()
    finally:
        for handle in handles:
            handle.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("post_path", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--provider", default="openai")
    parser.add_argument("--model", default="gpt-image-1.5")
    parser.add_argument("--size", default="1024x1536")
    parser.add_argument("--quality", default="high")
    parser.add_argument("--output-format", default="png")
    parser.add_argument(
        "--consistency-mode",
        choices=["none", "first_image_edit"],
        default="first_image_edit",
    )
    parser.add_argument("--reference-image", type=Path)
    args = parser.parse_args()

    post_path = args.post_path.resolve()
    output_dir = args.output_dir or (post_path.parent / "images")
    generate_images(
        post_path=post_path,
        output_dir=output_dir,
        provider=args.provider,
        model=args.model,
        size=args.size,
        quality=args.quality,
        output_format=args.output_format,
        consistency_mode=args.consistency_mode,
        reference_image=args.reference_image.resolve() if args.reference_image else None,
    )


if __name__ == "__main__":
    main()

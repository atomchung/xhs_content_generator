# XHS Content Generator

Skill-first Xiaohongshu workflow for sports knowledge posts.

## Current workflow

1. `xhs-topic-angle-shortlist`
2. `xhs-fact-pack`
3. `xhs-visual-asset-mix`
4. `xhs-note-assembly`
5. `xhs-image-style-duo` when a page needs generated art
6. `xhs-publish-review` after publishing

## Repository structure

- `skills/`
  Current XHS workflow skills.
- `scripts/generate_images_from_post.py`
  Batch-generate images from prompt blocks already written into a markdown post.
- `scripts/overlay_cover_text.py`
  Add cover text overlays to finished images.
- `skills/xhs-image-style-duo/scripts/generate_style_duo.py`
  Build duo-style image prompts and optionally generate the images.

## Notes

- The legacy CrewAI pipeline has been removed from this repo.
- This repo now treats the skill workflow as the source of truth.

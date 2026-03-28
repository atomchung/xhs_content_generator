# XHS Content Generator

Skill-first Xiaohongshu workflow for sports knowledge posts.

## Current workflow

1. `xhs-topic-angle-shortlist`
2. `xhs-fact-pack`
3. `research/story_spine.md` checkpoint to lock one governing story before drafting
4. `xhs-visual-asset-mix`
5. `xhs-cover-template` when the first image needs a fixed big-subject cover system
6. `xhs-note-assembly`
7. `xhs-image-style-duo` when a generated page needs two style candidates
8. `xhs-publish-review` after publishing, then save the durable summary under `reviews/` and mirror it into the post workspace when useful

## Global content guardrails

Apply these rules across the whole XHS workflow:

1. Prefer Chinese over unnecessary English.
   If a sports league, rule, or business term is important, explain it in Chinese the first time it appears. Do not assume the reader understands English abbreviations.
2. Tell the story so a non-fan can follow it.
   Every post should quickly answer three questions for a new reader:
   - What is this?
   - Why is it hot right now?
   - Why should I care?
3. Jargon must earn its place.
   If a term only makes sense to existing fans and does not help the story, cut it or translate it into a simpler idea.
4. One post should tell one story.
   Before writing, decide the single question, conflict, or change the post will carry. Park the other valid angles instead of letting them crowd the main draft.

## Repository structure

- `skills/`
  Current XHS workflow skills.
- `notes/skills-audit.md`
  Durable audit table for the current skill system.
- `scripts/generate_images_from_post.py`
  Batch-generate images from prompt blocks already written into a markdown post.
- `scripts/overlay_cover_text.py`
  Add cover text overlays to finished images.
- `skills/xhs-image-style-duo/scripts/generate_style_duo.py`
  Build two style-candidate image prompts and optionally generate the images.

## Notes

- The legacy CrewAI pipeline has been removed from this repo.
- This repo now treats the skill workflow as the source of truth.

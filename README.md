# XHS Content Generator

Skill-first Xiaohongshu workflow for sports knowledge posts.

## Current workflow

1. `xhs-topic-angle-shortlist`
2. `xhs-fact-pack`
3. `research/story_spine.md` checkpoint to lock one governing story before drafting
4. `xhs-visual-asset-mix`
5. `xhs-note-assembly`
6. `xhs-image-style-duo` when a page needs generated art
7. `xhs-publish-review` after publishing, then save the durable summary under `reviews/` and mirror it into the post workspace when useful

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
   Before writing, decide the single question, conflict, or change the post will carry. Park the other valid angles in notes instead of letting them crowd the main draft.

## Repository structure

- `skills/`
  Current XHS workflow skills.
- `demo_posts/<date>-<slug>/`
  One folder per post. Store research, fact pack, final text, prompts, and generated images inside that post workspace.
- `demo_posts/<date>-<slug>/research/story_spine.md`
  One-story framing checkpoint: what question the post answers, what tension carries it, and which side angles get parked.
- `demo_posts/<date>-<slug>/reviews/`
  Local post workspace reviews and postmortems for that specific post.
- `reviews/`
  Durable publish-review archive for cross-post learning and git-tracked summaries.
- `notes/`
  Durable implementation notes and operating rules that should be reusable across sessions and agents.
- `scripts/generate_images_from_post.py`
  Batch-generate images from prompt blocks already written into a markdown post.
- `scripts/overlay_cover_text.py`
  Add cover text overlays to finished images.
- `scripts/scaffold_post_folder.py`
  Create a standard post workspace with `research/`, `text/`, `prompts/`, `images/`, and `reviews/`.
- `skills/xhs-image-style-duo/scripts/generate_style_duo.py`
  Build duo-style image prompts and optionally generate the images.
- `hypo.md`
  Shared hypothesis board for testing storytelling techniques across posts.

## Notes

- The legacy CrewAI pipeline has been removed from this repo.
- This repo now treats the skill workflow as the source of truth.

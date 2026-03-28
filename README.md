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
   Before writing, decide the single question, conflict, or change the post will carry. Park the other valid angles in notes instead of letting them crowd the main draft.

## Repository structure

- `skills/`
  Current XHS workflow skills.
- `demo_posts/<date>-<slug>/`
  One folder per post-shaped idea. It can be a draft, a parked idea, or a published post, but it should already have one concrete story angle.
- `demo_posts/<date>-<slug>/README.md`
  Workspace metadata. Record whether the post is `draft`, `parked`, or `published`, then add the public note URL after publishing.
- `demo_posts/<date>-<slug>/research/story_spine.md`
  One-story framing checkpoint: what question the post answers, what tension carries it, and which side angles get parked.
- `demo_posts/<date>-<slug>/reviews/`
  Local post workspace reviews and postmortems for that specific post.
- `explorations/`
  Cross-post exploration space for ideas that are not yet one concrete post.
- `explorations/series/`
  Multi-post topic systems, recurring franchises, and longer-term content lanes.
- `explorations/visuals/`
  Cover systems, style tests, and reusable visual directions.
- `explorations/workflows/`
  Process experiments, prompt-method tests, and production workflow trials.
- `reviews/`
  Durable publish-review archive for cross-post learning and git-tracked summaries.
- `reviews/published-history.md`
  Running index of posts that were actually published, linked to the public note, workspace, and review file.
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
- `xhs_content_generator` is the account-specific repo for the current sports Xiaohongshu account.
- Local sibling repo `xhs_skills/` is the upstream, more generic skill set. A rule should only be promoted back there after it proves reusable across accounts.

## Drafts vs Explorations

Use `demo_posts/` when the work is already post-shaped:

- there is a concrete angle
- there is a likely title direction
- the work may become a publishable note

Use `explorations/` when the work is still cross-post or pre-post:

- a theme series that may spawn many posts
- a visual language or cover template
- a workflow or prompt experiment
- a creator benchmark or account-direction study

Explicit trigger examples:

- Send to `explorations/` when the ask sounds like:
  - "帮我想一个系列"
  - "先做主题规划"
  - "探索一下这个视觉方向"
  - "沉淀一个模板"
  - "研究类似作者"
  - "先别落成具体帖子"
- Send to `demo_posts/` when the ask sounds like:
  - "帮我做这篇"
  - "这个题今天想发"
  - "给我这条的标题和正文"
  - "围绕这个事件出一篇"
  - "先做这个题的切角"

Rule of thumb:

- `demo_posts/` = one post workspace
- `explorations/` = one idea can feed many posts

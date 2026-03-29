# XHS Content Generator

Skill-first Xiaohongshu workflow for sports knowledge posts.

## Current workflow

Default user-facing flow:

1. Do topic ideation and maintain a reusable backlog:
   - return `2-3` topic / possible-angle candidates
   - pick one topic worth researching now
   - save the other ideas back into the cross-post backlog
2. Once one topic is worth continuing, scaffold `demo_posts/<date>-<slug>/`.
3. Build `research/fact_pack.md` as the main per-post research file:
   - what happened
   - why now
   - must-know facts
   - key numbers
   - source map
   - visual and story raw material
4. Turn the research into `research/story_spine.md`:
   - one-sentence story
   - governing question
   - chosen angle
   - core tension
   - what to keep and what to park
5. Turn `fact_pack + story_spine` into the publishable post:
   - title
   - body copy
   - page `1-4` on-image copy
   - default body shape: total judgment, necessary background, conflict / hook
6. Lock the cover before doing the rest of the images:
   - cover structure
   - cover title text
   - one recommended style by default
   - one ready-to-paste final prompt
7. After the cover direction is locked, finish the remaining pages:
   - recommend real images / official screenshots when they are better
   - otherwise give ready-to-paste final prompts
8. After publishing, run publish review and sync durable learning back into `reviews/` and `hypo.md`.

Core workflow skills:

- `xhs-topic-angle-shortlist`
  Use for topic ideation, possible-angle generation, and backlog maintenance before one topic is chosen for deep research.
- `xhs-fact-pack`
  Use as the main per-post research layer after one topic is chosen, before the final story line is locked.
- `xhs-note-assembly`
  Use after `fact_pack + story_spine` are ready and the team wants the publishable post.

Optional skill branches:

- `xhs-visual-asset-mix`
  Only when `real image vs screenshot vs generated image` is genuinely unclear.
- `xhs-cover-template`
  Only when the default cover system does not fit the post.
- `xhs-image-style-duo`
  Use when a page needs a generated-image prompt; default to one web-ready final prompt, and switch to two prompts only when the user explicitly wants a comparison.
- `xhs-publish-review`
  Only after publishing.

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
- `notes/skills-audit.md`
  Durable audit table for the current skill system.
- `demo_posts/<date>-<slug>/`
  One folder per post being actively researched or drafted.
- `demo_posts/<date>-<slug>/README.md`
  Workspace metadata. Record whether the post is `draft`, `parked`, or `published`, then add the public note URL after publishing.
- `demo_posts/<date>-<slug>/research/fact_pack.md`
  The main per-post research file: facts, numbers, source map, visual raw material, and open questions.
- `demo_posts/<date>-<slug>/research/story_spine.md`
  The story-line checkpoint that turns research into one chosen story: what question the post answers, what tension carries it, and which side angles get parked.
- `demo_posts/<date>-<slug>/reviews/`
  Local post workspace reviews and postmortems for that specific post.
- `explorations/`
  Cross-post exploration space for ideas that are not yet one concrete post.
- `explorations/backlog/`
  Cross-post topic backlog, possible-angle backlog, and importance tracking.
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
  Export per-image prompt files and `web_prompts.md` for direct use in ChatGPT / Gemini style web UIs. It does not call image APIs.
- `scripts/overlay_cover_text.py`
  Add cover text overlays to finished images.
- `scripts/scaffold_post_folder.py`
  Create a standard post workspace with `research/`, `text/`, `prompts/`, `images/`, and `reviews/`.
- `skills/xhs-image-style-duo/scripts/generate_style_duo.py`
  Export one recommended final prompt by default, or two prompts in explicit compare mode, for direct use in ChatGPT / Gemini style web UIs. It does not call image APIs.
- `hypo.md`
  Shared hypothesis board for testing storytelling techniques across posts.

## Notes

- The legacy CrewAI pipeline has been removed from this repo.
- This README is the top-level workflow source of truth for the repo.
- Individual skills should implement the steps and exception branches defined here rather than redefining a separate default flow.
- `xhs_content_generator` is the account-specific repo for the current sports Xiaohongshu account.
- Local sibling repo `xhs_skills/` is the upstream, more generic skill set. A rule should only be promoted back there after it proves reusable across accounts.

## Drafts vs Explorations

Use `demo_posts/` when the work is already post-shaped:

- there is one topic worth actively researching
- the work now needs a fact pack or story line
- the work may become a publishable note soon

Use `explorations/` when the work is still cross-post or pre-post:

- a topic or angle backlog entry
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

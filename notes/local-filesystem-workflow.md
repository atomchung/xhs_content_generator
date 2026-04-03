# Local Filesystem Workflow

## Purpose

This note defines the recommended local filesystem workflow for this repo as of 2026-03-21.

It is meant to answer:

- where each kind of work should live
- what stays local-only
- what should be durable and git-tracked
- how one post should move through the repo from idea to publish review

## Guiding Idea

Treat the repo as four layers:

1. workflow tools
2. cross-post backlog and explorations
3. per-post working folders
4. durable learning artifacts

Do not mix these layers together.

## Layer 1: Workflow Tools

These are reusable assets that define how work gets done.

### `skills/`

Use `skills/` for stable workflow instructions.

Current pipeline:

1. `xhs-topic-angle-shortlist`
2. `xhs-fact-pack`
3. `research/story_spine.md` checkpoint
4. `xhs-note-assembly` - default `publish-ready copy` plus a minimum per-page storyboard
5. `xhs-cover-template` quick cover check - escalate only when the default cover system does not fit
6. `xhs-visual-asset-mix` - only when remaining pages still need material routing
7. `xhs-image-style-duo`
8. `xhs-publish-review`

Do not put one-off post outputs in `skills/`.

### `scripts/`

Use `scripts/` for reusable automation.

Current important scripts:

- `scripts/scaffold_post_folder.py`
- `scripts/generate_images_from_post.py` - export web-ready prompt files from `post.md`, no API image generation
- `scripts/overlay_cover_text.py`

If a repeated workflow still requires manual shell steps every time, consider promoting it into `scripts/`.

## Layer 2: Cross-Post Backlog And Explorations

### `explorations/backlog/`

Use this folder for:

- topic ideas that can feed many future posts
- possible angles that are not yet one final story line
- importance updates and next-review dates

When one topic becomes one active post, move downstream into:

- `demo_posts/<date>-<slug>/`

## Layer 3: Per-Post Working Folders

### `demo_posts/<date>-<slug>/`

Each post should get one workspace folder.

Recommended structure:

```text
demo_posts/<date>-<slug>/
├── README.md
├── research/
│   ├── fact_pack.md
│   └── story_spine.md
├── text/
│   └── post.md
├── prompts/
├── images/
└── reviews/
```

### When to create the folder

Create the post folder as soon as a topic is chosen and the team intends to continue.

Use:

```bash
python3 scripts/scaffold_post_folder.py --date YYYY-MM-DD --slug <slug> --title "<working title>"
```

### What each file is for

#### `research/fact_pack.md`

This is the main per-post research file.

Use it for:

- what happened
- why now
- must-know facts
- key numbers
- source map
- risks and unresolved points
- visual and story raw material

#### `research/story_spine.md`

This is the story-line checkpoint that turns research into one chosen story.

Write here before drafting:

- the one-sentence story
- the single governing question
- the main character or focal point
- the central conflict
- why now
- why the reader should care
- side angles to park

If the post cannot be summarized cleanly here, do not draft yet.

#### `text/post.md`

- title candidates
- final title
- final body
- image duties
- source list

#### `prompts/`

- image prompt drafts
- per-style prompt variants
- visual plan notes

#### `images/`

- manually generated images
- curated screenshots / photos
- edited exports
- final deliverables

#### `reviews/`

- full post-specific publish reviews
- image-sequence observations
- postmortem notes tied to this one case

## Layer 4: Durable Learning Artifacts

These should be git-tracked because they are useful beyond one post.

### `reviews/`

Use root `reviews/` for durable, cross-post publish-review summaries.

File naming:

```text
reviews/YYYY-MM-DD-<slug>.md
```

This is the tracked archive.

If a post also has a local case workspace, mirror the fuller review into:

```text
demo_posts/<date>-<slug>/reviews/YYYY-MM-DD-publish-review.md
```

### `hypo.md`

Use `hypo.md` for cross-post storytelling hypotheses.

Only store reusable learnings here:

- what narrative technique we are testing
- whether it is active, supported, mixed, or retired
- which cases informed the update

Do not turn `hypo.md` into a dumping ground for one-off comments.

### `notes/`

Use `notes/` for durable implementation notes and operating rules.

Good examples:

- how to read Xiaohongshu post HTML and images
- how local filesystem workflow should work
- repeated manual procedures that future agents should not rediscover from scratch

## Git Tracking Rules

### Tracked by default

- `skills/`
- `scripts/`
- `reviews/`
- `notes/`
- `hypo.md`
- `README.md`

### Local-only by default

- `demo_posts/`
- `runs/`
- `tmp/`
- `db/`
- `xhs_skills/`

Important detail:

`demo_posts/` is currently ignored in `.gitignore`, so it is a local working area rather than the durable repo history.

That means:

- detailed post work can live there
- final reusable lessons should be copied into tracked files

## Recommended End-to-End Flow

1. Choose a topic with `xhs-topic-angle-shortlist`.
2. Update `explorations/backlog/` with active, watch-later, or parked ideas.
3. Scaffold `demo_posts/<date>-<slug>/`.
4. Build `research/fact_pack.md`.
5. Lock the story in `research/story_spine.md`.
6. Draft the post in `text/post.md`.
7. Plan prompt variants in `prompts/`.
8. Generate and curate assets in `images/`.
9. Publish.
10. Write a durable summary to `reviews/YYYY-MM-DD-<slug>.md`.
11. If the review changes our storytelling rules, update `hypo.md`.
12. If the workflow itself changed, update `notes/` or the relevant skill.

## Rules Of Thumb

- One post folder per topic, not one giant scratchpad.
- One post should tell one story.
- Put working mess in `demo_posts/`; put reusable lessons in tracked files.
- If something needs to survive sessions, it must live in a tracked note, review, script, or skill.
- If a manual workflow repeats, turn it into a script or a note.

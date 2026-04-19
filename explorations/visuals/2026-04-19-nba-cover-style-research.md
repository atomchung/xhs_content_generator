# NBA Cover Style Research — 2026-04-19

> Source experiment: `~/Side_project/xhs_autoresearch/`
> Subject held constant: LeBron James / tomahawk dunk
> Total: 30 original styles + 14 mutation attempts = 44 AI image variants reviewed
> Judge: Claude Opus 4.7 for text-level A/B, then human review on actual generated images

---

## TL;DR

- **One style wins everything. Stop hunting for more.**
- The canonical S1-i "3D comic panel break-out" prompt beats all 14 mutation attempts
- Any addition to the prompt (watercolor wash, speed lines, aura, gold leaf, geometric beams) makes it worse — busy backgrounds fight the subject
- Keep this prompt locked, only swap `{player}` and `{action}`
- Multi-arm / multi-ball glitches are generation-time issues, not prompt issues — solve by re-generating, not by editing the prompt

---

## 🏆 Locked Canonical Prompt

```
3D comic panel break-out illustration, {PLAYER_NAME} breaking through the comic panel frame,
{ACTION_PHRASE} in foreground bursting toward viewer, torn comic panel edges as frame,
Ben-day dots visible on receding background panels, Arturo Torres bold black outlines,
the basketball casting shadow onto the panel surface, dramatic foreshortening with exaggerated forearm and hand,
pop-art colored background (crimson + cobalt + goldenrod), photorealistic foreground transition on the player,
Jack Kirby superhero energy, cinematic composition, vertical 3:4 aspect --ar 3:4 --stylize 250
```

**Only two variables allowed:**
- `{PLAYER_NAME}` — e.g. `LeBron James`, `Luke Kennard`, `Rui Hachimura`
- `{ACTION_PHRASE}` — e.g. `mid-air tomahawk dunk`, `step-back three-pointer release`, `mid-range turnaround jumper`

**Do NOT modify anything else. Every phrase earned its spot by surviving 14 elimination rounds.**

---

## Reference Renders (human-approved)

The canonical prompt with `LeBron James` + `mid-air tomahawk dunk` is the calibration reference. When generating for a new player/action, compare output against this reference for:

- Break-out frame visibility (torn comic panel edges)
- Ben-day dots on receding background
- Crimson + cobalt + goldenrod color balance
- Foreshortening on the raised arm/hand
- Bold Arturo Torres black outlines
- Photorealistic player transitioning into pop-art background

---

## What was tested and rejected

### Phase D — Alternative artist/trend-backed styles (4 tried, all rejected)
- **D-1a Tyson Beck playoff branding** — too dark overall
- **D-1b Tyson Beck crop minimal** — clean but subject too dark
- **D-4a Blueprint technical explosion** — text illegible, no visual burst, can't carry CTR
- **D-4b Blueprint minimalist** — same issue as D-4a

### Phase E — S1-i direct mutations (4 tried, human approved 2 but later surpassed by original)
- E-1 ball-burst (球破框) — approved initially
- E-2 three-panel sequence (多格連續) — approved initially
- E-3 diagonal tear — not tested
- E-4 SFX typography — not tested

### Phase F Round 1 — Original 4/12 pool re-test (4 tried, 3 rejected, 1 kept)
- S6-d gold leaf — kept as #2 (only bright watercolor variant that survives)
- S6-i duotone risograph — rejected by user
- **H-2 watercolor + comic speed lines** — ranked #1 in this round
- H-7 geometric comic + watercolor aura — rejected

### Phase F Round 2 — Remaining v2 ≥ 4/6 originals (3 tried, all rejected)
- S6-a ink splash — black ink fights the subject, pointless overlap
- S6-e Chinese ink wash — more ink = dirtier canvas, bad
- H-3 Pop Art + watercolor edge — background too saturated, feels shrill

### Phase F Round 3 — H-2 deep-dive mutations (4 tried, all rejected)
- H-2 + geometric beams + Kirby crackle — background too busy
- H-2 warm-dominated palette — background too busy
- H-2 watercolor-infused figure — background too busy + subject tension drops
- H-2 watercolor aura — background too busy + subject tension drops

---

## Hard Boundaries (learned from failures)

### Color / lighting
- ❌ Dark / moody / desaturated palettes
- ❌ Over-saturated hot-pop colors (Pop Art territory is shrill, not bright)
- ✅ Bright high-key Kirby 64-color (crimson + cobalt + goldenrod) — the ONE working palette

### Composition
- ❌ Minimal / blueprint / infographic aesthetic — can't carry CTR
- ❌ Large text overlay as the visual hero — AI renders text as mush
- ❌ Multi-character scenes (split panels, two players posing) — AI can't stabilize
- ❌ Geometric beams / auras / light explosions added to background — compounds clutter
- ❌ Watercolor washes as background — either dirty or competing for attention

### Anatomy / object handling
- ❌ `photorealistic` on player simultaneously with `exaggerated heroic proportions` → AI renders duplicate arms
- ❌ Mentioning `basketball` + `ball casting shadow` + `ball at release` in one prompt → AI renders multiple balls
- ✅ One basketball, one raised hand, tucked other arm — solve at generation time with re-rolls and negative params

### Ink / painterly additions
- ❌ Black sumi ink splatter — competes with Arturo Torres outlines, visually fights
- ❌ High-density brushwork / layered Chinese ink — looks dirty
- ✅ Flat Ben-day dot shading + clean bold outlines is the only non-redundant ink language

---

## Generation-time tactics for multi-arm / multi-ball glitches

These belong to generation, not prompt engineering:

1. Generate 4–8 variations per prompt and pick the clean one
2. For Midjourney: append `--no duplicate limbs, duplicate basketballs, extra arms`
3. Lock `--seed` once you find a clean variant, then port to other players/actions
4. If flux/leonardo: lower guidance scale slightly (~6.5) to reduce prompt rigidity that causes AI to over-render anatomy

---

## Action Description Library

When filling `{ACTION_PHRASE}`, use these verified patterns:

| Action type | Pattern | Example |
|---|---|---|
| Dunk | `mid-air {variant} dunk` | `mid-air tomahawk dunk`, `mid-air windmill dunk` |
| Step-back 3 | `{variant} three-pointer release` | `step-back three-pointer release` |
| Mid-range | `{variant} jumper` | `mid-range turnaround jumper`, `mid-range fadeaway jumper` |
| Drive layup | `{variant} layup` | `Euro-step layup`, `reverse layup` |
| Pass | `no-look {variant} pass` | `no-look bounce pass`, `no-look cross-court pass` |

**Do not over-describe the action.** The canonical prompt's `dramatic foreshortening with exaggerated forearm and hand` line already handles the visual treatment — the action phrase just needs to be a 3-4 word label.

---

## Team / Player Color Reference

When generating, mentally note the player's current team for palette alignment (the canonical prompt's crimson+cobalt+goldenrod works regardless, but the player's jersey should render team-correct):

| Player | Team | Jersey primary | Accent |
|---|---|---|---|
| LeBron James | LAL | Lakers purple | gold |
| Rui Hachimura (八村塁) | LAL | Lakers purple | gold |
| Luke Kennard | MEM | Grizzlies navy | powder blue |
| Stephen Curry | GSW | Warriors royal blue | gold |
| Nikola Jokic | DEN | Nuggets navy | gold |
| Giannis | MIL | Bucks green | cream |
| SGA | OKC | Thunder orange | turquoise |

---

## Integration with xhs-skills

When any skill needs an NBA cover illustration:

1. Read this file — take the canonical prompt
2. Substitute `{PLAYER_NAME}` and `{ACTION_PHRASE}` from the post's subject
3. Generate 4–8 variations, pick the clean anatomy
4. Do NOT try to "improve" the prompt with additional descriptors — it has been exhaustively tested

**Skill-layer guardrails (must enforce):**
- Reject any prompt that adds `watercolor`, `aura`, `speed lines`, `beams`, `gold leaf`, `Chinese ink`, `geometric`, `blueprint`, `minimal`, `dark`, `moody`, `Pop Art color`
- Reject any prompt that omits `photorealistic foreground transition on the player`
- Reject any prompt that omits `--ar 3:4 --stylize 250`

---

## Research artifact trail

Full experiment log lives in `~/Side_project/xhs_autoresearch/`:
- `styles_catalog.md` — All 30 original styles with v1/v2 judge scores + human-verification outcomes
- `templates/style_01_3d_break_out.md` — Full Style 01 spec with anti-duplicate technique library
- `new_style_exploration.md` — Phase D candidates derived from web-researched viral NBA artists (Tyson Beck, Arturo Torres, Ryan Simpson)
- `runs/nba_style_exp_v2/` — Raw 30-round A/B logs
- `runs/nba_style_exp/` — Original 4/12 run with Gemini 2.5 Flash judge

---

## Open questions for next round

1. **Cross-subject stability** — does the canonical prompt hold quality when swapped to other players/actions? Test set proposed: LeBron dunk (baseline) + Kennard step-back 3 + Rui mid-range + Curry 3 + Jokic no-look pass
2. **Is there a Style 02?** — This research only locks down "the comic break-out style." If the account wants a second stylistic axis for variation (e.g. Anime Cover / Mascot Q in the production style_duo), that's a separate research track.
3. **Seed-based consistency** — once a clean LeBron render is achieved, does locking seed transfer to other subjects for consistency across a post series?

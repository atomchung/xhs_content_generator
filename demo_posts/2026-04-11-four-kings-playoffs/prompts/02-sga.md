## 这张图的任务

SGA 单人介绍卡 v2。**人物大、动作有张力**，文字模块位于画面**正中央**（和封面横带同位置），分成两个独立小模块：标题文字 + 战绩数据。

## 版式结构

```
┌──────────────────────────────┐  3:4 竖版，SGA 大图占满整个画布
│                              │
│   SGA 上半身 / 头 / 出手臂      │  ← ~35% 高度，人物头部 + 持球臂
│   动态、有张力                 │
│                              │
├══════════════════════════════┤
│  联盟第一人 ｜ 卫冕冠军         │  ← 标题模块 ~14%（同封面横带样式）
│         S G A               │     实色黑底 + 金色上下边
├──────────────────────────────┤  ← 两模块之间留 ~3% 视觉空隙
│  🏆 冠军 × 1                 │
│  🏆 MVP × 1                  │  ← stats 模块 ~14%（独立小卡片）
│  🏆 得分王 × 1               │     深色底，三行金色图标 + 字
├══════════════════════════════┤
│                              │
│   SGA 下半身 / 跳投腿姿        │  ← ~34% 高度，人物腿部
│                              │
└──────────────────────────────┘
```

**关键概念**：人物图是**整张画布的底层**，full-body 在画面里被中间的两个文字 panel **遮住中段**，所以观众看到的是"上半身从 panel 上方探出来 + 下半身从 panel 下方露出来"的效果。人物本身的物理姿态是完整全身，只是中段被 UI 挡住。

## 文字模块规格

### Module 1 — 标题模块（同封面横带）

- 实色黑底 `#0a0a0a`，上下两条 2px 金色细线作为边
- 第 1 行（小标签）：`联盟第一人 ｜ 卫冕冠军` — Alibaba PuHuiTi Heavy，白色，小字
- 第 2 行（人名）：`SGA` — Alibaba PuHuiTi Heavy，纯金色 `#FFD700`，最大字号
- 占画面 ~14% 高度

### Module 2 — 战绩数据模块（独立小卡片，和标题分开）

- 在标题模块下方留 ~3% 视觉空隙后是这块
- 实色黑底 `#0a0a0a`，但只用一条 2px 金色细线作为底边（和上方标题视觉上区分但同系列）
- **三行**，每行格式：`[金色奖杯图标] [奖项] × [数量]`
  - `🏆 冠军 × 1`
  - `🏆 MVP × 1`
  - `🏆 得分王 × 1`
- 字体：Alibaba PuHuiTi Heavy，白色 fill，奖杯图标金色 `#FFD700`
- 三行垂直堆叠，左对齐或居中
- 占画面 ~14% 高度
- **不要写完整数据**（PPG / FG% / streak 全部移到正文 post.md，封面和卡都不出现）

## 人物动作：中距离急停后仰跳投（更大、更有张力）

- **不一定全身**——人物本身物理上是完整的，但被中间 panel 挡住中段
- 视觉上**头 + 出手臂**在 panel 上方，**腿 + 脚**在 panel 下方
- 出手瞬间的最高点：右臂完全伸直、肘部锁死、球刚离开指尖
- 球的位置在画面**最顶边**或紧贴顶边——给"刚出手"的速度感
- 身体后仰幅度更大，腰部明显往后弯
- 脸：冷峻、嘴角一丝若有若无的笑、眼神锁死前方
- 下半身：双脚都已经离地（处于跳投空中阶段），脚尖朝下
- 镜头：低角度仰拍 + 略微 3/4 侧角，让出手臂的延伸感最大化

## Final Prompt

```text
Vertical 3:4 single-character INTRODUCTION CARD in the exact style of Blue Lock (ブルーロック) character key visuals and the First Slam Dunk 2022 movie poster — modern clean digital flat shading, thin neon outlines, cold cinematic lighting, icy desaturated base palette with saturated gold neon accents.

LAYERED COMPOSITION: the player illustration is the FULL-CANVAS background layer (fills the entire 3:4 frame from edge to edge). Two separate text modules are overlaid on top of the player at the vertical CENTER of the card — they hide the player's mid-section but his upper body (head + shooting arm) is clearly visible ABOVE the modules and his lower body (legs + feet) is clearly visible BELOW the modules.

BACKGROUND-LAYER ILLUSTRATION (full canvas):
A lean sleek NBA point guard in an Oklahoma City Thunder blue-and-orange jersey #2, captured at the absolute APEX of his signature MID-RANGE PULL-UP FADEAWAY — body in mid-air at the peak of the jump, both feet off the ground, body arched backward in a deep pronounced fadeaway lean, right shooting arm fully extended straight up at maximum reach with elbow locked, the ball just released from his fingertips and floating at the very TOP edge of the canvas, left arm trailing for balance. Cold emotionless face with the faintest knowing smirk of a man who already knew it was going in, sharp jawline, short dark hair, eyes locked dead ahead. Long elongated athletic limbs giving the pose maximum tension and reach. Camera: low angle hero shot looking UP from below his waist, slight 3/4 side angle, so his arm extension reads as impossibly long and the body fadeaway lean is dramatic.

The player illustration is intentionally LARGER than the canvas can fit — his head is near the top, his ball is at the top edge, and his feet are near the bottom. The middle of his torso is positioned right where the text modules will overlay. He must be the brightest, most saturated element in the image.

Behind him: a faint watermark-level silhouette of the OKLAHOMA CITY THUNDER PRIMARY SHIELD LOGO (shield outline with a basketball inside, NO "OKC" text, NO "THUNDER" text, just the bare shield+ball symbol), rendered in deeply muted dark teal-charcoal, low saturation, clearly behind the subject. Gold neon rim-light on his silhouette. Thin warm-gold atmospheric particles. Deep teal-charcoal base. NO ego-beast, NO mascot, NO HUD overlays inside the player area.

OVERLAY MODULE 1 — TITLE BAND (positioned at vertical center, ~45% from top):
A solid horizontal band overlaying the player's torso. Fill: pure solid black (#0a0a0a), fully opaque, no transparency. Top and bottom edges bordered by thin 2px gold pinstripe lines (matching the cover series style). Band height: ~14% of total poster height.

Inside Module 1, two rows of text:
- ROW A (small, white): "联盟第一人 ｜ 卫冕冠军" in Alibaba PuHuiTi Heavy, pure white, no outline, horizontally centered. ~30% of band height.
- ROW B (largest text on the entire card): "SGA" in Alibaba PuHuiTi Heavy, pure GOLD (#FFD700), thin 1px black outline, horizontally centered with generous letter-spacing. ~60% of band height. This must be the single biggest text element on the card.

VISUAL GAP: a clean ~3% gap between Module 1 and Module 2 — in this gap, a thin sliver of the player illustration is visible (his belt or waist line peeks through), confirming the modules are separate floating overlays.

OVERLAY MODULE 2 — TROPHY STAT PANEL (positioned directly below Module 1, ~62% from top):
A separate solid horizontal panel, smaller than Module 1. Fill: pure solid black (#0a0a0a), fully opaque. Bottom edge bordered by a single 2px gold pinstripe line. Panel height: ~14% of total poster height.

Inside Module 2, exactly THREE rows of text, each row showing one trophy achievement:
- Row 1: a small gold trophy icon (golden cup, flat-shaded, NOT photoreal) followed by "冠军 × 1"
- Row 2: a small gold trophy icon followed by "MVP × 1"
- Row 3: a small gold trophy icon followed by "得分王 × 1"

Text style: Alibaba PuHuiTi Heavy or bold sans-serif, white fill, no outline. Trophy icons: pure gold #FFD700, simple flat silhouette (NOT 3D, NOT photoreal). All three rows horizontally centered as a block, left-aligned within that block so the trophy icons line up vertically. Three rows ONLY — no fourth row, no extra stats, no PPG, no FG%, no streak counters.

RESULT: the viewer sees the player's head and shooting arm in the top ~35% of the card, then the title band (Module 1) and trophy panel (Module 2) stacked in the central ~30%, then the player's legs and feet in the bottom ~35%.

Style notes: Blue Lock / First Slam Dunk aesthetic. NOT manga ink, NOT painterly, NOT photorealism. Clean flat shading, thin neon outlines, sharp legible typography. Player illustration must extend cleanly above and below both overlay modules — the head and arm fully visible at top, the legs and feet fully visible at bottom. NO text bleed outside the modules. NO HUD inside the player illustration zones. Aspect ratio 3:4 vertical.
```

## 如果要继续改

- Module 1 / Module 2 没有视觉间隔，黏在一起 → 强调 "a clean visible 3% gap between Module 1 and Module 2, the player's waist must peek through this gap"
- 人物中段没有被 panel 挡住，整个 panel 飘在他身上很怪 → 强调 "the modules are opaque solid black, they completely hide the player's torso behind them"
- 人物腿部没出来 → 强调 "the player's lower body (knees/legs/feet) must be clearly visible below Module 2"
- 出手臂没在 panel 上方 → 强调 "the shooting arm and the ball must be ABOVE Module 1, in the top 35% of the canvas"
- 奖杯图标变成立体 3D 渲染 → 强调 "flat 2D gold silhouette icons, NOT 3D, NOT realistic trophies"
- 出现 4 行或更多 stat → 强调 "EXACTLY 3 rows in Module 2: 冠军, MVP, 得分王 — no more, no less"

## 不要动什么

- 3:4 纵向比例
- 双 module 中央堆叠（标题 + 战绩分开）
- Module 1 标题模块 = 实色黑 + 金色上下边 + 标签 + SGA 金色大字
- Module 2 战绩模块 = 实色黑 + 金色下边 + 三行 trophy icon + 字
- 两 module 之间的可见间隔（人物腰部从中间露出）
- 人物头 + 臂在上方，腿在下方
- OKC 盾形 watermark 背景（不是吉祥物，不带文字）
- 中距离急停后仰的签名动作 + 出手最高点
- Blue Lock flat-shaded 数码画风
- Stats 锁死三行：冠军 / MVP / 得分王

## 事实校正

- ✅ 1× 冠军（2025 NBA Finals 冠军）
- ✅ 1× MVP（2024-25 赛季 MVP）
- ✅ 1× 得分王（2024-25 赛季得分王 32.7 PPG）
- ❌ 不要写他场均、命中率等具体数字（已搬到 post 正文）
- ❌ 不要写"DPOY"等防守奖项（他没有）

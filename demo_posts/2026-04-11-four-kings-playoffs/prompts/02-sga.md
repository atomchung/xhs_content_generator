## 这张图的任务

SGA 单人介绍卡 v3。**人物再放大 —— 脸至少占画面 20%**。只保留**一个**文字模块（标题模块，与封面同款横带）位于画面正中央。**Stats 不再用框装**，直接以浮动文字+发光效果贴在人物图上，融为画面一部分。

## 版式结构

```
┌──────────────────────────────┐  3:4 竖版
│                              │
│   SGA 巨大头部 + 出手臂       │  ← 头部就占 ~20%，张力极强
│   动态、有张力                │
│   （旁边浮动 stats 文字）     │  ← stats 直接贴在画面上,无框
│                              │
├══════════════════════════════┤
│  联盟第一人 ｜ 卫冕冠军        │  ← 唯一的文字模块 ~14%
│         S G A               │     实色黑底 + 金色上下边
├══════════════════════════════┤
│                              │
│   SGA 下半身 / 跳投腿姿       │  ← 人物腿部
│                              │
└──────────────────────────────┘
```

**关键概念**：
- 人物图是整张画布的底层，**脸至少占 20% 画布**
- 中间只有**一条**横带（标题模块）挡住人物中段
- Stats 是**浮动文字**，直接 paint 在人物图上的空白区域，没有任何 panel/box，靠金色发光与人物画融合

## Stats 浮动文字规格（不要 panel）

- **不要任何方框、底色、边框、卡片**——这只是直接贴在画面上的文字
- 字体：Alibaba PuHuiTi Heavy
- 颜色：金色 `#FFD700` 数字 + 白色文字，自带柔和金色外发光（如同霓虹）
- 排版：竖向堆叠在画面**右上角或左上角**（避开人物的脸和出手臂）
- **三行**：
  - `🏆 冠军 × 1`  ← 只有这行带金色奖杯 emoji
  - `MVP × 1`     ← 不带 emoji
  - `得分王 × 1`  ← 不带 emoji
- 三行靠左对齐，"× 1" 中的数字最大、金色高亮

## 文字模块规格

### 唯一的文字模块 — 标题模块（同封面横带）

- 实色黑底 `#0a0a0a`，上下两条 2px 金色细线作为边
- 第 1 行（小标签）：`联盟第一人 ｜ 卫冕冠军` — Alibaba PuHuiTi Heavy，白色，小字
- 第 2 行（人名）：`SGA` — Alibaba PuHuiTi Heavy,纯金色 `#FFD700`,最大字号
- 占画面 ~14% 高度
- 位于画面**正中央**(同封面横带位置)

## 人物动作:中距离急停后仰跳投(脸要占 20%)

- **脸是画面绝对主角**——头部至少占整张画布 20% 面积
- 极近距离 hero shot,镜头拉到非常近,脸部细节清晰可见
- 脸部表情:冷峻、嘴角一丝若有若无的笑、眼神锁死前方
- 出手臂还在,但相对于脸已经是次要元素
- 视觉上头 + 出手臂在 panel 上方,腿 + 脚在 panel 下方
- 球的位置在画面**最顶边**或紧贴顶边——给"刚出手"的速度感
- 身体后仰幅度更大,腰部明显往后弯
- 下半身:双脚都已经离地(处于跳投空中阶段)
- 镜头:**极近距离**仰拍 + 略微 3/4 侧角

## Final Prompt

```text
Vertical 3:4 single-character INTRODUCTION CARD in the exact style of Blue Lock (ブルーロック) character key visuals and the First Slam Dunk 2022 movie poster — modern clean digital flat shading, thin neon outlines, cold cinematic lighting, icy desaturated base palette with saturated gold neon accents.

LAYERED COMPOSITION: the player illustration is the FULL-CANVAS background layer (fills the entire 3:4 frame from edge to edge). The player's FACE must occupy at least 20% of the total canvas area — this is a FACE-DOMINANT hero portrait. ONE single text module (a title band) is overlaid on top of the player at the vertical CENTER of the card — it hides only a thin slice of the player's mid-section.

BACKGROUND-LAYER ILLUSTRATION (full canvas, FACE-DOMINANT):
A lean sleek NBA point guard in an Oklahoma City Thunder blue-and-orange jersey #2, captured at the absolute APEX of his signature MID-RANGE PULL-UP FADEAWAY. The CAMERA IS PULLED IN EXTREMELY CLOSE — his face is the single largest element in the entire card and must cover AT LEAST 20% of the canvas area. Sharp jawline, short dark hair, eyes locked dead ahead, cold emotionless expression with the faintest knowing smirk of a man who already knew the ball was going in. Every facial detail (eyes, eyebrows, nostril, lip line, jaw shadow) must be crisply readable.

Pose: body in mid-air at the peak of the jump, both feet off the ground, body arched backward in a deep pronounced fadeaway lean, right shooting arm fully extended straight up at maximum reach with elbow locked, the ball just released from his fingertips and floating at the very TOP edge of the canvas, left arm trailing for balance. Long elongated athletic limbs giving the pose maximum tension and reach. Camera: extreme close-up low-angle hero shot looking UP from below his chest, slight 3/4 side angle.

The player illustration is intentionally LARGER than the canvas can fit — his head is huge and dominates the upper portion, his ball is at the top edge, his shoulders and torso fill the middle, and his lower body extends below into the bottom portion. He must be the brightest, most saturated element in the image.

Behind him: a faint watermark-level silhouette of the OKLAHOMA CITY THUNDER PRIMARY SHIELD LOGO (shield outline with a basketball inside, NO "OKC" text, NO "THUNDER" text, just the bare shield+ball symbol), rendered in deeply muted dark teal-charcoal, low saturation, clearly behind the subject. Gold neon rim-light on his silhouette. Thin warm-gold atmospheric particles. Deep teal-charcoal base. NO ego-beast, NO mascot.

FLOATING STAT TEXT (NOT in any panel, NOT in any box, just paint-on-image text):
In the upper-right region of the canvas (or wherever there is empty negative space NOT covering his face or shooting arm), three lines of floating stat text painted directly onto the illustration with NO background panel, NO border, NO box, NO card — just glowing text floating on the image like a neon decal. Each line glows with a soft warm gold halo. Font: Alibaba PuHuiTi Heavy or bold sans-serif. Numbers in bright gold #FFD700, labels in pure white, all with thin 1px black outline for legibility against any background.

The three lines, vertically stacked, left-aligned:
- Line 1: a small flat-shaded gold trophy icon (🏆 style, NOT 3D, NOT photoreal) followed by "冠军 × 1"
- Line 2: "MVP × 1"   (NO trophy icon — text only)
- Line 3: "得分王 × 1"   (NO trophy icon — text only)

ONLY line 1 has the trophy icon. Lines 2 and 3 are pure text, no icons, no bullets, no symbols. The "× 1" numerals on each line are the visually loudest part of the stat text. Three lines total, no fourth line, no PPG, no FG%, no extra data.

OVERLAY MODULE — TITLE BAND (the only text panel on this card, positioned at vertical center, ~50% from top):
A single solid horizontal band overlaying the player's torso. Fill: pure solid black (#0a0a0a), fully opaque, no transparency. Top and bottom edges bordered by thin 2px gold pinstripe lines (matching the cover series style). Band height: ~14% of total poster height.

Inside the title band, two rows of text:
- ROW A (small, white): "联盟第一人 ｜ 卫冕冠军" in Alibaba PuHuiTi Heavy, pure white, no outline, horizontally centered. ~30% of band height.
- ROW B (largest text on the entire card): "SGA" in Alibaba PuHuiTi Heavy, pure GOLD (#FFD700), thin 1px black outline, horizontally centered with generous letter-spacing. ~60% of band height. This must be the single biggest text element on the card.

There is NO second text panel. There is NO trophy stat box. The stat text floats freely on the illustration as glowing decals — that is the only way stats appear.

RESULT: the viewer sees the player's MASSIVE face and shooting arm dominating the top ~50% of the card with floating gold stat text glowing in the upper corner, then the title band cutting across the middle ~14%, then the player's lower body in the bottom ~36%.

Style notes: Blue Lock / First Slam Dunk aesthetic. NOT manga ink, NOT painterly, NOT photorealism. Clean flat shading, thin neon outlines, sharp legible typography. The face must be huge — at least 20% of the canvas area. The stat text must be unmissable but must NOT live inside any panel or box. Aspect ratio 3:4 vertical.
```

## 如果要继续改

- 脸不够大 → 强调 "the face MUST occupy at least 20% of the canvas, this is a face-dominant portrait, pull the camera EVEN closer"
- Stats 被画进了一个 box/panel → 强调 "NO panel, NO box, NO border, NO card background — the stat text is painted DIRECTLY on the illustration as floating glowing text only"
- Stats 三行都有 emoji → 强调 "ONLY line 1 (冠军) has the trophy icon. Lines 2 (MVP) and 3 (得分王) are PURE TEXT, no icons whatsoever"
- 出现 4 行或更多 stat → 强调 "EXACTLY 3 lines: 冠军 × 1, MVP × 1, 得分王 × 1 — no more, no less"
- 标题模块也消失了 → 强调 "the title band IS still required, only the stats panel is removed"
- 出手臂没在 panel 上方 → 强调 "the shooting arm and the ball must be ABOVE the title band, in the top half of the canvas"
- 奖杯图标变成立体 3D 渲染 → 强调 "flat 2D gold silhouette icon, NOT 3D, NOT realistic trophy"

## 不要动什么

- 3:4 纵向比例
- 唯一的标题模块在画面正中央(实色黑 + 金色上下边 + 标签 + SGA 金色大字)
- Stats 直接浮在画面上(无框、无 panel、无 box)
- Stats 锁死三行:冠军 / MVP / 得分王
- **只有冠军这行**带金色奖杯图标
- 人物头 + 臂在标题带上方,腿在下方
- 脸至少占画布 20% 面积
- OKC 盾形 watermark 背景(不是吉祥物,不带文字)
- 中距离急停后仰的签名动作 + 出手最高点
- Blue Lock flat-shaded 数码画风

## 事实校正

- ✅ 1× 冠军(2025 NBA Finals 冠军)
- ✅ 1× MVP(2024-25 赛季 MVP)
- ✅ 1× 得分王(2024-25 赛季得分王 32.7 PPG)
- ❌ 不要写他场均、命中率等具体数字(已搬到 post 正文)
- ❌ 不要写"DPOY"等防守奖项(他没有)

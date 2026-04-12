## 这张图的任务

TATUM 单人介绍卡。与 SGA 卡同一系列 layout：通过把整个人物放大让脸自然变大（~20% 画布），不是大头照。标志性 step-back 三分动作。只保留**一个**标题横带，Stats 以浮动文字贴在画面上。跟腱复出叙事用右腿金色裂纹线条暗示。

## 版式结构

```
┌──────────────────────────────┐  3:4 竖版
│  球↑ 出手瞬间                │  ← 球紧贴顶边
│  TATUM 巨大的头(占 ~20%)      │  ← 专注锁定篮筐
│  出手臂伸直                  │  ← 旁边浮动 stats 文字
│  ← step-back 位移 →          │  ← 撤步的水平位移可见
├══════════════════════════════┤
│  无私复出 ｜ 攻防一体          │  ← 唯一的文字模块 ~14%
│         TATUM               │     实色黑底 + 金色上下边
├══════════════════════════════┤
│   下半身 / 撤步落地           │
│   右脚跟腱金色裂纹            │  ← 跟腱复出暗示
└──────────────────────────────┘
```

**关键概念**：
- 完整的 step-back 3 动作图——撤步位移、出手臂、球的飞行都在
- 整个人物 zoom in 一档，头部被挤到画面上方变大（~20% 画布）
- 中间只有**一条**横带（标题模块）挡住人物中段
- Stats 是**浮动文字**，直接 paint 在画面空白区域，没有任何 panel/box
- 右腿跟腱处有淡金色数码裂纹——不血腥，只是 healed battle-scar 符号

## Stats 浮动文字规格（不要 panel）

- 不要任何方框、底色、边框、卡片
- 字体：Alibaba PuHuiTi Heavy
- 颜色：金色 `#FFD700` 数字 + 白色文字，自带柔和金色外发光
- 排版：竖向堆叠在画面空白处（避开人物的脸和出手臂）
- **三行**：
  - `🏆 冠军 × 1`  ← 只有这行带金色奖杯 emoji
  - `FMVP × 1`    ← 不带 emoji
  - `全明星 × 6`   ← 不带 emoji
- 三行靠左对齐

## 文字模块规格

### 唯一的文字模块 — 标题模块（同封面横带）

- 实色黑底 `#0a0a0a`，上下两条 2px 金色细线
- 第 1 行（小标签）：`无私复出 ｜ 攻防一体` — Alibaba PuHuiTi Heavy，白色，小字
- 第 2 行（人名）：`TATUM` — Alibaba PuHuiTi Heavy，纯金色 `#FFD700`，最大字号
- 占画面 ~14% 高度
- 位于画面**正中央**

## 人物动作：招牌 STEP-BACK 三分（整体放大，脸自然占 20%）

- **完整的 step-back 三分动作图**，不是大头照
- 身体刚刚从一个大幅度向后撤步（step-back）落地
- 后腿稳稳着地、前腿抬起，**水平位移清晰可读**——这是 step-back 的灵魂
- 出手臂完全伸直在最高点，球刚离开指尖飞向画面顶边
- 表情：冷静、专注，眼神锁死篮筐方向（画面外的上方）
- 短辫发（twist braids）、宽肩、wing forward 体型
- 右腿跟腱处有几条淡金色数码裂纹发光线（healed battle-scar 符号，不血腥）
- 通过把整个人物 scale 放大一档让脸自然变大
- 镜头：仰角 hero shot + 略微 3/4 侧角，让撤步位移清晰可见

## Final Prompt

```text
Vertical 3:4 single-character INTRODUCTION CARD in the exact style of Blue Lock (ブルーロック) character key visuals and the First Slam Dunk 2022 movie poster — modern clean digital flat shading, thin neon outlines, cold cinematic lighting, icy desaturated base palette with saturated gold-crimson neon accents over a deep forest-green-black background.

LAYERED COMPOSITION: the player illustration is the FULL-CANVAS background layer. This is a FULL ACTION POSE — step-back displacement, shooting arm, airborne ball all visible — but the entire figure has been SCALED UP one notch so it bursts out of the canvas, making the player's HEAD naturally enlarge to occupy approximately 20% of the canvas area. This is NOT a face close-up portrait — the action remains complete, only the camera pulled tighter so the head reads bigger. ONE single text module (a title band) is overlaid on top of the player at the vertical CENTER of the card.

BACKGROUND-LAYER ILLUSTRATION (full canvas, COMPLETE ACTION POSE, scaled up):
An NBA wing forward in a Boston Celtics green-and-white jersey #0, captured at the release moment of his signature STEP-BACK THREE-POINTER. His body has just landed from a big lateral step-back that opened space from an unseen defender — the step-back displacement is clearly readable: back leg firmly planted, front leg lifting, a visible HORIZONTAL GAP between where he was and where he now is. This lateral displacement is the single most important visual element of the pose — it is NOT a pull-up, NOT a catch-and-shoot, it is a STEP-BACK. His shooting arm is fully extended at the apex of the release, elbow locked, the ball just leaving his fingertips and floating at the very TOP edge of the canvas. Eyes locked on the rim, calm focused expression of a man who already knows the ball is going in. Short twist braids, broad shoulders, wing build.

CRITICAL POSE DETAIL: the lateral step-back must be visually readable — the back leg should be clearly planted while the body is already shifting backward and upward into the release.

Stylized thin cracks of gold neon light running along his right Achilles tendon area — subtle digital glow-lines that read as healed battle-scars from a ruptured Achilles. NOT ink, NOT blood, NOT gory — just clean thin gold neon glow cracks, visible but understated.

The figure is SCALED UP so it bursts beyond the canvas: his head is pushed up near the top of the frame and reads LARGE (occupies roughly 20% of the canvas area as a natural consequence of the zoom), his shooting arm and the ball pierce the top edge, his torso fills the middle (where the title band will overlay). The face is large because the WHOLE figure is large — NOT because the camera switched to a portrait shot.

Camera: low-angle hero shot looking UP from below his chest, slight 3/4 side angle so the step-back displacement reads clearly, framed tighter than a wide shot — but still a full-action frame, NOT a face close-up. He must be the brightest, most saturated element in the image.

Behind him: a faint watermark-level silhouette of the BOSTON CELTICS shamrock clover symbol (a simple three-leaf shamrock, NO "CELTICS" text, NO "BOSTON" text, just the bare shamrock shape), rendered in deeply muted dark forest-green, low saturation, clearly behind the subject. Warm gold-crimson neon rim-light on his silhouette. Thin gold atmospheric particles. Deep matte forest-green-black base. NO ego-beast, NO mascot.

FLOATING STAT TEXT (NOT in any panel, NOT in any box, just paint-on-image text):
In a corner of the canvas (wherever there is empty negative space NOT covering his face or shooting arm), three lines of floating stat text painted directly onto the illustration with NO background panel, NO border, NO box — just glowing text floating on the image like a neon decal. Each line glows with a soft warm gold halo. Font: Alibaba PuHuiTi Heavy or bold sans-serif. Numbers in bright gold #FFD700, labels in pure white, all with thin 1px black outline.

The three lines, vertically stacked, left-aligned:
- Line 1: a small flat-shaded gold trophy icon (🏆 style, NOT 3D, NOT photoreal) followed by "冠军 × 1"
- Line 2: "FMVP × 1"   (NO trophy icon — text only)
- Line 3: "全明星 × 6"   (NO trophy icon — text only)

ONLY line 1 has the trophy icon. Lines 2 and 3 are pure text, no icons. Three lines total, no fourth line.

OVERLAY MODULE — TITLE BAND (the only text panel on this card, positioned at vertical center, ~50% from top):
A single solid horizontal band overlaying the player's torso. Fill: pure solid black (#0a0a0a), fully opaque. Top and bottom edges bordered by thin 2px gold pinstripe lines. Band height: ~14% of total poster height.

Inside the title band, two rows of text:
- ROW A (small, white): "无私复出 ｜ 攻防一体" in Alibaba PuHuiTi Heavy, pure white, no outline, horizontally centered.
- ROW B (largest text on the entire card): "TATUM" in Alibaba PuHuiTi Heavy, pure GOLD (#FFD700), thin 1px black outline, horizontally centered with generous letter-spacing.

There is NO second text panel. The stat text floats freely on the illustration as glowing decals.

Style notes: Blue Lock / First Slam Dunk aesthetic. NOT manga ink, NOT painterly, NOT photorealism. Clean flat shading, thin neon outlines, sharp legible typography. The head reads big (~20% of canvas) because the WHOLE figure is scaled up. The Achilles gold scar is subtle, not gory. The step-back horizontal gap must be clearly visible. The stat text must NOT live inside any panel or box. Aspect ratio 3:4 vertical.
```

## 如果要继续改

- 脸不够大 → 强调 "the WHOLE figure must be scaled up further so the head naturally occupies ~20% of the canvas"
- Step-back 被画成普通跳投 → 强调 "visible horizontal gap between back leg and front leg, lateral displacement clearly readable, this is a STEP-BACK not a pull-up"
- 跟腱金色裂痕被画成血腥伤口 → 强调 "clean digital glow-lines, not ink, not blood, just thin gold neon cracks"
- Stats 被画进 box → 强调 "NO panel, NO box, NO border — floating glowing text only"
- Stats 三行都有 emoji → 强调 "ONLY line 1 (冠军) has the trophy icon"

## 不要动什么

- 3:4 纵向比例
- 唯一的标题模块在画面正中央（实色黑 + 金色上下边 + 标签 + TATUM 金色大字）
- Stats 直接浮在画面上（无框）
- Stats 锁死三行：冠军 / FMVP / 全明星
- 只有冠军这行带金色奖杯图标
- 通过整体放大让脸自然占画布 ~20%（scale up，不是 portrait crop）
- Celtics 三叶草 watermark 背景（不带文字）
- Step-back 3 招牌动作 + 撤步水平位移必须可见
- 跟腱金色裂纹（healed Achilles battle-scar motif）
- Blue Lock flat-shaded 数码画风

## 事实校正

- ✅ 1× 冠军（2024 NBA Finals）
- ✅ 1× FMVP（2024）
- ✅ 6× 全明星（2020–2025）
- ✅ 跟腱断裂 10 个月复出（2025/5 受伤 → 2026/3/6 复出）
- ❌ 不要写他复出后的具体场均数据（放在 post 正文）
- ❌ 不要写 All-NBA 次数（不确定具体几次，不写硬数字）

## 这张图的任务

JOKIC 单人介绍卡。与 SGA 卡同一系列 layout：通过把整个人物放大让脸自然变大（~20% 画布），不是大头照。标志性 no-look pass 动作。只保留**一个**标题横带，Stats 以浮动文字贴在画面上。

## 版式结构

```
┌──────────────────────────────┐  3:4 竖版
│  ←球（飞向画面左）            │  ← 球往一侧飞出
│  JOKIC 巨大的头(占 ~20%)      │  ← 头扭向反方向看
│  传球臂从右肩水平甩出          │  ← 旁边浮动 stats 文字
│                              │
├══════════════════════════════┤
│  全能中锋 ｜ 小丑              │  ← 唯一的文字模块 ~14%
│         JOKIC               │     实色黑底 + 金色上下边
├══════════════════════════════┤
│   下半身                     │
│                              │
└──────────────────────────────┘
```

**关键概念**：
- 完整的传球动作图——传球臂、扭头反向看、球的飞行轨迹都在
- 整个人物 zoom in 一档，头部被挤到画面上方变大（~20% 画布）
- 中间只有**一条**横带（标题模块）挡住人物中段
- Stats 是**浮动文字**，直接 paint 在画面空白区域，没有任何 panel/box

## Stats 浮动文字规格（不要 panel）

- 不要任何方框、底色、边框、卡片
- 字体：Alibaba PuHuiTi Heavy
- 颜色：金色 `#FFD700` 数字 + 白色文字，自带柔和金色外发光
- 排版：竖向堆叠在画面空白处（避开人物的脸和传球臂）
- **三行**：
  - `🏆 冠军 × 1`  ← 只有这行带金色奖杯 emoji
  - `MVP × 3`     ← 不带 emoji
  - `FMVP × 1`    ← 不带 emoji
- 三行靠左对齐

## 文字模块规格

### 唯一的文字模块 — 标题模块（同封面横带）

- 实色黑底 `#0a0a0a`，上下两条 2px 金色细线
- 第 1 行（小标签）：`全能中锋 ｜ 小丑` — Alibaba PuHuiTi Heavy，白色，小字
- 第 2 行（人名）：`JOKIC` — Alibaba PuHuiTi Heavy，纯金色 `#FFD700`，最大字号
- 占画面 ~14% 高度
- 位于画面**正中央**

## 人物动作：招牌 NO-LOOK PASS（整体放大，脸自然占 20%）

- **完整的传球动作图**，不是大头照
- 站在高位 / 低位，右手刚刚把球甩出，球飞向画面一侧
- 头部明显**扭向与球飞行方向相反**，视线锁死另一侧——no-look pass 的灵魂
- 表情：平静、嘴角一丝若有若无的笑、慢节奏读防守的智者神情
- 大体格、宽肩、厚实身躯（7 尺中锋体型）
- 淡色短发、胡子
- 通过把整个人物 scale 放大一档让脸自然变大
- 镜头：仰角 hero shot + 略微 3/4 侧角

## Final Prompt

```text
Vertical 3:4 single-character INTRODUCTION CARD in the exact style of Blue Lock (ブルーロック) character key visuals and the First Slam Dunk 2022 movie poster — modern clean digital flat shading, thin neon outlines, cold cinematic lighting, icy desaturated base palette with saturated gold neon accents.

LAYERED COMPOSITION: the player illustration is the FULL-CANVAS background layer. This is a FULL ACTION POSE — passing arm, head-fake, ball mid-flight all visible — but the entire figure has been SCALED UP one notch so it bursts out of the canvas, making the player's HEAD naturally enlarge to occupy approximately 20% of the canvas area. This is NOT a face close-up portrait — the action remains complete, only the camera pulled tighter so the head reads bigger. ONE single text module (a title band) is overlaid on top of the player at the vertical CENTER of the card.

BACKGROUND-LAYER ILLUSTRATION (full canvas, COMPLETE ACTION POSE, scaled up):
A massive 7-foot NBA center in a Denver Nuggets navy-and-yellow jersey #15, captured at the exact moment of his signature NO-LOOK PASS. He stands tall in the high post, his right hand has just flicked the ball out sideways toward an unseen cutter — the ball is mid-flight near one edge of the canvas, leaving a faint golden motion trail. Crucially, his HEAD is turned hard to the OPPOSITE direction from where the ball is going — eyes locked on a decoy across the floor, creating the classic misdirection. This head-and-eyes-versus-ball-direction split is the soul of the pose and must read instantly. Calm, slow-motion chess-master expression with a slight knowing smirk. Big thick body, broad shoulders, thick neck, light skin, full beard, short blondish-brown hair.

The figure is SCALED UP so it bursts beyond the canvas: his head is pushed up near the top of the frame and reads LARGE (occupies roughly 20% of the canvas area as a natural consequence of the zoom), his passing arm extends across the upper portion with the ball trailing away, his torso fills the middle (where the title band will overlay). The face is large because the WHOLE figure is large — NOT because the camera switched to a portrait shot. Every facial feature (eyes, beard, smirk, jaw) must be cleanly readable.

Camera: low-angle hero shot looking UP from below his chest, slight 3/4 side angle, framed tighter than a wide shot — but still a full-action frame, NOT a face close-up. He must be the brightest, most saturated element in the image.

Behind him: a faint watermark-level silhouette of the DENVER NUGGETS team symbol (basketball with stylized Rocky Mountain peaks, NO "NUGGETS" text, NO "DENVER" text, just the bare symbol), rendered in deeply muted dark navy, low saturation, clearly behind the subject. Warm gold neon rim-light on his silhouette. Thin warm-gold atmospheric particles. Deep navy-charcoal base. NO ego-beast, NO mascot.

FLOATING STAT TEXT (NOT in any panel, NOT in any box, just paint-on-image text):
In a corner of the canvas (wherever there is empty negative space NOT covering his face or passing arm), three lines of floating stat text painted directly onto the illustration with NO background panel, NO border, NO box — just glowing text floating on the image like a neon decal. Each line glows with a soft warm gold halo. Font: Alibaba PuHuiTi Heavy or bold sans-serif. Numbers in bright gold #FFD700, labels in pure white, all with thin 1px black outline.

The three lines, vertically stacked, left-aligned:
- Line 1: a small flat-shaded gold trophy icon (🏆 style, NOT 3D, NOT photoreal) followed by "冠军 × 1"
- Line 2: "MVP × 3"   (NO trophy icon — text only)
- Line 3: "FMVP × 1"   (NO trophy icon — text only)

ONLY line 1 has the trophy icon. Lines 2 and 3 are pure text, no icons. Three lines total, no fourth line.

OVERLAY MODULE — TITLE BAND (the only text panel on this card, positioned at vertical center, ~50% from top):
A single solid horizontal band overlaying the player's torso. Fill: pure solid black (#0a0a0a), fully opaque. Top and bottom edges bordered by thin 2px gold pinstripe lines. Band height: ~14% of total poster height.

Inside the title band, two rows of text:
- ROW A (small, white): "全能中锋 ｜ 小丑" in Alibaba PuHuiTi Heavy, pure white, no outline, horizontally centered.
- ROW B (largest text on the entire card): "JOKIC" in Alibaba PuHuiTi Heavy, pure GOLD (#FFD700), thin 1px black outline, horizontally centered with generous letter-spacing.

There is NO second text panel. The stat text floats freely on the illustration as glowing decals.

Style notes: Blue Lock / First Slam Dunk aesthetic. NOT manga ink, NOT painterly, NOT photorealism. Clean flat shading, thin neon outlines, sharp legible typography. The head reads big (~20% of canvas) because the WHOLE figure is scaled up. The stat text must NOT live inside any panel or box. Aspect ratio 3:4 vertical.
```

## 如果要继续改

- 脸不够大 → 强调 "the WHOLE figure must be scaled up further so the head naturally occupies ~20% of the canvas"
- 头没有扭向反方向 → 强调 "his head MUST turn hard to the OPPOSITE direction from where the ball is going — this is the no-look pass hallmark"
- Stats 被画进 box → 强调 "NO panel, NO box, NO border — floating glowing text only"
- Stats 三行都有 emoji → 强调 "ONLY line 1 (冠军) has the trophy icon"
- 出现 4 行或更多 stat → 强调 "EXACTLY 3 lines"

## 不要动什么

- 3:4 纵向比例
- 唯一的标题模块在画面正中央（实色黑 + 金色上下边 + 标签 + JOKIC 金色大字）
- Stats 直接浮在画面上（无框）
- Stats 锁死三行：冠军 / MVP / FMVP
- 只有冠军这行带金色奖杯图标
- 通过整体放大让脸自然占画布 ~20%（scale up，不是 portrait crop）
- Nuggets 队徽 watermark 背景（不带文字）
- No-look pass 招牌动作 + 头扭向球飞行的反方向
- Blue Lock flat-shaded 数码画风

## 事实校正

- ✅ 1× 冠军（2023 NBA Finals）
- ✅ 3× MVP（2020-21 / 2021-22 / 2023-24）
- ✅ 1× FMVP（2023）
- ❌ 不要写场均、命中率等具体数字
- ❌ 不要写"得分王"等他没有的奖项

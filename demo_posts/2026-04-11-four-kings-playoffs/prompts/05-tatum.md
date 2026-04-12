## 这张图的任务

TATUM 单人介绍卡。与 SGA 卡同一系列 layout：通过把整个人物放大让脸自然变大（~20% 画布），不是大头照。**防守姿态**——低重心防守站位，双臂张开封锁传球路线，呼应"攻防一体"的标题叙事。只保留**一个**标题横带，Stats 以浮动文字贴在画面上。跟腱复出叙事用右腿金色裂纹线条暗示。

## 版式结构

```
┌──────────────────────────────┐  3:4 竖版
│                              │
│  TATUM 巨大的头(占 ~20%)      │  ← 眼神锁定持球人
│  双臂张开封锁传球路线          │  ← 旁边浮动 stats 文字
│  低重心防守站位               │  ← 防守姿态，不是进攻
├══════════════════════════════┤
│  无私复出 ｜ 攻防一体          │  ← 唯一的文字模块 ~14%
│         TATUM               │     实色黑底 + 金色上下边
├══════════════════════════════┤
│   下半身 / 宽步距防守马步      │
│   右脚跟腱金色裂纹            │  ← 跟腱复出暗示
└──────────────────────────────┘
```

**关键概念**：
- 完整的防守姿态图——双臂张开、低重心、宽步距，呼应"攻防一体"
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

## 人物动作：防守站位 DEFENSIVE STANCE（整体放大，脸自然占 20%）

- **完整的防守姿态图**，不是大头照，不是进攻动作
- 低重心防守站位（defensive stance）：膝盖弯曲、重心下沉、双脚宽步距
- 双臂向两侧张开，手掌朝前，**封锁传球路线**——呼应"攻防一体"叙事
- 臂展完全展示，两只手臂几乎和 Wemby 一样撑满画面宽度
- 表情：极度专注、锁定、杀气——眼神盯死面前的持球人
- 短辫发（twist braids）、宽肩、wing forward 体型
- 右腿跟腱处有几条淡金色数码裂纹发光线（healed battle-scar 符号，不血腥）
- 通过把整个人物 scale 放大一档让脸自然变大
- 镜头：正面偏低仰角 hero shot，让双臂张开的防守宽度最大化

## Final Prompt

```text
Vertical 3:4 single-character INTRODUCTION CARD in the exact style of Blue Lock (ブルーロック) character key visuals and the First Slam Dunk 2022 movie poster — modern clean digital flat shading, thin neon outlines, cold cinematic lighting, icy desaturated base palette with saturated gold-crimson neon accents over a deep forest-green-black background.

LAYERED COMPOSITION: the player illustration is the FULL-CANVAS background layer. This is a FULL DEFENSIVE POSE — arms spread wide, low center of gravity, wide stance — but the entire figure has been SCALED UP one notch so it bursts out of the canvas, making the player's HEAD naturally enlarge to occupy approximately 20% of the canvas area. This is NOT a face close-up portrait — the action remains complete, only the camera pulled tighter so the head reads bigger. ONE single text module (a title band) is overlaid on top of the player at the vertical CENTER of the card.

BACKGROUND-LAYER ILLUSTRATION (full canvas, DEFENSIVE STANCE, scaled up):
An NBA wing forward in a Boston Celtics green-and-white jersey #0, locked into an intense DEFENSIVE STANCE — this is NOT an offensive pose, NOT a shooting pose. He is guarding his man on the perimeter: knees deeply bent, center of gravity low, feet spread wide in a strong athletic base. BOTH ARMS are extended out to his sides with palms facing forward, cutting off passing lanes — his wingspan stretches nearly the full width of the canvas. His eyes are locked dead ahead on the ball-handler in front of him with laser focus and killer intent — the expression of a man who came back from a ruptured Achilles not to score, but to DEFEND. Short twist braids, broad shoulders, wing build, muscular frame.

CRITICAL POSE DETAIL: this must read as a DEFENSIVE stance, NOT an offensive pose. The low center of gravity, wide base, and outstretched arms closing off space are the defining visual elements. He is NOT holding a ball, NOT shooting, NOT dunking — he is GUARDING.

Stylized thin cracks of gold neon light running along his right Achilles tendon area — subtle digital glow-lines that read as healed battle-scars from a ruptured Achilles. NOT ink, NOT blood, NOT gory — just clean thin gold neon glow cracks, visible but understated.

The figure is SCALED UP so it bursts beyond the canvas: his head is pushed up near the top of the frame and reads LARGE (occupies roughly 20% of the canvas area as a natural consequence of the zoom), his outstretched arms extend beyond the left and right edges of the canvas, his torso fills the middle (where the title band will overlay). The face is large because the WHOLE figure is large — NOT because the camera switched to a portrait shot.

Camera: slightly low-angle hero shot, nearly FRONTAL (facing the defender head-on, as if you are the ball-handler being guarded), framed tighter than a wide shot — maximizing the visual width of his outstretched defensive arms. He must be the brightest, most saturated element in the image.

Behind him: a faint watermark-level silhouette of the BOSTON CELTICS shamrock clover symbol (a simple three-leaf shamrock, NO "CELTICS" text, NO "BOSTON" text, just the bare shamrock shape), rendered in deeply muted dark forest-green, low saturation, clearly behind the subject. Warm gold-crimson neon rim-light on his silhouette. Thin gold atmospheric particles. Deep matte forest-green-black base. NO ego-beast, NO mascot.

FLOATING STAT TEXT (NOT in any panel, NOT in any box, just paint-on-image text):
In a corner of the canvas (wherever there is empty negative space NOT covering his face or outstretched arms), three lines of floating stat text painted directly onto the illustration with NO background panel, NO border, NO box — just glowing text floating on the image like a neon decal. Each line glows with a soft warm gold halo. Font: Alibaba PuHuiTi Heavy or bold sans-serif. Numbers in bright gold #FFD700, labels in pure white, all with thin 1px black outline.

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

Style notes: Blue Lock / First Slam Dunk aesthetic. NOT manga ink, NOT painterly, NOT photorealism. Clean flat shading, thin neon outlines, sharp legible typography. The head reads big (~20% of canvas) because the WHOLE figure is scaled up. The Achilles gold scar is subtle, not gory. The defensive stance (low, wide, arms out) must be unmistakable — this is a DEFENDER, not a scorer. The stat text must NOT live inside any panel or box. Aspect ratio 3:4 vertical.
```

## 如果要继续改

- 脸不够大 → 强调 "the WHOLE figure must be scaled up further so the head naturally occupies ~20% of the canvas"
- 被画成进攻动作（投篮/持球）→ 强调 "this is a DEFENSIVE stance — low center of gravity, arms spread wide, NO ball in hand, NOT shooting"
- 双臂没有张开 → 强调 "BOTH arms must extend wide to the sides, palms forward, cutting off passing lanes — wingspan fills the canvas width"
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
- 防守站位动作（低重心 + 双臂张开封锁传球路线）
- 跟腱金色裂纹（healed Achilles battle-scar motif）
- Blue Lock flat-shaded 数码画风

## 事实校正

- ✅ 1× 冠军（2024 NBA Finals）
- ✅ 1× FMVP（2024）
- ✅ 6× 全明星（2020–2025）
- ✅ 跟腱断裂 10 个月复出（2025/5 受伤 → 2026/3/6 复出）
- ❌ 不要写他复出后的具体场均数据（放在 post 正文）
- ❌ 不要写 All-NBA 次数（不确定具体几次，不写硬数字）

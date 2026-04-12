## 这张图的任务

WEMBY 单人介绍卡。与 SGA 卡同一系列 layout：通过把整个人物放大让脸自然变大（~20% 画布），不是大头照。标志性 chasedown block 动作。只保留**一个**标题横带，Stats 以浮动文字贴在画面上。因为 Wemby 没有冠军/MVP 等大奖，用**本季三围**（得分/篮板/盖帽）代替。

## 版式结构

```
┌──────────────────────────────┐  3:4 竖版
│  球↓ 被 WEMBY 手掌拍下        │  ← 球在最顶边被拍
│  WEMBY 巨大的头(占 ~20%)      │  ← 仰头看球，冷静表情
│  封盖的手臂从画面顶穿出        │  ← 旁边浮动 stats 文字
│                              │
├══════════════════════════════┤
│  少林绝学 ｜ 外星人            │  ← 唯一的文字模块 ~14%
│         WEMBY               │     实色黑底 + 金色上下边
├══════════════════════════════┤
│   极长的下半身               │
│                              │
└──────────────────────────────┘
```

**关键概念**：
- 完整的 chasedown block 动作图——封盖臂、跃起身体、球被拍飞都在
- 整个人物 zoom in 一档，头部被挤到画面上方变大（~20% 画布）
- 因为 Wemby 身高极高（7'4"），放大后身体会极大地填满画面
- 中间只有**一条**横带（标题模块）挡住人物中段
- Stats 是**浮动文字**（本季三围），直接 paint 在画面空白区域，没有任何 panel/box

## Stats 浮动文字规格（不要 panel）

- 不要任何方框、底色、边框、卡片
- 字体：Alibaba PuHuiTi Heavy
- 颜色：金色 `#FFD700` 数字 + 白色文字，自带柔和金色外发光
- 排版：竖向堆叠在画面空白处（避开人物的脸和封盖臂）
- **三行**（本季数据，**没有 emoji**）：
  - `得分 26.5`
  - `篮板 11.4`
  - `盖帽 4.3`
- 三行靠左对齐，数字最大、金色高亮
- ⚠️ 因为没有冠军，**三行都不带奖杯 emoji**

## 文字模块规格

### 唯一的文字模块 — 标题模块（同封面横带）

- 实色黑底 `#0a0a0a`，上下两条 2px 金色细线
- 第 1 行（小标签）：`少林绝学 ｜ 外星人` — Alibaba PuHuiTi Heavy，白色，小字
- 第 2 行（人名）：`WEMBY` — Alibaba PuHuiTi Heavy，纯金色 `#FFD700`，最大字号
- 占画面 ~14% 高度
- 位于画面**正中央**

## 人物动作：招牌 CHASEDOWN BLOCK（整体放大，脸自然占 20%）

- **完整的封盖动作图**，不是大头照
- 从身后追上来的 chasedown，身体腾空跳到最高点
- 右臂完全伸直向上，手掌张开拍在球上，球在画面**最顶边**
- 另一只手臂横向展开（展现 8 尺臂展的视觉冲击力）
- 极长、极瘦、外星人一般的身体比例——四肢长度超乎正常
- 脸部表情：冷静、专注、略带冷漠——仿佛封盖只是理所当然的日常
- 短深色头发、瘦削脸型
- 通过把整个人物 scale 放大一档让脸自然变大
- 镜头：仰角 hero shot + 略微 3/4 侧角

## Final Prompt

```text
Vertical 3:4 single-character INTRODUCTION CARD in the exact style of Blue Lock (ブルーロック) character key visuals and the First Slam Dunk 2022 movie poster — modern clean digital flat shading, thin neon outlines, cold cinematic lighting, icy desaturated base palette with saturated silver-gold neon accents.

LAYERED COMPOSITION: the player illustration is the FULL-CANVAS background layer. This is a FULL ACTION POSE — blocking arm, leaping body, swatted ball all visible — but the entire figure has been SCALED UP one notch so it bursts out of the canvas, making the player's HEAD naturally enlarge to occupy approximately 20% of the canvas area. This is NOT a face close-up portrait — the action remains complete, only the camera pulled tighter so the head reads bigger. ONE single text module (a title band) is overlaid on top of the player at the vertical CENTER of the card.

BACKGROUND-LAYER ILLUSTRATION (full canvas, COMPLETE ACTION POSE, scaled up):
An impossibly tall, impossibly long-limbed 7-foot-4 NBA center in a San Antonio Spurs black-and-silver jersey #1, captured at the absolute apex of his signature CHASEDOWN BLOCK. He has leaped from behind to reach his maximum vertical height — his right arm is fully extended STRAIGHT UP, palm flat and wide open, slapping the ball down at the very TOP EDGE of the canvas. His left arm extends OUT laterally to show his otherworldly 8-foot wingspan. Both arms are impossibly long, creating a massive cross-like wingspan silhouette. His body is stretched vertically to maximum — everything about this figure screams inhuman length and reach.

He looks calm, focused, almost bored — as if blocking shots is just routine. Lean face, short dark hair, slight stubble, sharp cheekbones, eyes locked upward on the ball with cold quiet confidence. The "alien" aesthetic should come through in his proportions: limbs too long, fingers too long, reach too high.

The figure is SCALED UP so it bursts beyond the canvas: his head is pushed up near the top of the frame and reads LARGE (occupies roughly 20% of the canvas area as a natural consequence of the zoom), his blocking arm and the ball pierce the top edge, his torso fills the middle (where the title band will overlay). The face is large because the WHOLE figure is large — NOT because the camera switched to a portrait shot.

Camera: low-angle hero shot looking UP from below his chest, slight 3/4 side angle, framed tighter than a wide shot — amplifying his already unreal height. He must be the brightest, most saturated element in the image.

Behind him: a faint watermark-level silhouette of the SAN ANTONIO SPURS team symbol (a lone star above a cowboy spur, NO "SPURS" text, NO "SAN ANTONIO" text, just the bare spur + star symbol), rendered in deeply muted dark silver-charcoal, low saturation, clearly behind the subject. Cool silver-white neon rim-light on his silhouette. Thin silver-white atmospheric particles. Deep matte-black charcoal base. NO ego-beast, NO mascot.

FLOATING STAT TEXT (NOT in any panel, NOT in any box, just paint-on-image text):
In a corner of the canvas (wherever there is empty negative space NOT covering his face or blocking arm), three lines of floating stat text painted directly onto the illustration with NO background panel, NO border, NO box — just glowing text floating on the image like a neon decal. Each line glows with a soft warm gold halo. Font: Alibaba PuHuiTi Heavy or bold sans-serif. Numbers in bright gold #FFD700, labels in pure white, all with thin 1px black outline.

The three lines, vertically stacked, left-aligned:
- Line 1: "得分 26.5"   (NO trophy icon, NO emoji — text only)
- Line 2: "篮板 11.4"   (NO trophy icon — text only)
- Line 3: "盖帽 4.3"    (NO trophy icon — text only)

NO trophy icon on ANY line — these are per-game stats, not championship honors. NO emoji of any kind. Numbers are visually loudest (large, bright gold). Three lines total, no fourth line.

OVERLAY MODULE — TITLE BAND (the only text panel on this card, positioned at vertical center, ~50% from top):
A single solid horizontal band overlaying the player's torso. Fill: pure solid black (#0a0a0a), fully opaque. Top and bottom edges bordered by thin 2px gold pinstripe lines. Band height: ~14% of total poster height.

Inside the title band, two rows of text:
- ROW A (small, white): "少林绝学 ｜ 外星人" in Alibaba PuHuiTi Heavy, pure white, no outline, horizontally centered.
- ROW B (largest text on the entire card): "WEMBY" in Alibaba PuHuiTi Heavy, pure GOLD (#FFD700), thin 1px black outline, horizontally centered with generous letter-spacing.

There is NO second text panel. The stat text floats freely on the illustration as glowing decals.

Style notes: Blue Lock / First Slam Dunk aesthetic. NOT manga ink, NOT painterly, NOT photorealism. Clean flat shading, thin neon outlines, sharp legible typography. The head reads big (~20% of canvas) because the WHOLE figure is scaled up. The alien-long limbs and the wingspan must read as inhuman and imposing. The stat text must NOT live inside any panel or box. Aspect ratio 3:4 vertical.
```

## 如果要继续改

- 脸不够大 → 强调 "the WHOLE figure must be scaled up further so the head naturally occupies ~20% of the canvas"
- 身体比例没有体现"外星人"感 → 强调 "limbs impossibly long, fingers too long, reach too high — inhuman alien proportions"
- 没有展现臂展 → 强调 "left arm MUST extend laterally to show his 8-foot wingspan"
- Stats 被画进 box → 强调 "NO panel, NO box, NO border — floating glowing text only"
- Stats 出现了奖杯 emoji → 强调 "NO trophy icon on ANY line — these are per-game stats, not honors"

## 不要动什么

- 3:4 纵向比例
- 唯一的标题模块在画面正中央（实色黑 + 金色上下边 + 标签 + WEMBY 金色大字）
- Stats 直接浮在画面上（无框）
- Stats 锁死三行：得分 / 篮板 / 盖帽（本季数据）
- **三行都不带 emoji**（因为没有冠军）
- 通过整体放大让脸自然占画布 ~20%（scale up，不是 portrait crop）
- Spurs 队徽 watermark 背景（不带文字）
- Chasedown block 招牌动作 + 臂展展示
- Blue Lock flat-shaded 数码画风

## 事实校正

- ⚠️ 得分 26.5 / 篮板 11.4 / 盖帽 4.3 为预估值——**生图前请替换为 2025-26 赛季实际数据**
- ❌ 不要写冠军 / MVP / DPOY（他目前没有这些荣誉）
- ❌ 不要写 ROY（虽然有，但和其他三人的冠军/MVP 级别不对称，不适合放这里）

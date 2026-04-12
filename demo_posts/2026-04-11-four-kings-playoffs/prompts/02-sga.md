## 这张图的任务

SGA 单人介绍卡。上方大图展示人物，下方文字模块给出身份 + 关键数据。视觉语言和封面保持同一系列（Blue Lock 风格 + OKC Thunder 盾形 watermark 背景 + 实色黑横带文字）。

## 版式结构

```
┌──────────────────────────────┐  3:4 竖版
│                              │
│     SGA 全身大图              │  ← ~70% 高度
│     签名动作：中距离急停后仰    │
│     背景：OKC 盾形 watermark   │
│     金色大气粒子               │
│                              │
├══════════════════════════════┤  实色黑横带（同封面样式）
│  联盟第一人 ｜ 卫冕冠军         │  ← 标签行，白色小字
│         S G A               │  ← 人名，金色，最大
├──────────────────────────────┤  横带下方 stat 区（黑底延伸）
│  31.4 分 · 55.3% 命中 · 卫冕 MVP   │  ← 第 1 行
│  连续 20+ 得分 138 场 · 破 Wilt 63 年纪录 │  ← 第 2 行
└──────────────────────────────┘
```

## 文字模块规格（和封面横带样式一致）

**横带区（solid #0a0a0a 黑底 + 上边 2px 金色细线）**：
- 第 1 行（标签行）：`联盟第一人 ｜ 卫冕冠军` — Alibaba PuHuiTi Heavy，白色，小字
- 第 2 行（人名）：`SGA` — Alibaba PuHuiTi Heavy，纯金色，最大字号

**横带下方 stat 区（黑底延伸，白色 monospace，两行内）**：
- 第 1 行：`31.4 分  ·  55.3% 命中  ·  卫冕 MVP`
- 第 2 行：`连续 20+ 得分 138 场  ·  破 Wilt 63 年纪录`

## 人物动作：中距离急停后仰跳投（全身）

- **全身**——单人卡空间充足，不用半身
- 身体重心轻微后倾，右肘抬至出手点
- 球刚刚离指尖（或指尖正在送球）
- 冷峻沉静的脸，嘴角极轻微的笑
- 短发，身形修长
- 低角度仰拍，全身从画面底部撑到顶部

## Final Prompt

```text
Vertical 3:4 single-character INTRODUCTION CARD in the exact style of Blue Lock (ブルーロック) character key visuals and the First Slam Dunk 2022 movie poster — modern clean digital flat shading, thin neon outlines, cold cinematic lighting, icy desaturated base palette with saturated gold neon accents.

LAYOUT: two strict zones. ZONE 1 (top ~70% of total height): full-body character illustration, no text. ZONE 2 (bottom ~30%): solid black text panel. A clear hard line separates the two — Zone 2 is a completely opaque black block, nothing from Zone 1 bleeds through.

ZONE 1 — FULL-BODY CHARACTER ILLUSTRATION:
A lean sleek NBA point guard in an Oklahoma City Thunder blue-and-orange jersey #2, FULL-BODY portrait (head to foot, both feet visible at the bottom of Zone 1), captured at the apex of his signature MID-RANGE PULL-UP FADEAWAY — body slightly fading back, right shooting elbow cocked at release point, ball just leaving his fingertips, left arm trailing for balance, cold emotionless face with the faintest knowing smirk of a man who already knew it was going in, short dark hair, long athletic limbs. Camera: low angle looking UP from below his waist so his full body fills Zone 1 from bottom to top. He is the brightest, most saturated element on the card.

Behind him: a faint watermark-level silhouette of the OKLAHOMA CITY THUNDER PRIMARY SHIELD LOGO (shield outline with a basketball inside, NO "OKC" text, NO "THUNDER" text, bare shield+ball symbol only), rendered in deeply muted dark teal-charcoal, low saturation — clearly behind the subject, never competing with him. Gold neon rim-light traces his silhouette. Thin warm-gold atmospheric particles. Deep teal-charcoal base. NO ego-beast. NO mascot. NO HUD overlays inside Zone 1 — the illustration is clean.

ZONE 2 — SOLID BLACK TEXT PANEL (bottom ~30% of poster):
Fill: pure solid black (#0a0a0a), fully opaque, no transparency, no gradient. Top edge has a thin 2px gold pinstripe border line — same style as the cover series title band.

Three rows of text inside Zone 2:

ROW A — TAG LINE (small, white, top of Zone 2):
"联盟第一人 ｜ 卫冕冠军"
Alibaba PuHuiTi Heavy, pure white, no outline, horizontally centered. ~15% of Zone 2 height.

ROW B — PLAYER NAME (largest text on the entire card):
"SGA"
Alibaba PuHuiTi Heavy, pure GOLD (#FFD700), thin 1px black outline, horizontally centered, generous letter-spacing. ~45% of Zone 2 height. This must be the single largest text element on the card — noticeably bigger than the tag line and stats.

ROW C — STAT BLOCK (small, white monospace, exactly 2 lines):
Line 1: "31.4 分  ·  55.3% 命中  ·  卫冕 MVP"
Line 2: "连续 20+ 得分 138 场  ·  破 Wilt 63 年纪录"
Horizontally centered. ~30% of Zone 2 height. Exactly two lines — no more.

Style notes: Blue Lock / First Slam Dunk aesthetic. NOT manga ink, NOT painterly, NOT photorealism. Clean flat shading, thin neon outlines, sharp legible typography. Zone 1 has zero text — all text lives in Zone 2. Zone 2 text hierarchy is strict: tag line small → player name large gold → stats small. Aspect ratio 3:4 vertical.
```

## 如果要继续改

- Zone 1 / Zone 2 不够清晰，文字和图混在一起 → 强调 "Zone 2 is a COMPLETELY SOLID OPAQUE BLACK panel, no illustration bleeds through"
- SGA 被画成半身 → 强调 "FULL BODY from head to foot, both feet visible"
- "SGA" 字号不够大 → 强调 "SGA must be 3× taller than the tag line above it"
- Stat 第 2 行被截断 → 缩短为 "138 场连续 20+ · 刷新历史纪录"
- 背景出现 RUMBLE 吉祥物 → 强调 "NO mascot, only the bare OKC shield symbol as a watermark"

## 不要动什么

- 3:4 纵向比例
- 两区版式（上图下字）
- Zone 2 实色黑底 + 金色上边线
- 标签行白色 / 人名金色 / stat 白色的三层字号层级
- OKC 盾形 watermark（不是吉祥物，不带文字）
- SGA 全身中距离急停后仰
- Blue Lock flat-shaded 数码画风
- Stat 控制在两行内

## 事实校正

- ✅ 31.4 PPG / 55.3 FG%
- ✅ 138 场连续 20+ 得分（打破 Wilt 的 126 场纪录）
- ✅ 卫冕 MVP（2025 赛季获奖）
- ✅ MVP 赔率 -2000
- ❌ 不要写 SGA 是"首次进季后赛"（他之前进过）

## 这张图的任务

SGA 单人介绍卡 v4。**通过把整个人物放大让脸自然变大** —— 不是改成大头照,是把整个动作镜头拉近,人物整体往画面外挤,头部因此被推到画面顶端、变大占 ~20%。动作、出手臂、腿部全部还在,只是整体 scale 变大。只保留**一个**文字模块（标题模块,与封面同款横带）位于画面正中央。**Stats 不再用框装**,直接以浮动文字+发光效果贴在人物图上,融为画面一部分。

## 版式结构

```
┌──────────────────────────────┐  3:4 竖版
│   球↑ 出手臂                 │  ← 球紧贴顶边
│   SGA 巨大的头(占 ~20%)       │  ← 头被往上挤,变大
│  ╲                           │
│   ╲ 后仰身躯                 │  ← 旁边浮动 stats 文字
├══════════════════════════════┤
│  联盟第一人 ｜ 卫冕冠军        │  ← 唯一的文字模块 ~14%
│         S G A               │     实色黑底 + 金色上下边
├══════════════════════════════┤
│   后仰的腿                   │
│   双脚离地                   │  ← 腿/脚仍然完整可见
└──────────────────────────────┘
```

**关键概念**:
- 这**仍然是一张完整的动作图**——出手臂、后仰身躯、腾空双腿都在
- 只是把整个人物 zoom in 一档,人物变得"撑出画布",头部因此挤到画面上方变大
- 头部自然占据 ~20% 画布(不是因为换成大头照,是因为人物整体放大)
- 中间只有**一条**横带(标题模块)挡住人物中段
- Stats 是**浮动文字**,直接 paint 在人物图上的空白区域,没有任何 panel/box,靠金色发光与人物画融合

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

## 人物动作:中距离急停后仰跳投(整体放大,脸自然占 20%)

- **这是完整的跳投动作图,不是大头照**
- 出手臂、后仰身躯、腾空双腿、出手瞬间的球——全部都在画面里
- 通过把整个人物 scale 放大一档让脸自然变大,而**不是**改成脸部特写
- 人物整体被"撑出画布":头部被推到画面上方,变得很大(~20% 画布)
- 球紧贴画面**最顶边**,出手臂在头侧伸直
- 身体后仰,腰部明显往后弯
- 下半身:双脚都已经离地(处于跳投空中阶段),腿、脚在标题带下方仍然清晰可见
- 脸部表情:冷峻、嘴角一丝若有若无的笑、眼神锁死前方
- 镜头:仰角 hero shot + 略微 3/4 侧角,镜头距离比 v2 拉近一档(但不是脸部特写)

## Final Prompt

```text
Vertical 3:4 single-character INTRODUCTION CARD in the exact style of Blue Lock (ブルーロック) character key visuals and the First Slam Dunk 2022 movie poster — modern clean digital flat shading, thin neon outlines, cold cinematic lighting, icy desaturated base palette with saturated gold neon accents.

LAYERED COMPOSITION: the player illustration is the FULL-CANVAS background layer (fills the entire 3:4 frame from edge to edge). This is a FULL ACTION POSE — shooting arm, fadeaway torso, airborne legs all visible — but the entire figure has been SCALED UP one notch so it bursts out of the canvas, making the player's HEAD naturally enlarge to occupy approximately 20% of the canvas area. This is NOT a face close-up portrait — the action remains complete, only the camera pulled tighter so the head reads bigger. ONE single text module (a title band) is overlaid on top of the player at the vertical CENTER of the card — it hides only a thin slice of the player's mid-section.

BACKGROUND-LAYER ILLUSTRATION (full canvas, COMPLETE ACTION POSE, scaled up):
A lean sleek NBA point guard in an Oklahoma City Thunder blue-and-orange jersey #2, captured at the absolute APEX of his signature MID-RANGE PULL-UP FADEAWAY. This is the COMPLETE shooting motion — body in mid-air at the peak of the jump, both feet off the ground and clearly visible in the bottom portion of the canvas, body arched backward in a deep pronounced fadeaway lean, right shooting arm fully extended straight up at maximum reach with elbow locked, the ball just released from his fingertips and floating at the very TOP edge of the canvas, left arm trailing for balance. Long elongated athletic limbs giving the pose maximum tension and reach.

The figure is SCALED UP so it bursts beyond the canvas: his head is pushed up near the top of the frame and reads LARGE (occupies roughly 20% of the canvas area as a natural consequence of the zoom), his shooting arm and the ball pierce the top edge, his torso fills the middle (where the title band will overlay), and his bent jumping legs and feet remain clearly visible in the bottom third. The face is large because the WHOLE figure is large — NOT because the camera switched to a portrait shot. Sharp jawline, short dark hair, eyes locked dead ahead, cold emotionless expression with the faintest knowing smirk of a man who already knew the ball was going in. Every facial feature (eyes, brows, lip line, jaw shadow) must be cleanly readable.

Camera: low-angle hero shot looking UP from below his waist, slight 3/4 side angle, framed tighter than a wide shot — but still a full-action frame, NOT a face close-up. He must be the brightest, most saturated element in the image.

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

RESULT: the viewer sees the player's enlarged head + shooting arm + ball dominating the top ~50% of the card (with floating gold stat text glowing in a corner), then the title band cutting across the middle ~14%, then his fadeaway torso bottom + bent jumping legs + airborne feet clearly visible in the bottom ~36%. It's a complete shooting motion, just zoomed in.

Style notes: Blue Lock / First Slam Dunk aesthetic. NOT manga ink, NOT painterly, NOT photorealism. Clean flat shading, thin neon outlines, sharp legible typography. The head reads big (~20% of canvas) because the WHOLE figure is scaled up — this is NOT a portrait or face close-up, the legs and feet must still be clearly visible at the bottom. The stat text must be unmissable but must NOT live inside any panel or box. Aspect ratio 3:4 vertical.
```

## 如果要继续改

- 脸不够大 → 强调 "the WHOLE figure must be scaled up further so the head naturally occupies ~20% of the canvas — this is NOT a face portrait, the action stays full"
- 被画成大头照,腿没了 → 强调 "the legs and feet MUST remain clearly visible in the bottom third, this is a complete shooting motion not a portrait"
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
- 人物头 + 臂在标题带上方,腿在下方(完整动作,不是大头照)
- 通过整体放大让脸自然占画布 ~20% 面积(scale up,不是 portrait crop)
- OKC 盾形 watermark 背景(不是吉祥物,不带文字)
- 中距离急停后仰的签名动作 + 出手最高点
- Blue Lock flat-shaded 数码画风

## 事实校正

- ✅ 1× 冠军(2025 NBA Finals 冠军)
- ✅ 1× MVP(2024-25 赛季 MVP)
- ✅ 1× 得分王(2024-25 赛季得分王 32.7 PPG)
- ❌ 不要写他场均、命中率等具体数字(已搬到 post 正文)
- ❌ 不要写"DPOY"等防守奖项(他没有)

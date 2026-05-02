# MLB 帽封面 prompt — Style 7：Karina × 李政厚 半潮流半棒球反差封

## 推荐风格

- 风格：**Vertical split-frame magazine cover** — 左半 Karina 时装编辑模式 / 右半李政厚棒球员模式，同一顶 MLB 帽，两种生活
- 为什么选它（**6+1 版里 concept 最实**）：
  - Karina = MLB China 2022-2025 历史代言人（fashion side 的真实化身）
  - 李政厚 = 2024 SF Giants 1.13 亿合约现役外野手（baseball side 的真实化身）
  - **不是隐喻，是把 post 的两端 punchline 直接拍出来** — 同一个 logo 在他们身上意味两件完全不同的事
- 这张图最该卖什么：**「她戴是潮流，他戴是工作。同一个 logo，两种生活。」 — 视觉自带答案，正文负责给数字**

## 硬规则套用（来自 `explorations/visuals/2026-04-11-four-kings-prompt-lessons.md`）

- **Rule 1（"放大"≠"特写"）**：用户上一版反馈「头太小」 — 套用「the WHOLE figure scaled up so the head naturally enlarges」措辞，不是 face close-up。每张脸约占画布 13-15% 高度，feed 缩图可识别
- **Rule 5（多人物逐人写死差异化）**：左右两人的 pose / wardrobe / backdrop / lighting 全部表格化指定 + 排除句明禁两人共享同一动作

## 标题与排版（与 Style 4 v3 / Style 6 同步）

- 主标：**MLB 在上海**（5 字 / 简体）
- 副标：**是潮牌 不是棒球**（7 字 / 简体）
- 标题位置：跨越中线，画面正中（chest height ~ 50% 垂直位置）放大字
- masthead：「MLB」三个字母作为顶端杂志刊名
- 视觉接缝：两半之间一条极细虚线（or soft gradient），让 split 一眼读懂

## 多人物动作 / 装 / 背景表

| 字段 | 左半（Karina） | 右半（李政厚） |
|---|---|---|
| 模式 | 时装编辑封 | 棒球员现场 |
| 动作 / 姿势 | 双手插大衣口袋，三分之二身正向，单眼半阖（i-D 招牌） | 三分之二身侧 ~30°，一手扶球棒拄地，另一手戴打击手套自然垂下，看向画面外远处球场 |
| 表情 | 克制冷静，轻微不在场感 | 比赛后的沉静专注，无笑 |
| 装 | 米奶油 oversized cashmere 圆领针织 + **干净** MLB 黑帽 + 细银项链 | SF Giants 风条纹球衣（**通用棒球员条纹**，不要明显球队 logo）+ 打击手套 + **沾灰带汗** MLB 黑帽（同款帽，但磨旧）|
| 背景 | 米奶油 cyclorama 编辑棚（plain，no street）| 棒球场外野草皮 + 远处看台轻虚化 + 黄昏暖侧光 |
| 灯光 | 柔和均匀编辑棚灯，从右上轻 wraparound | 户外硬光，左侧高反差金色暖侧光，影子重 |

## Final Prompt

```text
A 3:4 vertical hybrid magazine cover with a deliberate vertical-split composition: LEFT HALF is fashion editorial (Esquire / Vogue Korea visual language), RIGHT HALF is sports portrait moment (a Korean MLB outfielder on the field after a game). Both subjects wear the same black baseball cap with crisp white "MLB" wordmark — but everything else about them is opposite. The image is a comic illustration cover, NOT a photograph.

LAYOUT BASE:
- Canvas vertical-split down the center (~50/50). A barely-visible thin dotted hairline divider runs vertically at the seam — present but understated.
- Each subject occupies their half, chest-up framing, head visible at upper-quarter horizontal line.
- CRITICAL SCALE RULE: the WHOLE figure scaled up in each half so each head naturally enlarges to approximately 13-15% of total canvas height — NOT a face close-up, NOT a tiny figure. Each face must be clearly recognizable when the cover is shrunk to 200px-wide XHS feed thumbnail. Avoid wide-angle distortion: render each subject as if shot with a portrait telephoto.

================================================
LEFT HALF — KARINA, FASHION EDITORIAL MODE
================================================

Subject (left half): a single female Korean idol model archetype based on Karina (Yu Ji-min) of aespa — sharp angular jawline, almond eyes, defined cheekbones, signature composed-and-distant expression. Photo-accurate likeness rendered as comic illustration (not photo) — physically-rendered manga figure with photo-accurate likeness, clean ink linework, two-tone cell-shaded skin, fashion-illustration grade.

Pose: three-quarter body framing, head slightly tilted, body facing camera straight-on. Both hands tucked into front coat pockets. ONE strand of hair falls across the closed/half-aheld camera-left eye (i-D magazine signature). Visible eye gazes calmly past the camera lens. Mouth closed, expression composed and slightly aloof.

Wardrobe (deliberately editorial-luxury, NOT athletic):
- Black baseball cap with crisp white "MLB" wordmark — pristine, undamaged, freshly out-of-box. Worn straight, brim shadowing forehead lightly.
- Oversized cream cashmere crewneck knit, soft texture, no graphics, no team marks.
- A single delicate silver chain at neckline, half-hidden under collar.

Background (left half only): clean cream-oat seamless cyclorama editorial studio backdrop, even diffused soft warm key light from upper-right, no environmental props, no street, no clutter.

================================================
RIGHT HALF — LEE JUNG-HOO, BASEBALL PLAYER MODE
================================================

Subject (right half): a single male Korean professional baseball player archetype based on Lee Jung-hoo (李政厚 / 이정후), San Francisco Giants outfielder. Photo-accurate East-Asian male likeness rendered as comic illustration (not photo) — physically-rendered manga figure with photo-accurate likeness, clean ink linework, two-tone cell-shaded skin. Key facial anchors: round-soft jawline (NOT angular), gentle almond eyes, full-but-soft lips, calm focused post-game expression with no smile, slight sweat sheen on temples.

Pose: three-quarter body angled ~30 degrees away from camera (his body opens toward the field/right edge of frame). One hand grips the handle of a wooden baseball bat resting tip-down on the ground beside him. Other hand wears a leather batting glove, hanging loose at his side. Head turned to look out into the middle distance toward the outfield (NOT at the camera, NOT at Karina). Posture relaxed but vigilant, post-game settling pose.

Wardrobe (deliberately athletic, NOT editorial):
- Same model black baseball cap with crisp white "MLB" wordmark — but visibly weathered: faint dust streaks, sweat darkening at the brim band, slightly crumpled crown. Same cap design as Karina's, but lived-in.
- Generic professional baseball pinstripe jersey in cream with thin navy vertical stripes (do NOT render any specific MLB team logo or chest patch). Plain navy undershirt visible at neckline.
- Brown leather batting glove visible on one hand.

Background (right half only): real outdoor late-afternoon golden-hour baseball field setting — green outfield grass with chalk foul line, blurred distant stadium bleachers and grandstand, slight haze. Strong directional warm sunset key light from camera-left creating sharp shadow on his right facial side. Real-game atmosphere, NOT a studio.

================================================
POSE DIFFERENTIATION ENFORCEMENT (multi-character hard rule)
================================================

The two figures MUST NOT share the same action, the same backdrop, the same lighting, or the same wardrobe register. Specifically:
- Do NOT make Lee Jung-hoo also pose like a fashion model with hands in pockets.
- Do NOT make Karina hold a baseball bat or wear baseball gear.
- Do NOT show Karina on a baseball field; she stays in editorial cyclorama.
- Do NOT show Lee Jung-hoo on a clean studio backdrop; he stays on the field.
- Do NOT make their gazes meet or interact — Karina looks past camera, Lee Jung-hoo looks at distant outfield.
- Do NOT blend the two halves into one continuous environment; the seam must be visible.

================================================
TEXT OVERLAY (Simplified Chinese ONLY, NO Traditional)
================================================

- Top masthead (medium condensed serif, warm off-white, centered above the seam): 「MLB」 — top 8% of canvas only

- Top-right corner mono caption stack (very small, low opacity warm gray): 「VOL. 04 / 2026」 / 「上海」 / tiny mock barcode

- Optional small left-margin caption (small mono, low opacity): 「Karina × 李政厚」 — pure magazine credit treatment, low visual weight

- **CENTER MAIN TITLE BLOCK — the dominant element after the two faces**, positioned at vertical 45-62% of canvas, horizontally centered ACROSS THE SEAM (the title bridges both halves visually), occupying roughly 80% of canvas width:
  - 主标 (Simplified Chinese): 「MLB 在上海」 — MASSIVE bold modern Simplified-Chinese sans-serif, characters approximately 11-13% of canvas height each, warm crisp off-white, single line, centered. Sits at vertical 47-55% of canvas. Must be readable at 200px-wide thumbnail.
  - 副标 (Simplified Chinese): 「是潮牌 不是棒球」 — directly below 主标, large condensed Simplified-Chinese sans-serif, characters approximately 6-7% of canvas height, soft warm white, single line, centered. Sits at vertical 56-62% of canvas.
  - Subtle gradient darkening behind text only (NOT a hard band, must integrate with both halves)

- ALL Chinese characters MUST be SIMPLIFIED CHINESE (简体中文). Verify each character: 在 / 是 / 潮 / 牌 / 不 / 棒 / 球 / 上 / 海 — all simplified.

================================================
COLOR PALETTE
================================================

LEFT HALF (Karina, fashion): warm cream-oat backdrop + cream cashmere knit + crisp white MLB wordmark + black cap.
RIGHT HALF (Lee Jung-hoo, baseball): green outfield grass + cream pinstripes + warm golden-hour sunset + same black MLB cap (now weathered).
SHARED across both halves: crisp white type for headline.

================================================
STYLE
================================================

Hybrid magazine cover comic illustration, NOT photo. Magazine-grade typographic discipline. The visual irony is intentional and the cover's core argument: the same MLB cap on a fashion idol and on a real MLB ballplayer means two completely different things. Both subjects must read as illustrated portraits, not AI photos.

--ar 3:4 --stylize 250
```

## 如果要继续改

- **比例红线**：每张脸 13-15% 画布高度。如果第一张生出来还是头太小，加：`subject heads must each occupy roughly 14% of canvas height — not smaller`
- **不要让两人互动**：他们不看彼此、不在同一空间。一旦视线交汇就变成了「合照」，concept tension 就塌
- **球队 logo 红线**：右半李政厚穿通用棒球条纹即可，**不要画 SF Giants 实体 logo / SF 字母 / 巨人队胸标** — 否则可能触发版权问题
- **背景红线**：左半绝对不能掉到街景；右半绝对不能掉到棚景。两边各守边界
- 备选女明星：可换 Jennie（视觉记忆深 但 narrative 对齐弱）— 把左半 Karina 的描述整段替换为之前 Style 4 v3 里 Jennie 的 wardrobe 描述即可

## 视觉宪法合规说明

- **Person Recognition Gate**：Karina 88 / Lee Jung-hoo 78，两人都 HIGH，直接用名字
- **photoreal 关键词清查**：prompt 全文未出现违禁词；右半「real outdoor」「golden-hour」是场景描述不是渲染语言，渲染语言锁定 `comic illustration not photo`
- **运动员 photo 高发风险**：右半李政厚是双高发场景（运动员 + 户外光） — 三道闸：(a) rendering rule 段；(b) STYLE 段；(c) 整段最后再写「both subjects must read as illustrated portraits, not AI photos」
- **简体中文强锁**：与 Style 4 v3 / Style 6 同步规则
- **多人物 Rule 5**：本 prompt 完整套用 — 表格化 + 排除句 + 后段 POSE DIFFERENTIATION ENFORCEMENT redundancy

## 跑出第一张后评估四件事

1. **比例**：两个头是不是 13-15% 高度？feed 缩图认得出来吗？（red flag：头还是太小 → 加 `not smaller than 14%` 强制）
2. **像不像**：Karina 角颌 + 李政厚圆颌 是不是分开了？（AI 容易把两人脸混着画）
3. **是否漂 photoreal**：右半运动员场景最危险
4. **接缝**：左右两半的视觉边界清晰吗？（红 flag：背景渐变成同一空间 → concept tension 就塌）

跑完丢回来。


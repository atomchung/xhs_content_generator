# MLB 帽封面 prompt — Style 4：杂志街拍封面（Editorial Fashion / Jennie 原型）

## 推荐风格

- 风格：High-fashion editorial street style cover — **Vogue China masthead 骨架 + i-D 半脸构图**（单眼半阖 / 单眼遮发）；模特原型走 Jennie（BLACKPINK）— 既奢华又街头，跟「MLB 是潮牌不是棒球」的 concept 同频
- 为什么选它：用最不像体育的视觉语言（时装杂志封）讲体育 IP，**形式本身就是论点**；选 Jennie 原型扣的是「韩流明星把这股风吹到上海街头」这条隐线 — 视觉自带答案
- 这张图最该卖什么：**「这不是体育，这是时装」+「这股风从首尔吹来」 — 一张图同时讲两件事**

## 标题与排版（已锁）

- 主标：**MLB 在上海**（5 字）
- 副标：**是潮牌 不是棒球**（7 字）
- masthead：「MLB」三个字母作为顶端杂志刊名巨字（Vogue 风骨架）
- 模特构图参考：i-D 招牌单眼半阖 / 一束发遮单眼

## Final Prompt

```text
A 3:4 vertical high-fashion editorial magazine cover, hybrid layout: Vogue China masthead discipline + i-D one-eye-covered half-face composition, deliberately treating an MLB cap as a couture object.

Subject: a single Korean idol model in her mid-20s, archetype based on Jennie Kim from BLACKPINK — almond eyes, defined jawline, soft full lips, signature confident yet detached expression. The face must be photo-accurate likeness of Jennie Kim, but rendered as comic illustration (not photo) — physically-rendered manga figure with photo-accurate likeness, clean ink linework on facial features, two-tone cell-shaded skin, fashion-illustration grade. One eye is softly half-closed (i-D signature gesture), the visible eye gazes calmly just past the camera lens. Mouth closed, expression composed.

Pose: three-quarter body framing — head, torso, and one hand visible. Straight-spined editorial posture, slight contrapposto, one hand resting at chest height fingertips brushing the lapel of her coat, the other hand tucked into front pocket. Composed, slightly aloof.

Wardrobe (luxury-streetwear hybrid, Jennie-coded):
- Black baseball cap with crisp white "MLB" wordmark on the front panel, worn straight, brim shadowing the upper face slightly. The cap is the single visual anchor of the cover.
- Oversized cream-camel wool overcoat with structured shoulders, soft drape, lapel collar. No visible brand markings.
- A single delicate silver chain at the neckline, half-hidden under the coat collar.
- Plain cream-white inner top.

Background: studio-grade seamless cyclorama in deep cool charcoal gray (Pantone 19-3906 territory), even diffused lighting, no environmental props, no street scene, no clutter. The figure stands isolated against flat color — this is what makes the image read as fashion editorial, not street snap.

Lighting: single soft key light from camera-upper-left creating a clean drop-shadow on camera-right side of the cap brim; faint hair-light catching the cap's top curve; tiny catch-light in the visible eye; slight warm rim-light barely catching the coat's left shoulder edge (this single warm tone evokes Shanghai golden-hour without showing any city).

Layout (Vogue China structure + i-D framing):
- Model occupies center of frame, head at upper-third horizontal line, MLB cap is the visual peak
- Wide top band and wide bottom band of negative space reserved for typography
- One strand of hair falls across the closed eye (i-D move, must be deliberate not accidental)

TEXT OVERLAY — Vogue China masthead + i-D condensed sans typographic discipline:
- Top masthead (massive condensed serif, warm off-white, full canvas width): 「MLB」 — top 13% of canvas, set as if MLB were the magazine's nameplate
- Top-right vertical mono caption stack (small, low opacity warm gray): 「VOL. 04 / 2026」 / 「上海」 / a tiny mock barcode below
- Bottom title block (over a 12%-tall thin transparent dark band for legibility):
  - 主标 main headline (large bold modern Chinese sans, warm off-white): 「MLB 在上海」 — single line, centered or left-aligned within band
  - 副标 sub-headline directly below (medium condensed Chinese sans, slightly thinner weight, soft warm white): 「是潮牌 不是棒球」 — single line
  - Both lines max 8 characters, restrained editorial spacing

COLOR PALETTE: deep charcoal gray (background) + warm cream-camel (coat) + crisp white (MLB wordmark + main headline) + soft warm amber rim-light (single accent only) + black (cap) — strictly five tones, no extras.

STYLE: editorial fashion cover illustration, comic illustration not photo, magazine-grade typographic discipline, restrained luxury composition. The visual irony is intentional — a sports cap is treated as the cover-feature couture object. Jennie's likeness must read as illustrated portrait, not AI photo.

--ar 3:4 --stylize 250
```

## 如果要继续改

- 背景优先改什么：cyclorama 颜色 — 默认深炭灰；可改成米白（更温柔 Vogue 调）/ 砖红（更扎眼 i-D 调）/ 一抹上海弄堂虚化（实景背景，但会从「fashion editorial」滑回「street snap」需要谨慎）
- 大衣可换：默认 oversized 米驼大衣；可换 cropped tweed jacket（更 Chanel 时代 Jennie）/ oversized leather varsity（更街头）/ 黑白格 monogram 大衣（更街头 luxury）
- **不要动什么**：「MLB」当 masthead 顶在最上 + Jennie 单眼遮发的 i-D 招牌 — 这两个是这版的灵魂双标记；五色限制（多色就毁了）；`comic illustration not photo` 的渲染语言
- 标题字层级：MLB（masthead）> 主标「MLB 在上海」> 副标「是潮牌 不是棒球」> 右上 mono caption — 四层视觉权重不能反

## 视觉宪法合规说明

- **Person Recognition Gate**：Jennie Kim 评 92 分，HIGH tier，按规则直接用名字 + comic illustration 渲染（不需要 photo anchors）
- **photoreal 关键词清查**：prompt 全文未出现 `photorealistic / photoreal / studio photo / 8k photo / octane render / reference photo / hyperreal`；用 `physically-rendered manga figure with photo-accurate likeness, rendered as comic illustration (not photo)` 的 canonical 措辞，符合视觉宪法第 3 条
- **三层 illustration 约束**：rendering rule（subject 段）、masthead style line、final STYLE 段都显式写「comic illustration not photo」— 这是 photoreal 高发场景下的三道闸
- **生图后兜底**：如果第一张漂向 photoreal，下一版补 `2D illustration, flat shading, no photographic textures, no skin pore detail` 三段强制

## Concept layer 注释

这版同时承担两个 punchline：
1. **形式即论点** — 用 Vogue 封面语言讲一顶棒球帽，视觉就是「这是时装不是体育」
2. **隐藏路径** — 选 Jennie 原型而非中国模特，把「这股风从首尔吹来」隐写进图

正文负责给数字（一千家店 / 30% / 十几倍），封面负责给 mood 和 origin hint。两层互不打架。


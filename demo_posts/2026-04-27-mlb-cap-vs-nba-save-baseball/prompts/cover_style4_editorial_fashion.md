# MLB 帽封面 prompt — Style 4：杂志街拍封面（Editorial Fashion / Jennie 原型）

## 推荐风格

- 风格：High-fashion editorial street style cover — **Vogue China masthead 骨架 + i-D 半脸构图**（单眼半阖 / 单眼遮发）；模特原型走 Jennie（BLACKPINK）— 既奢华又街头，跟「MLB 是潮牌不是棒球」的 concept 同频
- 为什么选它：用最不像体育的视觉语言（时装杂志封）讲体育 IP，**形式本身就是论点**；选 Jennie 原型扣的是「韩流明星把这股风吹到上海街头」这条隐线 — 视觉自带答案
- 这张图最该卖什么：**「这不是体育，这是时装」+「这股风从首尔吹来」 — 一张图同时讲两件事**

## 标题与排版（已锁）

- 主标：**MLB 在上海**（5 字 / 简体）
- 副标：**是潮牌 不是棒球**（7 字 / 简体）
- 标题位置：**画面正中（chest height ~ 50% 垂直位置）放大字** — 为了 XHS feed 流缩图一秒识别
- masthead：「MLB」三个字母作为顶端杂志刊名巨字（保留 Vogue 风骨架，但缩小让位给中央大标题）
- 模特构图参考：i-D 招牌单眼半阖 / 一束发遮单眼

## Final Prompt

```text
A 3:4 vertical high-fashion editorial magazine cover, hybrid layout: Vogue China masthead discipline + i-D one-eye-covered half-face composition, deliberately treating an MLB cap as a couture object.

Subject: a single Korean idol model in her mid-20s, archetype based on Jennie Kim from BLACKPINK — almond eyes, defined jawline, soft full lips, signature confident yet detached expression. The face must be photo-accurate likeness of Jennie Kim, but rendered as comic illustration (not photo) — physically-rendered manga figure with photo-accurate likeness, clean ink linework on facial features, two-tone cell-shaded skin, fashion-illustration grade. One eye is softly half-closed (i-D signature gesture), the visible eye gazes calmly just past the camera lens. Mouth closed, expression composed.

Pose: three-quarter body framing — head, torso, and one hand visible. Straight-spined editorial posture, slight contrapposto. Both hands tucked into front coat pockets (do NOT raise hands to chest — chest area must be left clean for the centered title block). Composed, slightly aloof.

Wardrobe (luxury-streetwear hybrid, Jennie-coded):
- Black baseball cap with crisp white "MLB" wordmark on the front panel, worn straight, brim shadowing the upper face slightly. The cap is the single visual anchor of the cover.
- Oversized cream-camel wool overcoat with structured shoulders, soft drape, lapel collar. No visible brand markings.
- A single delicate silver chain at the neckline, half-hidden under the coat collar.
- Plain cream-white inner top.

Background: studio-grade seamless cyclorama in deep cool charcoal gray (Pantone 19-3906 territory), even diffused lighting, no environmental props, no street scene, no clutter. The figure stands isolated against flat color — this is what makes the image read as fashion editorial, not street snap.

Lighting: single soft key light from camera-upper-left creating a clean drop-shadow on camera-right side of the cap brim; faint hair-light catching the cap's top curve; tiny catch-light in the visible eye; slight warm rim-light barely catching the coat's left shoulder edge (this single warm tone evokes Shanghai golden-hour without showing any city).

Layout (Vogue China structure + i-D framing, optimized for XHS feed thumbnail visibility):
- Model occupies upper portion of frame; head at top-25% horizontal line so the chest/coat area below is open for a massive centered title block
- MLB cap is the visual peak at top, the centered title is the second visual anchor at mid-canvas
- One strand of hair falls across the closed eye (i-D move, must be deliberate not accidental)

TEXT OVERLAY — Simplified Chinese only (NO Traditional Chinese characters anywhere). Hybrid of compact Vogue masthead at top + massive XHS-feed-friendly center headline:

- Top masthead (medium-large condensed serif, warm off-white, centered): 「MLB」 — top 8% of canvas only (smaller than a typical magazine masthead so the centered title gets visual priority); set as the magazine nameplate but restrained

- Top-right corner mono caption stack (very small, low opacity warm gray): 「VOL. 04 / 2026」 / 「上海」 / tiny mock barcode below — must NOT compete with centered title

- **CENTER MAIN TITLE BLOCK — the dominant visual element after the cap**, positioned at vertical 45-62% of canvas (across the model's chest/coat area), horizontally centered, occupying roughly 75-85% of canvas width:
  - 主标 main headline (Simplified Chinese): 「MLB 在上海」 — set as MASSIVE bold modern Simplified-Chinese sans-serif, characters approximately 11-13% of canvas height each, warm crisp off-white, single line, centered. Sits at vertical 47-55% of canvas. This text must be readable even when the cover is shrunk to 200px-wide thumbnail in the XHS feed.
  - 副标 sub-headline (Simplified Chinese): 「是潮牌 不是棒球」 — directly below 主标, large condensed Simplified-Chinese sans-serif, characters approximately 6-7% of canvas height, soft warm white, single line, centered. Sits at vertical 56-62% of canvas.
  - Subtle treatment behind text for legibility against the camel coat: a barely-perceptible soft gradient darkening behind the title text only (NOT a hard band — gradient must not look like a billboard)
  - Restrained editorial letter-spacing; both lines must read as ONE coherent title block, not two separate elements

- All Chinese characters MUST be SIMPLIFIED CHINESE (简体中文). Do NOT render any traditional/繁体 character variant. Verify each character: 在 (not 在 with extra strokes), 是 / 潮 / 牌 / 不 / 棒 / 球 / 上 / 海 — all simplified forms.

COLOR PALETTE: deep charcoal gray (background) + warm cream-camel (coat) + crisp white (MLB wordmark + main headline) + soft warm amber rim-light (single accent only) + black (cap) — strictly five tones, no extras.

STYLE: editorial fashion cover illustration, comic illustration not photo, magazine-grade typographic discipline, restrained luxury composition. The visual irony is intentional — a sports cap is treated as the cover-feature couture object. Jennie's likeness must read as illustrated portrait, not AI photo.

--ar 3:4 --stylize 250
```

## 如果要继续改

- 背景优先改什么：cyclorama 颜色 — 默认深炭灰；可改成米白（更温柔 Vogue 调）/ 砖红（更扎眼 i-D 调）/ 一抹上海弄堂虚化（实景背景，但会从「fashion editorial」滑回「street snap」需要谨慎）
- 大衣可换：默认 oversized 米驼大衣；可换 cropped tweed jacket（更 Chanel 时代 Jennie）/ oversized leather varsity（更街头）/ 黑白格 monogram 大衣（更街头 luxury）
- **不要动什么**：「MLB」当 masthead 顶在最上 + Jennie 单眼遮发的 i-D 招牌 — 这两个是这版的灵魂双标记；五色限制（多色就毁了）；`comic illustration not photo` 的渲染语言
- 标题字层级（已为 XHS feed 调整）：**主标「MLB 在上海」（巨字中央）> MLB masthead > 副标「是潮牌 不是棒球」> 右上 mono caption** — 中央大标题升为最高权重，masthead 让位
- XHS feed 缩图测试：把封面缩到 200px 宽，主标必须仍可识别；如果不行，再放大 10-15%

## 视觉宪法合规说明

- **Person Recognition Gate**：Jennie Kim 评 92 分，HIGH tier，按规则直接用名字 + comic illustration 渲染（不需要 photo anchors）
- **photoreal 关键词清查**：prompt 全文未出现 `photorealistic / photoreal / studio photo / 8k photo / octane render / reference photo / hyperreal`；用 `physically-rendered manga figure with photo-accurate likeness, rendered as comic illustration (not photo)` 的 canonical 措辞，符合视觉宪法第 3 条
- **三层 illustration 约束**：rendering rule（subject 段）、masthead style line、final STYLE 段都显式写「comic illustration not photo」— 这是 photoreal 高发场景下的三道闸
- **生图后兜底**：如果第一张漂向 photoreal，下一版补 `2D illustration, flat shading, no photographic textures, no skin pore detail` 三段强制
- **简体中文强制**：prompt 显式写「Simplified Chinese only, NO Traditional」并逐字列出（在/是/潮/牌/不/棒/球/上/海）— 避免 Midjourney / Sora 偶发画繁体

## Concept layer 注释

这版同时承担两个 punchline：
1. **形式即论点** — 用 Vogue 封面语言讲一顶棒球帽，视觉就是「这是时装不是体育」
2. **隐藏路径** — 选 Jennie 原型而非中国模特，把「这股风从首尔吹来」隐写进图

正文负责给数字（一千家店 / 30% / 十几倍），封面负责给 mood 和 origin hint。两层互不打架。


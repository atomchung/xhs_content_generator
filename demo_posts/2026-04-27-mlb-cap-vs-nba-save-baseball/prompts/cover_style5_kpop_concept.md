# MLB 帽封面 prompt — Style 5：韩流偶像专辑封风（K-pop Concept Photo）

## 推荐风格

- 风格：K-pop concept photo cover — 柔光 / 粉紫渐变 / 偶像写真排版 / 韩文小字 detail，整体偶像专辑封面感
- 为什么选它：直接挑明背后真相 — 这股 MLB 风**就是韩流偶像穿出来的**。用韩国偶像专辑封面的视觉语言讲一个「美国体育 IP 在中国靠什么红」的故事，画面本身就是答案。这是五种里 concept layer 最深的一版
- 这张图最该卖什么：**视觉先告诉你答案 — 这股风的源头不在纽约，在首尔**

## Final Prompt

```text
A 3:4 vertical K-pop album cover style poster, dreamy concept-photo aesthetic with soft pastel gradient and idol-photoshoot composition.

Subject: a single androgynous young East-Asian person in early 20s, soft delicate features, photo-accurate East-Asian likeness rendered as comic illustration (not photo). The figure is captured in a relaxed concept-photo pose — head tilted slightly down-and-right, hand brushing the cap brim, eyes half-closed in a soft contemplative expression, parted lips. Clean modern haircut with a single fringe strand falling over the brow.

Wardrobe: black baseball cap with crisp white "MLB" wordmark, worn slightly tilted in styling — the cap is the styling anchor of the entire concept. Soft cream oversized cardigan over a thin white inner tee, one delicate silver earring catching highlight.

Background: dreamy cool-warm gradient sky transitioning from soft lavender at top to peach at bottom, faint pink-tinted lens flare at upper-right, blurred bokeh of distant city lights at lower edge, atmospheric haze. The mood is melancholic, soft, idol-poster contemplative — NOT energetic, NOT street.

Rendering rules:
- physically-rendered manga figure with photo-accurate likeness, rendered as comic illustration (not photo)
- soft cell-shaded skin with pastel undertones (cool peach + soft lavender bounce)
- crisp ink line ONLY on the cap edge and MLB wordmark, soft anti-aliased lines on facial features
- background fully painted with soft gradient, no hard edges
- overall finish: matte pastel, like a Korean idol's solo concept photo

Lighting: soft diffused even key light, no harsh shadows, faint warm rim-light on the cap brim from upper-right.

Layout: figure centered slightly upper-frame, large amount of pastel sky above for typography, small caption space at bottom.

TEXT OVERLAY — Korean idol album cover typography discipline:
- Top headline (medium-large delicate serif, warm white): 「中国一千家 MLB 店」 — top 14% of canvas, restrained not aggressive
- Subline directly below (small condensed Chinese sans): 「但它从来不是从美国传来的」
- Top-right small Korean caption (mono, low opacity): 「서울 → 상하이」 (meaning Seoul → Shanghai), then below it 「2021 — 2023」
- Bottom-center tiny credit line (mono, low opacity warm gray): 「from a Korean company, not the American league」

COLOR PALETTE: soft lavender + warm peach + cream + warm off-white type + crisp white MLB wordmark + a single charcoal black (only on the cap).

STYLE: K-pop concept photo cover illustration, comic illustration not photo, dreamy idol-album restraint, melancholic-soft mood, magazine-grade composition discipline. The visual irony is intentional — this is a Korean idol album cover used to tell an American baseball brand's story.

--ar 3:4 --stylize 250
```

## 如果要继续改

- 背景优先改什么：渐变色调 — 默认 lavender + peach；可改成 mint + butter（更春天感）/ powder blue + dusty rose（更冷冬感），一次只换一组
- 不要动什么：韩文小字「서울 → 상하이」是这版的灵魂 punchline，**不能换成中文** — 这一行字的存在本身就是论点；MLB 帽作为「styling anchor」而非「sport item」的处理
- 关键约束：禁 photoreal 关键词；prompt 里 K-pop concept photo 是视觉语言不是真照片，要用 illustration not photo 反复约束

## 视觉宪法合规说明

K-pop concept photo 是 photoreal 高发场景。本 prompt 三处显式 illustration not photo 约束。如果生图漂向 photoreal，下一版加 `2D illustration, soft cell shading, no skin texture, no photographic grain`。

## Concept layer 注释

这是五种里唯一一种**视觉本身就承担 punchline** 的：
- Style 1（cyberpunk）：讲「衣服已脱钩运动」
- Style 2（mascot Q）：讲「衣服热 vs 比赛冷」
- Style 3（portrait comic）：讲「一张脸 + 一顶帽，让你代入」
- Style 4（editorial fashion）：讲「这是时装不是体育」
- **Style 5（K-pop concept）：讲「源头是首尔，不是纽约」 — 视觉直接给答案，正文负责给数字**

如果要选「最不解释也能让人愣一下」的，选 5。


# 道奇 = 日本队 封面 v7 — 一百公尺电影海报版（已选定）

## Person Recognition Gate
```json
[
  {"person": "Shohei Ohtani / 大谷翔平", "confidence": 92, "tier": "HIGH", "reason": "全球级超巨", "anchors_suggestion": "直接用名字"},
  {"person": "Yoshinobu Yamamoto / 山本由伸", "confidence": 65, "tier": "MED", "reason": "棒球圈外辨识度中等", "anchors_suggestion": "#18 短发 lean 5'10\" 平静面孔"},
  {"person": "Roki Sasaki / 佐佐木朗希", "confidence": 55, "tier": "MED", "reason": "新签约国际辨识度低", "anchors_suggestion": "#11 短黑发 6'2\" 修长 25 岁较年轻面孔"}
]
```

## 推荐风格
- 风格：**「100 Meters / 一百公尺」(2024) Studio 4°C 电影海报版式**
- 为什么选它：v6 已锁定一百公尺为画面美学；本版叠加该电影**官方海报**的版式语言（单一巨型主角 + 顶部 3 人卡 + 大字纵向标题 + 厚涂水彩背景）— 让一张图直接读起来像「一部新海报」，CTR 心理路径走「电影感新作」而不是「体育新闻封面」
- 这张图最该卖什么：「优衣库为什么冠名道奇球场」八个字像电影主标 + 三位日本投手像电影主演阵容，一句视觉宣言

## Final Prompt

```text
A 3:4 portrait Japanese animation film poster in the visual language of "100 Meters / 一百公尺" (2024, Studio 4°C, Wataru Iwaisawa). Compose the entire image as a real movie poster, not a sports photo.

POSTER LAYOUT (top to bottom):

— Top 12% strip: three character portrait cards aligned horizontally, equal width, separated by thin cream borders. Each card shows a head-and-shoulders watercolor portrait of one Japanese MLB pitcher in Dodgers cream pinstripe uniform with cap, painted in the soft 2D animation style of 100 Meters — confident brush-pen outlines, minimal interior shading, sun-flare backlight. Below each portrait, a small clean white label in two lines: Chinese name (top) and jersey number (bottom).
  - Left card: Roki Sasaki, label "佐佐木朗希  #11", tall lean 25-year-old with short black hair, calm focused expression
  - Middle card: Yoshinobu Yamamoto, label "山本由伸  #18", neat short black hair, athletic compact build, calm composed expression
  - Right card: Shohei Ohtani, label "大谷翔平  #17", signature calm half-smile, lean muscular build

— Center 60% main visual: Shohei Ohtani as the dominant single hero, painted at 3/4 body height, captured at the apex of his pitching delivery — torso fully torqued, throwing arm whipping forward, fastball just released and suspended in air. The painting style is pure 100 Meters film aesthetic: fluid hand-drawn 2D character with painterly watercolor body, expressive bold brush-pen outlines, sun-flare backlight pouring in from upper right. He occupies center-left of the frame with the throwing arm extending into negative space on the right.

— Background behind hero: thick painterly watercolor wash of dreamy Dodger Stadium light — pale Dodger blue sky bleeding into warm cream sunset, several large soft-edged sun-flare orbs floating around the upper right, abstract dust mote texture. NO architectural detail, NO crowd. Pure light + watercolor.

— Title block (large, occupies bottom-center 25% of frame): the main Chinese title 「优衣库为什么冠名道奇球场」 set in bold confident vertical-feeling kinetic typography, dark navy ink with subtle red dropshadow, sized to be the strongest type element on the poster. Title typography style references 100 Meters film logo's calligraphic ink-brush energy, but cleaner and Chinese.

— Below title: small horizontal credits-strip line in soft gray Chinese: "道奇 已经穿上 UNIQLO ｜ 2026 春".

— Bottom-right corner: small clean red Uniqlo wordmark logo, the only fully saturated red in the entire poster.

COLOR PALETTE: pale cream + powder Dodger blue + warm sunset peach + the single saturated Uniqlo red as accent only on chest patches and bottom-right logo. Watercolor bleed at color edges. Slight overexposure on right-side highlights.

WARDROBE DETAIL: all three pitchers in Dodgers home cream pinstripe uniforms with bold red UNIQLO wordmark patch on chest where the Dodgers script would normally sit, rendered in the same painterly stroke as the rest of the uniforms.

EXCLUSIONS: no 90s manga screentones, no comic panel borders, no comic break-out, no 3D CG cel-shading, no speed lines, no shonen sound effects, no Pop Art, no minimal flat illustration, no photoreal stadium image. Pure 2024-era Studio 4°C painterly Japanese animation film poster only.

--ar 3:4 --stylize 400
```

## 如果要继续改
- 想再放大电影感：在主视觉上方再加一行小字英文「A NEW JAPAN ARRIVES IN LOS ANGELES」
- 想强化海报感：底部加一行手写电影 staff credits（虚构的导演 / 制片字样）
- 三人卡顺序可调：现按「年轻 → 熟练 → 巨星」从左到右递进
- 不要动：100 Meters 笔触 / 厚涂水彩背景 / 唯一红 = Uniqlo / 主标版式 / 三人顶部卡

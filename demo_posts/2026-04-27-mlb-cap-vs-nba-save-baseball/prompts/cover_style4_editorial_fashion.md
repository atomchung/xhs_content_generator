# MLB 帽封面 prompt — Style 4：杂志街拍封面（Editorial Fashion）

## 推荐风格

- 风格：High-fashion editorial street style cover（Vogue / Hypebeast / 安邸 风），冷光 + 大留白 + 大字标题压底
- 为什么选它：本篇 punchline 就是「MLB 是潮牌不是棒球」。用最不像体育的视觉语言（时装杂志封面）来讲一个体育 IP 的故事，**形式本身就是论点**。这是五种里 concept tension 最强的一版
- 这张图最该卖什么：**「这不是体育，这是时装」 — 用一张高冷杂志封反写棒球**

## Final Prompt

```text
A 3:4 vertical high-fashion editorial magazine cover, the visual language of Vogue / i-D / Hypebeast street style covers, deliberately treating an MLB cap as a couture object.

Subject: a single Chinese model in their early 20s, sharp angular pose, three-quarter body framing — head, torso, and hands visible. Composed and confident expression, mouth closed, eyes locked just past the camera lens. The model wears a black baseball cap with crisp white "MLB" wordmark, oversized neutral-tone overcoat in soft camel, statement silver chain barely visible at neckline, hands tucked into front pockets, posture straight-spined and editorial. Photo-accurate East-Asian likeness rendered as comic illustration (not photo) — clean ink linework, two-tone cell shading, fashion-illustration grade.

Background: studio-grade seamless cyclorama in deep cool charcoal gray, even diffused lighting, no environmental props, no street, no clutter. The figure stands isolated against pure flat color — this is what makes it read as fashion editorial, not street snap.

Lighting: a single soft key light from camera-upper-left creating a clean shadow on the camera-right side of the cap brim; barely-there hair light catching the cap's top curve; tiny catch-light in the eyes.

Layout: model occupies center of frame, leaving a wide top band and a wide bottom band of negative space deliberately for typography. The MLB cap sits at roughly the upper-third horizontal line.

TEXT OVERLAY — full magazine masthead treatment, restrained luxury typography:
- Top masthead band (large condensed serif, warm off-white): 「MLB」 — set huge across the top 12% like a magazine logotype, treated as if MLB were the magazine's title
- Top-right small mono caption: 「VOL. 04 / 2026」 / 「中国一千家店」 stacked
- Bottom band (clean condensed sans, warm off-white): 「背后没一个美国人 / 一家韩国公司在卖」 — two lines, max 8 characters per line, bottom 18% of canvas
- Bottom-right tiny corner barcode mock — pure graphic decoration, low opacity

COLOR PALETTE: deep charcoal gray + warm camel coat + warm off-white type + crisp white MLB wordmark — strictly four tones, no extras.

STYLE: editorial fashion cover illustration, comic illustration not photo, deliberate visual irony of treating a sports cap as luxury object, restrained luxury composition, magazine-grade typographic discipline.

--ar 3:4 --stylize 250
```

## 如果要继续改

- 背景优先改什么：cyclorama 颜色 — 深炭灰 → 米白（更温） / 砖红（更扎眼）；不要换成实景，一换实景就掉回街拍
- 不要动什么：「MLB」当 masthead 顶在最上的处理（这个反讽必须保留）；四色限制（多色就毁了）；comic illustration not photo 的渲染语言
- 关键约束：禁 photoreal 关键词 — 「fashion editorial」很容易被生图工具误读成 photoreal，prompt 里要反复强调 illustration not photo

## 视觉宪法合规说明

杂志封面是 photoreal 的高发场景。这版 prompt 三处显式约束（rendering rule、masthead style、style line）确保收到的是漫画化插画，不是 AI 假照片。如果生图工具仍漂向 photoreal，下一版加 `2D illustration, flat shading, no photographic textures` 三段强制。


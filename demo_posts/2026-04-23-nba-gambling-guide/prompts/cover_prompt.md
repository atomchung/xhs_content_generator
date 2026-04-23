# NBA 赌盘主题封面 prompt — v1

## 推荐风格
- 风格：Editorial Collage（体育商业杂志拼贴）
- 为什么选它：这是商业 / 合规主题，不是球员动作题，所以跳过 canonical comic break-out。题目要同时装下「人物被挂在市场上」+「赌盘 UI」+「资金流」，collage 能把这些元素压成一张视觉海报
- 这张图最该卖什么：冲突——球员身影 + 赌盘数字 + 「最脆的一环」这三件事叠在一起的压迫感
- 真人风险处理：**不画具体球员**。主体用 **anonymous NBA silhouette / back view + blurred jersey number**，直接规避 Person Recognition Gate；不出现真实球员名字、不出现可辨脸部特征

## Final Prompt

```text
Editorial sports magazine collage cover, 3:4 vertical aspect ratio, investigative journalism aesthetic.

Main subject: an anonymous NBA player seen from behind, mid-court, wearing a generic modern NBA jersey with the number intentionally blurred / unreadable, shoulders slumped, standing alone on a hardwood court under a single overhead spotlight. No face visible. No team logo visible. Not based on any real player.

Around and behind him, a layered collage of sports betting UI fragments: a semi-transparent mobile sportsbook interface showing "PLAYER PROPS" and "UNDER" in bold, odds numbers like "-110" and "+180" floating as cut-out paper pieces, a shadowy chart with arrows representing money flow, torn newspaper headlines reading "INTEGRITY ALERT" and "LIFETIME BAN", a faint stack of $100 bill textures fading into the background.

Color palette: desaturated court-wood brown + deep navy + accent crimson red (for the "UNDER" text and warning elements) + a single neon green line graph. Moody, noir-editorial lighting — not bright, not flashy, feels like a long-form investigative feature.

Composition: clear top 1/3 reserved for a bold Chinese headline block (leave negative space), middle 1/2 is the silhouette + collage layers, bottom 1/4 has smaller scattered betting UI elements fading out.

Texture: slight paper grain, subtle halftone dots in the red accent areas, edges of collage pieces visible like torn magazine scraps.

Style references: Bloomberg Businessweek cover design, The Athletic investigative feature layout, ESPN The Magazine editorial illustration.

No text rendered by the AI — all Chinese headline text will be overlaid in post-production. Any betting UI text should be short English fragments only (ODDS, UNDER, PROP, ALERT).

--ar 3:4 --stylize 300
```

## 如果要继续改

- 背景优先改什么：如果 collage 元素显得太散，把赌盘 UI 的数量从 4-5 片减到 2-3 片，让中央剪影更突出
- 如果颜色看起来太 pop，压暗整体曝光再加 paper grain
- 不要动什么：
  - anonymous / back view / blurred jersey number 这三条不能动，是规避肖像风险的硬锚点
  - 「no text rendered by the AI」也不能动——标题交由用户用阿里巴巴普惠体 Bold 后期叠加，不让 AI 写中文
  - 3:4 竖版不能改

## 标题叠加指引（后期 overlay）

- 标题：`NBA 最怕的不是谁赢`（第一行）/ `是球员卖自己`（第二行）
- 字体：阿里巴巴普惠体 Heavy
- 颜色：白字 + 细红描边（呼应 collage 里的 crimson accent）
- 位置：占据上 1/3 预留的 negative space，左对齐

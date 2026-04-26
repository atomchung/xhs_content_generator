# 道奇日本赞助轨迹 P2 prompt

## Person Recognition Gate
- 本页不出现真人（数据 / 品牌图）。Tadashi Yanai 🔴 LOW，不入图，仅以「Uniqlo 红圈 logo + 创始人家族标记」抽象代替。

## 推荐风格
- 风格：Bloomberg / Sportico / FT 风格的杂志级编辑信息图
- 为什么选它：本页核心是「钱的轨迹 + 一个封顶冠名」，必须用图表语言而不是球员动作。photoreal 球场镜头无法承载 5 个时间节点 + 数字
- 这张图最该卖什么：从 2018 → 2026 的日本赞助总额曲线 + Uniqlo 封顶节点 = 「洛杉矶队怎么变成日本队」的一句话视觉证明

## Final Prompt

```text
A clean editorial 3:4 portrait infographic in the style of Bloomberg Businessweek / Sportico / Financial Times sports business feature. Dodger blue (#005A9C) and cream (#EFE4D2) base palette, Uniqlo red (#FF0000) used only as accent on key callouts.

Top quarter: bold black headline in Chinese reading "从洛杉矶队 到 日本队", with subtitle in smaller weight reading "道奇日本赞助 8 年涨了 10 倍".

Center 60% of frame: a tall vertical ascending line chart from bottom-left to upper-right, showing five labeled data points plotted on a timeline axis (years on Y axis, revenue on X axis flipped to climb upward visually). Each node is a small circular dot connected by a thick blue line that thickens as it rises:

- 2018: small dot, label "Ohtani 加入天使 / 日赞助 ~$10M (估)"
- 2023/12: medium dot, label "Ohtani 签道奇 10年7亿 / 97%延期"
- 2024: medium dot, label "ANA + Daiso + Toyo + Kowa 新增 / +$70M 估"
- 2025: large dot, label "新增 6 家日本赞助 / 总 20 家 / 全队赞助突破 $200M"
- 2026/03: largest dot in bright Uniqlo red, label "UNIQLO FIELD 冠名 5 年 ≥$125M"

The 2026 node should visually pop with a red glow and a small Uniqlo wordmark badge next to it.

Lower 15% of frame: a horizontal callout box with thin gold border containing two facts in clean Chinese sans-serif:
- 左 box: "Uniqlo 在美国体育的 第一次大单"
- 右 box: "76 个赞助商里 / 20 个来自日本"

Bottom strip: small data source line in light gray Chinese: "数据：MLB.com / Sportico / Japan Times / SponsorUnited"

Typography: clean modern sans-serif, mix of large bold Chinese headline + smaller Chinese body + Latin numerals. No emojis. No watercolor. No comic style. No photorealistic stadium image. No real human figures.

Layout style: editorial financial magazine spread, generous white/cream space, single dominant chart, calm hierarchy.

--ar 3:4 --stylize 200
```

## 如果要继续改
- 优先改：可以把 X/Y 轴换成更明显的「时间 vs 金额」双轴；或把 Uniqlo node 做成红色矩形 chip 而不是圆点
- 不要动：5 个节点的时间和金额；2026 红色高亮；蓝/奶/红三色限定；Bloomberg 编辑信息图风格

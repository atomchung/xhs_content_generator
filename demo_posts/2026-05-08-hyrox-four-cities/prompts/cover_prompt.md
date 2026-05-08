# Hyrox 全球 4 城补充图 prompt — 同一只桃子，4 种背景

## 推荐风格
- 风格：小桃子吉祥物 2x2 国家拼图（继承 5-16 主帖 + 规则图同款角色 + 配色）
- 为什么选它：
  - 同款桃子角色 + 暖米/红/黑配色 = 视觉一致性强化账号 IP
  - 「同一只桃子在 4 个城市跑」= 比纯世界地图更有人设感，用角色一致性反衬背景多样性
  - 2x2 拼图 XHS 信息流认知成本低，差异 0.3 秒被感知
- 用途：5-16 主帖补充图（可替代或并列 page3 世界地图），也可独立发
- 这张图最该卖什么：**4 个差异巨大的城市背景 = 「Hyrox 是真全球」的视觉证据**

## Story Atoms
- 主角：**同一只**小桃子吉祥物在 4 个城市分别做 Hyrox 动作（IP 一致 + 背景换 4 种）
- 4 城选择 = 4 个 Hyrox 故事阶段：
  - 🇩🇪 **柏林 Berlin** — Hyrox 故乡，2017 创立地（**起源**）
  - 🇺🇸 **拉斯维加斯 Las Vegas** — Hyrox World Championship 主办（**顶峰**）
  - 🇮🇳 **班加罗尔 Bengaluru** — 8,200 人 / 1 年 5 倍（**爆发**）
  - 🇨🇳 **上海 Shanghai** — 5-16 中国首战（**新战场**）
- 阅读顺序（左上→右上→左下→右下）= 时间线 + 地理跳跃，右下角上海 = 中文读者视线终点 = 转化效率最高
- 视觉差异锚（per-cell 配色 + 地标）：
  - 柏林：cool blue-gray dawn + Fernsehturm 电视塔 + Brandenburg Gate
  - 维加斯：vibrant magenta-purple neon night + Strip casinos
  - Bengaluru：warm golden midday + 殖民圆顶建筑 + 棕榈树
  - 上海：warm orange-navy sunset + 东方明珠 + 陆家嘴三件套
- 情绪冲突：「同一只小桃子」（IP 一致）vs 「4 种完全不同的世界」（全球性）→ 一致中的多样

## Generation Order
1. 角色锚 — 复用规则图同款桃子（确认 IP 一致）
2. 单 cell 测试 — 先跑 1 个城市（建议从上海开始，参考好找 + 错了好调）
3. Final 4-cell composite — 满版生成

## 角色一致性锚（每次新生图都要复述一次）
```text
Character anchor: round bald-headed chibi peach mascot with small bright-green leaf sprout on top of head, pale-beige skin (#F4D9C2), two large solid black dot eyes with single small white highlight, two small pink blushing cheek circles, no nose, open mouth showing one tooth (determined / shouting expression), solid bright-red (#E63946) onesie / one-piece T-shirt, stubby short arms and legs, thick consistent black outline, kawaii Chinese mascot illustration style.
```

## Final Image Prompt（直接给生图工具）
```text
Magazine-style 2x2 city-grid poster, 3:4 vertical layout, "Hyrox around the world" theme in established peach-mascot account style.

TOP (~16% of canvas):
- Massive bold red sans-serif Chinese headline 「Hyrox 跑遍 4 大城」 with thick white outline and black drop shadow
- Behind headline, manga-style red-orange radiating speed lines emanating from top center
- Smaller black bold subline below: 「同一只桃子，4 种城市」

MIDDLE GRID (middle ~74%):
2x2 grid (2 rows, 2 columns) of 4 city cells, each cell shows the same peach-mascot performing a Hyrox action in front of a distinct city skyline silhouette. Each cell has a thin hand-drawn black frame.

Mascot identity (MUST be identical across all 4 cells): round bald-headed chibi peach character with small bright-green leaf sprout on top of head, pale-beige skin, two large solid black dot eyes with single white highlight, two pink blushing cheek dots, no nose, open mouth showing one tooth, solid bright-red onesie / one-piece T-shirt, stubby short arms and legs, thick consistent black outline.

- Cell 1 — TOP-LEFT — Berlin 🇩🇪 (Hyrox origin):
  Background: Berlin TV Tower (Fernsehturm) silhouette on left + Brandenburg Gate silhouette on right, cool blue-gray dawn sky gradient, dim mood. Mascot in mid-stride running pose with one leg lifted, focused expression, small blue sweat drop.
  Bottom of cell: white text label "柏林 Berlin · Hyrox 故乡 since 2017".

- Cell 2 — TOP-RIGHT — Las Vegas 🇺🇸 (World Championship):
  Background: Las Vegas Strip casino skyline silhouette (replica Eiffel Tower, large sphere venue, casino marquees) with neon sign accents, vibrant magenta-purple-pink night sky gradient. Mascot squatting and throwing a yellow medicine ball upward at a wall target.
  Bottom of cell: white text label "拉斯维加斯 Las Vegas · 世锦赛".

- Cell 3 — BOTTOM-LEFT — Bengaluru 🇮🇳 (India breakout):
  Background: outdoor open plaza with Indian colonial-era government building silhouette (Vidhana Soudha-style domes) + tall palm trees on both sides, warm golden midday sun, hint of soft red dust haze. Mascot in deep lunge pushing a heavy black sled forward with both hands.
  Bottom of cell: white text label "班加罗尔 Bengaluru · 8,200 人 1 年 5 倍".

- Cell 4 — BOTTOM-RIGHT — Shanghai 🇨🇳 (China debut):
  Background: Shanghai Bund skyline silhouette with Oriental Pearl TV Tower (left) + Lujiazui supertall trio (Shanghai Tower, World Financial Center, Jin Mao Tower, right side), warm orange-to-navy sunset sky gradient. Mascot mid-stride sprinting toward viewer with arms pumping, determined expression.
  Bottom of cell: white text label "上海 Shanghai · 5-16 中国首战".

Each cell's city skyline is rendered as a flat silhouette slightly darker than the sky gradient. Mascot scale is identical across all 4 cells (~50% of cell height). Each cell's sky color is distinct (Berlin cool blue-gray / Vegas magenta-purple / Bengaluru warm gold / Shanghai orange-navy) but all share the same red mascot uniform and black outline treatment.

BOTTOM (~10%):
- Centered black bold caption: 「全球 100+ 站，覆盖 57 国家 / 赛事」
- Small black "HYROX" wordmark bottom-right corner

OVERALL OUTSIDE-CELL BACKGROUND (header band, footer band, inter-cell gutters): warm cream-beige base color (#F5EBDD), matches account visual anchor.

COLOR PALETTE: warm cream-beige base + bold pure red (mascot uniforms + headline) + solid black (outlines, text, landmark silhouettes) + per-cell sky gradient (Berlin cool blue-gray / Vegas magenta-purple / Bengaluru warm gold / Shanghai orange-navy) + small light-blue sweat drops + bright green for leaf sprout + yellow accent for medicine ball.

STYLE: kawaii Chinese 小红薯 mascot poster, manga energy lines on title only, thick consistent black outlines, flat clean colors with light cell-shading, kid-book illustration aesthetic. City landmarks rendered as flat silhouettes (shape recognition only, no surface detail). Avoid photoreal, avoid 3D rendering. Each cell readable at thumbnail size in XHS feed.

--ar 3:4 --stylize 250
```

## 推荐
- 4 城选择背后的逻辑：起源（柏林）+ 顶峰（维加斯）+ 爆发（Bengaluru）+ 新战场（上海）= 4 个完整 Hyrox 故事阶段，缺一个故事就有断层
- 阅读路径（左上→右上→左下→右下）= 时间线，右下角落到上海 = 中文读者视线终点，转化锚点
- 适合作为：5-16 主帖 page3（世界地图）的替代版本，比纯地图更有人设感

## 如果要继续改
- 替换城市候选池（如果生图工具识别不出地标）：
  - 柏林 → 伦敦（大本钟 / 伦敦眼，地标识别度更高，但牺牲「Hyrox 起源」叙事）
  - 拉斯维加斯 → 纽约（自由女神 / 帝国大厦，但牺牲「世锦赛」叙事）
  - Bengaluru → 孟买（Gateway of India 海岸线，地标更国际通用）
  - **上海不要换**（中国首战是叙事核心）
- 不要动什么：
  - 红色小桃子角色（IP 锚）
  - 暖米底 + 红 + 黑配色（视觉锚）
  - 4 cell 的色温差异（Berlin 冷 / Vegas 紫 / Bengaluru 金 / 上海橙 — 这是「全球感」的视觉关键）
- 数字层级要保住：标题 > 城市名 > 城市 tag > HYROX 角标
- 风险与回退：
  - 4 城地标对生图工具偏挑战，第一次出图建议先单 cell 测试再合成
  - 如果 Bengaluru / Vegas 地标怎么 prompt 都不像，回退方案：换更好识别的伦敦 + 纽约
  - 如果 4 cell 信息密度过满 → 改 1x4 横条 layout（垂直堆叠 4 cell），单 cell 内信息量减少

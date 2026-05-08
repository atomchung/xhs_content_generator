# Hyrox 规则 101 解释图 prompt — 8 跑 + 8 关

## 推荐风格
- 风格：小桃子吉祥物 + 漫画动态线（继承账号已验证的红薯/桃子吉祥物视觉锚）
- 为什么选它：
  - 用户给的参考图就是这个风格 + 配色，账号在 XHS 已经被读者认作「红色小桃子 = 我们家 Hyrox」
  - 漫画动态线（manga 集中线）+ 暖米底配色 = 既有教育图的可读性，又有热血感，不像 PPT
  - 与 5-16 主帖（meme 表情包众生相）形成「主帖搞笑 + 科普图正经」的内容矩阵差异
- 这张图最该卖什么：**「8 跑 + 8 关」一句话规则 + 8 个站点视觉化让小白 5 秒看懂**

## Story Atoms
- 主角：同一个红色小桃子吉祥物在 8 个 cell 里分别做 8 个动作（保持角色一致 = 强化 IP 记忆）
- 动作清单（按 Hyrox 官方顺序 1–8）：
  1. SkiErg 滑雪机 1000m
  2. Sled Push 推雪橇 50m
  3. Sled Pull 拉雪橇 50m
  4. Burpee Broad Jumps 波比跳远 80m
  5. Rowing 划船机 1000m
  6. Farmers Carry 农夫走 200m
  7. Sandbag Lunges 沙包弓步 100m
  8. Wall Balls 壁球 100 次（男）/ 75 次（女）
- 信息层级：标题「HYROX 怎么玩」> 副标「8 跑 + 8 关」> 8 个站点 cell > 底部完赛时间
- 情绪冲突：「看起来好简单」的一格图卡 vs 「实际想跑死人」的真实体感（用动态线 + 汗滴暗示）
- 背景符号：暖米底 + 红 + 黑（参考图配色）+ 不再加上海剪影（科普图保持干净，外滩留给主帖封面）

## Generation Order
1. Mascot anchor — 先用一张图固定小桃子角色长相（避免 8 个 cell 角色不一致）
2. Single station test — 先只跑一个 cell（如 SkiErg）确认角色 + 动作能渲染对
3. Final 8-cell composite — 满版生成

## 角色一致性锚（每次新生图都要复述一次）
```text
Character anchor: round bald-headed chibi peach mascot with small bright-green leaf sprout on top of head, pale-beige skin (#F4D9C2), two large solid black dot eyes with single small white highlight, two small pink blushing cheek circles, no nose, open mouth showing one tooth (determined / shouting expression), solid bright-red (#E63946) onesie / one-piece T-shirt, stubby short arms and legs, thick consistent black outline, kawaii Chinese mascot illustration style.
```

## Final Image Prompt（直接给生图工具）
```text
Magazine-style infographic explainer poster, 3:4 vertical layout, Hyrox race rules explainer in established peach-mascot account style.

TOP (~22% of canvas):
- Massive bold red sans-serif Chinese headline 「HYROX 怎么玩」 with thick white outline and black drop shadow
- Behind headline, manga-style red-orange radiating speed lines emanating from top center
- Smaller black bold subline below: 「8 跑 + 8 关 = 一场比赛」

MIDDLE GRID (middle ~68%):
4x2 grid (4 rows, 2 columns) of 8 station cells, each cell has a thin hand-drawn black frame and shows the same peach-mascot demonstrating one Hyrox station.

Mascot identity (must be consistent across all 8 cells): round bald-headed chibi peach character with small bright-green leaf sprout on top of head, pale-beige skin, two large solid black dot eyes with single white highlight, two pink blushing cheek dots, no nose, open mouth showing one tooth, solid bright-red onesie / one-piece T-shirt, stubby short arms and legs, thick consistent black outline.

- Cell 1 (numbered "1" in red circle top-left of cell): mascot pulling down SkiErg ski-ergometer machine handles with both arms, blue sweat drop flying. Label below cell: "SkiErg 滑雪机 1000m"
- Cell 2 (numbered "2"): mascot in deep lunge pushing a heavy black sled forward with both hands, "HYROX" wordmark on sled. Label: "Sled Push 推橇 50m"
- Cell 3 (numbered "3"): mascot leaning back pulling a thick black rope attached to a black sled, both arms gripping rope. Label: "Sled Pull 拉橇 50m"
- Cell 4 (numbered "4"): mascot mid-air during a burpee broad jump, arms extended forward, legs extended back, motion lines. Label: "Burpee Jump 波比跳 80m"
- Cell 5 (numbered "5"): mascot seated on a rowing machine, pulling the handle to chest, knees bent. Label: "Row 划船 1000m"
- Cell 6 (numbered "6"): mascot walking forward holding two heavy black kettlebells, one in each hand, slight sway. Label: "Farmers Carry 农夫走 200m"
- Cell 7 (numbered "7"): mascot in deep forward lunge with a brown sandbag draped across both shoulders. Label: "Sandbag Lunges 沙包弓步 100m"
- Cell 8 (numbered "8"): mascot squatting then throwing a yellow medicine ball at a wall target high above head. Label: "Wall Balls 壁球 100 次"

Each cell number is a small bold red circle with white number in top-left corner. Between cells, tiny black running-mascot silhouettes with small "→" arrows implying "跑 1km between every station".

BOTTOM (~10%):
- Centered black bold caption: 「跑 8 公里 + 8 站 = 完赛 60–90 分钟」
- Small black "HYROX" wordmark bottom-right corner
- Tiny "上海站 5.16" tag bottom-left corner

BACKGROUND: warm cream-beige base color throughout. No Shanghai skyline (this is a clean explainer, not the cover). Cells visually separated by thin imperfect hand-drawn black frame lines (comic-book look).

COLOR PALETTE: warm cream-beige background + bold pure red for mascot uniforms, main headline, and number circles + solid black for outlines, text, sleds, kettlebells + small light-blue accent for sweat drops + pale-beige for mascot skin + bright green for leaf sprout + brown for sandbag + yellow for medicine ball.

STYLE: kawaii Chinese 小红薯 mascot infographic, manga energy lines on title only, thick consistent black outlines, flat clean colors with light cell-shading, kid-book illustration aesthetic. Avoid photoreal, avoid 3D rendering, avoid clutter. Each cell must be readable at thumbnail size in XHS feed.

--ar 3:4 --stylize 250
```

## 推荐
- 适合作为：单图科普 / Hyrox 入门指南帖的封面（独立帖）/ 5-16 主帖之外的科普 spinoff
- 角色一致性是这张图的命门：8 个 cell 里的小桃子必须看起来是同一只。如果某次生图发现角色漂移，砍到 4 个 cell + 加大 cell 尺寸
- 站点顺序不要乱：Hyrox 全球比赛固定 1→8 顺序，乱了会被懂行读者吐槽

## 如果要继续改
- 站点太多生图工具撑不住时，备用版面：
  - **6-cell 版**：砍掉 Sled Pull（和 Push 视觉相似）+ Sandbag Lunges（和 Burpee Jump 视觉相似），保留最有辨识度的 6 个
  - **2-page 版**：分成图 A（站点 1-4）+ 图 B（站点 5-8 + 完赛信息）
  - **Hero + 8 icon 环绕版**：中央一只大桃子在跑 + 8 个小站点 icon 围一圈
- 不要动什么：
  - 红色小桃子的角色长相（IP 锚）
  - 暖米底 + 红 + 黑配色（视觉锚）
  - 站点编号 1–8 的官方顺序
- 数字层级要保住：「HYROX 怎么玩」(头条) > 「8 跑 + 8 关」(副标) > 各 cell 标号 > 完赛时间
- 风险：8 cell 信息密度对生图工具偏挑战，第一次出图大概率角色不一致或文字糊。预期需要 2-3 次迭代

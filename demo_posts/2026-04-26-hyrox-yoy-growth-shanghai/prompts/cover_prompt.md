# Hyrox 续集封面 prompt — 4 种海报构图变体（小红薯 mascot 风）

## 推荐风格
- 风格：小红薯 mascot Q 版（参考用户提供的 `LET'S HYROX` 四格漫画样本）
- 为什么选它：上一版黑底霓虹黄 + 3 mascot 挤同一构图翻车，画面信息密度爆掉；这次锁死小红薯原型（peachy 圆豆身 + 红 T + 绿叶 + 厚黑描边 + 干净浅底），4 种海报构图同测找最稳的
- 这张图最该卖什么：**百万人在跑 + 上海站 5.16 倒数**

## 共用风格锁（4 个变体都不动）

角色四件套（一致到像同一只 mascot 的不同分身）：
- 草莓 / 圆豆形身体，**peachy-beige 肤色**（不是红色，红色只是 T 恤）
- 头顶一片绿色叶子（草莓蒂感）
- 厚一致的黑描边，flat cel-shaded illustration
- 点状黑眼 + 圆形粉色腮红 + 简单弧线嘴
- 红色短袖 T 恤覆盖躯干，**裸臂裸腿**（不画裤子）
- 短粗手脚，chibi 头身比约 1:1

底色规则：
- 暖白 / 米色 / 软粉橙底
- **禁止黑底**、**禁止霓虹黄底**（上一版翻车的来源）
- 道具用黑色（铁橇 / 壶铃 / sandbag），**不用黄色道具**

文字层：
- 中文走阿里巴巴普惠体 Bold/Heavy
- 英文走 HYROX 加粗 sans-serif
- 主色：深红字 + 黑描边（在浅底上）
- 必含：`--ar 3:4 --stylize 250`

---

## 走法 A — 起跑线群像（已选 · v2 动感强化版）

### Story Atoms
- 主角：6 个小红薯排在起跑线，朝镜头爆冲
- 动作瞬间：前排 3 个大尺寸冲刺姿（身体倾斜 / 单脚高抬 / 后脚扬尘）+ 后排 3 个小一号带 motion blur
- 动感增强：低视角仰拍 + 速度线 + 身体倾斜 + 后脚扬尘 + 汗珠成弧
- 文字精简：标题一句 + 副标一行，**画面里 HYROX 字样只在起跑拱门上出现一次**
- 情绪：起跑爆冲那一刻 + 标题质问 "又过了一年，他更赚钱吗" 的反差
- 卖点：标题是商业拷问，画面是体感冲刺，反差越强越抓人

### Final Prompt A

```text
High-energy race start-line action poster with chibi 小红薯-style mascots sprinting toward camera, 3:4 vertical magazine cover layout.

CHARACTER LOCK (apply to all 6 mascots):
- Round strawberry-shaped peachy-beige body with soft rounded base
- Single green stem leaf on top of head
- Thick consistent black outline, flat cel-shaded illustration
- Simple dot eyes (wide energetic expression), round pink blush cheeks, open shouting or determined mouths
- Red short-sleeve T-shirt covering torso, bare arms and bare short stubby legs
- Cute chibi proportions, head-to-body ratio about 1:1

DYNAMIC POSES — push the energy hard:
FOREGROUND (lower 55%): 3 large mascots side by side at the start line, each leaning aggressively forward in mid-stride sprint toward camera, one leg lifted high and bent, trailing leg pushing off behind. Bodies tilted at varying diagonal angles, NOT upright. Small dust clouds kick up from each trailing foot. Sweat droplets scatter in curved arcs around them. Mouths open in shouting / hyped expressions.

MIDGROUND (mid 25%): 3 smaller mascots running behind the front row with subtle motion blur and softer outlines, suggesting a much larger crowd.

MOTION GRAPHICS: dynamic thin black speed lines radiate outward from behind the foreground mascots toward the edges of the canvas. Light wind streaks cross the scene horizontally. Slight motion-blur trail behind each foreground mascot.

CAMERA: low angle looking up at the runners — heroic perspective, exaggerated forward thrust.

BACKGROUND (upper 20%): stylized Shanghai Bund skyline silhouette in deep navy — Oriental Pearl TV Tower (left), Lujiazui supertall trio of Shanghai Tower, World Financial Center, Jin Mao Tower (right). A clean black race start arch frames the runners. The bold sans-serif word "HYROX" sits on the top center of the arch — this is the ONLY in-image HYROX wordmark anywhere in the composition.

BACKGROUND COLOR: warm cream and off-white sky with very soft pink horizon glow.

TEXT OVERLAY (only two text blocks total, beyond the arch wordmark):
- Top headline (massive bold Chinese sans-serif, deep red with thick black outline, slightly tilted for energy): 「又过了一年，HYROX 他更赚钱吗」
- Subline below headline (medium black Chinese sans-serif, NO HYROX text in this line): 「上海站 5.16 倒数 15 天」

NO other HYROX wordmark anywhere else. No bottom-corner logo. No banner repeating HYROX. No subtitle saying HYROX. The arch is the sole repeat.

STYLE: high-energy race-start action poster, cute mascot illustration with explosive composition, sport-event poster polish. No clutter. No neon yellow background. No photorealistic elements.

--ar 3:4 --stylize 250
```

---

## 走法 B — 8 站关卡图（知识感强）

### Story Atoms
- 主角：8 个小红薯，各自做一个 Hyrox 标志动作
- 动作瞬间：跑 / 推橇 / 拉橇 / burpee broad jump / 划船 / sandbag / wall ball / kettlebell
- 情绪：闯关 / 通关感
- 卖点：一图说清 Hyrox 是什么 + 终点是上海

### Final Prompt B

```text
Hyrox 8-station race-day map poster with 小红薯-style chibi mascots, 3:4 vertical layout.

CHARACTER LOCK (same across all 8 mascots): round strawberry-shaped peachy-beige body, single green stem leaf on top, thick black outline, dot eyes, round pink blush cheeks, simple curved mouth, red short-sleeve T-shirt covering torso, bare arms and short stubby legs, chibi proportions.

LAYOUT: a winding curving dotted-line race track threads from top-left to bottom-right of the canvas through 8 numbered stations, each station hosts 1 mascot performing one signature Hyrox movement.

STATION 1 (top-left): mascot running with sweat droplets
STATION 2: mascot in deep front lunge pushing a black sled forward
STATION 3: mascot hauling a black sled backward by rope, leaning back
STATION 4: mascot mid-air in a burpee broad jump
STATION 5: mascot rowing on a black ergometer machine, leaning back
STATION 6: mascot squatting with a black sandbag on one shoulder
STATION 7: mascot raising a black kettlebell overhead with both arms
STATION 8 (bottom-right, finish line): mascot crossing finish line with both arms raised, wearing a red finisher medal on red ribbon

Each station has a small black-circle number badge (1 through 8) next to the mascot.

BACKGROUND: clean cream off-white background with very subtle dotted grid texture. Bottom 15%: small Shanghai Bund silhouette in deep navy as the finish-line backdrop, Oriental Pearl TV Tower clearly visible.

TEXT OVERLAY:
- Top headline (massive bold Chinese sans-serif, deep red with black outline): 「8站走完 = HYROX」
- Subline (medium black Chinese sans-serif): 「上海站 5.16 你能撑到第几站?」
- Bottom-right corner: small black wordmark "HYROX SHANGHAI 5.16"

STYLE: race-day station map illustrated as a cute mascot infographic poster, knowledge-graphic feel, clean composition, no neon yellow background, no photorealistic elements.

--ar 3:4 --stylize 250
```

---

## 走法 C — 官方海报致敬（hero + 群像，最像 Hyrox 官方）

### Story Atoms
- 主角：1 个大 hero 小红薯做最帅的推橇动作 + 6 个小一号小红薯散点围绕
- 动作瞬间：hero 弓步推黑橇正对镜头，周围 6 个做其他 station 动作
- 情绪：单英雄聚焦 + 群体陪衬，海报感最强
- 卖点：最像 Hyrox 官方比赛海报构图

### Final Prompt C

```text
Hyrox official-style race poster featuring one hero mascot surrounded by smaller station mascots, 3:4 vertical layout, 小红薯-style chibi illustration.

CHARACTER LOCK (apply to hero and all 6 surrounding mascots): round strawberry-shaped peachy-beige body, single green stem leaf on top of head, thick black outline, dot eyes, round pink blush cheeks, simple curved mouth, red short-sleeve T-shirt covering torso, bare arms and bare short stubby legs.

HERO (center, occupying ~50% of canvas height): 1 large mascot in a deep front-facing lunge pushing a heavy black sled forward toward camera, intense focused determined expression, sweat droplets flying, clearly the biggest figure on canvas.

SURROUNDING HALO (6 smaller mascots at ~30% of hero size, balanced around the hero, none overlapping the hero):
- Top-left: mascot mid-stride running
- Top-right: mascot raising a black kettlebell overhead with both arms
- Mid-left: mascot rowing on a black ergometer
- Mid-right: mascot throwing a black wall ball upward
- Bottom-left: mascot mid-air burpee broad jump
- Bottom-right: mascot squatting with black sandbag on shoulder

BACKGROUND: warm cream off-white background with a soft red radial gradient glow behind the hero (like a spotlight). Bottom 25%: Shanghai Bund skyline silhouette in deep navy — Oriental Pearl TV Tower, Shanghai Tower, World Financial Center, Jin Mao Tower.

TEXT OVERLAY:
- Top thin banner (black bold Chinese sans-serif on cream): 「100万人 已报名」
- Center title behind/around hero head height (massive bold Chinese sans-serif, deep red with thick black outline): 「HYROX 上海」
- Bottom date strip (large black bold sans-serif): 「2026.05.16 · 倒数 15 天」
- Bottom-right corner: small black wordmark "HYROX"

STYLE: official Hyrox brand event poster polish translated to chibi mascot illustration, cinematic race poster composition, clean and uncluttered. No neon yellow background. No photorealistic elements.

--ar 3:4 --stylize 250
```

---

## 走法 D — 终点冲线（情绪反差 — 不是备赛紧迫，是完赛喜悦）

### Story Atoms
- 主角：4 个小红薯一起冲过 HYROX 终点线 + 3 个已完赛在后
- 动作瞬间：4 种不同冲线姿（双手举 / 跨步 / 指天 / 跪地笑），所有人挂红色完赛奖牌
- 情绪：完赛喜悦 + 上海地标
- 卖点：钩老粉 "上次没跑这次跑" 的逆向情绪驱动

### Final Prompt D

```text
Race finish-line celebration scene with 小红薯-style chibi mascots crossing a Hyrox finish line in front of Shanghai Bund, 3:4 vertical poster layout.

CHARACTER LOCK (apply to all mascots): round strawberry-shaped peachy-beige body, single green stem leaf on top of head, thick black outline, dot eyes, round pink blush cheeks, simple curved mouth, red short-sleeve T-shirt covering torso, bare arms and bare short stubby legs.

FOREGROUND (lower 50%): 4 mascots crossing a black HYROX finish-line ribbon together at the same moment, each in a different finishing pose:
- Leftmost: arms raised triumphantly overhead, mouth wide-open shouting in joy
- Second from left: mid-stride lunging across the line, leaning forward
- Second from right: pointing one finger to the sky, eyes closed smiling
- Rightmost: collapsing onto knees but smiling, arms slightly back

All 4 mascots wear a round red finisher medal on a red ribbon around their necks. Sweat droplets, joyful and exhausted expressions.

MIDGROUND: 3 smaller mascots already past the finish line, hugging each other or sitting on the ground holding their medals up to the sky.

BACKGROUND (upper 35%): stylized Shanghai Bund skyline silhouette in deep navy — Oriental Pearl TV Tower, Lujiazui supertall trio. Sky is warm sunset gradient from soft pink at horizon to cream at top. A black HYROX finish arch frames the top of the canvas, with red and black confetti / streamers falling (no yellow).

TEXT OVERLAY:
- Top headline (massive bold Chinese sans-serif, deep red with thick black outline): 「5.16 终点见」
- Subline (medium black Chinese sans-serif): 「HYROX 上海 · 100万人陪你跑完」
- Bottom-right corner: small black wordmark "HYROX SHANGHAI"

STYLE: race finish-line celebration poster in chibi mascot illustration, emotional triumphant tone, clean composition. No neon yellow background. No photorealistic elements.

--ar 3:4 --stylize 250
```

---

## 推荐挑选顺序
1. 先看 **C**（最像 Hyrox 官方海报，hero + 群像兼得）
2. 如果 C 觉得太挤，落 **A**（起跑线最干净）
3. 如果想做"涨知识"型，落 **B**（8 站关卡图）
4. 如果想换情绪到完赛喜悦，落 **D**（终点线）

## 不要动什么
- 小红薯原型四件套（peachy 圆豆身 / 头顶绿叶 / 红短袖 T / 厚黑描边）— 4 个变体的视觉锚
- 暖白 / 米色底 — **黑底霓虹黄是上一版翻车的来源**
- 红色 + 黑色道具配色 — 不要黄色道具

## 如果还想再多试
- hero 动作可以从推橇换成跳箱 / 壶铃过头 / sandbag squat 看哪个最帅
- 上海地标可以从外滩换成外白渡桥 / 南浦大桥（更有识别度）
- 文字 hook 可以 A/B：「100万人」「营收 15 亿」「8 站 → 100+ 站」三选一

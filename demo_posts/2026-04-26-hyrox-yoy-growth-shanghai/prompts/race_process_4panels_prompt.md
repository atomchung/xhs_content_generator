# Hyrox 续集 后续图 prompt — 4 格漫画 × 3 阶段（小红薯 mascot 风）

## 推荐风格
- 风格：维持 cover 走法 A v2 的小红薯 mascot 原型
- 为什么这样切：cover 问商业问题（"更赚钱吗"），后续图用赛事 4 格漫画给体感反差 — "钱"叙事 + "苦/爽"叙事双钩
- 这组图最该卖什么：赛事过程的真实体感（备赛苦 / 比赛日狼狈 / 完赛爽），让没跑过的人觉得 "我也想试"

## 共用风格锁（3 张图都不动）

角色四件套：
- 圆豆草莓形 peachy-beige 身体 + 头顶绿色叶子
- 厚一致黑描边，flat cel-shaded
- 点状黑眼 + 圆形粉色腮红 + 弧线嘴（按格子情绪变化）
- 红色短袖 T 恤 + 裸臂 + 短粗腿
- chibi 头身比 1:1

格子结构：
- 2 × 2 共 4 格，每格之间薄黑分隔线
- 每格内单独的暖白 / 米色底
- 每格底部一行小黑字 caption（中文，阿里巴巴普惠体 Bold）
- 每格构图遵循 "一物一动作"（参考用户提供的 LET'S HYROX 四格样本）

道具与配色：
- 黑色道具（铁橇 / 壶铃 / 划船机 / sandbag）+ 红色 T / 红色奖牌
- **禁止霓虹黄底、禁止黑底**

必含：`--ar 3:4 --stylize 250`

---

## Page A — 备赛 4 格（"报名一时爽，备赛火葬场"）

### Story Atoms
- 卖什么：报名容易，备赛是真活
- 4 格情绪曲线：兴奋 → 痛苦 → 心痛（钱包） → 焦虑（失眠）
- 适合贴在正文 "为什么参赛人数能涨这么多" 段后面，证明流量是真金白银砸出来的

### Final Prompt A

```text
4-panel comic strip with chibi 小红薯-style mascots showing pre-race preparation, 3:4 vertical layout, 2 rows by 2 columns with thin black borders between panels.

CHARACTER LOCK (apply to mascot in every panel):
- Round strawberry-shaped peachy-beige body
- Single green stem leaf on top of head
- Thick consistent black outline, flat cel-shaded illustration
- Simple dot eyes, round pink blush cheeks, expression-varied mouth
- Red short-sleeve T-shirt covering torso, bare arms and bare short stubby legs
- Cute chibi proportions, head-to-body ratio about 1:1

PANEL 1 (top-left) — 报名:
Mascot sitting at a laptop on a small desk, finger pressing the enter key, screen displays "HYROX SHANGHAI 5.16 REGISTER". Sparkly excited eyes, big open smile, a small "+1" floats up beside the screen. Bottom caption (small bold black Chinese sans-serif): 「报名一时爽」

PANEL 2 (top-right) — 训练房:
Mascot in a deep front lunge pushing a heavy black sled, sweat droplets flying in arcs, mouth open shouting, motion lines radiating outward. Background hints at a gym (small dumbbell silhouette). Caption: 「训练火葬场」

PANEL 3 (bottom-left) — 买装备:
Mascot standing happily holding up a pair of running shoes in one hand, shopping bags of black athletic gear at feet, cash bills with ¥ marks flying out of an open red wallet on the ground. Big grin but slightly worried eyes. Caption: 「钱包瘦三圈」

PANEL 4 (bottom-right) — 失眠倒数:
Mascot lying flat in a small bed at night, eyes wide open, dark window behind, a wall calendar above the bed shows "5.16" circled in red. Single sweat drop on forehead. Caption: 「夜里数到天亮」

PANEL BACKGROUNDS: each panel has its own warm cream / off-white background. Thin black border separates panels.

STYLE: 4-panel comic strip in 小红薯-style chibi mascot illustration, race-preparation montage with comedic emotional swings, kid-book friendly comic strip tone. No neon yellow background. No photorealistic elements.

--ar 3:4 --stylize 250
```

---

## Page B — 比赛日 4 格（8 站里最痛苦的 4 个）

### Story Atoms
- 卖什么：Hyrox 不是马拉松，是 8 个力量站点 + 跑，每一站都让你怀疑人生
- 4 格选最有辨识度 + 最能让小白 "啊原来是这样" 的 4 个动作：推橇 / 划船 / sandbag / burpee broad jump
- 适合贴在正文 "为什么 Hyrox 能从健身房圈出 100 万人" 段后面 — 给小白一图看懂这运动是什么

### Final Prompt B

```text
4-panel comic strip with chibi 小红薯-style mascots showing 4 of the toughest Hyrox race-day stations, 3:4 vertical layout, 2 rows by 2 columns with thin black borders.

CHARACTER LOCK (same mascot in every panel): round strawberry-shaped peachy-beige body, single green stem leaf on top, thick black outline, dot eyes, round pink blush cheeks, expression-varied mouth, red short-sleeve T-shirt, bare arms and short stubby legs, chibi proportions.

PANEL 1 (top-left) — 推橇地狱:
Mascot in deep front lunge pushing a heavy black sled forward, face strained with gritted teeth, sweat droplets flying, motion lines behind sled showing it just barely moving. Caption (bottom, small bold black Chinese sans-serif): 「推到怀疑人生」

PANEL 2 (top-right) — 划船机:
Mascot seated on a black rowing ergometer, leaning aggressively back, legs extended, both arms pulling the handle to chest, exhausted face with tongue slightly out, sweat droplets. Caption: 「划船比上班累」

PANEL 3 (bottom-left) — Sandbag 蹲:
Mascot squatting with a heavy black sandbag draped over one shoulder, knees bent deep, shaky wobble lines around legs, exhausted but determined face. Caption: 「Sandbag 是亲戚」

PANEL 4 (bottom-right) — Burpee broad jump:
Mascot mid-air in a burpee broad jump, body arched forward, both arms thrown forward, mouth wide open shouting, small dust cloud at takeoff point on the ground below. Caption: 「Burpee 跳到飞起」

PANEL BACKGROUNDS: each panel warm cream / off-white background, thin black border between panels.

STYLE: 4-panel comic strip in 小红薯-style chibi mascot illustration, race-day station suffering montage with comedic exaggeration, kid-book friendly. No neon yellow background. No photorealistic elements.

--ar 3:4 --stylize 250
```

---

## Page C — 完赛 4 格（"为奖牌活该")

### Story Atoms
- 卖什么：完赛瞬间的情绪曲线 — 撞线爆喜 → 收奖牌珍贵 → 拍照炫耀 → 累瘫
- 4 格情绪曲线：狂喜 → 感动 → 得意 → 累倒
- 适合贴在正文 "为什么明知道苦还要报" 段后面 — 完赛体感是商业模式的底层燃料

### Final Prompt C

```text
4-panel comic strip with chibi 小红薯-style mascots showing the finish-line celebration sequence, 3:4 vertical layout, 2 rows by 2 columns with thin black borders.

CHARACTER LOCK (same mascot in every panel): round strawberry-shaped peachy-beige body, single green stem leaf on top, thick black outline, dot eyes, round pink blush cheeks, expression-varied mouth, red short-sleeve T-shirt, bare arms and short stubby legs.

PANEL 1 (top-left) — 撞线:
Mascot crossing a black finish-line ribbon at full sprint, both arms raised triumphantly overhead, mouth wide open shouting in joy, sweat droplets, motion lines from behind suggesting full speed. Caption (small bold black Chinese sans-serif): 「冲过那条线」

PANEL 2 (top-right) — 收奖牌:
Mascot bending forward slightly to receive a round red finisher medal on a red ribbon, a hand enters from off-frame placing the medal around the neck. Sparkly grateful eyes, soft smile, single emotion tear droplet at corner of eye. Caption: 「奖牌 = 命换的」

PANEL 3 (bottom-left) — 拍照炫耀:
Mascot striking a flexed-bicep pose with one arm, holding the red medal up to the camera with the other hand, huge grin and proud closed eyes, a small camera "click" mark beside. Caption: 「朋友圈九宫格」

PANEL 4 (bottom-right) — 瘫倒:
Mascot lying flat on its back on the ground, eyes drawn as small "x x" closed-exhausted marks, tongue slightly out, the red medal still resting on its chest, "z Z z" sleep marks floating up. Caption: 「然后睡三天」

PANEL BACKGROUNDS: each panel warm cream / off-white background, thin black border between panels.

STYLE: 4-panel comic strip in 小红薯-style chibi mascot illustration, finish-line emotional arc from triumph to exhaustion, kid-book friendly comic strip. No neon yellow background. No photorealistic elements.

--ar 3:4 --stylize 250
```

---

## 推荐贴文顺序
1. 图 1：cover 走法 A v2（起跑爆冲 + 商业拷问标题）
2. 图 2：Page A（备赛 4 格 — 报名爽 / 训练苦 / 钱包瘦 / 失眠数）
3. 图 3：Page B（比赛日 4 格 — 推橇 / 划船 / sandbag / burpee）
4. 图 4：Page C（完赛 4 格 — 撞线 / 奖牌 / 拍照 / 瘫倒）

正文叙事可以这样搭：
- cover 抛"更赚钱吗"
- Page A 答"流量是真金白银砸出来的"（备赛 = 装备 + 课时 + 时间）
- Page B 答"运动本身够硬"（8 站不是健身房日常）
- Page C 答"情绪燃料够强"（明知道苦还要报）

## 不要动什么
- 小红薯原型四件套（peachy 圆豆 / 绿叶 / 红 T / 厚黑描边）
- 暖白 / 米色底，每格独立背景
- 黑色道具 + 红色 T / 红色奖牌
- 每格 caption 一行 5-7 字最易读

## 如果还想再多改
- caption 文案可以再往 "梗化" 推（"我命由橇不由我" / "Sandbag 是前世债主"），目前是平稳网感
- 如果想压缩成 1 张图带完整故事，可把 12 格做成 3×4 或 4×3 大格漫画

# Sports Illustration Styles Exploration

来源：Xiaohongshu / Instagram 运动插画帐号
目的：探索现有风格包未覆盖的插画风格，评估是否值得纳入 style-profiles

---

## 第一轮测试结论

- Style A（Watercolor Ink Sketch）：**生成效果好**，保留并作为后续探索的锚点
- Style B（Dynamic Comic Art）：背景不够干净、缺乏速度感，v2 修正
- Style C（Anime Crossover）：**放弃**，不是画法风格而是概念风格，不适合标准化

成功要素提炼（Style A 为什么好）：
- 人物和背景用两种完全不同的渲染方式，形成天然层次
- 背景极度简洁——只有颜色，没有具体物件
- 手绘质感而非数字感
- 构图留白多，一眼看懂

---

## Style A — Watercolor Ink Sketch（水墨水彩速写）

状态：**v1 通过**

### 风格描述

人物用黑白墨线精细刻画（线描 + 交叉排线），背景用松散的水彩色块渲染。
两层的对比是核心视觉张力：精确的灰阶人物 vs. 流动的彩色水彩背景。

关键特征：
- 人物：黑白灰墨线，有笔触感，线条干净但不死板
- 背景：柔和粉彩水彩渐晕（薄荷绿、粉、桃、鹅黄）
- 人物不上彩色，靠墨线自身完成光影
- 背景不画具体物件，只有颜色和晕染
- 整体像运动杂志编辑插画或高级速写本
- 构图简洁，一人一球，留白多

### 适合场景

- 人物特写、运动员介绍
- 调性更文艺、更"手作感"的首图
- 球星故事、个人成长类

### Prompt

```text
Black-and-white ink illustration of a tall basketball player in a Spurs jersey, dribbling low with one hand, confident forward-leaning stance, rendered entirely in grayscale ink with visible cross-hatching and sketch-like line work. Background is loose abstract watercolor washes in soft pastel tones — mint green, blush pink, warm peach, and pale yellow — bleeding into each other with no hard edges. The figure is precise and detailed while the background is painterly and fluid. Sports editorial illustration feel, strong contrast between monochrome subject and colorful wash background, vertical 3:4 composition, generous negative space, no readable text, no logos, no watermarks.
```

---

## Style B — Dynamic Comic Art（动态漫画插画）

状态：**v2 修正** — v1 问题：背景太满、缺速度感

### v1 → v2 改动

- 背景从暗色渐变改为干净纯色 / 极简抽象，学 Style A 的"背景只有颜色"
- 加入明确的速度线、动作残影、风压变形
- 减少双人构图的复杂度，聚焦单人爆发动作
- 强调漫画里的"速度帧"而非"合照海报"

### 风格描述

美式运动漫画的速度帧——一个球员在全速冲刺或爆发瞬间，整个画面都在为速度服务。
背景极简干净，所有能量集中在人物的动作线和身体变形上。

关键特征：
- 人物：略微夸张的比例，动态变形（拉伸的四肢、模糊的手脚）
- 速度线：密集、有方向性，从人物身后向外放射
- 动作残影 / motion ghost：人物轮廓的半透明重影
- 背景：纯色或极简色块，不画具体场景
- 粗线条、高对比、饱和色彩
- 整体像漫画里翻到高潮页的单帧

### 适合场景

- 球星高光时刻（绝杀、暴扣、突破）
- 需要"炸裂感"的首图
- 赛季预告、季后赛氛围

### Prompt

```text
Bold comic-book speed frame of a basketball player in a dark Spurs jersey exploding forward in a full-speed crossover dribble, body stretched and leaning hard, one arm extended with the ball, exaggerated dynamic proportions showing raw athletic power. Dense parallel speed lines radiating behind the figure, subtle motion ghost afterimages trailing the arms and legs. Background is a clean flat warm color field with no objects, no arena, no scenery — only the speed lines break the emptiness. Thick confident ink outlines, high contrast, saturated bold colors, the entire composition screams velocity and explosive energy. Comic-book action frame aesthetic, vertical 3:4 composition, no readable text, no logos, no watermarks.
```

---

## Style D — Ink Wash Silhouette（水墨剪影）

状态：新探索

### 风格描述

从 Style A 的墨线继续往东方美学推进。不画细节线条，而是用浓淡不一的水墨块面直接塑造人物剪影。
像中国传统水墨画和运动摄影的结合——墨色浓淡即是光影。

关键特征：
- 人物：不用线描，用墨色浓淡直接渲染体块和剪影
- 墨分五色：焦、浓、重、淡、清，靠墨色本身完成层次
- 飞白 / 枯笔效果：速度感来自笔触的断裂和飞溅
- 背景：留白或极淡墨渍，大面积空白
- 可加极少量彩色点缀（一抹红、一点金）提升视觉焦点
- 整体像水墨画展里的运动主题作品

### 适合场景

- 高级感、东方美学调性
- 球星退役 / 致敬 / 生涯回顾类内容
- 差异化封面（和市面主流风格拉开距离）

### Prompt

```text
Traditional ink wash painting of a basketball player mid-jump shot, rendered as a bold sumi-e silhouette using varying ink densities — deep black for the torso and arms, lighter gray washes for the legs and motion trail. No line drawing, only ink wash blocks and splashes forming the figure. Flying-white dry brush strokes at the edges of the limbs to convey explosive speed. Vast white negative space as background with only a few pale ink mist spots. One small accent of vermillion red on the basketball as the single color element. East Asian ink painting meets sports photography, calligraphic brush energy, vertical 3:4 composition, generous breathing room, no readable text, no logos, no watermarks.
```

---

## Style E — Risograph Duotone（双色印刷风）

状态：新探索

### 风格描述

模拟 Risograph 双色叠印效果——整张图只用两个颜色叠加，天然干净。
颗粒质感 + 错位套色产生独特的复古现代感。是当下独立杂志和设计社群非常流行的视觉语言。

关键特征：
- 只有两种颜色（如：深蓝 + 荧光橙，或酒红 + 金色）
- 两色叠加处产生第三色
- 明显的印刷颗粒 / grain 质感
- 轻微的套色错位（misregistration），像手工丝网印刷
- 构图简洁大胆，人物作为图形元素存在
- 整体像独立体育杂志封面或限量版海报

### 适合场景

- 设计感强的封面
- 数据型帖子的辅助插画（比 Minimal Data Poster 更有温度）
- 系列帖子统一视觉（换两个颜色即可变体）
- 适合批量出图保持一致性

### Prompt

```text
Risograph-style duotone illustration of a basketball player in a powerful defensive stance, low center of gravity, arms wide, intense focus. Rendered in only two ink colors — deep navy blue and fluorescent orange — overlapping to create a third brownish tone where they mix. Visible print grain texture across the entire image, slight color misregistration offset between the two layers giving a handmade screen-print feel. The figure is bold and graphic, simplified into strong shapes rather than detailed anatomy. Background is a clean single-tone field with minimal geometric elements. Retro-modern independent magazine cover aesthetic, vertical 3:4 composition, no readable text, no logos, no watermarks.
```

---

## Style F — Gouache Editorial（不透明水彩编辑插画）

状态：新探索

### 风格描述

扁平不透明水彩（gouache）质感，色块清晰但能看到笔触。
像 The New Yorker 封面或 Monocle 杂志插画——现代、干净、有设计感但保留手绘温度。

关键特征：
- 扁平色块，不做渐变，颜色边界清晰
- 可见的笔刷纹理，但不凌乱
- 有限色板（4-6 色），每张图有统一的色彩情绪
- 人物略微风格化（简化五官、几何化身体）
- 背景是纯色或简单几何分割
- 整体像高端杂志约稿的编辑插画

### 适合场景

- 球星人物介绍、赛季总结
- 调性成熟、有品味感的首图
- 多张图保持系列感（统一色板即可）
- 适合女性向或综合型体育帐号

### Prompt

```text
Gouache editorial illustration of a basketball player walking forward with quiet confidence, ball tucked under one arm, casual post-game energy. Painted in flat opaque color blocks with visible brush texture — teal jersey, warm brown skin tones, dusty pink background. Limited palette of 5 colors maximum, no gradients, clean color boundaries with slight painterly edges. The figure is gently stylized with simplified facial features and slightly elongated proportions. Background is a single flat color with one subtle geometric division. Modern editorial illustration style like a high-end magazine cover, sophisticated and warm, vertical 3:4 composition, no readable text, no logos, no watermarks.
```

---

## Style G — Stencil Poster（模板海报）

状态：新探索

### 风格描述

像街头艺术或限量版丝网印刷海报——人物被简化成高对比的模板剪影，
只保留最关键的轮廓和动作剪影，用极少的色彩层次完成整张图。

关键特征：
- 人物简化为 2-3 层的模板剪影（黑 + 一个主色 + 白高光）
- 没有线条，纯靠色块裁切形成轮廓
- 极高对比度，像照片做了 posterize 再手工裁切
- 背景纯色或简单放射线
- 喷溅 / 纸张质感增加手工感
- 整体像 Shepard Fairey / Obey 风格的运动海报

### 适合场景

- 强态度、强立场的封面（MVP、冠军、历史纪录）
- 需要"一眼记住"的图标级封面
- 球星个人 brand 感
- 适合大字标题叠加

### Prompt

```text
High-contrast stencil poster of a basketball player raising one fist in victory celebration, reduced to a bold three-layer cutout — deep black shadows, a single vibrant red mid-tone, and stark white highlights. No drawn lines, only sharp shape boundaries between the three tonal layers, like a hand-cut screen print. The figure is a powerful simplified silhouette with just enough detail to read the pose and emotion. Background is a clean flat cream color with subtle paper texture and faint spray-paint overspray at the edges. Street art meets sports iconography, propaganda poster energy, vertical 3:4 composition, no readable text, no logos, no watermarks.
```

---

## 风格矩阵总结

| 风格 | 核心视觉 | 背景策略 | 手感 | 适合调性 |
|---|---|---|---|---|
| A. Watercolor Ink Sketch | 墨线人物 + 水彩背景 | 水彩色块，无物件 | 速写本 | 文艺、故事 |
| B. Dynamic Comic Art v2 | 漫画速度帧 + 速度线 | 纯色，无场景 | 漫画 | 热血、高光 |
| D. Ink Wash Silhouette | 水墨块面剪影 | 留白 | 书法 | 高级、致敬 |
| E. Risograph Duotone | 双色叠印 + 颗粒 | 单色底 | 印刷 | 设计、系列 |
| F. Gouache Editorial | 扁平色块 + 笔触 | 纯色几何 | 杂志 | 成熟、品味 |
| G. Stencil Poster | 三层模板剪影 | 纯色 + 纸质感 | 海报 | 态度、图标 |

共同原则（从 Style A 的成功提炼）：
1. 背景必须干净——只有颜色 / 留白 / 极简图形，不画具体场景
2. 人物和背景用不同渲染方式，形成天然分层
3. 保留手工 / 物理媒介质感，不追求数字完美
4. 构图留白多，一眼看懂主角动作

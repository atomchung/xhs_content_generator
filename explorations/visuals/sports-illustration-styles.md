# Sports Illustration Styles Exploration

来源：Xiaohongshu / Instagram 运动插画帐号
目的：探索现有风格包未覆盖的插画风格，评估是否值得纳入 style-profiles

---

## 测试结论

| 风格 | 状态 | 说明 |
|---|---|---|
| A. Watercolor Ink Sketch | **保留** | 生成效果好，作为主推新风格 |
| B. Dynamic Comic Art | 放弃 | v1 背景太满，v2 残影太花 |
| C. Anime Crossover | 放弃 | 概念风格，不适合标准化 |
| D. Ink Wash Silhouette | **备选** | 待测试 |
| E. Risograph Duotone | **备选** | 待测试 |
| F. Gouache Editorial | 放弃 | — |
| G. Stencil Poster | 放弃 | — |

成功要素提炼（Style A 为什么好）：
1. 人物和背景用两种完全不同的渲染方式，形成天然层次
2. 背景极度简洁——只有颜色，没有具体物件
3. 手绘质感而非数字感
4. 构图留白多，一眼看懂

---

## Style A — Watercolor Ink Sketch（水墨水彩速写）

状态：**保留 — 生成效果通过**

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

## Style D — Ink Wash Silhouette（水墨剪影）

状态：**备选 — 待测试**

### 风格描述

从 Style A 的墨线继续往东方美学推进。不画细节线条，而是用浓淡不一的水墨块面直接塑造人物剪影。
墨色浓淡即是光影，飞白枯笔即是速度。

关键特征：
- 人物：不用线描，用墨色浓淡直接渲染体块和剪影
- 墨分五色：焦、浓、重、淡、清，靠墨色本身完成层次
- 飞白 / 枯笔效果：速度感来自笔触的断裂和飞溅
- 背景：留白或极淡墨渍，大面积空白
- 可加极少量彩色点缀（一抹红、一点金）提升视觉焦点

### 适合场景

- 高级感、东方美学调性
- 球星退役 / 致敬 / 生涯回顾
- 差异化封面

### Prompt

```text
Traditional ink wash painting of a basketball player mid-jump shot, rendered as a bold sumi-e silhouette using varying ink densities — deep black for the torso and arms, lighter gray washes for the legs and motion trail. No line drawing, only ink wash blocks and splashes forming the figure. Flying-white dry brush strokes at the edges of the limbs to convey explosive speed. Vast white negative space as background with only a few pale ink mist spots. One small accent of vermillion red on the basketball as the single color element. East Asian ink painting meets sports photography, calligraphic brush energy, vertical 3:4 composition, generous breathing room, no readable text, no logos, no watermarks.
```

---

## Style E — Risograph Duotone（双色印刷风）

状态：**备选 — 待测试**

### 风格描述

模拟 Risograph 双色叠印效果——整张图只用两个颜色叠加，天然干净。
颗粒质感 + 错位套色产生独特的复古现代感。

关键特征：
- 只有两种颜色（如：深蓝 + 荧光橙，或酒红 + 金色）
- 两色叠加处产生第三色
- 明显的印刷颗粒 / grain 质感
- 轻微的套色错位（misregistration）
- 构图简洁大胆，人物作为图形元素存在

### 适合场景

- 设计感强的封面
- 系列帖子统一视觉（换两个颜色即可变体）
- 数据型帖子的辅助插画

### Prompt

```text
Risograph-style duotone illustration of a basketball player in a powerful defensive stance, low center of gravity, arms wide, intense focus. Rendered in only two ink colors — deep navy blue and fluorescent orange — overlapping to create a third brownish tone where they mix. Visible print grain texture across the entire image, slight color misregistration offset between the two layers giving a handmade screen-print feel. The figure is bold and graphic, simplified into strong shapes rather than detailed anatomy. Background is a clean single-tone field with minimal geometric elements. Retro-modern independent magazine cover aesthetic, vertical 3:4 composition, no readable text, no logos, no watermarks.
```

---

## 如何接入现有风格选择系统

### 现有机制分析

当前选风格是**单轴决策**——只看题目类型：

```
题目类型 → 风格
─────────────────────────
人物主角题 → Game Cinematic / Anime Cover
商业新闻题 → Editorial Collage / Minimal Data Poster
轻松角色化 → Mascot Q
```

代码实现在 `generate_style_duo.py` 的 `recommend_style_ids()`：
用关键词匹配 brief 内容，按题目类型返回风格 ID。

### 新风格带来的问题

A / D / E 三个风格和现有风格的区别不在"题目类型"，而在**调性 / 情绪**：

| 风格 | 题目类型 | 调性 |
|---|---|---|
| Anime Cover | 人物题 | 热血、动作 |
| Game Cinematic | 人物题 | 明星、气场 |
| **Watercolor Ink Sketch** | 人物题 | **文艺、故事** |
| **Ink Wash Silhouette** | 人物题 | **致敬、回顾** |
| Editorial Collage | 商业题 | 信息密度 |
| Minimal Data Poster | 商业题 | 极简结构 |
| **Risograph Duotone** | 人物题 / 商业题 | **设计、系列** |
| Mascot Q | 轻松题 | 可爱、角色化 |

→ 选择逻辑需要变成**双轴决策**：先判断题目类型，再判断调性。

### 建议的双轴选择树

```
第一轴：这张图卖什么？
├── 卖人物
│   ├── 第二轴：调性是什么？
│   │   ├── 热血 / 动作强 / 对峙    → Anime Cover
│   │   ├── 明星气场 / 商业新闻人物  → Game Cinematic
│   │   ├── 文艺 / 故事 / 个人成长   → Watercolor Ink Sketch ← 新
│   │   ├── 致敬 / 退役 / 生涯回顾   → Ink Wash Silhouette ← 新
│   │   └── 不确定                   → Game Cinematic（默认）
│   │
├── 卖结构 / 数据
│   ├── 信息密度高 / 多元素          → Editorial Collage
│   ├── 极简 / 数字为主              → Minimal Data Poster
│   └── 系列感 / 设计统一            → Risograph Duotone ← 新
│   │
├── 卖角色 / 轻松                    → Mascot Q
│
└── 不确定 → 先问：卖人物还是卖结构？
```

### 代码层面需要改的地方

如果确认要接入，需要改 4 个文件：

**1. `generate_style_duo.py` — `STYLE_SPECS`**
新增 3 个 style spec（anchor_prefix / background_prefix / final_prefix / style_suffix / mode）

**2. `generate_style_duo.py` — `recommend_style_ids()`**
新增调性关键词匹配，在现有题目类型匹配之前插入：

```python
# 调性优先匹配（新增）
if has_any(prompt, ["故事", "成长", "介绍", "profile", "文艺", "手绘", "editorial sketch"]):
    return ["watercolor_ink_sketch", "game_cinematic"]
if has_any(prompt, ["致敬", "退役", "生涯", "回顾", "传奇", "legacy", "tribute"]):
    return ["ink_wash_silhouette", "watercolor_ink_sketch"]
if has_any(prompt, ["系列", "series", "统一风格", "duotone", "印刷", "设计感"]):
    return ["risograph_duotone", "editorial_collage"]
```

**3. `references/style-profiles.md`**
新增 3 个风格的 profile 描述（目标 / 适合 / 避免）

**4. `references/style-selection-rules.md`**
从单轴改为双轴决策树

### 风险和注意

- 关键词匹配只是第一层筛选，brief 里不一定有明确的调性词
- 如果 brief 没有调性信号，仍然 fallback 到现有的题目类型匹配
- 新风格的 `mode` 建议：A 和 D 用 `hero`（单人物），E 用 `poster`
- 三个新风格都还没大量实测，先作为备选，在 `recommend_style_ids()` 里权重排低于现有风格

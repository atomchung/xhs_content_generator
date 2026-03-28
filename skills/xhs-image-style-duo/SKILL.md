---
name: xhs-image-style-duo
description: 为已确定要生图的页面输出两种视觉风格候选，并把 prompt 拆成共享骨架、主体锚点、背景层和最终 prompt。用户提到生图、图片 prompt、同一张图换风格、封面画风、图像风格不稳定、人物想换不同视觉方向、背景太乱、动作没张力时，务必使用这个 skill。它负责风格延展，不负责整组图分工，也不负责首图版式模板。
---

# XHS Image Style Duo

这个 skill 只做一件事：

在已经确定要生图的前提下，从多个风格包里给出 `2 个候选方向`。

默认不是固定“两种画风”，而是：

- 先锁住同一张图的共享骨架
- 再挑 `1 个主风格 + 1 个备选风格`
- 最后输出两套可直接继续迭代的 prompt

这个 skill 不负责决定整篇帖子该用真人图、官方截图还是生图。那一步交给 `xhs-visual-asset-mix`。  
如果是图 1 首图，还要先过 `xhs-cover-template`，先锁封面结构和文字安全区。

## 什么时候用

遇到这些任务直接使用：

- 用户要把一个故事做成两种图片风格
- 用户说“同一张图换几种风格看看”
- 用户说“背景太乱”“动作没张力”“不像封面图”
- 用户要更像动漫名场面 / 游戏动画 / 杂志拼贴 / 极简海报 / Q 版
- 用户想优化图片生成顺序，避免背景一改就全部重跑

## 如果画面任务还没锁

- 如果还没决定这张图是不是首图：
  先回到 `xhs-visual-asset-mix`
- 如果是首图，但还没锁封面结构：
  先回到 `xhs-cover-template`
- 如果用户只是想长期探索视觉语言，还没落到某一页：
  优先放进 `explorations/visuals/`

## 先做 5 个判断

1. 这张图是不是首图
- 如果是首图，先确认封面模板已经锁住
- 如果没有，先回到 `xhs-cover-template`

2. 主角是谁
- 必须只有一个绝对主角

3. 这一张图最该卖什么
默认从下面选一个：
- 脸
- 动作
- 冲突
- 情绪
- 信息结构

4. 背景是不是稳定的
- 如果用户明显还在探索背景，先不要把背景写死

5. 这张图更适合哪种风格包
- 热血运动动画
- 欧美游戏动画
- 体育商业杂志拼贴
- 极简数据海报
- Q 版吉祥物

如果读者不懂赛事或规则，画面里也要有足够明确的主角、冲突和信息锚点。  
图上可见文字是否真的需要，也要先判断；真正给用户看的角标和封面词，优先短中文。

## 更好的生成顺序

不要一开始就写“完整终稿 prompt”。按这个顺序做：

### Step 1. 抽故事骨架

先拆成 4 个元素：

- 主角
- 动作瞬间
- 冲突/情绪
- 背景符号

其中前 3 个先锁死，背景符号暂时只记关键词。

### Step 2. 先做人物锚点

先写 `subject anchor prompt`：

- 只画主角
- 只保留很简单的背景
- 重点锁脸、发型、服装、姿势、镜头

这一层的目的：

- 锁住“这个人长什么样”
- 锁住“他在这个故事里最有张力的动作”

### Step 3. 再做背景层

单独写 `background prompt`：

- 不抢主角
- 只承担世界观和冲突说明
- 用 2-3 个背景符号就够

如果背景之后要改，优先只改这层。

### Step 4. 最后合成封面 prompt

把人物锚点和背景层合成成 `final cover prompt`。

如果背景经常变，优先重写：

- `background prompt`
- `final cover prompt`

不要先推翻 `subject anchor prompt`。

## 风格包

这里的 “duo” 指 `两种候选`，不是固定两种画风。

默认从下面的风格包里选 `1 主 + 1 备`：

### A. 热血运动动画封面

- 适合人物主角、情绪冲突、热血动作
- 不是泛二次元，而是海报感更强的运动动画封面

### B. 欧美游戏动画电影感

- 适合巨星、联盟变化、商业新闻人物题
- 更立体、更高级、更像高预算游戏动画 key art

### C. 体育商业杂志拼贴

- 适合转播、薪资、扩军、平台战争
- 用人物、数字、场馆、屏幕、剪报做高密度商业新闻海报

### D. 极简数据海报

- 适合规则、钱、结构变化
- 人物可以弱化，数字和信息结构更重要

### E. Q 版吉祥物

- 适合更轻一点、更可收藏、更偏拟人角色的题
- 不是普通 chibi，而是带运动吉祥物语义的角色化转译

优先级默认是：

- 人物大新闻 -> `欧美游戏动画电影感` / `热血运动动画封面`
- 商业新闻 -> `体育商业杂志拼贴` / `极简数据海报`
- 轻松角色化 -> `Q 版吉祥物`

## 如果要直接生成图片

优先用脚本：

- [scripts/generate_style_duo.py](./scripts/generate_style_duo.py)

这个脚本现在会从风格包里生成两套候选，并且额外输出：

- `story_atoms`
- `subject_anchor_prompt`
- `background_prompt`
- `final_prompt`

用途：

- 先稳定角色和动作
- 再单独试背景
- 最后输出最终封面图

## 存档约定

如果当前已经有贴文目录，默认把风格 prompt 和生成结果写进贴文目录：

- prompt 建议放在 `demo_posts/<date>-<slug>/prompts/<style>/prompts.md`
- 图片建议放在 `demo_posts/<date>-<slug>/images/<style>/`

同一篇贴文的图片实验不要散落到多个无关目录。

## 输出格式

始终按下面结构输出：

```markdown
## Story Atoms
- 主角：
- 动作瞬间：
- 情绪冲突：
- 背景符号：

## Generation Order
1. Subject anchor
2. Background layer
3. Final cover

## Style 1
- 风格摘要：
- 为什么选它：
- subject anchor prompt：
- background prompt：
- final cover prompt：

## Style 2
- 风格摘要：
- 为什么选它：
- subject anchor prompt：
- background prompt：
- final cover prompt：

## 推荐
- 适合首图的是：
- 背景如果要改，优先改哪一层：
```

## 快速参考

- [references/style-profiles.md](./references/style-profiles.md)
何时读：要从风格包里挑主风格和备选风格时。

- [references/style-selection-rules.md](./references/style-selection-rules.md)
何时读：不确定该优先选哪两个风格包时。

- [references/prompt-polish-rules.md](./references/prompt-polish-rules.md)
何时读：用户说背景太乱、动作不够、脸不够像、Q 版不够可爱时。

- [references/output-evaluation.md](./references/output-evaluation.md)
何时读：已经生成了两套风格，但不知道该怎么判断谁更适合继续做时。

## 不要这样做

- 不要先决定画风，再决定这张图要卖什么
- 不要先把背景写得比主角还重要
- 不要把所有题都塞进同一种画风
- 不要让 Q 版只是大头版真人
- 不要在背景还没定时就反复重做角色
- 不要把可见文案默认写成英文大字

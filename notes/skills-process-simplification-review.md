# Skills Process Simplification Review

日期：2026-03-29

## 2026-04-08 补记：为什么这一篇一开始没按 skills 走

触发背景：

- 这次做 `2026-04-07-dodgers-owner-sports-investments`（七亿买下大谷的男人 / Walter）
- 整条 workflow 前半段几乎**完全没调用任何 xhs-* skill**，全靠手写
- 直到用户连续三次具体指责（正文格式混乱、第 X 图混进正文、刻意 wordplay「名下最便宜」），才回头 Read 对应的 `SKILL.md`
- 这一节只记录失误、归因、skill 可能的修改方式，不重写流程

### 这次具体踩到的坑

1. **写 `post.md` 发布正文之前没有 Read `xhs-note-assembly/SKILL.md`**
   - 第一版正文 500+ 字（规范 150–300），7 段而不是 3 段
   - 没有 number shock 开头，没有二选一收口
   - 夹了「道奇是他名下最便宜的一支」这种刻意 wordplay，用户直接定性「不通顺」「刻意」

2. **把「图组分工」和「发布正文」混在同一段里**
   - 第一版 post.md 的发布正文里出现了 `第 1 图 / 第 2 图 / P1 / P2` 字样
   - 用户直接问：「為什麼文字會有第 x 圖？ 圖片和 post 為啥合再一起了」
   - 这是 skill 里从没明文禁过的红线被我当成了暗线来猜

3. **230 亿市值数据研究了但没落盘**
   - 跑了 5 个 WebSearch 拿到 Forbes 2026 估值、Lakers $10B、Cadillac F1 ~$1.2B 等等
   - 数据只活在 chat 里和 TodoWrite 计划里
   - 被系统 reminder 打断一次后就完全没写进 `fact_pack.md` 或 `post.md`
   - 用户问「整合完毕了吗」才发现只是「研究 + 口头规划 + 没真动笔」

4. **封面 prompt 迭代没过 `xhs-cover-template` 自检**
   - 做了 A/B/C/D/E/F/G 七版 cover prompt + 一组 4 帧视频分镜
   - 中间完全没跑过「主角 / 动作 / 冲突 / 背景符号」四项检查
   - 能成立纯粹是因为用户自己在每一版都拍板了方向

5. **Review 被要求时默认只看本地文件**
   - 用户两次说「review 這篇貼文」
   - 第一次我直接读本地 `post.md` 做了一次产品侧评审
   - 用户纠正「文章已經發了，基於線上數據去 review」才想到 `xhs-publish-review` skill 的存在
   - 这个 skill 的 description 里其实写清楚了触发条件，但我**在用户说「review」时完全没主动搜索 skills 目录**

6. **整合数据阶段卡在「规划 → 中断 → 白干」循环**
   - 当时模式：研究 → TodoWrite 计划 → 在 chat 里数字数预排版 → 系统 reminder → 没写文件 → 下一轮重来
   - 根因：我花太多时间在「写之前想完美」，没先把草稿直接 Edit 进文件

### 为什么一开始就没按 skills 走（归因）

**A. skills 不是自动触发的，我需要主动识别**

- Claude Code 里 skill 生效靠两条路径：用户显式 `/skill-name` 或我自己 Read `SKILL.md`
- 看到「接下来产生 post.md」这类任务，我的默认反射是「直接写」，不是「先 Read 规范」
- 这不是 skill 写得不好，是**触发语义在我这边太弱**

**B. `scaffold_post_folder.py` 产出的 `post.md` 是空文件**

- scaffold 只建好目录结构，`post.md` 内部是空的
- 没有骨架 section（「标题」「发布正文」「图组分工」「自检」），所以我直接在空白上即兴发挥
- 没有顶部 meta 提醒（如「写之前 Read skills/xhs-note-assembly/SKILL.md」）
- 结果第一版的段落数、字数、区块划分全靠我的短期记忆，而我恰好没读过最新的 SKILL.md

**C. `xhs-note-assembly/SKILL.md` 里没有明文「禁区」段落**

- 里面写了推荐格式、字数区间、emoji 数量
- 但**没有明文写「正文里禁止出现 Page / 第 X 图 / P1-P8 / 图组标签」**
- 导致我把工作稿的 per-page 备注留在了正文里
- 也没写「发布正文」和「图组分工」必须是两个物理上分开的 section

**D. `xhs-fact-pack/SKILL.md` 没规定「研究数据必须先落盘再被引用」**

- 现在的逻辑隐含「fact_pack 是输入，post 是输出」
- 但没有硬性红线说「WebSearch 结果 → 必须先 Edit 进 fact_pack.md → 再允许在 post.md 里引用」
- 所以 230 亿这组数据一度只活在 chat context 里

**E. `xhs-publish-review/SKILL.md` description 触发词太窄**

- 现在的 description 关键词是「对比真实发帖版本和草稿」「复盘」「归因」
- 用户说「review 這篇貼文」时，我的第一反应是「pre-publish review」而不是「post-publish retrospective」
- 缺一个触发词把「已发布 + review」这个组合硬绑到这个 skill

**F. 我自己的写作工作流有问题**

- 默认习惯：research → chat 里铺长计划 → TodoWrite → 数字数 → Edit
- 前四步都会被系统 reminder / 新指令打断，一旦打断就全白干
- 正确做法应该是：草稿直接 Edit 进文件（哪怕粗），原子 commit，然后再 polish
- 这是流程习惯问题，不是 skill 问题，但 skill 可以帮我更早进入「动手」模式（比如 xhs-note-assembly 的第一条指令就是「把下面 template 贴进 post.md」）

### Skills 可能的修改方式

**1. `xhs-note-assembly/SKILL.md`**

- 在 description 里加触发词：「生成 post.md 发布正文 / 写小红书正文 / 改文案 时必须先读这个 skill」
- 新增 **「绝对禁区」段落**：
  - 发布正文里禁止出现 `Page X / 第 X 图 / P1–P8 / 图组 / 图片 X` 任何一种图位标签
  - 发布正文和图组分工必须是两个 `##` 级别的独立 section，且图组分工的首句必须写「读者看不到这部分，只是工作稿」
- 新增 **「写作前必答」checklist**（写之前必须在脑子里过一遍）：
  - 目标字数？（默认 150–300）
  - 几段？（默认 3）
  - 开头是什么 number shock？（先写出这个数字）
  - 每段 1 个数字是什么？
  - 二选一收口是哪两个？
- 把当前 `post.md` 里的「本版规范自检」那一段正式写进 skill 作为**必须复制**的模板

**2. `scripts/scaffold_post_folder.py`**

- `post.md` 不能再是空文件，必须出生时就带骨架：
  ```
  ## Working Brief
  - One-sentence story:
  - Title direction:
  - 格式说明：发布正文和图组分工是两件事，正文里不要写「第 X 图」
  
  ## 标题
  - 主标：
  - 封面副标：
  - 备用标题：
  
  ## 发布正文（直接复制到小红书）
  > 按 xhs-note-assembly 规范：3 段 / 150–300 字 / number shock 开头 / 二选一收口
  ```text
  [正文]
  ```
  
  ### 本版规范自检
  - [ ] 字数 150–300
  - [ ] 3 段
  - [ ] 每段 1 个数字
  - [ ] number shock 开头
  - [ ] 二选一收口
  - [ ] 禁区检查：无 Page / 第 X 图 / P1–P8
  
  ## 图组分工（读者看不到，是工作稿）
  - **P1 封面**：
  - **P2**：
  ...
  
  ## 来源尾注
  ```
- 顶部加 meta 注释：`<!-- 写正文前必须 Read skills/xhs-note-assembly/SKILL.md -->`
- 这样即使我忘了读 skill，**文件骨架本身就在提醒规范**

**3. `xhs-fact-pack/SKILL.md`**

- 新增红线：**任何 WebSearch / WebFetch 的数据，必须先 Edit 进 `fact_pack.md` 的对应 section，才能被 `post.md` 引用**
- 禁止「查完直接写正文」的 shortcut
- 这样 230 亿这类数据不会再只活在 chat context 里
- 理由：fact_pack 是 single source of truth，post 只是它的一次消费；数据不落盘等于没查

**4. `xhs-publish-review/SKILL.md`**

- description 补触发词：「用户说 `review 这篇 / 复盘 / 总结这篇怎么发的 / 线上版 vs 草稿 / 对比发出去的版本`，只要涉及**已发布**的帖子，都应触发这个 skill」
- 特别点明：**只要用户用了过去式「发了 / 发布了 / 已经发」+ review / 看一下 / 检查**，默认进这个 skill，不要跳去产品侧文字评审
- 并加一条「前置条件」：开始前必须先确认线上内容来源（URL / 截图 / 贴文字），**拿不到就走「截图版复盘」或「单边复盘」**，绝不用本地草稿冒充发布版

**5. `notes/local-filesystem-workflow.md`**

- 在 workflow 入口加一行硬规则：**新开一个 post workspace 后的第一步是 Read `xhs-note-assembly/SKILL.md`，然后才能动 `post.md`**
- 这条规则放在 scaffold 脚本说明的正下方，让它和 scaffold 动作紧邻

**6. 不做的事（避免扩面）**

- **不**新建任何 `.md` 说明文件专门讲这次的坑（这正是这份文件 2026-04-03 补记里定过的原则「不再让每个问题都变成一份新 `.md`」）
- **不**新建 entry-point skill（会和现有 8 个 skill 抢触发空间，反而增加噪音）
- **不**把这次的失误硬写成评分表或 lint 脚本（过度工程，skill 里加几行红线就够了）

### 这次最该先改的 3 件事

1. **`scripts/scaffold_post_folder.py` 的 `post.md` 改成带骨架 + 禁区 + 自检 checklist 的模板**
   — 这一条性价比最高，因为即使 skill 没触发，骨架本身就会强制我走规范
2. **`xhs-note-assembly/SKILL.md` 加「绝对禁区」段落 + description 触发词**
   — 堵住「第 X 图混进正文」和「skill 没主动触发」两个洞
3. **`xhs-publish-review/SKILL.md` description 补「已发布 + review」触发词**
   — 避免下次再把 publish review 做成 pre-publish review

前两条做完，这次的 6 个具体坑里至少 4 个会在下一篇自动消失。



## 2026-04-03 补记

这次调整不是要再发明一层新流程，而是把真实发布复盘里已经验证的问题，回写到现有 skill。

触发背景：

- `2026-04-03-wnba-expansion-player-shuffle` 的发布版最后收敛成：
  `强封面 + 短正文 + 不发弱内页`
- 复盘显示，之前的问题不是信息不够，而是默认 workflow 对“封面检查、发布口语化、内页存在价值”限制不够硬。

这次改动重点：

1. `xhs-cover-template`
   不再只被理解成例外处理器；首图默认先过一次 `主角 / 动作 / 冲突 / 背景符号` 的快速检查。
2. `xhs-note-assembly`
   默认交付 `publish-ready copy`，并在商业题里优先 `结果 / 最大数字 / 最短归因`，不再先把研究稿直接交出去。
3. `xhs-visual-asset-mix`
   新增最小 storyboard gate；内页如果说不清 `任务 / 场面 / 新增信息`，就删页，不要硬做。
4. `xhs-publish-review`
   复盘必须明确指出哪些经验应该回写到现有 `SKILL.md`，而不是继续增生新的流程说明文件。

这次为什么这样改：

- 要把“封面强，不代表内页也该存在”写成硬规则
- 要把“研究成稿”和“发布成稿”分开，但仍然留在同一个 skill 里
- 要减少用户看到的流程分叉，不再让每个问题都变成一份新 `.md`
- 要让 `README -> skill docs -> publish review` 三层形成闭环，而不是各写各的

## 目标

重新审视当前从 `发想题目 -> 切角 -> 事实 -> 成稿 -> 生图` 的整条 skills 流程，找出哪些步骤对用户来说是非必要的，应该简化。

## 当前流程

当前 repo 顶层流程写成：

1. `xhs-topic-angle-shortlist`
2. `xhs-fact-pack`
3. `story_spine.md`
4. `xhs-visual-asset-mix`
5. `xhs-cover-template`
6. `xhs-note-assembly`
7. `xhs-image-style-duo`
8. `xhs-publish-review`

问题不是“这些步骤有没有价值”，而是：

- 它们对内部整理有价值
- 但很多步骤不应该直接暴露给用户
- 也不应该每一篇都完整走一遍

## 必须保留的骨架

真正必要的只有 4 段：

1. 锁一个题
2. 锁一个故事
3. 锁最终帖子和每张图任务
4. 输出可直接使用的生图 prompt

发布后的 `review` 单独算，不属于产出时的必经步骤。

## 非必要点与简化建议

### 一、选题阶段

#### 非必要点 1：默认每次都输出 3 到 5 个角度

问题：
- 这适合“我没题，帮我想几个”。
- 不适合“我已经知道想做什么，只需要你帮我锁方向”。

应该简化：
- 如果用户已经给出明确题目，就不要强制跑 shortlist。
- 直接进入：
  `一句话切角 + why now + 封面入口`

#### 非必要点 2：角度打分、综合分、多个筛子默认全展示

问题：
- 对内部判断有帮助。
- 对用户常常只是额外信息噪音。

应该简化：
- 默认只给：
  `第一推荐`
  `为什么`
  `不做另外几个的原因`
- 分数和筛子只在你自己内部判断时使用，不默认展示。

### 二、研究阶段

#### 非必要点 3：`research.md`、`fact_pack.md`、`story_spine.md` 三层拆分过细

问题：
- 这对 repo 整理有价值。
- 但对一篇普通帖子来说，容易变成“写三份相近文档”。

应该简化：
- 把它们合并成一个更轻的 `post_brief` 概念：
  - 角度
  - 核心事实
  - 为什么现在值得讲
  - 这篇到底在讲什么
- `story_spine` 继续保留，但更适合作为内部检查项，而不是必须显式多开一份文件给用户理解。

#### 非必要点 4：对简单人物/事件帖也强制完整 fact pack

问题：
- 商业题、争议题、高风险数据题需要 fact pack。
- 但一些简单介绍型或轻知识型帖子，不一定需要完整论证链。

应该简化：
- 只在下面情况强制完整 fact pack：
  - 有争议
  - 有钱/估值/规则
  - 有大量数字
  - 有真假口径风险
- 其他情况只保留 `3-5 条必须知道的事实`。

### 三、正文与图组阶段

#### 非必要点 5：`xhs-visual-asset-mix` 和 `xhs-note-assembly` 分得太开

问题：
- 一个在分图任务，一个在写最终帖子。
- 但对用户来说，通常只是想知道：
  `这篇 4 张图分别干嘛 + 帖子怎么写`

应该简化：
- 默认把图组任务直接并进成稿输出。
- 只有当用户明确在纠结：
  `真人图 vs 截图 vs 生图`
  才单独启用 `xhs-visual-asset-mix`。

#### 非必要点 6：图 1 还要单独经过 `cover-template`

问题：
- 对封面系统沉淀有帮助。
- 但对当前账号已经有固定封面语言时，不应该每次都重新走完整模板。

应该简化：
- 当前账号默认封面结构应该变成系统常识。
- 只有当这篇封面明显偏离默认结构，才单独开 `cover-template`。

### 四、生图阶段

#### 非必要点 7：默认输出两种风格候选

问题：
- `xhs-image-style-duo` 当前默认是两种风格候选。
- 这适合探索，不适合交付。

应该简化：
- 默认只输出 `一个推荐风格 + 一个 final prompt`。
- 只有用户明确说“给我两个风格看看”，才启用 duo 模式。

#### 非必要点 8：把 `story atoms / subject anchor / background prompt / final prompt` 全交给用户

问题：
- 这是内部调图结构，不是用户真正需要的交付。

应该简化：
- 默认只给用户：
  `可直接贴给 Gemini / GPT 的 final prompt`
- 其余分层 prompt 只保留给内部调试，不默认展示。

#### 非必要点 9：生成太多中间文件和目录

问题：
- `style_prompts.md`
- `style_prompts.json`
- `cover_input.txt`
- `cover_template.md`
- `visual_asset_mix.md`
- 各种 style 子目录

这些对内部留档有意义，但对用户是认知负担。

应该简化：
- 用户层默认只接触两类文件：
  - `post.md`
  - `final_prompts.md` 或单个 `.txt`
- 其他都作为内部产物，不需要用户挑选。

#### 非必要点 10：把“过程说明”写进最终 prompt

问题：
- 这是目前最明显的问题。
- prompt 里混入：
  - 参考谁
  - 像哪个贴文
  - 上传图片
  - 工作流解释
  - 为什么这样改

应该简化：
- 最终 prompt 只能保留：
  - 构图
  - 视觉风格
  - 排版
  - 字体要求
  - 负面限制

### 五、人工介入阶段

#### 非必要点 11：每个 skill 都要单独“人类拍板”

问题：
- shortlist 要拍板
- fact pack 要拍板
- asset mix 要拍板
- note assembly 要拍板
- cover 也要拍板

这会把一次创作拆成太多次停顿。

应该简化：
- 整条链路只保留 `1-2 次` 人工拍板：
  1. 题目和切角
  2. 封面和最终成稿

### 六、账号规则阶段

#### 非必要点 12：账号默认规则散落在太多地方

问题：
- README 有一份
- account note 有一份
- skill 里又写一份
- 具体 post workspace 里还会再写一次

应该简化：
- 账号默认规则只保留一个 source of truth。
- skill 里只引用，不再重复展开。

## 建议的新简化流程

### 默认流程

1. `chat 锁题`
   输出：
   - 一句话切角
   - why now
   - 封面入口

2. `chat 锁 brief`
   输出：
   - 3-5 条必须事实
   - 3 段正文结构
   - 4 张图各自任务

3. `chat 出最终帖子`
   输出：
   - 标题
   - 正文
   - 图上文案

4. `chat 出最终生图 prompt`
   输出：
   - 图 1 final prompt
   - 图 3/图 4 final prompt

### 只有在特殊情况才加开的步骤

- `xhs-topic-angle-shortlist`
  只在“用户没题”时开启
- `xhs-fact-pack`
  只在争议/商业/数字风险题时开启
- `xhs-visual-asset-mix`
  只在“真人图还是生图”确实没想清楚时开启
- `xhs-cover-template`
  只在封面明显偏离默认系统时开启
- `xhs-image-style-duo`
  只在用户明确要“两种风格候选”时开启

## 最值得先改的 5 件事

1. 默认不再给用户看中间 prompt 文件
2. 默认只交付 `可直接贴 Gemini 的 final prompt`
3. 把 `story_spine + fact_pack + asset mix` 压缩成一个轻量 brief
4. 把人工拍板次数降到最多两次
5. 把账号默认封面规则改成系统常识，而不是每次重新解释

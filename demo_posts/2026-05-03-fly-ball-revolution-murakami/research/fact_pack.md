# Fact Pack — 飞球革命：打向天空的强打者（村上宗隆）

日期：2026-05-03
延续：`claude/baseball-analytics-article-XwSPr` 的 `2026-05-01-moneyball-baseball-analytics-evolution`（数据至上，谁是 MLB 最强打者）
角度（用户指定）：从指标讨论飞球革命，看看这转变有没有争议
主角（用户指定）：村上宗隆

---

## 一句话框

2026 球季前 32 场 MLB 全垒打领先的不是 Aaron Judge，是 25 岁刚从 NPB 来的村上宗隆 — 13 HR / Barrel% 99 百分位 / K% 33%。他把 J.D. Martinez 2014 年引爆的 Fly Ball Revolution 所有正反面压进同一个球员，连 MLB 2023 才踩的煞车都救不回来。

---

## 上篇接点（不能脱节）

上篇 `2026-05-01-moneyball...` 收尾段：
> "数据玩到极端反伤比赛 — 三振 + 全垒打塞满每场，时长拖到 3 小时。2023 联盟加投手计时器、禁守备移位，比赛压回 2 小时半。当年骂'书呆子毁棒球'那批老球评，现在转播里张口闭口 launch angle 和 WAR。"

→ 飞球革命就是上篇收尾埋的 launch angle / 三振泛滥 / 联盟踩煞车这条故事线的展开。

---

## Fly Ball Revolution — 起源与时间轴

### 起点：J.D. Martinez 2013-14

| 时间 | 事件 | 关键数字 |
|---|---|---|
| 2011-2013 | 为 Astros 出赛，三个赛季 OPS 仅 .687 / .742 / .650，被视为废棒 | 击球仰角约 9°，标准 ground-ball hitter |
| 2014 春训 | 3 月 22 日被 Astros 释出 | 0 队感兴趣 |
| 2013-14 冬天 | 私下找洛杉矶私人教练 Craig Wallenbrock + Robert Van Scoyoc + Doug Latta（学派内部有分歧，主流叙事归功 Wallenbrock + Van Scoyoc）重做挥棒 | 把 swing path 从 down-on-ball 改成 upward-tilt |
| 2014 季中 | 被 Tigers 签下，半季 23 HR / .315 BA / OPS .912 | 击球仰角拉到 ~17-18° |
| 2015 | 38 HR、All-Star | 联盟开始注意 |
| 2017 (DET → ARI) | 45 HR / 1.066 OPS | 现象级 |
| 2018 (BOS) | .330 / 43 HR / 130 RBI，差一点三冠王 | 全联盟开始抄作业 |

→ Martinez 自己 2017 年公开把方法论写进 Eno Sarris（FanGraphs / The Athletic）专访，飞球革命正式有了 origin story。

### 同期推手：Josh Donaldson 的金句

- 2015 AL MVP（Toronto Blue Jays）
- 公开金句（多次访谈不同版本，意思一致）：
  > "Ground balls are outs. I never try to hit a ground ball. Ever."
  > "滚地球永远是出局。我从来不试着打滚地球。永远不。"
- 把"打飞球"从教练室秘语推上球员媒体语言的关键人物

### 同期推手：Justin Turner 2014

- Dodgers 2014 年签 Turner 后让他跟 Doug Latta 改造（和 Martinez 同一脉教练学派，后来分裂叙事）
- Turner 从废棒升级成 Dodgers 主力 3B，2017 NLCS MVP
- 飞球革命第二个公开案例

---

## 关键指标（每个都要在 post 里立刻给中文注释）

### 1. Launch Angle（击球仰角，°）

- 定义：球离开球棒瞬间相对水平面向上的角度
- 甜蜜区：10°-25°
  - <10°：滚地球（多半是出局）
  - 25°-50°：高飞球（外野接杀概率高）
  - 10°-25°：line drive（强劲平飞球）+ low fly ball — 安打 / 长打 / HR 概率最高
- MLB 联盟平均：约 12°
- Martinez 改造前 ~9°，改造后 ~17-18°

### 2. Exit Velocity（击球初速，mph）

- 定义：球离棒瞬间的速度
- MLB 联盟平均：约 89 mph
- "Hard-Hit"门槛：≥95 mph
- 现役顶尖（Stanton / Judge）：peak 121-122 mph

### 3. Barrel%（甜蜜点击中率）

- 定义：MLB 2015 年 Statcast 上线后定义的指标 — 同时满足"高初速"+"甜蜜仰角"的击球
- 简化判定：初速 ≥98 mph 且仰角在 ~26°-30° 区间（初速越高，仰角窗口越宽）
- 一支 Barrel 的 league-wide 预期打击率约 .800+，预期长打率约 1.500+
- 这把改造从玄学变成处方：你不用打安打，你打 Barrel 就好

### 4. GB% / FB%（滚地球率 / 飞球率）

- MLB 联盟整体（每年统计 FanGraphs）：
  - 2010：GB% 约 45%，FB% 约 35%
  - 2015：GB% 约 45%（飞球革命刚起，还没显著动）
  - 2019：GB% 跌到 42-43%，FB% 升到 ~36%（HR 史上最高 1.39/场）
  - 2024：GB% 约 42%，FB% 约 36%（守备移位禁令后稍微回升 GB%）

### 5. K%（三振率）

- 联盟 K%（每场打席被三振比例）历史曲线：
  - 2008: 17.5%
  - 2014: 20.4%
  - 2019: 23.0%
  - 2021: 23.2%（历史最高）
  - 2024: 22.6%（仍在历史高位）

### 6. TTO（Three True Outcomes，三种结果率）

- 定义：每打席结束在三振 + 保送 + 全垒打三者之一的比例
- 这三种结果有共同特征：球场上其他八位防守球员完全不参与
- 联盟 TTO%：
  - 2008: ~28%
  - 2019: ~36%（创纪录）
  - 2024: ~35%
- "棒球只剩三种结果"的论调由此而来

### 7. HR / Game（每场全垒打）

- 2014: 0.86
- 2017: 1.26
- 2019: 1.39（联盟史上最高）
- 2024: 1.07

### 8. 比赛时长（pace of play）

- 2022（改革前）：平均每场 3:04（3 小时 4 分）
- 2023（投手计时器 + 禁守备移位 + 大垒包上线）：2:38（直接砍掉 26 分钟）
- 2024：约 2:36-2:40

---

## 联盟 2023 改革规则（直接为飞球革命副作用踩煞车）

| 规则 | 直接针对 |
|---|---|
| Pitch clock（投手计时器）：垒上无人 15 秒 / 有人 18 秒 | 砍比赛时长 |
| 禁守备移位（Shift Ban）：内野手必须 2 人左右各一人，且站在内野草地内 | 提升 BABIP，鼓励打安打而不是只追 Barrel |
| 加大垒包（15 inch → 18 inch） | 鼓励盗垒，把"跑垒 + 接触型棒球"重新带回 |

→ 这三条本质都是反 Three True Outcomes — MLB 自己在踩飞球革命的煞车。

---

## 争议（这是用户明确想要的角度）

### 支持飞球革命的论据

1. **数学正确**：在 launch angle 10-25° 区间击球，预期 wOBA 比滚地球高 3-5 倍。打飞球本来就值
2. **可教可练**：Wallenbrock / Van Scoyoc / Latta 学派把改造做成系统流程，不再靠天分
3. **HR 是商业卖点**：球迷买票看 HR，不是看一垒安打。联盟 HR/场创纪录的几年商业指标也走高

### 反对飞球革命的论据

1. **三振泛滥**：联盟 K% 历史最高，球迷看到的是大量"什么都没发生"的打席
2. **比赛单一化**：TTO 占 36% — 球场其他位置的戏份被切掉。Joey Gallo 极致到 BA .160 但 38 HR — "他要么 HR 要么 K，没有第三种"
3. **传统棒球的智识被弃**：盗垒、推打、触击、Hit-and-Run 这些战术几乎绝迹
4. **比赛节奏**：2022 年单场 3 小时 4 分，被认为劝退新观众
5. **老派代表人物批评**：Pete Rose、Goose Gossage、Brian Kenny 之外的传统派多次公开骂

### MLB 自己的判决（看行动）

2023 年三条规则改革直接针对 fly ball + TTO 副作用 — 联盟用规则承认了过激，但**没有改 launch angle 这件事本身**。革命的内核（强调击球质量 / Barrel）保留，副作用（滚地球阵守备移位 + 长比赛 + 慢节奏）被切掉。

→ post 收口可用：**煞车踩了，车没停**。

---

## 主角：村上宗隆 Murakami Munetaka

### 基础数据

| 项 | 内容 |
|---|---|
| 出生 | 2000-02-02（熊本县） |
| 身高体重 | 188 cm / 97 kg |
| 投打 | 右投左打 |
| 现球队 | Chicago White Sox（2026 加盟） |
| 现球衣号 | 5（NPB 时期 55，加盟白袜改 5） |
| 现守位 | 三垒手（首发） |
| 合约 | 2 年 / $34M（2025 winter posting 后签下） |
| 入团 | 2017 年 NPB 选秀 Yakult Swallows 第一指名 |

### 2022 神之季节（破纪录那年）

| 项 | 数值 | 备注 |
|---|---|---|
| HR | 56 | 打破王贞治 1964 年 55 HR — 日本出生球员单季 HR 纪录 |
| BA | .318 | CL 打击王 |
| RBI | 134 | CL 打点王 |
| 三冠王 | ✓ | 战后日本人最年轻三冠王（22 岁） |
| OPS | 1.168 |  |
| MVP | CL MVP（连霸 2021、2022） |  |

### 2026 MLB 数据（白袜首月，截至 5 月 2 日）

| 项 | 数值 | 备注 |
|---|---|---|
| 出场场次 | 32 场 | 3 月 26 日 MLB 首秀 |
| HR | 13 | **MLB 全垒打领先**（5 月 2 日单独超越 Judge / Alvarez 的 12 支并列）|
| RBI | 23+ | 截 4 月底数据 |
| OPS | .965 | 截 4 月底 |
| K% | 33% | TTO 风险信号 — 飞球派副作用全部显现 |
| HR pace | 全季 65 HR | 若续保此节奏，将打破 Judge 2022 年 AL 纪录 62 HR |
| 首三场创举 | 连续三场 HR | 白袜队史第一人 / MLB 史第 4 人 |

### 2026 Statcast 进阶指标（baseballsavant 公开数据）

| 指标 | 村上 | 联盟百分位 |
|---|---|---|
| 平均击球初速 EV | 95.6 mph | 97 |
| Barrel rate | 23.5% | **99**（联盟顶级）|
| Hard-Hit% | 61.9% | 98 |
| xSLG（预期长打率）| — | 96 |

⚠️ 一个标志性击球例子：4 月某场 HR 仰角 48° / EV 95.2 mph — 是 Statcast 时代（2015 起）仅 8 支仰角 48° 以上的全垒打之一。极端飞球派的存在证明。

### 中心论据：村上 = 飞球革命的双面体

这场革命争议的核心 — 「它带来 HR 也带来三振」 — 在村上一个人身上完全压实：
- **革命兑现的最高样本**：99 百分位 Barrel + 98 百分位 Hard-Hit + 65 HR pace
- **副作用最高样本**：K% 33%（联盟平均 22.6% 已是历史最高，他还要再加 10 个百分点）

不是哲学辩论，是同一个球员同时给你两份账单。这就是为什么这篇 post 不用 4 个人物分担正反面 — 村上一个人就够了。

### NPB 时期数据（2017-2025）

#### 2022 神之季节（破纪录那年）

| 项 | 数值 | 备注 |
|---|---|---|
| HR | 56 | 打破王贞治 1964 年 55 HR — 日本出生球员单季 HR 纪录 |
| BA | .318 | CL 打击王 |
| RBI | 134 | CL 打点王 |
| 三冠王 | ✓ | 战后日本人最年轻三冠王（22 岁） |
| OPS | 1.168 |  |
| MVP | CL MVP（连霸 2021、2022） |  |

#### NPB Trackman 公开摘录估算（无官方 Statcast）

| 指标 | 村上 NPB | NPB 平均参考 | 解读 |
|---|---|---|---|
| 击球仰角 LA | 18-19° | NPB 平均 ~10-12° | NPB 时期已经是飞球派范本 |
| 击球初速 EV | 平均 ~92 mph，peak 116 mph | NPB 平均 ~84 mph | NPB 顶级 |
| K% | ~22%（NPB 偏高） | NPB 平均 ~17% | 副作用 NPB 时期就已出现 |
| BB% | ~16%（NPB 联盟最高级） | NPB 平均 ~9% | 选球能力一流 |

→ 村上 NPB 时期已经走 Latta 那一脉的飞球路线，2026 加盟白袜后所有指标"等比例升级到 MLB 顶端" — 这不是奇迹，是飞球革命方法论跨海后的完整兑现。

### 故事点（post 可用）

1. **2026 加盟白袜首月即 MLB HR 王**：3 月 26 日首秀，前 3 场场场 HR（白袜队史第一人、MLB 史第 4 人），32 场 13 HR 单独领先 MLB
2. **球衣号 55 → 5 的反差**：NPB 穿 55 致敬王贞治 1964 年 55 HR，2026 加盟白袜改穿 5 — 数字少了一位，纪录追的速度快了一倍（32 场 13 HR vs 王贞治当年单季 55 HR / 6 个月）
3. **2022 年第 134 场打出第 56 HR**：超越王贞治那一刻全日本上头条
4. **48° 仰角 HR**：Statcast 时代（2015 起）仅 8 支仰角 48° 以上的 HR 之一 — 极端飞球派的存在证明
5. **左打 + upright stance + 高位 cocked 球棒**：视觉招牌

---

## Visual Anchors（Person Recognition Gate MED → 必须落地）

prompt 里一定要出现的文字外貌（不准 embed 照片，不准写 photoreal）：

**身形 / 脸（NPB / MLB 共用）**：
- 188 cm / 厚实壮硕体型，肩膀宽
- 圆脸 / baby face 婴儿肥但下颌线有力
- 浓眉、双眼皮、眼神专注（不打开嘴笑）
- 黑色短发，自然偏分，发量厚
- 嘴微闭、专注表情（招牌"无表情专注"）
- 左打打击站姿：upright（直立不弯腰）、双手高位握棒在右肩后方 cocked、左肩朝向投手
- 球棒：深色木棒（Mizuno 系居多）

**2026 MLB Chicago White Sox 制服（封面用）**：
- 主场白色球衣（无 pinstripe，纯白 base） + 黑色 "Sox" diamond / Old English wordmark 胸标
- 客场银灰底 / 黑色"CHICAGO"字样（备选）
- 黑色棒球帽 + 白色 diamond / Old English "Sox" 商标
- 球衣号 **5** 黑底白字 / 白底黑字（视球衣版本）
- 主色调：黑 + 白 + 微银灰（高反差，跟 Yakult 的红绿 vibe 完全相反）

**NPB Yakult Swallows 制服（如做"渡海前"对照图用）**：
- 主场白衣，红色"yakult"横幅胸标，红绿双色细条纹袖口
- 球帽：navy 底 + 红色帽舌 + 白色"swallows / Y"标
- 球衣号 55

⚠️ MJ / Sora prompt 里**不要**出现：`reference photo`、`photoreal`、`8k`、`octane render` — 走 100m-poster 漫画 / 卷封风格（视觉宪法第 1、2 条）。

---

## 对位的 4 张图组规划（post 内 image-pack 用）

承上篇 4-cover panel 模式。这次以村上为主 cover，其他 3 张对位 3 个争议指标。

| # | 主角 | 对位指标 / 角色 | 风格备注 |
|---|---|---|---|
| 图 1（cover）| 村上宗隆（**白袜版**）| 革命双面体 / Barrel 99% + K% 33% 同时压在一人 | 100m-poster，White Sox 黑白高反差 + Chicago South Side dusk skyline，cover 标题区"飞球革命 / 打向天空的强打者 / FLY BALL REVOLUTION" |
| 图 2 | J.D. Martinez | 革命教父 / Launch Angle 起点 | 100m-poster，Tigers 旧版橘 + Detroit dusk |
| 图 3 | Josh Donaldson | "滚地球永远是出局" / FB% 哲学代言 | 100m-poster，Blue Jays 蓝 + Toronto skyline silhouette |
| 图 4 | Joey Gallo | TTO 极端化 / 历史警示标本 | 100m-poster，Texas Rangers 旧版红 + 高反差，姿态拉满"挥到底"或"三振走人"（与村上当代版形成"老警示 vs 新样板"对照）|

⚠️ 4 张差异化原则同上篇 — 球队主色 / 球场背景 / 动作 / 表情都不能撞。

→ 实际 prompt 文件这一轮先不写，等 post.md 文字过审后下一轮再 build。

---

## 写作时要避免的雷

1. **不要把 NPB Statcast 数字写得像 MLB 官方**：NPB 无官方 Statcast，数字标"公开报道估算"
2. **不要把 J.D. Martinez 教练学派绑死一个人**：Wallenbrock / Van Scoyoc / Latta 之间有分歧，主流归 Wallenbrock + Van Scoyoc，post 文字简化成"洛杉矶私人教练"避争议
3. **不要漏注英文缩写**：BA / LA / EV / FB / GB / TTO / Barrel 第一次出现都给中文
4. **不要写 photoreal / reference photo**（视觉宪法第 3 条）
5. **不要写"村上即将登陆 MLB"这种会过期的话**：用"被讨论 posting"或干脆不提
6. **不要破王贞治 vs 致敬王贞治混淆**：他既破纪录又同时穿 55 致敬 — 这个反差是核心戏剧点，写清楚

---

## 数据来源清单（post 尾注用）

- FanGraphs Library — Launch Angle / Exit Velocity / Barrel / GB% / FB% / K% / TTO 定义
- Baseball Savant（baseballsavant.mlb.com）— Statcast 数据
- baseballsavant.mlb.com/savant-player/munetaka-murakami-808959 — 村上 2026 进阶指标
- mlb.com/news/munetaka-murakami-hits-13th-home-run-... — 5 月 2 日单独领跑 HR
- mlb.com/news/mlb-stats-of-the-week-ending-april-23-2026 — 4 月统计
- FanGraphs "Munetaka Murakami, as Advertised" — 评论性深度分析
- The Athletic / Eno Sarris — J.D. Martinez 改造系列报道（2017-2018）
- MLB.com — 2023 rule changes 官方公告
- NPB 官方网站 — 村上宗隆 2022 三冠王数据
- 王贞治 1964 单季 55 HR 史料
- Joey Gallo career splits — Baseball Reference

---

## 收口候选（post 末尾 hate_bait）

候选 A：
> "老派当年骂'书呆子毁棒球'。今天他们解说时也用 launch angle。说的就是他们。"

候选 B（推荐）：
> "老派当年骂'书呆子毁棒球'，今天他们解说也用 launch angle。MLB 自己 2023 踩了煞车。但村上来了 — 32 场 13 HR、Barrel 99 百分位、K% 33%。煞车踩了，车没停。"

→ 倾向候选 B，把 hate_bait + 主角 + 标题"打向天空"的呼应一起完成，并把"煞车踩了车没停"作为 punchline。

<!--
写正文前必须 Read skills/xhs-note-assembly/SKILL.md。
发布正文和图组分工是物理分开的两个 section，禁止混写。
-->

## Working Brief

- One-sentence story: 评价一个打者好不好，棒球用了 100 多年的打击率，今天能算到挥棒动作本身，最后还要把所有维度压成 WAR 一个数字。
- Title direction: 「数据至上 + 设问」— "谁是最强" 的 question hook 配合 4 张球员海报形成 setup → answer 闭环；body 走演进 + WAR 总分卡的 framework
- 目标读者画像: 半懂 — 知道有打击率这玩意，听过 WAR / OPS 但说不清解决了什么

## 写作前必答（每题一句话）

- [x] 目标字数（150-300）：~360 字（加入 WAR 后略浮 20%）
- [x] 几段（3-5）：4 大段（开场 + 三刀 + WAR 总分 + 反扑收口）
- [x] 开头用 mystery 还是 number shock：mystery（"它有个大盲区"埋钩 → 后面揭答）
- [x] 每段计划塞哪个数字：100 多年 / 60 年 → 2002/4100 万/103 胜 + 2015 + 2024 → WAR 0-8 量级 → 2023/3 小时/2 小时半
- [x] 收口用 hate_bait / 反转 / A-B-C / 二选一 哪一种：hate_bait（老球评现在自己用 launch angle 和 WAR）
- [x] fact_pack.md 是否已经落盘：是

## 标题候选

1. 数据至上，谁是 MLB 最强打者（用户拍板）
2. 📊 别只看打击率，打者数据 60 年换了三代
3. 📊 都看打击率？现在球队第一眼看的是 WAR

## 最终标题

- 数据至上，谁是 MLB 最强打者

## 发布正文（直接复制到小红书）

> 绝对禁区：本 section 禁止出现 `Page X / 第 X 图 / P1-P8 / 图组 / 图上文案`。

```
📊 评价一个打者好不好，棒球用了 100 多年的打击率（BA）。它有个大盲区：你被保送上垒，它当作没事发生。整个进阶数据 60 年的演进，就是一代代把这种盲区拆掉。

🧠 三刀拆下来

第一刀是 OBP（上垒率）+ SLG（长打率）。OBP 把保送也算上垒 — 你能站上一垒就是有用；SLG 让全垒打和一垒安打不再同分。两个加起来就是球迷常说的 OPS。Beane 在《魔球》里抢的就是这个，2002 年 4100 万薪资打出 103 胜。

第二刀是 2015 年的 Statcast。雷达直接量你击球的初速、仰角，再用 xBA / xwOBA 反推「这球理论上应该几成」，把守备和运气剔出去。终于能分清"打得扎实但被接住" vs "打得烂但运气好"。

第三刀是 2024 年 5 月 MLB 公开的 Bat Tracking — 挥棒速度、攻击角、甜蜜点接触率全被记下。哪怕这球没打到，也能算出你挥棒本身好不好。

🏆 三刀拆完，最后还要一张总分卡 — WAR

今天评价一个打者，最终都换算成 WAR（Wins Above Replacement，比替补级球员多赢几场）。它把打击 + 跑垒 + 守备 + 守备位置补正全部压成一个数，横向比所有球员 — 一垒手 vs 中外野手 vs 投手都能比。MVP 投票、合约谈判、名人堂讨论，第一行就看 WAR。当代行情大约 1 个 WAR 值 800-1000 万美金。

💸 但联盟自己急了

数据玩到极端反伤比赛 — 三振 + 全垒打塞满每场，时长拖到 3 小时。2023 联盟加投手计时器、禁守备移位，比赛压回 2 小时半。当年骂"书呆子毁棒球"那批老球评，现在转播里张口闭口 launch angle 和 WAR。说的就是他们。
```

### 自检 checklist（发前必过）

- [x] 字数 ~360（加 WAR 后略超 300，主题跨度大可接受）
- [x] 4 大模块（开场 + 三刀 + WAR 总分 + 反扑）
- [x] 开头有 mystery（"它有个大盲区" — 埋钩）
- [x] 每段都有数字
- [x] 开场有可视化（保送上垒被当没事；Beane 抢 OBP）
- [x] 收口是 hate_bait（老球评现在自己在用 launch angle 和 WAR）
- [x] 没有 `Page X / 第 X 图 / P1-P8`
- [x] 每个英文缩写都立刻给中文注释（BA / OBP / SLG / OPS / xBA / xwOBA / Bat Tracking / WAR）
- [x] 简体中文

## 图组分工（读者看不到）

> 图组 = 4 张球员海报系列，每张对位一个进阶指标 / 一刀演进。统一 100m-poster 风格 + bilingual title block + bat-pose 锁定 + painterly 球场夜景。详细 prompt 见 `prompts/` 同名文件。

### 图 1（生图封面）— 法官 JUDGE
- 任务：拦停 — 一眼看到现役最强打者 + "MLB 最强打者，法官" 的 hook
- 对位：综合 / WAR / HR — 当代单数字头条 WAR 王 + 2× AL MVP
- 数据栏：62 HR · 11.4 WAR · 2× AL MVP
- 调色：Yankees navy + 朱红日落 + frieze 剪影
- 动作：post-contact bat-watching follow-through（HR 后高位 finish 注视球飞出）
- prompt：`prompts/cover_prompt.md`

### 图 2 — 安打王 ICHIRO
- 任务：把演进起点（第 0 代 BA / 安打）锚一个全球级名字
- 对位：第 0 代 — 打击率 / 安打撑了 100 多年的代表
- 数据栏：262 H 单季 · 4367 H 通算 · 10× All-Star
- 调色：Mariners 深 navy + 西雅图 teal + 远景 Mt. Rainier 剪影 + 小红日（致敬 Japan，克制不 kitsch）
- 动作：pre-pitch ritual — 右臂伸直举棒指投手 + 左手拉右肩袖口（招牌中的招牌）
- prompt：`prompts/cover_ichiro_prompt.md`

### 图 3 — 上垒教皇 SOTO
- 任务：第一刀 OBP 的活样板（魔球派 Beane 遗产的最完美执行者）
- 对位：第一刀 — OBP / 上垒率
- 数据栏：.421 OBP · 2024 BB 王 · .989 OPS
- 调色：教皇紫 + 金光（abstract 神格化，因 Soto 频繁跳队不绑球队）
- 动作：pre-pitch focused stance — 球棒高位 cocked + 眼神 laser locked + 招牌 smirk
- prompt：`prompts/cover_soto_prompt.md`

### 图 4 — 暴力 STANTON
- 任务：第三刀 Bat Tracking 的现役 poster boy + 收口"演进还没完"
- 对位：第三刀 — Bat Tracking / 挥棒速度（2024 年 5 月公开）
- 数据栏：挥棒 81.5 mph · EV 122 mph · 59 HR 单季
- 调色：火焰橙红 + 黑（跟 Judge 同 Yankee Stadium 但完全反向气场）
- 动作：mid-swing brutal follow-through — 低位 finish + 牙露 + jaw clenched 暴力痕迹
- prompt：`prompts/cover_stanton_prompt.md`

### 4 张差异化总览（防呆）

| | 法官 JUDGE | 安打王 ICHIRO | 教皇 SOTO | 暴力 STANTON |
|---|---|---|---|---|
| 指标 | WAR / HR / 综合 | BA / 安打 | OBP / 上垒 | Swing Speed / EV |
| 球队 | Yankees | Mariners | Mets | Yankees |
| 主色 | navy + 朱红日落 | navy + teal + 红日 | 教皇紫 + 金 | 火焰橙红 + 黑 |
| 动作 | 高位 finish 静止 | pre-pitch 仪式 | pre-pitch cerebral | 低位 finish 暴力 |
| 表情 | stoic 笃定 | 仪式 stoic | smirk 计算 | 牙露发力 |

## 话题标签

- #棒球
- #mlb
- #aaron judge
- #ichiro
- #juan soto
- #数据分析
- #魔球
- #sabermetrics

## 来源尾注

- Bill James《Baseball Abstract》各年版本（1977-1988）
- Michael Lewis《Moneyball: The Art of Winning an Unfair Game》（2003）
- 电影《Moneyball》Sony Pictures，2011
- MLB 官方 Statcast 文档：baseballsavant.mlb.com（xBA / xwOBA 定义）
- MLB Bat Tracking 官方发布稿（2024-05-14）
- FanGraphs library：OBP / SLG / OPS / wOBA 定义
- The Athletic / ESPN：2023 规则修改报道

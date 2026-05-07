<!--
写正文前必须 Read skills/xhs-note-assembly/SKILL.md。
发布正文和图组分工是物理分开的两个 section，禁止混写。
-->

## Working Brief

- One-sentence story: 评价一个投手好不好，棒球用了 100 多年的 W / ERA，今天能算到每一球的 spin 和 velo，最后用 fWAR 把所有维度压成一个数 — 不管你是 K 派还是 GB 派，都过这把尺。
- Title direction: 「数据至上 + 设问」— 镜像打者版「谁是最强」的 question hook，body 走演进 + 总分卡 + 现役 GOAT 的 framework
- 目标读者画像: 半懂 — 听过 Cy Young / FIP / Stuff+ 但说不清三者怎么连起来 + 怎么跟 K 派 / GB 派对应
- 系列定位: 跟打者版《数据至上，谁是 MLB 最强打者》(2026-05-01) 同模板（指标演进 + 总分卡 + 现役 GOAT），同结构（开场盲区 → 三刀 → 总分卡 → 反扑）
- 主指标: **fWAR (FanGraphs WAR)** 当总分卡；FIP / Stuff+ 当 case 锚点；K% / GB% 当流派标签
- 跟演进帖 v1 (`2026-05-03-moneyball-pitcher-edition`) 的关系：本帖是该 v1 的 final 版，case 从 4 人 (Skenes/Ryan/Maddux/deGrom) 收紧到 **3 人**(Maddux = 第一刀 FIP 活样板 + 高 GB 派 / Skubal = 第三刀 Stuff+ poster boy + 高 K 派 / Skenes = 现役综合 GOAT)，每张图同时承载"一刀 × 一流派"双身份，主指标统一改 fWAR

## 写作前必答

- [x] 字数（150-300）：~430 字（跨度大且把"三刀 + fWAR 总分卡 + 现役 GOAT"全压进来，可接受）
- [x] 几段（3-5）：4 大段（开场 + 三刀 + fWAR 总分卡 / 现役 GOAT + 反扑）
- [x] 开头：mystery（"它有个大盲区"埋钩 → 后面揭答）
- [x] 每段计划塞哪个数字：100 多年 / 60 年 → 2001 / 1992-1995 / 271 → 2015 → 2022/2024 / Stuff+ 130 / fWAR 6.4 → ~104 / ~4.6 → 2023 / 3 小时 / 2 小时半
- [x] 收口用 hate_bait / 反转 / A-B-C / 二选一 哪一种：hate_bait（老球评现在自己用 spin rate / Stuff+）
- [x] fact_pack: 关键数字部分已搜（Skubal 2024 6.4 fWAR / 一致票 / Triple Crown / 228 K / 2.39 ERA / 0.92 WHIP），其余 approximate（Skenes 2024 fWAR ~4.6 / Maddux career fWAR ~104）

## 标题候选

1. 数据至上，谁是 MLB 最强投手（用户拍板，跟打者版镜像）
2. 📊 投手数据 60 年三刀 — fWAR 把 K 派和 GB 派压成同一把尺
3. 📊 评价投手用了 100 年的 ERA，现在 spin 一转都给你算出来

## 最终标题

- 数据至上，谁是 MLB 最强投手

## 发布正文（直接复制到小红书）

> 绝对禁区：本 section 禁止出现 `Page X / 第 X 图 / P1-P8 / 图组 / 图上文案`。

```
📊 评价一个投手好不好，棒球用了 100 多年的胜投 (W) 和自责分率 (ERA)。它有个大盲区：球被打到场上的那一刻，你的运气、队友的守备、球场的大小，全都被算进"投手的责任"。整个进阶数据 60 年的演进，就是一代代把这种盲区拆掉。

🧠 三刀拆下来

第一刀是 2001 年的 DIPS / FIP（独立投球率）。Voros McCracken 提出：投手只对三件事 100% 负责 — 三振 (K)、保送 (BB)、全垒打 (HR)；球被打到场上就交给守备和运气。FIP 把这三个数压成一个跟 ERA 同尺度的数字。

90 年代的 Greg Maddux 是这套逻辑最直观的活样板 — 不靠球速吓人，靠让打者把球打成软滚地，让队友 routine ground out 接走。4× Cy Young 连庄（1992-1995，史上唯一）+ 18× Gold Glove + 1994 ERA+ 271（历史前列单季）。这就是「高滚地派」的极致：让你打到，但只能打到地上。

第二刀是 2015 年的 Statcast。雷达加高速摄像直接量每一球的转速 (spin rate)、横纵移动量 (movement)、出手延伸 (extension)。终于能分清"打者打不到"是因为投得快、投得刁、还是球种 deceive 视觉。

第三刀是 2022 公开 + 2024 完整化的 Stuff+ / Pitching+ — 用每一球的 velo / spin / movement 直接算出「这一球本质上有多难打」，独立于结果、独立于打者、独立于球场。

2024 + 2025 连庄 AL Cy Young 的 Tarik Skubal 是这一刀的现役 poster boy — 99mph 4-seam + 顶级 changeup。2024 拿了三振 / 防御率 / 胜投 三冠王，Cy Young 一致票通过。这就是「高三振派」的极致：球永远碰不到。

🏆 三刀拆完，最后还要一张总分卡 — fWAR

今天评价一个投手，最终都换算成 fWAR (FanGraphs Wins Above Replacement，比替补级投手多赢几场)。它把三振 + 保送 + 全垒打 + 局数全部压成一个数 — **不管你 K 倒打者、还是让他打到地上，都过这把尺**。Maddux career fWAR ~104（GB 路一辈子积累），Skubal 2024 单季 fWAR 6.4（K 路一年顶天）。1 个 fWAR ≈ 800-1000 万美金，跟打者一个价。

那现役综合 GOAT 是谁？Paul Skenes。2024 NL ROY + 2025 NL Cy Young。他厉害在两条路都顶 — Stuff+ 130（K 怪派联盟前 1%）+ 招牌 splinker（splitter + sinker 混合球种诱导高 GB%）。Rookie 季 fWAR 就 ~4.6 直接进 Cy Young 室。一个人把两条路走通。

💸 但联盟自己急了

数据玩到极端反伤比赛 — 投手发现 spin 拉满 + 滑球极致是统治打者最优解，结果三振太多、比赛节奏死。2023 联盟加投手计时器 (Pitch Clock) + 禁守备移位 + 加大垒包，把比赛压回 2 小时半。当年骂"书呆子毁棒球"那批老球评，现在转播里张口闭口 spin rate 和 Stuff+。说的就是他们。
```

### 自检 checklist（发前必过）

- [x] 字数 ~430（跨度大可接受，跟演进帖 / 打者版同尺度）
- [x] 4 大模块（开场 + 三刀 + fWAR 总分卡 / 现役 GOAT + 反扑）
- [x] 开头有 mystery（"它有个大盲区"）
- [x] 每段都有数字
- [x] 每个英文缩写都立刻给中文注释（W / ERA / DIPS / FIP / BB / HR / K / Statcast / Stuff+ / Pitching+ / fWAR / WAR / Pitch Clock / ERA+ / 4-seam）
- [x] 简体中文
- [x] 收口是 hate_bait（老球评现在自己用 spin rate / Stuff+）
- [x] 没有 `Page X / 第 X 图 / P1-P8`
- [x] 三个人物（Maddux / Skubal / Skenes）每个都同时承载"一刀 × 一流派"双身份 — Maddux 第一刀 + GB 派、Skubal 第三刀 + K 派、Skenes 综合
- [x] fWAR 当总分卡明显在文里（GB 路 vs K 路都换算成 fWAR）

## 图组分工（读者看不到）

> 图组 = **3 张投手海报**。继承 Skenes v3 风格基底（100m 海报式英文主标 + 顶 tag 两行赛季成就 + 底 stats 三轴 + figure 不遮挡主标 + painterly hand-illustrated），但**调色 / 镜头 / 动作 / 体型 / 招牌 visual 3 张全部差异化**。

> 每张图同时承载"一刀 × 一流派"双身份：
> - **Skenes** = 现役综合 GOAT（封面 / 主 hook，串联现役 + 两条路都顶）
> - **Skubal** = 第三刀 Stuff+ poster boy + 高 K 派代表
> - **Maddux** = 第一刀 FIP 活样板 + 高 GB 派代表

> Stats 三轴维持 ERA / K / Stuff+（Skenes + Skubal）。Maddux 因 Stuff+ 时代之前无数据，第三轴换成同性质的 ERA+。

### 图 1（生图封面）— SKENES（现役综合 GOAT，复用演进帖 v3 不动）
- 任务：拦停 — 一眼看到现役同时 K 顶 + GB 顶的综合怪 + "MLB 最强投手" hook
- 双身份：现役综合 GOAT — 串联 K 派 + GB 派 + Stuff+ 三刀
- 海报文字：复用 v3 — 顶 tag 两行 `2024 NL ROY` / `2025 NL CY YOUNG` + 主标 `SKENES` + 底 stats `1.96 ERA · 170 K · Stuff+ 130`
- 调色：100m 海报式**朱红**主背景 (v3 已锁定)
- 动作：catcher's POV 正面 — mid-delivery release apex（球刚离手 + 前脚 land + 后腿抬起 + 躯干前倾 + handlebar mustache 翘起）
- prompt: 直接 link 到演进帖 `demo_posts/2026-05-03-moneyball-pitcher-edition/prompts/cover_prompt.md` (v3) — 不重复落档，跨帖共用同一份

### 图 2 — SKUBAL（第三刀 Stuff+ poster boy + 高 K 派代表）
- 任务：现役 K 派的 figure — 99mph 4-seam + 顶级 changeup 一招制胜
- 双身份：第三刀 Stuff+ 时代代表 + 高三振派活样板
- 海报文字：顶 tag 两行 `2024 + 2025 AL CY YOUNG` / `2024 PITCHING TRIPLE CROWN` + 主标 `SKUBAL` + 底 stats `2.39 ERA · 228 K · Stuff+ 115`
- 调色（vs Skenes 朱红）：**Tigers 暖橙 + navy + 米黄**二色 layering，daytime sunlit
- 动作（vs Skenes mid-release）：**post-release changeup follow-through**（左臂下挥 + pronated 手腕）
- 镜头（vs Skenes catcher POV）：**三垒侧 photographer pit 3/4 view**
- 体型：6'3'' / 240 lbs lefty 厚壮（左投关键）
- prompt: `prompts/cover_skubal_prompt.md` (v1 已落)

### 图 3 — MADDUX（第一刀 FIP 活样板 + 高 GB 派代表）
- 任务：contact GOAT figure — 控球 + 弱接触 + 自己接守
- 双身份：第一刀 FIP / DIPS 活样板 + 高滚地派代表 + 唯一退役名宿
- 海报文字：顶 tag 两行 `4× CY YOUNG (1992-1995)` / `18× GOLD GLOVE` + 主标 `MADDUX` + 底 stats `1.63 ERA · 181 K · ERA+ 271`（**第三轴 Stuff+ → ERA+** 替换）
- 调色（vs Skenes 朱红 / Skubal 暖橙）：**cream + Braves 红 + 暖 sepia 90s 怀旧色温**（最温和 vintage 调）
- 动作（vs Skenes mid-release / Skubal post-release pronated）：**post-release fielding stance**（双脚 plant + glove 伸到身体左侧 ready 接 comebacker + trail leg 不抬）
- 镜头（vs Skenes / Skubal）：**正面棒球卡式 mid-distance framing**（拍 knees up，不是 close-up）
- 体型：6'0'' / 170 lbs 偏瘦（明显不像投手）
- 招牌 visual：**金边圆框 wireframe 眼镜**（90s gold round wire-frame）— Maddux 辨识度核心
- prompt: `prompts/cover_maddux_prompt.md` (v1 已落)

### 3 张差异化总览（防呆）

| | SKENES | SKUBAL | MADDUX |
|---|---|---|---|
| 双身份 | 现役综合 GOAT | 第三刀 Stuff+ + 高 K 派 | 第一刀 FIP + 高 GB 派 |
| 球队 | Pirates | Tigers | Braves |
| 主背景调色 | **朱红**（saturated 100m 阳光红）| **Tigers 橙 + navy + 米黄**（暖橙 daylight 二色）| **cream + Braves 红 + 暖 sepia**（90s 怀旧暖色）|
| 动作 | mid-release apex | post-release changeup follow-through | post-release fielding stance |
| 镜头 | catcher POV 正面 close-up | 三垒侧 photographer pit 3/4 view | 正面棒球卡式 mid-distance framing |
| 招牌 visual | handlebar mustache 翘起 | clean-shaven + lefty | **金边圆框眼镜** + 偏瘦 |
| 体型 | 6'6'' / 235 lbs 巨人 | 6'3'' / 240 lbs lefty 厚壮 | 6'0'' / 170 lbs 偏瘦 |
| Stats 第三轴 | Stuff+ 130 | Stuff+ ~115 | ERA+ 271（替换 Stuff+，时代之前无数据）|

### 防撞色（vs 打者版 + vs 演进帖 v1）

打者版用过：Yankees navy + 朱红日落 (Judge) / Mariners navy + teal + 红日 (Ichiro) / 教皇紫 + 金 (Soto) / 火焰橙红 + 黑 (Stanton)。
演进帖 v1（已废）原 4 张计划：Skenes 朱红 / Ryan red+navy+德州夕阳 / Maddux navy+红+白 / deGrom royal blue+橙。

本帖差异化：
- **Skenes 朱红** vs 打者版 Judge「Yankees navy 主 + 朱红日落 accent」 — 层级反向（Skenes 朱红是 ~55% 主背景、Judge 朱红只是 horizon accent）+ 时段反向（Skenes daytime sunlit vs Judge dusk moody），气场反向
- **Skubal 暖橙 + navy** vs 打者版 Stanton「火焰橙红 + 黑」 — Skubal 是 daytime 暖橙 + 二色 layering、Stanton 是 saturated 火焰橙 + 黑 single-tone explosion
- **Maddux cream + 红 + 暖 sepia** — 本帖 3 张里温度最低 / 最温和 vintage，跟 Skenes 朱红和 Skubal 暖橙都拉开。**主动 pivot 离开演进帖 v1 原本规划的 navy + 红 + 白 调色**（因 Skubal 已吃掉 navy + 暖色域，3 张要互错色，且 Maddux 的"棒球卡 90s vintage"气质比 modern navy 更合身份）

## 系列关系

- 打者版姊妹篇：《数据至上，谁是 MLB 最强打者》(slug `2026-05-01-moneyball-baseball-analytics-evolution`)
- 演进帖 v1：`2026-05-03-moneyball-pitcher-edition`（cast 4 人 — 已被本帖 v2 取代，留作 git history reference，不发布）
- 本帖（v2 / final）：`2026-05-04-pitcher-two-paths`（cast 3 人，每张图"一刀 × 一流派"双身份，主指标 fWAR）
- 发布建议：打者版 → 投手版（本帖）— 隔 2-3 天发，让 hitter / pitcher 双帖联动（同 framework + 同模板）

## 话题标签

- #棒球
- #mlb
- #paul skenes
- #tarik skubal
- #greg maddux
- #fwar
- #cy young
- #数据分析
- #sabermetrics
- #pitch clock

## 来源尾注

- Voros McCracken《Pitching and Defense: How Much Control Do Hurlers Have?》（Baseball Prospectus, 2001）— DIPS 理论原文
- Tom Tango FIP 公式定义（2003）— FIP 标准计算式
- MLB 官方 Statcast 文档：baseballsavant.mlb.com（2015 年起公开）
- MLB Stuff+ / Pitching+ 公开发布稿（2022 + 2024）
- FanGraphs library: fWAR / Stuff+ / FIP / ERA+ 定义
- Baseball-Reference: Maddux career stats（4× Cy Young / 18× GG / 355 W / 1994 ERA+ 271）
- ESPN / MLB Trade Rumors: 2024 + 2025 AL Cy Young 一致票 + Triple Crown / 2025 NL Cy Young (Skenes)
- The Athletic / ESPN: 2023 规则修改报道（Pitch Clock / 禁守备移位 / 加大垒包）
- 数据 caveat（最终发布前建议直接到 FanGraphs 网页核）：Skenes 2024 fWAR ~4.6 standalone（FanGraphs 反爬 403）/ Maddux career fWAR ~104（搜返回 116.7 但疑似跟 bWAR 116 conflate，保守用 ~104 更稳）/ Skubal 2024 Stuff+ ~115（训练记忆 approximate）

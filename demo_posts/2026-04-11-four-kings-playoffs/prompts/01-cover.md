## 这张图的任务

0.5 秒内让人在 XHS feed 滑过时**直接认出 4 张脸 + 主标题**。封面没有单一主角，走 2x2 四宫格角色选择卡版式，但**人物半身放大、脸是绝对主角**，背景队徽弱化成深色剪影，标题用一条**实色横带**横切画面正中央确保可读。

## 锁定风格：Blue Lock 现代日式

- 画风：Blue Lock（ブルーロック）/ First Slam Dunk 新剧场版主视觉
- flat-shaded 数码上色、清晰 HUD 文字层
- 四种颜色分区，但**饱和度全部压低**——背景越暗、越雾，人物越跳

## 这次改动的核心（v3）

| 维度 | v2（上一版） | v3（这一版） |
| --- | --- | --- |
| **人物大小** | 全身或 3/4 身 | **半身/胸以上**，脸占该 quadrant ~40% 面积 |
| **stat 数据行** | 每人一行 PPG/APG 等 | **全部删除** |
| **背景队徽** | 队徽 + 队名 wordmark | **纯 logo 剪影**，无文字，颜色压暗当 watermark |
| **背景配色** | 各队主色饱和 | **去饱和 + 压暗**，让人物跳出来 |
| **主标位置** | 横跨中央 + 打破分割线 | **专属横带**（solid 黑底 + 金边），不和球员标签挤 |
| **底排名字位置** | quadrant 顶部（撞标题）| quadrant **底部**（让出中央带）|

## 签名动作 + 队徽背景表

**关键妥协**：半身构图意味着 Jokic 的踢腿、Wemby 的水平飞身、Tatum 的撤步横向 gap **都看不到了**。签名动作只能靠**上半身姿态 + 手臂位置**暗示。脸的辨识度优先于全身招牌动作。

| 位置 | 球员 | 半身姿态 | 背景纯 logo（无文字）| 主色（去饱和）| 夺冠 |
| --- | --- | --- | --- | --- | --- |
| 左上 | **SGA** | 持球举至出手点的瞬间，胸以上，冷脸微笑 | OKC Thunder 盾形剪影（**纯盾型 + 篮球**，无 OKC 文字）| 深 teal + 暗橙 | **2025** |
| 右上 | **JOKIC** | 单手出手 follow-through，肩膀侧倾，络腮胡正脸 | Denver Nuggets **山峰剪影**（无 Nuggets 文字）| 暗 navy + 暗金 | **2023** |
| 左下 | **WEMBY** | 仰拍胸以上，一只手从画面上方往下伸要扇球，冷眼锁定下方 | San Antonio Spurs **单只马刺剪影**（无 SPURS 文字）| 暗 charcoal + 暗银 | （空白）|
| 右下 | **TATUM** | 出手 follow-through，胸以上，专注脸 | Boston Celtics **纯三叶草剪影**（无 CELTICS 文字）| 暗 forest green + 暗白 | **2024** |

## 中央文字：实色横带（重点改动）

```
横带（占画面纵向 ~22%，solid 深色底）
  主标：NBA 季后赛开打     ← 巨大金色
  副标：四大天王全部归位！  ← 小一号纯白
```

- **不再让标题"漂浮在四宫格上面"**——v2 漂浮的结果是被左下右下的名字标签挤成中间细条
- 改成一条**实心横带**横切画面 50% 高度位置：
  - 横带底色：solid `#0a0a0a` 黑色，上下两条 1px 金色细线作为边
  - 主标 "NBA 季后赛开打"：**纯金色 fill + 黑色 1px 描边**，Alibaba PuHuiTi Heavy，字号占横带 ~60% 高度
  - 副标 "四大天王全部归位！"：**纯白色 fill 无描边**，Alibaba PuHuiTi Heavy，字号占横带 ~30% 高度
  - 整条横带占画面 ~22%
- 横带把画面切成上下两半，**自带分割线**——四宫格的中央十字分割线只剩竖向一条
- 因为底色是 solid 黑，金色和白色文字都能拿到最大对比度，**不会再和球员色块糊在一起**

## HUD 极简化（v3）

每格只剩 3 个文字元素：

1. **球员英文名**（big label）
2. **夺冠年份**（gold pill，Wemby 留空）
3. **角标 01-04 / 02-04 / 03-04 / 04-04**

**全部 stat 数据行删除**——没有 PPG / FG% / DPOY 赔率 / 27.8 / 12.9 / 10.9 这些数字。封面只承担"认人 + 认主题"，数字留给单人卡。

**位置规则**：
- 上排（SGA / Jokic）name label 放在 quadrant **顶部**
- 下排（Wemby / Tatum）name label 放在 quadrant **底部**——让出中央横带
- 夺冠 pill 紧贴名字下方（上排）/ 上方（下排）
- 角标放在离 name label 最远的角落

## Final Prompt

```text
Vertical 3:4 key visual poster in the exact style of Blue Lock (ブルーロック) anime promo art and the First Slam Dunk 2022 movie poster — modern clean digital flat shading, thin neon outlines, cold cinematic lighting, icy desaturated base palette. Subjects pop bright against deeply muted backgrounds.

Composition: a 2x2 grid character select screen, but with two important modifications. (1) Each player is rendered HALF-BODY / CHEST-UP, with the FACE as the absolute dominant element of each quadrant — face occupies roughly 40% of each quadrant's area, easily recognizable at thumbnail scale in a social media feed. (2) A solid horizontal TITLE BAND cuts across the image at the vertical midpoint, replacing the 2x2 horizontal divider. The 2x2 grid retains only its vertical center divider; the horizontal divider IS the title band.

CRITICAL FRAMING RULE: half-body chest-up portrait of each player. NO full-body shots. NO leg-kick poses. NO horizontal flying poses. The face is king. Signature shooting motions are conveyed only through upper-body posture, head angle, and arm position visible above the chest line.

CRITICAL BACKGROUND RULE: each team logo behind the player is rendered as a PURE SYMBOL silhouette — NO team wordmarks, NO "OKC", NO "Nuggets", NO "SPURS", NO "CELTICS" text anywhere in the background. Just the bare iconic shape of each team's logo, in a deeply DESATURATED dark version of the team color, sitting like a faint watermark behind the player. The player must be visually brighter and more saturated than the background logo at all times.

TOP-LEFT QUADRANT — SGA (chest-up portrait):
A lean handsome NBA point guard in an Oklahoma City Thunder blue-and-orange jersey #2, captured CHEST-UP at the release point of his mid-range jumper — shooting arm fully extended upward into the top of the frame, ball just leaving his fingertips at the very top edge, body upright facing roughly 3/4 toward the camera, cold emotionless face with the faintest knowing smirk, calm killer eyes, short dark hair. The face is the brightest, sharpest element in the quadrant. Behind him: faint dark silhouette of the OKLAHOMA CITY THUNDER PRIMARY SHIELD LOGO (the shield outline with a basketball inside, NO "OKC" text, NO "THUNDER" text, just the bare shield+ball symbol), rendered in deeply muted dark teal-charcoal, low saturation, almost a watermark. Subject pops bright. Background tint: deep desaturated teal-charcoal.

TOP-RIGHT QUADRANT — JOKIC (chest-up portrait):
A heavyset bearded Serbian-looking NBA center in a Denver Nuggets navy-and-gold jersey #15, captured CHEST-UP at the follow-through of a one-handed fadeaway shot — shooting hand frozen in follow-through pose extended toward the upper-right corner of the frame, shoulders visibly twisted from the side-leaning Sombor Shuffle motion, head turned slightly with a calm knowing half-smile, eyes locked forward past the camera, shaggy hair, thick full beard. The beard and the smirk are the recognition anchors. Behind him: faint dark silhouette of the DENVER NUGGETS PRIMARY MOUNTAIN LOGO (just the angular mountain peak skyline silhouette, NO "Denver" text, NO "Nuggets" text, just the bare mountain shape), rendered in deeply muted dark navy with very subtle gold edge accents, low saturation, watermark-like. Background tint: deep desaturated navy.

BOTTOM-LEFT QUADRANT — WEMBY (chest-up portrait, low angle up):
An ultra-tall lanky 22-year-old French center in a San Antonio Spurs black-and-silver jersey #1, captured CHEST-UP from a slight LOW angle looking up at him so he feels impossibly tall, ONE arm (right) reaching DOWN from the top of the frame across the upper portion of the quadrant as if swatting an unseen ball away below the bottom edge of the frame, the other shoulder squared, cold piercing eyes locked on a target below the frame, calm killer expression, elongated anime-proportioned facial features (long jaw, wide forehead, cool alien-handsome look). The downward-reaching arm and the cold downward gaze are the recognition anchors. Behind him: faint dark silhouette of a SINGLE SPUR (the iconic spur from the San Antonio Spurs logo, just the bare spur shape, NO "SPURS" text, NO wordmarks), rendered in deeply muted dark charcoal-silver, low saturation, watermark-like. Background tint: deep desaturated charcoal-black, the coldest of all four quadrants.

BOTTOM-RIGHT QUADRANT — TATUM (chest-up portrait):
A wing forward in a Boston Celtics green-and-white jersey #0, captured CHEST-UP at the follow-through of his step-back jumper — shooting arm fully extended into the upper-right of the frame at the apex of the release, body upright with a slight backward lean from the just-completed step-back, eyes locked forward on the rim, focused intense expression, short twist braids. The shooting follow-through and the focused face are the recognition anchors. Behind him: faint dark silhouette of a SINGLE BOSTON CELTICS SHAMROCK (just the bare three-leaf shamrock shape, NO "CELTICS" text, NO wordmarks, NO leprechaun, NO Lucky), rendered in deeply muted dark forest-green, low saturation, watermark-like. Background tint: deep desaturated forest-green.

CENTER OF THE FRAME — SOLID TITLE BAND (replaces the horizontal grid divider):

A solid horizontal band cutting cleanly across the image at the vertical midpoint — this band physically replaces the 2x2 grid's horizontal divider line. Band height: roughly 22% of total poster height. Band fill: solid pure black (#0a0a0a), opaque, no transparency, no gradient. Top and bottom edges of the band are bordered by a thin 2px gold pinstripe line, like a wrestling pay-per-view announcement bar.

Inside the band, two lines of Chinese text, both in Alibaba PuHuiTi Heavy:
- Line 1 (main title, larger): "NBA 季后赛开打" — pure GOLD fill (#FFD700), thin 1px black outline, no drop-shadow needed (the solid black band IS the contrast). This line takes ~60% of the band's height. This is the single biggest text element on the entire poster.
- Line 2 (subtitle, smaller, below main): "四大天王全部归位！" — pure WHITE fill, no outline, no decoration. This line takes ~30% of the band's height, sitting tight under the main title.

The two text lines are perfectly horizontally centered in the band. Maximum legibility is the goal. The solid black band ensures the title NEVER bleeds into any quadrant's color or any player's body — it is its own clean horizontal stripe.

HUD LABELS in each quadrant (minimal — no stats):

TOP ROW (SGA, JOKIC) — name labels at TOP of quadrant:
- A large uppercase Alibaba PuHuiTi Heavy label with the player's last name: "SGA" / "JOKIC" — white fill with thin black outline, sitting in the top corner of the quadrant farthest from the center vertical divider (SGA top-left corner of TL quadrant, JOKIC top-right corner of TR quadrant).
- Directly under each name: a small gold pill/badge with black text "2025 CHAMP" (SGA) / "2023 CHAMP" (JOKIC).

BOTTOM ROW (WEMBY, TATUM) — name labels at BOTTOM of quadrant:
- A large uppercase Alibaba PuHuiTi Heavy label with the player's last name: "WEMBY" / "TATUM" — white fill with thin black outline, sitting in the BOTTOM corner of the quadrant farthest from the center vertical divider (WEMBY bottom-left corner of BL quadrant, TATUM bottom-right corner of BR quadrant). Both labels must respect a generous 8% safe margin from the frame edges so no letter is clipped.
- Directly above each name (between name and title band): a small gold pill/badge with black text. WEMBY: NO pill at all (leave the space completely empty and clean, do NOT add "—", "NO RING", "?", or any placeholder). TATUM: "2024 CHAMP".

NO STAT LINES ANYWHERE. No PPG, no RPG, no APG, no FG%, no DPOY odds, no streak counters. The four quadrants contain ONLY: player half-body portrait + faint background logo silhouette + name label + champ pill (3 of 4) + tiny corner page-counter.

Tiny page-counter tag in the corner farthest from the name label of each quadrant: "01/04" "02/04" "03/04" "04/04" in small monospace.

Style notes: this is modern Japanese sports anime key visual — Blue Lock / First Slam Dunk aesthetic. NOT manga ink, NOT painterly, NOT photorealism. Cold clean flat shading, thin neon outlines, sharp legible typography. Each player's FACE is the dominant element of their quadrant (~40% of quadrant area). Background team logos must be deeply desaturated and watermark-faint so the player always pops brighter. The solid black title band with gold/white text is the second-most-dominant element. NO team wordmarks, NO team city names, NO team nicknames anywhere in the backgrounds — only bare iconic shapes. Aspect ratio 3:4 vertical.
```

## 使用说明

- **跑图方式**：把这段 prompt 丢进 ChatGPT 4o 生图 / Gemini 2.5 Image / Midjourney / Imagen，每次出 2-4 张候选，挑一张最干净的。
- **判断顺序**：
  1. **缩到 thumbnail 大小看一眼**——4 张脸是不是都能认出来？主标 "NBA 季后赛开打" 是不是能读？这是真正的 feed 测试
  2. 黑色横带是不是干净的实色，没有被球员或队徽穿透
  3. 主标金色 vs 副标白色，色差是不是足够大
  4. 4 个背景 logo 是不是都没有文字（没有 OKC / Nuggets / SPURS / CELTICS 字样）
  5. 4 个背景 logo 是不是都被压暗成 watermark，球员明显比背景亮
  6. WEMBY 那一格的夺冠 pill 是不是真的空白（没有 — / NO RING / ? 之类的）
  7. TATUM 的 M 是不是没被画面右边裁掉（8% safe margin）
  8. 4 个名字标签都在该在的位置（上排在顶 / 下排在底）
- **常见失败模式**：
  - 球员被画成全身 / 站姿 → 强调 "CHEST-UP HALF-BODY portrait, face dominant, NO full body"
  - 背景 logo 还是带文字 → 强调 "PURE SYMBOL only, no wordmark, no team name"
  - 黑色横带变成半透明渐变 → 强调 "solid opaque #0a0a0a black, no transparency, no gradient"
  - 主标和副标字号几乎一样 → 强调 "main title is 60% of band height, subtitle is 30%, clear size hierarchy"
  - 下排名字标签飘到 quadrant 顶部撞上横带 → 单独 regenerate 那一格，强调 "WEMBY label at the BOTTOM-LEFT corner, TATUM label at the BOTTOM-RIGHT corner"

## 不要动什么

- 2x2 四宫格 + 中央实色横带切分的版式
- 半身/胸以上的人物构图（脸 ~40% quadrant 面积）
- 实色黑横带 + 金主白副的标题
- 纯 logo 剪影背景（无文字、watermark 化）
- 全部去除 stat 数据行
- 4 个英文 name label：SGA / JOKIC / WEMBY / TATUM
- 3 个夺冠 pill：2025 / 2023 / 2024 CHAMP（Wemby 留空）
- 上排 name label 在顶 / 下排 name label 在底的位置规则
- 3:4 纵向比例
- Blue Lock flat-shaded 数码画风

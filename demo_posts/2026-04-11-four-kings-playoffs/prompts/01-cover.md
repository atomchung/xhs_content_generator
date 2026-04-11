## 这张图的任务

0.5 秒内让人明白"这是 NBA 2026 季后赛 × 四大天王"。封面没有单一主角，走 2x2 四宫格角色选择卡版式，每人一种主色 + 一个**视觉上互不重复**的签名动作 + 背后自己球队的**官方队徽**剪影。

## 锁定风格：Blue Lock 现代日式

- 画风：Blue Lock（ブルーロック）/ First Slam Dunk 新剧场版主视觉
- flat-shaded 数码上色、冷色调、清晰 HUD 文字层
- 每人背后一只 flat-shaded 巨型**球队官方队徽**剪影（取代之前的吉祥物）
- 四种颜色分区（SGA 金 / Jokic 蓝紫 / Wemby 青绿 / Tatum 红绿）

## 签名动作 + 队徽背景表

**关键原则**：四人动作必须视觉上互不重复——三个是跳投手最容易糊在一起，所以靠**镜头角度 + 身体朝向 + 画面构图**拉开差异。

| 位置 | 球员 | 招牌动作 | 镜头差异化 | 背景队徽 | 主色 | 夺冠标签 |
| --- | --- | --- | --- | --- | --- | --- |
| 左上 | **SGA** | 中距离急停后仰 | **低角度仰拍**（视角在防守人胸口往上），身体纵向撑满画面 | OKC Thunder 队徽（盾形 + 闪电 + 篮球）| 金 + 蓝橙 | **2025 CHAMP** |
| 右上 | **JOKIC** | **Sombor Shuffle**（一脚向侧踢开）| **正侧面角度**，让踢开的那条腿横向伸出画面最长的一边 | Denver Nuggets 队徽（山峰 + 金色篮球 + Nuggets wordmark）| 蓝紫 + 银 | **2023 CHAMP** |
| 左下 | **WEMBY** | **追身盖帽**（从后方一臂往下扫）| **高角度俯拍 + 身体斜向飞扑**，整个身体几乎水平从左上斜切到右下 | San Antonio Spurs 队徽（银色 Spurs 文字 + 倒挂马刺齿轮）| 青绿 + 银 | （空白）|
| 右下 | **TATUM** | **Step-back 3-pointer**（撤步三分）| **水平视角**，身体重心侧移，**撤步位移**横向可见（后脚与前脚之间有一个明显横向间隙）| Boston Celtics 队徽（绿色三叶草 + 白色 "C" / 或 Celtics wordmark）| 红 + 绿白 | **2024 CHAMP** |

四个角度分工：**低角仰拍 / 正侧 / 高角俯拍 / 水平**——视觉上不会糊。

## 中央文字：主副标分层（重点改动）

```
主标（巨大）：NBA 季后赛开打
副标（小一号）：四大天王全部归位！
```

- **主标**"NBA 季后赛开打"：字号最大，纵向占画面 ~18-20%，**金色 fill + 白色粗描边 + 黑色 drop-shadow**，横跨封面正中央、打破四宫格分割线，像拳击赛事海报的主赛名
- **副标**"四大天王全部归位！"：字号小一号（~主标 60%），**白色 fill + 金色描边 + 细黑描边**，紧贴主标下方
- 两个标题颜色必须有明显色差（金 vs 白），一眼能看出哪个是主哪个是副
- 字体：Alibaba PuHuiTi Heavy
- 主标 + 副标合计占画面高度 ~28%，比任何一个球员都醒目

## Final Prompt

```text
Vertical 3:4 key visual poster in the exact style of Blue Lock (ブルーロック) anime promo art and the First Slam Dunk 2022 movie poster — modern clean digital flat shading, thin neon outlines, cold cinematic lighting, HUD data overlays baked into the image, icy desaturated base palette with saturated neon accent colors.

Composition: a 2x2 grid character select screen. Four NBA star archetypes, each in their own color-graded quadrant, separated by thin neon-line dividers that feel like a video game UI. In each quadrant, behind the player, a massive flat-shaded silhouette of that player's OFFICIAL TEAM LOGO (not mascot) fills the upper background — rendered as a single bold flat-color silhouette in the team's primary color, large enough to be the clear background anchor.

CRITICAL: the four poses MUST feel visually distinct from each other. Three of the four are jumpshot-type actions, so differentiation comes from CAMERA ANGLE and BODY ORIENTATION — low angle / profile side / high angle / level angle. Do NOT make all four look like variations of the same pose.

TOP-LEFT QUADRANT — SGA (low-angle upward shot):
A lean sleek NBA point guard in an Oklahoma City Thunder blue-and-orange jersey #2, captured mid MID-RANGE PULL-UP FADEAWAY, body fading slightly backward, elbow cocked at release point, ball just leaving fingertips, cold emotionless face with the faintest smirk, short dark hair. CAMERA: low angle shot from defender's chest height looking UP at him, so he dominates the vertical of the quadrant and the viewer feels shot-over. Body vertical, facing the camera. Behind him: massive flat-shaded silhouette of the OKLAHOMA CITY THUNDER OFFICIAL LOGO (shield with a basketball and a stylized lightning-bolt "T", "OKC" wordmark), rendered in flat dark-orange-on-teal-black. Gold-orange atmospheric particles. Deep teal-black base background.

TOP-RIGHT QUADRANT — JOKIC (profile side angle):
A tall heavyset bearded Serbian-looking center in a Denver Nuggets navy-and-gold jersey #15, performing his signature SOMBOR SHUFFLE — ONE LEG (left) fully kicked out to the SIDE and up, body leaning sideways AND backward, one-handed fadeaway release at the apex of a small side-hop, eyes focused on the rim not the defender, calm knowing half-smile. Shaggy hair, thick beard. CAMERA: direct PROFILE side angle, so the kicked-out leg extends horizontally across the widest part of the quadrant and is unmissable. Body oriented sideways, not facing camera. Behind him: massive flat-shaded silhouette of the DENVER NUGGETS OFFICIAL LOGO (mountain peak range with a gold basketball above, "Nuggets" wordmark arched below), rendered in flat navy-blue-on-navy-black with gold accents. Violet-silver atmospheric particles. Deep navy-black base background.

BOTTOM-LEFT QUADRANT — WEMBY (high-angle diagonal flying pose):
An ultra-tall lanky 22-year-old French center in a San Antonio Spurs black-and-silver jersey #1, captured mid CHASEDOWN BLOCK from the weakside — flying in from behind an unseen layup attempt, body NEARLY HORIZONTAL in the air cutting diagonally across the quadrant from upper-left to lower-right, one arm (right) fully extended DOWNWARD to swat a layup away from above, the other arm trailing for balance, elongated anime-proportioned limbs, cold piercing eyes looking down at the shooter. CAMERA: HIGH angle looking down at his horizontal flying body — the exact opposite framing of SGA's upward shot above him. Body oriented diagonally, head lower than feet. Behind him: massive flat-shaded silhouette of the SAN ANTONIO SPURS OFFICIAL LOGO ("SPURS" wordmark in silver block letters with an inverted silver SPUR replacing the U), rendered in flat silver-gray-on-black. Teal-silver atmospheric particles. Deep black base background. Color temperature noticeably colder than the other three quadrants.

BOTTOM-RIGHT QUADRANT — TATUM (level horizontal angle with lateral displacement):
A wing forward in a Boston Celtics green-and-white jersey #0, launching his signature STEP-BACK THREE-POINTER — body just landed from a big lateral step-back, back leg planted while front leg lifts, a VISIBLE HORIZONTAL GAP between back and front leg showing the lateral displacement, shooting arm fully extended at the apex of the release, elbow locked straight, eyes locked dead on the rim. Short twist braids, serious focused face. Stylized thin cracks of gold light running along his right Achilles as clean digital glow-lines (symbolizing his healed tendon from the rupture). CAMERA: LEVEL horizontal angle, viewer at eye height, so the lateral step-back displacement is the main readable element. Body oriented slightly sideways with clear lateral shift. Behind him: massive flat-shaded silhouette of the BOSTON CELTICS OFFICIAL LOGO (bold green shamrock with a white "CELTICS" wordmark arched over it, or alternatively the primary circular logo with the shamrock), rendered in flat Celtics-green-on-forest-black. Crimson-gold atmospheric particles. Deep forest-green-black base background.

POSE DIFFERENTIATION SUMMARY (must be enforced):
- SGA: vertical body, LOW angle up
- JOKIC: sideways body with kicked-out leg, PROFILE angle
- WEMBY: horizontal flying body, HIGH angle down
- TATUM: upright with lateral step-back gap, LEVEL angle
These four camera angles must all be visibly different so the four poses never look like variations of one jumpshot.

CENTER OF THE FRAME — MAIN TITLE + SUBTITLE (the visual centerpiece, breaking all four quadrants):

MAIN TITLE (the biggest element on the whole poster, occupying ~18-20% of total poster height by itself):
"NBA 季后赛开打" — in Alibaba PuHuiTi Heavy, GOLD fill with a thick WHITE outline and a black drop-shadow, rendered like a boxing pay-per-view main event banner. This is the single largest text element in the entire image. It must break the horizontal center of the poster and overlap the quadrant dividers.

SUBTITLE (directly below, smaller — about 60% the size of the main title):
"四大天王全部归位！" — in Alibaba PuHuiTi Heavy, WHITE fill with a thin GOLD outline and a subtle black drop-shadow. Positioned tight under the main title.

The two lines must be visibly COLOR-DIFFERENTIATED so it's immediately clear which is main and which is subtitle — main title is gold on white outline, subtitle is white on gold outline. Main title + subtitle together occupy ~28% of total poster height. Text must be unmissable at 0.5 seconds.

HUD LABELS in each quadrant (Blue Lock stat card style):
- Top-left of each quadrant, a large uppercase white-on-black Alibaba PuHuiTi Heavy label with the player's last name: "SGA" / "JOKIC" / "WEMBY" / "TATUM" — big and bold like a fighting game character name plate, white fill with thin black outline and each player's accent color drop-shadow.
- DIRECTLY UNDER each name label, a small CHAMPIONSHIP TAG in a thin rectangular pill/badge shape, gold fill with black text, reading the player's championship year (or left empty for Wemby):
  SGA:    "2025 CHAMP"
  JOKIC:  "2023 CHAMP"
  WEMBY:  (no championship tag — leave this space empty and clean; do NOT add any placeholder like "NO RING" or "—")
  TATUM:  "2024 CHAMP"
- Below the champ tag (or below the name for Wemby), a single tiny white monospace stat line:
  SGA:    "20+ × 138  ·  31.4 PPG"
  JOKIC:  "27.8 / 12.9 / 10.9"
  WEMBY:  "DPOY -5000 · 3.0 BPG"
  TATUM:  "26.8 → 21.3  ·  8.7 → 9.8"
- Small corner tag in each quadrant's lower corner: "01/04" "02/04" "03/04" "04/04".

Background: each quadrant tinted by its character's color (gold/violet/teal/red), thin digital neon grid overlay like a game UI, paper-cut flat shading with NO ink textures and NO paint textures. Fully clean digital finish.

Style notes: this is modern Japanese sports anime key visual — Blue Lock / First Slam Dunk aesthetic. NOT manga ink, NOT painterly, NOT photorealism. Cold clean flat shading, thin neon outlines, sharp legible typography. Each character's face clearly readable at ~50-55% of their quadrant (the main title takes the rest of the attention). The four team logos behind the players must be clearly identifiable as official NBA team logos (not mascots), rendered as bold flat silhouettes. Aspect ratio 3:4 vertical.
```

## 使用说明

- **跑图方式**：把这段 prompt 丢进 ChatGPT 4o 生图 / Gemini 2.5 Image / Midjourney / Imagen，每次出 2-4 张候选，挑一张最干净的。
- **判断顺序**：
  1. 先看**主标"NBA 季后赛开打"**是不是字最大、金色、没乱码
  2. 再看**副标"四大天王全部归位！"**是不是紧贴主标下方、颜色和主标明显区分（白 vs 金）
  3. 再看四色分区（金 / 蓝紫 / 青绿 / 红绿）是不是泾渭分明
  4. 再看四个**球队官方队徽**剪影是不是能看出队（Thunder 闪电盾 / Nuggets 山峰篮球 / Spurs 马刺字标 / Celtics 三叶草）
  5. 再看四个**镜头角度是不是都不一样**（SGA 仰 / Jokic 侧 / Wemby 俯 / Tatum 平）——这是这次改动的核心
  6. 再看**夺冠标签**：SGA 2025 CHAMP / JOKIC 2023 CHAMP / TATUM 2024 CHAMP / WEMBY 留空
  7. 最后看四个英文名标签 SGA / JOKIC / WEMBY / TATUM 是不是都有
- **常见失败模式**：
  - 主标副标颜色没拉开 → 让主标变成纯金色，副标变成纯白色，色差更大
  - 队徽被画成吉祥物 → 在 prompt 末尾加粗 "OFFICIAL TEAM LOGO, not mascot, not character"
  - 四个球员姿势长得一样（都是跳投）→ 单独把有问题的那一格重跑，强调 camera angle 差异
  - Wemby 被画成正面防守而不是飞行盖帽 → 强调 "body horizontal in air, high angle camera"
  - 夺冠标签漏掉 / Wemby 那一格也被画上 CHAMP 字样 → 重跑时强调 "Wemby has NO championship tag"

## 不要动什么

- 2x2 四宫格结构
- 四色分区（金 / 蓝紫 / 青绿 / 红绿）
- 四人签名动作（表里已列）
- 四个**官方队徽**剪影（不是吉祥物！）
- 四种不同的镜头角度（低仰 / 侧 / 高俯 / 水平）
- 中文主标 "NBA 季后赛开打"（金色、最大）
- 中文副标 "四大天王全部归位！"（白色、小一号）
- 四个英文 name label：SGA / JOKIC / WEMBY / TATUM
- 三个夺冠标签：2025 / 2023 / 2024 CHAMP（Wemby 留空）
- 3:4 纵向比例
- Blue Lock flat-shaded 数码画风（不要港漫水墨、不要日系格斗肌肉漫、不要照片级写实）

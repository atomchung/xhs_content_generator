# Paul Skenes 封面 prompt v3 — 一百公尺式明亮朱红海报

> v3 改动（来自用户反馈）：
> 1. **确认 catcher's POV 正面单版**（"对正面"）
> 2. **顶 tag 两行荣誉叠**：「2024 NL ROY」+「2025 NL CY YOUNG」
> 3. **整体明亮干净** — 抛弃 v2 PNC Park 黑色夜场 + Pittsburgh skyline + Clemente 桥的复杂背景
> 4. **风格基底改为参考《一百公尺》(100m) 电影海报** — 朱红阳光背景 + 单一主角 + painterly hand-illustrated + 极简构图、阳光 clarity 而非 nighttime moodiness

> 系列继承：英文 SKENES 主标（不回到 kanji 主标）+ Pirates 黑 jersey + handlebar mustache + 6'6" power-pitcher + mid-delivery release apex pose + `--ar 3:4 --stylize 250` + 禁词清单。

> ⚠️ 系列一致性 flag：这次主封面（Skenes）走「100m 海报朱红明亮背景 + 西式 magazine-cover 英文主标 + 两行赛季荣誉 tag」的混合排版。其他 3 张（RYAN / MADDUX / DEGROM）写之前必须跟用户确认是同步改成这套、还是保留打者版 v4 kanji 主导日影海报风。

## 决策记录

- 主封面 / 综合 / 现役 — 镜像打者版 Judge 主封面位置（用户拍板：现役球员优先）
- Skenes 2024 完整赛季 NL ROY + 2025 NL Cy Young（按用户事实输入）
- 1.96 ERA + 170 K（rookie 季 K/9 = 11.5）+ Stuff+ 130（联盟前 1%）
- 6'6'' / 235 lbs power-pitcher 体型 + handlebar mustache = 全联盟最辨识 rookie 视觉符号
- 调色锁朱红 + 黑 + 金黄 — 朱红当主背景（100m 海报基底），黑 + 金黄做 figure / text accent

## 海报文字（v3）

| 层级 | 文字 | 字型规格 | 位置 |
|---|---|---|---|
| ① 主标（最大）| `SKENES` | bold heavy condensed display（slab serif 或 extra-bold condensed sans），巨型横跨画面 ~70% 宽。颜色：cream / off-white fill + 黑墨 brush-textured outline，跟《100m》海报 kanji 同质感（虽然是英文，但要 hand-painted brushed-edge 不是 clean Helvetica 现代 sans）| 画面上中段，figure 头顶上方（不跟 figure 重叠 — 100m 海报式"字在上 figure 在下"清晰层级，区别于 SI cover layered overlap）|
| ② Tag line（顶，两行叠）| 第 1 行 `2024 NL ROY` / 第 2 行 `2025 NL CY YOUNG` | thin all-caps sans-serif，soft white 或浅奶油色，generous letter-spacing，两行垂直居中对齐 | 画面顶部 ~3-8% 位置 |
| ③ Stats / Credits 行（底）| `1.96 ERA · 170 K · Stuff+ 130` | thin tabular sans-serif，soft white，比顶 tag 略小 | 画面底部 ~5% 位置，居中 |

数据来源：1.96 ERA = 2024 完整赛季（133 IP）/ 170 K = 2024 全季三振数 / Stuff+ 130 = 2024 平均 Stuff+，联盟前 1% / 2024 NL ROY = 国联年度新人王（一致票通过）/ 2025 NL Cy Young = 按用户事实输入。

**注意**：移除 v1 的中文 kanji 主标层；移除 v2 的 SI-cover figure 局部遮挡字母效果（这次 figure 站在主标下方，不遮挡字）。

## 锁定动作 — Mid-Delivery Release Apex（投球出手定格）

> 跟 v1 / v2 一致，未改动。catcher 视角下投手正面对画，球刚离手的爆发瞬间。

- **球已离手**（球刚出手指 — 投向 camera）
- **右手臂**：full extension at release point，掌心朝下，手腕 snap 后的 follow-through 起步；从 catcher's POV foreshortened 朝 camera 方向
- **左手臂**（glove arm）：弯曲收回胸前，手套 tucked in 朝身体内侧
- **躯干**：完全前倾压向 camera，胸口几乎平行地面，背部弯成弧
- **前脚**（左脚）：刚 land，膝盖微弯吸震
- **后脚**（右脚）：抬离投手板，膝盖弯曲、脚跟向上甩到接近臀部高度
- **头部 / 视线**：眼睛 hard-locked 锁向 camera，下巴前突，眉头紧拧
- **表情**：jaw clenched + 嘴抿紧 + handlebar mustache 翘起清晰可见 + 鼻孔翕张 — fierce 全力发力
- **构图**：腰部以上为主，figure 占画布约 55-60%（v3 略调低，把上方留 SKENES 主标空间）

## Visual Anchors（必须有的识别度）

- **6'6" / 235 lbs power-pitcher 巨人体型**（厚重肩膀 + 大块头肌肉）
- **handlebar mustache**（粗、深棕色、两端微翘起）— Skenes 全联盟最辨识符号，必须画清晰、必须翘起两端
- 短深棕色头发（帽子下露一段）
- 方下颌 + 方脸型
- **年轻 early-20s 面孔**（生于 2002，2024 时 22 岁）— 不能画成中年大叔
- **右投**（throw arm = 右手）
- 球衣号 **30**
- **Pirates 主场黑色 alternate jersey**：黑底 + 金黄 cursive "Pirates" wordmark 横跨胸前 + 金黄描边
- 帽子：**黑色 Pirates 帽子 + 正面金黄 "P" logo**（圆体 P）

## Person Recognition Gate

```json
[{"person": "Paul Skenes", "confidence": 60, "tier": "MED", "reason": "2024 NL ROY breakout star, 2025 NL Cy Young per user fact, MLB All-Star Game starter as rookie, viral handlebar mustache + 100mph splinker arsenal, but only one full MLB season at training cutoff so model data is thin", "anchors_suggestion": "towering 6'6'' / 235 lbs power-pitcher build, recognizable thick handlebar mustache as signature facial feature with both ends curled slightly upward, short dark brown hair, square jaw, broad muscular shoulders, young early-20s appearance"}]
```

→ MED，prompt 内 embed 文字 anchors。

---

## Final Prompt（catcher's POV 单版）

```text
Japanese sports cinema poster illustration, 3:4 vertical, in the style of the 2024 Japanese film "100m" (一百公尺) theatrical poster — bright crimson sunlit backdrop, single hero, monumental composition, painterly hand-illustrated key art, clean minimal composition, sunlit clarity rather than nighttime moodiness, ALL TITLES BAKED INTO THE POSTER.

CAMERA ANGLE: directly from home plate / catcher's position looking back toward the pitcher's mound — fully frontal view of the pitcher in mid-delivery. Paul Skenes' chest and face are squared up toward camera; his throwing right arm reaches forward toward camera at release point as if the ball is being launched directly at the viewer.

POSE (locked) — Mid-Delivery Release Apex: Paul Skenes frozen at the exact moment the ball has just left his right hand. Right arm fully extended forward toward camera at full release point — palm rotated downward, fingers having just snapped, wrist beginning the follow-through arc. The thrown right arm appears foreshortened toward the camera in this frontal POV. Left arm (glove arm) tucked across the chest, glove pulled inward toward his torso for balance, glove pointing down-left. Torso bent forward aggressively over the front leg — chest leaning toward camera, back curved into a deep forward arc. Front foot (LEFT foot, since he is right-handed) just landed and planted firmly, knee slightly flexed for absorption. Back foot (RIGHT foot) lifted off the rubber, trail leg bent and kicking upward behind him with the heel raised toward his hips, leg spinning into follow-through. Head locked forward, chin jutted out aggressively, eyes hard-locked on the camera, jaw clenched, lips pressed tight, the thick handlebar mustache clearly visible and slightly curled upward at both ends, brow furrowed in maximum-effort intensity. Framed from waist up, figure dominates ~55-60% of canvas height (slightly less than v2 to leave room for the giant SKENES nameplate above his head).

CHARACTER (Paul Skenes, locked): towering 6'6'' / 235 lbs power-pitcher build with broad muscular shoulders that fill the frame, square jaw, square face shape, recognizable thick handlebar mustache as the signature facial feature with both ends curled slightly upward (this mustache must be clearly drawn and visible — it is his core visual identifier), short dark brown hair just visible under the cap brim, young early-20s appearance (NOT middle-aged), focused dark eyes shaded under the cap. Wearing the Pittsburgh Pirates black alternate home uniform — solid black jersey with the cursive "Pirates" wordmark across the chest in bold yellow-gold with gold outlining, jersey number 30 visible on the left chest panel beneath the wordmark or on the sleeve. Black Pirates cap with the iconic round yellow-gold "P" logo on the front (round serif "P"). Right hand throws — the ball has just left the right hand. Likeness recognizably Paul Skenes via the handlebar mustache + power-pitcher build + young face combination.

STYLE — POSTER ILLUSTRATION: hand-illustrated key art quality with thick black contour outlines on the figure, soft poster-paint cel shading, slight grain texture overlay. The figure has a frozen-statue-mid-explosion quality — full forward kinetic intent but rendered as a still illustration, NOT motion blur. Limited tonal range — each form rendered in three values (light / mid / shadow). Subtle textured brush noise across flat color fills. Variable-weight black ink on key contours. The overall feel is bright, clean, sunlit — like a daytime crimson-soaked Japanese movie-poster painting, NOT a moody nighttime scene.

BACKGROUND — bright crimson sunlit backdrop in the style of the "100m" (一百公尺) theatrical poster (painterly, NOT photo): a dominant warm crimson-red field fills the upper two-thirds of the canvas — bright, saturated, sunlit (think the daytime crimson of a Japanese sports-movie poster, not the dark navy of a night stadium). At the very top of the canvas, the crimson softens to a slightly warmer cream-orange suggesting overhead sunlight bleed. Across the lower third behind the figure, a clean horizontal painted abstraction suggests an out-of-focus baseball-field horizon — a thin band of muted yellow-gold (foul-line area or stadium-light-reflection band) and a thin band of warm cream-tan (infield dirt suggestion). NO Pittsburgh skyline, NO Clemente Bridge, NO stadium architecture, NO crowd — the background is intentionally minimalist and clean, pulling all attention to the figure. NO photoreal elements anywhere. The atmosphere is bright, sunlit, painterly, and uncluttered — uniformly crimson with soft cream highlights, like the "100m" poster's signature sunlit-red backdrop.

POSTER TEXT LAYOUT (modeled on the bright "100m" Japanese cinema poster — but with Western English nameplate replacing the kanji main title, since the team name SKENES is the brand here):

- ① MAIN NAMEPLATE — the English word "SKENES" rendered in massive bold heavy-weight condensed display typography (a thick chunky slab serif or extra-bold condensed sans-serif). Color: cream / off-white fill with thin black brush-textured outline edges (the same hand-painted distressed-edge feel as the kanji main title in the "100m" poster — NOT a clean Helvetica modern sans, but a brushed display face that reads as hand-painted poster lettering). Sized to occupy roughly 70% of canvas width. Position: horizontally centered in the UPPER-MID third of the canvas, sitting just above the figure's cap (the figure does NOT overlap or obscure the nameplate — clean separation between the SKENES title above and the figure below, like the "100m" poster's clear hierarchy of kanji-on-top + figure-below).

- ② TOP TAG LINES (two stacked lines) — at the very top of the canvas, two short tag lines stacked vertically and centered:
  - First line: "2024 NL ROY"
  - Second line (directly below the first): "2025 NL CY YOUNG"
  Both rendered in thin all-caps sans-serif with generous letter-spacing, soft white / light cream color, sitting above the SKENES nameplate. Each line sized small (~3% of canvas height each, total ~7% with line spacing). Functions as the achievement / billing tagline at the top of a sports-movie poster.

- ③ STATS / CREDITS LINE — "1.96 ERA · 170 K · Stuff+ 130" centered along the bottom 5% of the canvas, in a thin tabular sans-serif, soft white, slightly smaller than the top tag lines. Functions as the stats footer of the poster.

All text rendered crisply and fully legibly. Hierarchy from most-to-least dominant: SKENES nameplate (massive cream brush-edged) > top tags (thin white, two stacked lines) ≈ bottom stats line (thin white). NO Chinese characters anywhere. NO secondary subtitle below the SKENES nameplate.

COLOR PALETTE (locked): bright crimson-red (dominant ~55% — sunlit sky / background field) + warm cream highlights (~15% — top horizon glow + nameplate fill + bottom field tan band) + Pirates deep black (~20% — jersey + cap + figure outlines + nameplate edge stroke) + Pirates yellow-gold (~5% — jersey wordmark + cap "P" logo + lower horizon band) + warm skin tone + soft white (top tags + bottom stats). Six values total. The overall feel is bright, sunlit, daytime — NOT nighttime navy.

EMOTION: monumental, kinetic, weaponized power, sunlit clarity — the millisecond AFTER release when 100mph leaves the hand, captured in the bright daytime poster palette of "100m". Frozen explosive intent under crimson sun.

--ar 3:4 --stylize 250
```

---

## 跑图说明

### 跑图建议
1. 这一版只跑 V1 catcher's POV 单镜头 — 4-6 张择优
2. 评分维度：
   - **handlebar mustache 是否清晰、两端微翘** — 画错就不像 Skenes
   - 姿势是不是 mid-delivery release apex（球已离手 + 前脚刚 land + 后腿抬起 + 躯干前倾 + 右臂朝 camera 伸）
   - 6'6" 巨人体型 + 年轻 early-20s 面孔（不能画成中年大叔）
   - 球衣 / 装备：黑色 Pirates jersey + 金黄 cursive "Pirates" wordmark + 30 号 + 黑帽 + 金 P logo
   - **背景是否明亮干净**：朱红主色 + cream 高光 + 极简 horizon 抽象带，**没有 Pittsburgh skyline、没有 Clemente 桥、没有夜场黑沉感**
   - **SKENES 主标 100m 海报式层级**：cream/off-white fill + 黑墨 brush-textured outline，hand-painted 不是 clean Helvetica，**figure 不遮挡主标**（清晰分层：tag 顶 + SKENES 中上 + figure 中下 + stats 底）
   - 顶 tag 是不是两行叠："2024 NL ROY" / "2025 NL CY YOUNG"，浅白 thin sans-serif，all caps
   - 底 stats："1.96 ERA · 170 K · Stuff+ 130"，浅白 thin tabular sans-serif
   - **没有任何中文 / kanji 字符出现**
3. 镜头气质：catcher POV → 极致压迫感、像球员投向你的封面、面部 + mustache 极清晰、明亮朱红背景把 figure 衬得 monumentally clean

### 不要动的（铁律）
- 动作锁定 mid-delivery release apex
- 文字层级（v3）：SKENES 巨型主标 > 顶两行 tag（2024 NL ROY + 2025 NL CY YOUNG）≈ 底 stats — 英文主导，**完全没有中文 / kanji**
- 主标 SKENES 是 100m 海报式 hand-painted brush-textured 字型（cream fill + 黑墨 outline），**figure 不遮挡字**
- 背景是 100m 海报式朱红阳光（明亮 / 干净 / 极简），**不是 PNC Park 黑色夜场**
- handlebar mustache 必须清晰且两端微翘
- 6'6" 巨人体型 + 年轻 early-20s 面孔
- `--ar 3:4 --stylize 250`
- 禁词：photoreal / photorealistic / 8k / octane / studio photo / reference photo
- 这版**允许 prompt 内含文字**（baked-in 海报）

### Person Recognition Gate 复检

Skenes confidence = 60（MED），prompt 内已 embed 文字 anchors。生图后若辨识度仍不理想，可手动跑 photo pipeline：

```bash
python scripts/fetch_player_photo.py --player "Paul Skenes"
```

→ 提取 ESPN headshot → Read 写 appearance.md → 替换 prompt 内 anchors。

---

## 历史版本

- **v1**（已 push，git 历史可查）：100m kanji 主导排版（兵主 + SKENES 双语）+ V1 catcher POV + V2 侧角双版 + PNC Park 黑色夜场背景
- **v2**：西式 SI-cover 排版（SKENES 大字被 figure 局部遮挡）+ PNC Park 黑色夜场（被 v3 取代，未 push）
- **v3（当前）**：100m 海报式朱红明亮背景 + 西式 SKENES 英文主标（hand-painted brush-edged）+ 两行 tag（2024 NL ROY + 2025 NL CY YOUNG）+ 底 stats + catcher POV 单版

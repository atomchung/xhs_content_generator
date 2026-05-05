# Paul Skenes 封面 prompt — 100m-poster 锁定 + catcher 视角 / 侧角双版

> 系列规则继承打者版 Judge `cover_prompt.md` v4：100m 海报双语标题排版（kanji 主导 / 英文 secondary 同笔触）+ painterly 球场夜景 + pose 锁定 + `--ar 3:4 --stylize 250`。
> 这一张差异化在：**投手版主封面**（对位打者版 Judge 主封面位置）+ **调色（Pirates 黑 + 金黄 + PNC Park 夜景 + Pittsburgh skyline）** + **动作（mid-delivery release apex 投球瞬间，跟打者动作完全反向）** + **数据栏（ERA + Stuff+ + ROY）**。

## 决策（为什么选 Skenes 配 兵主）

- 主封面 / 综合 / 现役 — 镜像打者版 Judge 主封面位置（用户拍板：现役球员优先）
- Skenes 是 2024 完整赛季 NL ROY + Cy Young finalist（3rd），rookie 年就当 All-Star 先发（MLB 50+ 年首位）
- **1.96 ERA** + **133 IP / 170 K**（rookie 季 K/9 = 11.5）
- **Stuff+ 130+** 联盟前 1% — 直接对位 post.md 第三刀 Stuff+ 时代代表
- **splinker**（splitter + sinker 混合球种）2024 年 viral，独家武器
- 6'6'' / 235 lbs power-pitcher 体型 + **handlebar mustache** = 全联盟最辨识 rookie 视觉符号
- 调色对位：Pirates 黑 + 金黄（跟打者版 Stanton 的火焰橙红 + 黑区分 — Pirates 金是冷金 / arsenal 金，不是火焰橙）
- 称号「兵主」= 武器之主 / arsenal master，对位他多球种 100mph 武库 + 招牌 splinker

## 海报文字

| 层级 | 文字 |
|---|---|
| ① 主标 | `兵主` |
| ② 国际副标 | `SKENES` |
| ③ Tag line（顶）| `MLB 最强投手` |
| ④ Credits（底）| `1.96 ERA · Stuff+ 130 · 2024 NL ROY` |

数据来源：1.96 ERA = 2024 完整赛季（133 IP）/ Stuff+ 130 = 2024 平均 Stuff+，联盟前 1% / NL ROY = 2024 国联年度新人王（一致票通过）。

## 锁定动作 — Mid-Delivery Release Apex（投球出手定格）

跟打者版 4 张全部"挥棒"或"持棒"动作完全反向 — 这是**投手版独家动作**：球刚刚离手、整个躯干前倾压到 release point、后腿蹬起 spinning、front-leg landing 的爆发瞬间。

- **球已离手**（球刚出手指，画面里看不到球但能感觉到刚被投出）
- **右手臂**：已伸到 release point full extension，手指刚 release 完毕，掌心朝下，手腕 snap 后的 follow-through 起步状态
- **左手臂**（glove arm）：弯曲收回到胸前 / 略向左侧，手套朝下 / 朝身体内侧（balance arm tucked in）
- **躯干**：完全前倾压向 home plate，胸口几乎平行地面，背部弯成一道弧
- **前脚**（左脚）：刚 land，脚掌完全接地，膝盖微弯吸震（front foot strike）
- **后脚**（右脚）：已抬离投手板，膝盖弯曲、脚跟向上甩到接近臀部高度（trail leg up & spinning）
- **头部 / 视线**：眼睛 hard-locked 锁向 home plate 方向，下巴前突，眉头紧拧
- **表情**：**jaw clenched + 嘴抿紧 + handlebar mustache 翘起清晰可见 + 鼻孔翕张** — 全力发力的 fierce 表情，绝对不要 stoic（兵主名字 = 火力全开的武器之主，不是冷静思考者）
- **构图**：腰部以上为主，figure 占画布约 60%（动作大、覆盖面广 — 跟打者 50-55% 略高）

## Visual Anchors（必须有的识别度）

- **6'6" / 235 lbs power-pitcher 巨人体型**（跟 Judge / Stanton 同级别但更年轻 / 更壮硕）
- **handlebar mustache**（粗、深棕色、两端微翘起）— **这是 Skenes 全联盟最辨识的视觉符号，必须画清晰、必须翘起两端，不要画成普通胡子**
- 短深棕色头发（帽子下露一段）
- 方下颌 + 方脸型 + 厚重肩膀 + 大块头肌肉
- 年轻 early-20s 面孔（生于 2002，2024 时 22 岁）— 不能画成中年大叔
- **右投**（throw arm = 右手）
- 球衣号 **30**
- **Pirates 主场黑色 alternate jersey**：黑底 + 金黄 cursive "Pirates" script 横跨胸前 + 金黄描边
- 帽子：**黑色 Pirates 帽子 + 正面金黄 "P" logo**（圆体 P，跟其他 P 区分）
- **可选**：右臂 / 左臂上隐约可见 sleeve tattoo 边缘（Skenes 招牌 — 但这条非必要，因为 illustration 里不画 tattoo 也不影响辨识，画了反而可能 distracting）

## Person Recognition Gate

```json
[{"person": "Paul Skenes", "confidence": 60, "tier": "MED", "reason": "2024 NL ROY breakout star, MLB All-Star Game starter as rookie, viral handlebar mustache + 100mph splinker arsenal, but only one full MLB season so model training data is thin", "anchors_suggestion": "towering 6'6'' / 235 lbs power-pitcher build, recognizable thick handlebar mustache as signature facial feature with both ends curled slightly upward, short dark brown hair, square jaw, broad muscular shoulders, young early-20s appearance"}]
```

→ MED，prompt 内必须 embed `anchors_suggestion` 文字 anchors。

---

## V1 — Catcher's POV（投手正面 / 朝 camera 投）

Final Prompt：

```text
Japanese sports cinema poster illustration, 3:4 vertical, in the style of contemporary Japanese sport-movie key art (e.g. "100m" / "The First Slam Dunk" theatrical posters) — single hero, monumental composition, dominant Pirates black + gold atmosphere, cinematic stillness frozen at peak action, ALL TITLES BAKED INTO THE POSTER.

CAMERA ANGLE: directly from home plate / catcher's position looking toward the pitcher's mound — fully frontal view of the pitcher in mid-delivery. Paul Skenes' chest and face are squared up toward camera, his throwing right arm reaching toward the camera at release point as if the ball is being launched directly at the viewer.

POSE (locked) — Mid-Delivery Release Apex: Paul Skenes frozen at the exact moment the ball has just left his right hand. Right arm extended fully forward toward camera at full release point — palm rotated downward, fingers having just snapped, wrist beginning the follow-through arc. The thrown right arm appears foreshortened toward the camera in this frontal POV. Left arm (glove arm) tucked across the chest, glove pulled inward toward his torso for balance, glove pointing down-left. Torso bent forward aggressively over the front leg — chest leaning toward camera, back curved into a deep forward arc. Front foot (LEFT foot, since he is right-handed) just landed and planted firmly, knee slightly flexed for absorption. Back foot (RIGHT foot) lifted off the rubber, trail leg bent and kicking upward behind him with the heel raised toward his hips, leg spinning into follow-through. Head locked forward, chin jutted out aggressively, eyes hard-locked on the camera (the catcher / batter / viewer), jaw clenched, lips pressed tight, the thick handlebar mustache clearly visible and slightly curled upward at both ends, brow furrowed in maximum-effort intensity. Framed from waist up, figure dominates ~60% of canvas height with monumental forward-leaning power.

CHARACTER (Paul Skenes, locked): towering 6'6'' / 235 lbs power-pitcher build with broad muscular shoulders that fill the frame, square jaw, square face shape, recognizable thick handlebar mustache as the signature facial feature with both ends curled slightly upward (this mustache must be clearly drawn and visible — it is his core visual identifier), short dark brown hair just visible under the cap brim, young early-20s appearance (NOT middle-aged), focused dark eyes shaded under the cap. Wearing the Pittsburgh Pirates black alternate home uniform — solid black jersey with the cursive "Pirates" wordmark across the chest in bold yellow-gold with gold outlining, jersey number 30 visible on the left chest panel beneath the wordmark or on the sleeve. Black Pirates cap with the iconic round yellow-gold "P" logo on the front (round serif "P" — distinct from any other team's "P"). Right hand throws — the ball has just left the right hand. Likeness recognizably Paul Skenes via the handlebar mustache + power-pitcher build + young face combination.

STYLE — POSTER ILLUSTRATION: hand-illustrated key art quality with thick black contour outlines on the figure, soft poster-paint cel shading, slight grain texture overlay. The figure has a frozen-statue-mid-explosion quality — full forward kinetic intent but rendered as a still illustration, NOT motion blur. Limited tonal range — each form rendered in three values (light / mid / shadow). Subtle textured brush noise across flat color fills. Variable-weight black ink on key contours.

BACKGROUND — PNC Park night atmosphere with Pittsburgh skyline (painterly, NOT photo): a moody Pittsburgh night sky dominates the upper canvas — deep midnight black at the top transitioning down to a warm yellow-gold glow along the horizon line (stadium lights + city glow bleed). Across the upper third, a soft silhouette of the Pittsburgh downtown skyline rendered in slightly darker black-grey shapes against the gold-glowing horizon — recognizable as a city skyline but not detailed individual buildings. In the upper-mid third, the iconic yellow-gold steel arches of the Roberto Clemente Bridge (PNC Park's signature view) span horizontally as a thin silhouette, painted in muted gold against the black sky — present as an atmospheric anchor, not the focus. NO individual fans, NO scoreboard text, NO photorealism, NO detailed crowd. The atmosphere is painterly and moody, like a Japanese movie-poster painted backdrop. Yellow-gold stays as an ATMOSPHERIC ACCENT (~25% of canvas — sky horizon glow + bridge silhouette + jersey wordmark), with deep black dominating ~55% of the canvas.

POSTER TEXT LAYOUT (modeled on Japanese cinema posters such as the 2024 Japanese film "100m" poster):

The text hierarchy is the OPPOSITE of a Western banner: the Chinese characters are the dominant title, the English is the international subtitle. CRITICAL: the Chinese characters "兵主" and the English word "SKENES" must share the SAME visual treatment — same brush-textured edge, same heavy weight, same color, same slight grain/distress — so they read as one bilingual title block by the same poster designer, not two mismatched fonts pasted together.

- ① MAIN TITLE — the two Simplified Chinese characters "兵主" rendered in massive bold brush-stroke calligraphic poster typography, off-white / cream color with subtle paper-grain distress along the edges (Japanese-poster brushed-kanji feel). This is the largest text element in the poster, occupying about 30% of canvas width. Position: upper-middle of the canvas, sitting just above the figure's cap. Both Han characters must be accurately formed and legible (兵 with 八 + 斤 components, 主 with the dot on top stroke).

- ② INTERNATIONAL SUBTITLE — the English word "SKENES" rendered immediately below the "兵主" title, in a heavy condensed serif or chunky display typeface that VISUALLY MATCHES the "兵主" treatment (same off-white color, same brush-textured / slightly distressed edges, similar visual weight per glyph). Sized at roughly 50% the width of the "兵主" title above. The two together form one unified bilingual title block.

- ③ TAG LINE — the Simplified Chinese phrase "MLB 最强投手" placed at the very top of the canvas (above ① ②) as a thin centered tag, in a simple light-weight sans-serif with slight letter-spacing, soft white. Functions as the "catchphrase" line at the top of a Japanese movie poster.

- ④ STATS / CREDITS LINE — "1.96 ERA · Stuff+ 130 · 2024 NL ROY" centered along the bottom 6% of the canvas, in a thin tabular sans-serif, soft white, smaller than the tag line above. Functions as the credits / billing block at the bottom of a Japanese movie poster.

All text rendered crisply and fully legibly. Simplified Chinese characters accurately formed (not garbled). Hierarchy from most-to-least dominant: 兵主 > SKENES > MLB 最强投手 > stats line.

COLOR PALETTE (locked): Pirates deep black (dominant ~55% — sky + jersey + cap + skyline) + Pirates yellow-gold (~25% — horizon glow + bridge silhouette + jersey wordmark + cap "P" logo) + warm skin tone + black ink contours + brushed off-white text. Six values total. NO red, NO blue, NO orange — keep palette strictly black + gold + skin + paper.

EMOTION: monumental, kinetic, weaponized power — the millisecond AFTER release when 100mph leaves the hand. Like a Japanese sport-movie poster announcing the protagonist's signature attack. Frozen explosive intent.

--ar 3:4 --stylize 250
```

---

## V2 — 侧角（3/4 view, ESPN highlight angle from third-base side）

Final Prompt：

```text
Japanese sports cinema poster illustration, 3:4 vertical, in the style of contemporary Japanese sport-movie key art (e.g. "100m" / "The First Slam Dunk" theatrical posters) — single hero, monumental composition, dominant Pirates black + gold atmosphere, cinematic stillness frozen at peak action, ALL TITLES BAKED INTO THE POSTER.

CAMERA ANGLE: approximately 30 to 45 degrees off-axis from the catcher-line, positioned on the third-base side photographer pit. Three-quarter view of the pitcher in mid-delivery — the full extension of his throwing arm + the deep forward-bent torso + the trail leg kicking up are all clearly visible. This is the iconic ESPN baseball-broadcast angle for capturing pitcher delivery mechanics.

POSE (locked) — Mid-Delivery Release Apex: Paul Skenes frozen at the exact moment the ball has just left his right hand. From this 3/4 angle (camera on third-base side), his throwing right arm is fully extended forward and slightly across the body, reaching toward camera-right (toward home plate direction) — arm straight at full release point, palm rotated downward, fingers having just snapped the ball. Left arm (glove arm) tucked across the chest, glove pulled toward his torso for balance, glove pointing downward-inward. Torso bent forward dramatically over the front leg — body folded into a deep forward arc, almost parallel to the ground at the chest. Front foot (LEFT foot) just landed, knee flexed for absorption, foot pointing toward camera-right. Back foot (RIGHT foot) lifted off the rubber, trail leg bent and kicking upward behind him with the heel raised toward his hips, the elevated trail leg clearly silhouetted on the left side of the frame. Head locked toward camera-right (toward home plate), chin jutted out aggressively, eyes hard-locked on the unseen target, jaw clenched, lips pressed tight, the thick handlebar mustache clearly visible from this 3/4 angle and slightly curled upward at both ends, brow furrowed in maximum-effort intensity. Framed from waist up with extended arm and elevated trail leg pushing the figure to occupy ~60% of canvas height in monumental forward-leaning power.

CHARACTER (Paul Skenes, locked): towering 6'6'' / 235 lbs power-pitcher build with broad muscular shoulders that fill the frame, square jaw, square face shape, recognizable thick handlebar mustache as the signature facial feature with both ends curled slightly upward (this mustache must be clearly drawn and visible — it is his core visual identifier), short dark brown hair just visible under the cap brim, young early-20s appearance (NOT middle-aged), focused dark eyes shaded under the cap. Wearing the Pittsburgh Pirates black alternate home uniform — solid black jersey with the cursive "Pirates" wordmark across the chest in bold yellow-gold with gold outlining, jersey number 30 visible on the back or sleeve. Black Pirates cap with the iconic round yellow-gold "P" logo on the front (round serif "P"). Right-handed pitcher — throwing arm = right arm. Likeness recognizably Paul Skenes via the handlebar mustache + power-pitcher build + young face combination.

STYLE — POSTER ILLUSTRATION: hand-illustrated key art quality with thick black contour outlines on the figure, soft poster-paint cel shading, slight grain texture overlay. Frozen-statue-mid-explosion quality — full forward kinetic intent but rendered as a still illustration, NOT motion blur. Limited tonal range — each form rendered in three values (light / mid / shadow). Subtle textured brush noise across flat color fills. Variable-weight black ink on key contours.

BACKGROUND — PNC Park night atmosphere with Pittsburgh skyline (painterly, NOT photo): a moody Pittsburgh night sky dominates the upper canvas — deep midnight black at the top transitioning down to a warm yellow-gold glow along the horizon line (stadium lights + city glow bleed). Across the upper third, a soft silhouette of the Pittsburgh downtown skyline rendered in slightly darker black-grey shapes against the gold-glowing horizon — recognizable as a city skyline but not detailed individual buildings. In the upper-mid third, the iconic yellow-gold steel arches of the Roberto Clemente Bridge (PNC Park's signature view) span horizontally as a thin silhouette, painted in muted gold against the black sky — present as an atmospheric anchor, not the focus. NO individual fans, NO scoreboard text, NO photorealism, NO detailed crowd. The atmosphere is painterly and moody, like a Japanese movie-poster painted backdrop. Yellow-gold stays as an ATMOSPHERIC ACCENT (~25% of canvas), with deep black dominating ~55%.

POSTER TEXT LAYOUT (modeled on Japanese cinema posters; bilingual title block must read as ONE poster designer's matched typography):

- ① MAIN TITLE — the two Simplified Chinese characters "兵主" rendered in massive bold brush-stroke calligraphic poster typography, off-white / cream color with subtle paper-grain distress along the edges. Largest text element, occupying ~30% of canvas width. Position: upper-middle, just above the figure's cap. Both Han characters accurately formed and legible.

- ② INTERNATIONAL SUBTITLE — the English word "SKENES" rendered immediately below the "兵主" title, in a heavy condensed serif or chunky display typeface that VISUALLY MATCHES the "兵主" treatment (same off-white color, same brush-textured / slightly distressed edges, similar visual weight per glyph). Sized at roughly 50% the width of the "兵主" title above.

- ③ TAG LINE — the Simplified Chinese phrase "MLB 最强投手" placed at the very top of the canvas (above ① ②) as a thin centered tag, in a simple light-weight sans-serif with slight letter-spacing, soft white.

- ④ STATS / CREDITS LINE — "1.96 ERA · Stuff+ 130 · 2024 NL ROY" centered along the bottom 6% of the canvas, in a thin tabular sans-serif, soft white, smaller than the tag line above.

All text rendered crisply and fully legibly. Simplified Chinese characters accurately formed (not garbled). Hierarchy from most-to-least dominant: 兵主 > SKENES > MLB 最强投手 > stats line.

COLOR PALETTE (locked): Pirates deep black (dominant ~55%) + Pirates yellow-gold (~25%) + warm skin tone + black ink contours + brushed off-white text. Six values total. NO red, NO blue, NO orange.

EMOTION: monumental, kinetic, weaponized power — the millisecond AFTER release when 100mph leaves the hand. Frozen explosive intent.

--ar 3:4 --stylize 250
```

---

## 跑图说明

### 跑图建议
1. V1（catcher's POV / frontal）和 V2（侧角）各跑 2-4 张
2. 评分维度：
   - **handlebar mustache 是否清晰、两端微翘** — 这是 Skenes 辨识度核心，画错就不像
   - 姿势是不是 mid-delivery release apex（球已离手 + 前脚刚 land + 后腿抬起 + 躯干前倾压低）—— 不是 windup 起手 (太早) 也不是 follow-through 收尾 (太晚)
   - 6'6" 巨人体型是否撑出画面（肩宽 + 大块头）
   - 球衣 / 装备：黑色 Pirates jersey + 金黄 cursive "Pirates" wordmark + 30 号 + 黑帽 + 金 P logo 是否齐全
   - 背景：PNC Park 夜场气场 — 黑天 + 金黄横线 horizon glow + Pittsburgh skyline 剪影 + Clemente 桥 yellow steel 横跨（painterly，**not photo**）
   - 文字层级是否对：兵主 最大、SKENES 第二、MLB 最强投手 顶 tag、stats 底 credits
   - 兵主 + SKENES 是否字型质感统一（笔触 / 描边 / 颜色 / 磨砂感一致 — 不能一个毛笔一个 Helvetica）
   - 中文字形清晰、笔画完整（兵 = 八 + 斤、主 = 上面一点 + 王）
3. 两版气质对比：
   - V1 catcher POV → 极致压迫感、像球员"投向你"的封面、面部 + mustache 极清晰
   - V2 侧角 → 投球力学全展开、像 ESPN broadcast 截屏的设计版、能看到 trail leg 抬起 + 躯干前倾全弧线

### 不要动的（铁律）
- 动作锁定 mid-delivery release apex（前脚刚 land + 后腿抬起 + 躯干前倾 + 右臂 release）
- 文字层级：兵主 > SKENES > MLB 最强投手 > stats — kanji 主导、英文衬位
- 兵主 + SKENES 必须同笔触 / 同质感 / 同颜色（一组 bilingual title block）
- 调色锁定 black + gold（不掺其他颜色 — 跟打者版 Stanton 火焰橙红 + 黑做硬区分）
- 背景元素：PNC Park 夜 + 黑天 + 金黄 horizon + Pittsburgh skyline + Clemente 黄钢桥剪影（painterly，**not photo**）
- handlebar mustache 必须清晰且两端微翘（Skenes 辨识度 #1）
- 6'6" 巨人体型 + 年轻 early-20s 面孔（不能画成中年大叔）
- 中文用简体（兵主 / 最强 / 投手）
- `--ar 3:4 --stylize 250`
- 禁词：photoreal / photorealistic / 8k / octane / studio photo / reference photo
- 这版**允许 prompt 内含文字**（baked-in 海报）— 跟系列其他 3 张同规格

### Person Recognition Gate 复检

Skenes confidence = 60（MED），prompt 内已 embed 文字 anchors（handlebar mustache + 6'6" 巨人 + early-20s + 方下颌 + 短深棕发 + 厚肩）。生图后若辨识度仍不理想，可手动跑 photo pipeline：

```bash
python scripts/fetch_player_photo.py --player "Paul Skenes"
```

→ 提取 ESPN headshot → Read 写 appearance.md → 替换 prompt 内 anchors。但首轮先按当前 prompt 跑，成本低。

# Giancarlo Stanton 系列封面 prompt — 暴力挥棒 Bat Tracking 王

> 系列规则继承 Judge `cover_prompt.md` v4：100m 海报双语标题排版（kanji 主导 / 英文 secondary 同笔触）+ painterly 球场夜景 + bat-pose 锁定 + `--ar 3:4 --stylize 250`。
> 这一张差异化在：**调色（Yankee Stadium 火焰橙红 + 黑，跟 Judge 同队但完全不同气质）+ 动作（mid-swing 暴力 follow-through，跟 Judge 的 post-contact stoic 反向）+ 数据栏（速度 + EV）**。

## 决策（为什么选 Stanton 配 暴力挥棒 / Bat Tracking 王）

- 第三刀（2024 年 5 月）公开 Bat Tracking 后 Stanton 直接成为新指标 poster boy
- **2024 swing speed 81.5 mph** = MLB 全联盟最快，远高于联盟平均 71 mph
- **122.4 mph max EV** = Statcast 时代史上第二高（Stanton 自己保持着第一）
- 2017 NL MVP（59 HR with Marlins，过去 25 年单季 HR 数前列）
- 2024 ALCS MVP（季后赛轰 7 支 HR 关键期助 Yankees 进 WS）
- **跟 Judge 同 Yankees + 同体型，必须靠调色 + 动作完全反向才能区隔**：
  - Judge → 朱红日落 + post-contact stoic 静止
  - Stanton → 火焰橙红炸裂 + mid-swing 暴力动态

## 海报文字

| 层级 | 文字 |
|---|---|
| ① 主标 | `暴力` |
| ② 国际副标 | `STANTON` |
| ③ Tag line（顶）| `MLB 最快挥棒` |
| ④ Credits（底）| `挥棒 81.5 mph · EV 122 mph · 59 HR 单季` |

数据来源：81.5 mph = 2024 MLB swing speed 最快值（Bat Tracking 公开后第一组数据）/ 122 mph = Stanton 历史最大 EV（Statcast 时代史上第二，仅次于他自己的更早纪录）/ 59 HR = 2017 NL MVP 季单季 HR 数。

## 锁定动作 — Mid-Swing Brutal Follow-Through（暴力定格）

跟 Judge 的 post-contact 静止反向 — 这是**球刚被砸出去的动态瞬间**，整个躯干扭过、肌肉紧绷、bat 横扫过左肩的暴烈一刻。

- **接触刚发生**（球刚离棒，画面里看不到球但能感觉到刚被打飞）
- **球棒**：双手仍握，bat 已经**横扫过身体到左侧**（右打者，所以挥棒后 bat 落到左边），棒头指向画面**左下** 7 点钟方向（finish 位置低，跟 Judge 的高位完全不同）
- **躯干**：完全扭转过来，**胸口对画面右下**（hips 已 over-rotate），从原本 closed stance 拧成 fully open
- **重心**：完全在前脚（左脚），后脚（右脚）**脚跟离地、脚尖只剩一点点接触**像 spinning 状态
- **手臂**：双臂伸展到最大延伸（full extension），二头肌 + 三角肌 紧绷可见
- **头部 / 视线**：head turned to camera-right and slightly up，眼睛 hard-locked 跟着球飞出去的方向（画面右上出框 — 跟 Judge 一样轨迹但表情不同）
- **表情**：**jaw clenched + 嘴微开 + 牙齿露出一点点 + 鼻孔翕张 + 眉头拧紧** — 这是发力痕迹未消的"刚刚屠杀了一颗棒球"的表情，**绝对不要 stoic** — Stanton 是 violence personified
- **构图**：腰部以上，figure 占画布约 60%（动作大、覆盖面广）

## Visual Anchors（必须有的识别度）

- 6'6" / 245 lbs **massive 体型**（跟 Judge 同级别巨人 — 但 Stanton 比 Judge 略矮 1 英寸、肩膀略窄一点）
- 黑发 + **full thick dark beard**（比 Judge 的胡子明显更浓密 / 更野）
- Latin / 黑人混血五官（Stanton 父亲非裔美籍 + 母亲爱尔兰 + 波多黎各裔）— 偏深的肤色、宽鼻梁、明显的颧骨线
- **右打、右投**（跟 Judge 一样）
- 球衣号 **27**（不是 99！— 这是跟 Judge 区分的关键）
- **Yankees 主场球衣**：白底 navy pinstripes + navy 联锁 NY 胸标 — **跟 Judge 同款**，所以队长 C 字章 ⚠️ **不画**（Stanton 不是队长，那是 Judge 的标志）
- 头盔：navy Yankees 头盔 + 白色 NY 正面 logo

## Person Recognition Gate

```json
[{"person": "Giancarlo Stanton", "confidence": 80, "tier": "HIGH", "reason": "2017 NL MVP, 2× All-Star, 2024 ALCS MVP, MLB record exit velocity holder, 6'6'' massive frame and full beard make likeness deeply trained although less hyper-recognizable than Judge", "anchors_suggestion": null}]
```

→ HIGH 直接用名字。**重点**：和 Judge 同队同体型同款球衣 — 必须靠 27 号 + 没有 C patch + 更野胡子 + 暴力动作来区分。

---

## Final Prompt — 3/4 ESPN angle

```text
Japanese sports cinema poster illustration, 3:4 vertical, in the style of contemporary Japanese sport-movie key art (e.g. "100m" / "The First Slam Dunk" theatrical posters) — single hero, monumental composition, dominant fire-orange flame atmospheric background over Yankee Stadium night, kinetic violence rather than stillness, ALL TITLES BAKED INTO THE POSTER.

CAMERA ANGLE: approximately 30 to 45 degrees off-axis from a straight pitcher's-view, positioned on the third-base side photographer pit. Three-quarter view of the batter — face partially visible looking toward camera-right and upward (toward the ball flying out), the dynamic body twist of an over-rotated power swing clearly visible.

POSE (locked) — Mid-Swing Brutal Follow-Through: Giancarlo Stanton frozen in the violent moment just AFTER contact — the ball has just been crushed off the bat. As a right-handed batter who has swung through with maximum violence, his body is fully torqued, hips over-rotated past 90 degrees, chest now pointing toward the camera-right-and-down. Both hands still grip the bat which has WHIPPED THROUGH and is now FINISHING LOW ON THE LEFT SIDE — bat barrel angled toward the lower-left of the frame at roughly 7 o'clock (low finish position, unlike a calm high-finish admiring stance). Front (left) foot fully planted with weight transferred completely onto it; back (right) foot's heel is lifted with only the toe ball touching the ground, body in spinning kinetic state. Both arms at full extension through the swing — biceps, deltoids, and forearms visibly engaged and tensed. Head turned to camera-right and slightly upward, eyes hard-locked on the unseen ball flying toward the upper-right of the frame. Facial expression of raw violent effort — jaw clenched, mouth slightly open with teeth visible, nostrils flared, brow knitted in strain. NOT a stoic admiring face — this is the post-impact aftershock face of a man who just murdered a baseball at 122 mph. Framed from waist up, large figure occupies ~60% of canvas height.

CHARACTER (Giancarlo Stanton, locked): towering 6'6'' / 245 lbs massive frame with broad shoulders dominating the frame (slightly less wide than Aaron Judge's silhouette but still huge). Dark complexion (Black + Puerto Rican + Irish heritage), broad nose bridge, prominent cheekbones, FULL THICK DARK BEARD — fuller and slightly wilder than typical, an unmistakable Stanton trait. Wearing classic New York Yankees home uniform — vertical pinstripe white jersey with navy interlocking "NY" on the left chest, jersey number 27 visible on left sleeve. CRITICAL: NO captain's "C" patch (that is Judge's marker, Stanton is not the captain). Navy Yankees batting helmet with white interlocking NY logo on the front. Dark wood bat. Likeness recognizably Giancarlo Stanton — distinct from Aaron Judge by the fuller beard, slightly broader nose, and number 27.

STYLE — POSTER ILLUSTRATION: hand-illustrated key art quality with thick black contour outlines on the figure, soft poster-paint cel shading, slight grain texture overlay. Variable-weight black ink lines emphasized on the silhouette and tensed muscle / fabric strain. KINETIC sense — slight implied motion blur on the bat barrel (very subtle, cel-shaded blur not photographic) suggesting the violent speed of the swing. Limited tonal range — each form rendered in three values (light / mid / shadow). Subtle textured brush noise across flat color fills.

BACKGROUND — Yankee Stadium Night with Fire-Orange Flame Atmosphere (painterly, NOT photo): the same Yankee Stadium at night as Judge's poster, BUT the atmospheric color is RADICALLY DIFFERENT — instead of Judge's calm crimson sunset, the entire surrounding atmosphere glows with INTENSE FIRE ORANGE-RED, as if the air itself is heated and crackling from the violence of the swing. Deep navy / black sky in the upper corners fades into intense fire-orange / crimson-orange in the mid-canvas, concentrated in a halo around the figure (suggesting the heat and explosion of a 122 mph contact). Across the upper third, a faint silhouette of Yankee Stadium's iconic white frieze (the scalloped upper-deck arch) running horizontally, rendered as a faint cream-colored architectural shape, partly obscured by the orange glow. NO individual fans, NO scoreboard text, NO photo realism. The atmosphere is painterly, moody, and incandescent — like a Japanese movie poster painted with the heat of a bomb going off.

COLOR PALETTE (locked): fire orange-red flame glow (dominant ~50%) + deep navy-black sky (~25%) + cream-white frieze accent + Yankees pinstripe white + navy uniform (uniform only) + black ink contours + warm skin tone + brushed off-white text. Eight values total. Notice: NO calm crimson sunset (that's Judge's palette) — Stanton's palette is HOTTER, more orange, more aggressive.

POSTER TEXT LAYOUT (modeled on Japanese cinema posters; bilingual title block must read as ONE poster designer's matched typography):

- ① MAIN TITLE — the two Simplified Chinese characters "暴力" rendered in massive bold brush-stroke calligraphic poster typography, off-white / cream color with subtle paper-grain distress along the edges. Largest text element, occupying ~30% of canvas width. Position: upper-middle, just above the figure's helmet. Both Han characters accurately formed and legible.

- ② INTERNATIONAL SUBTITLE — the English word "STANTON" rendered immediately below the "暴力" title, in a heavy condensed serif or chunky display typeface that VISUALLY MATCHES the "暴力" treatment (same off-white color, same brush-textured edges, similar visual weight per glyph). Sized ~50% the width of "暴力". Together they form one unified bilingual title block.

- ③ TAG LINE — the Simplified Chinese phrase "MLB 最快挥棒" placed at the very top of the canvas as a thin centered tag, in a simple light-weight sans-serif with slight letter-spacing, soft white. Functions as the "catchphrase" line.

- ④ STATS LINE — "挥棒 81.5 mph · EV 122 mph · 59 HR 单季" centered along the bottom 6% of the canvas, in a thin tabular sans-serif, soft white, smaller than the tag line.

All text rendered crisply and fully legibly. Simplified Chinese characters accurately formed (not garbled). Hierarchy: 暴力 > STANTON > MLB 最快挥棒 ≈ stats.

EMOTION: kinetic violence, the aftershock of brutal force, raw explosive power — the moment AFTER a 122 mph contact when the air still vibrates from the impact. Like a Japanese movie poster announcing a martial-arts protagonist's signature finishing strike.

--ar 3:4 --stylize 250
```

## 跑图建议
- 跑 2-4 张
- 评分维度：
  - 动作：mid-swing follow-through 低位 finish（bat 在左下，**不是高位 admiring 姿势** — 那是 Judge）
  - 表情：**jaw clenched + 嘴张 + 牙露 + 鼻孔翕张** — 是发力痕迹未消的"刚屠杀了棒球"，不是 stoic
  - 球衣号 **27**（不是 99）+ **没有** C 字章（Stanton 不是队长）
  - 胡子比 Judge 明显更浓密
  - 火焰橙红主导（不是朱红日落 — 那是 Judge）
  - 暴力 + STANTON 字型统一笔触
- 不要动：
  - 动作（不要换成 pre-pitch / mid-stance / 静止 — 那不能传达"暴力挥棒"）
  - 调色（火焰橙红 ≠ Judge 的朱红日落，必须强烈区隔）
  - 球衣号 27 + 无 C patch（这是跟 Judge 的视觉差异核心）
  - 表情野性（Stanton 是 violence personified，不是 stoic judge）

## 系列差异化总览（Judge / Stanton 同队同体型，必须区分）

| | Judge | Stanton |
|---|---|---|
| 球衣号 | 99 | 27 |
| 队长章 | C 在左胸 | **无** |
| 胡子 | 修齐 | **更野更浓** |
| 动作 | post-contact bat-watching（高位 finish）| mid-swing brutal（低位 finish）|
| 表情 | stoic 笃定 | 发力痕迹 + 牙露 + jaw clenched |
| 调色 | 朱红日落（calm sunset glow）| **火焰橙红炸裂**（incandescent flame）|
| 主标 | 法官 | 暴力 |
| 副标 | JUDGE | STANTON |
| Tag | MLB 最强打者 | MLB 最快挥棒 |
| 数据 | 62 HR · 11.4 WAR · 2× MVP | 81.5 mph · 122 mph EV · 59 HR |

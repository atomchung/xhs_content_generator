# 村上宗隆 MURAKAMI 封面 prompt v1 — 100m-poster + White Sox 黑白高反差

## 决策

- 风格：100m-poster（朱日漫电影海报）— 沿用上篇 `2026-05-01-moneyball-baseball-analytics-evolution` 4-cover 系列同款风格池（视觉宪法第 1 条：账号默认走漫画 / 卷封 / 名场面）
- 输出方式：直接按海报格式输出，主标 + 副标 + tag + credits 全部 baked into the image，不走后期叠字
- 镜头：投手视角 frontal — 让 White Sox 黑色 "Sox" diamond 胸标 + 球衣号 5 + 左打 cocked 站姿一次全显
- Person Recognition Gate：MED tier 68 → 文字 anchors 必须落进 prompt 内 character description（不 embed 照片，不写 photoreal — 视觉宪法第 3 条）
- 跟上篇 Aaron Judge cover 的色调切割：上篇 Yankees navy + 朱红日落（暖色系），这张 White Sox 黑 + 白 + 银灰（冷色系工业 monochrome），swipe 上一眼可分

## 海报文字（v1，按 100m-poster 模板）

| 层级 | 文字 | 在 100m 海报里相当于 | 字型规格 |
|---|---|---|---|
| ① 主标（最大）| `村上` | 日文 kanji 主标 | brushed 厚重笔触 + 极轻微纸纹质感 + 米白 / off-white（在黑底上） |
| ② 国际副标 | `MURAKAMI` | 英文国际版片名 | heavy condensed display 字型，**和「村上」同样的笔触 / 质感**（统一 distress 边缘、统一颜色） |
| ③ Tag line（顶）| `飞球革命 — 打向天空的强打者` | 海报顶部宣传 tag | 简单 thin sans-serif，少量字间距撑开，淡白色 |
| ④ Credits 行（底）| `13 HR · 65 HR PACE · BARREL 99% · K 33%` | 演职员表 / 数据补充 | tabular 风格 thin sans，比 tag 还小 |

**关键**：① 和 ② 必须看起来像**同一张海报的同一组排版师做的**（统一笔触 / 统一描边 / 统一磨砂质感）。不能一个走毛笔、一个走 Helvetica。

数据来源：13 HR / 65 HR pace = 2026 球季前 32 场（截 5 月 2 日 MLB.com 报道）/ Barrel rate 23.5% = MLB 99 百分位（baseballsavant）/ K% 33% = 4 月底报道。

---

## 固定动作 — Pre-Pitch Cocked Stance（左打 upright）

不是挥击瞬间，是"准备开炮前一秒"的紧绷静止 — 像 100m 海报里的 pre-race 起跑前定格。

- **站姿**：upright（直立不弯腰），重心居中，等待投手出手前的静止
- **左打 batter's box**：左肩朝向投手（画面右侧 = 投手方向）
- **球棒**：双手高位握住，球棒在右肩后方 cocked，棒头向上、向后偏；棒身延伸出画面左上角
- **头部 / 视线**：脸朝画面右（朝投手），双眼锁住投手出手点；下颚微收
- **表情**：嘴闭、stoic — 不笑、不张牙、不咬牙；招牌"无表情专注"
- **脚**：双脚分开比肩稍宽，脚尖朝内（前脚轻微 closed stance），后脚扎实
- **气场**：coiled stillness — 静中蓄爆

## Visual Anchors（必须有的识别度，已写入 prompt 内）

- 188 cm / 厚实壮硕体型，肩膀宽
- 圆脸 / baby face 婴儿肥但下颌线有力
- 浓眉、双眼皮、专注眼神（不开嘴笑）
- 黑色短发，自然偏分，发量厚
- White Sox 主场白色球衣（**无 pinstripe，纯白 base**）+ 黑色 "Sox" Old English diamond wordmark 胸标
- 黑色棒球帽 + 白色 Old English "Sox" diamond 商标
- 球衣号 **5** 黑底白字（左袖）
- 深色木球棒（Mizuno 系，棒身偏深）

## Person Recognition Gate

```json
[{
  "person": "Murakami Munetaka 村上宗隆",
  "confidence": 68,
  "tier": "MED",
  "reason": "2022 NPB Triple Crown / 56 HR 破王贞治 1964 单季纪录、2026 White Sox 首秀且 5 月单独领跑 MLB HR；日 / 台媒体饱和但西方 AI 训练面部识别仍在中段",
  "anchors_suggestion": "188 cm 厚实壮硕 / 圆脸 baby-face 但下颌线有力 / 浓眉双眼皮 / 黑色短发偏分 / 嘴闭 stoic 专注 / 左打 upright 站姿 / 球棒高位 cocked 在右肩后方 / White Sox 纯白主场衣 + 黑 Sox diamond 胸标 / 球衣号 5 / 黑色 Sox helmet"
}]
```

→ MED，必须在 prompt 内 character description 段嵌入文字 anchors（下方 Final Prompt 已包含全部 8 项）。

---

## Final Prompt

```text
Japanese sports cinema poster illustration, 3:4 vertical, in the style of contemporary Japanese sport-movie key art (e.g. "100m" / "The First Slam Dunk" theatrical posters) — single hero, monumental composition, high-contrast black / white / cold-silver palette, cinematic stillness, ALL TITLES BAKED INTO THE POSTER.

CAMERA ANGLE: directly from the pitcher's mound looking back at home plate — fully frontal view of the left-handed batter. Munetaka Murakami's body is squared up toward camera with his chest, helmet front, and left-chest "Sox" diamond emblem all visible facing the viewer. Because he bats left, his left shoulder is rotated slightly toward camera-right (where the unseen pitcher would stand if this view were reversed; here the camera IS the pitcher's POV).

POSE (locked): Munetaka Murakami in PRE-PITCH cocked batting stance — the still moment BEFORE the swing, not the swing itself. Standing upright in the batter's box (he does NOT crouch), weight evenly distributed, feet shoulder-width apart with a slightly closed front stance, front toe turned slightly inward. Both hands grip the bat held high, cocked behind his right shoulder (camera's left side from this frontal POV), bat barrel angled up and slightly back, the bat extending out of the upper-left corner of the frame. Head turned to face camera-right (toward the imagined release point), chin tucked slightly, eyes laser-locked forward. Mouth firmly closed, jaw set, stoic blank focus — NO snarl, NO smile, NO open mouth — his signature flat intensity. Framed from waist up, figure centered, ~50% of canvas height (poster proportions reserve title space above and below). The atmosphere of the pose is "one second before detonation" — coiled stillness, not motion. NO motion blur, NO swing arc, NO follow-through.

CHARACTER (Munetaka Murakami): towering 188cm thick muscular build with broad shoulders that dominate the frame width, round baby-face cheeks paired with a strong defined jawline, thick black eyebrows, double-eyelid focused dark eyes shaded under the helmet brim, thick black short hair with a natural side part visible at the sideburns. Wearing the classic Chicago White Sox home uniform — solid white jersey (NO pinstripes, fully plain white base) with the iconic black Old English "Sox" diamond wordmark across the left chest, jersey number "5" visible in black on the left sleeve. Black Chicago White Sox batting helmet with the white Old English "Sox" diamond logo on the front. Dark walnut wood bat, slim Mizuno-style barrel. Likeness recognizably Munetaka Murakami.

STYLE — POSTER ILLUSTRATION: hand-illustrated key art quality with thick black contour outlines on the figure, soft poster-paint cel shading, slight grain texture overlay. The figure has a noble-statue stillness rather than dynamic motion blur. Limited tonal range — each form is rendered in three values (light / mid / shadow). Subtle textured brush noise across flat color fills. Variable-weight black ink on key contours.

BACKGROUND — Chicago South Side industrial dusk (painterly, not photo): stylized evening atmosphere of the Chicago South Side rendered as a moody poster painting. Deep charcoal-black sky dominating the upper half, transitioning to a cold steel-silver glow along the horizon line (industrial dusk + stadium lights bleed). Across the upper third, a soft silhouette of a generic Chicago South Side skyline running horizontally — distant tall building shapes on the far left, smaller industrial / stadium structures on the right — rendered as faint silver-gray architectural shapes, NOT a detailed crowd. Below that, the suggestion of a dark outfield wall with a subtle, slightly weathered painted "Sox" diamond just barely visible in darker black-on-charcoal — present but not dominant. NO individual fans, NO scoreboard text, NO flash dots, NO photo realism, NO red accents, NO green accents. The atmosphere is painterly and moody, like a Japanese movie-poster painted backdrop. The cold steel-silver stays as an ATMOSPHERIC ACCENT (industrial dusk / glow, ~20% of canvas), not the dominant field.

POSTER TEXT LAYOUT (v1 — modeled on Japanese cinema posters such as the 2024 Japanese film "100m" poster):

The text hierarchy here is the OPPOSITE of a Western banner: the Chinese characters are the dominant title, the English is the international subtitle. CRITICAL: the Chinese characters "村上" and the English word "MURAKAMI" must share the SAME visual treatment — same brush-textured edge, same heavy weight, same color, same slight grain / distress — so they read as ONE bilingual title block designed by the same poster designer, not two mismatched fonts pasted together.

- ① MAIN TITLE — the two Simplified Chinese characters "村上" rendered in massive bold brush-stroke calligraphic poster typography, off-white / cream color with subtle paper-grain distress along the edges (Japanese-poster brushed-kanji feel). This is the largest text element in the poster, occupying about 30% of canvas width. Position: upper-middle of the canvas, sitting just above the figure's helmet. Both Han characters must be accurately formed and legible.

- ② INTERNATIONAL SUBTITLE — the English word "MURAKAMI" rendered immediately below the "村上" title, in a heavy condensed serif or chunky display typeface that VISUALLY MATCHES the "村上" treatment (same off-white color, same brush-textured / slightly distressed edges, similar visual weight per glyph). Sized at roughly 55% the width of the "村上" title above. The two together form one unified bilingual title block.

- ③ TAG LINE — the Simplified Chinese phrase "飞球革命 — 打向天空的强打者" placed at the very top of the canvas (above ① ②) as a thin centered tag, in a simple light-weight sans-serif with slight letter-spacing, soft white. Functions as the "catchphrase" line at the top of a Japanese movie poster.

- ④ STATS / CREDITS LINE — "13 HR · 65 HR PACE · BARREL 99% · K 33%" centered along the bottom 6% of the canvas, in a thin tabular sans-serif, soft white, smaller than the tag line above. Functions as the credits / billing block at the bottom of a Japanese movie poster.

All text rendered crisply and fully legibly. Simplified Chinese characters accurately formed (not garbled). Hierarchy from most-to-least dominant: 村上 > MURAKAMI > 飞球革命 — 打向天空的强打者 > stats line.

COLOR PALETTE (locked): White Sox black (dominant, ~50% of canvas — sky + outfield wall + helmet + jersey "Sox" wordmark + bat) + cold steel-silver glow (~20% — industrial dusk accent at horizon + skyline silhouettes) + uniform white (~15% — jersey body) + warm Asian skin tone + brushed off-white text + thin black ink contours. Six values total. EXPLICITLY NO: Yankees navy, NO crimson, NO red, NO Yakult red-green, NO Tigers orange, NO Blue Jays royal — this palette must read as "Chicago South Side industrial monochrome", visually distinct from the previous Aaron Judge poster (which used Yankees navy + crimson sunset).

EMOTION: monumental, cinematic, restrained power — the coiled second BEFORE the decisive swing. Like a Japanese sport-movie poster announcing the protagonist's quiet menace. He is "about to detonate" and the viewer feels it without any motion in the image.

--ar 3:4 --stylize 250
```

---

## 如果要继续改

- **背景优先改什么**：如果 "Chicago South Side skyline" 渲染太具象 / 出现错误地标，改成 "generic American industrial dusk skyline silhouette, cold gray steel-mill silhouettes"
- **如果脸部识别度不够**（村上 MED tier，最大风险）：在 character description 段加 "specifically resembling Murakami Munetaka, the Japanese baseball star — round face, baby cheeks, strong jaw, thick brows, double-eyelid eyes, intense flat stare"，再不行就 fallback 跑 photo pipeline（Wikipedia API → Read 图 → 文字 anchors 加更多细节）
- **如果他变成挥击姿势**：强化 "PRE-pitch, NOT swinging, NO bat motion, bat held still high behind shoulder" 的限定语
- **不要动**：
  - ① ② 主副标 baked-in 不能拿掉
  - Visual Anchors 8 项必须全在
  - palette 锁定黑 / 白 / 银三色（**绝不加红 / 绿**，跟 Yakult / Tigers / Blue Jays / Rangers 完全切开）
  - "no photoreal / no reference photo / no octane render" 关键词不能出现（视觉宪法第 3 条）
  - --ar 3:4 --stylize 250 必须保留

## 跟上篇 Judge cover 的差异化（防呆）

| | Aaron Judge（上篇 cover）| Murakami（这张）|
|---|---|---|
| 球队 | Yankees | White Sox |
| 主色调 | Yankees navy + 朱红日落 | 黑 + 白 + 冷银灰 |
| 时间感 | 暮色暖光（hot sunset）| 工业冷夜（cold industrial dusk）|
| 动作 | post-contact 高位 follow-through | pre-pitch 高位 cocked（静态蓄势）|
| 表情 | stoic 笃定（已经知道这球没了）| stoic 专注（即将开炮）|
| 主标 kanji | 法官 | 村上 |
| 国际副标 | JUDGE | MURAKAMI |
| 数据栏 | 62 HR · 11.4 WAR · 2× AL MVP（career 历史数）| 13 HR · 65 HR PACE · BARREL 99% · K 33%（2026 当代时事数）|

→ 两张同摆 swipe 上：色调互斥（暖 vs 冷）、动作互斥（after vs before）、数据互斥（career vs current pace），不会撞脸。

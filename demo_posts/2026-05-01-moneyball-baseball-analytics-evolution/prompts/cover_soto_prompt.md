# Juan Soto 系列封面 prompt — 上垒教皇 OBP 王

> 系列规则继承 Judge `cover_prompt.md` v4：100m 海报双语标题排版（kanji 主导 / 英文 secondary 同笔触）+ painterly 球场夜景 + bat-pose 锁定 + `--ar 3:4 --stylize 250`。
> 这一张差异化在：**调色（教皇紫 + 金）+ 动作（pre-pitch focused stance）+ 数据栏（OBP 王口径）**。

## 决策（为什么选 Soto 配 OBP 王）

- 第一刀 sabermetrics 拆掉打击率 → 上垒率 OBP — Soto 是 Beane 派遗产的最完美现役执行者
- 25 岁职业生涯 OBP 已经 ~.421（历史前 20，跟 Frank Thomas / Stan Musial 同列）
- 2024 MLB BB 王（129 个保送）
- 频繁跳队（Nationals → Padres → Yankees → Mets，2024 末签 $765M / 15 年史上最大合约），所以**调色不绑球队，走 abstract 神格化** — 教皇紫 + 金

## 海报文字

| 层级 | 文字 |
|---|---|
| ① 主标 | `教皇` |
| ② 国际副标 | `SOTO` |
| ③ Tag line（顶）| `MLB 上垒教皇` |
| ④ Credits（底）| `.421 OBP · 2024 BB 王 · .989 OPS` |

数据来源：.421 = 职业生涯 OBP（截至 2024 末，Mets 签约前夕）/ 129 BB = 2024 MLB 保送王 / .989 = 2024 OPS。

## 锁定动作 — Pre-Pitch Focused Stance（教皇式 cerebral 静止）

跟 Judge 的"球已飞出后的 stoic"反向 — 这是**球还没投出前的 cerebral 计算**。Soto 全联盟最辨识的不是挥棒，是他**站在打击区里研究投手的眼神** — "你投什么我都知道"的 OBP 王特质。

- **接触尚未发生**，pitcher windup 中
- **球棒**：双手握，举到右肩高度（左打者）后侧高位 cocked，棒头略向后指（10 点钟方向）
- **躯干**：左肩对着 pitcher（左打站位），3/4 转向 camera-right
- **重心**：分布均衡，前脚（右脚）抬起一点点准备 stride
- **头部 / 视线**：head turned to camera-right (toward pitcher), 眼神 laser locked, 微微挑眉，**slight smirk / defiant focus** — 这是 Soto 招牌的"我看穿你了"表情
- **不要做 Soto Shuffle 的 swaying 动作** — 那个动起来不适合海报，要静止瞬间
- **构图**：腰部以上，figure 占画布约 50%

## Visual Anchors（必须有的识别度）

- 6'2" / 224 lbs lean-power 体型，肩宽强壮但比 Judge / Stanton 苗条
- 修剪过的黑色短胡 + 短黑发（头盔下露一小段）
- 多明尼加裔 Latin 五官，方下颌但比 Judge 圆润
- **左打、左投**（球棒在右肩侧、左手在下握）
- 球衣号 **22**
- **Mets 主场球衣**：白底 + 细 navy + orange 双色斑点 pinstripes（Mets 的 pinstripes 不是单色），navy "Mets" cursive script 在左胸 + 小 orange 描边
- 头盔：navy + orange 双色，正面白色 "NY" interlocking logo（Mets 版，跟 Yankees 的 NY 不同 — Mets 的 N 和 Y 字型更圆 / 套色不同）
- ⚠️ 不要画成 Yankees navy 头盔 — 现在是 Mets

## Person Recognition Gate

```json
[{"person": "Juan Soto", "confidence": 85, "tier": "HIGH", "reason": "5x All-Star, 2019 WS champion, 4 MVP top-5 finishes by age 25, $765M record contract Dec 2024 made global headlines, distinctive 'Soto Shuffle' makes likeness deeply trained", "anchors_suggestion": null}]
```

→ HIGH 直接用名字。

---

## Final Prompt — 3/4 ESPN angle

```text
Japanese sports cinema poster illustration, 3:4 vertical, in the style of contemporary Japanese sport-movie key art (e.g. "100m" / "The First Slam Dunk" theatrical posters) — single hero, monumental composition, dominant regal-purple atmospheric background with cathedral gold light shaft, cinematic stillness, ALL TITLES BAKED INTO THE POSTER.

CAMERA ANGLE: approximately 30 to 45 degrees off-axis from a straight pitcher's-view, positioned on the first-base side photographer pit. Three-quarter view of the batter — face partially visible looking toward camera-right (toward where the pitcher would be), body twist visible.

POSE (locked) — Pre-Pitch Focused Stance: Juan Soto in his signature cerebral pre-pitch focus moment — the pitcher is in windup, the ball has NOT yet been thrown. As a left-handed batter, his left shoulder points toward the pitcher (camera-right). Both hands grip the bat which is cocked back over his right shoulder at high-load position, the bat barrel angled slightly backward toward the upper-left of the frame at roughly 10 o'clock. Body weight balanced, front (right) foot lifted just slightly preparing to stride forward. Head turned sharply to camera-right, eyes laser-locked on the pitcher (off-frame), with a subtle confident smirk / defiant focus — the look of a hitter who sees the pitch coming before it's thrown. Jaw set, eyebrows slightly raised. Body relaxed but coiled with kinetic potential. Framed from waist up, figure occupies ~50% of canvas height.

CHARACTER (Juan Soto, locked): athletic 6'2'' lean-power frame, broad shoulders but slimmer than Judge or Stanton, trimmed black beard, short black hair under helmet, Dominican Latin features, square but slightly rounded jaw. Wearing New York Mets home uniform — white jersey with navy + orange double-color thin pinstripes, navy script "Mets" cursive wordmark with thin orange outline across the left chest, jersey number 22 visible on left sleeve. Mets batting helmet — navy with an orange brim, white interlocking "NY" Mets logo on the front (the rounded Mets-style NY, not the Yankees angular NY). Dark wood bat. Likeness recognizably Juan Soto.

STYLE — POSTER ILLUSTRATION: hand-illustrated key art quality with thick black contour outlines on the figure, soft poster-paint cel shading, slight grain texture overlay. Noble-statue stillness rather than dynamic motion. Limited tonal range — each form rendered in three values (light / mid / shadow). Subtle textured brush noise across flat color fills. Variable-weight black ink on key contours.

BACKGROUND — Regal Cathedral Atmosphere (painterly, abstract, NOT a literal stadium): deep regal purple field dominates the canvas (~50%) — rich royal purple / amethyst, painterly and slightly textured but mostly flat. From the upper-left corner, a single dramatic broad gold light shaft beams down at a 45-degree angle (cathedral / "papal blessing" feeling), illuminating the figure's right shoulder and helmet. The shaft fades into the purple field. Faint cathedral-window-style geometric divisions barely suggested in the upper corners (very subtle, nothing literal). NO stadium, NO crowd, NO horizon, NO scoreboard — this is a deliberately abstract neutral canvas appropriate for a player who has changed teams 4 times in 5 years. Slight grain across the full background.

COLOR PALETTE (locked): regal royal purple (dominant ~50%) + cathedral gold light shaft (~20%) + Mets navy + orange pinstripe accents (uniform only) + cream white jersey + warm Latin skin tone + black ink contours + brushed off-white text. Eight values total.

POSTER TEXT LAYOUT (modeled on Japanese cinema posters; bilingual title block must read as ONE poster designer's matched typography):

- ① MAIN TITLE — the two Simplified Chinese characters "教皇" rendered in massive bold brush-stroke calligraphic poster typography, off-white / cream color with subtle paper-grain distress along the edges. Largest text element, occupying ~30% of canvas width. Position: upper-middle, just above the figure's helmet. Both Han characters accurately formed and legible.

- ② INTERNATIONAL SUBTITLE — the English word "SOTO" rendered immediately below the "教皇" title, in a heavy condensed serif or chunky display typeface that VISUALLY MATCHES the "教皇" treatment (same off-white color, same brush-textured edges, similar visual weight per glyph). Sized ~50% the width of "教皇". Together they form one unified bilingual title block.

- ③ TAG LINE — the Simplified Chinese phrase "MLB 上垒教皇" placed at the very top of the canvas as a thin centered tag, in a simple light-weight sans-serif with slight letter-spacing, soft white. Functions as the "catchphrase" line.

- ④ STATS LINE — ".421 OBP · 2024 BB 王 · .989 OPS" centered along the bottom 6% of the canvas, in a thin tabular sans-serif, soft white, smaller than the tag line.

All text rendered crisply and fully legibly. Simplified Chinese characters accurately formed (not garbled). Hierarchy: 教皇 > SOTO > MLB 上垒教皇 ≈ stats.

EMOTION: cerebral, regal, calculating — the moment when the OBP king reads the pitcher's mind before the ball is thrown. Like a Japanese movie poster announcing a chess-master protagonist.

--ar 3:4 --stylize 250
```

## 跑图建议
- 跑 2-4 张
- 评分维度：
  - Mets 球衣 + helmet（不能误画成 Yankees）
  - 左打站位 + bat 在右肩 cocked（不能画成右打）
  - 教皇紫主导 ~50% + 金光从左上斜射
  - 表情有 "smirk / defiant focus"（不是 stoic 沉默 — 那是 Judge）
  - 教皇 + SOTO 字型笔触统一
- 不要动：
  - 调色（regal purple + cathedral gold）— 这是 Soto 跨球队的"神格化"识别
  - 背景 NO stadium（跟 Judge / Ichiro / Stanton 的球场背景区别开）
  - 文字层级（教皇 > SOTO > tag > stats）

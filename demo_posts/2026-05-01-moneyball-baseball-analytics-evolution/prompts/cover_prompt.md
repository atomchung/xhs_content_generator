# Aaron Judge 封面 prompt v3 — 100m-poster 锁定 + 投手视角 / 侧角双版

## 决策（v2 → v3）

- 风格已选定：**100m-poster（朱红日漫电影海报）** — 用户在 v2 4 风格中拍板
- 输出方式：**直接按海报格式输出**，标题 + 副标 baked into the image，不走后期叠字
- 出两个镜头版本（同一动作，不同角度）：
  - **V1 投手视角**（frontal）— 从投手丘看回本垒，Judge 身体正面对画
  - **V2 侧角**（3/4 角度）— ESPN highlight 经典角度，~30-45° off-axis 从三垒 photographer pit 方向看

## 海报文字（v4 — 参考 100m 海报排版）

v3 错在哪：把 JUDGE 当主标 + 法官当 accent，等于把英文当老大、中文当装饰 — 这是中文圈商业海报的逻辑，**不是 100m 海报逻辑**。100m 海报是「日文 kanji 才是主标，英文是国际副标，tag line 在上，credits 在下」。这次按 100m 模型重排：

| 层级 | 文字 | 在 100m 海报里相当于 | 字型规格 |
|---|---|---|---|
| ① 主标（最大）| `法官` | 日文 kanji 主标 | brushed 厚重笔触 + 极轻微纸纹质感 + 黑墨色 |
| ② 国际副标 | `JUDGE` | 英文国际版片名 | heavy condensed display 字型，**和「法官」同样的笔触 / 质感**（不是 clean 现代 sans，那样会和 kanji 不搭）|
| ③ Tag line（顶）| `MLB 最强打者` | 海报顶部宣传 tag | 简单 thin sans-serif，少量字间距撑开，淡白色 |
| ④ Credits 行（底）| `62 HR · 11.4 WAR · 2× AL MVP` | 演职员表 / 数据补充 | tabular 风格 thin sans，比 tag 还小 |

**关键**：① 和 ② 必须看起来像**同一张海报的同一组排版师做的**（统一笔触 / 统一描边 / 统一磨砂质感）。不能一个走毛笔、一个走 Helvetica。

数据来源：62 HR = 2022 AL 单季 HR 纪录 / 11.4 WAR = 2022 bWAR / 2× AL MVP = 2022 + 2024。

---

## 固定动作（V1 / V2 共用）— Bat-Watching Follow-Through

Judge 全联盟最辨识的 HR 后定格：

- **接触已发生**，球已离棒
- **球棒**：双手仍握、挥到左肩高度过头，棒头指向左上
- **躯干**：从打击站位转过来；V1 版正面对画，V2 版 3/4 转向画面右侧
- **重心**：完全在前脚，后脚跟微抬
- **头部 / 视线**：下颚抬、眼睛锁住球飞出去的方向（V1 上右、V2 上右；都跟着 ball 出框）
- **表情**：嘴闭、stoic — "我知道这球没了" 的笃定，不是欢呼

## Visual Anchors（两版共用，必须有的识别度）

- 6'7'' / 282 lbs 的高大身型 — 肩宽撑出画面
- pinstripe 白底主场球衣 + navy 联锁 NY 胸标
- 队长 **C 字章** 在左胸 NY 标上方（2022 起，**漏了不像 Judge**）
- 球衣号 **99** 在左袖
- navy Yankees 头盔 + 白色 NY 正面 logo
- full dark beard 修齐、方下颌

## Person Recognition Gate

```json
[{"person": "Aaron Judge", "confidence": 88, "tier": "HIGH", "reason": "Yankees captain since 2022, 2× AL MVP (2022, 2024), 8+ years mainstream coverage", "anchors_suggestion": null}]
```

→ HIGH，直接用名字。

---

## V1 — 投手视角（Frontal / Pitcher's POV）

Final Prompt：

```text
Japanese sports cinema poster illustration, 3:4 vertical, in the style of contemporary Japanese sport-movie key art (e.g. "100m" / "The First Slam Dunk" theatrical posters) — single hero, monumental composition, dominant crimson background, cinematic stillness, ALL TITLES BAKED INTO THE POSTER.

CAMERA ANGLE: directly from the pitcher's mound looking back at home plate — fully frontal view of the batter. Aaron Judge's body is squared up toward camera with his chest, helmet front, and left-chest "NY" emblem all visible facing the viewer.

POSE (locked): Aaron Judge in bat-watching follow-through stance — the swing is finished, the ball has just left the bat. From this pitcher's POV, his torso has rotated through and is now squared toward camera. Both hands still grip the bat, which has swung up and over his left shoulder; from the camera's perspective the bat is held high on the RIGHT side of the frame, barrel angled toward the upper-right corner. Front foot planted, back heel slightly lifted. Chin tilted up and slightly to his right (camera's left), eyes locked on the unseen ball flying toward the upper-right area of the frame. Jaw clenched, mouth closed, stoic focus. Framed from waist up, figure centered, ~50% of canvas height (poster proportions reserve title space above and below).

CHARACTER (Aaron Judge): towering 6'7'' frame with broad shoulders dominating the frame, full dark beard neatly trimmed, square jaw, focused dark eyes shaded under the helmet brim. Wearing classic New York Yankees home uniform — vertical pinstripe white jersey with navy interlocking "NY" on the left chest (visible on camera's right side from this frontal angle) and a small navy captain's "C" patch above the heart, jersey number 99 visible on left sleeve. Navy Yankees batting helmet with white interlocking NY logo on the front. Dark wood bat. Likeness recognizably Aaron Judge.

STYLE — POSTER ILLUSTRATION: hand-illustrated key art quality with thick black contour outlines on the figure, soft poster-paint cel shading, slight grain texture overlay. The figure has a noble-statue stillness rather than dynamic motion blur. Limited tonal range — each form is rendered in three values (light / mid / shadow). Subtle textured brush noise across flat color fills. Variable-weight black ink on key contours.

BACKGROUND — Yankee Stadium evening atmosphere (painterly, not photo): stylized night atmosphere of Yankee Stadium rendered as a moody poster painting. Deep navy blue sky dominating the upper half, transitioning to a warm crimson glow along the horizon line (sunset / stadium lights bleed). Across the upper third, a soft silhouette of Yankee Stadium's iconic white frieze (the scalloped upper-deck arched detail) running horizontally, rendered as a faint cream-colored architectural shape, NOT a detailed crowd. Below that, the suggestion of a deep navy outfield wall with a subtle, slightly weathered painted "NY" interlocking logo just barely visible in darker navy on the wall — present but not dominant. NO individual fans, NO scoreboard text, NO flash dots, NO photo realism. The atmosphere is painterly and moody, like a Japanese movie-poster painted backdrop. Crimson stays as an ATMOSPHERIC ACCENT (sunset / glow, ~25% of canvas), not the dominant field.

POSTER TEXT LAYOUT (v4 — modeled on Japanese cinema posters such as the 2024 Japanese film "100m" poster):

The text hierarchy here is the OPPOSITE of a Western banner: the Chinese characters are the dominant title, the English is the international subtitle. CRITICAL: the Chinese characters "法官" and the English word "JUDGE" must share the SAME visual treatment — same brush-textured edge, same heavy weight, same color, same slight grain/distress — so they read as one bilingual title block by the same poster designer, not two mismatched fonts pasted together.

- ① MAIN TITLE — the two Simplified Chinese characters "法官" rendered in massive bold brush-stroke calligraphic poster typography, off-white / cream color with subtle paper-grain distress along the edges (Japanese-poster brushed-kanji feel). This is the largest text element in the poster, occupying about 30% of canvas width. Position: upper-middle of the canvas, sitting just above the figure's helmet. Both Han characters must be accurately formed and legible.

- ② INTERNATIONAL SUBTITLE — the English word "JUDGE" rendered immediately below the "法官" title, in a heavy condensed serif or chunky display typeface that VISUALLY MATCHES the "法官" treatment (same off-white color, same brush-textured / slightly distressed edges, similar visual weight per glyph). Sized at roughly 50% the width of the "法官" title above. The two together form one unified bilingual title block.

- ③ TAG LINE — the Simplified Chinese phrase "MLB 最强打者" placed at the very top of the canvas (above ① ②) as a thin centered tag, in a simple light-weight sans-serif with slight letter-spacing, soft white. Functions as the "catchphrase" line at the top of a Japanese movie poster.

- ④ STATS / CREDITS LINE — "62 HR · 11.4 WAR · 2× AL MVP" centered along the bottom 6% of the canvas, in a thin tabular sans-serif, soft white, smaller than the tag line above. Functions as the credits / billing block at the bottom of a Japanese movie poster.

All text rendered crisply and fully legibly. Simplified Chinese characters accurately formed (not garbled). Hierarchy from most-to-least dominant: 法官 > JUDGE > MLB 最强打者 > stats line.

COLOR PALETTE (locked): Yankees navy (dominant, ~50% of canvas — sky + outfield wall) + atmospheric crimson glow (~25% — sunset accent at horizon) + cream-white frieze accent + pinstripe white + black ink contours + warm skin tone + brushed off-white text. Seven values total.

EMOTION: monumental, cinematic, restrained power — the quiet second AFTER the decisive moment. Like a Japanese sport-movie poster announcing the protagonist's signature move.

--ar 3:4 --stylize 250
```

---

## V2 — 侧角（3/4 view, ESPN highlight angle）

Final Prompt：

```text
Japanese sports cinema poster illustration, 3:4 vertical, in the style of contemporary Japanese sport-movie key art (e.g. "100m" / "The First Slam Dunk" theatrical posters) — single hero, monumental composition, dominant crimson background, cinematic stillness, ALL TITLES BAKED INTO THE POSTER.

CAMERA ANGLE: approximately 30 to 45 degrees off-axis from a straight pitcher's-view, positioned slightly toward the third-base side photographer pit. Three-quarter view of the batter — face partially visible, body twist clearly visible. This is the iconic ESPN baseball-highlight camera angle.

POSE (locked): Aaron Judge in bat-watching follow-through stance — the swing is finished, the ball has just left the bat. Body torqued through, torso rotated approximately three-quarters toward camera-right (toward where the pitcher's mound was). Both hands still grip the bat, which has swung up and over his left shoulder; from this 3/4 angle the bat barrel angles toward the upper-LEFT of the frame (his left = camera-left). Front foot planted, back heel slightly lifted, hips fully rotated. Chin tilted up, eyes locked on the unseen ball flying toward the upper-RIGHT of the frame (pull-side trajectory). Jaw clenched, mouth closed, stoic focus — the look of a man who already knows the ball is gone. Framed from waist up, figure occupies ~50% of canvas height with monumental presence.

CHARACTER (Aaron Judge): towering 6'7'' frame with broad shoulders dominating the frame, full dark beard neatly trimmed, square jaw, focused dark eyes shaded under the helmet brim. Wearing classic New York Yankees home uniform — vertical pinstripe white jersey with navy interlocking "NY" on the left chest and a small navy captain's "C" patch above the heart, jersey number 99 visible on left sleeve. Navy Yankees batting helmet with white interlocking NY logo on the front. Dark wood bat. Likeness recognizably Aaron Judge.

STYLE — POSTER ILLUSTRATION: hand-illustrated key art quality with thick black contour outlines on the figure, soft poster-paint cel shading, slight grain texture overlay. Noble-statue stillness rather than dynamic motion blur. Limited tonal range — each form rendered in three values (light / mid / shadow). Subtle textured brush noise across flat color fills. Variable-weight black ink on key contours.

BACKGROUND — Yankee Stadium evening atmosphere (painterly, not photo): stylized night atmosphere of Yankee Stadium rendered as a moody poster painting. Deep navy blue sky dominating the upper half, transitioning to a warm crimson glow along the horizon line (sunset / stadium lights bleed). Across the upper third, a soft silhouette of Yankee Stadium's iconic white frieze (the scalloped upper-deck arched detail) running horizontally, rendered as a faint cream-colored architectural shape, NOT a detailed crowd. Below that, the suggestion of a deep navy outfield wall with a subtle, slightly weathered painted "NY" interlocking logo just barely visible in darker navy on the wall — present but not dominant. NO individual fans, NO scoreboard text, NO flash dots, NO photo realism. The atmosphere is painterly and moody, like a Japanese movie-poster painted backdrop. Crimson stays as an ATMOSPHERIC ACCENT (sunset / glow, ~25% of canvas), not the dominant field.

POSTER TEXT LAYOUT (v4 — modeled on Japanese cinema posters such as the 2024 Japanese film "100m" poster):

The text hierarchy here is the OPPOSITE of a Western banner: the Chinese characters are the dominant title, the English is the international subtitle. CRITICAL: the Chinese characters "法官" and the English word "JUDGE" must share the SAME visual treatment — same brush-textured edge, same heavy weight, same color, same slight grain/distress — so they read as one bilingual title block by the same poster designer, not two mismatched fonts pasted together.

- ① MAIN TITLE — the two Simplified Chinese characters "法官" rendered in massive bold brush-stroke calligraphic poster typography, off-white / cream color with subtle paper-grain distress along the edges (Japanese-poster brushed-kanji feel). This is the largest text element in the poster, occupying about 30% of canvas width. Position: upper-middle of the canvas, sitting just above the figure's helmet. Both Han characters must be accurately formed and legible.

- ② INTERNATIONAL SUBTITLE — the English word "JUDGE" rendered immediately below the "法官" title, in a heavy condensed serif or chunky display typeface that VISUALLY MATCHES the "法官" treatment (same off-white color, same brush-textured / slightly distressed edges, similar visual weight per glyph). Sized at roughly 50% the width of the "法官" title above. The two together form one unified bilingual title block.

- ③ TAG LINE — the Simplified Chinese phrase "MLB 最强打者" placed at the very top of the canvas (above ① ②) as a thin centered tag, in a simple light-weight sans-serif with slight letter-spacing, soft white. Functions as the "catchphrase" line at the top of a Japanese movie poster.

- ④ STATS / CREDITS LINE — "62 HR · 11.4 WAR · 2× AL MVP" centered along the bottom 6% of the canvas, in a thin tabular sans-serif, soft white, smaller than the tag line above. Functions as the credits / billing block at the bottom of a Japanese movie poster.

All text rendered crisply and fully legibly. Simplified Chinese characters accurately formed (not garbled). Hierarchy from most-to-least dominant: 法官 > JUDGE > MLB 最强打者 > stats line.

COLOR PALETTE (locked): Yankees navy (dominant, ~50% of canvas — sky + outfield wall) + atmospheric crimson glow (~25% — sunset accent at horizon) + cream-white frieze accent + pinstripe white + black ink contours + warm skin tone + brushed off-white text. Seven values total.

EMOTION: monumental, cinematic, restrained power — the quiet second AFTER the decisive moment. Like a Japanese sport-movie poster announcing the protagonist's signature move.

--ar 3:4 --stylize 250
```

---

## 跑图说明

### 跑图建议
1. V1（投手视角）和 V2（侧角）各跑 2-4 张
2. 评分维度：
   - 姿势是不是 bat-watching follow-through（不是 mid-swing）
   - C patch / 99 / 头盔 NY / pinstripe 是否齐全
   - 背景：洋基球场夜场气场 — 深 navy 天 + 朱红日落辉 + frieze 剪影 + 微弱 NY 外野墙 logo（不是纯色块、不是详细人群）
   - 文字层级是否对：法官 最大、JUDGE 第二、MLB 最强打者 顶 tag、stats 底 credits
   - 法官 + JUDGE 是否字型质感统一（笔触 / 描边 / 颜色 / 磨砂感一致 — 不能一个毛笔一个 Helvetica）
   - 中文字形清晰、笔画完整（用户口径：完整保留简体中文，不会糊）
3. 两版气质对比：
   - V1 frontal → 庄严、像球员名片 / 海报正贴
   - V2 侧角 → 力量感更强、像 ESPN highlight 截屏的设计版

### 不要动的（铁律）
- 动作锁定 bat-watching follow-through
- 文字层级（v4 修正）：法官 > JUDGE > MLB 最强打者 > stats — kanji 主导、英文衬位
- 法官 + JUDGE 必须同笔触 / 同质感 / 同颜色（一组 bilingual title block）
- 背景元素：navy 主 + 朱红辅 + frieze 剪影 + 远处 NY 外野墙 logo（painterly，**not photo**）
- 中文用简体（最强 / 法官，不是 最強）
- `--ar 3:4 --stylize 250`
- 禁词：photoreal / photorealistic / 8k / octane / studio photo
- 这版**允许 prompt 内含文字**（baked-in 海报）— 是用户明确要求的特例，跟账号其他封面 prompt 内 NO TEXT 的默认相反，不要把这条习惯带回去

---

## 上一版（v2）4 风格变体备份

v2 跑过 4 个风格选最优：canonical-breakout / slam-dunk-classic / **100m-poster** / slam-dunk-movie。
v3 锁定 100m-poster。
完整 v2 4 风格 prompt 在 git 历史可查（commit 之前）。

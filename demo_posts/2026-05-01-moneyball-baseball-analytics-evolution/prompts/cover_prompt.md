# Aaron Judge 封面 prompt v3 — 100m-poster 锁定 + 投手视角 / 侧角双版

## 决策（v2 → v3）

- 风格已选定：**100m-poster（朱红日漫电影海报）** — 用户在 v2 4 风格中拍板
- 输出方式：**直接按海报格式输出**，标题 + 副标 baked into the image，不走后期叠字
- 出两个镜头版本（同一动作，不同角度）：
  - **V1 投手视角**（frontal）— 从投手丘看回本垒，Judge 身体正面对画
  - **V2 侧角**（3/4 角度）— ESPN highlight 经典角度，~30-45° off-axis 从三垒 photographer pit 方向看

## 海报文字（两版共用，baked-in）

| 位置 | 文字 | 备注 |
|---|---|---|
| 顶栏（小） | `MLB 最强打者` | 简体中文 |
| 副标（中下，Judge 上方）| `法官` | 简体中文 2 字，做日漫海报的大字效果 |
| 主标（大）| `JUDGE` | 英文大写 condensed bold，海报视觉中心 |
| 数据栏（最底） | `62 HR · 11.4 WAR · 2× AL MVP` | 英文 + 数字 |

数据来源：
- 62 HR = 2022 AL 单季 HR 纪录（破 Maris 1961 年 61 支）
- 11.4 WAR = 2022 bWAR，自 Babe Ruth 以来位置球员单季最高级别
- 2× AL MVP = 2022 + 2024 两届

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

DOMINANT COLOR: deep crimson red (vermillion / 朱) fills the entire background as a single flat field — no gradient, no detail, no horizon. The figure stands against this pure crimson plane with high-contrast separation. NO stadium, NO crowd, NO sky behind the figure.

POSTER TEXT LAYOUT (all text rendered as part of the poster image, baked-in, fully legible):
- TOP BAR: the Simplified Chinese line "MLB 最强打者" rendered crisply in clean white sans-serif, centered along the top 6% of the canvas. All five Chinese characters must be fully legible and properly formed.
- HAN CHARACTER ACCENT: the two Simplified Chinese characters "法官" rendered in a bold brushed poster-style typography (white with a thin black outline), placed prominently directly above the JUDGE wordmark — sized as a secondary headline, like a Japanese cinema poster's hand-brushed character accent. Both characters fully legible and properly formed.
- MAIN TITLE: the single English word "JUDGE" rendered in massive condensed bold sans-serif all-caps white with a thin black outline, positioned just above the figure's helmet, occupying ~25% of canvas width — this is the visual centerpiece text.
- BOTTOM STATS LINE: "62 HR · 11.4 WAR · 2× AL MVP" in clean white sans-serif, centered along the bottom 6% of the canvas.

All text is integral to the poster design, rendered crisply and fully legibly. The Simplified Chinese characters must be accurately formed (not garbled, not stylized into illegibility). Text hierarchy from largest to smallest: JUDGE > 法官 > MLB 最强打者 ≈ stats line.

COLOR PALETTE (locked): crimson red (~60% of canvas) + Yankees navy + pinstripe white + black ink + warm skin tone + small white text. Six values total.

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

DOMINANT COLOR: deep crimson red (vermillion / 朱) fills the entire background as a single flat field — no gradient, no detail, no horizon. The figure stands against this pure crimson plane with high-contrast separation. NO stadium, NO crowd, NO sky behind the figure.

POSTER TEXT LAYOUT (all text rendered as part of the poster image, baked-in, fully legible):
- TOP BAR: the Simplified Chinese line "MLB 最强打者" rendered crisply in clean white sans-serif, centered along the top 6% of the canvas. All five Chinese characters must be fully legible and properly formed.
- HAN CHARACTER ACCENT: the two Simplified Chinese characters "法官" rendered in a bold brushed poster-style typography (white with a thin black outline), placed prominently directly above the JUDGE wordmark — sized as a secondary headline, like a Japanese cinema poster's hand-brushed character accent. Both characters fully legible and properly formed.
- MAIN TITLE: the single English word "JUDGE" rendered in massive condensed bold sans-serif all-caps white with a thin black outline, positioned just above the figure's helmet, occupying ~25% of canvas width — this is the visual centerpiece text.
- BOTTOM STATS LINE: "62 HR · 11.4 WAR · 2× AL MVP" in clean white sans-serif, centered along the bottom 6% of the canvas.

All text is integral to the poster design, rendered crisply and fully legibly. The Simplified Chinese characters must be accurately formed (not garbled, not stylized into illegibility). Text hierarchy from largest to smallest: JUDGE > 法官 > MLB 最强打者 ≈ stats line.

COLOR PALETTE (locked): crimson red (~60% of canvas) + Yankees navy + pinstripe white + black ink + warm skin tone + small white text. Six values total.

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
   - 朱红色块是不是真的占画布 ~60%（不是稀释成粉红或暗红渐变）
   - 「JUDGE」英文主标大小 / 位置
   - 中文「MLB 最强打者」+「法官」字形清晰、笔画完整（用户口径：完整保留简体中文，不会糊）
3. 两版气质对比：
   - V1 frontal → 庄严、像球员名片 / 海报正贴
   - V2 侧角 → 力量感更强、像 ESPN highlight 截屏的设计版

### 不要动的（铁律）
- 动作锁定 bat-watching follow-through
- 朱红主色 ~60% 占比
- 文字层级 JUDGE > 法官 > MLB 最强打者 ≈ stats line
- 中文用简体（最强 / 法官，不是 最強 / 法官）
- `--ar 3:4 --stylize 250`
- 禁词：photoreal / photorealistic / 8k / octane / studio photo
- 这版**允许 prompt 内含文字**（baked-in 海报）— 是用户明确要求的特例，跟账号其他封面 prompt 内 NO TEXT 的默认相反，不要把这条习惯带回去

---

## 上一版（v2）4 风格变体备份

v2 跑过 4 个风格选最优：canonical-breakout / slam-dunk-classic / **100m-poster** / slam-dunk-movie。
v3 锁定 100m-poster。
完整 v2 4 风格 prompt 在 git 历史可查（commit 之前）。

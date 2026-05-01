# Ichiro Suzuki 系列封面 prompt — 安打王 Hit King

> 系列规则继承 Judge `cover_prompt.md` v4：100m 海报双语标题排版（kanji 主导 / 英文 secondary 同笔触）+ painterly 球场夜景 + bat-pose 锁定 + `--ar 3:4 --stylize 250`。
> 这一张差异化在：**调色（Mariners 深 navy + 西雅图 teal + 富士山红日）+ 动作（pre-pitch ritual 招牌）+ 数据栏（日美通算）**。

## 决策（为什么选 Ichiro 配 安打王）

- 第 0 代基础指标 BA / 安打 — 代表打击率撑了 100 多年那一段
- Ichiro 是日美棒球史上对"安打 / 接触"这一指标的极端化实践
- **262 H 单季纪录**（2004，至今未破）+ **4367 H 通算**（MLB 3089 + NPB 1278，吉尼斯世界纪录）+ **10 季连续 200+ H**（MLB 史上唯一）
- 2001 AL ROY + MVP 同年（MLB 史上仅 Fred Lynn 1975 也做到）
- 现役已退（2019），但 2025 名人堂首轮入选基本锁定 — 帖子上线时机刚好
- 调色对位：Mariners 深 navy + Pacific Northwest teal + 远景 Mt. Rainier 剪影 + **小红日（致敬 Japan，但克制不 kitsch）**

## 海报文字

| 层级 | 文字 |
|---|---|
| ① 主标 | `安打王` |
| ② 国际副标 | `ICHIRO` |
| ③ Tag line（顶）| `日美通算 安打之神` |
| ④ Credits（底）| `262 H 单季 · 4367 H 通算 · 10× All-Star` |

数据来源：262 H = 2004 MLB 单季纪录（破 Sisler 1920 年的 257）/ 4367 H = MLB 3089 + NPB 1278 通算（吉尼斯世界纪录）/ 10× All-Star = 2001-2010。

## 锁定动作 — Pre-Pitch Ritual（招牌仪式）

Ichiro 全联盟最辨识的不是挥棒、不是接球、不是跑垒，是他**进打击区后的招牌仪式动作** — 右手伸直把球棒举向投手、左手拉右肩袖口。这是 24 年职业生涯每一次打击前的开场，全世界球迷的肌肉记忆。

- **接触尚未发生**，pre-pitch routine 第二步（举棒指向投手 + 拉袖口）
- **球棒**：**右手单手握住棒柄底端**（左打者，所以右手在下），**整支球棒垂直 / 略向投手倾斜**举过头，棒头指向画面右上 11 点钟方向（投手所在方向）
- **左手**：抬到右肩，**手指捏住右肩 jersey 袖口边缘**做拉扯动作（这是招牌中的招牌）
- **躯干**：左肩对 pitcher（左打站位），**3/4 转向 camera-right** — 右臂伸直、左臂横过胸前的对角线构图非常上镜
- **重心**：站直，前后脚平衡，没有 stride 准备
- **头部 / 视线**：轻微低头、眼神 laser locked 望向 pitcher 方向（camera-right 出框），下巴收拢
- **表情**：完全 stoic、零表情、绝对专注 — 跟 Soto 的 smirk 反向
- **构图**：腰部以上，figure 占画布约 55%（瘦长身型撑得起更多高度）

## Visual Anchors（必须有的识别度）

- 5'11" / 175 lbs **lean-lithe 体型**，比 Judge / Stanton 明显瘦小（这是 Ichiro 的辨识度核心 — 用接触 + 速度而非 power）
- 黑色短发（头盔下露一段）+ 下颌线干净（早年 clean-shaven，中后期偶有 thin goatee — poster 用 clean-shaven 版本辨识度更强）
- 日本人五官（清晰的杏眼 + 高颧骨 + 狭长脸型），不要画成 generic Asian
- **左打、右投**（球棒在右肩、左手拉袖）
- 球衣号 **51**
- **Mariners 主场球衣**：奶白色（cream-tinged white）jersey + navy + Northwest teal piping，navy "Mariners" cursive script 在左胸 + teal 描边
- 头盔 / 帽子：**navy 底 + 正面 "S" compass-rose logo**（白色 S 嵌在 teal 罗盘玫瑰里）— 这跟 Yankees NY / Mets NY 完全不同，不能搞混
- **左前臂手腕带**：navy 弹性手腕带（Ichiro 招牌护腕，几乎每张照片都有）

## Person Recognition Gate

```json
[{"person": "Ichiro Suzuki", "confidence": 92, "tier": "HIGH", "reason": "Global icon spanning 28 pro seasons MLB+NPB, 2001 AL MVP+ROY, 10x All-Star, 4367-hit world record holder, 2025 first-ballot HoF lock, signature pre-pitch ritual deeply trained in vision models", "anchors_suggestion": null}]
```

→ HIGH 直接用名字。

---

## Final Prompt — 3/4 ESPN angle

```text
Japanese sports cinema poster illustration, 3:4 vertical, in the style of contemporary Japanese sport-movie key art (e.g. "100m" / "The First Slam Dunk" theatrical posters) — single hero, monumental composition, Pacific Northwest twilight atmospheric background with subtle Japanese-sun motif, cinematic stillness, ALL TITLES BAKED INTO THE POSTER.

CAMERA ANGLE: approximately 30 to 45 degrees off-axis from a straight pitcher's-view, positioned on the first-base side photographer pit. Three-quarter view of the batter — face partially visible looking toward camera-right (toward the pitcher), the diagonal composition of his extended right arm and tucked left arm clearly visible.

POSE (locked) — Ichiro's Signature Pre-Pitch Ritual: Ichiro Suzuki frozen in his iconic pre-pitch ritual moment — the second beat where he extends the bat toward the pitcher and tugs his right sleeve. As a left-handed batter, his left shoulder points toward the pitcher (camera-right). His RIGHT hand grips the bottom end of the bat handle, RIGHT ARM FULLY EXTENDED forward and slightly upward, the entire bat held nearly vertical and angled toward the upper-right of the frame at roughly 11 o'clock — pointed at the unseen pitcher. His LEFT hand is raised across his chest to his RIGHT shoulder, LEFT FINGERS PINCHING AND TUGGING THE EDGE OF HIS JERSEY SLEEVE at the right shoulder seam — this sleeve-tug is the signature gesture, must be clearly visible. Body upright, weight balanced evenly on both feet, no stride preparation. Head slightly tilted down, eyes laser-locked toward the pitcher (off-frame, camera-right direction), chin tucked. Facial expression completely stoic, zero affect — the face of total concentration ritual. Framed from waist up, lean figure occupies ~55% of canvas height (his slim build allows more vertical presence than power hitters).

CHARACTER (Ichiro Suzuki, locked): lean lithe 5'11'' / 175 lbs build — clearly slimmer than power hitters, narrow shoulders, athletic but not bulky. Short black hair just visible under the helmet brim. Clean-shaven Japanese facial features — almond-shaped focused eyes, high cheekbones, narrow jawline, distinctive Japanese male facial structure (NOT generic Asian — specifically Japanese in the way the cheekbones and chin are drawn). Wearing classic Seattle Mariners home uniform — cream-tinged white jersey with navy + Northwest-teal piping along the placket and sleeves, navy cursive "Mariners" script wordmark with teal outline across the left chest, jersey number 51 visible on left sleeve. Seattle Mariners batting helmet — navy with the iconic "S" compass-rose logo on the front (a white "S" inside a teal compass-rose / nautical-star design — NOT a Yankees NY, NOT a Mets NY, this is the Mariners compass S, which must be drawn distinctly). Visible navy elastic wristband on his left forearm (Ichiro's signature wristband). Dark wood bat. Likeness recognizably Ichiro Suzuki — Japanese-specific features.

STYLE — POSTER ILLUSTRATION: hand-illustrated key art quality with thick black contour outlines on the figure, soft poster-paint cel shading, slight grain texture overlay. Noble-statue stillness rather than dynamic motion — this is the calm before the swing, not the swing. Limited tonal range — each form rendered in three values. Subtle textured brush noise across flat color fills. Variable-weight black ink on key contours.

BACKGROUND — Pacific Northwest Twilight at T-Mobile Park (painterly, NOT photo): a moody twilight sky dominates the upper canvas — deep midnight navy at the top fading down through Mariners teal-aqua at the horizon line. The faint silhouette of Mount Rainier rises in the distance behind the figure as a soft pale-grey conical shape (very subtle, atmospheric, not detailed). Across the upper-mid third, a soft suggestion of T-Mobile Park's retractable-roof ribbing and upper-deck silhouette in slightly darker navy-gray, NOT a detailed crowd. In the upper-right corner, a single small CRIMSON-RED CIRCULAR DISC suggesting the Japanese sun / hinomaru — small, atmospheric, glowing softly against the navy sky (a quiet tribute to Ichiro's origin, not kitsch — must be subtle, occupying only ~5% of canvas). Slight grain across the background.

COLOR PALETTE (locked): midnight navy (dominant ~50%) + Mariners teal-aqua (horizon accent ~20%) + Mount Rainier soft pale grey (~10%) + crimson Japanese sun disc (small accent ~5%) + cream white jersey + warm skin tone + black ink contours + brushed off-white text. Nine values total.

POSTER TEXT LAYOUT (modeled on Japanese cinema posters; bilingual title block must read as ONE poster designer's matched typography):

- ① MAIN TITLE — the three Simplified Chinese characters "安打王" rendered in massive bold brush-stroke calligraphic poster typography, off-white / cream color with subtle paper-grain distress along the edges. Largest text element, occupying ~35% of canvas width (slightly wider than 2-character titles to accommodate the third character). Position: upper-middle, just above the figure's helmet. All three Han characters accurately formed and legible.

- ② INTERNATIONAL SUBTITLE — the English word "ICHIRO" rendered immediately below the "安打王" title, in a heavy condensed serif or chunky display typeface that VISUALLY MATCHES the "安打王" treatment (same off-white color, same brush-textured edges, similar visual weight per glyph). Sized ~50% the width of "安打王". Together they form one unified bilingual title block.

- ③ TAG LINE — the Simplified Chinese phrase "日美通算 安打之神" placed at the very top of the canvas as a thin centered tag, in a simple light-weight sans-serif with slight letter-spacing, soft white. Functions as the "catchphrase" line.

- ④ STATS LINE — "262 H 单季 · 4367 H 通算 · 10× All-Star" centered along the bottom 6% of the canvas, in a thin tabular sans-serif, soft white, smaller than the tag line.

All text rendered crisply and fully legibly. Simplified Chinese characters accurately formed (not garbled). Hierarchy: 安打王 > ICHIRO > 日美通算 安打之神 ≈ stats.

EMOTION: monastic concentration, ritualistic stillness, the calm before the strike — the moment when the Hit King prepares to make contact through pure ritualized focus. Like a Japanese movie poster announcing a swordmaster protagonist's pre-strike moment.

--ar 3:4 --stylize 250
```

## 跑图建议
- 跑 2-4 张
- 评分维度：
  - 招牌动作 — 右臂伸直举棒指投手 + 左手拉右肩袖口（**两个手部动作必须同时正确**）
  - lean / 苗条体型（不能画成 power hitter — 比 Judge / Stanton 明显瘦小）
  - Mariners "S" compass logo（不是 NY），navy + teal 配色
  - 日本人特征面孔（不是 generic Asian）
  - 远景 Mt. Rainier + 小红日 + 双层 navy/teal 天空渐变
  - 安打王 + ICHIRO 字型统一笔触
- 不要动：
  - 招牌动作（不要换成挥棒中、跑垒、接球 — 那些不如 ritual 上镜）
  - 体型（不能画大块头）
  - Mariners 队识别度（不要画成晚期 Yankees/Marlins 时期）
  - 红日要小要克制（占比不超过 5%，否则变成 kitsch 旭日旗）

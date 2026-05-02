# MLB 帽封面 prompt — Style 8：Karina × 李政厚 / 上海外野黄昏 100m 动漫海报

## 推荐风格

- 风格：**100m / 日系动漫电影海报**（参考 `references/cover-style-pool.md` 的 `100m-poster` ID + The First Slam Dunk / Weathering With You 视觉语言）— 戏剧性黄昏天空 + 单一连续场景 + 双 hero 前景 + 大气透视
- 概念演进（vs Style 7 v1 硬切左右）：两人都站在上海某球场的外野草地上，远景陆家嘴天际线。**她不该在这里（时尚穿搭），他属于这里（球员装束）。同一个场景，两种关系** — 视觉反差从「硬切」升级到「同地两种人」
- 这张图最该卖什么：**「她在球场上像走错片场，他在球场上是日常 — 同一个 MLB，两种生活」 — 反讽更深，picture 更连贯**

## 沿用与变更

| 项 | 沿用自 Style 7 v1 | 本版变更 |
|---|---|---|
| 角色 | Karina + 李政厚 | ✅ 不变 |
| 构图（双 hero、各占一半） | ✅ | ✅ 但去掉硬切接缝，改单一连续景 |
| 比例（头 13-15%）| ✅ Rule 1 套用 | ✅ 加强 |
| 多人物 Rule 5 | ✅ 表格化 + 排除句 | ✅ 不变 |
| 背景 | 左棚 / 右草地 | 🔄 **统一上海外野黄昏** |
| 风格 | editorial fashion | 🔄 **100m 日系动漫海报** |
| 标题 + 简体锁 | ✅ 同步 | ✅ 不变 |

## Person Recognition Gate

```json
[
  {"person": "Karina (aespa)", "confidence": 88, "tier": "HIGH"},
  {"person": "Lee Jung-hoo / 李政厚", "confidence": 78, "tier": "HIGH"}
]
```

## Final Prompt

```text
A 3:4 vertical Japanese anime movie poster cover, modeled on the visual language of "100 Meters" / The First Slam Dunk / Weathering With You theatrical posters — dramatic golden-hour sky, cinematic wide perspective, two heroes standing in foreground on a single continuous landscape, painterly cell-shaded anime illustration with high-contrast lighting and atmospheric depth.

================================================
ENVIRONMENT — single connected setting (NOT split-frame)
================================================

The two subjects stand on the same continuous landscape — there is NO vertical seam, NO hard split. They share one bright cinematic environment:

- FOREGROUND (lower 50% of canvas): a real Shanghai-style baseball outfield, green outfield grass with crisp chalk foul lines, slight wind ripple visible in the grass, bright sunlit field. The grass is the floor both subjects stand on.
- MIDGROUND (35-65% horizontal band, behind the subjects): empty bleachers and field rim, soft anime-poster blur.
- BACKGROUND (upper-mid horizon): the iconic Shanghai Pudong / Lujiazui skyline silhouette — Oriental Pearl TV Tower (left), Shanghai Tower + World Financial Center "bottle opener" + Jin Mao Tower (center-right cluster), rendered in clean anime-poster silhouette with rim-light catching tower edges.
- SKY (upper 35%): dramatic bright golden magic-hour sky transitioning from warm peach-orange at the horizon to cool magenta-violet at the top, with painterly cumulus clouds catching the sunset, subtle light rays, lens-flare glow at one corner. Bright, optimistic, anime-poster atmosphere.

The light source is a single warm golden-hour sun positioned camera-right behind the Shanghai skyline, casting a long warm side-light on both subjects from the same direction.

================================================
SUBJECTS — two heroes in foreground, single shared light
================================================

Composition: both subjects stand in the foreground on the grass, chest-up to upper-thigh framing, occupying lower 60% of canvas vertically. Karina is at canvas-left third, Lee Jung-hoo at canvas-right third. A wide gap between them frames the Shanghai skyline behind. They do NOT touch, do NOT face each other, do NOT interact.

CRITICAL SCALE RULE: the WHOLE figure scaled up so each head naturally enlarges to approximately 13-15% of total canvas height — NOT a face close-up, NOT a tiny figure. Each face must be clearly recognizable when the cover is shrunk to 200px-wide XHS feed thumbnail. Use cinematic portrait-telephoto-equivalent framing, no wide-angle distortion.

Both rendered as physically-rendered manga figures with photo-accurate East-Asian likenesses, rendered as cell-shaded anime poster illustration (not photo) — clean ink linework, two-tone cell shading with painterly highlights and rim lights, anime-movie-poster grade.

------------------------------------------------
LEFT SUBJECT — KARINA (aespa), fashion-out-of-place mode
------------------------------------------------

Archetype based on Karina (Yu Ji-min) of aespa: sharp angular jawline, almond eyes, defined cheekbones, signature composed-and-distant expression.

Pose: standing facing camera straight-on, slight contrapposto, weight on right leg, both hands tucked into front coat pockets. Head tilted slightly up-and-left, gazing past the camera into the upper-left middle distance with a calm and slightly aloof expression. ONE strand of hair lifted gently by wind across one cheek (anime poster wind cue). Mouth closed, magazine-cover composure.

Wardrobe (deliberately editorial-luxury, OUT OF PLACE on a baseball field):
- Black baseball cap with crisp white "MLB" wordmark — pristine, undamaged, freshly out-of-box.
- Oversized cream cashmere crewneck knit, slightly oversized, hem just below hip, soft texture, no graphics.
- Tailored cream wide-leg trousers (just visible at lower frame edge).
- A single delicate silver chain at neckline.
- Clean white sneakers (barely visible).

She is composed but visually displaced — she belongs to a magazine cover, not a ballfield.

------------------------------------------------
RIGHT SUBJECT — LEE JUNG-HOO (李政厚), at-home-on-field mode
------------------------------------------------

Archetype based on Lee Jung-hoo (李政厚 / 이정후), Korean MLB outfielder. Round-soft jawline (NOT angular), gentle almond eyes, full-but-soft lips, calm focused post-game expression with no smile, slight sweat sheen on temples.

Pose: standing three-quarter angled ~25° away from camera, body opening toward right edge of frame. One hand grips a wooden baseball bat resting tip-down on the grass beside him. Other hand wears a brown leather batting glove, hanging loose at his side. Head turned to look out across the field toward the upper-right middle distance (NOT at the camera, NOT at Karina). Posture relaxed but vigilant, the way a player settles after an at-bat.

Wardrobe (deliberately athletic, BELONGS on the baseball field):
- Same model black baseball cap with crisp white "MLB" wordmark — but visibly weathered: faint dust streaks at the brim, sweat darkening the band, slightly crumpled crown. Same cap design as Karina's, but lived-in.
- Generic professional baseball pinstripe jersey in cream with thin navy vertical stripes (do NOT render any specific MLB team logo, NO SF Giants chest patch, NO team name across chest). Plain navy undershirt at neckline.
- Cream baseball pants with grass-stain at one knee.
- Brown leather batting glove on one hand.

He is composed and at home — he belongs on a ballfield, this is his workplace.

================================================
POSE DIFFERENTIATION ENFORCEMENT (multi-character hard rule)
================================================

The two figures MUST NOT share the same action, gesture, gaze direction, or wardrobe register. Specifically:
- Do NOT make Lee Jung-hoo also tuck hands in pockets like a fashion model.
- Do NOT make Karina hold a baseball bat or wear baseball gear.
- Do NOT make their gazes meet or their bodies face each other.
- Do NOT have them stand at exactly the same depth — Karina slightly closer to camera, Lee Jung-hoo half a step further into the field.
- Do NOT make their lighting differ — both are lit by the same golden-hour sun from camera-right; the SCENE is unified, the SUBJECTS differ by wardrobe and pose.

================================================
ANIME POSTER STYLE CUES (100m / Slam Dunk Movie / Weathering With You vocabulary)
================================================

- Cell-shaded skin and fabric with sharp two-tone shadow but soft painterly highlights at the edges
- Hair rendered in clean anime strands with rim light catching tip edges
- Strong directional warm rim-light on both subjects from camera-right
- Subtle wind cues: Karina's hair strand lifts, grass blades sway, distant clouds drift
- Sky: painterly cumulus clouds catching sunset, faint sun-rays, optional bright lens flare in upper-right corner
- Composition perspective: slight low-angle (camera at chest-height of the subjects, looking up just a little) — gives heroes a cinematic standing-tall feel
- Optional very faint motion-line cues at canvas edges (Japanese poster convention, must be subtle not anime-fight-scene loud)
- NO speed-blur on subjects (they are still); only on grass / clouds for atmosphere

================================================
TEXT OVERLAY (Simplified Chinese ONLY, NO Traditional)
================================================

- Top masthead (medium condensed serif, warm cream-white, centered): 「MLB」 — top 8% of canvas, restrained

- Top-right corner mono caption stack (very small, low opacity warm cream): 「VOL. 04 / 2026」 / 「上海」 / tiny mock barcode — must NOT compete with center title

- Optional small left-margin caption (small mono, low opacity): 「Karina × 李政厚」 — pure magazine credit treatment

- **CENTER MAIN TITLE BLOCK — the dominant graphic element after the two heroes**, positioned at vertical 45-62% of canvas, horizontally centered (in the gap between the two subjects), occupying roughly 70-80% of canvas width:
  - 主标 (Simplified Chinese): 「MLB 在上海」 — MASSIVE bold modern Simplified-Chinese sans-serif with slight anime-poster theatrical weight, characters approximately 11-13% of canvas height each, warm crisp cream-white with a thin deep-navy outline-shadow for legibility against the bright sky/grass behind. Single line, centered. Sits at vertical 47-55% of canvas. Must read at 200px-wide thumbnail.
  - 副标 (Simplified Chinese): 「是潮牌 不是棒球」 — directly below 主标, large condensed Simplified-Chinese sans-serif, characters approximately 6-7% of canvas height, soft cream with thin navy shadow. Single line, centered. Sits at vertical 56-62% of canvas.
  - Subtle radial soft darkening behind the title block (NOT a hard band — anime posters use vignette darkening, not solid bars)

- ALL Chinese characters MUST be SIMPLIFIED CHINESE (简体中文). Verify each character: 在 / 是 / 潮 / 牌 / 不 / 棒 / 球 / 上 / 海 — all simplified.

================================================
COLOR PALETTE
================================================

- Sky: warm peach-orange at horizon → magenta-violet at top
- Pudong skyline: deep navy silhouette with golden rim-light on tower edges
- Grass: vivid sunlit emerald green with cooler shadow patches
- Karina: cream cashmere + cream trousers + black cap
- Lee Jung-hoo: cream pinstripes + brown leather + black cap
- Text: cream-white with deep navy outline shadow for legibility
- Overall mood: bright, optimistic, magic-hour, NOT moody, NOT dark

================================================
STYLE
================================================

Japanese anime movie poster illustration, painterly cell-shaded, theatrical golden-hour atmosphere, "100 Meters / First Slam Dunk / Weathering With You" visual register. NOT photo. NOT realistic 3D render. NOT manga-page style. The cover's argument: same MLB cap on a fashion idol who's out of place on a ballfield, and on a real ballplayer who's at home on it. Both subjects must read as anime poster portraits, not AI photos, not manga-page line art either — full-color anime poster polish.

--ar 3:4 --stylize 250
```

## 如果要继续改

- **背景亮度**：默认黄昏暖光；如果觉得不够亮，可改正午晴空（warmer cyan sky）/ 清晨蓝粉（cooler dawn）— 一次只换一组
- **天际线选择**：默认 Pudong（陆家嘴三件套 + 东方明珠最有上海识别度）；可换外滩民国建筑群（更复古）/ 西岸滨江（更年轻）— 但 Pudong 最一秒识别
- **球场细节**：默认外野草地 + 看台模糊；可加一些棒球场氛围细节（垒包剪影 / 投手丘 / 计分板）但要克制 — 太多就抢了上海天际线的视觉
- **比例红线（继续套）**：每张脸 13-15% 画布高度。如果还是头偏小，加 `subject heads must each occupy roughly 14% of canvas height — not smaller`
- **球队 logo 红线（继续套）**：通用棒球条纹，**不要画 SF 字母 / 球队胸标 / 队徽**
- **互动红线（继续套）**：两人不看彼此、不面向彼此

## 视觉宪法合规说明

- **photoreal 关键词清查**：prompt 全文未出现违禁词；「real Shanghai-style baseball outfield」「golden-hour sun」是场景描述不是渲染语言，渲染语言锁定 `cell-shaded anime poster illustration (not photo)`
- **运动员 photo 高发风险 + 黄昏外景双高发**：本版风险最高（运动员 + 户外 + 黄昏 + 写实城市）— 三道闸：(a) rendering rule；(b) ANIME POSTER STYLE CUES 段；(c) STYLE 段最后再写 "must read as anime poster portraits, not AI photos"
- **简体中文强锁**：与 Style 4 v3 / 6 / 7 同步规则
- **多人物 Rule 5**：完整套用 — 表格化 + 排除句 + lighting unification 段（统一光源是新加的，避免 AI 给两人不同光源把场景拆散）
- **Rule 1 整体放大**：明写「the WHOLE figure scaled up so each head naturally enlarges to approximately 13-15%」+ 「Each face must be clearly recognizable when the cover is shrunk to 200px-wide XHS feed thumbnail」

## Concept layer 注释（vs Style 7 v1）

| | Style 7 v1（硬切） | **Style 8（连景）** |
|---|---|---|
| 视觉切分 | 中央硬切，左棚右场 | 单一连续景，两人共处 |
| 风格 | editorial fashion 杂志封 | 100m 动漫海报 |
| 反讽机制 | 同帽两环境 | 同环境两关系 |
| 浓度 | 高（一眼看出对比） | 更深（看一会才意识到她不该在这里） |
| 风险 | 多人物 + 双场景 | 多人物 + 双场景 + 写实城市 + 黄昏（最高）|

如果选「冲击直接」，Style 7 v1。
如果选「优雅有后劲」，Style 8。

## 跑出第一张评估五件事

1. **比例**：两个头 13-15%，feed 缩图能认得出来
2. **像不像**：Karina 角颌 + 李政厚圆颌 是否分开
3. **景连不连**：两人是否真的共处一个场景，没掉成「合成图」
4. **天际线识别度**：陆家嘴三件套 + 东方明珠 是否一眼读出「上海」
5. **是否漂 photoreal**：运动员 + 户外 + 黄昏 + 写实城市 — 高风险三连

跑完丢回来。


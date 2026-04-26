# 道奇 = 日本队 封面 prompt v2

## Person Recognition Gate
```json
[
  {"person": "Shohei Ohtani", "confidence": 92, "tier": "HIGH", "reason": "全球级超巨", "anchors_suggestion": "直接用名字"}
]
```
v1 三人并列被否（构图静、张力弱）。v2 收成单 hero，Uniqlo 元素从背景墙搬到身上 + 拍法直接借 Uniqlo LifeWear 广告美学。

## 推荐风格
- 风格：**Uniqlo LifeWear ad campaign × MLB pitching action**（双轴融合：极简时装大片调性 + 棒球动作瞬间）
- 为什么选它：v1 把 Uniqlo 当背景 logo，本质还是球场新闻照。这版让 Uniqlo 的"视觉语言"本身（无缝奶白布景、硬朗等距打光、模特正面凝视、零特效）直接接管画面，再把投球动作的张力撞进这个干净到极致的框里 — 形成「时装大片 vs 球场动力」的二象拉扯
- 这张图最该卖什么：Uniqlo 美学里出现一个**正在发力的大谷** + 胸口 Uniqlo 红字 = 一句话画面宣告"道奇身上已经长出了 Uniqlo"

## Final Prompt

```text
A 3:4 portrait fashion-editorial hero image, shot in the unmistakable visual language of a Uniqlo LifeWear global ad campaign — seamless cream-white cyclorama backdrop, even soft key light, no shadow drama, calm minimal Japanese editorial composition. But the subject is in mid-pitch baseball action.

Single hero, center-frame: Shohei Ohtani frozen at the apex of his pitching delivery — front leg planted, torso fully torqued, throwing arm whipping forward, baseball just released and suspended mid-air about 30cm from his fingertips. Powerful coiled body, subtle tension in jaw and eyes, focused gaze just past the camera.

Wardrobe fusion (the key visual): he wears what reads simultaneously as a Dodgers home cream pinstripe jersey AND a Uniqlo LifeWear basic tee — clean cream base fabric, classic Dodgers blue pinstripes vertical, but the chest crest is replaced by a clean bold "UNIQLO" red wordmark logo (the real Uniqlo logo, sans-serif, brand red), positioned exactly where a chest sponsor patch would sit on a European football jersey or NPB jersey. Small "Dodgers" script visible just below the Uniqlo wordmark to anchor the team. Crisp tailoring, fashion-shoot fabric quality.

Dynamic tension elements: a small puff of dirt kicked up from his back foot, the released baseball captured tack-sharp mid-flight, a single bead of sweat at his temple. These are the only "sport" markers — the rest of the frame is pure Uniqlo ad calm.

Lower 10% of frame, very subtle: a thin horizontal strip of Dodger Stadium warning-track dirt and chalk infield line, just hinting at the stadium without showing it. The world above the dirt line is pure Uniqlo studio cream.

Top right corner: small clean Uniqlo logomark badge.
Bottom center: a thin black bar with bold Chinese text "道奇 已经穿上 UNIQLO" — typography in Uniqlo's clean sans style, not stadium banner style.

Color palette: Uniqlo cream/off-white background dominant, Dodger cream + blue pinstripes on jersey, Uniqlo red as the only saturated color accent (chest logo + bottom bar accent). Soft Japanese editorial light.

Photorealistic, fashion campaign quality, sharp detail on face and uniform fabric, motion frozen at 1/8000 shutter feel.

Exclusions: no full stadium background, no crowd, no flag, no banner border, no comic break-out, no watercolor, no aura, no speed lines, no Pop Art, no geometric pattern, no three-figure lineup.

--ar 3:4 --stylize 300
```

## 如果要继续改
- 想再放大 Uniqlo 美学：去掉底部 dirt strip，纯白底 + 投球动作（更像广告，更脱离体育新闻语境）
- 想再放大体育张力：把 dirt 提高到 25%，加一个虚化的本垒板
- 不要动：单 hero、Uniqlo 红 wordmark 在胸口、Uniqlo cyclorama 拍法、`--ar 3:4 --stylize 300`

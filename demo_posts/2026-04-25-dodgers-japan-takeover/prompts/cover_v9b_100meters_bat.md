# 道奇 = 日本队 封面 v9b — 一百公尺海报版（打击）

## Person Recognition Gate
```json
[{"person": "Shohei Ohtani / 大谷翔平", "confidence": 92, "tier": "HIGH", "reason": "全球级超巨", "anchors_suggestion": "左打 / 宽下颌 / 单眼皮带笑意 / 宽肩 / 193cm lean muscular / 短黑发"}]
```

## 推荐风格
- 风格：**100 Meters 电影海报严格仿版（打击动作）**
- 与 v9a 差异：v9b 打击 follow-through，v9a 投球 release apex
- 共同：纯红底 / 单人物 / 左上球员名块 / 巨型 motion-blur 主标 / 无左竖 tagline

## Final Prompt

```text
A 3:4 portrait Japanese animation movie poster in EXACT visual language and layout of the "100 Meters / 一百公尺" (2024) film poster — solid bold flat color background, single dynamic hero crossing the frame diagonally, MASSIVE distorted motion-blurred title typography across the bottom, scattered small vertical Chinese typography on the upper-left, festival laurel and date strip in corners. Movie poster, not sports photo.

BACKGROUND: completely flat solid vermillion red #E84033 (the iconic 100 Meters poster red). NO gradient, NO texture, NO scenery, NO stadium, NO clouds.

SINGLE HERO (center-right, occupying ~65% of canvas height): Shohei Ohtani as a left-handed batter captured one frame after contact — full follow-through, bat extended through the swing zone diagonally from lower-right to upper-left of the frame, wrists rolled over, eyes locked forward tracking the ball flight off-camera, weight transferred to front leg, back hip fully rotated open, body torqued and explosive. Visual energy slashes diagonally across the poster identical to the 100 Meters runners' diagonal crossing.

Hero face must read as Shohei Ohtani specifically: broad jawline, single-fold eyelids with focused tracking gaze, slight bared-teeth determination from contact effort, broad shoulders, lean muscular 193cm frame, short black hair under helmet. Real-world Ohtani likeness rendered through 100 Meters' painterly anime brush-pen style — confident bold black outlines, minimal interior shading, expressive sweat droplets flying off temple and forearm, slight motion blur on the bat tip.

WARDROBE: Dodgers home cream pinstripe uniform with Dodger blue batting helmet (with ear flap on the left side since he's a left-handed batter), bold red UNIQLO wordmark patch on a clean white square on the chest (so Uniqlo logo stays visible against red background). Batting gloves in cream and blue. Same brush-pen confidence as the body.

TOP-LEFT BLOCK (upper 25% of frame, left edge, all white type, vertical-poster cast-credit layout mimicking "松坂桃李 染谷將太" credits stack from reference):
- Small white laurel wreath badge at very top containing text "DODGER STADIUM 2026"
- Below the laurel, three player credits stacked as small vertical columns of clean white sans-serif Chinese:
  - 大谷翔平  #17
  - 山本由伸  #18
  - 佐佐木朗希  #11
- Each name + number on its own line, staggered like Japanese movie cast credits

NO vertical tagline on left edge. Left edge stays clean below the cast block.

TITLE BLOCK (occupies bottom 25% of frame, visual co-hero alongside figure): Chinese title「优衣库为什么冠名道奇球场」in HUGE bold sans-serif Chinese typography, white with subtle thin red drop shadow, characters STRETCHED and MOTION-BLURRED horizontally as if speeding past viewer at 100 mph — exact kinetic distorted treatment as「一百公尺」title in reference. Some character edges trail into red streaks. Title spans nearly full width.

Below title, small Latin subtitle in clean white: "DODGER STADIUM = UNIQLO FIELD".

BOTTOM-RIGHT: small white date strip "4.25 / 道奇主場 全季上映".

BOTTOM-CENTER (very small, gray): faux-staff credit lines styled like the reference's 5pt creator credits.

COLOR PALETTE: dominant flat vermillion red #E84033 + white typography + cream uniform + Dodger blue helmet + saturated Uniqlo red on chest patch (against white square). Hero body in subdued cream with shadow tones.

EXCLUSIONS: no stadium, no crowd, no light flare, no watercolor wash, no comic break-out frame, no separate speed lines, no 3D CG, no photoreal, no second figure, no left-edge vertical tagline, no pitcher's mound dirt.

--ar 3:4 --stylize 400
```

## 如果要继续改
- 脸不像 → 加 `face strongly resembles real-world Shohei Ohtani 2026 reference photo`
- 想画面更轰：把 follow-through 换成 contact moment（球离棒头 30cm）
- 不要动：左打 / 纯红底 / 左上球员名块 / 标题 motion-blur / 100 公尺笔触

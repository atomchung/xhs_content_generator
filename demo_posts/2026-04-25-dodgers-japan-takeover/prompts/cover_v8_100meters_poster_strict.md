# 道奇 = 日本队 封面 v8 — 一百公尺海报版式（最终）

## Person Recognition Gate
```json
[{"person": "Shohei Ohtani / 大谷翔平", "confidence": 92, "tier": "HIGH", "reason": "全球级超巨", "anchors_suggestion": "直接用名字 + 已公开面部特征：宽下颌、单眼皮带笑意、宽肩、身高 193cm lean muscular"}]
```

## 推荐风格
- 风格：**100 Meters 电影海报严格仿版**（参考用户提供海报图）
- 为什么选它：用户已锁定海报 reference，直接对位它的版式语言 — 纯色红底 / 单人动态对角线 / 巨型 motion-blur 标题压底 / 散落小字 / 顶左竖排 tagline
- 这张图最该卖什么：让小红书读者刷到第一秒以为是新番海报 / 电影海报 — 而不是体育新闻

## Final Prompt

```text
A 3:4 portrait Japanese animation movie poster in EXACT visual language and layout of the "100 Meters / 一百公尺" (2024) film poster — solid bold flat color background, single dynamic hero crossing the frame diagonally, MASSIVE distorted motion-blurred title typography across the bottom, scattered small vertical Chinese typography on the left, festival laurel and date strip in corners. This is a movie poster, not a sports photo.

BACKGROUND: completely flat solid vermillion red (#E84033, the iconic 100 Meters poster red). NO gradient, NO texture, NO scenery, NO stadium, NO clouds. Pure flat red wall.

SINGLE HERO (center-right of frame, occupying ~65% of canvas height): Shohei Ohtani captured at the apex of his pitching delivery — torso fully torqued, throwing arm whipping forward across the frame from upper right to lower left, fastball just released and suspended mid-air near his outstretched fingers. Body angled diagonally so the visual energy slashes across the poster identical to how the runners cross the 100 Meters poster.

Hero face must read as Shohei Ohtani specifically: broad jawline, single-fold eyelids with subtle warm half-smile lifted into focused intensity, broad shoulders, lean muscular 193cm frame. Hair short black under cap. Reference his real-world appearance, but rendered through 100 Meters' painterly anime brush-pen style — confident bold black outlines, minimal interior shading, expressive sweat droplets flying off his temple and arm, slight motion blur on the hand.

Wardrobe: Dodgers home cream pinstripe uniform with cap, bold red UNIQLO wordmark patch on a clean white square on the chest (so the Uniqlo logo stays visible against the red background), Dodgers cap. Painted with the same brush-pen confidence as the body.

TITLE BLOCK (occupies bottom 25% of frame, this is the main visual hero alongside the figure): the Chinese title「优衣库为什么冠名道奇球场」rendered in HUGE bold sans-serif Chinese typography, white with subtle thin red drop shadow, the characters STRETCHED and MOTION-BLURRED horizontally as if they are speeding past the viewer at 100 mph — exact same kinetic distorted treatment as the「一百公尺」title in the reference poster. Some character edges trail into red streaks. Title spans nearly full width.

Below title, small Latin subtitle in clean white: "DODGER STADIUM = UNIQLO FIELD".

LEFT EDGE VERTICAL TAGLINE (top-left, 18% of frame height, vertical Chinese reading top to bottom): a poetic single-line in clean white Chinese:「把這座球場，染成日本紅。」typeset vertically in elegant sans, two columns max.

SCATTERED CAST NAMES (lower-left strip just above title, vertical Japanese-poster-style credit columns in white small type, mimicking the「松坂桃李 染谷將太」credits stack from the reference):
- 大谷翔平  #17
- 山本由伸  #18
- 佐佐木朗希  #11
Stacked as small vertical columns of clean white sans-serif Chinese, each name with its number.

CORNER DETAILS:
- Top-left small festival-laurel-style badge: a thin white laurel wreath enclosing the text "DODGER STADIUM 2026"
- Bottom-right: small white date strip "4.25 / 道奇主場 全季上映"
- Bottom-center under title, very small grey credits line in Chinese: faux-staff credit text styled like the reference poster's 5pt creator credits

COLOR PALETTE: dominant flat vermillion red #E84033 background + white typography + cream uniform + Dodger blue cap accent + a single saturated Uniqlo red on the chest patch (which reads against the white square so it's visible). Hero body painted with subdued cream and shadow tones to stay visible against the bold red.

EXCLUSIONS: no stadium background, no crowd, no light flare, no watercolor wash background (this version has flat red instead of v6's painterly background), no comic break-out frame, no speed lines drawn separately (the motion is built into the title and figure), no 3D CG, no photoreal, no other figures. Single hero only.

--ar 3:4 --stylize 400
```

## 如果要继续改
- 想脸再像大谷：加一句 `face strongly resembles real-world Shohei Ohtani 2026 reference photo`
- 想更复古海报感：把红改成暖一点的 #D63A2F
- 不要动：单人物 / 纯红底 / 标题 motion-blur / 散落球员名小字 / 顶左竖排 tagline / 100 公尺笔触
- 与 v6 的差异：v6 是水彩抒情背景 + 太阳光斑，v8 是 100 公尺海报严格仿版（纯红底 + 海报版式 + 大字标题）

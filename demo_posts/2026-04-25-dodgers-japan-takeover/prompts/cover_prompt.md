# 道奇 = 日本队 封面 prompt

## Person Recognition Gate

```json
[
  {"person": "Shohei Ohtani", "confidence": 92, "tier": "HIGH", "reason": "全球级超巨, MJ 级辨识度", "anchors_suggestion": "直接用名字"},
  {"person": "Yoshinobu Yamamoto", "confidence": 65, "tier": "MED", "reason": "棒球圈外辨识度中等", "anchors_suggestion": "#18, 5'10\", 黑色短发, lean build"},
  {"person": "Roki Sasaki", "confidence": 55, "tier": "MED", "reason": "新签约球员，国际辨识度低", "anchors_suggestion": "#11, 6'2\" tall, lean, 黑短发, 25岁面孔"}
]
```

## 推荐风格
- 风格：Cinematic photoreal stadium opening-day shot
- 为什么选它：核心不是球员动作 hero shot，是「场地 + 品牌符号 + 人」的复合宣告。canonical break-out comic / watercolor 都会消耗掉 Uniqlo logo 的视觉冲击力
- 这张图最该卖什么：击球员视野墙正中的 "UNIQLO" 白色巨字 + 三个日籍投手并列 = 一句话画面宣告

## Final Prompt

```text
A cinematic photorealistic 3:4 portrait cover of Dodger Stadium opening day, late golden hour light. Background: the iconic batter's eye wall in center field prominently features a clean oversized white "UNIQLO" wordmark in the brand's bold sans-serif logo, occupying the upper third of the frame, warmly lit. Above it, on the press box facade, smaller white "FIELD" lettering completes the signage "UNIQLO FIELD". Dodger blue stadium seats stretch behind, partially filled with fans waving small Japanese rising-sun flags alongside Dodgers banners.

Foreground: three Japanese-born MLB pitchers stand side-by-side on the warning track, all in Dodgers home cream uniforms with blue pinstripes, looking toward the camera from a slight low angle. From left to right: Roki Sasaki (tall and lean, mid-20s, short tousled black hair, jersey #11), Shohei Ohtani (6'3" lean muscular build, signature calm expression, jersey #17), Yoshinobu Yamamoto (slightly shorter, athletic build, neat black hair, jersey #18). Photorealistic foreground transition on the players, razor-sharp detail on faces and jerseys, cinematic shallow depth of field softly blurring the wall behind.

Center of frame: a horizontal black banner with thin gold border, containing bold Chinese text "道奇主场 已经叫 UNIQLO FIELD", banner sits over the dirt warning track, styled like a stadium announcement bar.

Color palette: Dodger blue + cream + Uniqlo red accent only in the wordmark + soft golden light.

No watercolor, no comic break-out, no aura, no speed lines, no Pop Art, no Chinese ink, no geometric pattern, no minimal flat. Realistic stadium photography only.

--ar 3:4 --stylize 250
```

## 如果要继续改
- 背景优先改：可换 dawn 冷光（更仪式感）；或在远端加一面美日双国旗
- 不要动：Uniqlo logo 位置（视野墙正中）；三人并列顺序；中央横带标题；`--ar 3:4 --stylize 250`

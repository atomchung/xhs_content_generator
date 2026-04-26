# 道奇 = 日本队 封面 v5 — The First Slam Dunk 电影版风格

## Person Recognition Gate
```json
[{"person": "Shohei Ohtani", "confidence": 92, "tier": "HIGH", "reason": "全球级超巨", "anchors_suggestion": "直接用名字"}]
```

## 推荐风格
- 风格：**The First Slam Dunk (2022) 井上雄彦电影版** — CG-rotoscope + 手绘水墨纹理 + 真实运动捕捉感的运球肌理
- 为什么选它：v3 是 90s 漫画原作，v5 是 2022 年井上自导自画的电影版 — 同一作者 30 年后的进化版美学。运动镜头从 panel 静态升级到「电影摄影机贴脸跟拍」的临场感，但保留井上的手绘墨线
- 这张图最该卖什么：低机位仰拍大谷投球 follow-through，皮肤毛孔 / 制服褶皱清晰可辨，但整张图被一层手绘墨线包裹 — 真实和动画的边界感

## Final Prompt

```text
The First Slam Dunk (2022) movie aesthetic, Inoue Takehiko director's animated film visual style — hybrid of 3D CG character rigging with hand-drawn ink line overlays, cel-shaded textured surfaces with visible brush-pen outlines, sports cinematography realism fused with Japanese manga draftsmanship.

Subject: Shohei Ohtani captured in pitching follow-through one frame after release, throwing arm fully extended forward, body weight transferred onto front leg, back leg lifted, intense narrowed eyes locked on the catcher's mitt off-frame, mouth slightly open mid-exhale. Slight rotational motion blur on the throwing shoulder.

Camera: extremely low angle, wide cinematic lens (24mm equivalent), pitcher's mound dirt foreground in soft focus, the camera is at ground level looking up so the player towers over the frame — exact shot vocabulary of the Slam Dunk movie's iconic Sawakita Eiji shooting sequence.

Wardrobe: Dodgers home cream pinstripe uniform rendered with the film's signature touch — fabric weight and pinstripe ink lines visible, cap pulled low, bold red UNIQLO wordmark patch on chest where the Dodgers script would normally sit, rendered with the same hand-painted texture as the rest of the uniform.

Background: a single warm-toned cream backdrop with subtle Dodger Stadium architectural suggestions — light tower silhouette barely visible, no crowd detail, no busy background. Slight chromatic aberration at frame edges. Subtle film grain.

Color palette: muted warm cream + Dodger blue cap + a single saturated red on the UNIQLO patch + warm golden rim light on Ohtani's right shoulder. Low saturation overall, painterly washes rather than flat anime cel color.

Texture treatment: every shape has both a CG rendered base AND a hand-drawn ink contour, creating the unmistakable First Slam Dunk hybrid look. Visible inkwork on the jaw line, the throwing hand fingers, and uniform seams.

No 90s manga screentones, no comic break-out frame, no panel borders, no speed lines. This is movie cinematography, not manga page.

Bottom-center: small clean Chinese caption "道奇 已经穿上 UNIQLO" in subtle white film-subtitle style typography.

--ar 3:4 --stylize 350
```

## 如果要继续改
- 想更接近电影：加 `motion blur on background`，把背景再虚化一档
- 想更像剧场版高潮镜头：加一句 `god ray light through the stadium roof opening`
- 不要动：低角度仰拍 / hybrid CG + 手绘墨线 / 单一暖色背景 / Uniqlo 红胸口

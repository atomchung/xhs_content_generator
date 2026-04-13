# 棒球小白系列 — 角色三視圖 Prompt

日期：2026-04-13
用途：生成角色設定圖，確保後續所有影片的角色一致性。

## 怎麼用這份文件

1. 選一個生圖工具（Midjourney / DALL-E / Stable Diffusion）
2. 貼入下方 prompt 生成角色設定圖
3. 產出的圖作為後續影片 prompt 的**角色參考圖（character reference image）**
4. 影片生成時用 image-to-video 或 reference image 功能，搭配文字 prompt

## Prompt 1 — 角色三視圖（Turnaround Sheet）

```text
Character turnaround reference sheet.
A cute round cream-colored dumpling-shaped mascot with a small green sprout
poking out from the top of a deep red baseball cap, big round sparkling black
eyes with a white highlight dot, tiny dot nostrils, soft pink blush on both
cheeks, smooth egg-shaped body with no neck, tiny stubby arms and legs.
Soft plush toy texture with gentle gradient shading.
Wearing a deep crimson red baseball jersey with bold white letters "Din"
on the chest, white baseball pants, red round-toed cleats.

Three views evenly spaced on a clean white background:
front view, three-quarter view, back view.
Same character, same proportions, same colors in all three views.
3D kawaii mascot style, character design reference sheet layout.
```

## Prompt 2 — 表情表（Expression Sheet）

```text
Expression sheet of a cute round cream-colored dumpling-shaped mascot
with a small green sprout from a deep red baseball cap, big sparkling black
eyes with white highlight, soft pink blush, smooth egg-shaped body,
tiny stubby limbs. Wearing a deep crimson baseball jersey with white
letters "Din", white pants, red cleats.

Six expressions in a 2x3 grid on clean white background:
1. Default — big sparkling eyes, no visible mouth, neutral cute look
2. Curious — head tilted slightly, eyes looking to the side
3. Surprised — small round open mouth, widened eyes
4. Excited — big open D-shaped smile, arms raised slightly
5. Focused — slight forward lean, determined look
6. Confused — one eye slightly squinting, small wavy mouth

Same character in all six expressions. Soft plush toy texture.
3D kawaii mascot style, character design reference sheet layout.
```

## Prompt 3 — 動作道具表（Action & Props Sheet）

```text
Action pose sheet of a cute round cream-colored dumpling-shaped mascot
with a small green sprout from a deep red baseball cap, big sparkling black
eyes with white highlight, soft pink blush, smooth egg-shaped body,
tiny stubby limbs. Wearing a deep crimson baseball jersey with white
letters "Din", white pants, red cleats.

Four poses in a 2x2 grid on clean white background:
1. Holding a white baseball with red stitching in both hands, curious look
2. Gripping a wooden bat resting on shoulder, excited big smile
3. Pitching wind-up pose, one stubby leg raised, focused expression
4. Running to the right, stubby legs in motion, determined face

Same character in all four poses. Green sprout visible on cap in every pose.
Soft plush toy texture with gentle gradient shading.
3D kawaii mascot style, character design reference sheet layout.
```

## 使用注意

- 三個 prompt 產出後，挑選**最一致的那一組**作為系列角色基準
- 後續影片 prompt 搭配這張圖作為 reference image
- 如果工具支持 character reference（如 Kling），直接上傳這張圖
- 如果不支持，把設定圖裁切成單一角度，用 image-to-video 起始幀
- **綠芽必須在每個角度都從帽頂冒出**，這是角色辨識核心

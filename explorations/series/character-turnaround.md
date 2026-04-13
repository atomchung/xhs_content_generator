# 棒球小白系列 — 角色三視圖 Prompt

日期：2026-04-13
用途：生成角色設定圖（turnaround sheet），確保後續所有影片 prompt 的角色一致性。

## 怎麼用這份文件

1. 選一個生圖工具（Midjourney / DALL-E / Stable Diffusion）
2. 貼入下方 prompt 生成角色三視圖
3. 產出的圖作為後續影片 prompt 的**角色參考圖（character reference image）**
4. 影片生成時用 image-to-video 或 reference image 功能，搭配文字 prompt

## Prompt 1 — 角色三視圖（標準 Turnaround）

```text
Character turnaround sheet of a cute baseball mascot character.
Rounded bean-shaped body, oversized head taking up 50% of total height,
very short stubby limbs with no visible joints, thick clean dark outline,
simple black dot eyes, small curved smile, subtle pink blush marks on cheeks,
warm red-orange skin color, 2-heads-tall chibi proportions.

Three views on a clean white background, evenly spaced:
front view, three-quarter view, side view.
All three views showing the exact same character design, same proportions, same colors.

Flat clean coloring, thick uniform outline, no shading gradients,
no glossy rendering, no background elements.
Character design reference sheet style, professional and clean layout.
```

## Prompt 2 — 表情表（Expression Sheet）

```text
Expression sheet of a cute baseball mascot character.
Rounded bean-shaped body, oversized head, very short stubby limbs,
thick clean dark outline, warm red-orange skin color, subtle pink blush on cheeks.

Six facial expressions arranged in a 2x3 grid on clean white background:
1. Happy — small curved smile, dot eyes
2. Curious — head tilted, slightly wider eyes
3. Surprised — wide open round mouth, raised body posture
4. Excited — big D-shaped open mouth smile, arms slightly raised
5. Focused — determined straight-line mouth, slightly narrowed eyes
6. Confused — squiggle mouth, one eye slightly smaller than the other

Same character in all six expressions, consistent proportions and colors.
Flat clean coloring, thick outline, character design reference sheet style.
```

## Prompt 3 — 動作 / 道具變體（Action & Props Sheet）

```text
Action pose sheet of a cute baseball mascot character.
Rounded bean-shaped body, oversized head, very short stubby limbs,
thick clean dark outline, warm red-orange skin color, subtle pink blush on cheeks.

Four action poses arranged in a 2x2 grid on clean white background:
1. Holding a white baseball with red stitching in both hands, looking at it curiously
2. Gripping a wooden baseball bat resting on shoulder, excited expression
3. Wearing a red baseball cap, standing in a pitching wind-up pose
4. Running with short legs in motion blur, determined expression

Same character in all four poses, consistent design and proportions.
Flat clean coloring, thick outline, no background elements,
character design reference sheet style.
```

## 使用注意

- 三個 prompt 產出後，挑選**最一致的那一組**作為系列角色基準
- 後續影片 prompt 搭配這張圖作為 reference image
- 如果工具支持 character reference（如 Kling 的角色參考功能），直接上傳這張圖
- 如果不支持，把 turnaround 圖裁切成單一角度，用 image-to-video 起始幀

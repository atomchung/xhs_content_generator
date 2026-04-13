# 小紅薯棒球角色定調 — Turnaround Prompt

> 目的：在開始影片系列前，先產出正確的角色外觀，確認造型
> 用途：作為所有後續影片 prompt 的視覺基準
> 更新：2026-04-12 — 依照官方吉祥物圖片校正造型

---

## 官方造型校正（來自參考圖）

| 特徵 | 原始錯誤描述 | 正確描述 |
|------|------------|---------|
| 身體顏色 | red-brown sweet potato | cream / off-white（奶白色），紅色來自衣服 |
| 體型 | round chubby | egg/pear-shaped，上窄下寬 |
| 眼睛 | big sparkling black eyes → 小彎弧（錯） | 回歸大圓眼 + 白色高光點（參考原版土豆） |
| 臉部 | rosy pink cheeks only | two small dot nostrils + soft pink cheeks |
| 質感 | smooth soft matte | soft 3D gradient plush, slight sheen |

### 固定角色描述（英文，每個 prompt 必帶）

```
A cute round cream-colored dumpling-shaped mascot with a small green sprout on
top of its head, big round sparkling black eyes with a white highlight dot, tiny dot nostrils, soft pink blush on
both cheeks, smooth egg-shaped body with no neck, tiny stubby arms and legs.
Soft plush toy texture with gentle gradient shading.
```

---

## 棒球造型 — 紅襪風格（Red Sox Inspired）

### 配色邏輯

| 部位 | 顏色 | 說明 |
|------|------|------|
| 主球衣 | 深紅色（crimson red） | 紅襪 alternate 紅色球衣 |
| 字母 "RED" | 白色，球衣胸前大字 | 呼應小紅書品牌色 |
| 球帽 | 深紅色帽身 + 白帽沿 | 頭頂留開口讓綠葉伸出 |
| 球褲 | 白色 | 對比紅色球衣 |
| 球鞋 | 深紅色 + 白色鞋底 | 統一配色 |

---

## Prompt v1 — 正面定調（靜止）

```
A cute round cream-colored dumpling-shaped mascot with a small green sprout poking out from the top of a deep red baseball cap, big round sparkling black eyes with a white highlight dot, tiny dot nostrils, soft pink blush on both cheeks, smooth egg-shaped body with no neck, tiny stubby arms and legs. Soft plush toy texture with gentle gradient shading. Wearing a deep crimson red baseball jersey with bold white letters "Din" on the chest, white baseball pants, red round-toed cleats. Standing upright facing the camera, arms slightly out. Clean white studio background. Soft even lighting. 3D kawaii mascot style, Xiaohongshu mascot aesthetic.
```

*約 96 字*

---

## Prompt v2 — 投手造型帶手套

```
A cute round cream-colored dumpling-shaped mascot with a small green sprout poking out from the top of a deep red baseball cap, big round sparkling black eyes with a white highlight dot, tiny dot nostrils, soft pink blush on both cheeks, smooth egg-shaped body with no neck, tiny stubby arms. Soft plush toy texture with gentle gradient shading. Wearing a deep crimson red baseball jersey with bold white "Din" on the chest, white baseball pants, red cleats, a round brown fielder's glove on its left hand, gripping a white baseball in its right hand. Standing in relaxed ready pose. Clean white studio background. Soft even lighting. 3D kawaii mascot style, Xiaohongshu mascot aesthetic.
```

*約 101 字*

---

## Prompt v3 — 三視角設計稿

```
Character design sheet. Three views side by side: front, side, back. A cute round cream-colored dumpling-shaped mascot with a small green sprout poking through the top of a deep red baseball cap, small curved dot eyes, dot nostrils, soft pink blush cheeks, smooth egg-shaped body, tiny stubby arms and legs. Soft plush gradient texture. Deep crimson red baseball jersey with bold white "Din" on the chest, white baseball pants, red cleats. All three views same scale, same character. Clean white background. Flat soft lighting. 3D kawaii mascot character design sheet.
```

*約 88 字*

---

## 驗證清單

| 檢查項目 | 通過條件 |
|---------|---------|
| 身體顏色 | 奶白色 / 米白，不是紅色或橘色 |
| 眼睛形狀 | 大圓眼 + 白色高光點，有神，不是小點 |
| 綠葉位置 | 從紅色帽頂伸出，清楚可見 |
| 球衣顏色 | 深紅色（crimson），不是粉紅或橘紅 |
| "Din" 字樣 | 白色大字在胸前，清晰 |
| 體型 | 上窄下寬的蛋形，不是正圓 |
| 嘴巴 | 無（兩個小黑點是鼻子，不是眼睛） |

---

## 失敗模式預防

| 避開的詞 | 原因 |
|---------|------|
| ~~red-brown~~ | 會生成錯誤身體顏色 |
| ~~small curved dot eyes~~ | 改回大圓眼，小彎弧會讓角色失去表情張力 |
| ~~pinstripe~~ | 紅襪風格是純色紅衣，不是條紋 |
| ~~STRIKE / scoreboard~~ | AI 文字渲染不穩定 |

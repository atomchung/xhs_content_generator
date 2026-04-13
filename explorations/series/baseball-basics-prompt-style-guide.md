# 棒球小白系列 — AI 影片 Prompt 風格指南

日期：2026-04-13

## 這份指南在幹嘛

定義「棒球小白急救包」系列所有影片 prompt 的寫法規則，確保：
- 每支影片 3 個 prompt，每個 prompt 生成一段 ~10 秒影片
- 小紅薯角色在所有片段中保持一致
- prompt 結構統一，方便批量產出

## Prompt 公式

每個 prompt 遵循以下順序：

```
[鏡頭 Camera] + [主角 Subject] + [動作 Action] + [場景 Scene] + [光線 Lighting] + [風格 Style]
```

六個欄位，缺一不可。順序固定，不要打亂。

### 各欄位說明

| 欄位 | 寫什麼 | 範例 |
|------|--------|------|
| 鏡頭 Camera | 鏡位 + 鏡頭運動（一個就好） | `Close-up, static camera` / `Bird's eye view, slow zoom out` |
| 主角 Subject | 角色外觀描述（從角色卡複製） | 見下方角色卡 |
| 動作 Action | 一個明確動作，用動詞開頭 | `holding a baseball in both hands, looking at it curiously` |
| 場景 Scene | 環境 + 背景物件 | `on a clean pastel yellow background, no other objects` |
| 光線 Lighting | 光源方向 + 質感 | `soft diffused studio lighting, no harsh shadows` |
| 風格 Style | 整體視覺風格 | `3D animated, Pixar-inspired, cheerful mood` |

### 字數

每個 prompt 控制在 **40-60 個英文單字**。太短 AI 會亂猜，太長會互相干擾。

## 角色卡（Character Bible）

基於倉庫 `mascot_q` 風格（Power-Pro 豆形角色 × 小紅書薯隊長）。
完整設計見 `character-design.md`，三視圖 prompt 見 `character-turnaround.md`。

以下描述在每個 prompt 中**原封不動複製**，只改動作和場景。

```
A cute baseball mascot character with a rounded bean-shaped body, oversized head,
very short stubby limbs, thick clean dark outline, simple dot eyes, small curved smile,
subtle pink blush marks on cheeks, warm red-orange skin color.
The character is roughly 2 heads tall with Xiaohongshu mascot charm
and Power-Pro-like (Jikkyou Pawafuru Puroyakyu) proportions.
```

### 角色規則

- **不改外觀**：每個 prompt 都複製同一段角色描述
- **只改動作**：動作用獨立句子寫在角色描述之後
- **不加服裝**：裸薯就是完整角色，道具靠手持或頭戴，不穿在身上
- **表情靠替換**：替換 `small curved smile` → `curious expression with head tilted slightly` 等（完整表見 character-design.md）

## 鏡頭選擇指南

本系列常用的鏡頭，從近到遠：

| 鏡頭 | 什麼時候用 | prompt 寫法 |
|------|-----------|-------------|
| 特寫 Close-up | 看清物件細節（球的縫線、棒子紋路） | `Close-up shot, static camera` |
| 中景 Medium shot | 角色 + 動作（揮棒、跑步） | `Medium shot, static camera` |
| 全景 Wide shot | 角色 + 環境關係（站在場上） | `Wide shot, static camera` |
| 俯瞰 Bird's eye view | 場地全貌、位置關係 | `Bird's eye view, slow zoom out` |

### 鏡頭運動規則

- **一個 prompt 只用一種運動**（或不運動）
- 本系列預設 `static camera`（不動），只在需要展示空間時用 `slow zoom out` 或 `slow pan`
- 不用花式運動（dolly / crane / handheld），保持乾淨簡單

## 動作描述規則

- **一個 prompt 只有一個動作**
- 用**動詞開頭**：`holding` / `swinging` / `standing` / `looking at`
- 動作要具體：不寫 `playing baseball`，寫 `swinging a wooden bat with both hands`
- 如果角色不動，寫 `standing still, facing camera`

## 場景描述規則

- 本系列預設**乾淨淺色背景**（pastel yellow / pastel green / soft white）
- 不要複雜場景，讓注意力集中在角色和物件上
- 如果需要球場，用 `a simplified baseball diamond field with green grass and brown dirt`
- 道具一次最多出現 **1-2 個**

## 光線和風格（固定值）

以下兩行在所有 prompt 中保持不變：

```
Lighting: soft diffused studio lighting, warm tone, no harsh shadows
Style: 3D animated, Pixar-inspired, cheerful and educational mood, clean render
```

## 跨片段一致性技巧

1. **角色卡不改字** — 逐字複製
2. **Frame chaining** — 前一段的最後一幀當下一段的參考圖（如果工具支持）
3. **背景色統一** — 同一集的 3 個 prompt 用同一個背景色
4. **風格行不改字** — lighting 和 style 全系列統一

## Prompt 範例（完整示範）

### 好的 prompt：

```
Close-up shot, static camera.
A cute baseball mascot character with a rounded bean-shaped body, oversized head,
very short stubby limbs, thick clean dark outline, simple dot eyes, small curved smile,
subtle pink blush marks on cheeks, warm red-orange skin color.
The character is roughly 2 heads tall with Xiaohongshu mascot charm
and Power-Pro-like (Jikkyou Pawafuru Puroyakyu) proportions.
Holding a white baseball with red stitching in both hands,
looking at it with a curious expression, head tilted slightly.
On a clean pastel yellow background.
Soft diffused studio lighting, warm tone, no harsh shadows.
Flat clean coloring, thick outline, non-photoreal mascot illustration,
cheerful educational mood, no readable text, no logos, no watermarks.
```

### 不好的 prompt：

```
小紅薯拿著棒球看。
```
（太短、沒有鏡頭、沒有場景、沒有風格、中文可能不被支持）

```
A mascot character in a huge baseball stadium with fans cheering,
holding a bat while also catching a ball, the camera does a 360 orbit
around them while zooming in, dramatic cinematic lighting with lens flares.
```
（太多動作、太多鏡頭運動、場景太複雜、風格不統一）

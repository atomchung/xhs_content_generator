# 棒球小白系列 — 角色設計

日期：2026-04-13
基於：倉庫 `mascot_q` 風格（Style 5 - Mascot Q）

## 角色概念

**名稱：** 小薯（暫定）
**原型：** 小紅書薯隊長 × パワプロ（實況野球）豆形球員
**定位：** 棒球小白系列的固定講解員 / 主角

不是寫實球員，不是普通 chibi，是**帶運動語義的吉祥物角色** — 看一眼就知道「這是在講棒球」。

## 角色規格

### 身體

| 部位 | 描述 |
|------|------|
| 體型 | 圓潤豆形（bean-shaped），像一顆站起來的紅薯 |
| 頭身比 | 約 2 頭身（oversized head），頭佔身體 50% |
| 四肢 | 極短的手腳（very short limbs, stubby），沒有明顯關節 |
| 輪廓 | 粗黑色描邊（thick clean outline），乾淨不毛糙 |

### 臉部

| 部位 | 描述 |
|------|------|
| 眼睛 | 大圓黑點眼（simple dot eyes），間距略寬，在臉部中下方 |
| 嘴巴 | 小弧線嘴，預設微笑。可變化：驚訝（O 嘴）、興奮（D 嘴）、認真（一字嘴） |
| 臉頰 | 兩團淡粉色腮紅（subtle blush marks） |
| 表情系統 | 靠嘴型 + 眼睛大小 + 腮紅深淺控制，不用眉毛 |

### 顏色

| 部位 | 色值參考 | 描述 |
|------|---------|------|
| 身體主色 | 暖紅橘色 | 小紅書品牌色系，飽和但不刺眼 |
| 身體陰影 | 稍深的暖紅色 | 簡單一層陰影，不要複雜光影 |
| 描邊 | 深棕黑色 | 粗線條，統一寬度 |
| 腮紅 | 淡粉色 | 半透明圓形 |
| 眼睛 | 純黑 | 無高光（保持簡潔） |

### 服裝 / 道具

- **預設狀態：** 不穿衣服，裸薯就是完整角色
- **棒球系列道具：** 依場景添加，一次最多一個
  - 棒球手套（褐色）
  - 球棒（木色）
  - 棒球帽（紅色，可加 logo）
  - 棒球（白色紅縫線）
- **規則：** 道具是拿在手上或戴在頭上，不是穿在身上

## Prompt 用角色描述（Character Block）

以下文字在每個影片 prompt 中**逐字複製**，不改動：

```text
A cute baseball mascot character with a rounded bean-shaped body, oversized head,
very short stubby limbs, thick clean dark outline, simple dot eyes, small curved smile,
subtle pink blush marks on cheeks, warm red-orange skin color.
The character is roughly 2 heads tall with Xiaohongshu mascot charm
and Power-Pro-like (Jikkyou Pawafuru Puroyakyu) proportions.
```

### 表情變體（替換 `small curved smile` 部分）

| 表情 | 替換詞 |
|------|--------|
| 開心（預設） | `small curved smile` |
| 好奇 | `curious expression with head tilted slightly` |
| 驚訝 | `surprised wide-open round mouth` |
| 興奮 | `excited big D-shaped open mouth smile` |
| 認真 | `focused determined straight-line mouth` |
| 困惑 | `confused expression with a small squiggle mouth` |

## 風格規則（從 mascot_q 繼承）

- **Flat clean coloring** — 平塗填色，不要漸層渲染
- **Thick outline** — 粗描邊是視覺識別核心
- **Non-photoreal** — 不要寫實、不要光澤 anime 感
- **No mature body proportions** — 永遠保持豆形 2 頭身
- **No cluttered background** — 背景永遠乾淨
- **No readable text / logos / watermarks** — prompt 裡不加文字

# Player Reference Photos

## 用法

1. 把球員照片存到對應資料夾（如 `cameron-boozer/photo.jpg`）
2. Claude Code 會用 Read tool 看圖，自動生成 `appearance.md`
3. 封面 prompt 生成時引用 `appearance.md` 中的描述

## 目錄結構

```
references/players/
  aj-dybantsa/
    photo.jpg          ← 你存入的參照照片（建議正面 + 側面各一張）
    appearance.md      ← AI 看圖後自動生成的外貌描述
  cameron-boozer/
    photo.jpg
    appearance.md
  darryn-peterson/
    photo.jpg
    appearance.md
  caleb-wilson/
    photo.jpg
    appearance.md
```

## appearance.md 格式

AI 看完照片後會自動填寫以下欄位：

| 欄位 | 說明 | 範例 |
|------|------|------|
| 髮型 | 具體描述，不能只寫「短髮」 | 花椰菜頭（頂部蓬鬆捲髮 + 兩側 fade） |
| 髮色 | — | 黑色 |
| 膚色 | 相對描述 + 色調 | 深棕色、中棕偏暖 |
| 臉型 | — | 方臉、長臉、圓臉 |
| 臉部特徵 | 最突出的 2-3 個 | 高顴骨、寬鼻、濃眉 |
| 體型 | 身高體重 + 關鍵詞 | 6'9" 250 lbs，壯碩寬肩 |
| 招牌標記 | 護目鏡、臂套、紋身等 | 右眼周圍傷疤（Elite Eight 受傷） |

## 注意

- 照片選最近的（球員會換髮型）
- 一個球員可以存多張照片，AI 會綜合判斷
- `appearance.md` 隨時可以重新生成（刪掉後存新照片再跑一次）

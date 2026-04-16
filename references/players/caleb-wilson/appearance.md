# Caleb Wilson — 外貌參照

來源：ESPN headshot（AI 自動識別，2026-04-14）
Wikipedia：⚠️ 錯誤——返回的是 UCLA 美式足球同名球員，非 UNC 籃球 Caleb Wilson
狀態：✅ 已照片確認（ESPN）

| 欄位 | 描述 | 信心度 |
|------|------|--------|
| 髮型 | **中長 box braids / 個人辮**——從頭頂分區編成的個人辮，垂掛到耳朵以下，部分辮尾有珠飾/裝飾。是有體積感的垂掛辮，不是貼頭皮的 cornrows | **已確認**（ESPN headshot）|
| 髮色 | 黑色 | **已確認** |
| 膚色 | **深棕色**——與 Dybantsa 接近的深色，明顯深於 Boozer 和 Peterson | **已確認** |
| 臉型 | 偏圓臉，臉頰飽滿 | **已確認** |
| 臉部特徵 | 大眼睛、寬鼻、非常燦爛的笑容（露齒大笑）、臉部輪廓偏柔和圓潤而非銳利 | **已確認** |
| 體型 | 6'10" 215 lbs，長臂展（7 尺）、彈性長肢型 | **已確認**（選秀報告）|
| 招牌標記 | 帶珠飾的 box braids + 燦爛大笑容 | **已確認** |

## Prompt 用描述

```text
DEEP DARK BROWN SKIN — similar depth to Dybantsa, clearly darker than Boozer and Peterson. Round face with full cheeks, LARGE BRIGHT EYES, wide nose, very broad radiant smile showing teeth — his face reads as youthful and expressive rather than sharp or intimidating. HAIR: MEDIUM-LENGTH BOX BRAIDS / INDIVIDUAL PLAITS hanging down past his ears — sectioned braids with visible volume, some braided ends decorated with BEADS or small ornaments. The braids hang and sway with movement. This is NOT flat cornrows against the scalp — these are hanging individual braids with weight and dimension. BUILD: 6'10" 215 lbs, long elastic frame with a 7-foot wingspan — lean but with developing muscle, the second tallest of the four.
```

## 與 PR 現有 prompt 的差異（⚠️ 重大）

| 項目 | PR v6 寫的 | 照片實際 |
|------|-----------|---------|
| 髮型 | ❌「精緻 cornrow 貼頭皮幾何圖案（菱形/鋸齒）」 | **box braids / 個人辮**，是垂掛的，不是貼頭皮的 |
| 辮子特徵 | 「壓平貼頭的圖案型 cornrows」 | 有體積感的懸掛辮 + 辮尾珠飾 |
| 臉型 | 「骨骼結構突出、側臉輪廓銳利」 | **圓臉、臉頰飽滿、輪廓柔和** |

⚠️ PR 把 cornrows 給了 Wilson，但照片是 box braids；把 hanging braids 給了 Peterson，但 Peterson 實際是短 twists。

## Wikipedia Bug

`fetch_player_photo.py` 查 `Caleb_Wilson` 返回 UCLA football 同名球員。腳本需加運動項目消歧義。

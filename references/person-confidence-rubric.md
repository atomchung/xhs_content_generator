# Person Recognition Confidence Rubric

> Version: 2026-04-19 v1
> Purpose: 判斷 AI 生圖模型（MJ / Flux / SD）對某真人的訓練集深度，決定生圖前是否需要跑 photo pipeline
> Scope: 通用 — 適用任何真人主題（運動員 / 藝人 / 政治人物 / 企業家 / KOL）

---

## 評分方式

在任何需要生真人圖的 skill 啟動時，對 prompt 中每個真實人物跑一次信心自評：

### 核心問題
> 「**AI 生圖模型的訓練集裡，有多少這個人的照片**？」
>
> 注意：不是問 Claude 自己認不認得（Claude 知道歷史人物、Claude 讀過的新聞人物），而是問生圖模型（MJ / Flux / SD）訓練時看過多少此人的視覺資料。

### 基礎分數錨點（0-100）

| 分數 | 類型 | 範例 |
|---|---|---|
| 100 | 全球 icon | Obama / Taylor Swift / LeBron James / Messi / Elon Musk |
| 85 | 主流名人，長期曝光 5 年以上 | Nikola Jokic / Jimmy Fallon / Tim Cook / Zendaya |
| 65 | 領域內知名但破圈有限 | Rui Hachimura / 中堅期歌手 / unicorn 創始人 |
| 45 | 有曝光但臉譜不穩 | Cade Cunningham / 新生代藝人 / Series B CEO |
| 25 | 少量公開照片 | 大學球員 / G League / 地方政治人物 |
| 5 | 幾乎無訓練資料 | 未進聯盟選秀生 / 小眾 KOL / 非公眾人物 |

### 扣分條件（可累加）

| 條件 | 扣分 | 理由 |
|---|---|---|
| 2024 年後才進入主流視野 | -10 | 訓練集可能來不及涵蓋 |
| 同名亞洲人（漢字/拼音歧義）| -15 | AI 容易畫錯人 |
| 形象高度依賴造型（化妝 / 舞台服 / 制服）| -10 | 脫下造型後臉譜不穩 |

---

## 輸出格式（JSON）

Skill 應要求 Claude 回傳：

```json
{
  "person": "person name",
  "confidence": 65,
  "tier": "MED",
  "reason": "Japanese-Zimbabwean Lakers rotation player, 6 seasons in NBA but not All-Star level.",
  "anchors_suggestion": "Japanese-Zimbabwean heritage, 6'8 lean build, short black hair, angular jawline"
}
```

- `confidence` 整數 0-100
- `tier` 取值：`HIGH` / `MED` / `LOW`
- `reason` 一句話解釋
- `anchors_suggestion` 僅當 `tier == "MED"` 時填，否則 `null`

### Tier 對照

```
confidence >= 75  →  tier = "HIGH"
40 <= confidence < 75  →  tier = "MED"
confidence < 40   →  tier = "LOW"
```

---

## 三檔行為

### 🟢 HIGH（75+）
直接在 prompt 中用名字，不加額外外貌錨點。

範例 prompt 片段：
```
LeBron James mid-air tomahawk dunk, ...
```

### 🟡 MED（40-74）
1. 在 prompt 中加入 `anchors_suggestion` 作為外貌錨點（括號內）
2. 在對話中提示用戶信心度

範例 prompt 片段：
```
Rui Hachimura (Japanese-Zimbabwean heritage, 6'8 lean build, short black hair, 
angular jawline) mid-range turnaround jumper, ...
```

對話提示模板：
```
⚠️ {person_name} 辨識度 {score}（MED）
已自動加入外貌錨點：{anchors_suggestion}
若生圖後辨識度仍不理想，可手動跑 photo pipeline 取得更精準描述。
```

### 🔴 LOW（0-39）
**不直接輸出 prompt**，先向用戶確認：

```
🔴 {person_name} 辨識度 {score}（LOW）
AI 生圖模型對此人辨識度不足，直接用名字會畫錯臉。

選擇：
(A) 自動跑 photo pipeline（ESPN 首選 → Wikipedia 備援）
    → python scripts/fetch_player_photo.py --player "{name}"
(B) 手動提供此人 3-5 張參考照片路徑
(C) 忽略辨識度，直接用名字生（預期會畫錯臉）
```

---

## Photo Pipeline 整合

當 `tier == "LOW"` 且用戶選 (A)，跑：

```bash
python scripts/fetch_player_photo.py --player "{name}" [--espn-id {id}]
```

優先順序（運動帳號）：
1. **ESPN** — 官方 headshot，解析度穩定，帶 player_id 時最準
2. **Wikipedia API** — 無需 ID，通用備援
3. **（未來）Google Images 首圖** — 最後手段

Pipeline 產物：
- `references/players/{slug}/espn_headshot.png`（或 `wikipedia_photo.jpg`）
- `references/players/{slug}/appearance.md`（3-5 句外貌描述，由 Claude 讀圖後寫）

生圖 prompt 生成時 embed `appearance.md` 的描述替代 `anchors_suggestion`。

---

## 決策範例（NBA 主題）

| 人物 | 基礎分 | 扣分 | 最終 | Tier | 做法 |
|---|---|---|---|---|---|
| LeBron James | 100 | 0 | **100** | 🟢 | 只寫名字 |
| Nikola Jokic | 85 | 0 | **85** | 🟢 | 只寫名字 |
| Rui Hachimura | 65 | 0 | **65** | 🟡 | 加外貌錨點（實測 OK 可降為 HIGH）|
| Cade Cunningham | 45 | 0 | **45** | 🟡 | 加外貌錨點 |
| Luke Kennard | 45 | 0 | **45** | 🟡 | 加外貌錨點 |
| Cooper Flagg | 25 | -10（2024+）| **15** | 🔴 | **必跑 photo pipeline** |
| Ace Bailey | 25 | -10 | **15** | 🔴 | **必跑 photo pipeline** |
| Dylan Harper | 25 | -10 | **15** | 🔴 | **必跑 photo pipeline** |
| VJ Edgecombe | 25 | -10 | **15** | 🔴 | **必跑 photo pipeline** |

---

## 反饋校準日誌

當生圖實測結果和 rubric 預期不符時，在此記錄，用於未來版本調整 rubric 分數錨點。

| 日期 | 人物 | Rubric 預測 | 實測結果 | 應調整 |
|---|---|---|---|---|
| 2026-04-19 | Rui Hachimura | MED（65）| 辨識度實際 OK | 可考慮錨點列為 70+ 直接 HIGH |

---

## 版本歷史

- **2026-04-19 v1**：首版。ESPN 為運動帳號首選 photo source。Rui 實測 OK 註記。

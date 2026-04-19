# Player Appearance References

人物外貌具象化的全自動流程。AI 自己抓照片、自己看、自己描述、自己寫進 prompt。

## 全自動流程（本地 Claude Code）

```
Step 1: 抓照片
$ python scripts/fetch_player_photo.py --batch references/players/nba-tanking-four-kings.json

Step 2: AI 看圖 → 生成描述（Claude Code 自動執行）
Read("references/players/cameron-boozer/espn_headshot.png")
→ AI 描述外貌特徵
→ Write("references/players/cameron-boozer/appearance.md")

Step 3: 寫 prompt 時引用 appearance.md
Read("references/players/cameron-boozer/appearance.md")
→ 自動寫入封面 prompt 的人物描述段落
```

零人工介入。從球員名字到完整 prompt，全自動。

## 腳本用法

### 單人模式

```bash
# 已知 ESPN ID（最快最穩）
python scripts/fetch_player_photo.py "Cameron Boozer" \
    --espn-id 5041935 \
    --school Duke \
    --output references/players/cameron-boozer

# 不知道 ESPN ID（自動搜尋）
python scripts/fetch_player_photo.py "AJ Dybantsa" \
    --school BYU \
    --output references/players/aj-dybantsa
```

### 批次模式

```bash
python scripts/fetch_player_photo.py --batch references/players/nba-tanking-four-kings.json
```

Manifest 格式：
```json
[
    {
        "name": "Cameron Boozer",
        "school": "Duke",
        "espn_id": "5041935",
        "output": "references/players/cameron-boozer"
    }
]
```

## 目錄結構

```
references/players/
  nba-tanking-four-kings.json    ← 批次下載清單
  aj-dybantsa/
    espn_headshot.png            ← fetch_player_photo.py 自動下載
    wikipedia.jpg                ← fetch_player_photo.py 自動下載
    appearance.md                ← Claude Code 看圖後自動生成
  cameron-boozer/
    espn_headshot.png
    appearance.md
  ...
```

## Claude Code 看圖後的 appearance.md 格式

```markdown
# {Player Name} — 外貌參照

來源：ESPN headshot + Wikipedia（AI 自動識別）

| 欄位 | 描述 |
|------|------|
| 髮型 | 花椰菜頭（頂部蓬鬆捲髮 + 兩側 fade） |
| 髮色 | 黑色 |
| 膚色 | 中棕色帶暖色調 |
| 臉型 | 方臉 |
| 臉部特徵 | 強壯下顎線、對稱五官 |
| 體型 | 6'9" 250 lbs，壯碩寬肩 |
| 招牌標記 | 無 |

## Prompt 用描述

（AI 根據以上特徵自動生成一段可直接嵌入 image prompt 的英文描述）
```

## 圖片來源優先級

1. **ESPN headshot**（最穩定，URL 格式固定，只需 player ID）
2. **Wikipedia**（品質好，但不是每個球員都有）
3. **學校官網 roster**（未來擴充）

## 雲端環境限制

在受限環境（如 Claude Code Web）中，`fetch_player_photo.py` 無法執行（egress proxy 擋外部網站）。
此時退化為手動模式：用戶貼照片到對話中或存到目錄，AI 用 Read 看圖。
詳見 issue #11。

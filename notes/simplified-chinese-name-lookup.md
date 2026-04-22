# Simplified Chinese Name Lookup

## 為什麼這份 note 存在

寫任何涉及外國公眾人物（球員 / 高管 / 藝人 / 政治人物 / KOL）的小紅書貼文時，
**英文名的 naive pinyin 常常不是中文讀者認的名字**。用錯了不只是搜不到，整篇氣氛也會歪。

## 硬規則

下筆寫 post.md 之前，必須：

1. 在 `research/fact_pack.md` 的「Terms to translate」段，列出貼文會提到的**每一個外國人**的：
   - 英文名
   - 小紅書 / 微博 / 百度上**實際在用**的簡中名（不是自己按發音拼的）
   - 來源平台（在哪驗證的）
2. 找不到統一簡中名的（太新、太冷門），**保留英文**，不要自己造音譯
3. 寫 post.md 時嚴格套用 fact_pack 的對應表，不用記憶、不用猜

## 驗證方法（最快路徑）

- 小紅書 app 搜索框直接打**英文名**，看 AI 總結卡 + 熱門筆記標題出現的中文名
- 百度百科條目標題（如果有官方條目）
- 微博話題頁的 hashtag 用語

## 已知 case 表

| 人物 | Naive pinyin（錯） | 已建立的簡中名（對）| 來源 | 備註 |
|---|---|---|---|---|
| Adam Silver | 希尔弗 | **亚当·肖华**（後續只用 肖华） | 小紅書 AI 總結 / 百度 | NBA 總裁，媒體統一用「肖华」 |

> 新增一個 case 時，按同樣欄位加一行。日期放在 case log 段，這裡只留映射表。

## 流程 checklist（發布前過）

- [ ] fact_pack.md 有 `## Terms to translate` 段
- [ ] 該段列出 post.md 會出現的每一個外國人名
- [ ] 每一項都標了 source（哪個平台驗證的）
- [ ] post.md 裡的中文名與該表一一對應，不存在該表沒有的版本

## Case log

### 2026-04-22 — silver-gambling-ledger

- post.md 草稿用了「希尔弗」（naive pinyin）共 4 處，跑完完整 checklist 才暴露
- 用戶以小紅書搜索截圖（NBA 總裁 AI 總結卡）糾正：**亚当·肖华**
- 修法：4 處全部替換，首次全稱「亚当·肖华」，後續「肖华」；自檢 checklist 同步更新
- 觸發本 note 建立 + 加入案例表
- Workspace（branch-only）：`demo_posts/2026-04-20-silver-gambling-ledger/`

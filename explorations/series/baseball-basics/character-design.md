# 小紅薯棒球系列 — 角色設計文件

> 建立日期：2026-04-12
> 用途：棒球教學影片系列《棒球小白急救包》的統一角色設計
> 更新：2026-04-13 — 校正造型（奶白色身體、大圓眼、球衣改 Din logo）

---

## 基礎造型（Base Character）

### 中文設定

- **體型**：蛋形／梨形，上窄下寬，胖嘟嘟，身體有弧度光影層次
- **顏色**：奶白色（cream / off-white），質感柔軟有漸層
- **四肢**：極短的小手小腳，像貼在身體側邊的小突起，沒有脖子
- **眼睛**：大黑圓眼，有白色高光點，閃亮有神（參考原版咖啡色土豆的大眼）
- **鼻子**：兩個極小的黑色點點，在眼睛下方
- **臉頰**：淡粉色腮紅
- **頭頂**：一片嫩綠色小葉子（招牌特徵，任何裝備都不能完全遮住）
- **質感**：3D 漸層軟玩具感，有柔和光澤，不是霧面

### 英文 Prompt 固定描述（每個 prompt 必帶）

```
A cute round cream-colored dumpling-shaped mascot with a small green sprout on
top of its head, big round sparkling black eyes with a white highlight dot,
tiny dot nostrils, soft pink blush on both cheeks, smooth egg-shaped body
with no neck, tiny stubby arms and legs. Soft plush toy texture with gentle
gradient shading and subtle sheen.
```

> ⚠️ 眼睛：回歸**大圓眼 + 高光點**（大而有神），不是小彎弧。
> ⚠️ 身體：**奶白色**，不是紅棕色。紅色來自球衣，不是身體。

---

## 棒球裝備系統

### 隊服配色 — 紅襪風格（Red Sox Inspired）

| 部位 | 顏色 | 說明 |
|------|------|------|
| 主球衣 | 深紅色（crimson red） | 紅襪 alternate 配色 |
| 球衣 logo | 白色 **"Din"** 字，胸前 | 品牌識別，取代 "RED" |
| 球帽 | 深紅色帽身 + 白帽沿 | 帽頂留小孔讓綠葉伸出 |
| 球褲 | 白色 | 與深紅球衣形成對比 |
| 球鞋 | 深紅色 + 白色鞋底 | 統一配色 |

> **"Din" logo 說明**：字體風格參考球隊 wordmark，白色粗體，印在球衣胸前正中。
> AI 文字渲染風險：三個字母比 "RED" 多一個字母，渲染穩定性略低，若跑歪改描述為 wordmark-style white letters on chest。

### 棒球帽的特殊處理

> **帽頂開口規則**：所有戴帽造型，帽頂一律有小開口，讓綠葉自然伸出。
> 這是小紅薯最強的辨識特徵，任何配件都不能遮住。

---

## 四種場上造型

### 1. 投手（Pitcher）

**配件**：球帽 + 球衣 + 球褲 + 棒球手套（戴左手，右手持球）

**英文描述**：
```
wearing a deep red baseball cap with the green sprout poking through the top,
a deep crimson red baseball jersey with white "Din" letters on the chest,
white baseball pants, red cleats, a round brown fielder's glove on its left
hand, gripping a white baseball in its right hand
```

**關鍵動作特徵**：
- 投球前：左腳抬高膝蓋，重心後傾蓄力
- 投球瞬間：右手臂由上往下揮，身體前傾爆發
- 投球後：follow-through 姿勢，前傾，手臂自然下垂

---

### 2. 打者（Batter）

**配件**：打擊頭盔（取代帽子）+ 球衣 + 球褲 + 球棒（雙手持）

**頭盔特殊處理**：深紅色單耳頭盔，側邊小缺口讓綠葉伸出

**英文描述**：
```
wearing a deep red single-flap batting helmet with the green sprout poking
out from a small gap, a deep crimson red baseball jersey with white "Din"
on the chest, white baseball pants, holding a round wooden baseball bat
with both tiny hands
```

**關鍵動作特徵**：
- 準備：寬站姿，球棒舉在肩上，大眼睛盯球
- 揮棒：全身扭轉，球棒水平揮過，圓身體誇張旋轉
- 打中：球飛出，身體繼續旋轉一圈

---

### 3. 捕手（Catcher）

**配件**：捕手頭盔＋面罩 + 護胸 + 腿護 + 捕手手套（圓形大手套）

**面罩特殊處理**：深紅色頭盔配金屬格柵面罩，可透出大眼睛表情。綠葉從頭盔頂部伸出。

**英文描述**：
```
wearing a deep red catcher's helmet with a metal face guard showing its big
round eyes, chest protector, shin guards, the green sprout poking through
the top of the helmet, crouching in catcher's stance with a large round
catcher's mitt
```

**關鍵動作特徵**：
- 蹲姿：兩腿張開，身體前傾，手套朝外展示
- 比暗號：右手在腿間比出手指暗號
- 接球：手套往內縮，framing 動作

---

### 4. 外野手 / 守備通用（Fielder）

**配件**：球帽 + 球衣 + 球褲 + 外野手套（戴左手）

**英文描述**：
```
wearing a deep red baseball cap with the green sprout poking through the top,
a deep crimson red baseball jersey with white "Din" on the chest, white
baseball pants, wearing a brown fielder's glove on its left hand
```

---

## 情緒表情系統

| 情緒 | 身體 | 綠葉 | 眼睛 |
|------|------|------|------|
| 開心 | 上下彈跳，squash & stretch | 左右搖擺 | 大圓眼，彎成弧形 |
| 得意 | 挺胸，微微變大 | 直立挺翹 | 大眼閃光點變亮 |
| 難過/沮喪 | 身體向下塌陷，像洩氣球 | 垂下來 | 大眼向下看，無高光 |
| 緊張 | 身體微微顫抖 | 微微搖晃 | 大眼睜更大 |
| 不可置信 | 雙手舉起，身體後仰 | 往後甩 | 大眼高光點消失一瞬 |

---

## Prompt 組裝模板

```
[固定角色描述] + [場上造型裝備] + [動作描述] + [場景] + [鏡頭] + [風格]
```

**範例（投手版）**：
```
Single continuous shot. A cute round cream-colored dumpling-shaped mascot
with a small green sprout poking through the top of a deep red baseball cap,
big round sparkling black eyes with a white highlight dot, tiny dot nostrils,
soft pink blush cheeks, smooth egg-shaped body, tiny stubby arms. Soft plush
gradient texture. Wearing a deep crimson red baseball jersey with white "Din"
on the chest, white baseball pants, red cleats. [動作...] [場景...] [鏡頭...]
3D Pixar-style kawaii animation.
```

---

## 設計紀律

1. **綠葉永遠可見** — 不管戴什麼帽子，綠葉必須從開口伸出
2. **身體是奶白色** — 永遠是 cream / off-white，紅色只在球衣
3. **眼睛要大** — 大圓眼 + 高光點，這是角色表情力的來源
4. **Din logo 在胸前** — 白色，球衣正中
5. **不要嘴巴** — 情緒靠眼睛＋身體＋綠葉表達
6. **圓形物理** — 揮棒/投球用 squash & stretch，誇張化圓形身體的彈性

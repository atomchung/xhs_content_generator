# Silver 賭博帳本 封面 prompt

## v3 — 鎖定 Scorsese 海報風 × 4 構圖變體

**風格鎖死**（所有變體共用）：
Theatrical movie-poster illustration in the style of late-1990s Scorsese crime-cinema posters ("Casino", "Uncut Gems", "Rounders"), painted and posterized rather than photographed.
—— painted / oil brushwork / posterized 色塊，而非 photoreal。palette 走深紅 + 霓虹金 + 重黑 + 冷青點綴。

**變體 = 4 個構圖方向**，挑一個去生，不合就切下一個。

| | 構圖方向 | 文化 reference | 風險 / trade-off |
|---|---|---|---|
| A | 賭神 1989 致敬（周潤發版） | Hong Kong 賭博電影 icon | **犧牲 Silver 光頭錨點**換周潤發髮型 |
| B | 撲克桌對峙 | Casino / Rounders 橫向對決 | 需要「對面陰影人」不能過度描繪（否則誹謗） |
| C | 撲克牌扇形揭示 | 海報式 iconographic | 每張牌的圖示要抽象化，不能畫真人臉 |
| D | 籌碼雪崩 | Uncut Gems 張力 | 動態感強但可能模糊 Silver 臉 |

## Person Recognition Gate

- Adam Silver 中文圈視覺辨識度：**MED**，信心度約 55/100
- **錨點（B / C / D 版維持）**：middle-aged bald man、thin rectangular rimless glasses、narrow elongated angular face、dark well-tailored charcoal suit、composed but burdened expression
- **A 版錨點替換**：保留眼鏡 + 角面 + 西裝，但光頭換成周潤發《賭神》slicked-back 黑髮 + 賭神招牌笑容。這個 trade-off 刻意為之，見 A 版說明。

---

## Version A：賭神 1989 致敬（周潤發版）

### 為什麼選它
- 文化上最 hit 中文受眾對「賭博電影」的集體記憶
- 構圖意義：把 Silver 擺進「賭神」的位置，**論述直接寫在視覺裡** —— 他就是 NBA 的賭博之王
- post 收尾「你會簽這筆生意嗎」配這個視覺最到位

### Trade-off
- **光頭錨點被周潤發髮型取代**。用戶中文圈可能不太認 bald Silver，但會立刻認出賭神視覺 → 這是用 cultural icon 替代 personal icon 的刻意決策
- 如果堅持保光頭：砍掉「slicked-back jet-black hair」那一段，保留其他（微笑、蝴蝶結、撲克牌扇）即可降格到 Casino 風

### 構圖
- 中央半身肖像，略低角度
- Silver 戴細框方眼鏡、角面、slicked-back 黑髮（周潤發式）、咧嘴自信微笑、白齒
- 黑西裝 + 白襯衫 + 深紅蝴蝶結，左手小指一枚翡翠戒指
- 胸前緊握一把撲克牌扇，其中一張被兩指捏起半出牌背面對鏡頭
- 背景：深紅色絲絨賭場幕、暖金聚光燈由背後打頭部光圈

### Final Prompt

```text
Theatrical movie-poster illustration in the style of late-1990s Scorsese crime-cinema posters ("Casino", "Uncut Gems", "Rounders"), painted and posterized rather than photographed, with a deliberate tribute to 1989 Hong Kong gambling-film iconography (the Chow Yun-fat "God of Gamblers" visual codes). Central subject: Adam Silver reimagined as a charismatic gambling kingpin — narrow elongated angular face, thin rectangular rimless glasses intact, re-styled with pristine slicked-back glossy jet-black hair parted cleanly on the side (the signature 1980s Hong Kong leading-man hair, zero hairline recession), a wide confident toothy grin showing white teeth, expression reading as amused, in-control, dangerously charming. He wears a sharply tailored black tuxedo with a crisp white dress shirt, a deep crimson bow tie, a single jade ring on his left pinky visible. He holds a tight fan of playing cards up near his chest, the cards' backs facing the viewer, one card pinched between finger and thumb mid-reveal. Medium close-up, slightly low angle, centered composition. Background: deep crimson velvet casino backdrop with out-of-focus gilded columns and a warm amber spotlight haloing his head from behind, painted with Scorsese-poster flat posterized brushwork. Palette: deep crimson red, heavy black, Vegas-neon amber gold, small cold cyan accent only on the card backs. Heavy painterly texture, grainy 1990s film-poster print quality, 3:4 vertical movie-poster composition, cinematic theatrical framing, high-stakes noir mood, no readable text anywhere in the frame. --ar 3:4 --stylize 250
```

---

## Version B：撲克桌對峙

### 為什麼選它
- 橫向張力，敘事感最強 —— 一眼看到「Silver 坐在桌一端 vs 對面陰影人」
- 桌面二分（左籌碼 / 右案件）直接視覺化 post 的「收入帳本 vs 風險帳本」
- Casino / Rounders 的經典戲劇式文法

### 構圖
- 眼平視角，跨桌視角
- Silver 近景這邊：光頭、角面、深色西裝、雙手推一疊金籌碼向前
- 對面：三個陰影剪影（只剪影、不描繪五官、不可辨識 → 避開誹謗）
- 桌中央：左半金籌碼 + 鈔票，右半案件檔案 + 法槌 + 傳票
- 上方雪茄煙從金色聚光燈穿過

### Final Prompt

```text
Theatrical movie-poster illustration in the style of late-1990s Scorsese crime-cinema posters ("Casino", "Uncut Gems", "Rounders"), painted and posterized rather than photographed. Wide symmetrical dramatic poker-table showdown composition viewed from eye level across the green felt of a long casino table. Near side facing the camera: Adam Silver, middle-aged bald man with thin rectangular rimless glasses, narrow elongated angular face, wearing a sharply tailored dark charcoal suit, rendered in oil-painting brushwork and posterized flat color planes, dramatically lit from above, expression composed but intensely burdened, his hands pushing a single tall stack of polished gold casino chips forward across the felt. Opposite him at the far side of the table, three indistinct anonymous shadow silhouettes of seated figures rendered purely in silhouette against a deep crimson haze, no readable faces, no recognizable identities, no visible skin tones. The table's center is already cluttered: LEFT half piled with gold-rimmed chips and fanned hundred-dollar bills; RIGHT half strewn with opened case files, a judge's gavel, scattered subpoena envelopes, a pair of handcuffs partly buried in the paperwork. A single curl of cigar smoke drifts through the upper frame catching an amber Vegas-neon light shaft from above. Palette: deep crimson red, heavy black, amber gold, single cold cyan accent. Heavy painterly texture, grainy 1990s film-poster print quality, 3:4 vertical movie-poster composition, cinematic noir mood, no readable text anywhere in the frame. --ar 3:4 --stylize 250
```

---

## Version C：撲克牌扇形揭示（iconographic）

### 為什麼選它
- 每張撲克牌 = 一個案件證物，直接把 post 的「風險帳本」內容放進視覺
- Scorsese 海報愛用的分格 icon 文法，小紅書 feed 裡識別度高
- Silver 低調站在上半，撲克牌扇佔下半，視線引導自然

### 構圖
- 垂直構圖
- 上半：Silver 中遠景，光頭、角面、西裝，頂光打下，背影投射銳利
- 下半：一把巨大撲克牌扇橫跨畫布底三分之一，每張牌面是一個抽象 icon：
  - 1：NBA 球員剪影（抽象，不指涉真人）
  - 2：籃球場上浮出的球衣號碼
  - 3：場邊教練陰影
  - 4：法槌
  - 5：法庭剪影
  - 6：遠方拉斯維加斯 skyline
- Silver 右手向下伸出，兩指捏起其中一張牌微往前拉

### Final Prompt

```text
Theatrical movie-poster illustration in the style of late-1990s Scorsese crime-cinema posters ("Casino", "Uncut Gems", "Rounders"), painted and posterized rather than photographed. Vertical 3:4 composition. UPPER HALF: Adam Silver standing centered, medium-long shot, middle-aged bald man with thin rectangular rimless glasses, narrow elongated angular face, wearing a sharply tailored dark charcoal suit, composed burdened expression, lit dramatically from above with a single vertical shaft of amber Vegas-neon light throwing a sharp silhouette behind him. LOWER HALF: an oversized fan of six giant playing cards spreads across the bottom third of the frame, each card's face clearly illustrated with a different symbolic icon rendered in the same posterized painted style — card 1: an abstract faceless silhouette of a young player in a generic basketball uniform; card 2: a prominent basketball jersey number floating on a court; card 3: a shadowy coaching figure on a sideline; card 4: a judge's gavel resting on paperwork; card 5: a courtroom interior silhouette; card 6: a distant Las Vegas-style skyline at dusk. The card faces use crimson, amber gold, and black only. No readable numbers, no English text, no recognizable real faces. Silver's right hand reaches down and pinches one of the cards, pulling it slightly forward toward the viewer, dramatically lit. Palette: deep crimson, heavy black, Vegas-neon amber gold, single cold cyan accent at the edges. Heavy painterly texture, grainy 1990s film-poster print quality, theatrical noir mood, no readable text anywhere in the frame. --ar 3:4 --stylize 250
```

---

## Version D：籌碼雪崩

### 為什麼選它
- 動態感最強，觀眾在 feed 裡滑過去會停
- Uncut Gems 式焦慮張力
- 雪崩往下壓的方向感暗示「代價正在到來」

### 構圖
- Silver 中央頂天立地，雙臂微張向兩側彷彿在穩住場面
- 畫面右上角 → 左下角斜向：一場凝結在中途的籌碼 + 鈔票雪崩，畫筆式 motion-blur
- 雪崩落地處（左下）：撕毀的合約、打開的案件檔案、一把半埋在紙堆裡的法槌
- 左上角遠景：一面抽象色塊化的贊助商 logo 牆

### Final Prompt

```text
Theatrical movie-poster illustration in the style of late-1990s Scorsese crime-cinema posters ("Casino", "Uncut Gems", "Rounders"), painted and posterized rather than photographed. Central subject: Adam Silver, middle-aged bald man with thin rectangular rimless glasses, narrow elongated angular face, wearing a sharply tailored dark charcoal suit, rendered with deliberate oil-painting brushwork and posterized flat color planes, standing dead-center filling the vertical composition, arms slightly open at his sides as if bracing, expression stoic but visibly burdened, dramatic low amber uplight on his face from below. Around and above him: a frozen mid-cascade tsunami of glossy casino chips and bundles of hundred-dollar bills tumbling diagonally from the upper-right corner down to the lower-left, captured in painterly motion-blur streaks. Where the chips land near the lower-left, they pile onto a scattered heap of torn contracts, opened case files, and a single judge's gavel half-buried in the debris. Upper-left corner: a faint branding wall of abstract out-of-focus sportsbook-style logos reduced to painted colored shapes (no readable text, no identifiable brand). Palette: deep crimson red, heavy black, Vegas-neon amber gold, single cold cyan accent. Heavy painterly texture, grainy 1990s film-poster print quality, 3:4 vertical movie-poster composition, dramatic cinematic motion, theatrical noir mood, no readable text anywhere in the frame. --ar 3:4 --stylize 250
```

---

## 共通不要動

- Scorsese illustrated poster 鎖死 —— painted / posterized / 非 photoreal（這一層如果破了，真人感就回來了）
- B / C / D 的 Silver 外貌錨點（bald / thin rectangular glasses / narrow elongated angular face / charcoal suit）
- A 的周潤發替換錨點（slicked-back black hair / confident smile / tuxedo / jade pinky）
- palette：deep crimson red + heavy black + amber gold + single cold cyan accent
- 3:4 --stylize 250（硬規則）
- 零可讀文字（標題版式卡另外加）
- 真實球員 / 教練 / 官員五官：**不可描繪**，只能用匿名剪影或抽象 icon（誹謗風險）

## 如果要繼續改

- **A 版太 campy**：砍「dangerously charming」留「measured and in-control」；紅色從絲絨背景收到只剩蝴蝶結；拉回更 grounded 的 Casino Ace Rothstein feeling
- **B 版對面人影太弱**：把 `three indistinct shadow silhouettes` 改成 `three hooded figures in silhouette with only the glow of their chips visible`，增加神秘感
- **C 版牌上 icon 太抽象**：加一張 `large bold dollar sign` 作第七張牌，強化「這是錢的故事」
- **D 版太混亂**：把籌碼雪崩方向改為單方向垂直落下（上→下），動作感保留但更乾淨

## 推薦優先序

1. **C（撲克牌扇形）** — 最對位 post 的「帐本」敘事（每張牌 = 一個 case）
2. **B（撲克桌對峙）** — 敘事張力最強，對面陰影人留空間給讀者填上「Rozier / Billups / Jones」
3. **A（賭神致敬）** — cultural hit 最高但最冒險（光頭錨點被換）
4. **D（籌碼雪崩）** — 動態感強但敘事稍鬆

先跑 C，不行切 B，想玩文化梗跑 A，純視覺衝擊跑 D。

## 版本歷史

- v1（commit `b8ba377`）：editorial photo portrait + 天平。真人感太強、天平無聊，已退役。
- v2（commit `56d6a50`）：Kaiji manga + Scorsese poster 雙版。Scorsese 方向被採用，Kaiji 風收起。
- v3（本版）：Scorsese 鎖定，出 4 構圖變體。

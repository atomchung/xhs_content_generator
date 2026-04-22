# Silver 賭博帳本 封面 prompt

## 推薦風格（v2 — 換方向）

v1 走 editorial photo portrait + 天平，被判定真人感太強、天平構圖無聊。
v2 改走兩個動漫 / 電影海報方向，主要差別：

- **降真人感**：全部走 illustration / painted poster，不做 photoreal
- **換構圖**：天平換成**賭桌俯角**，桌面直接一分為二（左籌碼、右案件檔案），更具體、更具敘事、直接 hit 「賭博」的視覺預期
- **加戲劇張力**：借賭博類動漫 / 電影海報的成熟視覺語彙

推薦順序：**A（福本伸行 Kaiji 風）優先**，B（Scorsese Casino 海報風）備用。

## Person Recognition Gate

- Adam Silver 中文圈視覺辨識度：**MED**，信心度約 55/100
- 外貌錨點（v2 維持，但改為插畫/海報風格化呈現，不做 photoreal）：
  middle-aged bald man、thin rectangular rimless glasses、narrow elongated angular face、dark well-tailored charcoal suit、composed but intensely burdened expression
- 不跑 photo pipeline（MED tier）

---

## Version A：福本伸行《賭博默示錄》風（首選）

### 為什麼選它
- Kaiji / Akagi 是「賭博漫畫」的代名詞，文化上直接對位這篇的題目
- 福本風格標誌：極度拉長的下巴輪廓、銳利角面、濃重交叉陰影線、一顆汗珠、「ザワ…ザワ…」緊張線條
- Silver 在這個風格下就變成「做了個巨大決定、現在正看著賭桌的男人」—— 這就是 post 的 H04 role shift 原生題材
- 黑白紅三色為主 + 金色點綴，跟小紅書 feed 裡的照片類封面形成強烈對比

### Final Prompt

```text
Ultra-high-contrast manga illustration in the signature Fukumoto Nobuyuki "Kaiji / Akagi" gambling-manga style. Subject: Adam Silver rendered as a manga character — middle-aged bald man, thin rectangular rimless glasses, pronounced narrow angular face with exaggerated vertical elongation and sharp pointed chin, stylized dramatic cross-hatching on shadows, heavy inked linework, a single bead of sweat tracing his jawline, measured but intensely burdened expression, eyes deep-set with sharp highlights. He sits at the far end of a long underground casino gambling table shown in a steep dramatic overhead diagonal perspective. The table surface is split precisely down the middle: LEFT half piled with towering leaning stacks of polished casino chips and fanned-out bundles of banknotes, glowing with a warm gold accent, faint blurred neon sportsbook-style signage as abstract colored shapes in the far background (no readable logos, no readable text anywhere); RIGHT half strewn with opened case files, a torn NBA contract, a judge's gavel resting on a pile of subpoena envelopes, the sharp silhouette of handcuffs. Above the scene, classic Fukumoto-style jagged tension effect lines radiating from the subject and rendered as stylized ink streaks. Palette strictly black, white, deep crimson red, and a single gold accent on the chips. Heavy screentone dot halftones, exaggerated manga shading, expressive angular linework, no color outside the restricted palette, no readable text or English words anywhere in the frame, 3:4 vertical manga cover composition. --ar 3:4 --stylize 250
```

---

## Version B：Scorsese Casino / Uncut Gems 海報風（備用）

### 為什麼備用
- 如果 A 出圖太漫畫風、偏離 NBA 議題的嚴肅感，B 更「新聞類題材 + 電影感」
- illustrated movie poster 而非 photoreal，一樣能降真人感
- 霓虹紅 / 金 / 黑三色，賭場語彙 + 劇場感
- 中央頂天立地肖像 + 散落籌碼/撲克/輪盤 —— 電影海報的標準文法，小紅書讀者對這個 composition 很熟悉

### Final Prompt

```text
Theatrical movie-poster illustration in the style of late-1990s Scorsese crime-cinema posters ("Casino", "Uncut Gems", "Rounders"), painted and posterized rather than photographed. Central subject: Adam Silver, middle-aged bald man with thin rectangular rimless glasses, narrow elongated angular face, wearing a sharply tailored dark charcoal suit, rendered with deliberate oil-painting brushwork and posterized flat color planes, never photorealistic. He stands dead-center filling the vertical composition, medium-long shot from slightly low angle, backlit by a single vertical shaft of deep amber-gold Vegas-neon light from behind that throws his silhouette sharp against the frame. Around him, a dynamic symmetric scatter: a wide fan of playing cards mid-fall across the lower foreground, a cascade of casino chips tumbling through the front plane, a half-visible roulette wheel glowing red in the lower-left corner, and the upper corners framed with ghostly translucent iconographic silhouettes — upper LEFT: a glowing trophy and a dollar sign; upper RIGHT: a judge's gavel above a handcuff outline. Palette: deep crimson red, heavy black, Vegas-neon amber gold, with a single cold cyan accent at the edges. Heavy painterly texture, grainy 1990s film-poster print quality, 3:4 vertical movie-poster composition, dramatic cinematic framing, high-stakes noir mood, no readable text anywhere in the frame. --ar 3:4 --stylize 250
```

---

## 如果要繼續改

### 兩版共通的 "不要動"
- Silver 的外貌錨點（bald / thin rectangular glasses / narrow elongated angular face / dark charcoal suit / composed but burdened）
- 賭桌 / 撲克 / 籌碼 / 輪盤 / 法槌 / 手銬 的視覺語彙（這是整張圖的敘事骨架）
- 3:4 --stylize 250（硬規則）
- 零可讀文字（標題另外用版式卡加，不在生圖裡）

### A（Kaiji）優先改什麼
- 如果「ザワ…」緊張線條太少（氣氛不夠），加 `radiating angular tension lines in heavy black ink strongly fanning outward`
- 如果右半「案件檔案」看起來太弱，把 `case files` 換成 `a courtroom witness stand silhouette in the background`
- 如果紅色太少，把紅色從 accent 提升為 LEFT 半邊的主色（chips 變紅籌，金色退位）

### B（Casino）優先改什麼
- 如果畫面太像 Vegas 廣告，把 `Vegas-neon amber-gold` 改為 `muted amber with crimson shadows`
- 如果撲克牌分量太大，砍掉 fan of playing cards，只留 chips + roulette
- 如果電影感太誇張，把 `late-1990s Scorsese` 改為 `early-2020s arthouse crime poster minimalism`

---

## 歷史版本（keepsake，不用）

v1 走 editorial photo portrait + 天平，見 git history commit `b8ba377`。被判定真人感太強、天平太乏味，留作檔案。

# Silver 賭博帳本 封面 prompt

## 推薦風格

- 風格：editorial magazine cover photo portrait（premium business-magazine feel）
- 為什麼選它：這是系統題 / 治理題，不是球員動作題，按 CLAUDE.md 生圖鐵律情境 2 脫離 canonical。封面需要讓讀者一眼看到「一個人 + 兩邊帳本」的主結構，editorial portrait 最乾淨傳達這個判斷。
- 這張圖最該賣什麼：一個中年男人的職業重量（他做了一個決定） + 視覺化的「兩邊帳」（收入 vs 風險）。讀者一眼知道這篇在算帳。

## Person Recognition Gate

- Adam Silver 在中文圈的視覺辨識度：**MED**（常跟 NBA logo 一起出現，但沒有球員那種即時辨識度）
- 信心度約 55/100
- 必加外貌錨點：middle-aged bald man、thin rectangular/rimless glasses、narrow elongated face、dark well-tailored suit、calm measured expression
- 不跑 photo pipeline（MED tier 規則是加錨點即可，不必 photo）

## Final Prompt

```text
Editorial magazine cover photo portrait of Adam Silver, a middle-aged bald man with thin rectangular rimless glasses, narrow elongated face, clean-shaven, wearing a sharply tailored dark charcoal suit, composed and slightly burdened expression, direct measured gaze into camera. Medium close-up, three-quarter angle, shallow depth of field, dramatic single-source side lighting with soft rim light. Background is a single vertical composition split precisely down the middle: the LEFT half glows in warm gold and amber, suggesting a ledger column of crisp out-of-focus banknotes, gleaming trophy highlights, and abstract sportsbook-style signage reduced to colored bokeh shapes (no readable logos, no readable text); the RIGHT half is a cold cyan-blue atmosphere with faint silhouettes of a courtroom — a gavel resting on wood, shadowy handcuff outline, blurred newspaper fragments pinned to a dim wall. Centered between the two halves, floating softly behind the subject, a traditional brass balance scale, one pan visibly weighted and tilted toward the cold blue side. Subdued premium business-magazine palette, muted with two distinct accent temperatures (warm left, cold right). Film photography grain, solemn serious editorial mood, professional news-cover feeling, zero text overlay, no readable words anywhere in the frame. Realistic photojournalism rendering. --ar 3:4 --stylize 250
```

## 如果要繼續改

- 背景優先改什麼：
  - 如果金色那側看起來像賭場廣告，把 sportsbook-style signage 換成 `stacks of paper contracts and corporate sponsorship tags`
  - 如果藍色那側太像刑偵劇，把 handcuff outline 換成 `a lone subpoena envelope on a dim desk`，保留 gavel
- 不要動什麼：
  - Silver 的外貌錨點（bald / thin rectangular glasses / narrow elongated face / charcoal suit）
  - 構圖：vertical split + centered balance scale tilted to the risk side（這是整張圖的敘事骨架）
  - 3:4 --stylize 250（硬規則）
  - 無文字 overlay（標題另外用版式卡加，不在生圖裡）

## 備用版本 B（如果 A 太 busy）

改走 photojournalism 記者會場景：Silver 在發布台中段演講，背景是大 out-of-focus 贊助牆，贊助 logo 化作抽象色塊。更冷靜、更像新聞照片。

```text
Photojournalism scene: Adam Silver, middle-aged bald man with thin rectangular rimless glasses, narrow elongated face, in a dark charcoal suit, captured mid-speech at a stark press-conference podium. Sharp overhead light, face partly shadowed. Behind him, a large out-of-focus branding wall with layered sportsbook partnership logos reduced to soft abstract colored shapes (no readable text anywhere). 35mm film grain, muted blue-gray palette with a warm amber key light on the face, archival news-photo feeling, heavy editorial contrast. Expression composed and slightly burdened. Medium close-up, shallow depth of field, subtle motion blur on one raised hand. --ar 3:4 --stylize 250
```

A 是主打，B 作為備用。建議先跑 A，如果出圖太像賭場廣告再切 B。

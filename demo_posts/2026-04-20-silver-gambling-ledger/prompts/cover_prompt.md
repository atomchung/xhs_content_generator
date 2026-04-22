# Silver 賭博帳本 封面 prompt

## 鎖定版本：v2-B Scorsese Casino / Uncut Gems 海報風

最終風格：illustrated movie-poster，非 photoreal。
中央頂天立地 Silver 肖像 + 背後單道 Vegas 霓虹金光打剪影 + 前景散落撲克牌 / 籌碼 / 輪盤 + 上兩角懸浮 icon（獎盃$ vs 法槌 手銬）。
深紅 / 霓虹金 / 重黑 / 冷青點綴。

## Person Recognition Gate

- Adam Silver 中文圈視覺辨識度：**MED**，信心度約 55/100
- 必加錨點：middle-aged bald man、thin rectangular rimless glasses、narrow elongated angular face、dark well-tailored charcoal suit、composed but burdened expression
- 不跑 photo pipeline（MED tier，illustration 風格 + 錨點即可）

## Final Prompt

```text
Theatrical movie-poster illustration in the style of late-1990s Scorsese crime-cinema posters ("Casino", "Uncut Gems", "Rounders"), painted and posterized rather than photographed. Central subject: Adam Silver, middle-aged bald man with thin rectangular rimless glasses, narrow elongated angular face, wearing a sharply tailored dark charcoal suit, rendered with deliberate oil-painting brushwork and posterized flat color planes, never photorealistic. He stands dead-center filling the vertical composition, medium-long shot from slightly low angle, backlit by a single vertical shaft of deep amber-gold Vegas-neon light from behind that throws his silhouette sharp against the frame. Around him, a dynamic symmetric scatter: a wide fan of playing cards mid-fall across the lower foreground, a cascade of casino chips tumbling through the front plane, a half-visible roulette wheel glowing red in the lower-left corner, and the upper corners framed with ghostly translucent iconographic silhouettes — upper LEFT: a glowing trophy and a dollar sign; upper RIGHT: a judge's gavel above a handcuff outline. Palette: deep crimson red, heavy black, Vegas-neon amber gold, with a single cold cyan accent at the edges. Heavy painterly texture, grainy 1990s film-poster print quality, 3:4 vertical movie-poster composition, dramatic cinematic framing, high-stakes noir mood, no readable text anywhere in the frame. --ar 3:4 --stylize 250
```

## 如果要繼續改

- 背景優先改什麼：
  - 如果金色 Vegas 霓虹太像賭場廣告，把 `Vegas-neon amber-gold` 改為 `muted amber with crimson shadows`
  - 如果前景物件太擁擠，砍掉撲克牌扇，只留 chips + roulette
  - 如果電影感太誇張（過於 Scorsese），把 `late-1990s Scorsese crime-cinema` 改為 `early-2020s arthouse crime poster minimalism`
- 不要動：
  - Silver 外貌錨點（bald / thin rectangular glasses / narrow elongated angular face / charcoal suit）
  - 核心構圖（中央頂天立地 + 背後金光剪影 + 前景三件賭博物件 + 上兩角 icon 對比）
  - Palette（crimson + amber gold + heavy black + cold cyan accent）
  - 3:4 --stylize 250
  - 零可讀文字

## 版本歷史

- v1（commit `b8ba377`）：editorial photo portrait + 天平。真人感太強、天平無聊，已退役
- v2（commit `3e4c8ae`）：Kaiji manga + Scorsese poster 雙版。**B 版（Scorsese）被採用 = 當前鎖定版本**
- v3（commit `b4346a0`）：四構圖變體嘗試（God of Gamblers / poker showdown / card fan / chip avalanche），全部被否決，不用

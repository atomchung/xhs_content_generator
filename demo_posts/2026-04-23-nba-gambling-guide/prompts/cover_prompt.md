# 封面 prompt — 正式锁定版（v5 canonical）

## 锁定方向：手机 app + 虚焦球场（v4 第 ③ 案）

经 v3_A / v3_B / v4 六向比价，最终选 v4 第 ③ 案 — 手机 app 前景 + 球场虚焦背景。

理由：
- **直接命中题眼**：屏幕上的 `UNDER 2.5 REBOUNDS · -250` 就是「单人数据市场」这件事的字面证据；不需要任何隐喻
- **CTR 钩子是数字本身**：`-250` 在小红书首图能撑住停手的那一秒
- **AI 稳定度最高**：单一焦点、浅景深、文字锚字短且少
- **和前篇形成视觉互补**：前篇是大人物正面海报感，这篇是小道具特写新闻感 — 系列内有节奏变化，不是同一个壳套两次

## 风格家族（承前篇 + 本篇 v3 锁定）

- Cinematic film-still illustration（不是电影海报，是电影剧照）
- Painted + posterized oil-brushwork, never photoreal
- Palette: deep crimson red + Vegas amber-gold + heavy black + cold cyan accent
- 3:4 vertical, --stylize 250
- AI 只渲染指定短英文锚字，中文标题后期叠加

## Person Recognition Gate

- 前景手 + 背景球员都是 generic anonymous fictional figures
- 球员 jersey number intentionally blurred / unreadable, no real team logo, no real-world team colors
- 不需要跑 photo pipeline（无真实人物）

## Final Prompt

```text
Cinematic film-still illustration in the style of a Scorsese crime-drama close-up, painted and posterized oil-brushwork, never photorealistic.

Primary subject: an extreme close-up of a man's hand holding a smartphone in the lower-right foreground, thumb hovering over the screen. The phone screen is perfectly sharp and tilted toward the viewer. On the screen: a fictional sportsbook app interface with a minimalist dark UI — the readable bold white text reads "UNDER 2.5 REBOUNDS" on one line and "-250" on the line below, with a small crimson-red line chart fragment next to it showing a sharp downward spike. This is the only readable text in the image.

Background, deeply blurred (shallow depth of field, cinematic f/1.4 feel): a professional basketball arena during live play, amber-gold court lights, one generic anonymous fictional basketball player mid-motion running across the court — his figure is a painterly impression, jersey number unreadable due to blur, no real team identifiable. Faint courtside LED glow, blurred crowd silhouettes in the deep background.

The hand in the foreground is generic, middle-aged, unremarkable — belonging to an anonymous viewer, not a recognizable person.

Lighting: the phone screen glow is the sharp primary light, casting cold cyan and crimson reflections onto the holding fingers. The arena background glows amber-gold in the distance. Deep black occupies the middle depth between foreground hand and background court.

Palette: cold cyan (phone glow + screen UI), deep crimson red (screen chart + the "-250" text), Vegas amber-gold (background court), heavy black (middle depth). Heavy painterly oil-brush texture, grainy film-still quality. 3:4 vertical composition — upper half is deep-blur arena negative space reserved for headline overlay, lower half is sharp phone + hand. --ar 3:4 --stylize 250
```

## 标题叠加指引（后期 overlay）

- 标题：`三道防线`（第一行）/ `堵不住的那块市场`（第二行）
- 字体：阿里巴巴普惠体 Heavy
- 颜色：白字 + 细 crimson 描边（呼应屏幕里的 `-250` 红色折线）
- 位置：上半部 deep-blur arena 区域，左对齐

## 如果要继续改

- 如果屏幕 UI 文字（`UNDER 2.5 REBOUNDS` / `-250`）渲染崩：把 prompt 末尾加 `the on-screen text MUST be sharp, legible, and rendered in clean sans-serif typography`，仍然不行就保留干净屏幕 + 后期 Figma 叠 UI
- 如果背景球员被画太清抢主：把 `shallow depth of field` 改为 `extremely shallow depth of field, background near-bokeh blur`
- 如果手指被画成女性 / 偏年轻：把 `middle-aged, unremarkable` 改为 `weathered male hand, late 30s, slight 5 o'clock shadow on knuckles`
- 如果整张图缺戏剧感：把 `dim arena background` 改为 `dimly lit arena with one rim of harsh courtside spotlight`
- **不要动的**：
  - 屏幕只显示 `UNDER 2.5 REBOUNDS` + `-250` + 一段 crimson 折线 — 不增加任何其他可读文字
  - background player 是 anonymous fictional + jersey number unreadable
  - illustrated painted posterized, not photoreal
  - palette 四色（cyan + crimson + amber + black）
  - 3:4 --stylize 250

## 版本历史

- v1（cover_prompt.md 初版）：editorial collage + 赔率曲线 + 匿名背影 — 用户反馈 editorial 太理性、和前篇调性断
- v2（cover_prompt.md 同名 v2）：曲线 + collage 改良；用户反馈「避开这种封面」
- v3_A（`cover_prompt_v3_A_player.md`）：球员 + 三道裂开的防线 / Scorsese poster — 用户反馈「死板」
- v3_B（`cover_prompt_v3_B_monitor.md`）：诚信监控员 + 监控墙 / Scorsese poster — 用户反馈「死板」
- v4（`cover_prompt_v4_compare.md`）：6 个直给方向比价 — 板凳假伤 / LED 广告墙 / 手机 app / 记者会 / 通道错身 / FBI 记者会
- **v5（本文件）**：从 v4 选定 ③ 手机 app 案，锁为 canonical

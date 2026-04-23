# 封面 prompt v4 — 6 个方向比较版（直接、直给、高 CTR）

## 文件用途

把 6 个构图方向都写成可直接贴 ChatGPT / Gemini / Midjourney 的 final prompt，放在一个文件里比价。用户挑完再把赢家升级成正式 `cover_prompt.md`。

## 共享规则（每条 prompt 都内嵌这些锚点）

- **风格家族**：承袭前篇的 Scorsese-adjacent painterly noir，但这一轮从「电影海报」改成「电影剧照 / 新闻现场感」—— painted + posterized oil-brush quality, never photoreal
- **色板**：crimson red + Vegas amber-gold + heavy black + cold cyan accent —— 和前篇同一系列
- **真人规避**：所有人物 generic anonymous fictional figures, do not resemble any specific real NBA player / real NBA coach / real league official. Jersey numbers are intentionally blurred / unreadable. No real team logos. Not based on any real person.
- **文字**：AI 只渲染指定的短英文锚字，其他文字一律留给后期叠加中文标题
- **比例**：3:4 vertical, --stylize 250
- **标题预留**：每张图都留一块负空间给后期叠加 `三道防线 / 堵不住的那块市场`（阿里巴巴普惠体 Heavy, 白字 + crimson 细描边）

---

## ① 板凳「假伤」特写

**一句话**：事件本身的字面场景——板凳上抱着脚踝的匿名球员 + 跪下检查的队医 + 背景比分板 `MIN 3:42`。

```text
Cinematic film-still illustration in the style of a Scorsese crime-drama key frame, painted and posterized oil-brushwork, never photorealistic.

Primary scene: courtside bench of a professional basketball arena, mid-game. A generic anonymous fictional basketball player seated on the bench in the center-left of the frame, body hunched forward, both hands gripping his right ankle, face twisted in muted pain but eyes drifting off-camera as if distracted. He wears an unbranded dark basketball jersey with an intentionally blurred, unreadable jersey number; no real team colors or logos.

A team trainer kneels in front of him on one knee, a medical bag beside him, fingers pressing the player's ankle, head tilted in concern — trainer is a generic middle-aged man, face partially in shadow. Two teammates stand behind the bench in the mid-ground, hands on hips, watching silently, their faces softened and out of focus.

In the upper-right third of the frame: an overhead scoreboard, hanging slightly blurred but with one data field sharp and readable — the white block labeled "MIN" showing the numbers "3:42" in bold sans-serif, glowing amber-gold. This is the only readable text in the image.

Lighting: harsh overhead arena lights casting deep crimson-red shadows on the bench, with a single cold cyan rim light from the side catching the player's shoulder. The background court is deeply blurred, suggesting motion of distant players, with faint amber-gold bokeh from scoreboards and courtside LED panels.

Palette: deep crimson red, heavy black, Vegas amber-gold (scoreboard + bokeh only), single cold cyan accent. Heavy painterly oil-brush texture, grainy film-still quality, 3:4 vertical composition with the upper-left third reserved as negative space for a headline overlay, cinematic asymmetric framing, no other readable text anywhere. --ar 3:4 --stylize 250
```

---

## ② 场边 LED 广告墙 + 小球员

**一句话**：当下 NBA 球场的字面真实——courtside LED 整面都是博彩平台品牌，球员在广告墙前走过。

```text
Cinematic film-still illustration in the style of a Scorsese crime-drama courtside key frame, painted and posterized oil-brushwork, never photorealistic.

Scene: a wide courtside view from the lower seating level, looking toward the hardwood court during a live NBA-style game. Dominating the lower third of the frame: a long horizontal LED advertising board running along the sideline, saturated with fictional sportsbook branding — bold amber-gold and crimson-red logos and text fragments like "KINGSBOOK", "DUELPLAY", "MGM-STYLE" (fictional names evoking but not copying real sportsbook brands), blinking live odds ticker fragments. The LED board is painted with high-contrast glow, lit-up and dominant.

In the middle of the frame, a generic anonymous fictional basketball player in mid-stride, seen three-quarter from behind, dribbling a basketball. He is intentionally small in scale — maybe one-third the height of the frame — dwarfed by the overwhelming sportsbook LED panel behind and beside him. His jersey is plain dark fabric with an intentionally blurred, unreadable number; no real team logo.

Background: out-of-focus opposing bench, faint silhouettes of teammates, the arena rafters fading into deep black.

Lighting: the LED board glow is the primary light source, casting crimson and amber rim light onto the player's shoulder and the hardwood floor. A single cold cyan overhead spotlight catches the top of his head. Deep noir contrast elsewhere.

Palette: deep crimson red (LED accents), Vegas amber-gold (LED accents + floor reflection), heavy black, cold cyan rim. Heavy painterly oil-brush texture, grainy film-still quality. 3:4 vertical composition — upper half is dark arena negative space reserved for headline overlay, lower half is the LED board + small player. Cinematic documentary feel. The only readable text in the image is the short fictional sportsbook brand fragments on the LED board. --ar 3:4 --stylize 250
```

---

## ③ 手机 app + 虚焦球场

**一句话**：直给的双层现实——前景手机屏幕可读，背景球场模糊，同一个人出现在两层。

```text
Cinematic film-still illustration in the style of a Scorsese crime-drama close-up, painted and posterized oil-brushwork, never photorealistic.

Primary subject: an extreme close-up of a man's hand holding a smartphone in the lower-right foreground, thumb hovering over the screen. The phone screen is perfectly sharp and tilted toward the viewer. On the screen: a fictional sportsbook app interface with a minimalist dark UI — the readable bold white text reads "UNDER 2.5 REBOUNDS" on one line and "-250" on the line below, with a small crimson-red line chart fragment next to it showing a sharp downward spike. This is the only readable text in the image.

Background, deeply blurred (shallow depth of field, cinematic f/1.4 feel): a professional basketball arena during live play, amber-gold court lights, one generic anonymous fictional basketball player mid-motion running across the court — his figure is a painterly impression, jersey number unreadable due to blur, no real team identifiable. Faint courtside LED glow, blurred crowd silhouettes in the deep background.

The hand in the foreground is generic, middle-aged, unremarkable — belonging to an anonymous viewer, not a recognizable person.

Lighting: the phone screen glow is the sharp primary light, casting cold cyan and crimson reflections onto the holding fingers. The arena background glows amber-gold in the distance. Deep black occupies the middle depth between foreground hand and background court.

Palette: cold cyan (phone glow + screen UI), deep crimson red (screen chart + the "-250" text), Vegas amber-gold (background court), heavy black (middle depth). Heavy painterly oil-brush texture, grainy film-still quality. 3:4 vertical composition — upper half is deep-blur arena negative space reserved for headline overlay, lower half is sharp phone + hand. --ar 3:4 --stylize 250
```

---

## ④ 记者会麦克风阵列

**一句话**：出事之后被围堵的那一刻——多支采访麦从画面边沿伸进来，匿名球员半脸在阴影里。

```text
Cinematic film-still illustration in the style of a Scorsese crime-drama press-conference key frame, painted and posterized oil-brushwork, never photorealistic.

Primary scene: a post-game press scrum in a dim hallway just outside a basketball locker room. In the center-right of the frame: a generic anonymous fictional basketball player, chest-up view, wearing a plain dark team warm-up jacket with an intentionally blurred, unreadable number. His upper face is submerged in deep noir shadow cast from above — his eyes are invisible, only his lower jaw, clenched mouth, and a shadowed cheekbone catch the light. Not resembling any specific real NBA player.

From the lower edge and left edge of the frame: a dense cluster of press microphones thrust toward him — at least 8 mics visible, each capped with a small rectangular mic flag bearing short fictional network call-letters ("KBSN", "TSPT", "NSPN" — fictional and unreadable-at-first-glance, brand-evoking but not copying real networks). The mics create a diagonal forest of silver-black shapes crowding the player.

Background: out-of-focus press corridor, a few blurred reporter silhouettes with cameras raised, scattered white camera-flash pops creating bright hot spots. Walls are dark.

Lighting: multiple hard-key flash blowouts from camera strobes create harsh crimson-tinged rim light and deep cold cyan shadows on the player's face and jaw. The overall mood is overwhelming and intrusive.

Palette: deep crimson red (flash hot spots + mic-flag tips), heavy black (background + upper face shadow), Vegas amber-gold (faint hallway practicals), cold cyan (flash rim light on jaw). Heavy painterly oil-brush texture, grainy press-photo-still quality. 3:4 vertical composition — upper-left third reserved as black negative space for headline overlay. Cinematic claustrophobic framing, shallow depth of field on the mics. The only short readable text is the fictional mic-flag call-letters. --ar 3:4 --stylize 250
```

---

## ⑤ 球员通道错身（球员 vs 诚信官员）

**一句话**：球员从赛场走进调查的那一步——通道里两个身影对向错身，左球衣、右西装。

```text
Cinematic film-still illustration in the style of a Scorsese crime-drama corridor key frame, painted and posterized oil-brushwork, never photorealistic.

Scene: a dim concrete arena back-of-house corridor connecting the court to the league-office wing. The corridor stretches into perspective toward a distant warm amber-gold doorway.

Two figures, mid-stride, passing each other at the midpoint of the corridor in a diagonal cross-composition:

FIGURE LEFT: a generic anonymous fictional basketball player, seen three-quarter from behind as he walks away from the viewer toward the amber doorway. He wears a plain dark team warm-up jacket with an intentionally blurred, unreadable jersey number, a towel draped over his shoulder. Do not draw him in a shooting or dunking pose.

FIGURE RIGHT: a generic anonymous fictional sports-league integrity officer, seen three-quarter from the front, walking toward the viewer. He wears a sharply tailored dark navy suit and a white shirt without tie. A credential lanyard with a blurred unreadable badge hangs around his neck. He carries a closed manila case-folder under his left arm. He has full dark hair combed back, broader jawline, no glasses — explicitly not bald, not wearing thin rectangular rimless glasses — he does not resemble Adam Silver or any specific real NBA official. His eyes cast downward toward the player as they pass. Do not draw him in any conversational pose.

The two figures do not speak or touch — they are simply crossing paths, captured mid-step. Their shoulders are staggered in depth to emphasize the asymmetric diagonal composition.

Lighting: cold cyan overhead practicals down the corridor ceiling, warm amber-gold wash from the distant doorway casting long silhouettes back toward the viewer, single crimson-red accent bulb on one wall junction casting a faint red mark on the concrete.

Palette: cold cyan (corridor overhead), Vegas amber-gold (distant doorway + floor reflection), deep crimson red (single accent wall light), heavy black (ceiling + shadow pools). Heavy painterly oil-brush texture, grainy film-still quality. 3:4 vertical composition — upper quarter is dark ceiling negative space reserved for headline overlay. Cinematic asymmetric diagonal framing. No readable text anywhere. --ar 3:4 --stylize 250
```

---

## ⑥ FBI 联邦调查记者会

**一句话**：新闻感最强——两名 FBI 探员侧身背对镜头，台上展板写 `NBA Illegal Gambling · 2025`。

```text
Cinematic film-still illustration in the style of a Scorsese crime-drama federal-press-conference key frame, painted and posterized oil-brushwork, never photorealistic.

Primary scene: a federal press conference podium inside a dark government briefing room. Viewer perspective is from the lower-left third, looking up and forward toward the podium.

FOREGROUND LEFT: two generic anonymous fictional male federal agents in dark navy-blue suits, seen from behind three-quarter, shoulders squared. Their faces are not visible — only the backs of their heads, ears, and collared suits. One wears a small earpiece coil visible against the back of his neck. Do not base them on any specific real persons.

MID-GROUND CENTER: a blue podium with the fictional federal seal (abstract eagle silhouette, not any real seal) on its front panel. Behind the podium rises a large freestanding presentation board, painted in matte black, bearing the only readable text in the image — in bold white sans-serif: top line "NBA ILLEGAL GAMBLING CASE", lower line "2025". Below the text, a grid of four rectangular blacked-out silhouette portraits (heavily pixel-masked like evidence photos whose subjects are redacted), arranged in a 2×2 grid — faces unidentifiable, deliberate visual redaction.

BACKGROUND: deep navy blue drape with vertical folds, faint scattered white flash pops from off-camera press photographers creating bright rim highlights on the agents' shoulders.

Lighting: a single hard key light from upper-right casts long crimson-tinged shadows from the agents toward the podium. Amber-gold spot on the podium seal. Cold cyan edge light catching the presentation board. Deep black everywhere else.

Palette: deep crimson red (flash rims + agent collar shadows), Vegas amber-gold (podium seal light), cold cyan (presentation board edge), heavy black (drape + negative space). Heavy painterly oil-brush texture, grainy news-photo-still quality. 3:4 vertical composition — upper third is deep-black drape negative space reserved for headline overlay. Cinematic official-investigation mood. --ar 3:4 --stylize 250
```

---

## 生成后怎么挑

跑完看成图时，按这四条过：

1. **主题直达度**：不看文字的小红书用户，能不能 3 秒内 get「这事儿和 NBA 球员 + 博彩监管有关」
2. **非匿名风险**：AI 有没有把人物画成任何真实现役球员 / 官员的脸。**有就丢**
3. **文字稳定度**：指定的短英文锚字（`MIN 3:42` / `-250` / `UNDER 2.5 REBOUNDS` / `NBA ILLEGAL GAMBLING CASE · 2025` / 虚构 mic-flag）有没有被 AI 渲染成乱码
4. **系列辨识**：和前篇 Silver 封面放在一起，是不是能看出「同一个账号 + 同一个系列」（色板、painterly 质感、noir 光）

合格了的那一两个，告诉我选哪个，我升级成正式 `cover_prompt.md`。

## 各版预期风险速查

| 方向 | 最可能 fail 的点 | Fallback |
|---|---|---|
| ① 板凳假伤 | 场景太像普通比赛照，缺少 scandal 信号；`MIN 3:42` 渲染歪 | 加大比分板、加强 crimson |
| ② LED 广告墙 | 虚构 sportsbook logo 被渲染成字母汤 | 简化 logo 为抽象色块 + 单字母 |
| ③ 手机 app | 屏幕 UI 字串渲染崩、虚焦球员被画得过清 | 用 Figma 后期把屏幕 UI 手叠 |
| ④ 记者会麦克风 | 麦克风数量太多导致 AI 画叠麦 / 缺麦；mic-flag 渲染崩 | 砍到 5 支麦、mic-flag 不渲染文字 |
| ⑤ 通道错身 | AI 把两人画成同姿势同角度（踩过的坑）| 动作已在 prompt 写死，生 4-8 张挑 |
| ⑥ FBI 记者会 | 展板文字渲染崩；FBI 探员面部被补出来 | 展板 only 短英文 / 文字后期叠 |

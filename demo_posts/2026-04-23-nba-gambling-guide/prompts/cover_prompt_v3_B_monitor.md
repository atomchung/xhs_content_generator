# 封面 prompt v3_B — 坐在监控墙前的诚信监控员（Scorsese poster, 延续前篇视觉家族）

## 位置与承前篇

- 前篇封面：`demo_posts/2026-04-20-silver-gambling-ledger/prompts/cover_prompt.md`（v2-B Scorsese Casino / Uncut Gems 海报风 — Silver 主角）
- 本篇延续同一风格家族：illustrated movie-poster、painted + posterized、非 photoreal、crimson / amber-gold / black / cold cyan palette、3:4 --stylize 250、no readable text
- 叙事层级推进：前篇画「签下这笔生意的决策者」→ 本篇画「正在盯这个生态的执行者」——系列形成自然续集
- 同 A/B 双版比较：v3_A 球员版在 `cover_prompt_v3_A_player.md`

## 推荐风格
- 风格：Scorsese crime-cinema movie-poster illustration（和前篇同一风格包）
- 为什么选它：同家族视觉 + 叙事角色推进——「决策者 → 守护者」是系列逻辑最顺的下一步
- 这张图最该卖什么：**那双盯着单人市场的眼睛**——把「三道防线」具象成一个人在看整面监控墙

## Person Recognition Gate

- 主体是 **generic anonymous fictional integrity operator**，不是任何真实人物
- 为避免读成前篇主角 Silver，必须在 prompt 里写死差异锚点：
  - NOT bald（full head of dark hair combed back）
  - NOT wearing thin rectangular rimless glasses（no glasses at all）
  - NOT narrow elongated angular face（broader jawline）
  - 姿势：从背后 3/4 侧拍，脸基本不可见，只有下颌线和耳朵轮廓
- 风格是 illustrated / painted / posterized，不是 photoreal
- **不需要跑 photo pipeline**（无真实人物）

## Final Prompt

```text
Theatrical movie-poster illustration in the style of late-1990s Scorsese crime-cinema posters ("Casino", "Uncut Gems", "Rounders"), painted and posterized rather than photographed. Central subject: a generic anonymous fictional male sports-league integrity operator, seen from behind in a three-quarter back view, seated in a worn leather executive chair at a dark wood desk, shoulders squared, head slightly tilted upward toward a wall of monitors. He has a full head of dark hair combed back, no glasses, broader jawline; he wears a well-tailored dark navy suit. He does not resemble Adam Silver — explicitly NOT bald, NOT wearing thin rectangular rimless glasses, NOT a narrow elongated angular face. Only the back of his head, the side of his jaw, and his suited shoulders are visible; face is not rendered. Rendered with deliberate oil-painting brushwork and posterized flat color planes, never photorealistic.

Filling the upper two-thirds of the frame in front of him: a towering wall of surveillance monitors arranged in a grid, each screen glowing faintly. Most monitors show abstract painted basketball broadcast feeds and small line-chart overlays in muted amber. Three monitors in the wall pulse with a deep crimson red glow — on those three screens, a sharp downward-crashing line-chart spike is the dominant graphic, with small blinking red dots at the corners suggesting alerts. No readable text on the screens — graphics and colored indicators only.

Foreground: a dynamic scatter of Scorsese-poster objects echoing the previous cover — a wide fan of playing cards spread across the desk, a small cluster of casino chips stacked beside a closed manila folder, and a ceramic coffee cup casting a long shadow. Upper corners framed with ghostly translucent iconographic silhouettes — upper LEFT: a glowing magnifying glass over a dollar sign; upper RIGHT: a judge's gavel above a handcuff outline.

A single vertical shaft of deep amber-gold Vegas-neon light streams from behind the monitor wall, throwing the operator's silhouette dark against the glowing grid of screens. Palette: deep crimson red (only on the three alerting screens and their red dots), heavy black, Vegas-neon amber gold (backlight and dominant monitors), with a single cold cyan accent at the desk edge. Heavy painterly texture, grainy 1990s film-poster print quality, 3:4 vertical movie-poster composition, dramatic cinematic framing, high-stakes noir mood, no readable text anywhere in the frame. --ar 3:4 --stylize 250
```

## 标题叠加指引（后期 overlay）

- 标题：`三道防线`（第一行）/ `堵不住的那块市场`（第二行）
- 字体：阿里巴巴普惠体 Heavy
- 颜色：白字 + 细 crimson 描边（呼应三块红色警报屏）
- 位置：下 1/3 或叠在操作员肩膀上方暗色区——监控墙本身已经充满中上 2/3，标题往下压

## 如果要继续改

- 如果监控墙画得太像普通办公室：把 `wall of surveillance monitors arranged in a grid` 改为 `towering cinematic wall of CRT and modern flat-panel monitors in mixed sizes, mounted on dark wood panels`——加入老式 CRT 会增加电影感
- 如果操作员容易被读成 Silver：在 prompt 末尾再加一条 `operator is explicitly not Adam Silver; a different fictional person`
- 如果三块红屏不够显眼：把 `three monitors` 改为 `three larger central monitors occupying the visual focal point`
- **不要动的**：
  - 从背后 3/4 拍 + 脸不渲染 —— Person Recognition Gate 核心锚点
  - NOT bald / NOT thin rectangular rimless glasses / NOT narrow elongated angular face —— 避免读成前篇 Silver
  - illustrated painted posterized, not photoreal
  - palette（crimson + amber gold + black + cold cyan）
  - 3:4 --stylize 250
  - 屏幕上零可读文字，用图形 + 颜色示意 alert

## 版本历史

- v1：editorial collage + 赔率曲线 + 匿名背影（存档为 cover_prompt.md 初版）
- v2：同 v1，micro-adjustments；用户反馈「避开这种封面」
- v3_A（姐妹文件 `cover_prompt_v3_A_player.md`）：球员主视觉 + 三道裂开的防线
- **v3_B（本文件）**：监控员视角 + 监控墙，与前篇形成「决策者 → 执行者」的系列叙事

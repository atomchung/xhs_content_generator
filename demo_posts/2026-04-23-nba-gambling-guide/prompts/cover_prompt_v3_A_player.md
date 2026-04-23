# 封面 prompt v3_A — 被盯上的球员（Scorsese poster, 延续前篇视觉家族）

## 位置与承前篇

- 前篇封面：`demo_posts/2026-04-20-silver-gambling-ledger/prompts/cover_prompt.md`（v2-B Scorsese Casino / Uncut Gems 海报风）
- 本篇延续同一风格家族：illustrated movie-poster、painted + posterized、非 photoreal、crimson / amber-gold / black / cold cyan palette、3:4 --stylize 250、no readable text
- 主视觉从「Silver 肖像」换成「被盯上的匿名球员 + 三道裂开的防线」
- 同 A/B 双版比较：v3_B 监控员版在 `cover_prompt_v3_B_monitor.md`

## 推荐风格
- 风格：Scorsese crime-cinema movie-poster illustration（和前篇同一风格包）
- 为什么选它：系列一致性——读者一眼能认出这是同系列 vol.2；戏剧张力延续前篇的 high-stakes noir 情绪
- 这张图最该卖什么：**一个人站在一道裂开的防线前**——把「单人就能动」这件事直接画进画面

## Person Recognition Gate

- 主体是 **generic anonymous fictional NBA player**，不是任何真实球员
- 面部处理：noir shadow 遮住眼睛（upper half of face in deep shadow），下颌与嘴唇可见但无特征化
- 球衣号码故意模糊 / unreadable，不出现任何真实球队 logo，不出现任何真实球队配色
- 风格是 illustrated / painted / posterized，不是 photoreal
- **不需要跑 photo pipeline**（无真实人物）

## Final Prompt

```text
Theatrical movie-poster illustration in the style of late-1990s Scorsese crime-cinema posters ("Casino", "Uncut Gems", "Rounders"), painted and posterized rather than photographed. Central subject: a generic anonymous fictional NBA basketball player, front-facing medium shot from slightly low angle, standing dead-center filling the vertical composition, broad-shouldered but weighed down, rendered with deliberate oil-painting brushwork and posterized flat color planes, never photorealistic. The upper half of his face is submerged in deep noir shadow cast from above — his eyes are invisible, only the lower jaw, lips and a shadowed cheekbone catch the light. He wears a plain unbranded dark basketball jersey with an intentionally blurred, unreadable jersey number; no team logo anywhere; no real-world team colors.

Behind him, rising vertically into the frame, are three heavy metal barrier lines — thick rivet-studded steel defense rails stacked at different depths, each suggesting a "line of defense". The rail closest to him has a clear visible crack splitting down its center, faintly glowing with amber light from behind. A single shaft of deep amber-gold Vegas-neon light streams through that crack from behind him, throwing his silhouette sharp against the frame.

Foreground: a dynamic scatter of Scorsese-poster objects echoing the previous cover — a wide fan of playing cards mid-fall across the lower plane, a cascade of casino chips tumbling through the front plane, and a single basketball resting in the lower-right corner casting a long shadow. Upper corners framed with ghostly translucent iconographic silhouettes — upper LEFT: a glowing stopwatch and a dollar sign; upper RIGHT: a judge's gavel above a handcuff outline.

Palette: deep crimson red, heavy black, Vegas-neon amber gold (only in the crack and backlight), with a single cold cyan accent at the frame edges. Heavy painterly texture, grainy 1990s film-poster print quality, 3:4 vertical movie-poster composition, dramatic cinematic framing, high-stakes noir mood, no readable text anywhere in the frame. --ar 3:4 --stylize 250
```

## 标题叠加指引（后期 overlay）

- 标题：`三道防线`（第一行）/ `堵不住的那块市场`（第二行）
- 字体：阿里巴巴普惠体 Heavy
- 颜色：白字 + 细 crimson 描边
- 位置：可放在下 1/3 或侧栏——主视觉中上部已经满载（人物 + 三道防线），标题往下压更稳

## 如果要继续改

- 如果三道防线被画得太像监狱铁栅栏：改 `thick rivet-studded steel defense rails` 为 `three parallel luminous translucent barriers with thin golden frames`
- 如果球员被画得像真实球星：加 `do not resemble any specific real NBA player; generic fictional figure only`
- 如果前景太乱抢人物：砍掉扑克扇，只留 chips + basketball
- **不要动的**：
  - 脸部 upper-half in deep shadow（eyes invisible）—— Person Recognition Gate 核心锚点
  - blurred unreadable jersey number / no team logo / no real-world colors
  - illustrated painted posterized, not photoreal
  - palette（crimson + amber gold + black + cold cyan）
  - 3:4 --stylize 250
  - 零可读文字（除了后期叠加的中文标题）

## 版本历史

- v1：editorial collage + 赔率曲线 + 匿名背影（存档为 cover_prompt.md 初版）
- v2：同 v1，micro-adjustments；用户反馈「避开这种封面」
- **v3_A（本文件）**：球员主视觉 + 三道裂开的防线，Scorsese poster 家族
- v3_B（姐妹文件 `cover_prompt_v3_B_monitor.md`）：监控员视角，和前篇形成系列叙事层级

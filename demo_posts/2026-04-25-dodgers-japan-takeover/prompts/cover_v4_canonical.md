# 道奇 = 日本队 封面 v4 — Canonical NBA Break-out 移植到 MLB

## Person Recognition Gate
```json
[{"person": "Shohei Ohtani", "confidence": 92, "tier": "HIGH", "reason": "全球级超巨", "anchors_suggestion": "直接用名字"}]
```

## 推荐风格
- 风格：**Canonical 3D comic panel break-out**（账号 NBA 系金本，44 mutation 全败实测过）
- 为什么选它：账号视觉品牌已经被这个风格绑定，MLB 题保持同一品牌延续性最强；漫画跳出框 + photoreal 主体 + Pop Art 背景 = 账号读者一秒钟认得「这是我们家的封面」
- 这张图最该卖什么：大谷投球姿势从漫画格子里炸出来 + 胸口 UNIQLO 红字 = 同一品牌语言讲新故事

## ⚠️ 偏离 canonical 的实验项
canonical research 锁死规则：**只能换 `{PLAYER_NAME}` 和 `{ACTION_PHRASE}`**。本 prompt 多加了一条 `Dodgers home cream pinstripe jersey with bold red UNIQLO chest patch`，因为 Uniqlo 是本篇故事核心。这是**实验性偏离**，可能拖低品质，需要生成后人工对比确认是否值得。

如果想严格 canonical，删掉那一行，但 Uniqlo 故事就被画面丢了。

## Final Prompt

```text
3D comic panel break-out illustration, Shohei Ohtani breaking through the comic panel frame, mid-pitch fastball release in foreground bursting toward viewer, torn comic panel edges as frame, Ben-day dots visible on receding background panels, Arturo Torres bold black outlines, the baseball casting shadow onto the panel surface, dramatic foreshortening with exaggerated forearm and hand, pop-art colored background (crimson + cobalt + goldenrod), photorealistic foreground transition on the player, Jack Kirby superhero energy, cinematic composition, Dodgers home cream pinstripe jersey with bold red UNIQLO wordmark chest patch where the Dodgers script would normally sit, vertical 3:4 aspect --ar 3:4 --stylize 250
```

## 如果要继续改
- 严格 canonical 版（删 Uniqlo 行）：只换 `Shohei Ohtani` + `mid-pitch fastball release`，其余一字不动 — 出图最稳
- 想强化 MLB 不是 NBA 感：把 `basketball casting shadow` 换成 `baseball casting shadow`（已在本版替换）
- 不要加：watercolor / aura / speed lines / beams / gold leaf / ink / minimal — 这些 44 mutation 全败的禁词
- 不要动：`photorealistic foreground transition on the player` / `--ar 3:4 --stylize 250`

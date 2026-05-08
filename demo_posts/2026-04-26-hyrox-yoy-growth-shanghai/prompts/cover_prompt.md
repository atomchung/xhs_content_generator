# Hyrox 续集封面 prompt — 苦瓜女士 + 表情包众生相

## 推荐风格
- 风格：知名表情包人物群像（苦瓜女士 + 流泪猫猫头 + 痛苦面具小狗 + 黄豆人），统一 sticker 插画化处理
- 为什么选它：
  - Hyrox 的真实情绪是「100 万人在自愿受苦」，用「众生皆苦」类表情包做主角，比 Q 版健身吉祥物更贴情绪真相
  - 表情包人物自带辨识度，在 XHS 信息流刷到时 0.3 秒被认出
  - 自嘲式幽默正中评论区文化，比单纯热血更容易引发分享
  - 与上一篇 Q 版 Hyrox 帖形成「续集变奏」，老粉感知到风格升级而不是重复
- ⚠️ 视觉宪法说明：此版偏离账号视觉宪法第 1 条（默认漫画卷封风格），是基于「情绪真相」的有意识破例。如反响一般，下篇回退默认风格。
- 这张图最该卖什么：**「众生皆苦地在跑」的喜剧反差 + 「营收一年涨 50%」的商业论点**

## Story Atoms
- 主角：4 个知名表情包人物，统一插画 sticker 风格 + 黑底霓虹黄配色
  - **苦瓜女士**（中央 C 位）— 推黑色铁橇，bitter melon 表情皱成一团
  - **流泪猫猫头**（左侧）— 跑步腾空一脚，巨大泪眼一边跑一边流泪
  - **痛苦面具小狗**（右侧）— 壶铃高举过头，五官夸张痛苦扭曲
  - **黄豆人**（右下角，小尺寸）— 抱着完赛奖牌瘫坐，post-race 释然
- 动作瞬间：4 种 Hyrox 标志动作（推橇 / 跑步 / 壶铃 / 完赛瘫）= 比赛全流程缩影
- 情绪冲突：「众生皆苦」的自嘲表情 vs 「营收涨 50%」的商业数据 → 喜剧反差
- 背景符号：上海外滩剪影（保持原版）+ Hyrox 黑底霓虹黄

## Generation Order
1. Subject anchor（先锁 4 个 meme 角色 + 动作）
2. Background layer（外滩剪影，保持原版）
3. Final cover（合成 + 加大字）

## Style 1 — Q 版健身吉祥物（上一版，已废弃）
- 跳过原因：用户决定改走表情包众生相，主因是「自愿受苦」这层情绪 Q 版盖不住

## Style 2 — Meme Character Mashup（当前推荐）
- 风格摘要：4 个中文互联网知名表情包人物，统一手绘插画 sticker 化处理（不照搬网图，重画一遍），保留各自标志辨识度，统一黑描边 + Hyrox 黑底霓虹黄配色
- 关键约束：人物表情都是「我在自愿受苦」基调，但姿态在认真完成比赛动作 — 反差就是这张图的笑点

### Subject Anchor Prompt（只画人物）
```text
4 iconic Chinese internet meme characters reimagined as Hyrox fitness race competitors, illustrated in unified sticker-style line art with thick black outlines.

Character 1 (CENTER, focal anchor): "Bitter Melon Lady" — anthropomorphic bitter melon character, body shaped like a bumpy green bitter melon (warty texture, jade-green skin), with a humanoid woman face, drooping sad eyebrows, glistening tearful eyes, downturned mouth, hair pulled back into a low bun. She is in a deep lunge pushing a heavy black sled forward with both hands, sweat droplets flying, expression of "this is killing me but I'm doing it anyway".

Character 2 (LEFT): "Crying Cat Head" — round cream-white cartoon cat character with massive comically teary eyes streaming dramatic tear droplets down both cheeks, simple line-art body with stubby limbs, mid-stride running pose with one leg lifted high, wearing a black athletic tank top with neon yellow Hyrox-style accent, still trying to smile through the tears.

Character 3 (RIGHT): "Pain Mask Dog" — small white cartoon beagle-like dog character with an exaggerated suffering expression, eyes squeezed tightly shut, eyebrows pulled together in dramatic agony, big sweat droplet on forehead, mouth open in silent scream, both arms raised high holding a black kettlebell above the head, in a determined squat stance, wearing a black tank top with neon yellow accent.

Character 4 (BOTTOM-RIGHT corner, smaller scale ~30% size of others): "Yellow Bean Person" — round egg-yolk-yellow bean-shaped character with simple dot eyes and tiny relieved smile, sitting collapsed cross-legged on the ground, hugging a red Hyrox finisher medal to chest, post-race exhausted but content vibe.

All 4 characters drawn in unified illustrated sticker-style with thick consistent black outlines, flat clean colors, edgy meme humor energy. Characters share black + neon yellow Hyrox apparel theme but each retains their own iconic meme identity. The shared emotional thread reads as: "I am suffering and I chose this".

Plain off-white background. Composition centered on Bitter Melon Lady, the other three orbit around her.

--ar 3:4 --stylize 250
```

### Background Prompt（背景层，保持原版）
```text
Stylized Shanghai Bund skyline silhouette in clean flat illustration style. Iconic landmarks: Oriental Pearl TV Tower (left), Lujiazui supertall trio — Shanghai Tower, Shanghai World Financial Center (the bottle opener), Jin Mao Tower (right side). Soft sunset gradient sky from warm orange at horizon to deep navy at top. Empty middle ground for subject placement. Minimal, no people, no boats, no clutter.

--ar 3:4
```

### Final Cover Prompt（最终封面，给生图工具用）
```text
Magazine-style fitness race poster cover, 3:4 vertical layout, Chinese internet meme character mashup theme, self-aware comedic tone.

FOREGROUND (lower 60%): 4 iconic Chinese internet meme characters as Hyrox competitors, illustrated in unified sticker-style with thick black outlines and flat clean colors:

- CENTER (focal anchor): "Bitter Melon Lady" — anthropomorphic bitter melon character, body shaped like a bumpy green bitter melon with warty jade-green texture, with a humanoid woman face, drooping sad eyebrows, tearful eyes, downturned mouth, hair in a low bun. In a deep lunge pushing a heavy black sled with both hands, sweating, "this is killing me" expression.

- LEFT: "Crying Cat Head" — round cream-white cartoon cat with massive teary eyes streaming dramatic tears down both cheeks, mid-stride running with one leg lifted high, black tank top with neon yellow accent, smiling through tears.

- RIGHT: "Pain Mask Dog" — small white cartoon dog with exaggerated suffering mask expression, eyes squeezed shut, eyebrows pulled together in agony, sweat droplet on forehead, mouth open in silent scream, both arms raised holding a black kettlebell overhead, determined squat stance, black tank top with neon yellow accent.

- BOTTOM-RIGHT corner (smaller, ~30% scale): "Yellow Bean Person" — round egg-yolk-yellow bean character with dot eyes and tiny relieved smile, sitting collapsed cross-legged hugging a red Hyrox finisher medal, post-race exhausted but content.

All characters share the visual emotional thread: "I am suffering and I chose this". Unified sticker-illustration style. No real photo references embedded.

BACKGROUND (upper 40%): stylized Shanghai Bund skyline silhouette — Oriental Pearl TV Tower on the left, Lujiazui supertall trio (Shanghai Tower, World Financial Center, Jin Mao Tower) on the right. Soft sunset gradient from warm orange at horizon to deep navy at top.

TEXT OVERLAY:
- Top headline (massive, neon yellow Chinese text, bold sans-serif): 「100 万人在跑」occupying about 25% of canvas width at top, with subtle black outline for legibility against sky
- Subline below headline (medium white Chinese text): 「营收一年涨 50%」
- Bottom-right corner small mark: minimal "HYROX" wordmark in neon yellow

COLOR PALETTE: black + neon yellow (Hyrox brand) + soft warm sunset gradient + Bund silhouette deep navy + meme character signature colors (Bitter Melon jade-green, cream-white for cat and dog, egg-yolk yellow for bean).

STYLE: Chinese internet meme mashup poster, self-aware comedic, sticker-friendly illustration aesthetic. Avoid photoreal, avoid embedded reference photos, avoid generic Q-style mascots — characters must read as recognizable meme figures redrawn in unified sticker style.

--ar 3:4 --stylize 250
```

## 推荐
- 适合首图的：Final Cover Prompt（直接用）
- 背景如果要改，优先改：`Background Prompt` → 重新合成 `Final Cover Prompt`
- 角色替换池（如果某只 meme 不好出图，按这个序列替换）：
  - 苦瓜女士 → 不可替换（C 位锚，整张图的喜剧立足点）
  - 流泪猫猫头 → 悲伤蛙 / 沮丧蛙
  - 痛苦面具小狗 → 「我裂开了」西瓜 / 黄豆人放大版
  - 黄豆人 → doge / 葛优躺小人
- A/B 版本：场景主导（默认）vs 数字主导（headline 换「营收涨 50%」副「100 万人在跑」）

## 如果要继续改
- 角色不要超过 4 个：5+ 会变成乱炖，反差喜剧需要每个角色被看清
- 不要动什么：苦瓜女士 C 位 + 推橇动作（情绪锚 + 动作锚）+ 黑底霓虹黄配色
- 数字层级要保住：100 万 > 营收涨 50% > HYROX 标记
- 风险与回退：
  - 如果生图工具画不出可识别的「苦瓜女士」（中文 meme 在西方模型可能识别度低），改成「a woman whose face has bitter melon texture, wrinkled brow, tearful eyes」纯描述版
  - 如果整张图角色太满 → 砍掉黄豆人，只保留 3 个主角
  - 如果 meme 风格 5-16 当天反响一般 → 5-17 赛后那篇回退到 Q 版吉祥物（视觉宪法默认）

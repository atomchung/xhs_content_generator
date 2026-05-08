# Hyrox 续集封面 prompt — 100 万人在跑 + 营收涨 50%

## 推荐风格
- 风格：Q 版健身吉祥物风（实况野球豆薯感 + Hyrox 品牌色）
- 为什么选它：账号 2025-06-03 那篇 Hyrox 帖（2945 views / 43 分享）就是 Q 版，账号已被算法 + 老粉认 "Q 版 Hyrox" 标签；续集保留风格 = 老粉一秒认出 + 新读者继承上一篇分享惯性
- 这张图最该卖什么：**数字「100 万」的视觉冲击 + 「营收一年涨 50%」的体量论点**

## Story Atoms
- 主角：3 个 Q 版健身吉祥物（多元身形：高壮男 + 中等女 + 标准男），承担"百万人都在跑"的群像感
- 动作瞬间：1 个奔跑中（侧面，腾空一脚）+ 1 个推黑色铁橇（弓步发力）+ 1 个壶铃高举（双手过头）
- 情绪冲突：「百万人在跑」 vs 「营收一年涨 50%」 → 现象级体量 + 商业故事感
- 背景符号：上海外滩剪影（东方明珠 + 陆家嘴三件套：上海中心、环球金融、金茂）+ Hyrox 品牌色（黑底 + 霓虹黄）

## Generation Order
1. Subject anchor（先锁角色 + 动作）
2. Background layer（外滩剪影）
3. Final cover（合成 + 加大字）

## Style 1 — Anime Cover（本案不走，仅留备份）
- 跳过原因：Hyrox 没有单一明星主角，热血动漫名场面构图（单人英雄站姿）不适配；账号验证 Q 版 = 这条线流量基本盘

## Style 2 — Mascot Q（推荐）
- 风格摘要：実況野球豆薯感 + 小红薯吉祥物 + Hyrox 品牌黑黄配色，圆豆身、短手短脚、厚黑描边、点状黑眼，画面干净不堆道具
- 可爱元素：黑色铁橇、霓虹黄 Hyrox logo 背心、小汗珠、红色完赛奖牌（未上身）

### Subject Anchor Prompt（只画人物）
```text
3 chibi Q-style fitness race mascots in a Hyrox-style functional fitness scene, dough-round bodies, short stubby limbs, thick black outline, simple dot eyes, minimal facial features, friendly and energetic.

Mascot 1 (left): tall muscular male character, mid-stride running pose with one leg lifted high, sweat droplet, wearing black athletic tank top with neon yellow accent, black shorts.
Mascot 2 (center, slightly forward): average-build male character, lunging deep while pushing a heavy black sled forward with both hands, intense focused expression, neon yellow Hyrox-style tank top.
Mascot 3 (right): female character with short ponytail, raising a black kettlebell above head with both arms, smiling determined, black tank top with neon yellow accent.

Plain off-white background. Centered group composition. Clean Q-style mascot illustration, sticker-friendly, brand mascot poster aesthetic. No clutter, no extra props.

--ar 3:4 --stylize 250
```

### Background Prompt（背景层，可独立替换）
```text
Stylized Shanghai Bund skyline silhouette in clean flat illustration style. Iconic landmarks: Oriental Pearl TV Tower (left), Lujiazui supertall trio — Shanghai Tower, Shanghai World Financial Center (the bottle opener), Jin Mao Tower (right side). Soft sunset gradient sky from warm orange at horizon to deep navy at top. Empty middle ground for subject placement. Minimal, no people, no boats, no clutter.

--ar 3:4
```

### Final Cover Prompt（最终封面，给生图工具用）
```text
Magazine-style fitness race poster cover, 3:4 vertical layout.

FOREGROUND (lower 60%): 3 chibi Q-style mascots from Hyrox-style fitness racing — left mascot tall muscular male mid-stride running with one leg lifted, sweat droplet; center mascot average male in deep lunge pushing a heavy black sled with both hands forward, focused expression; right mascot female with short ponytail raising a black kettlebell above her head with both arms, smiling determined. All wearing black athletic tank tops with neon yellow Hyrox-style accents and black shorts. Round dough-like bodies, short stubby limbs, thick black outlines, simple dot eyes, minimal facial features. Friendly and energetic.

BACKGROUND (upper 40%): stylized Shanghai Bund skyline silhouette — Oriental Pearl TV Tower on the left, Lujiazui supertall trio (Shanghai Tower, World Financial Center, Jin Mao Tower) on the right. Soft sunset gradient from warm orange at horizon to deep navy at top.

TEXT OVERLAY:
- Top headline (massive, neon yellow Chinese text, bold sans-serif): 「100 万人在跑」occupying about 25% of canvas width at top, with subtle black outline for legibility against sky
- Subline below headline (medium white Chinese text): 「营收一年涨 50%」
- Bottom-right corner small mark: minimal "HYROX" wordmark in neon yellow

COLOR PALETTE: black + neon yellow (Hyrox brand) + soft warm sunset gradient + Bund silhouette deep navy.

STYLE: official Hyrox brand chibi mascot event poster, clean composition, no random props, no extra decoration, no chibi mascots in background. Kid-book friendly Q-mascot illustration but with sport-event poster polish.

--ar 3:4 --stylize 250
```

## 推荐
- 适合首图的：Final Cover Prompt（直接用）
- 背景如果要改，优先改：`Background Prompt` → 重新合成 `Final Cover Prompt`
- A/B 版本：场景主导（headline 「100 万人在跑」+ 副 「营收涨 50%」）vs 数字主导（headline 「营收涨 50%」+ 副 「100 万人在跑」）。当前默认走场景主导，5-16 当天发布 = 现场感优先

## 如果要继续改
- 背景优先改什么：上海剪影是否要换更具识别度的（外白渡桥/南浦大桥）or 加渐变光效
- 不要动什么：3 个 Q 版角色的 dough-body + dot eye + 黑底霓虹黄配色（这是和上一篇 Hyrox 帖建立的视觉锚，老粉一秒认出）
- 数字层级要保住：100 万 > 营收涨 50% > HYROX 标记，三层视觉权重不能乱

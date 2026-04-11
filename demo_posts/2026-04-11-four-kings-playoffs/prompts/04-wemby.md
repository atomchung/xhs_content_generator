## 这张图的任务

让人看见"身高异形 + 防守恐怖"的视觉冲击。文班的 archetype 是"新王 + DPOY"。最该卖的是**签名防守动作 + 一串让人退却的数字**（3.0 BPG 盖帽王 + DPOY 赔率 -5000）。

**修正说明（重要）**：旧版 prompt 里写的 "DRTG 101.7 全联盟第一" 是错的事实点，已整体替换。现在防守 headline 走两条明确的数字——**DPOY 赔率 -5000 隐含概率 ≈98% + 全联盟盖帽王 3.0 BPG**——这两条都经过核对。

## 锁定风格：Blue Lock 现代日式

- 画风：Blue Lock（ブルーロック）+ First Slam Dunk 新剧场版主视觉
- flat-shaded 数码上色、冷色调、清晰 HUD 文字层
- 背后 ego-beast：**The Coyote**（马刺灰狼吉祥物）flat-shaded 剪影，冷眼咆哮

## 签名动作：追身盖帽（chasedown block from weakside）

文班最 iconic 的防守动作：

- 从弱侧从后方飞身扑过来
- 一只手臂完全伸直，**从后上方往下扫**
- 对方正在上篮，他在对方毫无察觉的情况下从后方把球拍掉
- 脸部表情冰冷专注，眼神锁定对方手里的球
- 夸张的长肢体比例（anime manhua 允许）
- 镜头从低处往上仰拍，让他的身高看起来更不像人

这是他防守招牌。和正文里 "DPOY 赔率 -5000 / 盖帽王 / 22 岁首次季后赛" 的叙事完全对位。

## Final Prompt

```text
Vertical 3:4 single-character poster in the exact style of Blue Lock (ブルーロック) character key visuals and the First Slam Dunk 2022 movie poster — modern clean digital flat shading, thin neon outlines, cold cinematic lighting, HUD data overlays baked into the image, ego-beast aesthetic, icy desaturated base palette with saturated teal-silver neon accents. The overall color temperature must be noticeably colder than the other three character cards in this set.

Subject: an ultra-tall lanky 22-year-old French center in a San Antonio Spurs black-and-silver jersey #1, captured mid CHASEDOWN BLOCK from the weakside — flying in from behind an unseen layup attempt, one arm (right) fully extended downward to swat the ball away from above, the other arm trailing for balance, body stretched at full length in mid-air, elongated anime-proportioned limbs that make him look inhuman, cold piercing eyes locked on the ball, calm killer expression (not angry — cold). Camera tilted sharply upward from below so he dominates the frame vertically and looks impossibly tall.

CRITICAL POSE DETAIL: the blocking arm must be reaching DOWNWARD from above, not upward. This is a chasedown block from behind, NOT a dunk and NOT a normal block. His body should be nearly horizontal in the air at the peak.

Background ego-beast: behind him, a massive flat-shaded silhouette of THE COYOTE (the San Antonio Spurs' official gray coyote mascot) rendered as a predatory ego-beast — crouched low, eyes glowing cold cyan, teeth bared in a silent growl, body rendered as a single bold flat-color silhouette in cold gray/black. The Coyote silhouette must fill the upper half of the background behind the subject.

Aura & color: pale teal neon rim-light on the subject's silhouette, cold white lightning particles tracing his wingspan, deep matte-black base background for maximum cold contrast. Teal-silver atmospheric particles.

HUD overlay, Blue Lock style (all baked into the image):
- Top-right large uppercase label "WEMBY" in Alibaba PuHuiTi Heavy / bold sans-serif, white fill with thin black outline and teal drop-shadow, huge and bold like a fighting game character name plate.
- Directly under "WEMBY", smaller white monospace subtitle: "San Antonio Spurs · #1 · age 22".
- Left-middle structured stat block in white monospace, framed by thin neon grid lines:
  "BPG      3.0    ← LEADS LEAGUE"
  "DPOY     -5000  ← IMPLIED 98%"
  "PPG      24.8"
  "SEED     WEST #2"
- Secondary line smaller: "first career playoffs · Spurs back since 2018-19".
- Bottom banner, thin Chinese tagline: "他一个人把马刺抬到了西部第二".
- Small corner tag top-left: "PLAYER 03 / 04".

Background: deep matte-black arena, thin digital neon grid overlay like a game UI, blurred silhouette of a helpless opposing layup attempt at the bottom-left of the frame — a small player figure reaching toward the rim, his ball already being swatted away. Faint San Antonio Spurs court lines visible in the far distance as cold silver threads. NO ink textures, NO paint textures, NO brush strokes — fully clean digital finish.

Style notes: this is modern Japanese sports anime key visual — Blue Lock / First Slam Dunk / ego-beast aesthetic. NOT manga ink, NOT painterly, NOT photorealism. Cold clean flat shading, thin neon outlines, sharp legible typography. Subject occupies ~75% of frame vertically due to his height and the stretched chasedown pose, face and blocking arm both clearly readable, the Coyote silhouette behind him is clearly identifiable as a canid predator (not a generic wolf, not a dog), HUD text sharp and legible. Aspect ratio 3:4 vertical.
```

## 如果要继续改

- 最容易失败的一点：把 chasedown block 画成正面防守或者 dunk——这时候在 prompt 里额外强调 "the defender comes from BEHIND, the ball is below him, his arm reaches DOWN not up"
- 如果 Coyote 被画成普通狼/狗 → 强调 "stylized cartoon coyote mascot silhouette, NOT a realistic wolf"
- 如果 Wemby 看起来"只是很高"但没有恐怖感 → 把镜头再往低处拉、让他占满整个纵向画面

## 不要动什么

- 追身盖帽动作（从后方 + 一臂向下扫）
- 冷青绿 + 银主色（必须明显比其他三张更冷）
- The Coyote 吉祥物剪影当背景 ego-beast
- "WEMBY" 英文大号 label（不是"未来"）
- 马刺 #1 球衣
- 夸张身高比例
- 半身 + 低角度仰视
- Blue Lock flat-shaded 数码画风
- 3:4 纵向比例

## 事实校正清单（不要写错的事项）

- ✅ 3.0 BPG（不是 4.1）
- ✅ DPOY 赔率 ≈-5000 / 隐含 98%
- ✅ 22 岁
- ✅ 首次进季后赛
- ✅ 马刺西部第 2 种子，3/19 锁定
- ✅ 马刺自 2018-19 赛季以来首次进季后赛
- ❌ 不要写 "Spurs DRTG 101.7 全联盟第一"（错）
- ❌ 不要写本季"中段小腿伤缺阵"（2025 年初 DVT 是上赛季的事）

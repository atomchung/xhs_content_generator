# Aaron Judge 封面 prompt — 法官的 follow-through 破框 + 数据浮字

## 推荐风格
- 风格：canonical 3D comic break-out（账号金本，全题型默认）
- 为什么选它：真人动作题 + 高张力 + 力量爆发瞬间，落到双轴决策表「人物动作题 / 高张力」格的 ⭐ canonical；正文核心是"评价打者"+ WAR 总分卡，封面用现役 WAR 王 Judge 直接对应
- 这张图最该卖什么：**Judge 击球瞬间的力量感 + 标题"法官 JUDGE"双语并置的拦停感**

## Story Atoms
- 主角：Aaron Judge（HIGH tier，confidence 88，直接用名字）
- 动作瞬间：球棒已接触球的瞬间 + follow-through 起势 — 双手紧握球棒挥到右肩高度，身体重心已转过来，下颚抬起目光追着球飞出去的方向
- 情绪冲突：原始挥棒力量 vs 数据时代（封面破框处可点缀 launch angle 角度尺微浮现，不抢主角）
- 背景符号：Yankee Stadium 夜场，外野看台 + 旗帜灯光 bokeh，扬基条纹白底（pinstripes）+ 海军蓝阴影
- 时代锚：现役（2024-25），队长 C 字章在胸前

## Person Recognition Gate

```json
[
  {
    "person": "Aaron Judge",
    "confidence": 88,
    "tier": "HIGH",
    "reason": "Yankees captain since 2022, 2022 + 2024 AL MVP (62 HR record season + 11.4 bWAR), 8+ years mainstream MLB coverage, distinctive 6'7'' / 282 lbs frame and full beard make likeness training very deep",
    "anchors_suggestion": null
  }
]
```

→ HIGH 直接用名字，不加额外外貌锚点。

## 字幕（封面文字 — 后期叠字）
- 大标题（中下，第一视觉）：「法官 JUDGE」（横排两段：「法官」中文 + 「JUDGE」英文）
- 小标题（顶部细字）：「MLB 最强打者」
- 字体：阿里巴巴普惠体 Bold/Heavy，「JUDGE」英文用 condensed sans bold（呼应法庭/审判的标牌感）
- 配色建议：白字描黑边主体；「JUDGE」用霓虹金或 Yankees 海军蓝填色，呼应队伍色
- prompt 内 NO TEXT，所有字用 overlay_cover_text.py 后加

## Final Prompt

```text
3D comic break-out illustration cover, 3:4 vertical, Major League Baseball power hitter scene at night.

FOREGROUND (lower 70%): Aaron Judge mid-swing follow-through apex, framed from mid-thigh up, body torqued through the swing, hips fully rotated facing the camera-right side, both hands gripping the bat which is angled up toward the upper-right corner of the frame at shoulder height, bat barrel breaking out of the inner panel border. Head tilted up slightly, eyes locked on the ball flying out of frame to the upper right, jaw set, chest visibly puffed under the strain. Wearing classic New York Yankees home uniform — vertical pinstripe white jersey with navy interlocking "NY" on the left chest, navy "C" captain's patch above the heart, jersey number 99 visible on the left sleeve. Massive 6'7'' build, broad shoulders, well-trimmed full beard, short dark hair under the navy Yankees batting helmet. Sweat glint on the brow. Physically-rendered manga figure with photo-accurate likeness, rendered as comic illustration (not photo).

MID-GROUND (break-frame element): the bat barrel and a faint motion-arc trail of the swing pop forward of the inner panel border on the upper-right corner, creating the canonical 3D break-out effect. Subtle warm-yellow speed-arc lines radiate from the contact zone (very restrained, only 3-4 short arcs).

BACKGROUND (upper 30%): blurred bokeh of Yankee Stadium night-game stands — out-of-focus silhouettes of fans, white frieze along the upper deck, scattered camera flashes as small bright dots, deep navy night sky. Single dramatic spotlight from upper-left rim-lighting the figure's shoulder and bat.

COLOR PALETTE: Yankees navy + pinstripe white + warm stadium yellow rim-light + black ink outlines. Limited palette, high contrast, comic-book grain.

STYLE: canonical 3D comic break-out — physically-rendered manga figure with photo-accurate likeness, rendered as comic illustration (not photo). Bold black outlines on figure, soft cel-shading, comic panel break-frame composition with the bat barrel breaking the inner border. No watercolor, no aura, no speed lines beyond the 3-4 restrained arcs, no beams, no gold leaf.

NO TEXT in the generated image (all titles added in post-processing).

--ar 3:4 --stylize 250
```

## 推荐
- 适合首图的：上面这版 Final Prompt 直接用
- 后期叠字：用 `scripts/overlay_cover_text.py` 加阿里巴巴普惠体 Bold/Heavy
  - 顶部小字：「MLB 最强打者」（白色描黑边）
  - 中下大字：上行「法官」中文 / 下行「JUDGE」英文（英文加大、字间距撑开做"法庭判决书"质感）
  - 「JUDGE」描色建议：Yankees navy 填 + 霓虹金描边（高识别度配色）

## 如果要继续改

- 背景优先改什么：
  - 如果觉得 Yankee Stadium 夜场太一般 → 换成主场打过 walk-off 的近景外野墙 + 飞越的球
  - 如果想强化"数据时代"暗示 → 在球棒尾迹处叠一条非常浅的 launch angle 角度尺刻度（数字「28°」浮现），但不要抢主角
- 不要动什么：
  - Judge 的扬基条纹球衣 + 队长 C 字章（这是他识别度核心，比脸还快被认出）
  - 双手挥棒 follow-through 姿势（比单手挥棒更有"力量定格"感，呼应"最强打者"标题）
  - canonical 措辞（physically-rendered manga figure with photo-accurate likeness, rendered as comic illustration — not photo）
  - 限定调色板（navy + 白条纹 + 暖黄 + 黑，多了画面会乱）
- 如果想做系列封面：
  - 同构图换主角 → Shohei Ohtani（投打二刀）/ Mookie Betts / Bobby Witt Jr. — 都是当代 WAR 王梯队
  - 换标题语 → 「击球之神 OHTANI」/「速度之王 WITT」（同款"中文称号 + 英文姓"双语对照）

## 关键备忘
- Judge 球衣号 99（不是 27，27 是退役)
- 队长 C 字章是 2022 起加上的，不要漏
- 6'7'' 是他的招牌身高，构图时人物比例应该看起来比一般打者更高大（占画布高度的 ~75%）
- 球棒型号他常用 Chandler 或 Marucci，但封面画到这种细节没必要

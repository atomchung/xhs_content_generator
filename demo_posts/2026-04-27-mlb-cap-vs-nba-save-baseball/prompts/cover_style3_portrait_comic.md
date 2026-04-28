# MLB 帽封面 prompt — Style 3：类真人形象照（漫画化人像）

## 推荐风格

- 风格：physically-rendered manga figure with photo-accurate likeness, rendered as comic illustration（人像 close-up + 自然街头光 + 漫画化渲染，对应账号视觉宪法第 2 / 3 条 — 看得出像真人但不是照片）
- 为什么选它：用户要求「类真人形象照」。账号视觉宪法禁 photoreal 关键词，所以走 canonical 的等价做法 — 像本人脸、漫画质感渲染。这个风格跟 canonical-breakout 同一血缘，是最稳的 fallback
- 这张图最该卖什么：**一张脸 + 一顶帽 + 一个无声的街头瞬间，让读者下意识替自己代入「我也戴过这顶帽」**

## Final Prompt

```text
A 3:4 vertical magazine-style portrait cover. Single subject in foreground: a young Chinese person in their early 20s, ambiguous gender expression, short modern haircut, calm neutral expression with eyes looking slightly off-camera (not direct gaze), photo-accurate East-Asian likeness rendered as comic illustration (not photo). The composition is a tight chest-up portrait, head occupying about 35% of canvas height, centered slightly upper-left.

Wardrobe: black baseball cap worn straight with the iconic crisp white "MLB" wordmark prominent on the front panel — the cap is the visual anchor of the entire cover. Oversized cream-white cotton hoodie with a thin warm red drawstring, no other graphics on the hoodie. Shoulders and upper chest visible, frame cuts at upper sternum.

Background: shallow-depth-of-field Shanghai street at golden-hour late afternoon, blurred ginkgo leaves and warm bokeh, a faint out-of-focus storefront with a partial Chinese character sign, soft warm window light catching the right side of the face. The background is rendered as soft watercolor-like comic wash, NOT photographic.

Rendering rules:
- physically-rendered manga figure with photo-accurate likeness, rendered as comic illustration (not photo)
- crisp clean ink linework on facial features and cap edge
- soft cell-shaded skin tones with two-tone shadow
- hair rendered with clean comic strands, not photoreal hair
- background rendered with deliberate watercolor brush-edge softness so it visibly differs from the subject's render style — the figure is comic, the world around it is comic-wash

Lighting: warm golden window-light from camera-right hitting the cap brim and one cheek; cool ambient shadow on camera-left side; subtle rim-light on the hoodie's left shoulder edge.

TEXT OVERLAY (clean modern sans-serif, magazine cover layout):
- Top-left vertical mark (small mono): 「MLB cap」 / 「不是美国棒球做的」 stacked, low opacity warm gray
- Bottom headline band (massive bold Chinese, warm off-white over a thin transparent dark band): 「中国一千家店」 — bottom 14% of canvas
- Subheadline directly below: 「背后没一个美国人」 in slightly smaller weight

COLOR PALETTE: warm cream + soft warm red + golden-hour amber + deep cool charcoal shadow + crisp white cap wordmark.

STYLE: editorial portrait cover, comic illustration style, magazine-grade restraint, no clutter, no random graphics, no extra people, no logos other than MLB on the cap.

--ar 3:4 --stylize 250
```

## 如果要继续改

- 背景优先改什么：街景从「上海梧桐落叶」可以换成「成都太古里」或「北京三里屯」 — 同样街头属性，不同地标识别度；不要换成室内
- 不要动什么：渲染语言 — 人物漫画化、背景 watercolor wash，**两层都不能滑向 photoreal**；MLB 帽是单一视觉锚
- 关键约束：prompt 里绝不能出现 `photorealistic / photoreal / studio photo / 8k photo / octane render / reference photo` — 一旦滑过去就违反视觉宪法第 3 条

## 视觉宪法合规说明

用户原始需求是「类真人形象照」。本 prompt 用 canonical 等价做法实现：**像本人 ≠ 照片**。如果生图后觉得「还不够像真人」，下一版调整应该往「面部 anchor 更精确 / 五官比例更精确」走，**不要**往「加 photoreal 关键词」走。


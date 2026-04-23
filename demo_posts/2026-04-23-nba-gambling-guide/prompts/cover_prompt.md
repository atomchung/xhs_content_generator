# 第二篇封面 prompt — v2（已对齐前篇风格与审核红线）

## 前情对齐

- 前篇封面（`demo_posts/2026-04-20-silver-gambling-ledger/prompts/cover_prompt.md`）走的是 Silver 肖像 + Scorsese 式天平两边帐本 —— 主视觉是一个人 + 两边账
- 本篇不重复那个构图，也不再用 Silver 做封面。**主视觉改成一条赔率曲线**：一个人不出面，只有一条被一个人拉扭的线。视觉母题从「人物 + 帐本」转到「一条线的跳水」
- 风格家族保持一致：editorial collage / desaturated / crimson accent，**不走 canonical break-out**（非动作题）

## 推荐风格
- 风格：Editorial collage + line-chart hero
- 为什么选它：承前篇的 editorial 调性，视觉母题换成一条曲线——把「单人就能扭曲一条线」直接变成主视觉，比任何人物剪影都更精准
- 这张图最该卖什么：「一条线」被单人拉扭的瞬间；球员本人弱化到背景剪影
- 真人风险：**不画任何真实球员**。背影剪影是 generic / anonymous / blurred jersey number，直接规避 Person Recognition Gate

## Final Prompt

```text
Editorial sports-investigation magazine cover, 3:4 vertical aspect ratio, moody noir-editorial palette.

Primary visual: a large hand-drawn data line chart dominating the center of the frame. The line starts on the left at a calm positive value labeled "+120", runs flat for a short stretch, then crashes downward sharply to the right, ending at a deep low labeled "-250". Beneath the crashing line, a thin crimson horizontal dashed reference line is labeled "2.5" in small white type. The line chart should feel like a heartbeat monitor going flat — clinical, urgent, off-balance.

Background: faint newspaper halftone texture, desaturated court-wood brown and deep navy, with a single crimson red accent used only on the dashed reference line and the "-250" label. No bright pop-art colors.

In the lower-left foreground: a small anonymous NBA player silhouette seen from behind, wearing a generic modern basketball jersey with the number intentionally blurred / unreadable. No face. No team logo. Not based on any real player. He is walking away from the chart, small in scale, head slightly lowered. His silhouette overlaps faintly with the start of the crashing line, suggesting causation without showing it.

Around the edges: torn paper fragments of a mobile sportsbook interface showing the short English fragment "UNDER 2.5" in small type, and a faint shadowy stack of paper arrows indicating money flow. Kept intentionally small — the line chart is the hero, not the collage.

Composition: top 1/3 reserved as negative space for a bold Chinese headline block (headline will be overlaid in post-production, not rendered by AI). Middle 1/2 is the line chart + small silhouette. Bottom 1/4 has the collage fragments fading out.

Texture: slight paper grain, halftone dots around the crimson accents, editorial magazine feel similar to Bloomberg Businessweek investigative covers or The Athletic long-form feature illustrations.

No text rendered by the AI except the tiny number labels "+120", "-250", "2.5", and "UNDER 2.5". All Chinese copy is overlaid in post-production.

--ar 3:4 --stylize 300
```

## 标题叠加指引（后期 overlay）

- 标题：`三道防线`（第一行）`堵不住的那块市场`（第二行）
- 字体：阿里巴巴普惠体 Heavy
- 颜色：白字 + 细 crimson 描边（呼应图内红色虚线锚点）
- 位置：上 1/3 negative space，左对齐
- 两行字数控制在 4 / 8 以内（符合 xhs-note-assembly 的两行封面限制）

## 如果要继续改

- 如果线太抽象、没读者识别度：在 "+120" 和 "-250" 标签旁加一个更显眼的「↘」下降箭头作视觉引导
- 如果背影剪影太小看不见：把剪影移到右下角第三象限，放大到 height 的 1/4 左右——但不得超过 1/3，否则曲线会被抢
- **不要动的**：
  - 不画任何真实球员脸 / 号码 / 球队 logo
  - 不让 AI 渲染中文（只渲染 +120 / -250 / 2.5 / UNDER 2.5 这几个英文数字标签）
  - 不加 watercolor / aura / speed lines / Pop Art 这些 canonical 禁区词（虽然本题本身就不走 canonical，但风格包稳定性仍需维护）
  - 3:4 竖版不可动
  - crimson 只用在 2.5 虚线和 -250 标签上——不要泛红

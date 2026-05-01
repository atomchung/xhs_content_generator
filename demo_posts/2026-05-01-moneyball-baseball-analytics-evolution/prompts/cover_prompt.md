# Aaron Judge 封面 prompt v2 — 固定 follow-through 动作 + 4 风格变体

## v1 复盘 → v2 修法

| v1 问题 | v1 现象 | v2 修法 |
|---|---|---|
| 挥棒姿势奇怪 | 「mid-swing follow-through apex」太模糊，MJ 误读成静态拼贴 | 锁定具体名场面：**击球后 bat-watching follow-through**（HR 之后举棒注视球飞出去）— Judge 全联盟最辨识的招牌动作 |
| 背景诡异 | 看台 bokeh + 闪光点形状失控，画面糊成一团 | 砍掉细节人群 — 只留：深海军蓝夜空 + Yankee Stadium 标志性白色 frieze 剪影 + 单道顶光 |
| 画框感不知道是啥 | break-frame 没显式说，MJ 默认不画 panel border | 显式描述「thick black ink panel border around canvas, broken open in upper-right where bat barrel bursts forward」— 画框先存在才能破 |
| 线条感薄弱 | cel-shading + outline 没强调权重 | 显式强调「bold uniform-weight black ink contours, heavy silhouette, manga inker line work」+ 限制内部填色细节 |

**新策略：固定动作不变，跑 4 个风格，发图后挑赢的那张升 ⭐ canonical for MLB 题型。**

---

## 固定动作（4 个 prompt 共用）— Bat-Watching Follow-Through

Judge 全联盟最辨识的招牌姿势。基本是他打 HR 后的标准定格：

- **接触已发生**（球已离开棒头），不是挥棒中
- **球棒**：双手仍握，已挥到左肩高度过头，棒头指向画面左上方
- **躯干**：从打击站位扭转过来，3/4 视角面对画面右侧（投手方向）
- **重心**：完全转到前脚，后脚跟微抬
- **头部 / 视线**：下颚抬起，眼睛锁着球飞出去的方向（画面右上 / 出框）
- **表情**：嘴闭、下颌紧、stoic 不张扬（不是欢呼，是"我知道这球没了"的笃定）
- **构图**：人物从胸口以上撑出画布约 70%，球棒 + 视线方向把画面拉向右上，留出 title 空间在中下/底

## Visual Anchors（Judge 必须有的识别度）

- **身高 / 体型**：6'7'' / 282 lbs，画面里要看起来明显比一般打者高大、肩宽超过普通框
- **球衣**：Yankees pinstripe 主场白底（细海军蓝直条纹），navy 联锁 NY 标在左胸
- **队长 C 字章**：左胸 NY 标上方一个小型 navy 圆形 "C" patch（2022 起，**漏了就不像 Judge**）
- **球衣号 99**：左袖、背面都有
- **头盔**：navy 打击头盔，正面白色联锁 NY，单耳 flap 伸到右脸（右打者）
- **脸**：方下颌，full dark beard 修齐，眉骨重，无墨镜
- **球棒**：深色木棒（Chandler 或 Marucci 风），颜色接近黑棕

## Person Recognition Gate

```json
[
  {
    "person": "Aaron Judge",
    "confidence": 88,
    "tier": "HIGH",
    "reason": "Yankees captain since 2022, 2022 + 2024 AL MVP, 8+ years mainstream MLB coverage, distinctive 6'7'' frame and full beard make likeness training very deep",
    "anchors_suggestion": null
  }
]
```

→ HIGH 直接用名字。Visual Anchors 写在这里是给后期叠字 / 排版参考，不需要全塞进 final prompt。

## 字幕（封面文字 — 后期 overlay_cover_text.py 加）

- 顶部小字：「MLB 最强打者」（白字描黑边）
- 中下大字：上行「法官」中文 / 下行「JUDGE」英文（英文加大撑开字间距）
- 「JUDGE」描色：Yankees navy 填 + 霓虹金描边

---

## Style A — canonical 3D comic break-out（v1 修复版）

**最该走这条**：账号金本，动作题默认。v1 的 4 个问题这次都显式修了。

```text
3D comic break-out illustration cover, 3:4 vertical, single hero baseball power-hitter portrait.

POSE (locked): Aaron Judge in bat-watching follow-through stance — the swing is finished, the ball has just left the bat. Both hands still grip the bat which has swung up and over his left shoulder, the bat barrel angled toward the upper-left of the frame. His torso is rotated three-quarters toward camera-right (toward the pitcher's mound), front foot planted with all weight on it, back heel slightly lifted. His chin is tilted up, eyes locked on the unseen ball flying out toward the upper-right of the frame and beyond, jaw clenched, mouth closed in stoic focus — the look of a man who already knows the ball is gone. Framed from mid-thigh up, figure occupies ~70% of canvas height.

CHARACTER (Aaron Judge, locked): towering 6'7'' frame with broad shoulders that fill the panel width, full dark beard neatly trimmed, square jaw, focused dark eyes shaded under the helmet brim. Wearing classic New York Yankees home uniform — vertical pinstripe white jersey with navy interlocking "NY" on left chest and a small navy captain's "C" patch above the heart, jersey number 99 on left sleeve. Navy Yankees batting helmet with white interlocking NY logo on the front, single right-side ear flap. Dark wood bat. Physically-rendered manga figure with photo-accurate likeness, rendered as comic illustration (not photo).

COMIC PANEL FRAME: a thick uniform-weight black ink panel border frames the entire 3:4 canvas; in the upper-right corner the panel border is BROKEN OPEN where the imaginary trajectory of the ball escapes — out of this break, a single bold sweeping motion arc curves outward into the white space beyond the panel, suggesting the ball's flight path. The bat barrel may also slightly cross the upper-left panel border to reinforce the break-out feel.

LINE WORK: bold uniform-weight black ink contour outlines on the figure, especially heavy along the silhouette and primary forms (shoulders, helmet brim, bat). Manga inker line quality — confident, not sketchy. Limited interior shading lines; rely on cel-shaded color blocks for form, not crosshatch. The panel border itself is the thickest line in the image.

BACKGROUND (kept simple): deep navy night-sky gradient (dark navy at top fading to slightly lighter steel-blue at horizon line). A single low-contrast silhouette of Yankee Stadium's iconic white frieze (the scalloped upper-deck arch detail) running across the upper third as a thin pale shape, no people, no individual seats, no flash dots. One single dramatic spotlight beam from upper-left rim-lighting the figure's right shoulder, helmet, and bat — the rest of the figure has soft cel-shaded form light.

COLOR PALETTE (locked, do not add colors): Yankees navy + pinstripe white + warm stadium yellow rim-light + black ink + small white frieze accent. Five colors total. High contrast, comic-book grain.

NO TEXT in the generated image (titles added in post-processing).

--ar 3:4 --stylize 250
```

---

## Style B — slam-dunk-classic（90s 灌篮高手原作风）

**为什么也试这条**：Judge follow-through 的"力量定格"和井上雄彦画樱木的 finisher 极像 — heavy ink + speed lines + crosshatching + 90s 少年漫的"瞬间静止"美学，能给"最强打者"加上热血少年漫的情感重量。

```text
1990s shonen sports manga illustration, single page hero panel, 3:4 vertical, in the style of Takehiko Inoue's classic Slam Dunk era (mid-1990s — heavy hand-inked black-and-white with selective spot color).

POSE (locked): Aaron Judge in bat-watching follow-through stance — the swing is finished, the ball has just left the bat. Both hands still grip the bat which has swung up over his left shoulder, bat barrel angled toward upper-left. Torso rotated three-quarters toward camera-right, front foot planted, back heel lifted. Chin tilted up, eyes locked on the unseen ball flying toward upper-right, jaw clenched, mouth closed in stoic focus. Framed from mid-thigh up.

CHARACTER (Aaron Judge): towering 6'7'' frame, broad shoulders, full dark beard, square jaw. Yankees pinstripe home jersey, navy "NY" left chest, small "C" captain patch, number 99. Navy Yankees batting helmet with white NY. Dark wood bat. Likeness should remain recognizably Aaron Judge but rendered in classic shonen manga style — defined linework, expressive eyes, slight stylization while keeping the actual facial features.

LINE WORK & STYLE: heavy hand-inked black contour lines, varying line weight — thicker on the silhouette and shadow side. Generous use of crosshatching and parallel ink hatching for shadows on the jersey folds, helmet curve, and beard. White highlights left as bare paper on the helmet, bat, and one shoulder edge. Background features bold radial speed lines (manga 集中线 / shuchūsen) emanating from behind the figure outward to the canvas edges, and 3-5 long horizontal speed lines streaking from the bat barrel into the upper right indicating the ball's trajectory.

BACKGROUND: minimal — pure white paper background broken only by the radial speed lines and a single rough screentone (Ben-Day dot pattern) gradient on the upper area suggesting sky/atmosphere. No detailed crowd or stadium.

COLOR: predominantly black-and-white manga inking with ONE selective spot color — navy blue used only on the Yankees pinstripes, helmet, and "NY" logo. Everything else stays in ink and white.

EMOTION: late-1990s sports manga finisher panel — quiet intensity, the moment after the decisive blow. Like Sakuragi watching a dunk leave his hands.

NO TEXT in the generated image.

--ar 3:4 --stylize 250
```

---

## Style C — 100m-poster（朱红日漫电影海报）

**为什么也试这条**：日本运动电影海报美学（《100 米》《灌篮高手 The First Slam Dunk》海报）— 单一英雄站立 / 力量定格 + 大块朱红 + 巨型 motion-blur 标题 — 跟"最强打者"的封号气场 1:1 对位。这条出来如果赢，就把它升 ⭐ canonical for MLB 海报题。

```text
Japanese sports cinema poster illustration, 3:4 vertical, in the style of contemporary Japanese sport-movie key art (e.g. "100m" / "The First Slam Dunk" theatrical posters) — single hero, monumental composition, dominant single accent color, cinematic stillness.

POSE (locked): Aaron Judge in bat-watching follow-through stance — swing finished, ball has just left the bat. Both hands grip the bat swung up over his left shoulder, barrel toward upper-left. Torso three-quarters to camera-right, front foot planted, back heel lifted. Chin lifted, eyes locked on the ball flying toward upper-right, jaw clenched, stoic focus. Framed from mid-thigh up, figure occupies ~75% of canvas height with monumental presence.

CHARACTER (Aaron Judge): towering 6'7'' frame, broad shoulders dominating the frame, full dark beard, square jaw, eyes shaded under helmet brim. Yankees pinstripe home jersey, navy "NY" left chest, "C" captain patch, number 99. Navy Yankees batting helmet with white interlocking NY. Dark wood bat. Likeness recognizably Aaron Judge.

STYLE — POSTER ILLUSTRATION: hand-illustrated key art quality with thick black contour outlines on the figure, soft poster-paint cel shading, slight grain texture overlay. The figure has a slight noble-statue stillness rather than dynamic motion. Limited tonal range — every form is one of three values (light / mid / shadow). Subtle textured brush noise across flat color fills (poster-grade, not airbrushed smooth).

DOMINANT COLOR: deep crimson red (vermillion / 朱) fills the entire background as a single flat field — no gradient, no detail, just pure crimson plane. The figure stands against this red field with high-contrast separation. Yankees navy + pinstripe white provide the only color counterpoint.

BACKGROUND DETAILS: nothing — pure crimson plane behind the figure. No stadium, no crowd, no horizon. The crimson IS the background. Optionally, a single very faint Japanese-style horizontal line grain at the very top edge (suggesting a paper-printed poster artifact).

COLOR PALETTE (locked): crimson red (dominant, ~60% of canvas) + Yankees navy + pinstripe white + black ink + warm skin tone. Five values total.

EMOTION: monumental, cinematic, restrained power — the quiet second AFTER the decisive moment. Like a Japanese movie poster announcing the protagonist's signature move.

NO TEXT in the generated image (the title overlay will sit on the crimson field).

--ar 3:4 --stylize 250
```

---

## Style D — slam-dunk-movie（The First Slam Dunk 电影版）

**为什么也试这条**：井上雄彦自导电影《The First Slam Dunk》(2022) 的视觉语言 — CG 立体造型 + 手绘墨线轮廓 + 安静、致敬感、情感重量。适合给"现役 WAR 王"做半 legend 化的封面，比 canonical 多一层"史诗"质感。

```text
Hand-drawn CG-hybrid sports anime illustration, 3:4 vertical, in the visual style of Takehiko Inoue's "The First Slam Dunk" (2022 film) — physically-volumed character with hand-inked contour lines, restrained color, quiet emotional weight.

POSE (locked): Aaron Judge in bat-watching follow-through stance — swing finished, ball has just left the bat. Both hands grip the bat swung up over his left shoulder, barrel toward upper-left. Torso three-quarters to camera-right, front foot planted, back heel lifted. Chin lifted, eyes locked on the ball flying toward upper-right, jaw clenched, stoic focus. Framed from mid-thigh up.

CHARACTER (Aaron Judge): towering 6'7'' frame with anatomically correct mass and weight, broad shoulders, full dark beard, square jaw. Yankees pinstripe home jersey, navy "NY" left chest, "C" captain patch, number 99. Navy Yankees batting helmet with white interlocking NY. Dark wood bat. Likeness recognizably Aaron Judge but slightly stylized in the Inoue-film way — refined facial structure, expressive but understated.

STYLE — INOUE FILM HYBRID: figure rendered with subtle 3D-feel volumetric form (proper anatomical mass, weight, shadow falloff on the shoulders and helmet), but ALL contours and key creases are drawn in hand-inked variable-weight black brush lines (not 3D outlines). Flat or barely-modeled cel color fills inside the contours. Background is washed pencil-and-ink texture suggesting place without rendering it photorealistically.

LINE WORK: hand-drawn brush ink lines, variable weight — bold along the silhouette and shadow edges, light or broken along the lit edges. Lines feel drawn by hand, not vector-clean. A few selective unfinished line ends suggesting the drawn medium.

BACKGROUND: very subdued — soft pencil-textured grey wash suggesting a stadium interior in low light, no detailed crowd or seats. A barely-suggested white frieze line shape at the upper edge implies Yankee Stadium without rendering it. The background should feel like a memory or echo, not a place.

COLOR PALETTE: muted, restrained — Yankees navy + off-white pinstripe + warm skin tone + soft graphite grey background + black ink. Lower saturation than a typical comic cover. Almost monochrome with selective color accent.

EMOTION: legend-treatment — quiet, weighted, the moment captured for memory. Not hype, not motion — stillness with gravity. The shot you'd put in the credits sequence.

NO TEXT in the generated image.

--ar 3:4 --stylize 250
```

---

## 跑图建议

1. **每条 prompt 各跑 1-2 张**（共 4-8 张）
2. **挑评分维度**：
   - 姿势是否清晰对到 bat-watching follow-through（v1 主要错的就是这个）
   - Judge 脸 + 体型识别度（C patch / 99 / 头盔 NY 都在）
   - 风格语言强度（A 是不是真有破框 / B 是不是真有 90s manga 感 / C 是不是真朱红 / D 是不是真有 Inoue 静默感）
   - 背景是否干净不抢戏
3. **赢家处理**：
   - 如果 A 赢 → 维持 canonical，更新 `references/cover-style-pool.md` 加注「v2 修了 v1 四个问题」
   - 如果 C 赢 → 把 100m-poster 升为 MLB 海报题型的 ⭐ canonical（之前是 sandbox）
   - 如果 B / D 赢 → 升级为 MLB 题型 sandbox → live-tested
4. **赢家叠字**：用 `scripts/overlay_cover_text.py` 加阿里巴巴普惠体 Bold/Heavy
   - 顶部小字：「MLB 最强打者」
   - 中下大字：「法官」（中）/ 「JUDGE」（英）
   - C 风格上叠字时建议 JUDGE 英文用白色（朱红底高对比）
   - A / B / D 风格上 JUDGE 用 Yankees navy + 霓虹金描边

## 不要动的（4 条 prompt 共用铁律）

- 动作锁定：bat-watching follow-through（不要改成 mid-swing / 触球瞬间 / 单手挥棒）
- Visual Anchors 6 项不能漏：身高巨大感、pinstripe、NY 胸标、C 队长章、99 号、navy 头盔
- `--ar 3:4 --stylize 250` 必须有
- 禁词：photoreal / photorealistic / 8k / octane / studio photo / reference photo
- prompt 内 NO TEXT — 字幕全部后期叠

# Cover Prompt — 七亿买下大谷的男人（V2 / 无标题 / Walter 居中）

## 本轮变更
- **标题文字全部移出封面**，只交画面，文字后续在 XHS 客户端或 `overlay_cover_text.py` 单独叠
- **主角换回沃尔特本人**：金融人 + 老白男 + 黑西装 + 眼镜 + 短灰发 + 沉静表情；这次他必须站在画面正中
- **背景塞他名下的球星**：道奇大谷 / 山本由伸 / 湖人 LeBron / Luka / 切尔西 Palmer / Cadillac F1 头盔等元素，构成「他收藏的人」的视觉
- **构图必须有梗**：脱掉账号默认「人物 + 数字 + 球场」结构，改成 4 种风格化的「收藏 / 君王」化构图
- 比例：竖版 3:4
- 硬规则：**no text, no logos, no watermark**（文字事后叠）

## 共用人物 brief（每个 prompt 都要遵守）

**Front subject（沃尔特）**
- middle-aged to older American businessman, late 50s to 60s
- short neatly combed grey hair, slightly receding hairline
- thin rectangular glasses
- clean shaven, calm reserved expression, faint knowing smile
- impeccable charcoal or navy business suit, white shirt, dark tie
- composed posture, hands either clasped, in pockets, or holding a single object depending on version
- centered in the frame, occupying roughly 45–55% of the canvas height
- this man is the main character, must be the sharpest, best-lit element

**Background athletes（按版本不同呈现）**
- a Japanese baseball player in a Los Angeles Dodgers home white pinstripe uniform with a royal blue cap, mid-swing follow-through
- another Japanese pitcher in the same Dodgers uniform, mid wind-up
- a tall powerful African-American basketball player in a Los Angeles Lakers purple and gold #6 jersey, mid-dunk
- a young European footballer in a Chelsea royal blue home kit, arms spread celebrating
- a Formula 1 driver helmet in Cadillac livery (black, white, red accents)
- a WNBA player in a Los Angeles Sparks purple and yellow jersey, mid-jumpshot
- treat them as **secondary**: smaller, slightly desaturated, framed around the central man, never sharper than him

**Universal negatives（每个 prompt 都加）**
```
no text, no captions, no letters, no numbers, no logos, no watermark,
no signage, no jersey numbers visible, no team wordmarks,
no extra crowd faces in focus, no blurry main character,
no cartoon for realistic versions, no dutch angle unless specified,
single central subject must remain dominant
```

---

## Version A — 宝可梦收集页面 / TCG card binder

**梗**：把沃尔特画成「训练家」，背后是一整页他「收齐」的球星卡。读者一眼就懂「这些人都被他收了」。

**画面定位**
- 视角正面，沃尔特半身居中，双手各捏住一张发光卡片（不必看清卡面），脸上一抹微笑
- 他身后是一面巨大的卡册墙：3×4 的卡套格子，每一格里框着一个球星的胸像 / 动作截影
- 卡片有 holographic foil 边框、圆角、淡淡反光；空格留 1–2 个暗示「还没收完」

**Prompt（贴 Midjourney / Gemini / ChatGPT 通用）**
```
Vertical 3:4 cinematic illustration, modern trading card collector aesthetic.
Foreground: a calm, confident older American businessman in a sharp charcoal
suit, thin rectangular glasses, short combed grey hair, faint knowing smile,
half-body centered composition, holding two glowing holographic trading cards
in his hands like a master collector, soft rim light on his shoulders.
Background: a massive vertical binder page filling the entire backdrop,
arranged as a 3-by-4 grid of holographic foil trading card slots with rounded
corners and rainbow iridescent borders. Each occupied slot frames a different
athlete portrait: a Japanese baseball player in Dodgers home white pinstripes
mid-swing, a Japanese pitcher in the same uniform mid wind-up, a tall
African-American basketball player in Lakers purple and gold mid-dunk, a young
European footballer in Chelsea royal blue celebrating, a WNBA player in Sparks
purple and yellow shooting, a Formula 1 helmet in Cadillac black white and red
livery. One or two slots left intentionally empty and dark, hinting at unfinished
collection.
Lighting: warm key light on the businessman, cool holographic glow from the
card wall behind, shallow depth of field with the man in sharp focus and the
card grid softly luminous.
Color palette: deep navy and charcoal, accented by holographic rainbow shimmer
and Dodgers royal blue.
Mood: quiet power, "I caught them all".
Aspect ratio 3:4 vertical. No text, no captions, no letters, no numbers, no
logos, no watermark, no jersey numbers, no team wordmarks, no extra crowd
faces, no blurry main character, single central subject dominant.
```

---

## Version B — JoJo 奇妙冒险 / 漫画分镜风

**梗**：沃尔特摆 JoJo 经典 pose，背后浮出他的「替身」——一群运动员从光影里冒出来；漫画网点 + 「ゴゴゴ」氛围线（注意：氛围线不是字，是斜向集中线）。

**画面定位**
- 沃尔特微微侧身，下巴轻抬，一只手插裤袋一只手食指轻推眼镜，jojo 式戏剧性 pose
- 镜头略仰，强透视
- 背后多个球员从黑色烟雾 / 能量中半透明显现，重叠成一面「随从墙」
- 黑白漫画底 + 局部彩色高光（道奇蓝、湖人紫金、切尔西蓝）作为破墨

**Prompt**
```
Vertical 3:4 black-and-white manga illustration with selective spot color,
Hirohiko Araki JoJo's Bizarre Adventure influence, dramatic shonen pose.
Foreground: an older American businessman in a sharp charcoal three-piece
suit, thin rectangular glasses, short grey hair, calm intense expression,
slightly tilted chin, one hand pushing his glasses up with the index finger,
the other hand in his trouser pocket, dramatic three-quarter pose, low-angle
hero perspective, exaggerated strong shoulders.
Background: half-transparent ghostly figures of athletes rising out of dark
ink smoke and energy, stacked behind him like summoned stands. A Japanese
baseball player in Dodgers home pinstripes mid-swing, a tall basketball
player in Lakers purple and gold mid-dunk, a footballer in Chelsea royal blue
celebrating, a Formula 1 driver in a Cadillac helmet. The figures overlap and
fade into thick brush ink and screentone dots.
Style: high-contrast manga linework, halftone screentone shading, bold ink
brush strokes, dramatic radial speed lines pointing toward the central man,
selective spot color only on Dodgers royal blue, Lakers purple-gold, and
Chelsea blue accents, everything else black, white, and grey.
Mood: menacing, regal, "his stand has many faces".
Aspect ratio 3:4 vertical. No text, no captions, no letters, no Japanese
characters, no onomatopoeia text, no logos, no watermark, no jersey numbers,
no team wordmarks, single central subject dominant.
```

---

## Version C — 文艺复兴油画 / 君王登基

**梗**：把沃尔特画成巴洛克风格的「体育之王」，坐在用奖杯堆出的王座上，球星像宫廷随从一样列在两侧。这一版最适合「洛杉矶体育之王」这条副标。

**画面定位**
- 沃尔特正坐居中，王座由世界大赛奖杯 + NBA Larry O'Brien 杯 + 英超奖杯 + F1 Constructors 杯堆成
- 两侧站着 / 半跪着 4–5 名运动员，姿态像中世纪宫廷画
- 顶部斜射光（伦勃朗光）从画面左上打下，沃尔特脸亮，外侧人物半隐于暗
- 背景是模糊的体育场穹顶 + 厚重红色帷幔

**Prompt**
```
Vertical 3:4 baroque oil painting in the style of a Renaissance coronation
portrait, Caravaggio chiaroscuro lighting, museum quality.
Center: an older American businessman in a contemporary charcoal suit and thin
glasses, sitting upright on an imposing throne assembled from polished
championship trophies — a baseball World Series trophy, a basketball larger-
than-life golden trophy, a soccer trophy, and a Formula 1 constructors trophy
visibly fused into the throne structure. The man wears a faint knowing smile,
calm, regal, hands resting on the armrests, the absolute focal point.
Around him: four to five athletes arranged like courtiers in a royal painting,
two on each side, slightly behind and lower than the throne. A Japanese
baseball player in Dodgers home pinstripe whites, a tall basketball player in
Lakers purple and gold robes, a footballer in Chelsea royal blue, a WNBA
player in Sparks purple and yellow, a Formula 1 driver holding a Cadillac
black and red helmet under his arm. They stand in reverent half-bowed poses,
faces partially in shadow.
Background: heavy crimson velvet drapery, faint cathedral-like stadium dome
arches behind, dust motes catching the light.
Lighting: dramatic Rembrandt key light from upper left, deep shadows on
right, golden warm tones, sacred atmosphere.
Color palette: deep crimson, gold, charcoal, with accent colors from each
athlete's uniform.
Mood: "the king of Los Angeles sports", quiet absolute power.
Aspect ratio 3:4 vertical. No text, no captions, no letters, no numbers, no
logos, no watermark, no jersey numbers, no team wordmarks, no halos, single
central subject dominant.
```

---

## Version D — 漫威 / 电影海报式合成

**梗**：好莱坞大片海报的合成构图。沃尔特正面胸像占下半，背景是巨型立体拼贴的运动员剪影 + 城市天际线 + F1 赛车飞过。最「眼熟」、最点击友好。

**画面定位**
- 沃尔特正面胸像在画面下 1/3，目光直视镜头，双臂自然下垂或抱在胸前
- 中段：洛杉矶城市天际线（Crypto.com Arena 穹顶 + Dodger Stadium 灯柱）
- 上段：背景被切成 4–5 个梯形 / 斜切色块，每块塞一个动作中的球星 + 一辆 Cadillac F1 赛车横切而过
- 整体调色蓝金，电影海报式 vignette

**Prompt**
```
Vertical 3:4 hyper-cinematic Hollywood blockbuster movie poster composition,
multi-layer photo composite, Marvel/Christopher Nolan style key art.
Bottom third: an older American businessman in a charcoal suit and thin
glasses, photographed from chest up, looking directly into the camera with a
calm confident expression, faint smile, arms relaxed, sharply lit from above,
he is the anchor of the entire composition.
Middle band: a stylized Los Angeles skyline silhouette at golden hour, the
domed roof of a basketball arena and the light towers of a baseball stadium
visible, warm haze.
Upper two-thirds: a dramatic collage of athletes arranged in angled
trapezoidal segments behind and above the man — a Japanese baseball player in
Dodgers home pinstripes mid-swing, a tall basketball player in Lakers purple
and gold mid-dunk, a footballer in Chelsea royal blue celebrating, a WNBA
player in Sparks purple and yellow shooting, and a Formula 1 car in Cadillac
black white and red livery streaking diagonally across the upper edge with
motion blur.
Lighting: cinematic teal-and-orange grade, strong vignette, lens flare in the
upper right, god rays falling on the central businessman.
Color palette: deep navy, gold, with accent colors from each team.
Mood: epic, "one man, one empire".
Aspect ratio 3:4 vertical. No text, no captions, no letters, no numbers, no
logos, no watermark, no jersey numbers, no team wordmarks, no actor billing
block, single central subject dominant.
```

---

## 选稿提示 / 看图时的判断点

- **A 卡册页**：信息密度最高，最适合「12 个联赛」这条主线；风险是 AI 容易把卡片画歪
- **B JoJo**：风格反差最大，最容易在 XHS 信息流里被截停；风险是 AI 可能把人物画太年轻或脸不像金融人
- **C 油画王座**：和「洛杉矶体育之王」副标最契合，氛围最高级；风险是太严肃，不一定适合 XHS 调性
- **D 电影海报**：最稳、点击率最可预测；风险是缺梗、和其他财经号封面撞型

建议先各跑一张，挑 1 主 + 1 备；最终封面文字（标题）仍用 `overlay_cover_text.py` 后期叠，**生图阶段一律不写字**。

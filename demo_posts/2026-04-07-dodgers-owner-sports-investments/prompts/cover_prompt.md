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

## Version B — JoJo 奇妙冒险 / 石之海彩色漫画分镜风

**梗**：沃尔特摆 JoJo 经典 pose，背后浮出他名下的「替身」——一众真实球员从光影里冒出；参考 JoJo 第六部《石之海》（David Production 动画版）的饱和对比色、强烈光感和厚重线稿。和 F 版（真人电影）拉开：这版仍是**彩色漫画 / 动画质感**，不是真人摄影。

**本轮变更**
- 球员形象要**尽量贴近真实球员本人的识别度**：大谷翔平、LeBron James、Palmer / Enzo 级的切尔西欧洲面孔、Cadillac F1 车手等
- 颜色风格从原本「黑白 + 局部彩色」升级为**全彩《石之海》调色**：高饱和蓝紫 / 青绿 / 品红主色，强烈对比，热带监狱式厚光
- 仍保留 JoJo 戏剧性 pose 和厚重描线

**画面定位**
- 沃尔特微微侧身居中，下巴轻抬，一只手插裤袋，一只手食指轻推眼镜，低角度仰拍
- 背后浮出 4–5 名真实球员的 JoJo 化半身像，每人一个经典扭身 pose，排成弧形
- 《石之海》式彩色能量烟雾包围，替身光环用品红 / 青绿 / 柠檬黄打底
- 线稿厚重、阴影硬边、色块饱满，画风是动画而非真人

**Prompt**
```
Vertical 3:4 full-color anime illustration, JoJo's Bizarre Adventure Stone
Ocean (Part 6) anime style by David Production, Hirohiko Araki color
aesthetic, bold ink outlines, high-contrast cel shading, saturated tropical
and neon palette, dramatic shonen pose.
Foreground center: an older American businessman in his early 60s in a
sharp charcoal three-piece suit, thin rectangular glasses, short combed
grey hair, calm intense expression, slightly tilted chin, one hand pushing
his glasses up with the index finger, the other hand in his trouser pocket,
dramatic three-quarter JoJo-style pose with hips twisted and shoulders
exaggerated, low-angle hero perspective, bold confident silhouette.
Background: four to five athlete figures drawn in the same JoJo anime
style, rising out of swirling colored energy smoke and stand aura, arranged
in a shallow arc behind and above him, each striking a dramatic JoJo pose.
The athletes should be clearly recognizable as the following real
professional athletes, rendered as faithful JoJo-style anime portraits with
their actual facial features, hairstyles, and builds:
- Shohei Ohtani in a Los Angeles Dodgers home white pinstripe uniform with
  a royal blue cap, mid-swing follow-through, bat held high
- LeBron James in a Los Angeles Lakers purple and gold jersey, mid-dunk
  with one arm raised, muscular frame, headband, recognizable beard
- Yoshinobu Yamamoto in the same Dodgers uniform, mid wind-up with leg
  lifted, Japanese pitcher
- a young European footballer resembling Cole Palmer in a Chelsea royal
  blue home kit, arms spread celebrating
- a Formula 1 driver in a Cadillac black and red racing suit holding a
  matching helmet
Treat the athletes as summoned stands: slightly translucent at the edges
where they fade into the colored smoke, but their faces and bodies rendered
in sharp JoJo anime linework with clear likeness to the real players.
Style: thick bold outlines, hard cel shading with two or three shadow
tones, sparkling highlights, dramatic radial energy lines pointing toward
the central businessman, Araki-style muscular anatomy, Stone Ocean
iconography of swirling ink and abstract motifs.
Color palette: hyper-saturated Stone Ocean tones — electric violet, neon
magenta, tropical teal, lemon yellow, deep cobalt blue, with hot pink and
orange rim lights, against pools of deep indigo shadow.
Lighting: multi-colored key lights from above and sides casting hard
cel-shaded shadows, glowing rim light on every figure, dramatic colored
god rays slicing the background.
Mood: "his stand has many faces", regal, menacing, operatic JoJo theatrics.
Aspect ratio 3:4 vertical. No text, no captions, no letters, no Japanese
characters, no onomatopoeia text, no logos, no watermark, no jersey
numbers, no team wordmarks, single central subject dominant, athletes must
remain secondary to the man in the suit.
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

## Version E — X-Men / 教授 X 沃尔特

**梗**：把沃尔特画成 Charles Xavier（X 教授），坐在悬浮椅 / 轮椅上戴着 Cerebro 头盔，整个 X-Men 战队就是他名下的球星。大谷 = 他的「万磁王级」王牌，LeBron = Colossus 钢人，切尔西球员 = 闪电身法的 Quicksilver，F1 头盔人 = 赛博感突变体。

**画面定位**
- 沃尔特居中，悬浮椅上正坐，微微前倾，一手搭扶手，一手轻抬至太阳穴做「读取心智」手势
- 戴一副简化版 Cerebro 头盔（金属半罩 + 发光电极，不要过度未来感）
- 身后弧形排列 4–5 名「突变体形态」的球星：道奇大谷握棒、湖人巨人夸张肌肉、切尔西身影被蓝色电光包裹、F1 头盔冒出能量
- 背景：X 战警会议室 / Cerebro 穹顶，墙面是发光的地球全息 + 浮动数据点（代表 12 个联赛坐标）

**Prompt**
```
Vertical 3:4 cinematic illustration, X-Men comic movie key art aesthetic,
Marvel Studios cinematic realism with a comic-book edge.
Center: a calm, composed older American businessman in a sharp charcoal
suit and thin rectangular glasses, short combed grey hair, faint knowing
smile, seated upright in a sleek high-tech hover chair, one hand resting on
the armrest, the other hand raised with two fingers lightly touching his
temple in a mind-reading gesture. He wears a simplified minimal Cerebro-style
metallic half-helmet with soft glowing blue electrodes along the sides,
understated and elegant, not bulky. He is the unmistakable focal point, sharp
and well-lit.
Around him: four to five athlete figures arranged in a shallow arc behind
and slightly above the chair, each rendered like a distinct X-Men team
member with their own power aura. A Japanese baseball player in Dodgers home
white pinstripes mid-swing with faint motion trails, a towering muscular
African-American basketball player in Lakers purple and gold mid-dunk with
metallic skin highlights like a powerhouse, a young European footballer in
Chelsea royal blue surrounded by crackling electric blue energy, a WNBA
player in Sparks purple and yellow shooting with kinetic glow, a Formula 1
driver in a Cadillac black and red helmet emitting thin red energy lines.
The athletes are slightly desaturated and smaller than the central man,
framed like loyal team members.
Background: a circular high-tech command chamber, dark chrome walls with
softly glowing blue circuitry, a massive translucent holographic globe
floating behind the man, scattered floating data points marking major cities,
atmospheric volumetric light rays.
Lighting: cool blue rim light from the Cerebro helmet, warm key light on
the businessman's face, dramatic cinematic contrast, subtle lens flare.
Color palette: deep charcoal, cool electric blue, accent warmth on the
central face, team colors visible on each athlete.
Mood: "the professor who commands them all", calm godlike control.
Aspect ratio 3:4 vertical. No text, no captions, no letters, no numbers, no
logos, no watermark, no jersey numbers, no team wordmarks, no crowd, single
central subject dominant.
```

---

## Version F — JoJo 真人电影版 / live-action JoJo cinematic

**梗**：参考 2017 三池崇史《JoJo 的奇妙冒险：钻石不灭》真人电影 —— 真人演员 + 超饱和电影调色 + 舞台剧式夸张 pose + 超现实光感。和 B 版（黑白漫画）拉开：这版是彩色、真人质感、更多角色、更像电影海报。

**画面定位**
- 沃尔特站在画面正中偏前，JoJo 式站姿：髋部一扭、下巴一抬、一手插袋一手轻推眼镜
- 背后密集排列 6–7 名球星，每人一个 JoJo 经典 pose（反手指天、扭腰回眸、交叉双臂、单膝）
- 光是一束束彩色「纸灯笼」风格的强光从上方斜射，暗影厚、饱和度拉满
- 镜头略仰，强透视，所有人脸都朝观众

**Prompt**
```
Vertical 3:4 hyper-saturated cinematic live-action film still, inspired by
Takashi Miike's live-action JoJo's Bizarre Adventure Diamond Is Unbreakable,
theatrical bizarre poses, photoreal actors with surreal lighting and
exaggerated color grade.
Foreground center: an older American businessman in a sharp charcoal
three-piece suit, thin rectangular glasses, short grey hair, calm intense
expression, striking a dramatic JoJo-style pose — hips twisted, chin lifted,
one hand in his trouser pocket, the other hand slowly pushing his glasses up
with the index finger, shoulders strong and angular, three-quarter body shot.
Behind him, six to seven athletes arranged in a tight dramatic group, each
frozen in their own exaggerated JoJo-style theatrical pose, all facing the
camera: a Japanese baseball player in Dodgers home white pinstripes with bat
raised over his head, a Japanese pitcher in the same Dodgers uniform with
arms crossed, a tall African-American basketball player in Lakers purple and
gold flexing with one arm pointing skyward, a European footballer in Chelsea
royal blue kneeling on one knee with head turned back over shoulder, a WNBA
player in Sparks purple and yellow balancing on the balls of her feet arms
spread wide, a Formula 1 driver in a Cadillac black and red racing suit
holding his helmet under one arm with the other hand on his hip, all frozen
like a bizarre stage ensemble.
Lighting: harsh theatrical colored spotlights from above, hard shadows,
beams of magenta, cyan and gold cutting across the scene like stained glass,
deep contrast, glossy skin highlights, Miike-style surreal realism.
Color palette: over-saturated magenta, cyan, gold, royal blue, Lakers
purple, Chelsea blue, deep black shadows.
Background: abstract dark stage with blurred neon geometry, faint Italianate
architectural arches, cinematic smoke.
Mood: "his bizarre stand has many faces", theatrical, operatic, loud.
Aspect ratio 3:4 vertical. No text, no captions, no letters, no Japanese
characters, no onomatopoeia, no logos, no watermark, no jersey numbers,
no team wordmarks, single central subject dominant.
```

---

## Version G — Q 版人偶 / 实况野球 Power Pros 风

**梗**：所有球员都变成 Konami《实况野球》Power Pros 那种 2 头身、大头、圆点眼、无嘴或一字嘴的 Q 版人偶；沃尔特也跟着 Q 化，站在陈列柜 / 桌面玩具场景正中，像个收藏家把一整套公仔摆好。最可爱、信息量也最密。

**画面定位**
- 沃尔特 Q 版 2 头身，西装眼镜灰发保留识别特征，双手叉腰或一手轻抚下巴
- 他脚边和身后是一圈 Q 版球员人偶：道奇大谷挥棒、山本投球、湖人巨人扣篮、切尔西小人踢球、F1 小车、Sparks 女篮投篮
- 全部站在一个木质 / 亚克力展示台上，背景是模糊的玩具架子 + 柔和暖光
- 整体色调明亮、糖果色、微型摄影质感（tilt-shift）

**Prompt**
```
Vertical 3:4 adorable chibi super-deformed toy diorama illustration,
Konami Jikkyou Powerful Pro Baseball "Power Pros" mascot aesthetic,
two-heads-tall proportions, big round heads, tiny bodies, simple dot eyes,
minimal mouths, soft vinyl toy shading, tilt-shift miniature photography
feel.
Center: a chibi version of an older American businessman, two-heads-tall,
oversized round head, short grey hair, thin rectangular glasses as a tiny
highlight, calm faint smile, tiny charcoal suit with white shirt and dark
tie, hands confidently on his hips, standing proudly in the middle of a
polished wooden display stage. He is the tallest and most centered figure,
the collector himself turned into a figurine.
Around him, arranged in a semicircle on the same display stage: a chibi
Japanese baseball player in Dodgers home white pinstripes and royal blue
cap mid-swing with a tiny bat, a chibi Japanese pitcher in the same Dodgers
uniform winding up with one leg lifted, a chibi tall basketball player in
Lakers purple and gold leaping for a mini dunk, a chibi European footballer
in Chelsea royal blue kicking a tiny soccer ball, a chibi WNBA player in
Sparks purple and yellow taking a jumpshot, and a tiny Cadillac Formula 1
race car in black white and red livery parked at the front of the stage.
All figures share the same two-heads-tall chibi proportions, vinyl-toy
finish, soft plastic sheen.
Background: a softly blurred toy shelf with out-of-focus shelves, warm
ambient lighting, faint tiny championship trophies in the bokeh, cozy
collector-room atmosphere.
Lighting: soft diffused key light from upper front, gentle rim light,
pastel warm tones, tilt-shift miniature feel, shallow depth of field.
Color palette: cream background, Dodgers royal blue, Lakers purple and
gold, Chelsea blue, Cadillac red, all softened to candy tones.
Mood: "he collected the whole set", wholesome, proud, miniature diorama.
Aspect ratio 3:4 vertical. No text, no captions, no letters, no numbers, no
logos, no watermark, no jersey numbers, no team wordmarks, single central
subject dominant, chibi style consistent across all figures.
```

---

## 选稿提示 / 看图时的判断点

- **A 卡册页**：信息密度最高，最适合「12 个联赛」这条主线；风险是 AI 容易把卡片画歪
- **B JoJo 黑白漫画**：风格反差最大，最容易在 XHS 信息流里被截停；风险是 AI 可能把人物画太年轻或脸不像金融人
- **C 油画王座**：和「洛杉矶体育之王」副标最契合，氛围最高级；风险是太严肃，不一定适合 XHS 调性
- **D 电影海报**：最稳、点击率最可预测；风险是缺梗、和其他财经号封面撞型
- **E X-Men / 教授 X**：「幕后主脑」叙事最贴；风险是 Cerebro 头盔 AI 容易画夸张、脸被遮住
- **F JoJo 真人电影版**：最有戏剧张力 + 最多球员；风险是 6–7 个角色 AI 容易糊脸或比例崩
- **G 实况野球 Q 版**：最可爱、和「收藏家」母题完美贴合；风险是 XHS 上可爱风会稀释「体育之王」的重量感

建议先各跑一张，挑 1 主 + 1 备；最终封面文字（标题）仍用 `overlay_cover_text.py` 后期叠，**生图阶段一律不写字**。

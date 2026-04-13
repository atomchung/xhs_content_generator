# 棒球小白系列 — 角色設計

日期：2026-04-13

## 角色概念

**名稱：** 小 Din（暫定）
**原型：** 奶白色糰子造型，頭頂棒球帽冒出小綠芽
**定位：** 棒球小白系列的固定講解員 / 主角

## 角色基準描述（Master Prompt）

以下為角色的完整描述，所有 prompt 以此為基準：

```text
A cute round cream-colored dumpling-shaped mascot with a small green sprout
poking out from the top of a deep red baseball cap, big round sparkling black
eyes with a white highlight dot, tiny dot nostrils, soft pink blush on both
cheeks, smooth egg-shaped body with no neck, tiny stubby arms and legs.
Soft plush toy texture with gentle gradient shading.
Wearing a deep crimson red baseball jersey with bold white letters "Din"
on the chest, white baseball pants, red round-toed cleats.
Standing upright facing the camera, arms slightly out.
Clean white studio background. Soft even lighting.
3D kawaii mascot style, Xiaohongshu mascot aesthetic.
```

## 角色規格拆解

### 身體

| 部位 | 描述 |
|------|------|
| 體型 | 圓潤蛋形 / 糰子形（dumpling-shaped, egg-shaped body） |
| 膚色 | 奶白色（cream-colored） |
| 質感 | 軟絨毛絨玩具感（soft plush toy texture），帶柔和漸層陰影 |
| 脖子 | 無（no neck），頭和身體一體 |
| 四肢 | 極短粗手腳（tiny stubby arms and legs） |

### 頭部 / 臉部

| 部位 | 描述 |
|------|------|
| 眼睛 | 大圓亮黑眼，帶白色高光點（big round sparkling black eyes with a white highlight dot） |
| 鼻子 | 兩個小點（tiny dot nostrils） |
| 臉頰 | 兩團柔粉色腮紅（soft pink blush on both cheeks） |
| 嘴巴 | 預設不畫，需要時可加小弧線 |

### 帽子 + 綠芽

| 部位 | 描述 |
|------|------|
| 帽子 | 深紅色棒球帽（deep red baseball cap） |
| 綠芽 | 帽頂冒出一小株綠色嫩芽（small green sprout poking out from the top） |

綠芽是角色的**視覺識別核心**，每個 prompt 都必須保留。

### 服裝

| 部位 | 描述 |
|------|------|
| 上衣 | 深紅色棒球球衣，胸前白色粗體字「Din」（deep crimson red baseball jersey with bold white letters "Din"） |
| 褲子 | 白色棒球褲（white baseball pants） |
| 鞋子 | 紅色圓頭球鞋（red round-toed cleats） |

### 風格

| 項目 | 描述 |
|------|------|
| 渲染風格 | 3D kawaii mascot style |
| 平台調性 | Xiaohongshu mascot aesthetic（小紅書吉祥物感） |
| 質感 | 柔和漸層陰影（gentle gradient shading），不是硬邊平塗 |
| 光線 | 柔和均勻光（soft even lighting） |
| 背景 | 預設乾淨白色（clean white studio background） |

## 表情變體

角色表情靠眼睛大小 + 嘴型 + 身體姿態控制：

| 表情 | 描述修改 |
|------|---------|
| 預設 | 不加嘴巴描述，靠大眼 + 腮紅自帶可愛感 |
| 好奇 | `curious expression, head tilted slightly, eyes looking at [object]` |
| 驚訝 | `surprised expression, small round open mouth, eyes widened` |
| 興奮 | `excited expression, big open smile, arms raised slightly` |
| 認真 | `focused determined expression, slight forward lean` |

## 影片 Prompt 用角色描述（簡化版）

完整 master prompt 太長時，可用以下簡化版（保留所有關鍵辨識特徵）：

```text
A cute round cream-colored dumpling-shaped mascot with a small green sprout
from the top of a deep red baseball cap, big sparkling black eyes with white
highlight, soft pink blush, smooth egg-shaped body, tiny stubby limbs.
Soft plush toy texture. Wearing a deep crimson baseball jersey with white
letters "Din", white pants, red cleats.
3D kawaii mascot style, Xiaohongshu mascot aesthetic.
```

## 道具規則

- 角色自帶服裝（球衣 + 球褲 + 球鞋 + 帽子），不需要額外穿搭
- 道具靠手持：棒球、球棒、手套
- 一個 prompt 最多加一個手持道具
- 綠芽永遠從帽頂冒出，不被道具遮擋

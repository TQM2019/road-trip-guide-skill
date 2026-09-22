---
name: ev-road-trip-guide
description: |
  Build a shareable China long-distance pure-EV road-trip guide (路书) with
  day-by-day itinerary, ~300km charging stops near highway exits, car-sleeping
  notes, real road-network map (OSRM + Leaflet), city food picks, weather ranges,
  and unique scenic photos. Use when the user says 路书 / 自驾攻略 / 行程地图 /
  trip map / road trip guide / 纯电自驾 / 睡车 / 充电路线, or asks to plan a
  multi-day EV self-drive with charging stops and scenic days. Do NOT use for
  flight-only city trips, hotel-only itineraries without driving, or generic
  blog writing.
---

# EV Road Trip Guide（纯电路书）

生成可部署、可手机打开的**单文件图文路书**：左侧固定日期条 + 真实路网地图 + 逐日行程（天气/美食融在点位里）+ 独立景点图。

## When to use

- 用户要「自驾路书 / 行程地图 / 纯电自驾攻略 / 车中泊行程」
- 明确：纯电车、长途、要充电点、要景点、可睡车
- 产出：网页路书（可本地预览，可再部署成链接）

## Hard constraints（先确认再排期）

1. **节奏**：去程灵活排期，留充电与顺路停留
2. **充电**：约每 **300km** 一个高速口快充节点；山区段（承德→阿尔山→根河）进山前 90%+  
3. **睡车**：夜间保暖按目的地夜温；内蒙/林区 0℃ 级睡袋  
4. **返程**：若有指定途经城市（如青岛），返程单独成段，写清「日期 + 出发城市」  
5. **日期年份**：以用户为准（例 2026.9.25–10.5），不要写错年

## Pipeline（按序执行）

### 1. 抽硬约束
日期、出发/回家、车型续航假设、是否睡车、核心游玩区、返程是否绕城、日均是否赶。

### 2. 排骨架
- 去程：灵活安排天数到核心区
- 核心：约 5 天秋景/草原/林区环线  
- 返程：按用户要求（如经青岛）3 天到家  
每行格式：**`D1 9.25 绍兴 → 蚌埠 ~620km · 顺路点`**（只写城市，不写「山姆/出发」）

### 3. 真实路网（禁止只画直线）
1. 为每天选途经城市坐标（lon,lat）  
2. 调 OSRM：  
   `https://router.project-osrm.org/route/v1/driving/{lon,lat};...?overview=full&geometries=geojson`  
3. 抽稀坐标（约 250–400 点）写入 `DAY_ROUTES`  
4. Leaflet 画线：白描边 + 亮橙 `#FF3B00` 主线  
5. 底图可用高德 style8 / OSM / CARTO，可切换

### 4. 充电点
按累计约 280 / 580 / 880… 选**高速口或县城**快充，命名为「①湖州/长兴」等。  
导航按钮传 **城市名**（`navCity(name)`），不要传长标题。

### 5. 点位文案（融进行程，不单独堆块）
每个 location：`desc` 行程说明 → 再跟 **天气一行** + **美食一行（可搜点评）**。  
不要：页顶大块美食区、不要城市天气 chips 与正文重复。

### 6. 天气
用 Open-Meteo（或用户给的数据）；每天保留**一行**当日天气即可。  
格式：`阿尔山 阴 1~10°C 保暖`。查不到就不写。

### 7. 配图（一景一图，禁止复用）
- 优先网络**真实景点照**；搜不到宁可**不配图**，禁止塞无关图  
- 每个 `img` 只用一次；打包单文件时 base64 内嵌  
- 禁止：珠宝/地图/明星/动物/海报等错图

### 8. UI（固定交互）
- **左侧竖条日期**：`总览/全程` + `D1/9.25`…`D11/10.5`，`position:fixed`，独立上下滑  
- 绿色底只贴按钮区并**渐隐**，禁止 D11 下大色块  
- 日期块约 42×42（接近 1:1），绿底约 56px 略宽于按钮  
- 选中：主字保持白色，小字琥珀金  
- 总览 6 信息卡 **2 列 × 3 行**，卡等宽  
- 地图可随页滚走；正文可左右滑切换日期  
- 导航用高德 scheme / 网页 URI

### 9. 交付
1. 先 **本地 present_files** 让用户预览（用户要求「先本地预览」时不要急着上传）  
2. 再打包 `index.html` 单文件部署（Netlify Drop / GitHub Pages / Gofile 等）  
3. 语法检查：抽出最长 `<script>` 做 `node --check`

## Output data shape

```js
const DAYS = [{ id, label, date, title, color, locations: [{
  name, lat, lng, type, time, desc, img?, budget?, detail?, gmap?, dianpingKeyword?
}] }];
const DAY_ROUTES = { "1": { ll: [[lat,lng],...], km, h } };
const FOOD_BY_DAY = { "1": [{ name, lat, lng, desc, dianpingKeyword, budget }] };
const DAY_WEATHER = { "1": "<div class=\"weather-bar\">...</div>" };
```

`type`: `food | spot | drink | hotel | transport`（充电用 `transport` 名含「⚡」）

## Examples

**User:** xx到xx纯电睡车，9.25–10.5，返程经青岛，10.5 到家  
**Agent:** 确认约束 → 11 日骨架（D1–D3 去程 / D4–D8 核心 / D9–D11 青岛返程）→ OSRM 逐日几何 → 充电①–⑩ → 逐点嵌天气美食 → 真实景点一景一图 → 左侧竖条 UI → 本地预览 → 可部署单文件。

## Troubleshooting

| 问题 | 处理 |
|------|------|
| 打开空白 | 多半 JS 语法坏；`node --check` 最长 script，修好再交付 |
| 日期条盖住内容 | 检查 z-index 与 `overflow-x:hidden` 祖先（会破坏 sticky） |
| 缩放绿条变窄 | 竖条/按钮用固定 px，不要百分比宽度 |
| 导航搜不到 | `navCity()` 只传城市 |
| 图错/复用 | 删除错图；一景一图；搜不到就去掉 img |
| 天气重复 | 只保留当日天气条，卡片内 `weatherForLoc` 返回 null |

## Progressive disclosure

- UI 细节与文案规范 → `references/ui-spec.md`  
- 充电/睡车/保暖 → `references/charging-car-sleep.md`  
- 选题与删减原则 → `references/itinerary-method.md`  
- 单文件打包 → `scripts/build_single_file.py`

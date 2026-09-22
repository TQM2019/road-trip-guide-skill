# UI 规范（路书网页）

## 布局

```
[左固定竖条 56px] [主列：地图（可滚走）+ 正文]
```

- `.day-rail`: `position:fixed; left:0; top:0; bottom:0; width:56px; height:100vh; overflow-y:auto`
- 背景只给 `.rail-inner`（按钮容器），高度 `fit-content`，底部 `linear-gradient` 渐隐到透明
- 禁止：`height:100%` 的绿底铺满竖条（D11 下会留大色块）
- `.tab`: 约 42×42，`border-radius:11px`，两行文字：主字 `D5` / 小字 `9.29`；总览为 `总览` / `全程`

## 选中态

- 主字（总览、D1…）**保持白色** `#FFF8EC`
- 小字（日期/全程）**琥珀金** `#E8B56A`
- 底：半透明高亮 `rgba(255,248,236,.22)` + 细描边，不用大面积反白

## 总览 6 卡

`grid-template-columns: 1fr 1fr`（2×3），卡片 `width:100%` 等宽。

推荐六格：

1. 去程 · `9.25` / `绍兴`  
2. 返程 · `10.3` / `满洲里`  
3. 出行方式 · 纯电自驾 / 睡车上  
4. 充电节奏 · 约每 300km / 高速口快充  
5. 核心游玩 · 内蒙草原 / 大兴安岭秋景  
6. 里程 / 到家 · 去约 2,900km / 返约 2,800km · 10.5 傍晚到家  

格式统一：**日期 + 出发城市**；文案只写城市（去「山姆」「出发」）。

## 逐日文案

```
D1 9.25 绍兴 → 蚌埠 ~620km · 太湖 / 长江 / 张公山
```

- 不要「返程经青岛」这类后缀（除非用户要求）  
- 每天天气只一行；美食写在对应点位下，不单独「美食推荐」大块

## 地图

- OSRM 折线：白 `#FFFFFF` 描边 + 主线 `#FF3B00`  
- 每天 `DAY_ROUTES[id].ll`；总览叠全部天  
- `position: relative`（随页滚走，不吸顶）  
- 导航按钮：`openAS(navCity(name), lat, lng, encodeURIComponent(navCity(name)))`

## 色彩（第一版秋日杂志）

| token | 值 |
|-------|-----|
| paper | `#F7F1E5` |
| ink | `#2A2622` |
| forest | `#1F3D2B` |
| amber | `#C47A2C` |
| maple | `#A63D2E` |
| card | `#FFFDF8` |

## 触控

- 日期块 `touch-action: manipulation`，最小约 42px  
- 竖条 `overscroll-behavior: contain`，独立滚动  
- 正文可横向滑切换日（阈值约 56px，避免与纵向滚冲突）

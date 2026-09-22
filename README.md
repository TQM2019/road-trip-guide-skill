# road-trip-guide-skill

Agent skill：把「纯电长途自驾 + 车中泊」做成可部署的图文路书，适用于全季节。

适用于 MiMo Desktop / Claude Code 等支持 `SKILL.md` 的 Agent。

## 安装

```bash
# 通用：放到 skills 目录
# MiMo Desktop 全局
cp -r road-trip-guide-skill ~/.config/mimocode/skills/

# Claude Code
cp -r road-trip-guide-skill ~/.claude/skills/
```

或：

```bash
npx skills add <your-github-user>/road-trip-guide-skill
```

## 能做什么

- 灵活排期：去程 / 核心 / 返程三段式
- 约每 300km 充电点（高速口/县城）  
- OSRM **真实驾车路网**绘图（非直线）  
- 逐点嵌天气、美食（可跳点评）  
- 景点独立真实配图（禁止复用、禁错图）  
- 左侧固定日期竖条 UI + 可部署单文件 HTML  

## 触发示例

- 「做个纯电路书」  
- 「xx到xx自驾攻略，睡车，充电」
- 「行程地图 / trip map / road trip guide」  

## 目录

```
road-trip-guide-skill/
├── SKILL.md
├── locales/
├── references/
│   ├── ui-spec.md
│   ├── charging-car-sleep.md
│   └── itinerary-method.md
└── scripts/
    └── build_single_file.py
```

## License

MIT

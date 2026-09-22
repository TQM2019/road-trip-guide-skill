# 自驾路书攻略 Skill / Road Trip Guide Skill

[![Agent Skill](https://img.shields.io/badge/Agent-Skill-blue)](https://github.com/TQM2019/road-trip-guide-skill)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Chinese](https://img.shields.io/badge/语言-中文+English-orange.svg)]()

把「纯电长途自驾 + 车中泊」做成**可部署的图文路书**，适用于**全季节**。

输入出发地和目的地，自动生成一份完整的自驾攻略网页：真实路网地图 + 逐日行程 + 充电点 + 天气 + 美食 + 景点配图。

适用于 **MiMo Desktop / Claude Code / Codex** 等支持 `SKILL.md` 的 Agent 平台。

---

## ✨ 功能特性

- 🗺️ **灵活排期**：去程 / 核心游玩 / 返程三段式，按需求调整节奏
- ⚡ **充电规划**：约每 300km 标注高速口或县城快充节点
- 🛣️ **真实路网**：基于 OSRM 驾车路线绘制，非直线连接
- 🌤️ **天气融合**：逐日嵌天气信息，提前准备衣物
- 🍜 **美食推荐**：沿途城市美食，可对接大众点评
- 📷 **景点配图**：一景一图，真实照片，禁止复用
- 📱 **移动端适配**：左侧固定日期竖条 UI，手机打开即可用
- 📦 **单文件输出**：打包成可部署的 `index.html`，随处分享

---

## 🚀 安装

### 方式一：npx（推荐）

```bash
npx skills add TQM2019/road-trip-guide-skill
```

### 方式二：手动安装

```bash
# MiMo Desktop
cp -r road-trip-guide-skill ~/.config/mimocode/skills/

# Claude Code
cp -r road-trip-guide-skill ~/.claude/skills/

# Codex
cp -r road-trip-guide-skill ~/.codex/skills/
```

### 方式三：Git Clone

```bash
git clone https://github.com/TQM2019/road-trip-guide-skill.git
```

---

## 💡 使用示例

### 基础用法

> **「绍兴到海拉尔自驾攻略，睡车，充电」**

Agent 将自动生成：
- D1–D3 去程（日均 600–950km，不赶路）
- D4–D8 核心游玩（秋景/草原/林区环线）
- D9–D11 返程

### 进阶用法

> **「成都到拉萨自驾，GL8 混动，想睡酒店，10 天，要美食重点」**

> **「北京到三亚，纯电 SUV，不赶，要赶海 + 环岛，春节出发」**

> **「上海出发，去新疆独库公路，纯油车，只规划核心段 5 天」**

### 触发关键词

| 中文 | English |
|------|---------|
| 自驾路书 | road trip guide |
| 行程地图 | trip map |
| 纯电自驾 | EV road trip |
| 车中泊 / 睡车 | car sleeping |
| 充电路线 | charging route |
| 自驾攻略 | self-drive guide |

---

## 📁 项目结构

```
road-trip-guide-skill/
├── SKILL.md                  # Agent 技能主文件
├── locales/                  # 多语言支持
│   ├── en-US.json
│   └── zh-CN.json
├── references/               # 参考文档
│   ├── ui-spec.md            # UI 设计规范
│   ├── charging-car-sleep.md # 充电/睡车/保暖指南
│   └── itinerary-method.md   # 选题与删减原则
└── scripts/
    └── build_single_file.py  # 单文件打包工具
```

---

## 📋 输出数据

每个行程包含以下结构化数据：

| 字段 | 说明 |
|------|------|
| `DAYS` | 每日行程（点位、时间、描述、图片） |
| `DAY_ROUTES` | OSRM 真实路网坐标 |
| `FOOD_BY_DAY` | 每日美食推荐 |
| `DAY_WEATHER` | 当日天气 |

---

## 🤝 贡献

欢迎提交 Issue 或 PR！

1. Fork 本仓库
2. 创建分支 `git checkout -b feature/xxx`
3. 提交更改 `git commit -m 'Add xxx'`
4. 推送分支 `git push origin feature/xxx`
5. 提交 Pull Request

---

## 📄 License

[MIT](https://opensource.org/licenses/MIT)
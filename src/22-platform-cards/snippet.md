# 平台模拟卡片 — 实现思路

自定义 SVG 模板仿平台 UI：

- **Netflix 风格**：黑底红字「TOP 10 项目」海报行
- **Steam 风格**：游戏卡式仓库展示（名称/语言/星数/更新）
- **Letterboxd 风格**：圆点评分
- **Duolingo 风格**：连续打卡天数（喂 streak 数据）

```markdown
![Netflix Card](./assets/netflix-card.svg)
```

模板见本目录 `templates/`，改文字后 push，Actions 重渲染。

# 宠物进度卡 — 实现思路

「电子宠物随贡献进化」（9 阶段）：

1. Actions 读取 GitHub API 年度贡献数
2. 按阈值切 9 档（<50 蛋 / <200 幼体 / … / >5000 神兽）
3. 用对应 SVG 素材渲染「宠物 + 等级进度条 + 进化条件」卡片
4. README 嵌入生成图

```python
level = min(9, contributions // 500 + 1)
svg = render_pet(level, nickname="雪绒", progress=contributions % 500)
```

参考：`github-profile-pet`。

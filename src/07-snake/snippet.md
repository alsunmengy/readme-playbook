# 贡献贪吃蛇 — 代码片段

用 `Platane/snk`（GitHub Actions 自动生成）：

```yaml
# .github/workflows/snake.yml
name: Generate Snake
on:
  schedule: [{cron: '0 */6 * * *'}]
  workflow_dispatch:
  push: {branches: [main]}
jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: Platane/snk/svg-only@v3
        with:
          github_user_name: alsunmengy
          outputs: |
            dist/snake.svg
            dist/github-snake-dark.svg?palette=github-dark
      - uses: crazy-max/ghaction-github-pages@v3
        with:
          target_branch: output
          build_dir: dist
```

README 嵌入：
```markdown
![Snake animation](https://raw.githubusercontent.com/alsunmengy/alsunmengy/output/github-snake.svg)
```

> 暗色模式适配：用 `<picture>` 标签按主题切换两张 SVG。

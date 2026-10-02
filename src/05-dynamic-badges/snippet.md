# 动态徽章 — 代码片段

## shields.io 静态徽章（版本号/许可证）
```markdown
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
```

## 真正动态（Actions 定时更新数据）
```yaml
# .github/workflows/dynamic-badge.yml
name: Update badge data
on:
  schedule: [{cron: '0 */6 * * *'}]
  workflow_dispatch:
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          LINES=$(find . -name '*.py' | xargs wc -l | tail -1 | awk '{print $1}')
          echo "{\"schemaVersion\": 1, \"label\": \"lines of code\", \"message\": \"$LINES\", \"color\": \"blue\"}" > badge.json
```
badge.json 部署到 Pages 后，shields.io 端点即可渲染。

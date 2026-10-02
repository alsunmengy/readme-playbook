# 个人简介摘要卡 — 代码片段

用 `profile-summary-cards`（GitHub Actions 生成多张卡）：

```yaml
# .github/workflows/profile-summary.yml
name: Profile Summary
on:
  schedule: [{cron: '0 0 * * *'}]
  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: vn7n24fzkq/profile-summary-cards@release
        with:
          USERNAME: alsunmengy
```

生成后嵌入：
```markdown
![Profile Summary](https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=alsunmengy&theme=radical)
![Stats](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=alsunmengy&theme=radical)
```

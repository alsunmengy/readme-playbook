# 综合信息图 — 代码片段

用 `lowlighter/metrics`（30+ 插件 300+ 选项）：

```yaml
# .github/workflows/metrics.yml
name: Metrics
on:
  schedule: [{cron: '0 0 * * *'}]
  workflow_dispatch:
jobs:
  metrics:
    runs-on: ubuntu-latest
    steps:
      - uses: lowlighter/metrics@latest
        with:
          token: ${{ secrets.METRICS_TOKEN }}
          user: alsunmengy
          template: classic
          config_display: large
          plugin_isocalendar: yes
          plugin_languages: yes
          plugin_music: yes
          plugin_wakatime: yes
          output_action: commit
```

支持集成 Spotify、WakaTime、isocalendar 等。

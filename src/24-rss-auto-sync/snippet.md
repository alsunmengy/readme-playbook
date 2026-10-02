# 内容自动同步 — 代码片段

通用 RSS → README（覆盖博客/YouTube/StackOverflow）：

```yaml
name: RSS Sync
on:
  schedule: [{cron: '0 */4 * * *'}]
  workflow_dispatch:
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: gautamkrishnar/blog-post-workflow@v1
        with:
          feed_list: "https://blog.example.com/rss.xml,https://youtube.com/feeds/videos.xml?channel_id=UC...,https://stackoverflow.com/feeds/user/..."
          max_post_count: 6
```

README 标记块：
```markdown
<!-- RECENT-CONTENT:START -->
<!-- RECENT-CONTENT:END -->
```

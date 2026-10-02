# 博客文章自动同步 — 代码片段

用 `gautamkrishnar/blog-post-workflow`：

```yaml
# .github/workflows/blog-post.yml
name: Latest Blog Post
on:
  schedule: [{cron: '0 * * * *'}]
  workflow_dispatch:
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: gautamkrishnar/blog-post-workflow@v1
        with:
          feed_list: "https://your-blog.com/rss.xml"
          max_post_count: 5
          template: "[$$title]($$url)"
```

README 里放标记，Actions 自动填充：
```markdown
<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->
```

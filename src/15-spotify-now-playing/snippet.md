# Spotify 正在播放 — 代码片段

用 `novatorem`（Vercel 一键部署）：

1. Fork https://github.com/novatorem/novatorem
2. Spotify Developer Dashboard 建应用拿 Client ID/Secret
3. Vercel 配置环境变量后部署
4. README 嵌入：

```markdown
[![Spotify](https://novatorem.vercel.app/api/spotify)](https://open.spotify.com/user/your-id)
```

带均衡器动效：`spotify-github-profile`（同样 Vercel + Spotify OAuth）。

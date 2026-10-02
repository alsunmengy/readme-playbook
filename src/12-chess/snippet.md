# 交互式国际象棋 — 实现思路

README 不能跑 JS，「交互」靠 **Issue/PR 事件驱动**：

1. 部署轻量 Web 服务（或 GitHub Pages + Cloudflare Workers）托管棋盘页面
2. README 嵌入棋盘的 **SVG 快照图** + 「走棋」链接按钮
3. 访客点链接到 Issue 评论走法（如 `e2e4`）
4. GitHub Actions 监听 Issue 评论，用 python-chess 校验并更新棋盘 SVG
5. README 图片自动刷新，双方异步对战

本目录附 `board-render.py`：用 python-chess 生成当前局面 SVG。

# AI 参与徽章 — 代码片段

## 静态声明徽章
```markdown
![AI Badge](https://img.shields.io/badge/AI%20Assisted-Specs%20✓%20Code%20✓%20Review%20✓-7B61FF)
```

## Vibe Coding 占比（git 历史分析）
```bash
git log --pretty='%an <%ae>' | sort | uniq -c | sort -rn
```

Actions 跑分析脚本生成徽章 JSON，shields.io 端点渲染「AI 提交占比 42%」。

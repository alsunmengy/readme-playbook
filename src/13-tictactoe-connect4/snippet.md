# 井字棋 / 四子棋 — 实现思路

与国际象棋同构，状态机更简单：

1. 用 GitHub Issue 的**第 N 条评论**代表第 N 手
2. Actions 校验合法性后渲染棋盘 PNG/SVG 提交回仓库
3. README 引用该图片，访客刷新即见最新棋局

```python
# board.py 核心逻辑示例
def apply_move(board, move, player):
    if board[move] != ' ':
        raise ValueError('cell occupied')
    board[move] = player
    return board
```

四子棋增加重力下落与斜向胜负判定即可。

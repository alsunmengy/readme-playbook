#!/usr/bin/env python3
"""互动游戏走子处理器（由 issue_comment 事件触发）。
评论格式：井字棋 `!move <1-9>`，国际象棋 `!move <e2e4>`。
非法走法只回帖提示，绝不报错退出（避免失败通知邮件）。
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import *
REPO_ROOT = os.path.join(HERE, "..", "..")
GAMES = os.path.join(REPO_ROOT, "games")
DEMOS = os.path.join(REPO_ROOT, "assets", "demos")

BODY = os.environ.get("BODY", "")
USER = os.environ.get("USER", "访客")
ISSUE_TITLE = os.environ.get("ISSUE_TITLE", "")
ISSUE_NUMBER = os.environ.get("ISSUE_NUMBER", "0")

def comment(msg):
    try:
        subprocess.run(["gh", "issue", "comment", ISSUE_NUMBER, "--body", msg],
                       capture_output=True, text=True, timeout=30)
    except Exception:
        pass

def save_state(name, state):
    json.dump(state, open(os.path.join(GAMES, name), "w"), ensure_ascii=False, indent=2)

# ============ 井字棋 ============
def tictactoe_move(pos):
    p = os.path.join(GAMES, "tictactoe-state.json")
    st = json.load(open(p))
    board = st["board"]
    if not (1 <= pos <= 9):
        comment(f"@{USER} 走法无效：请评论 `!move 1` 到 `!move 9`（对应格子从左上到右下）。")
        return
    if board[pos - 1] != " ":
        comment(f"@{USER} 这个格子已经有子啦，换一个位置试试～")
        return
    board[pos - 1] = st["turn"]
    winner = check_winner(board)
    st["turn"] = "O" if st["turn"] == "X" else "X"
    st["history"].append({"user": USER, "move": pos})
    if winner:
        comment(f"🎉 **{USER}（{winner}）获胜！** 评论 `!move reset` 开新一局。")
        st["board"] = [" "] * 9
        st["turn"] = "X"
    elif all(c != " " for c in board):
        comment(f"🤝 平局！评论 `!move reset` 开新一局。")
        st["board"] = [" "] * 9
        st["turn"] = "X"
    else:
        comment(f"@{USER} 落子成功（{board[pos-1]} → 格 {pos}），现在轮到 {st['turn']}。")
    save_state("tictactoe-state.json", st)
    render_tictactoe(st)

def check_winner(b):
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a, x, y in lines:
        if b[a] != " " and b[a] == b[x] == b[y]:
            return b[a]
    return None

def render_tictactoe(st):
    board = st["board"]
    defs = (linear_gradient("bg", [(0, "#161b22"), (1, "#0d1117")]) +
            linear_gradient("acc", [(0, "#FF6FD8"), (1, "#7B61FF")]))
    out = svg_open(420, 470, defs) + rect(0, 0, 420, 470, "url(#bg)", rx=16)
    out += text(24, 38, "⭕ 井字棋 · 对战中", 17, "#e6edf3", weight="700")
    out += text(24, 60, "在对战帖评论 !move 1-9 落子", 11, "#8b949e")
    x0, y0, cell = 115, 105, 78
    for i in range(3):
        for j in range(3):
            x, y = x0 + j * cell, y0 + i * cell
            out += rect(x, y, cell - 8, cell - 8, "#21262d", rx=10, extra='stroke="#30363d" stroke-width="1.5"')
            v = board[i * 3 + j]
            out += text(x + (cell-8)/2, y + 8, str(i*3+j+1), 10, "#484f58", anchor="middle")
            if v.strip():
                color = "#FF6FD8" if v == "X" else "#58a6ff"
                out += text(x + (cell-8)/2, y + (cell-8)*0.72, v, 40, color, anchor="middle", weight="800")
    out += text(210, 420, f"轮到 {st['turn']} · 由 GitHub Actions 自动裁决", 12, "#8b949e", anchor="middle")
    out += "</svg>"
    open(os.path.join(DEMOS, "tictactoe-live.svg"), "w").write(out)

# ============ 国际象棋 ============
def chess_move(move):
    p = os.path.join(GAMES, "chess-state.json")
    st = json.load(open(p))
    if not re.fullmatch(r"[a-h][1-8][a-h][1-8]", move):
        comment(f"@{USER} 走法格式应为 `!move e2e4` 这样的坐标（起始格+目标格）。")
        return
    try:
        import chess
        board = chess.Board(st["fen"])
        mv = chess.Move.from_uci(move)
        if mv not in board.legal_moves:
            comment(f"@{USER} `{move}` 不是合法走法，当前回合：{'白' if board.turn else '黑'}方。")
            return
        board.push(mv)
        st["fen"] = board.fen()
        st["history"].append({"user": USER, "move": move})
        save_state("chess-state.json", st)
        import chess.svg
        svg = chess.svg.board(board, size=420)
        open(os.path.join(DEMOS, "chess-live.svg"), "w").write(svg)
        comment(f"@{USER} 走子成功 `{move}`。轮到{'黑' if board.turn else '白'}方。")
    except ImportError:
        comment(f"@{USER} 走法 `{move}` 已记录，但服务器缺 python-chess 暂无法裁决（管理员配置中）。")
    except Exception as e:
        comment(f"@{USER} 处理失败：{e}")

if __name__ == "__main__":
    m = re.search(r"!move\s+(\S+)", BODY)
    if not m:
        sys.exit(0)
    arg = m.group(1).lower()
    if "井字棋" in ISSUE_TITLE or "tictactoe" in ISSUE_TITLE.lower():
        if arg == "reset":
            save_state("tictactoe-state.json", {"board": [" "] * 9, "turn": "X", "issue": ISSUE_NUMBER, "history": []})
            comment("🔄 新一局开始！轮到 X。")
        else:
            tictactoe_move(int(arg) if arg.isdigit() else 0)
    elif "象棋" in ISSUE_TITLE or "chess" in ISSUE_TITLE.lower():
        chess_move(arg)
    else:
        comment("这个 Issue 不是对战帖哦，去 README 里点对应的游戏对战帖～")
    print("走子处理完成")

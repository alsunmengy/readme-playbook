#!/usr/bin/env python3
"""玩法 07 本地实现：贡献贪吃蛇。SMIL 动画 SVG，蛇沿贡献图蛇形前进，吃过的格子点亮。
完全本地生成，不依赖任何第三方在线服务或 action。
用法: python3 gen_snake.py alsunmengy assets/snake.svg
"""
import json, subprocess, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

QUERY = """query($login:String!){ user(login:$login){
  contributionsCollection{ contributionCalendar{
    weeks{ contributionDays{ date contributionCount } } } } } }"""

COLS, ROWS = 26, 7
CELL, PAD = 18, 12
W, H = PAD*2 + COLS*CELL, PAD*2 + ROWS*CELL + 60
DIM = ["#161b22", "#1c2530", "#243040", "#2c3a4d", "#34455a"]
LIT = ["#216e39", "#0e4429", "#006d32", "#26a641", "#39d353"]

def fetch(user):
    out = subprocess.run(["gh", "api", "graphql", "-f", f"login={user}", "-f", f"query={QUERY}"],
                         capture_output=True, text=True, check=True)
    cal = json.loads(out.stdout)["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    return [w["contributionDays"] for w in cal["weeks"]][-COLS:]

def snake_path():
    """蛇形遍历路径：蛇头从左上角出发，S 形走完所有格子"""
    pts = []
    for col in range(COLS):
        rows = range(ROWS) if col % 2 == 0 else reversed(range(ROWS))
        for row in rows:
            pts.append((PAD + col*CELL + CELL/2, PAD + row*CELL + CELL/2 + 60))
    return pts

def render(weeks):
    pts = snake_path()
    path_d = "M " + " L ".join(f"{x:.0f},{y:.0f}" for x, y in pts)
    total_dur = 24  # 蛇全程走完的秒数
    step = total_dur / len(pts)

    defs = linear_gradient("bg", [(0, "#161b22"), (1, "#0d1117")]) + \
           linear_gradient("snake", [(0, "#FF6FD8"), (1, "#7B61FF")]) + \
           f'<path id="track" d="{path_d}"/>'
    o = svg_open(W, H, defs) + rect(0, 0, W, H, "url(#bg)", rx=16)
    o += text(PAD, 30, "🐍 贡献贪吃蛇 —— 小蛇正在吃掉我的贡献图", 15, "#e6edf3", weight="700")

    # 贡献格子：被蛇吃过的格子从暗变亮
    flat = [d for w in weeks for d in w]  # weeks 已是「周→天列表」
    idx = 0
    for col in range(COLS):
        rows = range(ROWS) if col % 2 == 0 else reversed(range(ROWS))
        for row in rows:
            if idx >= len(pts):
                break
            cnt = flat[idx]["contributionCount"] if idx < len(flat) else 0
            lv = min(4, cnt // 3) if cnt else 0
            x, y = PAD + col*CELL, PAD + row*CELL + 60
            lit_t = idx * step
            o += (f'<rect x="{x}" y="{y}" width="{CELL-3}" height="{CELL-3}" rx="3" fill="{DIM[lv]}">'
                  f'<animate attributeName="fill" to="{LIT[lv]}" dur="0.3s" begin="{lit_t:.2f}s" fill="freeze"/></rect>')
            idx += 1

    # 蛇：头 + 4 节身子，沿 track 路径跑（时间偏移制造蛇身跟随）
    segs = [("head", "#FF6FD8", 11, 0), ("body1", "#e05fc0", 9.5, 0.18), ("body2", "#b163e0", 8.5, 0.36),
            ("body3", "#8b63f0", 7.5, 0.54), ("tail", "#7B61FF", 6.5, 0.72)]
    for name, color, r, lag in segs:
        begin = f"{-lag*total_dur:.2f}s" if lag > 0 else "0s"
        o += (f'<circle r="{r}" fill="{color}">'
              f'<animateMotion dur="{total_dur}s" repeatCount="indefinite" begin="{begin}" '
              f'rotate="auto"><mpath href="#track"/></animateMotion></circle>')

    # 蛇眼睛（跟着头）
    for dx in (-3.5, 3.5):
        o += (f'<circle r="2" fill="#0d1117">'
              f'<animateMotion dur="{total_dur}s" repeatCount="indefinite" '
              f'keyPoints="0;1" keyTimes="0;1" calcMode="linear">'
              f'<mpath href="#track"/></animateMotion></circle>')

    # 循环说明
    o += text(W/2, H - 14, "数据来源：GitHub 贡献日历 · 每日 12:00 自动重生成", 11, "#484f58", anchor="middle")
    o += "</svg>"
    return o

if __name__ == "__main__":
    user = sys.argv[1] if len(sys.argv) > 1 else "alsunmengy"
    weeks = fetch(user)
    out = sys.argv[2] if len(sys.argv) > 2 else "snake.svg"
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w").write(render(weeks))
    print("贪吃蛇 SVG 生成完成")

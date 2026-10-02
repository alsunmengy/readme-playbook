#!/usr/bin/env python3
"""玩法 08 本地实现：3D 等距贡献图。公共实例已下线，自己画等距柱状图！
用法: python3 gen_3d.py alsunmengy assets/contrib-3d.svg
"""
import json, subprocess, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

QUERY = """query($login:String!){ user(login:$login){
  contributionsCollection{ contributionCalendar{
    weeks{ contributionDays{ date contributionCount } } } } } }"""

LEVEL_COLORS = ["#21262d", "#0e4429", "#006d32", "#26a641", "#39d353"]

def fetch(user):
    out = subprocess.run(["gh", "api", "graphql", "-f", f"login={user}", "-f", f"query={QUERY}"],
                         capture_output=True, text=True, check=True)
    cal = json.loads(out.stdout)["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    return [w["contributionDays"] for w in cal["weeks"]][-24:]  # 最近 24 周

def level(c):
    return min(4, c // 3)

def iso_cube(x, y, h, color):
    s = 8; lift = 3.2
    dz = h * lift
    top = f"{x},{y-dz-s/2} {x+s},{y-dz} {x},{y-dz+s/2} {x-s},{y-dz}"
    left = f"{x-s},{y-dz} {x},{y-dz+s/2} {x},{y+s/2} {x-s},{y}"
    right = f"{x+s},{y-dz} {x},{y-dz+s/2} {x},{y+s/2} {x+s},{y}"
    dark = "#0d1117"
    o = f'<polygon points="{left}" fill="{color}" stroke="{dark}" stroke-width="0.6"/>'
    o += f'<polygon points="{right}" fill="{color}" stroke="{dark}" stroke-width="0.6" opacity="0.8"/>'
    o += f'<polygon points="{top}" fill="{color}" stroke="{dark}" stroke-width="0.6" opacity="0.95"/>'
    return o

def render(weeks):
    W, H = 860, 420
    defs = linear_gradient("sky", [(0, "#161b22"), (1, "#0d1117")]) + \
           linear_gradient("title", [(0, "#FF6FD8"), (1, "#7B61FF")])
    o = svg_open(W, H, defs) + rect(0, 0, W, H, "url(#sky)", rx=16)
    o += text(30, 42, "3D 贡献城市", 22, "#FF6FD8", weight="800")
    o += text(30, 66, "每个方块 = 一天 · 高度 = 当日贡献强度 · 最近 24 周", 12, "#8b949e")
    ox, oy = 430, 320
    cells = []
    for wi, week in enumerate(weeks):
        for di, day in enumerate(week):
            x = ox + (wi - di) * 8
            y = oy + (wi + di) * 4.2
            cells.append((x, y, day["contributionCount"]))
    cells.sort(key=lambda c: c[0] + c[1] * 2)  # 画家算法：远的先画
    for x, y, cnt in cells:
        lv = level(cnt)
        h = lv if lv > 0 else 0.35
        o += iso_cube(x, y, h, LEVEL_COLORS[lv])
    o += "</svg>"
    return o

if __name__ == "__main__":
    user = sys.argv[1] if len(sys.argv) > 1 else "alsunmengy"
    weeks = fetch(user)
    out = sys.argv[2] if len(sys.argv) > 2 else "contrib-3d.svg"
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w").write(render(weeks))
    print("3D 贡献城市 SVG 生成完成")

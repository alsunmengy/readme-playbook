#!/usr/bin/env python3
"""玩法 11 本地实现：奖杯陈列柜。公共实例会挂（402/404），自己画才稳！
用法: python3 gen_trophy.py alsunmengy assets/trophy.svg
"""
import json, subprocess, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

TROPHIES = [
    ("总星标",   "stars",     [(500,"SSS"),(250,"SS"),(100,"S"),(50,"A"),(20,"B"),(5,"C")]),
    ("粉丝数",   "followers", [(500,"SSS"),(200,"SS"),(100,"S"),(50,"A"),(10,"B"),(1,"C")]),
    ("公开仓库", "repos",     [(100,"SSS"),(60,"SS"),(40,"S"),(25,"A"),(15,"B"),(5,"C")]),
    ("连续贡献", "streak",    [(200,"SSS"),(100,"SS"),(50,"S"),(20,"A"),(10,"B"),(3,"C")]),
]

RANK_COLORS = {"SSS":"#FFD700","SS":"#FFA500","S":"#FF6FD8","A":"#7B61FF","B":"#58A6FF","C":"#8b949e"}

def gh(path):
    return json.loads(subprocess.run(["gh", "api", path], capture_output=True, text=True, check=True).stdout)

def fetch(user):
    u = gh(f"users/{user}")
    repos = gh(f"users/{user}/repos?per_page=100")
    stars = sum(r["stargazers_count"] for r in repos if not r["fork"])
    return {"stars": stars, "followers": u["followers"], "repos": u["public_repos"], "streak": 0}

def rank_of(val, table):
    for th, rk in table:
        if val >= th:
            return rk
    return "-"

def card(i, name, val, rk):
    w, h = 152, 190
    x, y = 10 + i * 162, 10
    c = RANK_COLORS.get(rk, "#8b949e")
    glow = 'filter="url(#glow)"' if rk in ("SSS", "SS") else ""
    o = rect(x, y, w, h, "#161b22", rx=14, extra=f'stroke="{c}" stroke-width="1.5" stroke-opacity="0.5"')
    o += f'<text x="{x+w/2}" y="{y+44}" font-size="34" text-anchor="middle" {glow}>🏆</text>'
    o += text(x + w/2, y + 78, name, 12, "#8b949e", anchor="middle")
    o += text(x + w/2, y + 122, rk, 34, c, anchor="middle", weight="800", extra=glow)
    o += text(x + w/2, y + 152, fmt_num(val), 15, "#e6edf3", anchor="middle", weight="700")
    return o

def board(d):
    n = len(TROPHIES)
    W, H = 20 + n * 162, 210
    defs = (linear_gradient("bg", [(0, "#161b22"), (1, "#0d1117")]) +
            '<filter id="glow"><feGaussianBlur stdDeviation="2.5" result="b"/>'
            '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    o = svg_open(W, H, defs) + rect(0, 0, W, H, "url(#bg)", rx=16)
    o += text(18, 30, "🏆 奖杯陈列柜", 14, "#e6edf3", weight="700")
    for i, (name, key, table) in enumerate(TROPHIES):
        o += card(i, name, d[key], rank_of(d[key], table))
    o += "</svg>"
    return o

if __name__ == "__main__":
    user = sys.argv[1] if len(sys.argv) > 1 else "alsunmengy"
    d = fetch(user)
    out = sys.argv[2] if len(sys.argv) > 2 else "trophy.svg"
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w").write(board(d))
    print("奖杯陈列柜 SVG 生成完成")

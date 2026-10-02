#!/usr/bin/env python3
"""玩法 02 本地实现：连续贡献天数卡片，GraphQL 拉日历自绘 SVG。
用法: python3 gen_streak.py alsunmengy assets/streak.svg
"""
import json, subprocess, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

QUERY = """query($login:String!){ user(login:$login){
  contributionsCollection{ contributionCalendar{
    weeks{ contributionDays{ date contributionCount } } } } } }"""

def fetch(user):
    out = subprocess.run(
        ["gh", "api", "graphql", "-f", f"login={user}", "-f", f"query={QUERY}"],
        capture_output=True, text=True, check=True)
    cal = json.loads(out.stdout)["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    return [d for w in cal["weeks"] for d in w["contributionDays"]]

def streak(days):
    streak_now = 0
    for d in reversed(days):
        if d["contributionCount"] > 0:
            streak_now += 1
        else:
            if streak_now == 0 and d["date"] == days[-1]["date"]:
                continue  # 今天还没提交不算断
            break
    best = run = 0
    for d in days:
        run = run + 1 if d["contributionCount"] > 0 else 0
        best = max(best, run)
    total = sum(d["contributionCount"] for d in days)
    return streak_now, best, total

def card(days):
    s_now, s_best, total = streak(days)
    W, H = 480, 175
    defs = (linear_gradient("bg", [(0, "#161b22"), (1, "#0d1117")]) +
            linear_gradient("fire", [(0, "#FF6FD8"), (1, "#FF9A3D")]))
    o = svg_open(W, H, defs) + rect(0, 0, W, H, "url(#bg)", rx=16)
    o += text(W/2, 40, "🔥 连续贡献日历", 16, "#e6edf3", anchor="middle", weight="700")
    cols = [("当前连续", f"{s_now} 天", "#FF6FD8"),
            ("历史最长", f"{s_best} 天", "#7B61FF"),
            ("年度总贡献", str(total), "#FF9A3D")]
    for i, (label, val, c) in enumerate(cols):
        x = 80 + i * 160
        o += text(x, 95, val, 22, c, anchor="middle", weight="700")
        o += text(x, 120, label, 12, "#8b949e", anchor="middle")
    o += text(W/2, 152, "保持热爱，持续输出", 12, "#8b949e", anchor="middle")
    o += "</svg>"
    return o

if __name__ == "__main__":
    user = sys.argv[1] if len(sys.argv) > 1 else "alsunmengy"
    days = fetch(user)
    os.makedirs(os.path.dirname(os.path.abspath(sys.argv[2])), exist_ok=True)
    open(sys.argv[2] if len(sys.argv) > 2 else "streak.svg", "w").write(card(days))
    print("连续贡献卡片 SVG 生成完成")

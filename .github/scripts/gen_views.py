#!/usr/bin/env python3
"""玩法 03 本地实现：访客计数徽章。数据源是 GitHub 自家 traffic API（绝对稳定）。
用法: python3 gen_views.py alsunmengy/readme-playbook assets/views.svg
"""
import json, subprocess, sys, os, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "star-history", "views-data.json")

def fetch(repo):
    out = subprocess.run(["gh", "api", f"repos/{repo}/traffic/views?per_page=100"],
                         capture_output=True, text=True, check=True)
    views = json.loads(out.stdout)["views"]
    return sum(v["count"] for v in views), sum(v["uniques"] for v in views)

def badge(total, uniq):
    W, H = 320, 76
    defs = linear_gradient("bg", [(0, "#161b22"), (1, "#0d1117")]) + \
           linear_gradient("acc", [(0, "#FF6FD8"), (1, "#7B61FF")])
    o = svg_open(W, H, defs) + rect(0, 0, W, H, "url(#bg)", rx=14)
    o += '<circle cx="34" cy="38" r="14" fill="url(#acc)"/>'
    o += text(62, 33, "页面访问量", 13, "#8b949e")
    o += text(62, 58, f"{fmt_num(total)} 人次（独立访客 {fmt_num(uniq)}）", 16, "#e6edf3", weight="700")
    o += "</svg>"
    return o

if __name__ == "__main__":
    repo = sys.argv[1] if len(sys.argv) > 1 else "alsunmengy/readme-playbook"
    try:
        total, uniq = fetch(repo)
    except Exception as e:
        print("traffic API 暂不可用，沿用历史数据:", e)
        d = json.load(open(DATA)) if os.path.exists(DATA) else {"total": 0, "unique": 0}
        total, uniq = d["total"], d["unique"]
    os.makedirs(os.path.dirname(os.path.abspath(DATA)), exist_ok=True)
    json.dump({"total": total, "unique": uniq, "date": str(datetime.date.today())}, open(DATA, "w"))
    out = sys.argv[2] if len(sys.argv) > 2 else "views.svg"
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w").write(badge(total, uniq))
    print(f"访客徽章 SVG 生成完成：累计 {total} 人次 / 独立访客 {uniq}")

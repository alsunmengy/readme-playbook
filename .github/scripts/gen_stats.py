#!/usr/bin/env python3
"""玩法 01/06 本地实现：GitHub 统计卡片 + 语言分布，纯自绘 SVG，零外部依赖。
用法: python3 gen_stats.py alsunmengy assets/stats.svg assets/langs.svg
"""
import json, subprocess, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

def gh(path):
    out = subprocess.run(["gh", "api", path], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)

def fetch(user):
    u = gh(f"users/{user}")
    repos = gh(f"users/{user}/repos?per_page=100&sort=updated")
    total_stars = sum(r["stargazers_count"] for r in repos if not r["fork"])
    langs = {}
    for r in repos:
        if r["fork"] or not r["language"]:
            continue
        langs[r["language"]] = langs.get(r["language"], 0) + 1
    return {
        "followers": u["followers"], "following": u["following"],
        "public_repos": u["public_repos"], "stars": total_stars,
        "name": u.get("name") or user,
        "langs": sorted(langs.items(), key=lambda x: -x[1])[:6],
    }

LANG_COLORS = {"Python":"#3572A5","JavaScript":"#f1e05a","TypeScript":"#3178c6","C":"#555555",
    "C++":"#f34b7d","C#":"#178600","HTML":"#e34c26","CSS":"#563d7c","Shell":"#89e051",
    "Dockerfile":"#384d54","Vue":"#41b883","Rust":"#dea584","Go":"#00ADD8","Lua":"#000080",
    "Kotlin":"#A97BFF","Java":"#b07219","PHP":"#4F5D95","Ruby":"#701516","Swift":"#F05138",
    "PLpgSQL":"#dad8d8","SCSS":"#c6538c","HCL":"#844FBA","Batchfile":"#C1F12E","PowerShell":"#012456",
    "Nix":"#7EBAE4","Astro":"#ff5a03","MDX":"#fcb32c","Kicad":"#314cb0","ShellCheck":"#cecfcb"}

def color(lang):
    return LANG_COLORS.get(lang, "#8b949e")

def stats_card(d):
    W, H = 480, 200
    defs = (linear_gradient("bg", [(0, "#161b22"), (1, "#0d1117")]) +
            linear_gradient("acc", [(0, "#FF6FD8"), (1, "#7B61FF")]))
    o = svg_open(W, H, defs) + rect(0, 0, W, H, "url(#bg)", rx=16)
    o += rect(0, 0, 6, H, "url(#acc)", rx=3)
    o += text(28, 42, d["name"] + " 的 GitHub 数据总览", 17, "#e6edf3", weight="700")
    items = [("获得星标", d["stars"]), ("粉丝", d["followers"]),
             ("公开仓库", d["public_repos"]), ("关注中", d["following"]), ("入站至今", "持续")]
    for i, (label, val) in enumerate(items):
        x = 28 + (i % 3) * 150
        y = 90 + (i // 3) * 62
        o += text(x, y, str(val), 24, "#FF6FD8", weight="700")
        o += text(x, y + 22, label, 12, "#8b949e")
    o += "</svg>"
    return o

def langs_card(d):
    W, H = 300, 200
    defs = linear_gradient("bg", [(0, "#161b22"), (1, "#0d1117")])
    o = svg_open(W, H, defs) + rect(0, 0, W, H, "url(#bg)", rx=16)
    o += text(24, 38, "常用语言分布", 15, "#e6edf3", weight="700")
    total = sum(c for _, c in d["langs"]) or 1
    x0, y0, w, h = 24, 58, W - 48, 14
    cx = x0
    for lang, cnt in d["langs"]:
        seg = w * cnt / total
        o += rect(cx, y0, seg, h, color(lang), rx=4)
        cx += seg
    for i, (lang, cnt) in enumerate(d["langs"]):
        x = 24 + (i % 2) * 140
        y = 110 + (i // 2) * 30
        o += f'<circle cx="{x+6}" cy="{y-5}" r="6" fill="{color(lang)}"/>'
        o += text(x + 18, y, f"{lang} {cnt*100//total}%", 13, "#c9d1d9")
    o += "</svg>"
    return o

if __name__ == "__main__":
    user = sys.argv[1] if len(sys.argv) > 1 else "alsunmengy"
    d = fetch(user)
    os.makedirs(os.path.dirname(os.path.abspath(sys.argv[2])), exist_ok=True)
    open(sys.argv[2] if len(sys.argv) > 2 else "stats.svg", "w").write(stats_card(d))
    open(sys.argv[3] if len(sys.argv) > 3 else "langs.svg", "w").write(langs_card(d))
    print("统计卡片 + 语言分布 SVG 生成完成")

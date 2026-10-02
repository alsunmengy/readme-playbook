#!/usr/bin/env python3
"""刷新 .github/badges/ 里 star 横幅和关注我的数字（PCB 同款，本地 SVG）。
用法: python3 refresh_badges.py alsunmengy/readme-playbook
"""
import json, os, re, subprocess, sys

BASE = os.path.join(os.path.dirname(__file__), "..")

def gh(path):
    return json.loads(subprocess.run(["gh", "api", path], capture_output=True, text=True, check=True).stdout)

def fmt(n):
    return ("%.1fk" % (n / 1000)).replace(".0k", "k") if n >= 1000 else str(n)

def rewrite(path, pattern, repl):
    p = os.path.join(BASE, path)
    c = open(p).read()
    c2 = re.sub(pattern, repl, c)
    if c2 != c:
        open(p, "w").write(c2)
        print(f"updated {path}")
    else:
        print(f"no change {path}")

if __name__ == "__main__":
    repo = sys.argv[1] if len(sys.argv) > 1 else "alsunmengy/readme-playbook"
    user = repo.split("/")[0]
    stars = gh(f"repos/{repo}")["stargazers_count"]
    followers = gh(f"users/{user}")["followers"]
    rewrite("badges/star-banner.svg", r"★ [0-9.,km]+", "★ " + fmt(stars))
    rewrite("badges/follow-me.svg", r"[0-9.,km]+ 人关注", fmt(followers) + " 人关注")

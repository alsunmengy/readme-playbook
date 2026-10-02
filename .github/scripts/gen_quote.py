#!/usr/bin/env python3
"""玩法 20 本地实现：每日语录卡片。按日期轮换（一天一条），本地语录库零依赖。
用法: python3 gen_quote.py assets/quote.svg
"""
import sys, os, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

QUOTES = [
    ("Talk is cheap. Show me the code.", "Linus Torvalds"),
    ("程序必须写给人看，顺带让机器执行。", "Harold Abelson"),
    ("过早优化是万恶之源。", "Donald Knuth"),
    ("代码胜于雄辩，但注释让代码活得更久。", "程序员的日常"),
    ("先解决问题，再写代码。", "John Johnson"),
    ("能跑的丑陋方案，胜过完美的不存在方案。", "黑客谚语"),
    ("调试比写代码难两倍，所以尽量写简单代码。", "Brian Kernighan"),
    ("Stay hungry, stay foolish.", "Steve Jobs"),
    ("简单是效率的灵魂。", "Shawn Austin"),
    ("每一次提交，都是给未来的自己写信。", "珂莱塔"),
    ("热爱可抵岁月漫长，代码可解世间无聊。", "爱弥斯"),
]

def render():
    q, author = QUOTES[datetime.date.today().toordinal() % len(QUOTES)]
    W, H = 560, 110
    defs = (linear_gradient("bg", [(0, "#161b22"), (1, "#0d1117")]) +
            linear_gradient("acc", [(0, "#FF6FD8"), (1, "#7B61FF")]))
    o = svg_open(W, H, defs) + rect(0, 0, W, H, "url(#bg)", rx=14)
    o += rect(0, 0, 5, H, "url(#acc)", rx=2.5)
    o += text(30, 42, "“ " + q + " ”", 15, "#e6edf3", weight="600")
    o += text(30, 76, "—— " + author, 13, "#8b949e")
    o += text(W - 24, 88, "每日一句", 10, "#484f58", anchor="end")
    o += "</svg>"
    return o

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "quote.svg"
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w").write(render())
    print("每日语录 SVG 生成完成")

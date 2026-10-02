#!/usr/bin/env python3
"""玩法 09 本地实现：动态终端模拟器。SMIL 动画 SVG，GitHub 原生渲染，零外部依赖。
用法: python3 gen_typing.py assets/terminal.svg
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

LINES = [
    ("$ whoami", "alsun梦游 · 服务器运维 & 创作者"),
    ("$ cat skills.txt", "Python / Docker / NAS / 硬件折腾"),
    ("$ echo hello", "你好，README！🐱"),
]

def render():
    W, H = 520, 168
    defs = linear_gradient("bg", [(0, "#1a1f29"), (1, "#0d1117")])
    o = svg_open(W, H, defs) + rect(0, 0, W, H, "url(#bg)", rx=14)
    o += rect(0, 0, W, 34, "#21262d", rx=14) + rect(0, 20, W, 14, "#21262d")
    for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        o += f'<circle cx="{22 + i*22}" cy="17" r="6" fill="{c}"/>'
    o += text(W/2, 22, "alsun梦游@github: ~", 12, "#8b949e", anchor="middle", font=MONO)
    y = 66
    for i, (cmd, out) in enumerate(LINES):
        o += text(24, y, cmd, 15, "#39d353", font=MONO,
                  extra=f'opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.01s" begin="{i*2.6}s" fill="freeze"/>')
        o += f'<text x="24" y="{y+24}" font-family="{FONT}" font-size="14" fill="#58a6ff" opacity="0">'
        o += f'<animate attributeName="opacity" from="0" to="1" dur="0.01s" begin="{i*2.6+1.1}s" fill="freeze"/>{esc(out)}</text>'
        y += 52
    o += rect(24, 146, 9, 18, "#39d353", rx=2,
              extra='opacity="0"><animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite" begin="7s"')
    o += "</svg>"
    return o

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "terminal.svg"
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w").write(render())
    print("终端动画 SVG 生成完成")

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

def animated_text(x, y, t, size, fill, font, begin, fade_dur="0.01s"):
    """带淡入动画的 text（规范写法，不用 extra 塞属性）"""
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{fill}" opacity="0">'
            f'<animate attributeName="opacity" from="0" to="1" dur="{fade_dur}" begin="{begin}" fill="freeze"/>'
            f'{esc(t)}</text>')

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
        o += animated_text(24, y, cmd, 15, "#39d353", MONO, f"{i*2.6}s")
        o += animated_text(24, y + 24, out, 14, "#58a6ff", FONT, f"{i*2.6+1.1}s")
        y += 52
    # 光标闪烁（结尾生效）
    o += (f'<rect x="24" y="146" width="9" height="18" rx="2" fill="#39d353" opacity="0">'
          f'<animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite" begin="7s"/>'
          f'</rect>')
    o += "</svg>"
    return o

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "terminal.svg"
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w").write(render())
    print("终端动画 SVG 生成完成")

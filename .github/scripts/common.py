"""公共 SVG 辅助：圆角矩形、文字、渐变 —— 全部脚本共用"""
from xml.sax.saxutils import escape

FONT = "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
MONO = "'JetBrains Mono','Fira Code',monospace"

def esc(t):
    return escape(str(t))

def rect(x, y, w, h, fill, rx=12, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>'

def text(x, y, t, size=14, fill="#ffffff", anchor="start", font=FONT, weight="400", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}" {extra}>{esc(t)}</text>')

def linear_gradient(gid, stops, x1="0", y1="0", x2="1", y2="1"):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<linearGradient id="{gid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{s}</linearGradient>'

def svg_open(w, h, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}"><defs>{defs}</defs>')

def fmt_num(n):
    return f"{n/1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)

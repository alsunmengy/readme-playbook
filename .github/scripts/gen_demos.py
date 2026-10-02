#!/usr/bin/env python3
"""批量生成各玩法演示图（全部本地绘制，确定性输出）：
04 WakaTime / 12 国际象棋 / 13 井字棋 / 15 Spotify / 16 博客同步 /
21 宠物卡 / 22 平台卡片 / 23 AI 徽章 / 24 内容同步 / 25 综合信息图
用法: python3 gen_demos.py [输出目录]
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets", "demos")
os.makedirs(OUT, exist_ok=True)

def card_open(w, h, title, subtitle=""):
    defs = (linear_gradient("bg", [(0, "#161b22"), (1, "#0d1117")]) +
            linear_gradient("acc", [(0, "#FF6FD8"), (1, "#7B61FF")]))
    o = svg_open(w, h, defs) + rect(0, 0, w, h, "url(#bg)", rx=16)
    o += text(24, 38, title, 17, "#e6edf3", weight="700")
    if subtitle:
        o += text(24, 60, subtitle, 11, "#8b949e")
    return o

def save(name, content):
    open(os.path.join(OUT, name), "w").write(content)
    print(f"  {name} ✓")

# ============ 04 WakaTime 编程时长周报 ============
def wakatime():
    o = card_open(520, 240, "⏱️ 本周编程时长", "WakaTime 周报示意图 · 每周自动更新")
    days = [("周一", 3.2), ("周二", 5.1), ("周三", 2.8), ("周四", 6.4), ("周五", 4.5), ("周六", 7.2), ("周日", 1.9)]
    maxv = 7.2
    for i, (day, hrs) in enumerate(days):
        x = 36 + i * 68
        bh = int(hrs / maxv * 110)
        o += rect(x, 190 - bh, 38, bh, "url(#acc)", rx=6)
        o += text(x + 19, 210, day, 11, "#8b949e", anchor="middle")
        o += text(x + 19, 182 - bh, f"{hrs}h", 10, "#c9d1d9", anchor="middle")
    o += text(24, 230, "总计 31.1 小时 · 主力语言 Python", 11, "#FF6FD8")
    return o + "</svg>"

# ============ 12 国际象棋棋盘 ============
def chess():
    o = card_open(480, 520, "♟️ 国际象棋 · 对战示意图", "访客在 Issue 评论走法（如 !move e2e4）即可下棋")
    board = [
        list("♜♞♝♛♚♝♞♜"), list("♟♟♟♟♟♟♟♟"),
        list("        "), list("        "), list("        "), list("        "),
        list("♙♙♙♙♙♙♙♙"), list("♖♘♗♕♔♗♘♖"),
    ]
    x0, y0, cell = 88, 100, 38
    for r in range(8):
        for c in range(8):
            x, y = x0 + c * cell, y0 + r * cell
            light = (r + c) % 2 == 0
            o += rect(x, y, cell, cell, "#f0d9b5" if light else "#b58863", rx=2)
            piece = board[r][c]
            if piece.strip():
                o += text(x + cell/2, y + cell*0.72, piece, 26, "#1a1a1a" if piece.isascii() or ord(piece) < 0x265F else "#111", anchor="middle")
    o += text(240, 480, "轮到白方 · 在对战帖评论即可落子", 12, "#8b949e", anchor="middle")
    return o + "</svg>"

# ============ 13 井字棋 ============
def tictactoe():
    o = card_open(420, 460, "⭕ 井字棋 · 对战示意图", "访客在 Issue 评论 !move 5 落子")
    x0, y0, cell = 115, 105, 78
    board = ["X", " ", "O", " ", "X", " ", " ", "O", " "]
    for i in range(3):
        for j in range(3):
            x, y = x0 + j * cell, y0 + i * cell
            o += rect(x, y, cell - 8, cell - 8, "#21262d", rx=10, extra='stroke="#30363d" stroke-width="1.5"')
            v = board[i * 3 + j]
            if v.strip():
                color = "#FF6FD8" if v == "X" else "#58a6ff"
                o += text(x + (cell - 8)/2, y + (cell - 8)*0.72, v, 40, color, anchor="middle", weight="800")
    o += text(210, 410, "当前轮到 O · 评论 !move <1-9> 落子", 12, "#8b949e", anchor="middle")
    return o + "</svg>"

# ============ 15 Spotify 正在播放 ============
def spotify():
    o = card_open(480, 160, "🎵 正在播放", "Spotify 联动 · 实时同步当前歌曲")
    o += rect(24, 74, 62, 62, "url(#acc)", rx=10)
    o += text(55, 114, "♪", 30, "#ffffff", anchor="middle")
    o += text(104, 100, "当前歌曲名称", 16, "#e6edf3", weight="700")
    o += text(104, 124, "歌手名 · 专辑名", 12, "#8b949e")
    # 均衡器动效（SMIL）
    for i, h in enumerate([14, 22, 10, 26, 18]):
        x = 380 + i * 16
        o += (f'<rect x="{x}" y="{112 - h}" width="8" height="{h}" rx="3" fill="#1DB954">'
              f'<animate attributeName="height" values="{h};{h*1.6};{h}" dur="{0.8 + i*0.2}s" repeatCount="indefinite"/>'
              f'<animate attributeName="y" values="{112-h};{112-h*1.6};{112-h}" dur="{0.8 + i*0.2}s" repeatCount="indefinite"/></rect>')
    return o + "</svg>"

# ============ 16 博客自动同步 ============
def blog():
    o = card_open(520, 220, "📝 最新博文", "RSS 自动同步 · 每天 12:00 更新列表")
    posts = [("用 GitHub Actions 搭建免费的自动化工作流", "10-01"),
             ("NAS 折腾手记：万兆网络改造全记录", "09-28"),
             ("从零开始写一个 README 生成器", "09-25")]
    for i, (t, d) in enumerate(posts):
        y = 86 + i * 44
        o += rect(24, y - 22, 472, 36, "#21262d", rx=8)
        o += text(40, y, "• " + t, 13, "#58a6ff")
        o += text(480, y, d, 11, "#8b949e", anchor="end")
    o += text(24, 210, "由 blog-post-workflow 自动填入标记区块", 11, "#484f58")
    return o + "</svg>"

# ============ 21 宠物进度卡 ============
def pet():
    o = card_open(560, 210, "🐾 电子宠物 · 贡献养成", "宠物随贡献数进化，共 9 个阶段")
    stages = ["蛋", "幼", "少", "青", "壮", "究", "极", "神", "绒"]
    icons = ["🥚", "🐣", "🐥", "🐱", "🐈", "🐈‍⬛", "🦁", "🐉", "✨"]
    cur = 3  # 当前阶段
    for i, (s, ic) in enumerate(zip(stages, icons)):
        x = 36 + i * 58
        active = i <= cur
        o += rect(x, 84, 46, 46, "url(#acc)" if active else "#21262d", rx=10)
        o += text(x + 23, 117, ic, 22, "#fff", anchor="middle")
        o += text(x + 23, 150, s, 11, "#FF6FD8" if active else "#484f58", anchor="middle", weight="700")
    o += text(36, 185, f"当前形态：青（第 {cur+1} 阶段）· 距下一阶段还需 120 贡献", 12, "#c9d1d9")
    return o + "</svg>"

# ============ 22 平台模拟卡片（Netflix + Steam） ============
def platform():
    o = card_open(560, 250, "🎬 平台风格卡片 · Netflix / Steam", "SVG 模板仿平台 UI")
    # Netflix 风格
    o += rect(24, 74, 250, 150, "#141414", rx=10, extra='stroke="#e50914" stroke-width="1.5"')
    o += text(40, 104, "N  本周热门 TOP 3", 15, "#e50914", weight="800")
    for i, t in enumerate(["readme-playbook", "Carlotta-PCB-Art", "LuoTianyi-PCB-Art"]):
        o += text(40, 136 + i * 28, f"{i+1}. {t}", 12, "#ffffff")
    # Steam 风格
    o += rect(290, 74, 250, 150, "#1b2838", rx=10, extra='stroke="#66c0f4" stroke-width="1.5"')
    o += text(306, 104, "🎮 我的仓库库", 15, "#66c0f4", weight="800")
    for i, (t, h) in enumerate([("readme-playbook", "31.2h"), ("hermes-tool-hongtou", "12.5h"), ("WeKite", "8.8h")]):
        o += text(306, 136 + i * 28, f"{t}  ·  {h}", 12, "#c7d5e0")
    return o + "</svg>"

# ============ 23 AI 参与徽章 ============
def ai_badge():
    o = card_open(520, 170, "🤖 AI 参与声明卡", "透明标注项目中的 AI 参与程度")
    items = [("规格设计", 90), ("代码编写", 75), ("代码审查", 60), ("文档维护", 85)]
    for i, (label, pct) in enumerate(items):
        y = 86 + i * 22
        o += text(24, y, label, 12, "#c9d1d9")
        o += rect(110, y - 11, 300, 12, "#21262d", rx=6)
        o += rect(110, y - 11, int(300 * pct / 100), 12, "url(#acc)", rx=6)
        o += text(490, y, f"{pct}%", 12, "#FF6FD8", anchor="end")
    return o + "</svg>"

# ============ 24 内容自动同步 ============
def rss():
    o = card_open(520, 200, "🔄 内容自动同步", "博客 / YouTube / StackOverflow → README")
    srcs = [("博客 RSS", "✅ 已同步 5 篇", "#58a6ff"), ("YouTube 频道", "✅ 已同步 3 条", "#FF0000"), ("StackOverflow", "✅ 已同步 2 条", "#F48024")]
    for i, (name, st, color) in enumerate(srcs):
        y = 88 + i * 38
        o += rect(24, y - 22, 472, 32, "#21262d", rx=8)
        o += rect(36, y - 15, 8, 8, color, rx=4)
        o += text(56, y, name, 13, "#e6edf3")
        o += text(480, y, st, 11, "#39d353", anchor="end")
    return o + "</svg>"

# ============ 25 综合信息图 ============
def metrics():
    o = card_open(560, 300, "📊 综合信息图（lowlighter/metrics）", "30+ 插件 · 300+ 选项 · 一张图全展示")
    # 左：isocalendar 热力图
    o += text(24, 84, "年度活跃日历", 12, "#8b949e")
    import random
    random.seed(7)
    for r in range(7):
        for c in range(30):
            lv = random.choice([0, 0, 1, 1, 2, 2, 3, 4])
            colors = ["#21262d", "#0e4429", "#006d32", "#26a641", "#39d353"]
            o += rect(24 + c * 17, 96 + r * 17, 13, 13, colors[lv], rx=3)
    # 下：数据格
    data = [("总提交", "1,234"), ("总 PR", "89"), ("总 Issue", "45"), ("Stars", "63")]
    for i, (k, v) in enumerate(data):
        x = 24 + i * 134
        o += rect(x, 232, 122, 50, "#21262d", rx=10)
        o += text(x + 61, 256, v, 18, "#FF6FD8", anchor="middle", weight="700")
        o += text(x + 61, 274, k, 11, "#8b949e", anchor="middle")
    return o + "</svg>"

for name, fn in [
    ("wakatime.svg", wakatime), ("chess.svg", chess), ("tictactoe.svg", tictactoe),
    ("spotify.svg", spotify), ("blog.svg", blog), ("pet.svg", pet),
    ("platform.svg", platform), ("ai-badge.svg", ai_badge), ("rss.svg", rss),
    ("metrics.svg", metrics),
]:
    save(name, fn())
print("全部演示图生成完成！")

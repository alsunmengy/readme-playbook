"""玩法 14：打砖块动画 —— 用贡献图当砖块生成 GIF
用法: python breakout.py contributions.json out.gif
依赖: pillow (pip install pillow)
"""
import json
import sys
import random
from PIL import Image, ImageDraw

W, H, CELL = 700, 420, 22
BRICK_COLORS = ["#216e39", "#30a14e", "#40c463", "#6be675"]


def load_bricks(path):
    """contributions.json: 52x7 的贡献强度矩阵 (0-4)"""
    with open(path) as f:
        grid = json.load(f)
    bricks = []
    for row, line in enumerate(grid[:7]):
        for col, level in enumerate(line[:32]):
            if level > 0:
                bricks.append({
                    "x": 40 + col * CELL, "y": 40 + row * (CELL // 2 + 4),
                    "w": CELL - 3, "h": CELL // 2 - 1,
                    "color": BRICK_COLORS[min(level, 4) - 1],
                })
    return bricks


def simulate(bricks, steps=150):
    ball = {"x": W / 2, "y": H - 60, "dx": random.choice([-4, 4]), "dy": -5}
    paddle = {"x": W / 2 - 45, "w": 90}
    frames = []
    for _ in range(steps):
        ball["x"] += ball["dx"]
        ball["y"] += ball["dy"]
        if ball["x"] < 10 or ball["x"] > W - 10:
            ball["dx"] *= -1
        if ball["y"] < 10:
            ball["dy"] *= -1
        if ball["y"] > H - 30 and abs(ball["x"] - (paddle["x"] + 45)) < 55:
            ball["dy"] = -abs(ball["dy"])
        for b in bricks[:]:
            if b["x"] < ball["x"] < b["x"] + b["w"] and b["y"] < ball["y"] < b["y"] + b["h"]:
                bricks.remove(b)
                ball["dy"] *= -1
                break
        frames.append(render(ball, paddle, bricks))
    return frames


def render(ball, paddle, bricks):
    img = Image.new("RGB", (W, H), "#0d1117")
    d = ImageDraw.Draw(img)
    for b in bricks:
        d.rectangle([b["x"], b["y"], b["x"] + b["w"], b["y"] + b["h"]], fill=b["color"])
    d.ellipse([ball["x"] - 7, ball["y"] - 7, ball["x"] + 7, ball["y"] + 7], fill="#f0f6fc")
    d.rectangle([paddle["x"], H - 20, paddle["x"] + paddle["w"], H - 12], fill="#58a6ff")
    return img


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "contributions.json"
    out = sys.argv[2] if len(sys.argv) > 2 else "breakout.gif"
    bricks = load_bricks(src)
    frames = simulate(bricks)
    frames[0].save(out, save_all=True, append_images=frames[1:], duration=80, loop=0)
    print(f"saved {len(frames)} frames -> {out}")

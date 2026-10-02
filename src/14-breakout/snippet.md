# 打砖块动画 — 实现思路

把贡献图（52x7 格子）当砖块：

1. Actions 里跑模拟：球在贡献图上弹跳，碰到「有贡献的格子」就消掉
2. 每帧渲染为 GIF（imageio / PIL），推到 output 分支
3. README 嵌入 GIF

```python
# breakout.py 骨架
import imageio.v3 as iio
frames = [render_frame(state) for state in simulate(steps=120)]
iio.imwrite('breakout.gif', frames, duration=0.08, loop=0)
```

本目录附完整可跑脚本 `breakout.py`。

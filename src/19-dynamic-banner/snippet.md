# 动态 SVG 横幅 — 代码片段

## capsule-render（渐变+动画）
```markdown
[![Banner](https://capsule-render.vercel.app/api?type=waving&color=0:FF6FD8,100:7B61FF&height=200&section=header&text=README%20Playbook&fontSize=60&fontColor=ffffff&animation=fadeIn)]()
```

## 亮暗主题自适应
```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="banner-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="banner-light.svg" />
  <img alt="Banner" src="banner-light.svg" />
</picture>
```
GitHub 根据用户亮暗主题自动选图！

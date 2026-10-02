# Bento 网格布局 — 代码片段

GitHub README 用 HTML `<table>` 模拟不对称网格：

```html
<table>
<tr>
<td rowspan="2" width="60%">
  <img src="https://github-readme-stats.vercel.app/api?username=alsunmengy&show_icons=true&theme=radical" />
</td>
<td>
  <img src="https://github-profile-trophy.vercel.app/?username=alsunmengy&theme=onedark" width="100%" />
</td>
</tr>
<tr>
<td>
  <img src="https://readme-typing-svg.demolab.com?...&lines=Hello" />
</td>
</tr>
</table>
```

关键：`rowspan`/`colspan` 造不对称感，`width` 百分比控制比例。

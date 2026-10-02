<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FF6FD8,100:7B61FF&height=220&section=header&text=README%20Playbook&fontSize=72&fontColor=ffffff&animation=fadeIn&desc=30%20%E4%B8%AA%20GitHub%20README%20%E8%8A%B1%E6%B4%BB%20%E7%8E%B0%E5%9C%BA%E5%B1%95%E7%A4%BA&descAlignY=60&descSize=22" />
</p>

<p align="center">
  <a href="https://github.com/alsunmengy/readme-playbook/stargazers"><img src="https://img.shields.io/github/stars/alsunmengy/readme-playbook?style=social&label=Star&color=yellow" /></a>
  <img src="https://komarev.com/ghpvc/?username=alsunmengy&color=brightgreen&style=flat-square&label=Views" />
  <img src="https://img.shields.io/badge/version-1.0.0-blue" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
  <a href="#-目录"><img src="https://img.shields.io/badge/玩法-30%20个-7B61FF" /></a>
</p>

> [!IMPORTANT]
> **这是一份「活的」README 教程**——你看到的每一个卡片、动画、徽章，都是教程里教的玩法，**本页本身就是全部 30 个玩法的现场演示**。每个玩法的可复制代码在 [`src/`](./src) 目录下独立成篇，拆成 30 个小项目，抄就完事了喵！

## 📑 目录

| 分类 | 玩法 |
|---|---|
| 📊 数据统计 | [01 统计卡片](#01-统计卡片) · [02 Streak](#02-连续贡献天数) · [03 访客计数](#03-访客计数) · [04 WakaTime](#04-wakatime) · [05 动态徽章](#05-动态徽章) · [06 摘要卡](#06-摘要卡) · [30 一键 Star](#30-一键-star) |
| 🎨 视觉娱乐 | [07 贪吃蛇](#07-贡献贪吃蛇) · [08 3D 贡献图](#08-3d-贡献图) · [09 终端动画](#09-动态终端) · [10 图标带](#10-滚动图标带) · [11 奖杯柜](#11-奖杯陈列柜) |
| 🕹️ 互动游戏 | [12 国际象棋](#12-交互式国际象棋) · [13 井字棋](#13-井字棋--四子棋) · [14 打砖块](#14-打砖块动画) |
| 🎧 生活社交 | [15 Spotify](#15-spotify-正在播放) · [16 博客同步](#16-博客自动同步) · [17 社交图标](#17-社交媒体图标) |
| ✨ 创意装饰 | [18 Bento](#18-bento-网格) · [19 动态横幅](#19-动态-svg-横幅) · [20 随机语录](#20-随机语录) · [27 图标墙](#27-技术栈图标墙) · [28 隐藏注释](#28-隐藏注释) · [29 提示框](#29-高亮提示框) |
| 🐾 养成模拟 | [21 宠物卡](#21-宠物进度卡) · [22 平台卡片](#22-平台模拟卡片) |
| 🤖 AI 自动化 | [23 AI 徽章](#23-ai-参与徽章) · [24 内容同步](#24-内容自动同步) |
| 📈 进阶可视 | [25 综合信息图](#25-综合信息图) · [26 星标曲线](#26-星标增长图) |

---

## 📊 数据统计类

### 01 统计卡片

<p align="center"><img src="https://github-readme-stats.vercel.app/api?username=alsunmengy&show_icons=true&theme=radical&hide_border=true" height="165" /><img src="https://github-readme-stats.vercel.app/api/top-langs/?username=alsunmengy&layout=compact&theme=tokyonight&hide_border=true" height="165" /></p>

<details><summary>💡 一行代码实现</summary>

```markdown
![GitHub stats](https://github-readme-stats.vercel.app/api?username=你的ID&show_icons=true&theme=radical)
```

</details>

### 02 连续贡献天数

<p align="center"><img src="https://streak-stats.demolab.com?user=alsunmengy&theme=radical&hide_border=true" /></p>

<details><summary>💡 一行代码实现</summary>

```markdown
[![GitHub Streak](https://streak-stats.demolab.com?user=你的ID&theme=radical)](https://git.io/streak-stats)
```

</details>

### 03 访客计数

你刚才的访问已经被它记下啦喵～（本页顶部的 `Views` 徽章）

<details><summary>💡 一行代码实现</summary>

```markdown
![Views](https://komarev.com/ghpvc/?username=你的ID&color=brightgreen&style=flat-square)
```

</details>

### 04 WakaTime

> [!TIP]
> WakaTime 需要先绑定编辑器插件记录编码时长，绑定后徽章自动出周报图表。详见 [`src/04-wakatime/`](./src/04-wakatime/)。

### 05 动态徽章

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI-Assisted-7B61FF?style=for-the-badge" />
</p>

### 06 摘要卡

<p align="center"><img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=alsunmengy&theme=radical" /><img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=alsunmengy&theme=radical" /></p>

---

## 🎨 视觉娱乐类

### 07 贡献贪吃蛇

> [!NOTE]
> 小蛇吃掉你的贡献方块！由 GitHub Actions 定时生成 SVG 动画（配置见 [`src/07-snake/`](./src/07-snake/)），生成后嵌入效果：

```markdown
![Snake animation](https://raw.githubusercontent.com/alsunmengy/readme-playbook/output/github-snake.svg)
```

### 08 3D 贡献图

<p align="center"><img src="https://github-profile-3d-contrib.vercel.app/api/alsunmengy?theme=github_dark&column=20" width="85%" /></p>

### 09 动态终端

<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=800&color=00FF41&width=435&lines=%24+whoami%3A+alsunmengy;%24+cat+skills.txt%3A+Python%2FDocker%2FNAS;%24+echo+%22Hello+World%22%3AHello+World%21&center=true&vCenter=true&repeat=true" /></p>

### 10 滚动图标带

<p align="center"><img src="https://skillicons.dev/icons?i=python,docker,linux,nginx,react,typescript,postgres,redis,git,github,vscode,ubuntu&perline=12" /></p>

### 11 奖杯陈列柜

<p align="center"><img src="https://github-profile-trophy.vercel.app/?username=alsunmengy&theme=onedark&margin-w=12&margin-h=12" width="85%" /></p>

---

## 🕹️ 互动游戏类

### 12 交互式国际象棋

> [!NOTE]
> README 不能跑 JS，但可以用 **Issue 评论驱动**实现异步对战：访客在 Issue 留下走法 → Actions 校验并重绘棋盘 SVG。完整方案 + 渲染脚本见 [`src/12-chess/`](./src/12-chess/)。

### 13 井字棋 / 四子棋

同上思路，状态机更简单，`src/13-tictactoe-connect4/` 附核心逻辑代码。

### 14 打砖块动画

贡献图当砖块，球弹来弹去消格子！`src/14-breakout/` 附完整可跑的 GIF 生成脚本。

---

## 🎧 生活与社交类

### 15 Spotify 正在播放

> [!TIP]
> 需要 Spotify 账号 + Vercel 部署（5 分钟搞定），带均衡器动效。步骤见 [`src/15-spotify-now-playing/`](./src/15-spotify-now-playing/)。

### 16 博客自动同步

```markdown
<!-- BLOG-POST-LIST:START -->
<!-- 这里会被 GitHub Actions 自动填充最新博文 -->
<!-- BLOG-POST-LIST:END -->
```

### 17 社交媒体图标

<p align="center">
  <a href="https://github.com/alsunmengy"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://space.bilibili.com/"><img src="https://img.shields.io/badge/Bilibili-00A1D6?style=for-the-badge&logo=bilibili&logoColor=white" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=rss&logoColor=white" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
</p>

---

## ✨ 创意与装饰类

### 18 Bento 网格

本页 [01 统计卡片](#01-统计卡片) 处的双卡并排就是 Bento 思路的最小实现——用 `<table>` 的 `rowspan`/`colspan` 拼不对称网格。大杂烩示例见 [`src/18-bento-grid/`](./src/18-bento-grid/)。

### 19 动态 SVG 横幅

本页顶部的渐变波浪横幅就是 capsule-render 生成的！亮暗主题自动切换的写法见 [`src/19-dynamic-banner/`](./src/19-dynamic-banner/)。

### 20 随机语录

<p align="center"><img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight" /></p>

刷新页面就换一句，永动机喵～

### 27 技术栈图标墙

<p align="center"><img src="https://skillicons.dev/icons?i=py,ts,react,docker,linux,nginx,postgres,redis,git,github,vscode,ubuntu,arch,raspberrypi,arduino,cpp,pytorch,tensorflow&perline=9" /></p>

### 28 隐藏注释

<!--
  🐱 这段字只有点「编辑」才能看到！
  TODO: 加一个 3D 城市版贡献图
  提醒: 千万别在这里写密码，公开仓库谁都能看到编辑页
-->

**就是现在**——这段字在页面上完全隐身，但你点编辑就能看到我留的小纸条。

### 29 高亮提示框

> [!NOTE] 补充信息
> [!TIP] 小技巧
> [!IMPORTANT] 关键信息
> [!WARNING] 注意事项
> [!CAUTION] 危险操作

五色提示框，GitHub 原生语法，零依赖。

---

## 🐾 养成与模拟类

### 21 宠物进度卡

> [!NOTE]
> 电子宠物吃你的贡献长大，共 9 个进化阶段。渲染脚本见 [`src/21-pet-card/`](./src/21-pet-card/)。

### 22 平台模拟卡片

Netflix「今日 TOP 10」、Steam 游戏卡、Duolingo 连胜……SVG 模板仿平台 UI，模板在 [`src/22-platform-cards/templates/`](./src/22-platform-cards/)。

---

## 🤖 AI 与自动化类

### 23 AI 参与徽章

<p align="center"><img src="https://img.shields.io/badge/AI%20Assisted-Specs%20%C2%9C%20Code%20%C2%9C%20Review%20%C2%9C-7B61FF?style=for-the-badge" /></p>

透明声明 AI 参与程度，或分析 git 历史算出「Vibe Coding 占比」。

### 24 内容自动同步

博客 / YouTube / StackOverflow 的 RSS 通过 Actions 定时同步进 README，零手动维护。通用配置见 [`src/24-rss-auto-sync/`](./src/24-rss-auto-sync/)。

---

## 📈 进阶可视化

### 25 综合信息图

> [!TIP]
> `lowlighter/metrics` 一张图塞下 30+ 插件（Spotify、WakaTime、isocalendar…），300+ 配置项。完整 workflow 在 [`src/25-metrics-infographic/`](./src/25-metrics-infographic/)。

### 26 星标增长图

<p align="center"><a href="https://star-history.com/#alsunmengy/readme-playbook&Date"><img src="https://api.star-history.com/svg?repos=alsunmengy/readme-playbook&type=Date" width="80%" /></a></p>

---

## 30 一键 Star

<p align="center">
  <a href="https://github.com/alsunmengy/readme-playbook">
    <img src="https://img.shields.io/github/stars/alsunmengy/readme-playbook?style=for-the-badge&logo=github&color=FFD700&label=⭐%20Star%20Me" />
  </a>
</p>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7B61FF,100:FF6FD8&height=160&section=footer&text=Made%20with%20%E2%9D%A4%20by%20Aemeath&fontSize=28&fontColor=ffffff&animation=fadeIn" />
</p>

> [!CAUTION]
> 教程里的 Actions 类玩法（07 / 06 / 16 / 24 / 25）需要在你自己的仓库里启用 Actions 权限并按各 `src/` 目录说明配置，图片类玩法（01–03 / 08–11 / 20 / 26 / 27）复制一行 URL 即刻生效。

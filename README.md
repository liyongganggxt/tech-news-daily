# 每日科技新闻 · Daily Tech News

> 🚀 自动聚合全球科技资讯，每天定时更新

🌐 **在线访问**：[https://liyongganggxt.github.io/tech-news-daily](https://liyongganggxt.github.io/tech-news-daily)

---

## ✨ 功能特性

- 📡 **多源聚合**：Hacker News、TechCrunch、The Verge、Wired、MIT Technology Review、Ars Technica
- ⏰ **每日自动更新**：GitHub Actions 每天 10:00（北京时间）自动抓取最新新闻
- 🔍 **实时搜索**：支持按标题、描述、来源关键词过滤
- 🏷️ **分类筛选**：按新闻分类快速切换
- 🌙 **深色主题**：护眼的深色 UI 设计
- 📱 **响应式布局**：完美适配桌面和移动设备

## 🗂️ 项目结构

```
tech-news-daily/
├── index.html              # 主页面
├── news.json               # 新闻数据（由 Actions 自动更新）
├── scripts/
│   └── fetch_news.py       # 新闻抓取脚本
└── .github/
    └── workflows/
        └── sync-news.yml   # GitHub Actions 工作流
```

## 🚀 快速部署

### 1. Fork / Clone 此仓库

```bash
git clone https://github.com/liyongganggxt/tech-news-daily.git
```

### 2. 开启 GitHub Pages

进入仓库 → **Settings** → **Pages**：
- Source: `Deploy from a branch`
- Branch: `main` / `(root)`
- 点击 **Save**

### 3. 手动触发首次同步

进入 **Actions** → `Daily Tech News Sync` → **Run workflow**

等待约 1 分钟后，刷新 Pages 链接即可看到新闻！

### 4. 后续自动更新

GitHub Actions 已配置每天 UTC 02:00（北京时间 10:00）自动运行。

## 📰 新闻来源

| 来源 | 类型 |
|------|------|
| Hacker News | Tech Community |
| TechCrunch | Startups & Tech |
| The Verge | Tech News |
| Wired | Tech & Science |
| MIT Technology Review | Deep Tech |
| Ars Technica | Tech Analysis |

## 📄 License

MIT License

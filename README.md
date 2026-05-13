# 每日科技新闻 · Daily Tech News

> 🚀 自动聚合全球 15 家权威科技媒体资讯，每 20 分钟自动更新

🌐 **在线访问**：[https://liyongganggxt.github.io/tech-news-daily](https://liyongganggxt.github.io/tech-news-daily)

---

## ✨ 功能特性

- 📡 **多源聚合**：15 家全球权威科技媒体，中文 5 家 + 英文 10 家
- ⏰ **自动更新**：GitHub Actions 每 20 分钟自动抓取最新新闻
- 🔍 **实时搜索**：支持按标题、描述、来源关键词过滤
- 🏷️ **分类筛选**：按新闻分类快速切换
- 🌙 **深色主题**：护眼的深色 UI 设计
- 📱 **响应式布局**：完美适配桌面和移动设备

## 📰 新闻来源

### 中文媒体（5 家）

| 来源 | 类型 |
|------|------|
| IT之家 (ithome.com) | 综合科技资讯 |
| 36氪 (36kr.com) | 创投 & 商业科技 |
| 少数派 (sspai.com) | 效率工具 & 数码生活 |
| 爱范儿 (ifanr.com) | 消费科技 & 生活方式 |
| 极客公园 (geekpark.net) | 深度科技 & 创新报道 |

### 英文媒体（10 家）

| 来源 | 类型 |
|------|------|
| The Verge | 科技 & 文化 |
| Ars Technica | 深度技术分析 |
| TechCrunch | 创投 & 初创公司 |
| Wired | 科技 & 科学 |
| MIT Technology Review | 前沿技术 |
| Engadget | 消费电子评测 |
| ZDNet | 企业 & 商业技术 |
| The Register | IT 行业新闻 |
| BBC Technology | 科技 & 社会 |
| Hacker News | 开发者社区热榜 |

## 🗂️ 项目结构

```
tech-news-daily/
├── index.html              # 主页面（深色主题、响应式布局）
├── news.json               # 新闻数据（由 Actions 自动更新）
├── .nojekyll               # 禁止 Jekyll 处理
├── scripts/
│   └── fetch_news.py       # 新闻抓取脚本（RSS/Atom）
└── .github/
    └── workflows/
        └── sync-news.yml   # GitHub Actions 定时工作流
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

GitHub Actions 已配置每 20 分钟自动运行（`*/20 * * * *`）。

> ⚠️ **注意**：GitHub scheduled workflows 可能存在 5-30 分钟延迟，新仓库首次需手动触发以激活定时任务。

## 🔧 自定义配置

在 `scripts/fetch_news.py` 中可调整：

- `RSS_FEEDS`：添加或替换 RSS 源
- `ITEMS_PER_FEED`：每个源抓取的条数（默认 10）
- `TOTAL_LIMIT`：总条数上限（默认 150）
- 请求超时时间（默认 20 秒）

## 📄 License

MIT License

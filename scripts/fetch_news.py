#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
科技新闻抓取脚本
每日从多个 RSS 源抓取科技新闻，生成 news.json 供前端页面展示
"""

import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
import re
import html
import os

# 科技类 RSS 源列表（公开免费，无需 API Key）
# 5个中文权威科技媒体 + 10个英文权威科技媒体
RSS_FEEDS = [
    # ── 中文媒体 (5) ──
    {
        "name": "IT之家",
        "url": "https://www.ithome.com/rss/",
        "category": "科技资讯",
        "lang": "zh"
    },
    {
        "name": "36氪",
        "url": "https://36kr.com/feed",
        "category": "创投科技",
        "lang": "zh"
    },
    {
        "name": "少数派",
        "url": "https://sspai.com/feed",
        "category": "效率工具",
        "lang": "zh"
    },
    {
        "name": "爱范儿",
        "url": "https://www.ifanr.com/feed",
        "category": "数码生活",
        "lang": "zh"
    },
    {
        "name": "极客公园",
        "url": "https://www.geekpark.net/rss",
        "category": "极客创新",
        "lang": "zh"
    },
    # ── 英文媒体 (10) ──
    {
        "name": "The Verge",
        "url": "https://www.theverge.com/rss/index.xml",
        "category": "Tech News",
        "lang": "en"
    },
    {
        "name": "Ars Technica",
        "url": "https://feeds.arstechnica.com/arstechnica/index",
        "category": "Tech Analysis",
        "lang": "en"
    },
    {
        "name": "TechCrunch",
        "url": "https://techcrunch.com/feed/",
        "category": "Startups & Tech",
        "lang": "en"
    },
    {
        "name": "Wired",
        "url": "https://www.wired.com/feed/rss",
        "category": "Tech & Science",
        "lang": "en"
    },
    {
        "name": "MIT Technology Review",
        "url": "https://www.technologyreview.com/feed/",
        "category": "Deep Tech",
        "lang": "en"
    },
    {
        "name": "Engadget",
        "url": "https://www.engadget.com/rss.xml",
        "category": "Consumer Tech",
        "lang": "en"
    },
    {
        "name": "ZDNet",
        "url": "https://www.zdnet.com/news/rss.xml",
        "category": "Enterprise Tech",
        "lang": "en"
    },
    {
        "name": "The Register",
        "url": "https://www.theregister.com/headlines.rss",
        "category": "IT & Dev",
        "lang": "en"
    },
    {
        "name": "BBC Technology",
        "url": "https://feeds.bbci.co.uk/news/technology/rss.xml",
        "category": "Global Tech",
        "lang": "en"
    },
    {
        "name": "Hacker News",
        "url": "https://hnrss.org/frontpage",
        "category": "Tech Community",
        "lang": "en"
    },
]

ITEMS_PER_FEED = 10  # 每个源最多抓取条目数
TOTAL_LIMIT = 150    # 总条目上限


def clean_html(raw_html):
    """去除 HTML 标签并解码 HTML 实体"""
    if not raw_html:
        return ""
    text = re.sub(r'<[^>]+>', '', raw_html)
    text = html.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:300] + "..." if len(text) > 300 else text


def parse_date(date_str):
    """解析多种日期格式，统一转换为 ISO 8601"""
    if not date_str:
        return datetime.now(timezone.utc).isoformat()
    formats = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt).isoformat()
        except ValueError:
            continue
    return datetime.now(timezone.utc).isoformat()


def fetch_rss(feed_info):
    """抓取并解析单个 RSS/Atom feed"""
    items = []
    url = feed_info["url"]
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; TechNewsBot/1.0)"
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as resp:
            content = resp.read()
        root = ET.fromstring(content)
        ns = {}
        # 尝试获取命名空间
        tag = root.tag
        if tag.startswith("{"):
            ns_uri = tag[1:tag.index("}")]
            ns["atom"] = ns_uri

        # 兼容 RSS 2.0 和 Atom
        entries = root.findall(".//item") or root.findall(".//{%s}entry" % ns.get("atom", ""))

        for entry in entries[:ITEMS_PER_FEED]:
            # 标题
            title_el = (entry.find("title") or
                        entry.find("{%s}title" % ns.get("atom", "")))
            title = clean_html(title_el.text if title_el is not None else "")

            # 链接
            link_el = (entry.find("link") or
                       entry.find("{%s}link" % ns.get("atom", "")))
            if link_el is not None:
                link = link_el.get("href") or link_el.text or ""
            else:
                link = ""

            # 描述 / 摘要
            desc_el = (entry.find("description") or
                       entry.find("summary") or
                       entry.find("{%s}summary" % ns.get("atom", "")) or
                       entry.find("{%s}content" % ns.get("atom", "")))
            description = clean_html(desc_el.text if desc_el is not None else "")

            # 发布日期
            date_el = (entry.find("pubDate") or
                       entry.find("{%s}published" % ns.get("atom", "")) or
                       entry.find("{%s}updated" % ns.get("atom", "")))
            pub_date = parse_date(date_el.text if date_el is not None else None)

            if title and link:
                items.append({
                    "title": title,
                    "link": link,
                    "description": description,
                    "pubDate": pub_date,
                    "source": feed_info["name"],
                    "category": feed_info["category"],
                    "lang": feed_info["lang"]
                })
    except Exception as e:
        print(f"[WARN] Failed to fetch {url}: {e}")

    return items


def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting news fetch...")
    all_items = []

    for feed in RSS_FEEDS:
        print(f"  Fetching: {feed['name']}", flush=True)
        items = fetch_rss(feed)
        all_items.extend(items)
        print(f"    Got {len(items)} items")

    # 按发布时间倒序排列
    all_items.sort(key=lambda x: x["pubDate"], reverse=True)
    all_items = all_items[:TOTAL_LIMIT]

    output = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "total": len(all_items),
        "items": all_items
    }

    out_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "news.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"[Done] Saved {len(all_items)} articles to news.json")


if __name__ == "__main__":
    main()

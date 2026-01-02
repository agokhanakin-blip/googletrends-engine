import feedparser

RSS_URL = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"

feed = feedparser.parse(RSS_URL)

trends = []
for entry in feed.entries:
    trends.append(entry.title)

print("=== Google Trends RSS ===")
for t in trends[:20]:
    print("-", t)

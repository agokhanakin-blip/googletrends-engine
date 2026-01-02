import feedparser
import json
from datetime import datetime

print("=== Google Trends Engine Started ===")

RSS_SOURCES = [
    "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US",
    "https://trends.google.com/trends/trendingsearches/realtime/rss?geo=US&category=gaming",
    "https://trends.google.com/trends/trendingsearches/realtime/rss?category=gaming"
]

items = []

for url in RSS_SOURCES:
    feed = feedparser.parse(url)
    if feed.entries:
        print(f"✔ RSS OK: {url}")
        for entry in feed.entries:
            title = entry.title.strip().lower()
            items.append(title)
        break
    else:
        print(f"✖ RSS EMPTY: {url}")

output = {
    "date": datetime.utcnow().strftime("%Y-%m-%d"),
    "source": "google_trends_rss",
    "count": len(items),
    "items": items[:20]
}

with open("trends.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"✔ trends.json generated ({len(items)} items)")
print("=== Google Trends Engine Finished ===")

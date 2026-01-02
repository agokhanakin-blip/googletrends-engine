import feedparser
import requests
import json
from datetime import datetime

print("=== Trend Engine Started ===")

BLOCK_WORDS = [
    "weekly", "thread", "discussion", "support",
    "deals", "monday", "post", "share your",
    "what have you been playing"
]

KEYWORDS = [
    "game", "games", "io", "puzzle",
    "racing", "multiplayer", "browser", "indie"
]

trends = []

# Reddit RSS
REDDIT_RSS = [
    "https://www.reddit.com/r/gaming/.rss",
    "https://www.reddit.com/r/pcgaming/.rss",
    "https://www.reddit.com/r/browsergames/.rss",
    "https://www.reddit.com/r/iosgaming/.rss",
    "https://www.reddit.com/r/IndieGaming/.rss",
]

for url in REDDIT_RSS:
    feed = feedparser.parse(url)
    for entry in feed.entries[:10]:
        title = entry.title.lower()

        if any(b in title for b in BLOCK_WORDS):
            continue

        if any(k in title for k in KEYWORDS):
            trends.append(title)

# Bing Trends
try:
    bing_url = "https://trends.bing.com/trending/api/v1/trendingSearches?cc=us"
    headers = {"User-Agent": "Mozilla/5.0"}
    data = requests.get(bing_url, headers=headers, timeout=10).json()

    for item in data.get("value", [])[:15]:
        q = item.get("query", "").lower()
        if any(k in q for k in KEYWORDS):
            trends.append(q)

except Exception as e:
    print("Bing error:", e)

clean = sorted(set(trends))

output = {
    "date": datetime.utcnow().strftime("%Y-%m-%d"),
    "source": "reddit_bing_filtered",
    "count": len(clean),
    "items": clean[:25]
}

with open("trends.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"✔ trends.json generated ({len(clean)} items)")
print("=== Trend Engine Finished ===")

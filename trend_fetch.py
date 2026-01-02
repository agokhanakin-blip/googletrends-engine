import feedparser
import requests
import json
from datetime import datetime

print("=== Trend Engine Started ===")

trends = []

# =========================
# REDDIT RSS (OYUN KAYNAĞI)
# =========================
REDDIT_RSS = [
    "https://www.reddit.com/r/gaming/.rss",
    "https://www.reddit.com/r/pcgaming/.rss",
    "https://www.reddit.com/r/browsergames/.rss",
    "https://www.reddit.com/r/iosgaming/.rss",
    "https://www.reddit.com/r/IndieGaming/.rss",
]

for url in REDDIT_RSS:
    feed = feedparser.parse(url)
    if feed.entries:
        print(f"✔ Reddit RSS OK: {url}")
        for entry in feed.entries[:5]:
            title = entry.title.lower()
            if "game" in title or "games" in title or "io" in title:
                trends.append(title)
    else:
        print(f"✖ Reddit RSS EMPTY: {url}")

# =========================
# BING TRENDS (JSON)
# =========================
try:
    bing_url = "https://trends.bing.com/trending/api/v1/trendingSearches?cc=us"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    r = requests.get(bing_url, headers=headers, timeout=10)
    data = r.json()

    for item in data.get("value", [])[:10]:
        query = item.get("query", "").lower()
        if "game" in query or "games" in query:
            trends.append(query)

    print("✔ Bing Trends OK")

except Exception as e:
    print("✖ Bing Trends ERROR:", e)

# =========================
# TEMİZLE + UNIQUE
# =========================
clean = sorted(list(set(trends)))

output = {
    "date": datetime.utcnow().strftime("%Y-%m-%d"),
    "source": "reddit_bing",
    "count": len(clean),
    "items": clean[:30]
}

with open("trends.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"✔ trends.json generated ({len(clean)} items)")
print("=== Trend Engine Finished ===")

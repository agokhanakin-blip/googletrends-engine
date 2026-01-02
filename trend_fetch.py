import feedparser
import json
from datetime import datetime

print("=== Google Trends Engine Started ===")

rss_url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
feed = feedparser.parse(rss_url)

output = {
    "date": datetime.utcnow().strftime("%Y-%m-%d"),
    "source": "google_trends_us",
    "items": []
}

if not feed.entries:
    print("FETCH ERROR: RSS empty")
else:
    for entry in feed.entries[:20]:
        title = entry.title.strip().lower()
        output["items"].append(title)
        print(f"PASSED: {title}")

with open("trends.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("✔ trends.json generated")
print("=== Google Trends Engine Finished ===")

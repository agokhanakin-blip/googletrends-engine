import feedparser

print("=== Google Trends Engine Started ===")

rss_url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
feed = feedparser.parse(rss_url)

if not feed.entries:
    print("FETCH ERROR: RSS empty")
else:
    for entry in feed.entries[:10]:
        print(f"PASSED: {entry.title}")

print("=== Google Trends Engine Finished ===")

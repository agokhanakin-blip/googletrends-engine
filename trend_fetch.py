from pytrends.request import TrendReq
import json
import re
from datetime import datetime

# Google bağlantısı
pytrends = TrendReq(hl='en-US', tz=360)

# Google Trends – US, son 7 gün
trending = pytrends.trending_searches(pn='united_states')[0].tolist()

# Oyunla alakalı kelime şartları
GAME_KEYWORDS = [
    "game", "games", "io", "puzzle", "play", "online", "browser"
]

# Spam / alakasız filtre
BLOCKLIST = [
    "lottery", "numbers", "bet", "raffle",
    "news", "actor", "movie", "show"
]

clean = []

for item in trending:
    text = item.lower()

    if any(bad in text for bad in BLOCKLIST):
        continue

    if any(ok in text for ok in GAME_KEYWORDS):
        clean.append({
            "keyword": item,
            "source": "google_trends",
            "date": datetime.utcnow().strftime("%Y-%m-%d")
        })

output = {
    "generated_at": datetime.utcnow().isoformat(),
    "count": len(clean),
    "trends": clean
}

with open("trends.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)

print(f"Generated {len(clean)} game-related trends.")

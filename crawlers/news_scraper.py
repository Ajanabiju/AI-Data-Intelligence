import feedparser

def get_ai_news():

    feed = feedparser.parse(
        "https://feeds.feedburner.com/oreilly/radar"
    )

    news = []

    for entry in feed.entries[:10]:

        news.append({
            "title": entry.title,
            "published": entry.get(
                "published",
                "Unknown"
            ),
            "url": entry.link
        })

    return news
import feedparser

def get_news():

    feed = feedparser.parse(
        "https://techcrunch.com/category/artificial-intelligence/feed/"
    )

    news = []

    for entry in feed.entries[:10]:

        news.append({
            "title": entry.title,
            "url": entry.link,
            "published": getattr(
                entry,
                "published",
                None
            )
        })

    return news
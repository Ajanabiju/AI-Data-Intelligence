import feedparser

def get_recent_papers(limit=10):

    url = (
        "http://export.arxiv.org/api/query?"
        f"search_query=cat:cs.AI&start=0&max_results={limit}"
    )

    feed = feedparser.parse(url)

    papers = []

    for entry in feed.entries:

        papers.append({
            "title": entry.title,
            "authors": [author.name for author in entry.authors],
            "published": entry.published,
            "url": entry.link
        })

    return papers
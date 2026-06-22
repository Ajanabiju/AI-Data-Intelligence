import feedparser

def get_jobs():

    feed = feedparser.parse(
        "https://weworkremotely.com/categories/remote-programming-jobs.rss"
    )

    jobs = []

    for entry in feed.entries[:10]:

        title = entry.title

        company = (
            title.split(":")[0]
            if ":" in title
            else "Unknown"
        )

        jobs.append({
            "company": company,
            "title": title,
            "url": entry.link,
            "published": getattr(
                entry,
                "published",
                None
            ),
            "is_remote": True,
            "role_family": "Engineering"
        })

    return jobs
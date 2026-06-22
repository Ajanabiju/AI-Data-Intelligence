def create_news(
    title,
    source,
    url,
    published_date
):

    return {
        "schemaVersion": "1.0",
        "recordType": "NEWS",
        "content": {
            "title": title,
            "source": source,
            "url": url,
            "published_date": published_date
        }
    }
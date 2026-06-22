def create_research_paper(
    title,
    authors,
    paper_url,
    published_date,
    github_url=None,
    github_stars=None
):

    return {
        "schemaVersion": "1.0",
        "recordType": "RESEARCH_PAPER",
        "content": {
            "title": title,
            "authors": authors,
            "paper_url": paper_url,
            "github_url": github_url,
            "github_stars": github_stars,
            "published_date": published_date
        }
    }
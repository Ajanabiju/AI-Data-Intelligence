import requests
from bs4 import BeautifulSoup

def get_papers(limit=20):

    url = "https://huggingface.co/papers/trending"

    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    papers = []

    for link in soup.find_all("a", href=True):

        href = link["href"]

        if "/papers/" in href:

            papers.append({
                "title": link.get_text(strip=True),
                "url": "https://huggingface.co" + href
            })

        if len(papers) >= limit:
            break

    return papers
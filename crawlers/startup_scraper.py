import requests
from bs4 import BeautifulSoup

def get_startups(limit=20):

    url = "https://www.ycombinator.com/companies"

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

    startups = []

    text = soup.get_text()

    words = text.split()

    for word in words:

        if len(word) > 3 and word[0].isupper():

            startups.append({
                "name": word,
                "source": "Y Combinator",
                "url": url
            })

    unique = []

    seen = set()

    for startup in startups:

        if startup["name"] not in seen:

            seen.add(startup["name"])

            unique.append(startup)

    return unique[:limit]
import requests

def get_startups(limit=1000):

    startups = []

    per_page = 100

    pages = limit // per_page

    for page in range(1, pages + 1):

        url = (
            "https://api.github.com/search/users"
            f"?q=type:org&per_page={per_page}&page={page}"
        )

        response = requests.get(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "Mozilla/5.0"
            }
        )

        data = response.json()

        for org in data["items"]:

            startups.append({
                "name": org["login"],
                "source": "GitHub Organizations",
                "url": org["html_url"]
            })

        print(
            f"Collected {len(startups)} startups..."
        )

    return startups[:limit]
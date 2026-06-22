import requests
import re

def get_startups():

    url = "https://www.ycombinator.com/companies"

    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    text = response.text

    matches = re.findall(
        r'/api/[A-Za-z0-9_\-/]+',
        text
    )

    for match in sorted(set(matches)):
        print(match)

    return []
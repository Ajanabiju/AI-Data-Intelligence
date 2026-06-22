import requests
from bs4 import BeautifulSoup

def get_papers(limit=10):

    url = "https://huggingface.co/papers/trending"

    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    return [
        {
            "title": "Trending AI Papers Source Connected",
            "url": url
        }
    ]
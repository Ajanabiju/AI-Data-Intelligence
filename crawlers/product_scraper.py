import requests

def get_products(limit=1000):

    products = []

    page_size = 100

    for offset in range(0, limit, page_size):

        url = (
            f"https://huggingface.co/api/models"
            f"?limit={page_size}"
            f"&offset={offset}"
        )

        response = requests.get(url)

        data = response.json()

        for item in data:

            products.append({
                "name": item.get("id"),
                "downloads": item.get("downloads"),
                "likes": item.get("likes")
            })

        print(
            f"Collected {len(products)} products..."
        )

    return products[:limit]
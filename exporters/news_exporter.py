import csv

def export_news(news, filename):

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "title",
                "url",
                "published"
            ]
        )

        writer.writeheader()

        for item in news:
            writer.writerow(item)

    print(f"Exported {len(news)} news articles")
import csv

def export_startups(startups, filename):

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "name",
                "source",
                "url"
            ]
        )

        writer.writeheader()

        writer.writerows(startups)

    print(
        f"Exported {len(startups)} startups"
    )
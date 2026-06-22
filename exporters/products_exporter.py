import csv

def export_products(products, filename):

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
                "downloads",
                "likes"
            ]
        )

        writer.writeheader()

        for product in products:
            writer.writerow(product)

    print(
        f"Exported {len(products)} products"
    )
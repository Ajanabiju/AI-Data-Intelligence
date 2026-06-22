import csv

def export_jobs(jobs, filename):

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "company",
                "title",
                "url",
                "published",
                "is_remote",
                "role_family"
            ]
        )

        writer.writeheader()

        for job in jobs:
            writer.writerow(job)

    print(f"Exported {len(jobs)} jobs")
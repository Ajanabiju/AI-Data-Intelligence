import csv

def export_entity_mapping(filename):

    mappings = [
        ["Open AI", "OpenAI"],
        ["OpenAI Inc.", "OpenAI"],
        ["Anthropic AI", "Anthropic"],
        ["DeepMind", "Google DeepMind"],
        ["x ai", "xAI"],
        ["Mistral", "Mistral AI"]
    ]

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Raw Name", "Canonical Name"]
        )

        writer.writerows(mappings)

    print(
        f"Exported {len(mappings)} mappings"
    )
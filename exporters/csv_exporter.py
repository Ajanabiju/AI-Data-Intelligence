import pandas as pd

def export_to_csv(data, filename):

    df = pd.DataFrame(data)

    df.to_csv(
        filename,
        index=False
    )

    print(
        f"Exported {len(data)} records to {filename}"
    )
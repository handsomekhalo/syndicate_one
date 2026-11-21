import csv
from pathlib import Path


def export_to_csv(records, file_path):
    if not records:
        raise ValueError("Cannot export an empty dataset")

    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=records[0].keys()
        )

        writer.writeheader()
        writer.writerows(records)
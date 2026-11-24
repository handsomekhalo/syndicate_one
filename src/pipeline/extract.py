import csv

def extract_csv(file_path):
    records = []

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        records = list(reader)

    return records
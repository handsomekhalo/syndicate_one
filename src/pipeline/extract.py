import csv

def extract_employees(file_path):
    employees = []

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            employees.append(row)

    return employees
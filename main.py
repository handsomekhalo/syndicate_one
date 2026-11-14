from src.pipeline.extract import extract_employees

employees = extract_employees("data/synthetic/employees.csv")

print("Total extracted employees:", len(employees))
print("First employee:", employees[0])
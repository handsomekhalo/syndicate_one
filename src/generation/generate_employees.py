
import random
from faker import Faker
import csv
from pathlib import Path
# fake = Faker()
fake = Faker("en_GB")

def generate_employee():
    employee = {
    "person_id": 1,
    "employer_id":1,
    "tenant_id": 3,
    "first_name":fake.first_name(),
    "last_name":fake.last_name(),
    "sa_id_number":"0211125132089",
    "employee_id":None,
    "bank_account_ref": f"ACC-{random.randint(100000, 999999)}",
    "city":fake.city(),
    "is_active": True,
    "phone_number": f"0{random.randint(600000000, 899999999)}",}
    

    
    
    return employee


def generate_employees(count):
    list_of_emps = []

    for i in range(1, count + 1):
        employee = generate_employee()
        employee["employee_id"] = i
        employee["person_id"] = i
        list_of_emps.append(employee)
        

    return list_of_emps



def export_employees_to_csv(employees, file_path):
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)#Creates the output folder if necessary

    with open(file_path, "w", newline="", encoding="utf-8") as file:#Opens the CSV file and closes it automatically
        # "w" Writes a new file or overwrites an existing one
        writer = csv.DictWriter(#csv.DictWriter	Writes Python dictionaries as CSV rows
            file,
            fieldnames=employees[0].keys()#Gets the column names from the first employee
        )

        writer.writeheader()
        writer.writerows(employees)




if __name__ == "__main__":
    employees = generate_employees(5)

    export_employees_to_csv(
        employees,
        "data/synthetic/employees.csv"
    )

    print("Successfully exported", len(employees), "employees")


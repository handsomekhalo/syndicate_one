
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








if __name__ == "__main__":
    employees = generate_employees(5)

    for employee in employees:
        print(
            employee["employee_id"],
            employee["person_id"],
            employee["phone_number"],
            employee["bank_account_ref"],

            employee["first_name"],
            employee["last_name"]
        )




import random

def generate_employee():
    employee = {
    "person_id": 1,
    "employer_id":1,
    "tenant_id": 3,
    "first_name":'alice',
    "last_name":"wonderland",
    "sa_id_number":"0211125132089",
    "employee_id":random.randint(1,1000),
    "bank_account_ref":12545,
    # "company_name": "liberty insure",
    # "registration_number": "k2712345678",
    # "industry": "IT",
    "city": "Cape Town",
    "is_active": True,
    "phone_number": "0763741256",
}
    

    
    
    return employee

# print(generate_employee())
# print(generate_employee())
# print(generate_employee())
def generate_employees(count):
    list_of_emps = []

    for i in range(1, count + 1):
        employee = generate_employee()
        employee["employee_id"] = i
        list_of_emps.append(employee)

    return list_of_emps



from src.pipeline.transform import clean_employee, get_missing_fields, has_required_fields, transform_employees
from src.pipeline.extract import extract_employees

employees = extract_employees("data/synthetic/employees.csv")


# employees[0]["first_name"] = "  thabo  "
employees[0]["first_name"] = "   "
employees[0]["last_name"] = "MOKOENA"
employees[0]["phone_number"] = "  076 374 1256  "
# employees[0]["first_name"] = "   "
valid_employees, rejected_employees = transform_employees(employees)
print(valid_employees[0])
print(rejected_employees[0])

# test_employee = {
#     "employee_id": "101",
#     "tenant_id": "3",
#     "first_name": "  thabo  ",
#     "last_name": "MOKOENA",
#     "phone_number": "  076 374 1256  "
# }

# result = clean_employee(test_employee)


# print(result)
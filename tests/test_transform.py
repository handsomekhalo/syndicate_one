import unittest
from src.pipeline.transform import clean_employee, get_missing_fields, transform_employees


class TestEmployeeTransformation(unittest.TestCase):

    def test_clean_employee(self):
        employee = {
            "employee_id": "101",
            "first_name": "  thabo  ",
            "last_name": "MOKOENA",
            "phone_number": "  076 374 1256  "
        }

        cleaned = clean_employee(employee)

        self.assertEqual(cleaned["first_name"], "Thabo")
        self.assertEqual(cleaned["last_name"], "Mokoena")
        self.assertEqual(cleaned["phone_number"], "0763741256")


    def test_get_missing_fields(self):
        incomplete_employee = {
            "first_name": "",
            "last_name": "",
            "phone_number": "",
            "employee_id": "12"
        }

        result = get_missing_fields(incomplete_employee)

        self.assertEqual(result, ["first_name","last_name"], "")
        # self.assertEqual(result, ["last_name"], "")
        # self.assertEqual(result, ["phone_number", ""])

    def test_transform_employees(self):
        employees = [
            {
                "employee_id": "101",
                "first_name": "Thabo",
                "last_name": "Mokoena",
                "phone_number": "0763741256",
                "is_active": "True"
            },
            {
                "employee_id": "102",
                "first_name": "",
                "last_name": "Dlamini",
                "phone_number": "0763741257",
                "is_active": "True"
            },
            {
                "employee_id": "103",
                "first_name": "Lerato",
                "last_name": "",
                "phone_number": "0763741258",
                "is_active": "False"
            }
        ]

        valid, rejected = transform_employees(employees)

        self.assertEqual(len(valid), 1)
        self.assertEqual(len(rejected), 2)
        self.assertEqual(rejected[0]["rejection_reasons"], ["first_name"])







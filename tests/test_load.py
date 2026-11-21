import unittest
from uuid import uuid4

from src.pipeline.load import load_employees
from src.database.connection import get_db_connection


class TestEmployeeLoading(unittest.TestCase):

    def test_load_prevents_duplicates(self):
        tenant_id = 999999
        employee_id = f"TEST-{uuid4().hex}"

        employee = {
            "employer_id": "TEST-COMPANY",
            "employee_id": employee_id,
            "person_id": "TEST-PERSON",
            "first_name": "Thabo",
            "last_name": "Mokoena",
            "sa_id_number": None,
            "bank_account_ref": None,
            "city": "Johannesburg",
            "phone_number": None,
            "is_active": True,
        }

        try:
            first_insert = load_employees([employee], tenant_id)
            second_insert = load_employees([employee], tenant_id)

            self.assertEqual(first_insert, 1)
            self.assertEqual(second_insert, 0)

        finally:
            with get_db_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        DELETE FROM employees
                        WHERE tenant_id = %s
                          AND employer_id = %s
                          AND employee_id = %s
                        """,
                        (tenant_id, "TEST-COMPANY", employee_id),
                    )


if __name__ == "__main__":
    unittest.main()
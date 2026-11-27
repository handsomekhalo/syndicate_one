import unittest
from uuid import uuid4

# from src.analysis import detect_shared_bank_accounts
from src.analysis.detection_rules import detect_shared_bank_accounts
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

    def test_detection_respects_tenant_isolation(self):
        tenant_a = 999999
        tenant_b = 999998
        suffix = uuid4().hex
        bank_ref = f"TEST-ACC-{suffix}"
        company_id = f"TEST-COMP-{suffix}"
        employee_id = f"TEST-EMP-{suffix}"
        vendor_id = f"TEST-VEN-{suffix}"
        registration_number = f"TEST-REGIST-{suffix}"
        is_active = True
        first_name = f"FIRST-NAME-{suffix}"
        last_name = f"LAST-NAME-{suffix}"
        vendor_status=True

        try:
            with get_db_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO companies (company_id, company_name, bank_account_ref, registration_number,is_active)
                        VALUES (%(company_id)s, %(company_name)s, %(bank_ref)s,%(registration_number)s,%(is_active)s)

                        """,
                        {"company_id": company_id,"company_name": f"TEST-COMPANY-{suffix}","bank_ref": bank_ref,
                         "registration_number": registration_number,"is_active":is_active
    },
                        
                    )
                    cursor.execute(
                        """
                        INSERT INTO employees (tenant_id, employer_id, employee_id, bank_account_ref,first_name,last_name,is_active)
                        VALUES (%(tenant)s, 'TEST-COMPANY', %(employee_id)s, %(bank_ref)s, %(first_name)s,%(last_name)s,%(is_active)s)
                        """,
                        {"tenant": tenant_a, "employee_id": employee_id, "bank_ref": bank_ref, "first_name": first_name,"last_name":last_name,"is_active":is_active},
                    )
                    cursor.execute(
                        """
                        INSERT INTO vendors (tenant_id, vendor_id, company_id, vendor_status)
                        VALUES (%(tenant)s, %(vendor_id)s, %(company_id)s, %(vendor_status)s)
                        """,
                        {"tenant": tenant_a, "vendor_id": vendor_id, "company_id": company_id,"vendor_status": vendor_status},
                    )

            # Connection block has exited, so the inserts are committed.
            findings_a = detect_shared_bank_accounts(tenant_a)
            findings_b = detect_shared_bank_accounts(tenant_b)

            self.assertEqual(len(findings_a), 1)
            self.assertEqual(findings_b, [])


        finally:
            with get_db_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        DELETE FROM vendors
                        WHERE tenant_id = %s AND vendor_id = %s AND company_id = %s
                        """,
                        (tenant_a, vendor_id, company_id),
                    )
                    cursor.execute(
                        "DELETE FROM companies WHERE company_id = %s",
                        (company_id,),
                    )
                    cursor.execute(
                        """
                        DELETE FROM employees
                        WHERE tenant_id = %s AND employee_id = %s
                        """,
                        (tenant_a, employee_id),
                    )


    if __name__ == "__main__":
        unittest.main()
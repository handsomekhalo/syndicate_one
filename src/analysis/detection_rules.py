

from src.database.connection import get_db_connection


def detect_shared_bank_accounts(tenant_id):
    query = """
        SELECT
            e.employee_id AS employee_id,
            c.company_id AS company_id,
            v.vendor_id AS vendor_id,
            TRIM(e.bank_account_ref) AS bank_account_ref
        FROM employees e
        JOIN companies c
            ON TRIM(e.bank_account_ref) = TRIM(c.bank_account_ref)
        JOIN vendors v
            ON c.company_id = v.company_id
        WHERE e.tenant_id = %(tenant_id)s
          AND v.tenant_id = %(tenant_id)s
          AND e.bank_account_ref IS NOT NULL
          AND TRIM(e.bank_account_ref) <> ''
          AND c.bank_account_ref IS NOT NULL
          AND TRIM(c.bank_account_ref) <> ''
    """
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, {"tenant_id": tenant_id})
            rows = cursor.fetchall()

    findings = []
    for row in rows:
        employee_id, company_id, vendor_id, bank_account_ref = row
        findings.append({
            "rule_code": "DR001",
            "employee_id": employee_id,
            "company_id": company_id,
            "vendor_id": vendor_id,
            "bank_account_ref": bank_account_ref,
            "reason": (
                f"Employee {employee_id}'s bank account reference ({bank_account_ref}) "
                f"matches company {company_id}, which is linked to vendor {vendor_id}."
            ),
        })

    return findings
            
           


if __name__ == "__main__":
    findings = detect_shared_bank_accounts(tenant_id=3)

    print("Detection results:")

    for finding in findings:
        print(finding)
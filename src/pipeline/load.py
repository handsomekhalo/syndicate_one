from src.database.connection import get_db_connection


def load_employees(employees, tenant_id):
    inserted_count = 0

    query = """
        INSERT INTO employees (
            tenant_id,
            employer_id,
            employee_id,
            person_id,
            first_name,
            last_name,
            sa_id_number,
            bank_account_ref,
            city,
            phone_number,
            is_active
        )
        VALUES (
            %(tenant_id)s,
            %(employer_id)s,
            %(employee_id)s,
            %(person_id)s,
            %(first_name)s,
            %(last_name)s,
            %(sa_id_number)s,
            %(bank_account_ref)s,
            %(city)s,
            %(phone_number)s,
            %(is_active)s
        )
        ON CONFLICT (tenant_id, employer_id, employee_id)
        DO NOTHING
        RETURNING id;
    """

    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            for employee in employees:
                record = employee.copy()

                # Tenant identity must come from trusted context,
                # not from the uploaded CSV.
                record["tenant_id"] = tenant_id

                cursor.execute(query, record)

                if cursor.fetchone() is not None:
                    inserted_count += 1

    return inserted_count
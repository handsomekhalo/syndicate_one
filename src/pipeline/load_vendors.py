from src.database.connection import get_db_connection


def load_vendors(vendors, tenant_id):
    inserted_count = 0

    query = """
        INSERT INTO vendors (
            tenant_id,
            vendor_id,
            company_id,
            vendor_status
        )
        VALUES (
            %(tenant_id)s,
            %(vendor_id)s,
            %(company_id)s,
            %(vendor_status)s
        )
        ON CONFLICT (tenant_id, vendor_id)
        DO NOTHING
        RETURNING id;
    """

    # Your task:
    # 1. Open the database connection and cursor.
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            for vendor in vendors:
                record = vendor.copy()
                record["tenant_id"] = tenant_id

                # value = str(record["vendor_status"]).strip().lower()
                record["vendor_status"] = str(record["vendor_status"]).strip().lower()
                if record["vendor_status"] not in ("active", "inactive"):
                    raise ValueError("Invalid vendor status")

                # Tenant identity must come from trusted context,
                # not from the uploaded CSV.
                # record["company_id"] = company_id

                cursor.execute(query, record)

                if cursor.fetchone() is not None:
                    inserted_count += 1


        return inserted_count
    # 2. Loop through vendors.
    # 3. Copy each vendor dictionary.
    # 4. Override tenant_id using the function argument.
    # 5. Execute the parameterized SQL query.
    # 6. Count successful insertions.


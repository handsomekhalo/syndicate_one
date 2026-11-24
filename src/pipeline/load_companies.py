from src.database.connection import get_db_connection


def load_companies(companies):
    inserted_count = 0



    query = """
        INSERT INTO companies (
            company_id,
            company_name,
            registration_number,
            city,
            is_active
        )
        VALUES (
            %(company_id)s,
            %(company_name)s,
            %(registration_number)s,
            %(city)s,
            %(is_active)s
        )
        ON CONFLICT (company_id)
        DO NOTHING
        RETURNING company_id;
    """

    # Your task: implement the database connection,
    # cursor, loop and inserted_count logic.
    
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            for company in companies:
                record = company.copy()

                value = str(record["is_active"]).strip().lower()
                if value in ("true", "yes", "1"):
                    record["is_active"] = True
                elif value in ("false", "no", "0"):
                    record["is_active"] = False
                else:
                    raise ValueError("Invalid company is_active value") 

                # Tenant identity must come from trusted context,
                # not from the uploaded CSV.
                # record["company_id"] = company_id

                cursor.execute(query, record)

                if cursor.fetchone() is not None:
                    inserted_count += 1


        return inserted_count
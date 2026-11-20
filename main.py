from src.pipeline.transform import clean_employee, convert_employee_types, get_missing_fields, has_required_fields, transform_employees
from src.pipeline.extract import extract_employees

from src.pipeline.extract import extract_employees
from src.pipeline.transform import transform_employees


def main():
    employees = extract_employees("data/synthetic/employees.csv")

    valid_employees, rejected_employees = transform_employees(employees)

    print("Total extracted:", len(employees))
    print("Valid employees:", len(valid_employees))
    print("Rejected employees:", len(rejected_employees))




from src.database.connection import get_db_connection


def test_database_connection():
    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT version();")
                result = cursor.fetchone()
                print("Database connected successfully!")
                print(result[0])

    except Exception as error:
        print(f"Database connection failed: {error}")


if __name__ == "__main__":
    main()
    test_database_connection()


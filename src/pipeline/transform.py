
required_fields = [
    "employee_id",
    "first_name",
    "last_name"
]

def has_required_fields(employee):
    for field in required_fields:
        if not employee.get(field, "").strip():
            return False

    return True


def transform_employees(employees):
    valid_employees = []
    rejected_employees = []


    for employee in employees:
        cleaned_employee = clean_employee(employee)

        try:
            converted_employee=convert_employee_types(cleaned_employee)

        except ValueError as error:
            cleaned_employee["rejection_reasons"] = [str(error)]
            rejected_employees.append(cleaned_employee)
            continue

        if has_required_fields(converted_employee):
            valid_employees.append(converted_employee)
        else:
            missing = get_missing_fields(converted_employee)
            converted_employee["rejection_reasons"] = missing
            rejected_employees.append(converted_employee)

        # if has_required_fields(cleaned_employee):
        #     valid_employees.append(cleaned_employee)
        # else:
        #     missing = get_missing_fields(cleaned_employee)
        #     # employee["rejection_reasons"] = missing
        #     cleaned_employee["rejection_reasons"] = missing
        #     rejected_employees.append(cleaned_employee)


    return valid_employees, rejected_employees

def get_missing_fields(employee):
    missing_fields = []

    for field in required_fields:
        if not employee.get(field, "").strip():
            missing_fields.append(field)
    return missing_fields


def clean_employee(raw_data):
    cleaned = raw_data.copy()
    cleaned["first_name"] = raw_data.get("first_name", "").strip().title()
    cleaned["last_name"] = raw_data.get("last_name", "").strip().title()
    cleaned["phone_number"]=raw_data.get("phone_number", "").replace(" ", "").strip()

    return cleaned

def convert_employee_types(employee):
    converted = employee.copy()

    converted["employee_id"] = int(employee["employee_id"])

    return converted


def convert_employee_types(employee):
    converted = employee.copy()

    value = str(employee.get("is_active", "")).strip().lower()

    if value in ("true", "yes", "1"):
        converted["is_active"] = True
    elif value in ("false", "no", "0"):
        converted["is_active"] = False
    else:
        raise ValueError("Invalid is_active value")


    return converted




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


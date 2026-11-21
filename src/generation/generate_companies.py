from faker import Faker

fake = Faker("en_GB")


def generate_company(company_id):
    return {
        "company_id": f"COMP-{company_id:04d}",
        "company_name": fake.company(),
        "registration_number": f"REG-{company_id:06d}",
        "city": fake.city(),
        "is_active": True,
    }


def generate_companies(count):
    companies = []

    for i in range(1, count + 1):
        companies.append(generate_company(i))

    return companies
from src.generation.generate_companies import generate_companies
from src.generation.generate_vendors import generate_vendors
from src.generation.export_csv import export_to_csv


def main():
    companies = generate_companies(5)
    vendors = generate_vendors(companies, tenant_id=3)

    export_to_csv(
        companies,
        "data/synthetic/companies.csv"
    )

    export_to_csv(
        vendors,
        "data/synthetic/vendors.csv"
    )

    print(f"Exported {len(companies)} companies")
    print(f"Exported {len(vendors)} vendors")


if __name__ == "__main__":
    main()
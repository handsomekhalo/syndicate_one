def generate_vendors(companies, tenant_id=3):
    vendors = []

    for index, company in enumerate(companies, start=1):
        vendor = {
            "vendor_id": f"VEN-{index:04d}",
            "tenant_id": tenant_id,
            "company_id": company["company_id"],
            "vendor_status": "active",
        }

        vendors.append(vendor)

    return vendors
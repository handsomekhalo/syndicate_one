CREATE TABLE IF NOT EXISTS companies (
    company_id TEXT PRIMARY KEY,
    company_name TEXT NOT NULL,
    registration_number TEXT NOT NULL UNIQUE,
    city TEXT,
    is_active BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS vendors (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    tenant_id BIGINT NOT NULL,
    vendor_id TEXT NOT NULL,
    company_id TEXT NOT NULL,
    vendor_status TEXT NOT NULL,

    CONSTRAINT fk_vendor_company
        FOREIGN KEY (company_id)
        REFERENCES companies(company_id),

    CONSTRAINT unique_tenant_vendor
        UNIQUE (tenant_id, vendor_id),

    CONSTRAINT unique_tenant_company_vendor
        UNIQUE (tenant_id, company_id)
);
CREATE TABLE IF NOT EXISTS employees (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    tenant_id BIGINT NOT NULL,
    employer_id TEXT NOT NULL,
    employee_id TEXT NOT NULL,
    person_id TEXT,

    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    sa_id_number TEXT,
    bank_account_ref TEXT,
    city TEXT,
    phone_number TEXT,

    is_active BOOLEAN NOT NULL,

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT unique_tenant_employee
        UNIQUE (tenant_id, employer_id, employee_id)
);
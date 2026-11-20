### 1. Synthetic Data Generation
- Built a Python employee data generator using Faker.
- Implemented sequential employee and person identifiers.
- Generated synthetic names, phone numbers, cities and fictional bank account references.
- Implemented CSV export to `data/synthetic/employees.csv`.

### 2. ETL Pipeline — Extraction
- Implemented CSV ingestion using `csv.DictReader`.
- Designed extraction to accept different file paths, laying the foundation for external company uploads.

### 3. ETL Pipeline — Transformation
- Implemented employee name and phone number normalization.
- Added required-field validation.
- Separated valid and rejected employee records.
- Implemented rejection reasons identifying missing fields.
- Integrated cleaning and validation into the transformation workflow.

### 4. Automated Unit Testing
Implemented three tests using Python's `unittest` framework:

- `test_clean_employee`
- `test_get_missing_fields`
- `test_transform_employees`

**Result: 3 tests passed successfully.**

### 5. Version Control
- Initialized a Git repository.
- Established `dev` and `main` branches.
- Planned GitHub Actions integration for automated testing and future CI/CD.

### 6. Current Development Stage
**Phase 2: ETL Pipeline — In Progress**

Completed: Synthetic employee generation, CSV extraction, basic cleaning, required-field validation and initial unit tests.

Currently working on: Data type conversion and identifier validation.

Next milestones: Additional validation, PostgreSQL loading, company/vendor datasets and relationship analysis.

**Project objective:** Develop a multi-tenant data engineering platform capable of identifying potential procurement irregularities, conflicts of interest and suspicious financial relationships through data processing and relationship analysis.
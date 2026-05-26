# Design Decisions

This file records the current project decisions. Keep it concise and update it when architecture-shaping choices change.

## Project Identity

- Project name: Staylytics
- Python package: `staylytics`
- LeaseFlow is unrelated and must not be used for this repository.

## MVP Scope

The MVP is local-first and CLI-first.

Included:

- CSV imports from Airbnb, Booking.com, and a custom direct booking format
- SQLite persistence
- row-level idempotency
- anonymized source identifiers
- CLI reports

Deferred:

- FastAPI
- frontend
- Azure/Terraform
- GitHub Actions
- forecasting
- Databricks
- tax/accounting logic
- payout reconciliation
- machine learning

## Tooling

- Python 3.12
- `uv` for dependency management
- pandas for CSV parsing
- SQLAlchemy Core for database access
- Typer for CLI
- pytest for tests
- ruff for linting and formatting
- mypy is deferred

## Import Strategy

- Imports start through CLI.
- Later FastAPI imports must call the same import service logic.
- `--dry-run` validates and compares rows without writing to the database.
- Airbnb property mapping uses `Listing`/`Kohde` aliases from `config/properties.yml`.
- Booking.com imports require `--property`.
- Direct booking CSV files include a required `property_slug` column.

## Privacy

- Raw CSV rows are not stored.
- Guest names, emails, phone numbers, IBANs, and free-text notes are not stored.
- Source reservation identifiers are stored only as HMAC-SHA256 hashes.
- `STAYLYTICS_HASH_SECRET` is required for imports.
- Import errors may store safe field values such as an unknown Airbnb listing alias, but never full raw rows.

## Idempotency

- Idempotency is row-level, not file-level.
- `dedupe_key` prevents duplicate rows.
- `content_hash` separates unchanged rows from updated rows.
- Re-importing overlapping files is expected and must not duplicate data.

## Data Model

MVP tables:

- `properties`
- `imports`
- `import_errors`
- `stays`
- `financial_transactions`

Money is stored as integer cents. CLI and CSV reports display euro values with two decimals.

## Reporting

Initial reports:

- `monthly_revenue`
- `platform_summary`

The primary revenue metric is `net_revenue`.

## Revenue Allocation

- Revenue is allocated by nights across calendar months.
- Adjustment rows are also split by nights when stay dates are available.
- Otherwise, adjustment rows use their allocation month, such as Booking.com payout date.
- Rounding differences are assigned to the final month in the split.


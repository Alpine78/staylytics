# Staylytics

Staylytics is a local-first ETL and analytics project for short-term rental data.

The MVP imports Airbnb, Booking.com, and direct booking CSV files, normalizes the data, anonymizes source identifiers, stores the result in SQLite, and produces CLI reports.

## MVP Scope

Included first:

- CLI imports
- source detection
- property mapping from `config/properties.yml`
- row-level deduplication
- SQLite storage
- monthly revenue and platform summary reports

Deferred:

- FastAPI
- frontend
- Azure and Terraform
- GitHub Actions
- tax/accounting logic
- payout reconciliation
- forecasting
- machine learning

## Setup

Requires Python 3.12 and `uv`.

```bash
# What it does: Installs project and development dependencies.
# Target filename/service: local Python environment
uv sync --dev
```

Create a local `.env` file from `.env.example` and set `STAYLYTICS_HASH_SECRET` before running imports.

## Planned CLI

```bash
# What it does: Initializes the local SQLite database.
# Target filename/service: Staylytics CLI
uv run staylytics init-db

# What it does: Validates and imports a CSV file.
# Target filename/service: Staylytics CLI
uv run staylytics import --file path/to/export.csv --property vaajalahti

# What it does: Validates a CSV import without writing to the database.
# Target filename/service: Staylytics CLI
uv run staylytics import --file path/to/export.csv --property vaajalahti --dry-run

# What it does: Produces a monthly revenue report.
# Target filename/service: Staylytics CLI
uv run staylytics report monthly-revenue
```

The CLI commands are planned, but not implemented yet. The first implementation steps should be written manually in small reviewable increments.

## Data Safety

Do not commit real Airbnb or Booking.com exports.

Local raw data, reports, `.env` files, and SQLite databases are ignored by Git. Test fixtures must be synthetic or manually anonymized.

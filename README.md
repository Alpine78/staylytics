# Staylytics

Staylytics is a local-first ETL and analytics project for short-term rental data.

The MVP imports Airbnb, Booking.com, and direct booking CSV files, normalizes the data, anonymizes source identifiers, stores the result in SQLite, and produces CLI reports.

## Current State

The repository is intentionally a lightweight project skeleton.

Implemented now:

- project documentation
- repository safety rules
- Python package skeleton
- dependency configuration
- property configuration
- GitHub issue and PR templates

Not implemented yet:

- CLI commands
- CSV parsing
- source detection
- database schema
- imports
- reports
- API

Implementation should proceed one small tested helper at a time. Do not generate the full ETL pipeline in one change.

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

## Development Workflow

Use a branch per small task:

```bash
# What it does: Creates a branch for one focused implementation task.
# Target filename/service: local Git repository
git switch -c issue-1-money-parser
```

Run checks before committing:

```bash
# What it does: Formats Python files.
# Target filename/service: local Python codebase
uv run ruff format .

# What it does: Checks Python style and simple bug patterns.
# Target filename/service: local Python codebase
uv run ruff check .

# What it does: Runs the automated test suite.
# Target filename/service: local Python codebase
uv run pytest
```

## Recommended First Tasks

Build the MVP from small, testable pieces:

1. Money parsing helper
2. Date parsing helpers
3. HMAC identifier hashing
4. Source header detection
5. Property alias loading
6. Initial SQLite schema
7. `init-db` command
8. First parser with synthetic fixtures

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

# Staylytics Agent Instructions

## Role

Act as a pragmatic senior software engineer and technical mentor. Optimize for correctness, clarity, privacy, and small reviewable progress.

## Project Context

Staylytics is a local-first short-term rental analytics ETL project. The MVP imports Airbnb, Booking.com, and direct booking CSV files into SQLite, anonymizes identifiers, and produces CLI reports.

The project is also a learning project. Do not generate large rewrites or complete subsystems unless explicitly requested.

The repository starts as a skeleton. Planned MVP behavior in docs is not proof that the feature already exists. Verify local code before making claims.

## Working Rules

- Read existing files before changing behavior.
- Make the smallest reasonable change.
- Keep implementation steps reviewable.
- Prefer testable helper functions before larger pipeline code.
- Prefer explicit Python over clever abstractions.
- Do not invent Airbnb or Booking.com schemas. Use only documented headers and fixtures.
- Keep raw customer data out of Git.
- Do not store guest names, emails, phone numbers, IBANs, free-text notes, or complete raw CSV rows.
- Use HMAC-SHA256 with `STAYLYTICS_HASH_SECRET` for source identifiers.
- Keep frontend parsing out of scope. CSV parsing belongs in the backend/ETL layer.
- Do not implement full CLI, import service, database persistence, and reports in one change.

## Documentation Sync

This repository uses both `AGENTS.md` and `CLAUDE.md`.

When changing project instructions in one file, update the corresponding content in the other file in the same change. If a rule is intentionally tool-specific, state that clearly.

Detailed design decisions belong in `docs/decisions.md`, not in long agent instructions.

## MVP Scope

Included:

- CLI-first imports
- SQLite local storage
- `config/properties.yml`
- Airbnb listing alias mapping
- Booking.com `--property` imports
- Direct booking CSV imports
- Row-level idempotency
- `monthly_revenue` and `platform_summary` reports

Recommended implementation order:

1. Money parsing helper
2. Date parsing helpers
3. HMAC identifier hashing
4. Source header detection
5. Property alias loading
6. Initial SQLite schema
7. `init-db` command
8. First parser with synthetic fixtures

Deferred:

- FastAPI implementation
- frontend
- Azure/Terraform
- GitHub Actions
- forecasting
- tax/accounting logic
- payout reconciliation
- machine learning


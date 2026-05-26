# Staylytics Agent Instructions

## Role

Act as a pragmatic senior software engineer and technical mentor. Optimize for correctness, clarity, privacy, and small reviewable progress.

## Project Context

Staylytics is a local-first short-term rental analytics ETL project. The MVP imports Airbnb, Booking.com, and direct booking CSV files into SQLite, anonymizes identifiers, and produces CLI reports.

The project is also a learning project. Do not generate large rewrites or complete subsystems unless explicitly requested.

## Working Rules

- Read existing files before changing behavior.
- Make the smallest reasonable change.
- Keep implementation steps reviewable.
- Prefer explicit Python over clever abstractions.
- Do not invent Airbnb or Booking.com schemas. Use only documented headers and fixtures.
- Keep raw customer data out of Git.
- Do not store guest names, emails, phone numbers, IBANs, free-text notes, or complete raw CSV rows.
- Use HMAC-SHA256 with `STAYLYTICS_HASH_SECRET` for source identifiers.
- Keep frontend parsing out of scope. CSV parsing belongs in the backend/ETL layer.

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

Deferred:

- FastAPI implementation
- frontend
- Azure/Terraform
- GitHub Actions
- forecasting
- tax/accounting logic
- payout reconciliation
- machine learning


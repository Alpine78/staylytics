# Privacy

Staylytics handles rental platform exports that may contain personal data. The MVP minimizes stored data.

## Rules

- Do not commit real raw CSV files.
- Do not store guest names.
- Do not store emails or phone numbers.
- Do not store IBANs.
- Do not store free-text notes or Airbnb `Details`.
- Do not store complete raw CSV rows.
- Do not expose personal data in CLI output, reports, import errors, or future APIs.

## Identifier Hashing

Reservation identifiers, confirmation codes, booking numbers, payout IDs, and direct external references are stored only as HMAC-SHA256 hashes.

The local secret is read from:

```text
STAYLYTICS_HASH_SECRET
```

Imports must fail if the secret is missing. The application must not generate a new secret automatically, because that would break idempotency across import runs.

## Git Hygiene

Ignored:

- `.env`
- `data/raw/`
- local SQLite databases
- generated reports

Allowed:

- synthetic fixtures in `tests/fixtures/`
- manually anonymized examples with fake identifiers

## Import Errors

`import_errors` may include safe diagnostic values, such as an unknown Airbnb listing alias. It must not include full raw rows or personal-data fields.

## Tax and Accounting

Staylytics is an operational analytics project. It is not a bookkeeping, VAT, or tax filing system.


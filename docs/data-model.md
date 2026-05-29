# Data Model

Staylytics separates stays from financial transactions.

This document describes the planned MVP data model. The database schema is not implemented in the initial skeleton.

## Core Tables

### properties

Represents an internal rental property.

Important fields:

- `slug`: stable technical identifier
- `name`: display name
- `city`
- `active`
- `active_from`
- `active_until`

`slug` must remain stable even if the display name or platform listing name changes.

### imports

Represents one import run.

Important fields:

- source platform
- source file basename
- source file hash
- encoding
- row counters
- status
- processed timestamp

The same file may be imported multiple times. Row-level idempotency prevents duplication.

### import_errors

Stores safe row-level validation errors.

It may store safe values required for debugging, such as an unknown Airbnb listing alias. It must not store guest data, IBANs, full raw CSV rows, or free-text details.

### stays

Represents booking/stay periods used for occupancy and nights.

Important fields:

- source platform
- property
- reservation identifier hash
- dedupe key
- content hash
- booking date, nullable
- check-in date
- check-out date
- nights
- normalized status
- source status
- last import id

`no_show` counts toward booked occupancy in the MVP.

### financial_transactions

Represents revenue-impacting rows.

Important fields:

- source platform
- property
- optional stay link
- source reference hash
- payout id hash, nullable
- dedupe key
- content hash
- transaction type
- source type
- transaction date
- allocation month
- allocation method
- gross amount cents, nullable
- fee cents, nullable
- net revenue cents
- currency
- payment status, nullable

Revenue reports use `financial_transactions`, not `stays`.

## Source Handling

### Airbnb

Handled row types:

- `Reservation`: creates a stay and a financial transaction
- `Adjustment`: creates only a financial transaction
- `Resolution Adjustment`: creates only a financial transaction
- `Payout`: skipped in the MVP

`Details` is ignored and never stored.

Airbnb `Paid out` is treated as `net_revenue`. Airbnb `gross_amount` is not inferred because the CSV does not contain the guest-paid total. Airbnb `Service fee` is stored as the actual CSV value; it is not calculated from Airbnb fee percentage rules.

`Cleaning fee` is ignored in the MVP. It has not been used in the current business context.

### Booking.com

Handled row types:

- `Reservation`: creates a stay and a financial transaction
- `Commission adjustment`: creates only a financial transaction

Booking.com `Net` is treated as `net_revenue`. `Commission` and `Payments Service Fee` are stored as positive fee costs.

`no_show` counts toward revenue and booked occupancy when the row contains a revenue amount.

### Direct

Direct bookings use a custom CSV format:

```csv
property_slug,booking_date,check_in_date,check_out_date,gross_amount,fee_amount,net_revenue,currency,status,external_reference
```

Rules:

- `property_slug` is required.
- `booking_date` is nullable.
- `fee_amount` is a positive cost. Empty means zero.
- If `net_revenue` is empty, it is calculated as `gross_amount - fee_amount`.
- If `net_revenue` is provided, it must match `gross_amount - fee_amount` within one cent.
- `external_reference` is hashed and not stored raw.
- Personal data is not allowed in the direct CSV format.

## Currency

The MVP supports only `EUR`. Other currencies fail with `unsupported_currency`.

Bitcoin and other currencies are deferred because they require separate precision, exchange-rate, and reporting decisions.


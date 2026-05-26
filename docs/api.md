# API Plan

The MVP is CLI-first. FastAPI is deferred until local imports and reports work.

The future API should reuse the same import and report service logic as the CLI.

## Planned Principles

- JSON responses
- versioned routes under `/api/v1`
- backend handles CSV parsing and source detection
- frontend must not parse Airbnb or Booking.com CSV files
- no authentication in the first local MVP
- API key or stronger authentication later

## Candidate Endpoints

```text
GET  /health
POST /api/v1/imports
GET  /api/v1/imports
GET  /api/v1/imports/{id}
GET  /api/v1/properties
GET  /api/v1/stays
GET  /api/v1/reports/monthly-revenue
GET  /api/v1/reports/platform-summary
```

OpenAPI is intentionally deferred until the import and report behavior is stable.


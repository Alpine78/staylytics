# Future Azure Plan

Azure and Terraform are deferred until the local CLI MVP works.

No Azure or Terraform code should be added while the project is still in the local skeleton and early ETL helper phase.

## Candidate Azure Architecture

```text
CSV upload
-> Azure Blob Storage
-> ETL worker
-> database
-> API
-> frontend or BI tool
```

## Candidate Services

- Azure Blob Storage for raw and processed files
- Azure SQL or PostgreSQL for relational storage
- Azure Functions or Azure Container Apps for API/ETL hosting
- Terraform for provisioning

## Deferred Decisions

- Azure SQL vs PostgreSQL
- Functions vs Container Apps
- API authentication model
- private networking and secrets management
- CI/CD deployment flow

## Current Rule

Do not add Azure infrastructure code before the local import, persistence, and reporting flow is working and tested.


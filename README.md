# CSV Schema Validator

A dependency-free Python CLI for checking CSV files before ingestion.

## Usage

```bash
python src/validate_csv.py orders.csv --required order_id amount
```

The command prints the row count and any missing required columns, returning exit code 1 if a column is missing. Python 3.10+; no packages required.

This starter utility validates headers, not field types, duplicate rows, or business rules. Extend it with your own validation policies before deploying in a pipeline.

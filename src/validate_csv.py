"""Validate CSV headers and required columns using the Python standard library."""
import argparse
import csv
from pathlib import Path


def validate(path: Path, required: list[str]) -> tuple[int, list[str]]:
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        headers = reader.fieldnames or []
        missing = sorted(set(required) - set(headers))
        count = sum(1 for _ in reader)
    return count, missing


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--required", nargs="+", default=[])
    options = parser.parse_args()
    rows, missing_cols = validate(options.csv_file, options.required)
    print(f"Rows: {rows}, missing columns: {missing_cols}")
    if missing_cols:
        raise SystemExit(1)

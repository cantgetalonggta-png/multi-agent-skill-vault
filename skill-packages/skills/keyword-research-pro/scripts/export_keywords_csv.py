#!/usr/bin/env python3
"""Simple CSV exporter for keyword tables.
Usage: python export_keywords_csv.py --input data.json --output keywords.csv
Expects a list of dicts with consistent keys.
"""

import argparse
import csv
import json
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data:
        print("Empty data", file=sys.stderr)
        sys.exit(1)

    fieldnames = list(data[0].keys())
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Wrote {len(data)} rows to {args.output}")

if __name__ == "__main__":
    main()

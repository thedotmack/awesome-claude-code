#!/usr/bin/env python3
"""
Sort THE_RESOURCES_TABLE.csv by category, sub-category, and display name.

This utility ensures resources are properly ordered for consistent presentation
in the generated README and other outputs.
"""

import csv
import sys
from pathlib import Path


def sort_resources(csv_path: Path) -> None:
    """Sort resources in the CSV file by category, sub-category, and display name."""
    # Read the CSV data
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        rows = list(reader)

    # Sort the rows
    # First by Category, then by Sub-Category (empty values last), then by Display Name
    sorted_rows = sorted(
        rows,
        key=lambda row: (
            row.get("Category", ""),
            row.get("Sub-Category", "") or "zzz",  # Empty sub-categories sort last
            row.get("Display Name", "").lower(),
        ),
    )

    # Write the sorted data back
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        if headers:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(sorted_rows)

    print(f"✓ Sorted {len(sorted_rows)} resources in {csv_path}")

    # Print summary of categories
    categories = {}
    for row in sorted_rows:
        cat = row.get("Category", "Unknown")
        subcat = row.get("Sub-Category", "") or "None"
        if cat not in categories:
            categories[cat] = {}
        if subcat not in categories[cat]:
            categories[cat][subcat] = 0
        categories[cat][subcat] += 1

    print("\nCategory Summary:")
    for cat in sorted(categories.keys()):
        print(f"  {cat}:")
        for subcat in sorted(categories[cat].keys()):
            count = categories[cat][subcat]
            if subcat == "None":
                print(f"    (no sub-category): {count} items")
            else:
                print(f"    {subcat}: {count} items")


def main():
    """Main entry point."""
    # Default to THE_RESOURCES_TABLE.csv in parent directory
    csv_path = Path(__file__).parent.parent / "THE_RESOURCES_TABLE.csv"

    if len(sys.argv) > 1:
        csv_path = Path(sys.argv[1])

    if not csv_path.exists():
        print(f"Error: CSV file not found at {csv_path}", file=sys.stderr)
        sys.exit(1)

    sort_resources(csv_path)


if __name__ == "__main__":
    main()

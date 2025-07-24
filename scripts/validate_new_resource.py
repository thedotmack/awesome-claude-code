#!/usr/bin/env python3
"""
Validate only the newest resource added to THE_RESOURCES_TABLE.csv.

This script identifies new resources by checking git diff for both uncommitted
and committed changes, then validates only the newest addition.
"""

import csv
import io
import os
import subprocess
import sys
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import validation functions from validate_links
try:
    from validate_links import (  # type: ignore[import-not-found]
        ACTIVE_HEADER_NAME,
        ID_HEADER_NAME,
        LAST_CHECKED_HEADER_NAME,
        LAST_MODIFIED_HEADER_NAME,
        LICENSE_HEADER_NAME,
        PRIMARY_LINK_HEADER_NAME,
        SECONDARY_LINK_HEADER_NAME,
        apply_overrides,
        load_overrides,
        validate_url,
    )
except ImportError:
    print("Error: Could not import from validate_links.py")
    sys.exit(1)

CSV_FILE = "THE_RESOURCES_TABLE.csv"


def run_git_command(cmd: list[str]) -> tuple[bool, str]:
    """Run a git command and return success status and output."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return result.returncode == 0, result.stdout
    except Exception as e:
        return False, str(e)


def get_csv_headers() -> list[str] | None:
    """Get CSV headers from the current file."""
    if not os.path.exists(CSV_FILE):
        return None

    with open(CSV_FILE, encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            return next(reader)
        except StopIteration:
            return None


def parse_csv_line(line: str, headers: list[str]) -> dict[str, str] | None:
    """Parse a CSV line into a dictionary using the provided headers."""
    try:
        # Use csv.reader to properly handle quoted fields
        reader = csv.reader(io.StringIO(line))
        values = next(reader)

        if len(values) != len(headers):
            return None

        return dict(zip(headers, values, strict=False))
    except Exception:
        return None


def get_added_resources() -> list[dict[str, str]]:
    """Get all resources added in uncommitted changes or the last commit."""
    added_resources = []
    headers = get_csv_headers()

    if not headers:
        print("Error: Could not read CSV headers")
        return []

    # Check uncommitted changes
    success, diff_output = run_git_command(["git", "diff", CSV_FILE])
    if success and diff_output:
        print("Checking uncommitted changes...")
        resources = parse_diff_for_additions(diff_output, headers)
        if resources:
            print(f"Found {len(resources)} new resource(s) in uncommitted changes")
            added_resources.extend(resources)

    # Check last commit if no uncommitted additions found
    if not added_resources:
        success, diff_output = run_git_command(["git", "diff", "HEAD~1", "HEAD", CSV_FILE])
        if success and diff_output:
            print("Checking last commit...")
            resources = parse_diff_for_additions(diff_output, headers)
            if resources:
                print(f"Found {len(resources)} new resource(s) in last commit")
                added_resources.extend(resources)

    return added_resources


def parse_diff_for_additions(diff_output: str, headers: list[str]) -> list[dict[str, str]]:
    """Parse git diff output and extract added CSV rows."""
    added_resources = []

    for line in diff_output.splitlines():
        # Look for added lines (start with +)
        if not line.startswith("+"):
            continue

        # Skip the +++ header line
        if line.startswith("+++"):
            continue

        # Remove the + prefix
        csv_line = line[1:]

        # Skip if this looks like the header row
        if csv_line.startswith(headers[0]):
            continue

        # Try to parse as CSV
        resource = parse_csv_line(csv_line, headers)
        if resource and resource.get(ID_HEADER_NAME):  # Ensure it has an ID
            added_resources.append(resource)

    return added_resources


def find_newest_resource(resources: list[dict[str, str]]) -> dict[str, str] | None:
    """Find the newest resource from a list of resources."""
    if not resources:
        return None

    # If only one resource, return it
    if len(resources) == 1:
        return resources[0]

    # Sort by ID (newest IDs are typically higher) and take the last one
    try:
        sorted_resources = sorted(resources, key=lambda r: r.get(ID_HEADER_NAME, ""))
        return sorted_resources[-1]
    except Exception:
        # If sorting fails, just return the last one in the list
        return resources[-1]


def validate_and_update_resource(resource: dict[str, str]) -> bool:
    """Validate the resource and update the CSV file."""
    print(f"\nValidating resource: {resource.get('Display Name', 'Unknown')}")
    print(f"ID: {resource.get(ID_HEADER_NAME, 'Unknown')}")
    print(f"Primary URL: {resource.get(PRIMARY_LINK_HEADER_NAME, 'None')}")

    # Load overrides
    overrides = load_overrides()

    # Apply overrides
    resource, locked_fields = apply_overrides(resource, overrides)

    if locked_fields:
        print(f"Fields locked by override: {', '.join(locked_fields)}")

    # Skip validation if active and last_checked are locked
    if "active" in locked_fields and "last_checked" in locked_fields:
        print("Skipping validation - fields locked by override")
        return True

    # Validate primary URL
    primary_url = resource.get(PRIMARY_LINK_HEADER_NAME, "").strip()
    primary_valid, primary_status, license_info, last_modified = validate_url(primary_url)

    # Update fields based on validation
    if "license" not in locked_fields and license_info and license_info != "NOT_FOUND":
        resource[LICENSE_HEADER_NAME] = license_info
        print(f"✓ Found license: {license_info}")

    if "last_modified" not in locked_fields and last_modified:
        resource[LAST_MODIFIED_HEADER_NAME] = last_modified
        print(f"✓ Found last modified: {last_modified}")

    # Validate secondary URL if present
    secondary_url = resource.get(SECONDARY_LINK_HEADER_NAME, "").strip()
    secondary_valid = True
    if secondary_url:
        secondary_valid, secondary_status, _, _ = validate_url(secondary_url)
        if not secondary_valid:
            print(f"✗ Secondary URL validation failed: {secondary_status}")

    # Update active status
    if "active" not in locked_fields:
        is_active = primary_valid and secondary_valid
        resource[ACTIVE_HEADER_NAME] = "TRUE" if is_active else "FALSE"

        if is_active:
            print("✓ Resource is valid and active")
        else:
            print(f"✗ Resource validation failed: {primary_status}")

    # Update last checked timestamp
    if "last_checked" not in locked_fields:
        resource[LAST_CHECKED_HEADER_NAME] = datetime.now().strftime("%Y-%m-%d:%H-%M-%S")

    # Update the CSV file
    return update_csv_file(resource)


def update_csv_file(updated_resource: dict[str, str]) -> bool:
    """Update the CSV file with the validated resource data."""
    try:
        # Read all rows
        with open(CSV_FILE, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            fieldnames = reader.fieldnames

        if not fieldnames:
            print("Error: Could not read CSV fieldnames")
            return False

        # Find and update the matching row
        resource_id = updated_resource.get(ID_HEADER_NAME)
        updated = False

        for i, row in enumerate(rows):
            if row.get(ID_HEADER_NAME) == resource_id:
                # Update the row with validated data
                rows[i].update(updated_resource)
                updated = True
                break

        if not updated:
            print(f"Warning: Could not find resource with ID {resource_id} in CSV")
            return False

        # Write back to CSV
        with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"\n✓ Updated {CSV_FILE} successfully")
        return True

    except Exception as e:
        print(f"Error updating CSV file: {e}")
        return False


def main():
    """Main entry point."""
    # Check if we're in a git repository
    success, _ = run_git_command(["git", "rev-parse", "--git-dir"])
    if not success:
        print("Error: Not in a git repository")
        sys.exit(1)

    # Check if CSV file exists
    if not os.path.exists(CSV_FILE):
        print(f"Error: {CSV_FILE} not found")
        sys.exit(1)

    # Get added resources
    added_resources = get_added_resources()

    if not added_resources:
        print("No new resources found in uncommitted changes or last commit")
        sys.exit(0)

    # Find the newest resource
    newest_resource = find_newest_resource(added_resources)

    if not newest_resource:
        print("Error: Could not identify newest resource")
        sys.exit(1)

    # Validate and update the resource
    success = validate_and_update_resource(newest_resource)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

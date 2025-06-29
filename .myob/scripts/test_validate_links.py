import csv
import os
import sys
from datetime import datetime

from validate_links import ACTIVE_HEADER_NAME, PRIMARY_LINK_HEADER_NAME, SECONDARY_LINK_HEADER_NAME, check_link_is_valid


def run_validation_test():
    """
    Run validation test on the predefined test CSV file.
    """
    print("=== Link Validation Test ===")
    print(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    test_csv_path = os.path.join(os.path.dirname(__file__), "resource-metadata.test.csv")

    if not os.path.exists(test_csv_path):
        print(f"Error: Test CSV file not found at {test_csv_path}")
        return None

    print(f"\nUsing test CSV: {test_csv_path}")

    # Read test CSV and backup original data
    test_rows = []
    original_rows = []
    with open(test_csv_path, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)
        test_rows.append(headers)
        original_rows.append(headers[:])  # Deep copy of headers

        for row in reader:
            test_rows.append(row)
            original_rows.append(row[:])  # Deep copy of each row

    print(f"Test data contains {len(test_rows)-1} resources:")

    # Display test resources
    headers = test_rows[0]
    primary_link_index = headers.index(PRIMARY_LINK_HEADER_NAME)
    secondary_link_index = headers.index(SECONDARY_LINK_HEADER_NAME)
    active_index = headers.index(ACTIVE_HEADER_NAME)

    for i, row in enumerate(test_rows[1:], 1):
        url = (
            row[primary_link_index].strip()
            if primary_link_index < len(row)
            else (row[secondary_link_index].strip() if secondary_link_index < len(row) else "")
        )
        status = row[active_index] if active_index < len(row) else "UNKNOWN"
        print(f"  {i}. {row[0]} (Current: {status})")
        print(f"     URL: {url}")

    print("\n--- Running Validation ---")

    # Test each resource individually
    results = []
    for i, row in enumerate(test_rows[1:], 1):
        url = (
            row[primary_link_index].strip()
            if primary_link_index < len(row)
            else (row[secondary_link_index].strip() if secondary_link_index < len(row) else "")
        )
        original_status = row[active_index] if active_index < len(row) else "UNKNOWN"

        if url:
            print(f"\n[{i}] Testing: {row[0]}")
            print(f"    URL: {url}")
            print(f"    Original Status: {original_status}")

            # Run validation
            is_active, status_info = check_link_is_valid(url, quiet=True)
            new_status = "TRUE" if is_active else "FALSE"

            print(f"    Validation Result: {new_status} (Status: {status_info})")

            results.append(
                {
                    "name": row[0],
                    "url": url,
                    "original_status": original_status,
                    "new_status": new_status,
                    "status_info": status_info,
                    "changed": original_status != new_status,
                }
            )
        else:
            print(f"\n[{i}] Skipping {row[0]} - No URL found")
            results.append(
                {
                    "name": row[0],
                    "url": "",
                    "original_status": original_status,
                    "new_status": "FALSE",
                    "status_info": "No URL",
                    "changed": original_status != "FALSE",
                }
            )

    # Summary
    print("\n=== Test Results Summary ===")
    changed_count = sum(1 for r in results if r["changed"])
    print(f"Total resources tested: {len(results)}")
    print(f"Status changes: {changed_count}")

    if changed_count > 0:
        print("\nResources with status changes:")
        for result in results:
            if result["changed"]:
                print(f"  • {result['name']}: {result['original_status']} → {result['new_status']}")
                print(f"    Reason: {result['status_info']}")

    print("\nDetailed Results:")
    for result in results:
        status_icon = "✅" if result["new_status"] == "TRUE" else "❌"
        change_icon = " (CHANGED)" if result["changed"] else ""
        print(f"  {status_icon} {result['name']}: {result['new_status']}{change_icon}")
        if result["url"]:
            print(f"     URL: {result['url']}")
        print(f"     Status Info: {result['status_info']}")

    # Cleanup: restore original CSV file
    print("\n--- Cleanup ---")
    print("Restoring original test CSV file...")
    with open(test_csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(original_rows)
    print("✅ Test CSV restored to original state")

    return results


if __name__ == "__main__":
    try:
        results = run_validation_test()
        print(f"\nTest completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"Test failed with error: {e}")
        sys.exit(1)

"""
Link validation script for the Awesome Claude Code repository that ensures
all resource URLs are accessible and updates the CSV with current status.

How it works:
1. Reads resource-metadata.csv to extract Primary/Secondary Link URLs
2. Validates each URL using HTTP requests (HEAD for regular URLs, GET for GitHub API)
3. Handles GitHub repository URLs by converting them to GitHub API endpoints
4. Implements exponential backoff retry logic for rate limiting and temporary failures
5. Updates CSV with Active status (TRUE/FALSE) and Last Checked timestamp
6. Provides detailed logging and summary of broken links
7. Supports GitHub Action mode for CI/CD integration with JSON output
"""

import argparse
import csv
import json
import random
import re
import sys
import time
from datetime import datetime

import requests

USER_AGENT = "awesome-claude-code Link Validator/1.0"
INPUT_FILE = ".myob/scripts/resource-metadata.csv"
OUTPUT_FILE = ".myob/scripts/resource-metadata.csv"
PRIMARY_LINK_HEADER_NAME = "Primary Link"
SECONDARY_LINK_HEADER_NAME = "Secondary Link"
ACTIVE_HEADER_NAME = "Active"
LAST_CHECKED_HEADER_NAME = "Last Checked"
HEADERS = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"}
PRINT_FILE = None


def parse_github_url(url):
    """
    Parse GitHub URL and return API endpoint if it's a GitHub repository content URL.
    Returns (api_url, is_github) tuple.
    """
    github_pattern = r"https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)"
    match = re.match(github_pattern, url)

    if match:
        owner, repo, branch, path = match.groups()
        api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}"
        return api_url, True

    return url, False


def check_link_is_valid(url, retry_count=0, max_retries=3, quiet=False):
    """
    Check if a URL returns a 40x status code with rate limiting and retry logic.
    Uses GitHub API for GitHub repository content URLs.
    Returns tuple (is_active, status_code/error_message)
    """
    try:
        # Check if this is a GitHub URL and convert to API endpoint
        api_url, is_github = parse_github_url(url)

        if is_github:
            # Use GET for GitHub API (HEAD not supported)
            response = requests.get(api_url, timeout=15, headers=HEADERS, allow_redirects=True)
        else:
            # Use HEAD for non-GitHub URLs
            response = requests.head(url, timeout=15, headers=HEADERS, allow_redirects=True)

        if response.status_code == 404:
            # If the link is 404, we can return immediately
            if not quiet:
                print(f"  ❌ BROKEN: {url} - Status: {response.status_code}", file=PRINT_FILE)
            return False, response.status_code

        # Handle rate limiting (429 Too Many Requests)
        if response.status_code == 429:
            raise requests.exceptions.HTTPError(f"Rate limited: {url} - Status: {response.status_code}")

        # Check if status code is in 40x range
        if 400 <= response.status_code < 500:
            raise requests.exceptions.HTTPError(f"Client error: {url} - Status: {response.status_code}")

        return True, response.status_code

    except Exception as e:
        if retry_count < max_retries:
            wait_time = (2**retry_count) + random.uniform(1, 2)
            if not quiet:
                print(f"⚠️  {url} - Error: {str(e)}. Retrying in {wait_time:.1f}s...", file=PRINT_FILE)
            time.sleep(wait_time)
            return check_link_is_valid(url, retry_count + 1, max_retries, quiet)
        else:
            if not quiet:
                print(f"⚠️  {url} - Error after {max_retries} retries: {str(e)}", file=PRINT_FILE)
            return False, str(e)


def process_csv(github_action=False):
    """
    Read the CSV, validate links, and update the Active column.
    """
    start_time = datetime.now()
    print(f"Starting validation at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}", file=PRINT_FILE)

    input_file = INPUT_FILE
    output_file = OUTPUT_FILE

    # Track broken links for summary
    broken_links = []
    total_links = 0

    # Read the CSV
    rows = []
    with open(input_file, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the header row
        rows.append(headers)
        primary_link_index = headers.index(PRIMARY_LINK_HEADER_NAME)
        secondary_link_index = headers.index(SECONDARY_LINK_HEADER_NAME)
        active_index = headers.index(ACTIVE_HEADER_NAME)
        last_checked_index = headers.index(LAST_CHECKED_HEADER_NAME)

        total_rows = sum(1 for _ in reader)
        print(f"Processing {total_rows} links...", file=PRINT_FILE)
        file.seek(0)
        next(reader)  # Skip header again

        for row_num, row in enumerate(reader, start=2):
            url = (
                row[primary_link_index].strip()
                if primary_link_index < len(row)
                else (row[secondary_link_index].strip() if secondary_link_index < len(row) else "")
            )
            if url:
                total_links += 1
                print(f"[{row_num-1}] Checking: {row[0]} - {url}", file=PRINT_FILE)

                # Validate the link
                is_active, status = check_link_is_valid(url, quiet=github_action)

                # Track broken links
                if not is_active:
                    broken_links.append(
                        {
                            "name": row[0] if len(row) > 0 else "Unknown",
                            "url": url,
                            "row_num": row_num - 1,
                            "status": status,
                        }
                    )
                    print(f"  ❌ BROKEN: Status {status}", file=PRINT_FILE)
                else:
                    print(f"  ✅ OK: Status {status}", file=PRINT_FILE)

                # Update the Active column and Last Checked column
                row[active_index] = "TRUE" if is_active else "FALSE"
                row[last_checked_index] = datetime.now().strftime("%Y-%m-%d:%H-%M-%S")

                delay = random.uniform(2, 4)
                time.sleep(delay)
            else:
                # No link to validate, mark as FALSE
                row[active_index] = "FALSE"
                row[last_checked_index] = datetime.now().strftime("%Y-%m-%d:%H-%M-%S")

            rows.append(row)

    # Write the updated CSV
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    # Calculate execution time
    end_time = datetime.now()
    duration = end_time - start_time

    if github_action:
        # Output JSON for GitHub Action
        result = {
            "timestamp": end_time.isoformat(),
            "execution_time": str(duration),
            "total_links": total_links,
            "active_links": total_links - len(broken_links),
            "broken_links": broken_links,
        }
        print(json.dumps(result, indent=2))

        print(f"\nValidation completed at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}", file=PRINT_FILE)
        print(f"Total execution time: {duration}", file=PRINT_FILE)
        print(f"Summary: {total_links - len(broken_links)}/{total_links} links are active", file=PRINT_FILE)
        if broken_links:
            print(f"\nBROKEN LINKS SUMMARY ({len(broken_links)} broken):", file=PRINT_FILE)
            print("=" * 80, file=PRINT_FILE)
            for i, link in enumerate(broken_links, 1):
                print(f"{i:2d}. [{link['row_num']:3d}] {link['name']}", file=PRINT_FILE)
                print(f"     URL: {link['url']}", file=PRINT_FILE)
                print(f"     Status: {link['status']}", file=PRINT_FILE)
                print(file=PRINT_FILE)
        else:
            print(f"\n🎉 All {total_links} links are working!", file=PRINT_FILE)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate links in resource-metadata.csv")
    parser.add_argument(
        "--github-action",
        action="store_true",
        help="Run in GitHub Action mode (outputs JSON to stdout, logs to stderr)",
    )
    args = parser.parse_args()

    PRINT_FILE = None

    if args.github_action:
        PRINT_FILE = sys.stderr

    print(f"Starting link validation{' in GitHub Action mode' if args.github_action else ''}...", file=PRINT_FILE)
    process_csv(github_action=args.github_action)

    print("Link validation completed!", file=PRINT_FILE)

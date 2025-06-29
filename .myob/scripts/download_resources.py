"""
Download resources from the Awesome Claude Code repository CSV file.

This script downloads all active resources (or filtered subset) from GitHub
repositories listed in the resource-metadata.csv file. It respects rate
limiting and organizes downloads by category.

Usage:
    python download_resources.py [options]

Options:
    --category CATEGORY     Filter by specific category
    --license LICENSE       Filter by license type
    --max-downloads N       Limit number of downloads (for testing)
    --output-dir DIR        Custom output directory (default: .myob/downloads)
"""

import argparse
import csv
import os
import random
import re
import time
from datetime import datetime
from pathlib import Path

import requests

# Constants
USER_AGENT = "awesome-claude-code Downloader/1.0"
HEADERS = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github.v3.raw"}
CSV_FILE = ".myob/scripts/resource-metadata.csv"
DEFAULT_OUTPUT_DIR = ".myob/downloads"


def sanitize_filename(name):
    """Sanitize a string to be safe for use as a filename."""
    # Replace spaces with hyphens and remove/replace problematic characters
    name = re.sub(r'[<>:"/\\|?*]', "", name)
    name = re.sub(r"\s+", "-", name)
    name = name.strip("-.")
    return name[:255]  # Max filename length


def parse_github_url(url):
    """
    Parse GitHub URL and extract owner, repo, branch, and path.
    Returns a dict with keys: owner, repo, branch, path, type
    """
    patterns = {
        # File in repository
        "file": r"https://github\.com/([^/]+)/([^/]+)/(?:blob|raw)/([^/]+)/(.+)",
        # Directory in repository
        "dir": r"https://github\.com/([^/]+)/([^/]+)/tree/([^/]+)/(.+)",
        # Repository root
        "repo": r"https://github\.com/([^/]+)/([^/]+)/?$",
        # Gist
        "gist": r"https://gist\.github\.com/([^/]+)/([^/#]+)",
    }

    for url_type, pattern in patterns.items():
        match = re.match(pattern, url)
        if match:
            if url_type == "gist":
                return {
                    "type": "gist",
                    "owner": match.group(1),
                    "gist_id": match.group(2),
                }
            elif url_type == "repo":
                return {
                    "type": "repo",
                    "owner": match.group(1),
                    "repo": match.group(2),
                }
            else:
                return {
                    "type": url_type,
                    "owner": match.group(1),
                    "repo": match.group(2),
                    "branch": match.group(3),
                    "path": match.group(4),
                }

    return None


def download_github_file(url_info, output_path, retry_count=0, max_retries=3):
    """
    Download a file from GitHub using the API.
    Returns True if successful, False otherwise.
    """
    try:
        if url_info["type"] == "file":
            # Download single file
            api_url = f"https://api.github.com/repos/{url_info['owner']}/{url_info['repo']}/contents/{url_info['path']}?ref={url_info['branch']}"
            response = requests.get(api_url, headers=HEADERS, timeout=30)

            if response.status_code == 200:
                # Create directory if needed
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Write file content
                with open(output_path, "wb") as f:
                    f.write(response.content)
                return True

        elif url_info["type"] == "dir":
            # List directory contents
            api_url = f"https://api.github.com/repos/{url_info['owner']}/{url_info['repo']}/contents/{url_info['path']}?ref={url_info['branch']}"
            response = requests.get(api_url, headers={**HEADERS, "Accept": "application/vnd.github+json"}, timeout=30)

            if response.status_code == 200:
                # Create directory
                os.makedirs(output_path, exist_ok=True)

                # Download each file in the directory
                items = response.json()
                for item in items:
                    if item["type"] == "file":
                        file_path = os.path.join(output_path, item["name"])
                        # Download the file content
                        file_response = requests.get(item["download_url"], headers=HEADERS, timeout=30)
                        if file_response.status_code == 200:
                            with open(file_path, "wb") as f:
                                f.write(file_response.content)
                return True

        elif url_info["type"] == "gist":
            # Download gist
            api_url = f"https://api.github.com/gists/{url_info['gist_id']}"
            response = requests.get(api_url, headers={**HEADERS, "Accept": "application/vnd.github+json"}, timeout=30)

            if response.status_code == 200:
                gist_data = response.json()
                # Create directory for gist
                os.makedirs(output_path, exist_ok=True)

                # Download each file in the gist
                for filename, file_info in gist_data["files"].items():
                    file_path = os.path.join(output_path, filename)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(file_info["content"])
                return True

        # Handle rate limiting
        if response.status_code == 429:
            raise requests.exceptions.HTTPError("Rate limited")

        return False

    except Exception as e:
        if retry_count < max_retries:
            wait_time = (2**retry_count) + random.uniform(1, 2)
            print(f"  Retry in {wait_time:.1f}s... (Error: {str(e)})")
            time.sleep(wait_time)
            return download_github_file(url_info, output_path, retry_count + 1, max_retries)

        print(f"  Failed after {max_retries} retries: {str(e)}")
        return False


def process_resources(category_filter=None, license_filter=None, max_downloads=None, output_dir=DEFAULT_OUTPUT_DIR):
    """
    Process and download resources from the CSV file.
    """
    start_time = datetime.now()
    print(f"Starting download at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Output directory: {output_dir}")

    # Track statistics
    total_resources = 0
    downloaded = 0
    skipped = 0
    failed = 0

    # Read CSV
    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Check if we've reached the download limit
            if max_downloads and downloaded >= max_downloads:
                print(f"\nReached download limit ({max_downloads}). Stopping.")
                break

            # Skip inactive resources
            if row["Active"].upper() != "TRUE":
                continue

            total_resources += 1

            # Apply filters
            if category_filter and row["Category"] != category_filter:
                continue

            if license_filter and row.get("License", "") != license_filter:
                continue

            # Get the URL (prefer primary link)
            url = row["Primary Link"].strip() or row["Secondary Link"].strip()
            if not url:
                continue

            display_name = row["Display Name"]
            category = sanitize_filename(row["Category"].lower().replace(" & ", "-"))

            print(f"\n[{downloaded + 1}] Processing: {display_name}")
            print(f"  URL: {url}")

            # Parse GitHub URL
            url_info = parse_github_url(url)
            if not url_info:
                print("  Skipped: Not a GitHub URL")
                skipped += 1
                continue

            # Determine output path
            safe_name = sanitize_filename(display_name)
            if url_info["type"] == "gist":
                resource_path = os.path.join(output_dir, category, f"{safe_name}-gist")
            elif url_info["type"] == "repo":
                resource_path = os.path.join(output_dir, category, safe_name)
                print("  Skipped: Full repository downloads not implemented")
                skipped += 1
                continue
            elif url_info["type"] == "dir":
                resource_path = os.path.join(output_dir, category, safe_name)
            else:  # file
                # Extract filename from path
                filename = os.path.basename(url_info["path"])
                resource_path = os.path.join(output_dir, category, safe_name, filename)

            # Download the resource
            print(f"  Downloading to: {resource_path}")
            if download_github_file(url_info, resource_path):
                print("  ✅ Downloaded successfully")
                downloaded += 1
            else:
                print("  ❌ Download failed")
                failed += 1

            # Rate limiting delay
            time.sleep(random.uniform(1, 2))

    # Summary
    end_time = datetime.now()
    duration = end_time - start_time

    print(f"\n{'=' * 60}")
    print(f"Download completed at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total execution time: {duration}")
    print("\nSummary:")
    print(f"  Total resources found: {total_resources}")
    print(f"  Downloaded: {downloaded}")
    print(f"  Skipped: {skipped}")
    print(f"  Failed: {failed}")
    print(f"{'=' * 60}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Download resources from awesome-claude-code CSV")
    parser.add_argument("--category", help="Filter by specific category")
    parser.add_argument("--license", help="Filter by license type")
    parser.add_argument("--max-downloads", type=int, help="Limit number of downloads")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help="Output directory")

    args = parser.parse_args()

    # Create output directory if needed
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)

    # Process resources
    process_resources(
        category_filter=args.category,
        license_filter=args.license,
        max_downloads=args.max_downloads,
        output_dir=args.output_dir,
    )


if __name__ == "__main__":
    main()

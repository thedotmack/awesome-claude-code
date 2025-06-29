"""
This script generates a README.md file for the Awesome Claude Code repository
by extracting resource metadata from a CSV file and formatting it into a structured Markdown document.
How it works:
1. Reads current README to extract header/footer sections
2. Reads CSV to get resource data
3. Generates fresh TOC based on CSV structure
4. Builds resource sections with descriptions
5. Combines: [README header] + [Generated TOC] + [CSV-based resources] + [README footer]
"""

import csv
import os
from collections import OrderedDict


def extract_readme_sections():
    """Extract header and footer content from existing README."""
    readme_path = os.path.join(os.path.dirname(__file__), "../..", "README.md")

    if not os.path.exists(readme_path):
        raise FileNotFoundError(f"README.md not found at {readme_path}")

    with open(readme_path, encoding="utf-8") as file:
        content = file.read()

    # Find the Contents section
    contents_start = content.find("## Contents")
    if contents_start == -1:
        raise ValueError("Could not find Contents section in README")

    # Find the Contributing section (start of footer)
    contributing_start = content.find("## Contributing")
    if contributing_start == -1:
        raise ValueError("Could not find Contributing section in README")

    # Extract header (everything up to and including "## Contents")
    header = content[: contents_start + len("## Contents")] + "\n\n"

    # Extract footer (Contributing section and everything after)
    footer = "\n" + content[contributing_start:].rstrip() + "\n"

    return header, footer


def generate_table_of_contents(organized_data):
    """Generate the table of contents section."""
    toc_lines = []

    for category, subcategories in organized_data.items():
        # Convert category name to anchor link
        anchor = category.lower().replace(" ", "-").replace("&", "").replace(".", "").replace(",", "")
        toc_lines.append(f"▪&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[{category}](#{anchor})  ")

        # Add subcategories if they exist and aren't just "_no_subcategory"
        if len(subcategories) > 1 or (len(subcategories) == 1 and "_no_subcategory" not in subcategories):
            for subcat in subcategories:
                if subcat != "_no_subcategory":
                    # Convert subcategory name to anchor link
                    sub_anchor = (
                        subcat.lower()
                        .replace(" ", "-")
                        .replace("&", "")
                        .replace(".", "")
                        .replace(",", "")
                        .replace("/", "")
                    )
                    toc_lines.append(
                        f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;▫&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[{subcat}](#{sub_anchor})  "
                    )

    return "\n".join(toc_lines) + "\n\n<br>\n\n"


def generate_readme_content(csv_path):
    """Generate README content from CSV data."""
    # Read CSV data in order - preserving the order from the CSV file
    rows = []
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Skip inactive resources
            if row["Active"].upper() == "TRUE":
                rows.append(row)

    # Organize data by category and sub-category, preserving CSV order
    organized_data = OrderedDict()

    for row in rows:
        category = row["Category"].strip()
        sub_category = row["Sub-Category"].strip()

        if category not in organized_data:
            organized_data[category] = OrderedDict()

        if sub_category:
            if sub_category not in organized_data[category]:
                organized_data[category][sub_category] = []
            organized_data[category][sub_category].append(row)
        else:
            if "_no_subcategory" not in organized_data[category]:
                organized_data[category]["_no_subcategory"] = []
            organized_data[category]["_no_subcategory"].append(row)

    # Extract header and footer from existing README
    header_content, footer_content = extract_readme_sections()

    # Generate table of contents
    toc_content = generate_table_of_contents(organized_data)

    # Start building README
    readme_content = header_content + toc_content

    # Generate content sections
    for category, subcategories in organized_data.items():
        readme_content += f"## {category}\n\n"

        # Add category description based on category type
        if category == "Workflows & Knowledge Guides":
            readme_content += "> A **workflow** is a tightly coupled set of Claude Code-native resources that facilitate specific projects\n\n"
        elif category == "Tooling":
            readme_content += "> **Tooling** denotes applications that are built on top of Claude Code and consist of more components than slash-commands and `CLAUDE.md` files\n\n"
        elif category == "CLAUDE.md Files":
            readme_content += "> **`CLAUDE.md` files** are files that contain important guidelines and context-specfic information or instructions that help Claude Code to better understand your project and your coding standards\n\n"
        elif category == "Official Documentation":
            readme_content += "> Links to some of Anthropic's terrific documentation and resources regarding Claude Code\n\n<!--lint disable double-link-->\n\n"

        # Process subcategories
        for sub_category, entries in subcategories.items():
            if sub_category != "_no_subcategory":
                readme_content += f"### {sub_category}\n\n"

            # Generate entries (preserve CSV order - no sorting)
            for entry in entries:
                display_name = entry["Display Name"]
                primary_link = entry["Primary Link"]
                author_name = entry["Author Name"]
                author_link = entry["Author Link"]
                description = entry["Description"].strip()

                # Format entry
                entry_line = f"[`{display_name}`]({primary_link})"
                if author_name:
                    entry_line += f" by [{author_name}]({author_link})" if author_link else f" by {author_name}"

                readme_content += entry_line + "  \n"

                if description:
                    readme_content += description + "\n\n"
                else:
                    readme_content += "\n"

        readme_content += "<br>\n\n"

    # Add footer content extracted from existing README
    readme_content += footer_content

    return readme_content


def main():
    """Main function to generate README from CSV."""
    print("=== README Generation from CSV ===")

    # Generate README content
    csv_path = os.path.join(os.path.dirname(__file__), "resource-metadata.csv")
    print("Generating README content from CSV...")
    readme_content = generate_readme_content(csv_path)

    # Write README.md
    readme_path = os.path.join(os.path.dirname(__file__), "../..", "README.md")
    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(readme_content)

    print(f"✅ README.md generated successfully at {readme_path}")

    # Count resources
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        total_count = sum(1 for row in reader if row["Active"].upper() == "TRUE")

    print(f"📊 Generated README with {total_count} active resources")


if __name__ == "__main__":
    main()

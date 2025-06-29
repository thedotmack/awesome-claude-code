# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the Awesome Claude Code repository - a curated list of slash-commands, CLAUDE.md files, CLI tools, and other resources for enhancing Claude Code workflows. The repository serves as a community resource hub for sharing knowledge and best practices.

## Common Development Tasks

### Adding New Resources

1. **Use the slash-command**: Run `/project:add-new-resource` to be guided through adding a new resource
2. **CSV-based addition (RECOMMENDED)**: Edit `.myob/scripts/resource-metadata.csv` directly and run `make generate` to create a perfectly formatted README.md
3. **Manual addition**: Edit README.md following the existing format and alphabetical ordering

### Generating README from CSV

The repository now supports data-driven README generation:

- Edit resources in `.myob/scripts/resource-metadata.csv` with fields: Display Name, Primary Link, Secondary Link, Author Name, Author Link, Category, Sub-Category, Description, Active, Last Checked
- Run `make generate` to generate README.md from CSV data
- The generated README includes hierarchical table of contents and maintains proper formatting

### Checking Links

Run `/check-links` to verify all links in the README are working properly. The link validation script:

- Validates all URLs in the CSV file
- Updates Active status and Last Checked timestamps
- Fetches license information from GitHub repositories
- Supports GitHub API for repository links
- Includes retry logic and rate limiting
- Supports `MAX_LINKS` parameter for faster testing: `make validate MAX_LINKS=10`

### Downloading Resources

Download active resources from GitHub using the download script:

- Run `make download-resources` to download all active resources
- Filter by category: `make download-resources CATEGORY='Slash-Commands'`
- Filter by license: `make download-resources LICENSE='MIT'`
- Limit downloads for testing: `make download-resources MAX_DOWNLOADS=5`
- Resources are saved to `.myob/downloads/` organized by category

### Creating Pull Requests

1. Follow the PR template in `.github/PULL_REQUEST_TEMPLATE.md`
2. Ensure entries are properly categorized and alphabetically ordered
3. Use permalinks when linking to GitHub files

## Repository Structure

- **README.md**: Main list of resources, organized by category (generated from CSV)
- **CONTRIBUTING.md**: Contribution guidelines
- **code-of-conduct.md**: Community standards
- **Makefile**: Build system with `generate` target for README generation
- **.myob/scripts/**: Data management and automation scripts
  - `resource-metadata.csv`: Single source of truth for all resource data
  - `generate_readme.py`: Converts CSV to formatted README.md with hierarchical TOC
  - `validate_links.py`: Comprehensive link validation with GitHub API support
- **.claude/commands/**: Custom slash-commands for this project
  - `add-new-resource.md`: Wizard for adding new resources
  - `add-new-claude-md.md`: Helper for adding CLAUDE.md files

## Key Guidelines

1. **Resource Quality**: Only include resources that provide genuine value to Claude Code users
2. **Formatting**: Follow existing formatting exactly - entries are categorized and alphabetically ordered
3. **Attribution**: Always include proper attribution and prefer permalinks for GitHub resources
4. **Categories**:
   - Workflows & Knowledge Guides
   - Tooling
   - Slash-Commands (organized by command name)
   - CLAUDE.md Files (organized by repository name)
   - Official Documentation

## Working with This Repository

- The repository excludes `.myob` and `.claude` directories from analysis unless specifically requested
- This is a documentation/curation project focused on maintaining high-quality, well-organized content
- **Data-driven approach**: The CSV file serves as the single source of truth for all resource metadata
- **Automated generation**: Use `make generate` to create perfectly formatted README from CSV data
- **Link validation**: Run `make validate` to validate all links. Implemented with GitHub API support, retry logic, and comprehensive status tracking
- Quality assurance features:
  - Link validation tests to ensure all curated resources remain accessible
  - Markdown linting to maintain consistent formatting
  - CSV-based data validation and integrity checks
  - Automated TOC generation with hierarchical structure

## Development Tools and Scripts

The `.myob/scripts/` directory contains several Python utilities for managing repository data:

1. **generate_readme.py**: Main generation script

   - Automatically migrates CSV schema if needed
   - Preserves exact ordering from CSV file
   - Generates hierarchical table of contents
   - Maintains all original README formatting and structure

2. **validate_links.py**: Comprehensive link checker

   - Supports both regular URLs and GitHub repository links
   - Fetches license information from GitHub API
   - Implements exponential backoff for rate limiting
   - Updates CSV with validation status and timestamps
   - GitHub Action compatible with JSON output
   - Supports `--max-links` parameter to limit validation scope

3. **download_resources.py**: Resource download utility

   - Downloads active resources from GitHub repositories
   - Supports filtering by category and license type
   - Handles files, directories, and gists
   - Implements rate limiting and retry logic
   - Organizes downloads by category
   - Supports `--max-downloads` for testing

## Development Best Practices

- When running Python or pip commands, ensure you are working inside the `venv` either by activating or by using the path to the relevant Python binary

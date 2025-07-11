# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the Awesome Claude Code repository - a curated list of slash-commands, CLAUDE.md files, CLI tools, and other resources for enhancing Claude Code workflows. The repository serves as a community resource hub for sharing knowledge and best practices.

## Common Development Tasks

### Adding New Resources

1. **Use the slash-command**: Run `/add-new-resource  ` to be guided through adding a new resource
2. **CSV-based additions (RECOMMENDED)**: Edit `THE_RESOURCES_TABLE.csv` directly and run `make generate` to create a perfectly formatted README.md
3. **Manual edits**: Edit README.md following the existing format and alphabetical ordering

### Generating README from CSV

The repository uses a template-based system for README generation:

- Edit resources in `THE_RESOURCES_TABLE.csv` with fields: ID (auto-generated), Display Name, Primary Link, Secondary Link, Author Name, Author Link, Category, Sub-Category, Active, Last Modified, Last Checked, License, and Description
- Edits to the `README.md` text besides the addition of new resources are located in the `templates/README.template.md`.
- Run `make generate` to generate `README.md` from CSV data using the template system
- The generated README includes hierarchical table of contents and maintains proper formatting
- Templates are stored in `templates/` for customization

### Checking Links

Run `/check-links` to verify all links in the README are working properly. The link validation script:

- Validates all URLs in the CSV file
- Updates Active status and Last Checked timestamps
- Fetches license information from GitHub repositories
- Fetches last modified dates for GitHub resources using Commits API
- Supports GitHub API for repository links
- Includes retry logic and rate limiting
- Supports `MAX_LINKS` parameter for faster testing: `make validate MAX_LINKS=10`

### Validating Single Resources

When adding new resources, validation happens automatically during the `make add_resource` process. You can also validate individual URLs:

```bash
make validate-single URL=https://github.com/example/repo
make validate-single URL=https://example.com/resource SECONDARY=https://docs.example.com NAME="My Resource"
```

### Using Template Overrides

The template system includes support for manual overrides when automatic processing needs adjustment:

- Edit `templates/resource-overrides.yaml` to override specific resource fields
- Supported fields: `active`, `license`, `description`
- Add `_locked: true` to prevent validation from updating a field
- Example override:
  ```yaml
  overrides:
    wf-d0cfdd2b: # Resource ID
      active: false
      active_locked: true
      notes: "Manually set inactive - broken link"
  ```
- Overrides are respected by all scripts: generation, validation, and downloads
- Use overrides sparingly - prefer fixing at the source when possible

### Downloading and Hosting Resources

Download active resources from GitHub using the download script:

- **Rate Limiting**: GitHub API allows 60 requests/hour without authentication, 5,000 with:
  ```bash
  export GITHUB_TOKEN=your_github_token  # Optional but recommended
  make download-resources
  ```
- Run `make download-resources` to download all active resources
- Filter by category: `make download-resources CATEGORY='Slash-Commands'`
- Filter by license: `make download-resources LICENSE='MIT'`
- Limit downloads for testing: `make download-resources MAX_DOWNLOADS=5`
- Resources whose license permits it are copied and hosted in this repo under `./resources`.

### Creating Pull Requests

1. Follow the PR template in `.github/PULL_REQUEST_TEMPLATE.md`
2. Ensure entries are properly categorized and alphabetically ordered
3. Use permalinks when linking to GitHub files

## Repository Structure

- **README.md**: Main list of resources, organized by category (generated from CSV)
- **CONTRIBUTING.md**: Contribution guidelines
- **code-of-conduct.md**: Community standards
- **Makefile**: Build system with `generate` target for README generation
- **scripts/**: Data management and automation scripts
  - `THE_RESOURCES_TABLE.csv`: Single source of truth for all resource data (includes ID column)
  - `generate_readme.py`: Template-based README generation with override support
  - `validate_links.py`: Link validation with override support
  - `download_resources.py`: Downloads resources with override support
- **.myob/templates/**: Template system files
  - `README.template.md`: Main template with placeholders
  - `readme-structure.yaml`: Defines section ordering and metadata
  - `resource-overrides.yaml`: Manual overrides for specific resources
- **.claude/commands/**: Custom slash-commands for this project
  - `add-new-resource.md`: Wizard for adding new resources

## Key Guidelines

1. **Resource Quality**: Only include resources that provide genuine value to Claude Code users
2. **Formatting**: Follow existing formatting exactly - entries are categorized and alphabetically ordered
3. **Attribution**: Always include proper attribution
4. **Categories**:
   - Workflows & Knowledge Guides
   - Tooling (CLI applications and other executables)
   - Hooks (new)
   - Slash-Commands (organized by command name)
   - CLAUDE.md Files (organized by repository name)
   - Official Documentation

## Working with This Repository

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

The `scripts/` directory contains several Python utilities for managing repository data:

1. **generate_readmepy**: Template-based generation script

   - Uses templates from `.templates/` for customizable output
   - Respects manual overrides from `resource-overrides.yaml`
   - Preserves exact ordering from CSV file
   - Generates hierarchical table of contents
   - Creates automatic backups before generation

2. **validate_links.py**: Link validation with override support

   - Supports both regular URLs and GitHub repository links
   - Fetches license information from GitHub API
   - Implements exponential backoff for rate limiting
   - Updates CSV with validation status and timestamps
   - GitHub Action compatible with JSON output
   - Supports `--max-links` parameter to limit validation scope

## Development Best Practices

- When running Python or pip commands, ensure you are working inside the `venv` either by activating or by using the path to the relevant Python binary.

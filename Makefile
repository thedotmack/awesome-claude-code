# Makefile for awesome-claude-code resource management
# Use venv python locally, system python in CI/CD
ifeq ($(CI),true)
    PYTHON := python3
else
    PYTHON := venv/bin/python3
endif
SCRIPTS_DIR := .myob/scripts

.PHONY: help process validate update clean test generate download-resources

help:
	@echo "Available commands:"
	@echo "  make process           - Extract resources from README.md and create/update CSV"
	@echo "  make validate          - Validate all links in the resource CSV"
	@echo "  make test              - Run validation tests on test CSV"
	@echo "  make generate          - Generate README.md from CSV data"
	@echo "  make update            - Run both process and validate"
	@echo "  make download-resources - Download active resources from GitHub"
	@echo "  make clean             - Remove generated files"
	@echo ""
	@echo "Options:"
	@echo "  make validate-github   - Run validation in GitHub Action mode (JSON output)"
	@echo "  make validate MAX_LINKS=N - Limit validation to N links"
	@echo "  make download-resources CATEGORY='Category Name' - Download specific category"
	@echo "  make download-resources LICENSE='MIT' - Download resources with specific license"
	@echo "  make download-resources MAX_DOWNLOADS=N - Limit downloads to N resources"
	@echo "  make download-resources HOSTED_DIR='path' - Custom hosted directory path"
	@echo ""
	@echo "Environment Variables:"
	@echo "  GITHUB_TOKEN - Set to avoid GitHub API rate limiting (export GITHUB_TOKEN=...)"

# Extract resources from README.md and create/update CSV
process:
	@echo "Processing README.md to extract resources..."
	$(PYTHON) $(SCRIPTS_DIR)/process_resources_to_csv.py

# Validate all links in the CSV
validate:
	@echo "Validating links in resource-metadata.csv..."
	@if [ -n "$(MAX_LINKS)" ]; then \
		echo "Limiting validation to $(MAX_LINKS) links"; \
		$(PYTHON) $(SCRIPTS_DIR)/validate_links.py --max-links $(MAX_LINKS); \
	else \
		$(PYTHON) $(SCRIPTS_DIR)/validate_links.py; \
	fi

# Run validation in GitHub Action mode
validate-github:
	$(PYTHON) $(SCRIPTS_DIR)/validate_links.py --github-action

# Run validation tests on test CSV
test:
	@echo "Running validation tests..."
	$(PYTHON) $(SCRIPTS_DIR)/test_validate_links.py

# Generate README.md from CSV data
generate:
	@echo "Generating README.md from CSV data..."
	$(PYTHON) $(SCRIPTS_DIR)/generate_readme.py

# Update: process resources then validate links
update: process validate
	@echo "Update complete!"

# Download resources from GitHub
download-resources:
	@echo "Downloading resources from GitHub..."
	@ARGS=""; \
	if [ -n "$(CATEGORY)" ]; then ARGS="$$ARGS --category '$(CATEGORY)'"; fi; \
	if [ -n "$(LICENSE)" ]; then ARGS="$$ARGS --license '$(LICENSE)'"; fi; \
	if [ -n "$(MAX_DOWNLOADS)" ]; then ARGS="$$ARGS --max-downloads $(MAX_DOWNLOADS)"; fi; \
	if [ -n "$(OUTPUT_DIR)" ]; then ARGS="$$ARGS --output-dir '$(OUTPUT_DIR)'"; fi; \
	if [ -n "$(HOSTED_DIR)" ]; then ARGS="$$ARGS --hosted-dir '$(HOSTED_DIR)'"; fi; \
	eval $(PYTHON) $(SCRIPTS_DIR)/download_resources.py $$ARGS

# Clean generated files (preserves scripts)
clean:
	@echo "Cleaning generated files..."
	@rm -f .myob/scripts/resource-metadata.csv
	@rm -rf .myob/downloads
	@echo "Clean complete!"

# Install required Python packages
install:
	@echo "Installing required Python packages..."
	@$(PYTHON) -m pip install --upgrade pip
	@$(PYTHON) -m pip install -e ".[dev]"
	@echo "Installation complete!"

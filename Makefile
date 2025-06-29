# Makefile for awesome-claude-code resource management
# Use venv python locally, system python in CI/CD
ifeq ($(CI),true)
    PYTHON := python3
else
    PYTHON := venv/bin/python3
endif
SCRIPTS_DIR := .myob/scripts

.PHONY: help process validate update clean test generate

help:
	@echo "Available commands:"
	@echo "  make process   - Extract resources from README.md and create/update CSV"
	@echo "  make validate  - Validate all links in the resource CSV"
	@echo "  make test      - Run validation tests on test CSV"
	@echo "  make generate  - Generate README.md from CSV data"
	@echo "  make update    - Run both process and validate"
	@echo "  make clean     - Remove generated files"
	@echo ""
	@echo "Options:"
	@echo "  make validate-github - Run validation in GitHub Action mode (JSON output)"

# Extract resources from README.md and create/update CSV
process:
	@echo "Processing README.md to extract resources..."
	$(PYTHON) $(SCRIPTS_DIR)/process_resources_to_csv.py

# Validate all links in the CSV
validate:
	@echo "Validating links in resource-metadata.csv..."
	$(PYTHON) $(SCRIPTS_DIR)/validate_links.py

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

# Clean generated files (preserves scripts)
clean:
	@echo "Cleaning generated files..."
	@rm -f .myob/scripts/resource-metadata.csv
	@echo "Clean complete!"

# Install required Python packages
install:
	@echo "Installing required Python packages..."
	@$(PYTHON) -m pip install --upgrade pip
	@$(PYTHON) -m pip install -e ".[dev]"
	@echo "Installation complete!"

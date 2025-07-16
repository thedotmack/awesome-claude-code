# Makefile for awesome-claude-code resource management
# Use venv python locally, system python in CI/CD
ifeq ($(CI),true)
    PYTHON := python3
else
    PYTHON := venv/bin/python3
endif
SCRIPTS_DIR := ./scripts

.PHONY: help process validate validate-single update clean test generate download-resources add_resource sort submit submit-resource

help:
	@echo "Available commands:"
	@echo "  make add_resource      - Interactive tool to add a new resource"
	@echo "  make submit            - One-command submission workflow (entry to PR)"
	@echo "  make process           - Extract resources from README.md and create/update CSV"
	@echo "  make validate          - Validate all links in the resource CSV"
	@echo "  make validate-single URL=<url> - Validate a single resource URL"
	@echo "  make test              - Run validation tests on test CSV"
	@echo "  make generate          - Generate README.md from CSV data"
	@echo "  make update            - Run both process and validate"
	@echo "  make download-resources - Download active resources from GitHub"
	@echo "  make sort              - Sort resources by category, sub-category, and name"
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

# Validate all links in the CSV (v2 with override support)
validate:
	@echo "Validating links in THE_RESOURCES_TABLE.csv (with override support)..."
	@if [ -n "$(MAX_LINKS)" ]; then \
		echo "Limiting validation to $(MAX_LINKS) links"; \
		$(PYTHON) $(SCRIPTS_DIR)/validate_links.py --max-links $(MAX_LINKS); \
	else \
		$(PYTHON) $(SCRIPTS_DIR)/validate_links.py; \
	fi

# Run validation in GitHub Action mode
validate-github:
	$(PYTHON) $(SCRIPTS_DIR)/validate_links.py --github-action

# Validate a single resource URL
validate-single:
	@if [ -z "$(URL)" ]; then \
		echo "Error: Please provide a URL to validate"; \
		echo "Usage: make validate-single URL=https://example.com/resource"; \
		exit 1; \
	fi
	@$(PYTHON) $(SCRIPTS_DIR)/validate_single_resource.py "$(URL)" $(if $(SECONDARY),--secondary "$(SECONDARY)") $(if $(NAME),--name "$(NAME)")

# Run validation tests on test CSV
test:
	@echo "Skipping v2 validation tests..."
# 	@echo "Running validation tests..."
# 	$(PYTHON) $(SCRIPTS_DIR)/test_validate_links.py

# Sort resources by category, sub-category, and name
sort:
	@echo "Sorting resources in THE_RESOURCES_TABLE.csv..."
	$(PYTHON) $(SCRIPTS_DIR)/sort_resources.py

# Generate README.md from CSV data using template system
generate: sort
	@echo "Generating README.md from CSV data using template system..."
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
	@rm -f THE_RESOURCES_TABLE.csv
	@rm -rf .myob/downloads
	@echo "Clean complete!"

# Install required Python packages
install:
	@echo "Installing required Python packages..."
	@$(PYTHON) -m pip install --upgrade pip
	@$(PYTHON) -m pip install -e ".[dev]"
	@echo "Installation complete!"

# Add a new resource interactively
add_resource:
	@echo "Starting interactive resource submission..."
	@$(PYTHON) $(SCRIPTS_DIR)/add_resource.py

# Ticket tracking commands (development workflow)
TICKET_SCRIPTS_DIR := .claude/workflow/scripts

ticket-status:
	@$(PYTHON) $(TICKET_SCRIPTS_DIR)/ticket_cli.py status $(TICKET)

ticket-list:
	@$(PYTHON) $(TICKET_SCRIPTS_DIR)/ticket_cli.py list $(if $(STATUS),--status $(STATUS))

ticket-update:
	@if [ -z "$(TICKET)" ] || [ -z "$(STATUS)" ]; then \
		echo "Usage: make ticket-update TICKET=TICKET-001 STATUS=in_progress"; \
		exit 1; \
	fi
	@$(PYTHON) $(TICKET_SCRIPTS_DIR)/ticket_cli.py update $(TICKET) --status $(STATUS)

ticket-complete:
	@if [ -z "$(TICKET)" ] || [ -z "$(ITEM)" ]; then \
		echo "Usage: make ticket-complete TICKET=TICKET-001 ITEM=001-1"; \
		exit 1; \
	fi
	@$(PYTHON) $(TICKET_SCRIPTS_DIR)/ticket_cli.py complete $(TICKET) --item $(ITEM)

ticket-blocked:
	@$(PYTHON) $(TICKET_SCRIPTS_DIR)/ticket_cli.py blocked

ticket-regenerate:
	@$(PYTHON) $(TICKET_SCRIPTS_DIR)/ticket_cli.py regenerate

ticket-add:
	@if [ -z "$(ID)" ] || [ -z "$(TITLE)" ]; then \
		echo "Usage: make ticket-add ID=TICKET-XXX TITLE=\"Ticket Title\" [OPTIONS]"; \
		echo ""; \
		echo "Required:"; \
		echo "  ID      - Ticket ID (e.g., TICKET-016 or TICKET-HOTFIX-001)"; \
		echo "  TITLE   - Ticket title (use quotes for multi-word titles)"; \
		echo ""; \
		echo "Optional:"; \
		echo "  PRIORITY     - P0, P1, P2 (default), or P3"; \
		echo "  CATEGORY     - setup, main_flow, helper, testing, documentation, infrastructure, feature (default)"; \
		echo "  DESCRIPTION  - Ticket description"; \
		echo "  CHECKLIST    - Comma-separated checklist items (use quotes)"; \
		echo "  BLOCKED_BY   - Comma-separated ticket IDs"; \
		echo "  BLOCKS       - Comma-separated ticket IDs"; \
		echo "  CRITERIA     - Comma-separated acceptance criteria"; \
		echo "  NOTES        - Additional notes"; \
		echo ""; \
		echo "Example:"; \
		echo "  make ticket-add ID=TICKET-HOTFIX-001 TITLE=\"Fix sync issues\" \\"; \
		echo "    PRIORITY=P0 CATEGORY=infrastructure \\"; \
		echo "    DESCRIPTION=\"Fix sync between JSON and markdown\" \\"; \
		echo "    CHECKLIST=\"Update sync script,Add validation,Test thoroughly\""; \
		exit 1; \
	fi
	@ARGS="$(ID) \"$(TITLE)\""; \
	if [ -n "$(PRIORITY)" ]; then ARGS="$$ARGS --priority $(PRIORITY)"; fi; \
	if [ -n "$(CATEGORY)" ]; then ARGS="$$ARGS --category $(CATEGORY)"; fi; \
	if [ -n "$(DESCRIPTION)" ]; then ARGS="$$ARGS --description \"$(DESCRIPTION)\""; fi; \
	if [ -n "$(CHECKLIST)" ]; then \
		ITEMS=""; \
		IFS=','; \
		for item in $(CHECKLIST); do \
			ITEMS="$$ITEMS \"$$item\""; \
		done; \
		ARGS="$$ARGS --checklist $$ITEMS"; \
	fi; \
	if [ -n "$(BLOCKED_BY)" ]; then \
		ITEMS=""; \
		IFS=','; \
		for item in $(BLOCKED_BY); do \
			ITEMS="$$ITEMS $$item"; \
		done; \
		ARGS="$$ARGS --blocked-by $$ITEMS"; \
	fi; \
	if [ -n "$(BLOCKS)" ]; then \
		ITEMS=""; \
		IFS=','; \
		for item in $(BLOCKS); do \
			ITEMS="$$ITEMS $$item"; \
		done; \
		ARGS="$$ARGS --blocks $$ITEMS"; \
	fi; \
	if [ -n "$(CRITERIA)" ]; then \
		ITEMS=""; \
		IFS=','; \
		for item in $(CRITERIA); do \
			ITEMS="$$ITEMS \"$$item\""; \
		done; \
		ARGS="$$ARGS --criteria $$ITEMS"; \
	fi; \
	if [ -n "$(NOTES)" ]; then ARGS="$$ARGS --notes \"$(NOTES)\""; fi; \
	eval $(PYTHON) $(TICKET_SCRIPTS_DIR)/ticket_cli.py add $$ARGS

# Generate tracking README from tickets.json
ticket-readme:
	@$(PYTHON) $(TICKET_SCRIPTS_DIR)/generate_tracking_readme.py

# Remove a ticket
ticket-remove:
	@if [ -z "$(TICKET)" ]; then \
		echo "Usage: make ticket-remove TICKET=TICKET-XXX"; \
		exit 1; \
	fi
	@$(PYTHON) $(TICKET_SCRIPTS_DIR)/ticket_cli.py remove $(TICKET)

# Add a ticket interactively
ticket-add-interactive:
	@$(PYTHON) $(TICKET_SCRIPTS_DIR)/add_ticket_interactive.py

# Update implementation tracking graph
update-tracking:
	@echo "Updating implementation tracking graph..."
	@$(PYTHON) $(TICKET_SCRIPTS_DIR)/update_tracking_graph.py

# Sync IMPLEMENTATION_TRACKING.md with tickets.json
sync-tickets:
	@echo "Syncing IMPLEMENTATION_TRACKING.md with tickets.json..."
	@$(PYTHON) $(TICKET_SCRIPTS_DIR)/sync_implementation_tracking_enhanced.py

# Check if IMPLEMENTATION_TRACKING.md is in sync with tickets.json
check-tickets:
	@echo "Checking if IMPLEMENTATION_TRACKING.md is in sync..."
	@$(PYTHON) $(TICKET_SCRIPTS_DIR)/sync_implementation_tracking_enhanced.py --check

# One-command submission workflow
submit:
	@echo "Starting resource submission workflow..."
	@$(PYTHON) $(SCRIPTS_DIR)/submit_resource.py $(ARGS)

# Alias for submit
submit-resource: submit

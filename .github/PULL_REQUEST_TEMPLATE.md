# Pull Request

## Type of Contribution

<!-- Select ONE by marking with an [x] -->

- [ ] **New Resource** - Adding a new resource to the list
- [ ] **Update Resource** - Updating existing resource information (e.g., broken link, license info)
- [ ] **Repository Improvement** - Improving the repository itself (not adding resources)

---

## For New Resources

### Resource Information

<!-- Complete all fields for new resources -->

- **Display Name**: <!-- e.g., "Claude Task Manager" or "/commit" -->
- **Category**: <!-- Select from: Workflows & Knowledge Guides, Tooling, Hooks, Slash-Commands, CLAUDE.md Files, Official Documentation -->
- **Sub-Category** (if applicable): <!-- e.g., "Version Control & Git", "Code Analysis & Testing" -->
- **Primary Link**: <!-- The main URL for the resource -->
- **Author Name**: <!-- Creator/maintainer name -->
- **Author Link**: <!-- Link to author's profile -->
- **License** (if known): <!-- e.g., MIT, Apache-2.0, GPL-3.0 -->

### Description

<!-- 1-2 sentences describing what the resource does and why it's valuable to Claude Code users -->

### Checklist for New Resources

<!-- All items must be checked -->

- [ ] Added entry to `THE_RESOURCES_TABLE.csv` (ID will be auto-generated)
- [ ] Ran `make generate` to update README.md (uses template system)
- [ ] Verified link works and points to correct resource
- [ ] Used appropriate category from the list above
- [ ] Description is concise (1-2 sentences max)
- [ ] For GitHub resources, used permalink where applicable
- [ ] Ran `make validate MAX_LINKS=1` to test link validation

---

## For Resource Updates

### What Changed?

<!-- Describe what you're updating -->

- **Resource Name**:
- **Change Type**: <!-- e.g., Fix broken link, Update license, Update description -->
- **Details**:

### Checklist for Updates

- [ ] Updated entry in `THE_RESOURCES_TABLE.csv`
- [ ] Ran `make generate` to update README.md
- [ ] Verified new information is correct
- [ ] Ran `make validate MAX_LINKS=1` to test if applicable

---

## For Repository Improvements

### Description of Changes

<!-- Describe what you're improving and why -->

### Checklist for Repository Changes

- [ ] Changes follow existing code style
- [ ] Updated relevant documentation
- [ ] Tested changes locally
- [ ] Pre-commit hooks pass

---

## Additional Notes

<!-- Any additional context that would help reviewers -->

## Questions?

- See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed contribution guidelines
- Use `/add-new-resource` in Claude Code for guided contribution (optional)
- The CSV approach ensures consistent formatting - never edit README.md directly!
- **Note**: The repository uses a template-based generation system. Resources get auto-generated IDs.
- **Special cases**: If a resource needs manual overrides (e.g., marking inactive), maintainers can use `.templates/resource-overrides.yaml`

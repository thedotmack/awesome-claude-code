# Contributing to Awesome Claude Code

## Contribution Guidelines

Please note that this project is released with a [Contributor Code of Conduct](code-of-conduct.md). By participating in this project you agree to abide by its terms.

Thank you for your interest in contributing to Awesome Claude Code! We welcome and appreciate all submissions. We especially look for submissions that: (a) are highly exemplary of effective best practices (and which you have actually used with teams or on your own); (b) are creative and innovative approaches to coding with Claude, or using the Claude Code interface in novel ways; (c) experiments with workflows that other Claude Code users might wish to try, and which provide good frameworks for things like documentation, testing, CI/CD, etc.

## How to Contribute

The repository uses a CSV-based approach where all resources are stored in `THE_RESOURCES_TABLE.csv` and the `README.md` is automatically generated.

**IMPORTANT**: Please submit resources one at a time. If you have multiple resources to contribute, create separate pull requests for each resource. This helps with review, testing, and ensures our automated notification system works correctly.

### Option 1: Script-Based Contribution (Recommended)

Use our interactive script to add new resources:

```bash
make add-resource
# OR
python scripts/add_resource.py
```

The script will:
- Guide you through selecting the resource type
- Prompt for all required information
- Validate your inputs
- Add the resource to `THE_RESOURCES_TABLE.csv`
- Generate an updated `README.md`
- Create a `.pr_template_content.md` file with pre-filled PR content

After running the script:
1. Review the changes to `THE_RESOURCES_TABLE.csv` and `README.md`
2. Copy the content from `.pr_template_content.md` into your PR description
3. Submit your pull request

### Option 2: Claude Code Slash Command

If you're using Claude Code, you can use the `/add-new-resource` command for a guided wizard experience.

### Option 3: Manual Contribution

If the automated tools aren't working for you:

1. **Fork this repository**

2. **Edit `THE_RESOURCES_TABLE.csv`** with these fields:
   - Display Name: The name of the resource as it appears in the README
   - Category: Main category (e.g., "Workflows & Knowledge Guides", "Tooling", "Hooks", "Slash-Commands", "CLAUDE.md Files")
   - Sub-Category: Optional sub-category (e.g., "Version Control & Git", "Code Analysis & Testing")
   - Primary Link: The main URL for the resource
   - Secondary Link: Optional secondary URL (e.g. permalink)
   - Author Name: The name/username of the author/creator/organization
   - Author Link: Link to the author's profile/website
   - Active: Set to TRUE for new resources
   - Last Modified: Leave empty for new entries
   - Last Checked: Use current date in YYYY-MM-DD format
   - License: License type if available (e.g., MIT, Apache-2.0)
   - Description: A brief description (1-2 sentences max)

3. **Run validation and generation**:
   ```bash
   make validate  # Check CSV integrity
   make generate  # Update README.md from CSV
   ```

4. **Submit a pull request** with both files changed

## What Makes a Resource "Awesome"?

Your submission should meet some or all of these criteria:

- Provides genuine value to Claude Code users
- Demonstrates innovative or exemplary usage patterns
- Follows best practices for `CLAUDE.md` files or slash-commands
- Comes from a reputable source (high star count is a plus!)
- Works with the latest version of Claude Code

## Important Notes

### GitHub Repository Notifications

When your GitHub-hosted resource is added to the list, an automated system will create a friendly notification issue on your repository informing you of the inclusion and providing badge options.

### Badges

If your resource is featured, you're encouraged to add a badge to your README:

[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)

```markdown
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)
```

Or the flat version:

[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/hesreallyhim/awesome-claude-code)

```markdown
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/hesreallyhim/awesome-claude-code)
```

## Submission Checklist

Before submitting:
- [ ] **One resource per PR** - Multiple resources require separate PRs
- [ ] Resource provides value to Claude Code users
- [ ] Link works and points to the correct resource
- [ ] Description is concise (1-2 sentences max)
- [ ] Appropriate category selected
- [ ] For GitHub resources, used permalink where applicable
- [ ] Ran `make validate` and `make generate`

## Need Help?

- **Script issues?** Feel free to submit manually
- **Broken links?** Open an issue
- **Security concerns?** Open an issue immediately
- **General questions?** Check existing issues first

## Quick Commands

```bash
# Add a new resource (interactive)
make add-resource

# Validate CSV integrity
make validate

# Generate README from CSV
make generate

# Test link validation
make validate MAX_LINKS=10
```

Thank you for helping make Awesome Claude Code even more awesome!

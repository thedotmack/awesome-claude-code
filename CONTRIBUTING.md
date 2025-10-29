# Contributing to Awesome Claude Code

## ⚠️ TEMPORARY PAUSE - Licensing Compliance

**New submissions are temporarily paused** while we resolve a licensing compliance issue with the upstream repository.

- **What's happening:** The upstream uses CC BY-NC-ND 4.0 which prohibits derivative works
- **What we're doing:** Working with the original maintainer to find a resolution
- **Timeline:** Expected resolution within 2-4 weeks
- **More info:** See [NOTICE.md](./NOTICE.md) and [LICENSE_COMPLIANCE.md](./LICENSE_COMPLIANCE.md)

We appreciate your patience and will resume accepting submissions once licensing is properly resolved.

---

Welcome! We're excited that you want to contribute to Awesome Claude Code. This guide will walk you through our streamlined contribution process.

**Important:** We take security seriously. All submissions are carefully reviewed to ensure they don't expose users to data risks or malicious code. Advanced tools may take additional time to review.

## Everyone Gets to Play 🎉

This is a truly community-driven awesome list. If your submission passes validation, it gets added automatically. No gatekeeping, no waiting.

### Validation = Inclusion

When your submission:
- ✅ Has working links
- ✅ Follows proper format
- ✅ Isn't spam or malicious
- ✅ Provides genuine value

**It automatically goes live.** No manual approval needed.

### Quality Guidelines (Objective Only)

- Working URLs that are publicly accessible
- Clear, descriptive (not marketing) language
- Proper license information
- No duplicate submissions
- Respects Claude Code Terms of Service

That's it. No subjective barriers.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](code-of-conduct.md). By participating in this project you agree to abide by its terms. Follow the conventions of the repo and don't engage in self-promotion. Use descriptive language, not "marketing" style.

## How to Submit a Resource

### 🚀 **[Click here to submit a new resource](https://github.com/thedotmack/awesome-claude-code/issues/new?template=submit-resource.yml)**

That's it! Just click the link above and fill out the form. No Git knowledge required.

### The Submission Process

Here's what happens when you submit a resource:

```mermaid
graph TD
    A[📝 Fill out submission form] --> B[🤖 Automated validation]
    B --> C{Valid?}
    C -->|❌ No| D[Bot comments with issues]
    D --> E[Edit your submission]
    E --> B
    C -->|✅ Yes| F[🤖 Bot automatically creates PR]
    F --> G[PR merged]
    G --> H[🎉 Resource goes live!]
    H --> I[You receive notification]
```

### What We Validate

When you submit a resource, our bot checks:

- ✅ All required fields are filled
- ✅ URLs are valid and accessible
- ✅ No duplicate resources exist
- ✅ License information (when available)
- ✅ Description length and quality

**NOTE:** By submitting a resource, you agree to allowing your codebase to be evaluated by a SoTA LLM for any security risks.

### If Changes Are Needed

Don't worry if validation fails! The bot will:

1. Post a clear comment explaining what needs to be fixed
2. Update the issue labels to reflect the status
3. Re-validate automatically when you edit your submission

Simply edit your issue to fix any problems - no need to create a new submission.

### After Validation Passes

The magic happens automatically:

1. Bot creates a fresh branch from latest main (no merge conflicts!)
2. Adds your resource to the CSV
3. Regenerates the README
4. Creates a pull request
5. Links everything back to your issue
6. Closes your submission issue

You'll be notified at every step, and if your resource is on GitHub, you'll receive a special notification issue in your repository! 🎉

## What Makes a Resource "Awesome"?

Your submission should:

- ✨ Provide genuine value to Claude Code users
- 🚀 Demonstrate innovative or exemplary usage patterns
- 📚 Follow best practices for the resource type
- 🔄 Work with the latest version of Claude Code
- 📝 Include clear documentation (demo videos are a huge bonus!)
- ❄️ Be unique and different from other existing awesome resources
- ⚖️ Respect the Terms of Service that govern the usage of Claude Code

We especially welcome:

- Proven workflows used in production
- Creative experiments pushing Claude Code's boundaries
- Tools that enhance Claude Code functionality
- Non-traditional applications (CI/CD, testing, documentation)

## Categories

Resources are organized into these categories:

- **Workflows & Knowledge Guides** - Comprehensive workflow systems
- **Tooling** - CLI applications and executables
  - IDE Integrations
- **Status Lines** - Status bar configurations and customizations
- **Hooks** - Claude Code hook configurations
- **Output Styles** - Configurations for customizing Claude Code's output formatting
- **Slash-Commands** - Individual command files
  - Version Control & Git
  - Code Analysis & Testing
  - Context Loading & Priming
  - Documentation & Changelogs
  - CI / Deployment
  - Project & Task Management
  - Miscellaneous
- **CLAUDE.md Files** - Project configuration files
  - Language-Specific
  - Domain-Specific
  - Project Scaffolding & MCP
- **Official Documentation** - Anthropic resources
- **Alternative Clients** - Alternative implementations and interfaces for Claude

## Adding New Categories

Repository maintainers can add new categories using the automated tool:

### Interactive Mode
```bash
make add-category
```

This will prompt you for:
- Category name
- ID and prefix
- Icon emoji
- Description
- Order position
- Subcategories

### Command Line Mode
```bash
make add-category ARGS='--name "My Category" --prefix "mycat" --icon "🎯"'
```

### What It Does
The `add-category` command automatically:
1. Updates `templates/categories.yaml` with the new category
2. Updates the GitHub issue template dropdown
3. Regenerates the README with the new section
4. Optionally creates a commit with all changes

### Examples
```bash
# Add a simple category with defaults
make add-category ARGS='--name "Extensions" --prefix "ext" --icon "🧩"'

# Add a category with multiple subcategories
make add-category ARGS='--name "Integrations" --prefix "int" --icon "🔗" --subcategories "API,Webhooks,Plugins"'

# Add a category at a specific position
make add-category ARGS='--name "Templates" --prefix "tmpl" --icon "📋" --order 5'
```

## Best Practices

- "Quick Start" section -> put it at the top!
- Include complete uninstall/cleanup instructions.
- Please mention if any core Claude Code system files are touched or managed by this resource.
- The more decoupled/indepedent your resource is from other resources or core Claude Code functionality, the easier it is for me to test, and for others to try out and adopt, and integrate with their workflow.
- Include an attribution to Anthropic, the company that built Claude Code and owns the license/trademark.

## Other Contributions

### Suggesting Improvements

For suggestions about the repository structure, new categories, or other enhancements:

1. **[Open a general issue](https://github.com/thedotmack/awesome-claude-code/issues/new)**
2. Describe your suggestion clearly
3. Explain the benefit to the community

### Reporting Issues

If you find problems with existing resources or the submission process:

- 📖 Check existing issues for similar reports
- 💬 Open a new issue with details
- 🐛 Include error messages and steps to reproduce
- 🔒 Report security issues immediately

## Badges

If your submission is approved, you can add a badge to your README:

[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/thedotmack/awesome-claude-code)

```markdown
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/thedotmack/awesome-claude-code)
```

Or the flat version:

[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/thedotmack/awesome-claude-code)

```markdown
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/thedotmack/awesome-claude-code)
```

## GitHub Repository Notifications

If your resource is on GitHub, our automated system will create a friendly notification issue on your repository informing you of the inclusion and providing badge options.

## Technical Details

For more information about how the repository works, including the automated systems, validation processes, and technical architecture, see [HOW_IT_WORKS.md](HOW_IT_WORKS.md).

---

Thank you for helping make Awesome Claude Code even more awesome! 🚀

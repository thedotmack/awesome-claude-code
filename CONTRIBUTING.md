# Contributing to Awesome Claude Code

## Contribution Guidelines

Please note that this project is released with a [Contributor Code of Conduct](code-of-conduct.md). By participating in this project you agree to abide by its terms.

Thank you for your interest in contributing to Awesome Claude Code! We welcome and appreciate all submissions. We especially look for submissions that: (a) are highly exemplary of effective best practices (and which you have actually used with teams or on your own); (b) are creative and innovative approaches to coding with Claude, or using the Claude Code interface in novel ways; (c) experiments with workflows that other Claude Code users might wish to try, and which provide good frameworks for things like documentation, testing, CI/CD, etc.

## How to Contribute

The repository uses a CSV-based approach where all resources are stored in `.myob/scripts/resource-metadata.csv` and the README.md is automatically generated. There are two ways to contribute:

### Option 1: Using the Claude Code Wizard (Optional)

> **TIP!** There is a project slash-command available in this repository, which is invoked as `/project:add-new-resource`, which can be used like a "wizard" to help users create their submission. If you are a Claude Code user, you may run Claude Code and invoke this command to help guide you through the process of creating a PR. (NOTE: This would be using _your_ Claude Code account/tokens/etc.)
>
> **Note:** You do NOT have to use the wizard to submit a PR, especially if your contribution isn't working well with the tool. Manual editing is perfectly acceptable and sometimes preferred.

### Option 2: Manual Contribution (Recommended if wizard isn't working)

1. **You do not need to be the owner/author** of the repository or file you're submitting. We are not hosting or distributing any of these files, but linking to them. If you've found (or discovered) a useful Claude Code resource, we'd love to include it! (That being said, do not link to a secondary distribution of a source whose license prohibits redistribution.) Self-contributions are of course welcome, as well.

2. **Follow the CSV-based workflow**:

   - Fork this repository
   - Edit `.myob/scripts/resource-metadata.csv` to add your resource with these fields:
     - Display Name: The name of the resource as it appears in the README
     - Category: Main category (e.g., "Workflows & Knowledge Guides", "Tooling", "Slash-Commands", "CLAUDE.md Files")
     - Sub-Category: Optional sub-category (e.g., "Version Control & Git", "Code Analysis & Testing")
     - Primary Link: The main URL for the resource
     - Secondary Link: Optional secondary URL
     - Author Name: The name of the author/creator
     - Author Link: Link to the author's profile/website
     - Active: Set to TRUE for new resources
     - Last Modified: Leave empty for new entries
     - Last Checked: Use current date in YYYY-MM-DD format
     - License: License type if available (e.g., MIT, Apache-2.0)
     - Description: A brief description (1-2 sentences max)
   - Run `make generate` to update README.md from the CSV data
   - Submit a pull request with both the CSV and README.md changes

3. **Make sure the source is "awesome"** - this means that it meets all or some of the following criteria:

   - It provides genuine value to Claude Code users
   - It demonstrates innovative or exemplary usage patterns
   - It follows best practices for `CLAUDE.md` files or slash-commands
   - It comes from a reputable or noteworthy source (high star count is a plus!)
   - It works with the latest, or most current, version of Claude Code

4. **Verify your submission**:
   - Check that your link works and points to the correct resource
   - Ensure you've selected the appropriate category and sub-category
   - Use permalinks for GitHub resources (click on the file/directory and select "Copy permalink" from the dropdown)
   - Run `make validate MAX_LINKS=1` to test link validation on your new entry

5. **Submit your PR** and we'll review it as soon as possible.

## Contribution Guidelines

- Additions to the list should be made by editing the `.myob/scripts/resource-metadata.csv` file, then running `make generate` to update README.md
- Never edit README.md directly - it is automatically generated from the CSV data
- Descriptions should be concise and informative (1-2 sentences max), and convey what value the resource provides to Claude Code users
- Include proper attribution and links to original sources (prefer permalinks if linking to Github files)
- The CSV maintains alphabetical ordering within categories automatically when README is generated
- **[Workflows & Knowledge Guides](README.md#workflows--knowledge-guides)** are tightly coupled sets of Claude Code resources that work together
- **[Slash-Commands](README.md#slash-commands)** should use the command name as the Display Name (e.g., `/commit` not "Git Commit Command")
- **[CLAUDE.md Files](README.md#claudemd-files)** should use the repository name as the Display Name, with the Primary Link pointing to the CLAUDE.md file
- Besides GitHub repositories, we welcome blog posts, articles, YouTube videos, Gists, and other resources
- Please submit an Issue if:
  - You find broken links or resources that are no longer available
  - You believe an entry contains misinformation or is no longer relevant to current Claude Code
  - You have suggestions to improve the repository structure or process

## Badges

If a file comes from a particular GitHub repository, that repository may include a badge to show that it has been featured in the Awesome Claude Code list. The same applies to blogs, websites, etc. This is optional, but encouraged.

Here are the badge assets:
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/hesreallyhim/awesome-claude-code)

We aim to maintain a high-quality collection that helps the Claude Code community. Even small contributions can make a big difference!

## Quick Start

1. Fork the repository
2. Add your resource to `.myob/scripts/resource-metadata.csv`
3. Run `make generate` to update README.md
4. Submit a PR with both files

Or use the Claude Code wizard: `/project:add-new-resource`

Thank you for helping make Awesome Claude Code even more awesome!

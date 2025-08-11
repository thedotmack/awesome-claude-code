#!/usr/bin/env python3
"""
Manual Badge Issue Notification
Creates a single notification issue in a specified GitHub repository
for manual/ad-hoc notifications about being featured in Awesome Claude Code
"""

import os
import re
import sys

from github import Github, GithubException

# Try to load .env file if it exists
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


# Configuration
ISSUE_TITLE = "🎉 Your project has been featured in Awesome Claude Code!"
NOTIFICATION_LABEL = "awesome-claude-code"


def parse_github_url(url: str) -> tuple[str | None, str | None]:
    """Extract owner and repo name from GitHub URL"""
    patterns = [
        r"github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$",
        r"github\.com/([^/]+)/([^/]+)/tree",
        r"github\.com/([^/]+)/([^/]+)/blob",
        r"github\.com/([^/]+)/([^/]+)/pull",
        r"github\.com/([^/]+)/([^/]+)/issues",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1), match.group(2)

    return None, None


def create_issue_body(resource_name: str, description: str) -> str:
    """Create friendly issue body with badge options"""
    github_url = "https://github.com/hesreallyhim/awesome-claude-code"

    # Use provided description or default
    description_text = (
        description
        if description
        else f"Your project {resource_name} provides valuable resources for the Claude Code community."
    )

    return f"""Hello! 👋

I'm excited to let you know that **{resource_name}** has been featured in the [Awesome Claude Code]({github_url}) list!

## About Awesome Claude Code
Awesome Claude Code is a curated collection of the best slash-commands, CLAUDE.md files, CLI tools, and other resources for enhancing Claude Code workflows. Your project has been recognized for its valuable contribution to the Claude Code community.

## Your Listing
{description_text}

You can find your entry here: [View in Awesome Claude Code]({github_url})

## Show Your Recognition! 🏆
If you'd like to display a badge in your README to show that your project is featured, you can use one of these:

### Option 1: Standard Badge
```markdown
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)
```
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)]({github_url})

### Option 2: Flat Badge
```markdown
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge-flat.svg)]({github_url})
```
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge-flat.svg)]({github_url})

## No Action Required
This is just a friendly notification - no action is required on your part. Feel free to close this issue at any time.

Thank you for contributing to the Claude Code ecosystem! 🙏

---
*This notification was sent because your project was added to the Awesome Claude Code list. \
This is a one-time notification.*"""


def notification_exists(repo, github_client) -> bool:
    """Check if notification issue already exists"""
    try:
        issues = repo.get_issues(state="all", creator=github_client.get_user().login)
        for issue in issues:
            if "awesome claude code" in issue.title.lower():
                return True
    except Exception as e:
        print(f"Warning: Could not check existing issues: {e}")
    return False


def can_create_label(repo) -> bool:
    """Check if we can create labels (requires write access)"""
    try:
        repo.create_label(NOTIFICATION_LABEL, "f39c12", "Featured in Awesome Claude Code")
        return True
    except Exception as e:
        # Label might already exist or we don't have permission
        print(f"Note: Could not create label: {e}")
        return False


def send_notification(
    repo_url: str,
    resource_name: str | None = None,
    description: str | None = None,
    skip_duplicate_check: bool = False,
    github_token: str | None = None,
) -> dict:
    """Send a notification issue to the specified repository"""

    result = {"repo_url": repo_url, "success": False, "message": "", "issue_url": None}

    # Parse repository URL
    owner, repo_name = parse_github_url(repo_url)
    if not owner or not repo_name:
        result["message"] = f"Invalid GitHub URL format: {repo_url}"
        return result

    repo_full_name = f"{owner}/{repo_name}"

    # Use resource name from input or default to repo name
    if not resource_name:
        resource_name = repo_name

    # Skip Anthropic repositories
    if "anthropic.com" in repo_url or "anthropics" in repo_full_name.lower():
        result["message"] = "Skipping Anthropics repository"
        return result

    # Initialize GitHub client
    if not github_token:
        github_token = os.environ.get("AWESOME_CC_PAT_PUBLIC_REPO")
        if not github_token:
            result["message"] = "No GitHub token provided (AWESOME_CC_PAT_PUBLIC_REPO)"
            return result

    try:
        github_client = Github(github_token)
        repo = github_client.get_repo(repo_full_name)

        # Check for existing notification unless skipped
        if not skip_duplicate_check and notification_exists(repo, github_client):
            result["message"] = "Notification issue already exists"
            return result

        # Try to create label (non-critical if it fails)
        labels = []
        if can_create_label(repo):
            labels = [NOTIFICATION_LABEL]

        # Create the issue
        issue_body = create_issue_body(resource_name, description or "")
        issue = repo.create_issue(title=ISSUE_TITLE, body=issue_body, labels=labels)

        result["success"] = True
        result["message"] = "Issue created successfully"
        result["issue_url"] = issue.html_url

    except GithubException as e:
        if e.status == 410:
            result["message"] = "Repository has issues disabled"
        elif e.status == 404:
            result["message"] = "Repository not found or private"
        elif e.status == 403:
            result["message"] = "Permission denied - check PAT permissions"
        else:
            result["message"] = f"GitHub API error: {str(e)}"
    except Exception as e:
        result["message"] = f"Unexpected error: {str(e)}"

    return result


def main():
    """Main execution for manual notification"""

    # Get inputs from environment variables (set by GitHub Actions)
    repo_url = os.environ.get("REPOSITORY_URL")
    resource_name = os.environ.get("RESOURCE_NAME", "").strip() or None
    description = os.environ.get("DESCRIPTION", "").strip() or None
    skip_duplicate_check = os.environ.get("SKIP_DUPLICATE_CHECK", "false").lower() == "true"

    if not repo_url:
        print("Error: REPOSITORY_URL environment variable is required")
        sys.exit(1)

    print(f"Sending notification to: {repo_url}")
    if resource_name:
        print(f"Resource name: {resource_name}")
    if description:
        print(f"Description: {description[:100]}...")
    if skip_duplicate_check:
        print("Skipping duplicate check")

    # Send the notification
    result = send_notification(
        repo_url=repo_url,
        resource_name=resource_name,
        description=description,
        skip_duplicate_check=skip_duplicate_check,
    )

    # Print result
    if result["success"]:
        print(f"✅ Success! Issue created: {result['issue_url']}")
    else:
        print(f"❌ Failed: {result['message']}")
        sys.exit(1)


if __name__ == "__main__":
    main()

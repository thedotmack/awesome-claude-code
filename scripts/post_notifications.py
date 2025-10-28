#!/usr/bin/env python3
"""
Script to automatically post notification messages as ISSUES to developer repositories.
Reads generated notification files and creates issues in each developer's repository.
"""

import os
import sys
import re
from typing import Dict, List, Optional

# Try to load .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Try to import GitHub library
try:
    from github import Github, GithubException
except ImportError:
    print("Error: PyGithub is required. Install with: pip install PyGithub")
    sys.exit(1)


# All gatekept tools with developer information and their repository URLs
REJECTED_DEVELOPERS = [
    {
        "issue": 228,
        "name": "Claude Control Terminal",
        "username": "schlunsen",
        "repository": "https://github.com/schlunsen/claude-control-terminal",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/228",
        "notification_file": "rejected_schlunsen_issue228.md",
    },
    {
        "issue": 205,
        "name": "Schaltwerk",
        "username": "2mawi2",
        "repository": "https://github.com/2mawi2/schaltwerk",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/205",
        "notification_file": "rejected_2mawi2_issue205.md",
    },
    {
        "issue": 175,
        "name": "Claude Code Sub agents Starter Kit",
        "username": "shinpr",
        "repository": "https://github.com/shinpr/ai-coding-project-boilerplate",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/175",
        "notification_file": "rejected_shinpr_issue175.md",
    },
    {
        "issue": 166,
        "name": "Claude Code Web Shell",
        "username": "vaderyang",
        "repository": "https://github.com/vaderyang/claudecode_web_shell",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/166",
        "notification_file": "rejected_vaderyang_issue166.md",
    },
    {
        "issue": 165,
        "name": "Claude Code Cheat Sheet",
        "username": "aeulker",
        "repository": "https://github.com/aeulker/Claude-Code-Cheat-Sheet",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/165",
        "notification_file": "rejected_aeulker_issue165.md",
    },
    {
        "issue": 108,
        "name": "Codanna",
        "username": "bartolli",
        "repository": "https://github.com/bartolli/codanna",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/108",
        "notification_file": "rejected_bartolli_issue108.md",
    },
    {
        "issue": 104,
        "name": "AI Coding Project Boilerplate",
        "username": "shinpr",
        "repository": "https://github.com/shinpr/ai-coding-project-boilerplate",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/104",
        "notification_file": "rejected_shinpr_issue104.md",
    },
]

WAITING_DEVELOPERS = [
    {
        "issue": 122,
        "name": "claude-code-guardian",
        "username": "jfpedroza",
        "repository": "https://github.com/jfpedroza/claude-code-guardian",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/122",
        "notification_file": "waiting_jfpedroza_issue122.md",
    },
    {
        "issue": 148,
        "name": "Claudable",
        "username": "Atipico1",
        "repository": "https://github.com/opactorai/Claudable",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/148",
        "notification_file": "waiting_Atipico1_issue148.md",
    },
    {
        "issue": 169,
        "name": "Claude Agent Toolkit",
        "username": "cheolwanpark",
        "repository": "https://github.com/cheolwanpark/claude-agent-toolkit",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/169",
        "notification_file": "waiting_cheolwanpark_issue169.md",
    },
    {
        "issue": 178,
        "name": "Claude Code Hook Comms (HCOM)",
        "username": "aannoo",
        "repository": "https://github.com/aannoo/claude-hook-comms",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/178",
        "notification_file": "waiting_aannoo_issue178.md",
    },
    {
        "issue": 183,
        "name": "Omnara",
        "username": "ishaansehgal99",
        "repository": "https://github.com/omnara-ai/omnara",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/183",
        "notification_file": "waiting_ishaansehgal99_issue183.md",
    },
    {
        "issue": 233,
        "name": "Session Driven Development",
        "username": "ankushdixit",
        "repository": "https://github.com/ankushdixit/sdd",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/233",
        "notification_file": "waiting_ankushdixit_issue233.md",
    },
    {
        "issue": 238,
        "name": "Claude Code Handbook",
        "username": "NikiforovAll",
        "repository": "https://nikiforovall.blog/claude-code-rules/",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/238",
        "notification_file": "waiting_NikiforovAll_issue238.md",
        "skip": True,  # Not a GitHub repo
    },
    {
        "issue": 242,
        "name": "Claude X",
        "username": "kunwar-shah",
        "repository": "https://github.com/kunwar-shah/claudex",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/242",
        "notification_file": "waiting_kunwar-shah_issue242.md",
    },
    {
        "issue": 243,
        "name": "conduit8",
        "username": "alexander-zuev",
        "repository": "https://github.com/conduit8/conduit8",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/243",
        "notification_file": "waiting_alexander-zuev_issue243.md",
    },
    {
        "issue": 244,
        "name": "Web Assets Generator",
        "username": "alonw0",
        "repository": "https://github.com/alonw0/web-asset-generator",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/244",
        "notification_file": "waiting_alonw0_issue244.md",
    },
    {
        "issue": 252,
        "name": "Claw Code",
        "username": "jamesrochabrun",
        "repository": "https://github.com/jamesrochabrun/Claw",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/252",
        "notification_file": "waiting_jamesrochabrun_issue252.md",
    },
    {
        "issue": 253,
        "name": "Claude Codex Api",
        "username": "4xian",
        "repository": "https://github.com/4xian/claude-codex-api",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/253",
        "notification_file": "waiting_4xian_issue253.md",
    },
    {
        "issue": 259,
        "name": "DevRag",
        "username": "tomohiro-owada",
        "repository": "https://github.com/tomohiro-owada/devrag",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/259",
        "notification_file": "waiting_tomohiro-owada_issue259.md",
    },
    {
        "issue": 264,
        "name": "Claude Code Agent SDK Pretty Printer",
        "username": "PepijnSenders",
        "repository": "https://github.com/PepijnSenders/claude-pretty-printer",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/264",
        "notification_file": "waiting_PepijnSenders_issue264.md",
    },
]


def parse_repo_url(repo_url: str) -> tuple[str, str]:
    """Parse GitHub repository URL to extract owner and repo"""
    match = re.match(r'https://github\.com/([^/]+)/([^/]+)/?', repo_url)
    if not match:
        raise ValueError(f"Invalid GitHub repository URL: {repo_url}")
    return match.group(1), match.group(2)


def read_notification_file(filepath: str) -> Optional[str]:
    """Read notification message from file"""
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def has_existing_notification(github_client: Github, owner: str, repo: str, marker: str = "thedotmack/awesome-claude-code") -> bool:
    """Check if we've already created a notification issue in this repository"""
    try:
        repo_obj = github_client.get_repo(f"{owner}/{repo}")
        
        # Check recent issues for our marker
        issues = repo_obj.get_issues(state='all', sort='created', direction='desc')
        for issue in issues[:50]:  # Check last 50 issues
            if marker in issue.body:
                return True
        
        return False
    except GithubException as e:
        print(f"  ⚠️  Error checking existing issues: {e}")
        return False


def create_notification_issue(github_client: Github, owner: str, repo: str, title: str, body: str, dry_run: bool = False) -> bool:
    """Create a notification issue in the developer's repository"""
    try:
        if dry_run:
            print(f"  [DRY RUN] Would create issue in {owner}/{repo}")
            print(f"  [DRY RUN] Title: {title}")
            print(f"  [DRY RUN] Body length: {len(body)} characters")
            return True
        
        repo_obj = github_client.get_repo(f"{owner}/{repo}")
        
        # Check if issues are enabled
        if not repo_obj.has_issues:
            print(f"  ⚠️  Issues are disabled for this repository")
            return False
        
        # Create the issue
        issue = repo_obj.create_issue(title=title, body=body)
        print(f"  ✅ Created issue #{issue.number}: {issue.html_url}")
        return True
        
    except GithubException as e:
        if e.status == 403:
            print(f"  ❌ Permission denied: {e.data.get('message', str(e))}")
        elif e.status == 404:
            print(f"  ❌ Repository not found or private: {owner}/{repo}")
        elif e.status == 410:
            print(f"  ❌ Repository has been deleted or archived")
        else:
            print(f"  ❌ GitHub API error: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Unexpected error: {e}")
        return False


def main():
    """Main function to post all notifications"""
    print("=" * 80)
    print("AWESOME CLAUDE CODE - Post Notifications to Developer Repositories")
    print("=" * 80)
    print()
    
    # Get GitHub token
    github_token = os.environ.get("AWESOME_CC_PAT_PUBLIC_REPO") or os.environ.get("GITHUB_TOKEN")
    if not github_token:
        print("Error: AWESOME_CC_PAT_PUBLIC_REPO or GITHUB_TOKEN environment variable is required")
        print("This token needs 'public_repo' scope to create issues in external repositories")
        sys.exit(1)
    
    # Check for dry run mode
    dry_run = os.environ.get("DRY_RUN", "false").lower() == "true"
    if dry_run:
        print("🔍 DRY RUN MODE - No issues will be created")
        print()
    
    # Initialize GitHub client
    try:
        from github import Auth
        auth = Auth.Token(github_token)
        github_client = Github(auth=auth)
        # Test the token only if not in dry run
        if not dry_run:
            user = github_client.get_user()
            print(f"✅ GitHub authentication successful (user: {user.login})")
        else:
            print(f"✅ GitHub client initialized (dry run mode)")
        print()
    except Exception as e:
        if not dry_run:
            print(f"❌ GitHub authentication failed: {e}")
            sys.exit(1)
        else:
            print(f"⚠️  GitHub authentication failed (continuing in dry run mode)")
            print()
            github_client = None
    
    # Get notifications directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    notifications_dir = os.path.join(repo_root, "outreach", "generated_notifications")
    
    if not os.path.exists(notifications_dir):
        print(f"❌ Notifications directory not found: {notifications_dir}")
        print("Run send_notifications.py first to generate notification files")
        sys.exit(1)
    
    # Combine all developers
    all_developers = REJECTED_DEVELOPERS + WAITING_DEVELOPERS
    
    # Track results
    posted = []
    skipped = []
    failed = []
    
    print(f"Processing {len(all_developers)} notifications...")
    print()
    
    # Post each notification
    for dev in all_developers:
        # Skip if marked to skip
        if dev.get('skip'):
            print(f"Skipping: {dev['name']} (not a GitHub repository)")
            skipped.append(dev)
            continue
        
        print(f"Processing: {dev['name']} (Issue #{dev['issue']})")
        
        # Read notification file
        notification_file = os.path.join(notifications_dir, dev['notification_file'])
        message = read_notification_file(notification_file)
        
        if not message:
            print(f"  ❌ Notification file not found: {dev['notification_file']}")
            failed.append(dev)
            continue
        
        # Parse repository URL
        try:
            owner, repo = parse_repo_url(dev['repository'])
        except ValueError as e:
            print(f"  ❌ {e}")
            failed.append(dev)
            continue
        
        # Check if already posted
        if not dry_run and has_existing_notification(github_client, owner, repo):
            print(f"  ⏭️  Already created notification issue in this repository")
            skipped.append(dev)
            continue
        
        # Create issue title
        issue_title = f"🎉 {dev['name']} is now featured in Awesome Claude Code!"
        
        # Create notification issue
        success = create_notification_issue(github_client, owner, repo, issue_title, message, dry_run)
        
        if success:
            posted.append(dev)
        else:
            failed.append(dev)
        
        print()
    
    # Print summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total notifications processed: {len(all_developers)}")
    print(f"Posted: {len(posted)}")
    print(f"Skipped: {len(skipped)}")
    print(f"Failed: {len(failed)}")
    print()
    
    if posted:
        print("✅ Successfully created notification issues:")
        for dev in posted:
            print(f"   - {dev['name']} → {dev['repository']}")
        print()
    
    if skipped:
        print("⏭️  Skipped:")
        for dev in skipped:
            reason = "(not a GitHub repo)" if dev.get('skip') else "(already notified)"
            print(f"   - {dev['name']} {reason}")
        print()
    
    if failed:
        print("❌ Failed to create issue:")
        for dev in failed:
            print(f"   - {dev['name']} → {dev['repository']}")
        print()
    
    if dry_run:
        print("🔍 This was a DRY RUN - no issues were actually created")
        print("Set DRY_RUN=false to post for real")
    else:
        print("✅ All developers have been notified in their own repositories!")
    
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())

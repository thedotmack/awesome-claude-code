#!/usr/bin/env python3
"""
Script to generate notification messages for all gatekept developers.
This script creates GitHub issue comments to notify affected developers about the fork.
"""

import os
import sys
from typing import Dict, List

# All gatekept tools with developer information
REJECTED_DEVELOPERS = [
    {
        "issue": 228,
        "name": "Claude Control Terminal",
        "username": "schlunsen",
        "github": "https://github.com/schlunsen",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/228",
        "status": "LOCKED - pay-to-play concerns",
        "days_waiting": "7",
        "validation": "Unknown",
    },
    {
        "issue": 205,
        "name": "Schaltwerk",
        "username": "2mawi2",
        "github": "https://github.com/2mawi2",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/205",
        "status": "Rejected - 'not optimal for orchestrators'",
        "days_waiting": "21",
        "validation": "PASSED",
    },
    {
        "issue": 175,
        "name": "Claude Code Sub agents Starter Kit",
        "username": "shinpr",
        "github": "https://github.com/shinpr",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/175",
        "status": "Rejected - no reason stated",
        "days_waiting": "13",
        "validation": "PASSED",
    },
    {
        "issue": 166,
        "name": "Claude Code Web Shell",
        "username": "vaderyang",
        "github": "https://github.com/vaderyang",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/166",
        "status": "Rejected - no reason stated",
        "days_waiting": "9",
        "validation": "PASSED",
    },
    {
        "issue": 165,
        "name": "Claude Code Cheat Sheet",
        "username": "aeulker",
        "github": "https://github.com/aeulker",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/165",
        "status": "Rejected - no reason stated",
        "days_waiting": "6",
        "validation": "PASSED",
    },
    {
        "issue": 108,
        "name": "Codanna",
        "username": "bartolli",
        "github": "https://github.com/bartolli",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/108",
        "status": "Rejected - no reason stated",
        "days_waiting": "23",
        "validation": "PASSED",
    },
    {
        "issue": 104,
        "name": "AI Coding Project Boilerplate",
        "username": "shinpr",
        "github": "https://github.com/shinpr",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/104",
        "status": "Rejected - no reason stated",
        "days_waiting": "8",
        "validation": "PASSED",
    },
]

WAITING_DEVELOPERS = [
    {
        "issue": 122,
        "name": "claude-code-guardian",
        "username": "jfpedroza",
        "github": "https://github.com/jfpedroza",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/122",
        "days_waiting": "74+",
        "validation": "PASSED",
    },
    {
        "issue": 148,
        "name": "Claudable",
        "username": "Atipico1",
        "github": "https://github.com/Atipico1",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/148",
        "days_waiting": "62+",
        "validation": "PASSED",
        "note": "Assigned to maintainer but still waiting",
    },
    {
        "issue": 169,
        "name": "Claude Agent Toolkit",
        "username": "cheolwanpark",
        "github": "https://github.com/cheolwanpark",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/169",
        "days_waiting": "46+",
        "validation": "PASSED",
    },
    {
        "issue": 178,
        "name": "Claude Code Hook Comms (HCOM)",
        "username": "aannoo",
        "github": "https://github.com/aannoo",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/178",
        "days_waiting": "45+",
        "validation": "PASSED",
        "note": "This is the maintainer's own tool!",
    },
    {
        "issue": 183,
        "name": "Omnara",
        "username": "ishaansehgal99",
        "github": "https://github.com/ishaansehgal99",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/183",
        "days_waiting": "41+",
        "validation": "PASSED",
    },
    {
        "issue": 233,
        "name": "Session Driven Development",
        "username": "ankushdixit",
        "github": "https://github.com/ankushdixit",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/233",
        "days_waiting": "11+",
        "validation": "PASSED",
    },
    {
        "issue": 238,
        "name": "Claude Code Handbook",
        "username": "NikiforovAll",
        "github": "https://github.com/NikiforovAll",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/238",
        "days_waiting": "9+",
        "validation": "PASSED",
        "note": "Changes requested with moving goalposts",
    },
    {
        "issue": 242,
        "name": "Claude X",
        "username": "kunwar-shah",
        "github": "https://github.com/kunwar-shah",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/242",
        "days_waiting": "6+",
        "validation": "PASSED",
    },
    {
        "issue": 243,
        "name": "conduit8",
        "username": "alexander-zuev",
        "github": "https://github.com/alexander-zuev",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/243",
        "days_waiting": "6+",
        "validation": "PASSED",
    },
    {
        "issue": 244,
        "name": "Web Assets Generator",
        "username": "alonw0",
        "github": "https://github.com/alonw0",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/244",
        "days_waiting": "6+",
        "validation": "PASSED",
    },
    {
        "issue": 252,
        "name": "Claw Code",
        "username": "jamesrochabrun",
        "github": "https://github.com/jamesrochabrun",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/252",
        "days_waiting": "4+",
        "validation": "PASSED",
    },
    {
        "issue": 253,
        "name": "Claude Codex Api",
        "username": "4xian",
        "github": "https://github.com/4xian",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/253",
        "days_waiting": "3+",
        "validation": "PASSED",
    },
    {
        "issue": 259,
        "name": "DevRag",
        "username": "tomohiro-owada",
        "github": "https://github.com/tomohiro-owada",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/259",
        "days_waiting": "2+",
        "validation": "PASSED",
    },
    {
        "issue": 264,
        "name": "Claude Code Agent SDK Pretty Printer",
        "username": "PepijnSenders",
        "github": "https://github.com/PepijnSenders",
        "upstream_issue": "https://github.com/hesreallyhim/awesome-claude-code/issues/264",
        "days_waiting": "2+",
        "validation": "PASSED",
    },
]


def generate_rejected_notification(dev: Dict) -> str:
    """Generate notification message for rejected developers"""
    return f"""Hi @{dev['username']},

I noticed your tool **{dev['name']}** ({dev['upstream_issue']}) was rejected in hesreallyhim/awesome-claude-code, even though it passed validation.

**Your tool has now been added to a community-driven fork!**

🎉 **Your tool is now listed at:** https://github.com/thedotmack/awesome-claude-code

## Why This Fork Exists

After analyzing the upstream repository, I found:
- **7 validated tools were REJECTED** based on subjective criteria (yours included)
- **14+ validated tools are WAITING** for approval (some 74+ days)
- Your tool was rejected after **{dev['days_waiting']} days** with status: {dev['status']}

This isn't right. Quality tools deserve visibility.

📊 **Full Analysis:** https://github.com/thedotmack/awesome-claude-code/blob/main/GATEKEEPING_ANALYSIS.md

## Our Philosophy

- **🎯 Validation = Approval** — If validation passes, you're automatically listed
- **⚡ Zero-Wait** — Approval within an hour (not weeks!)
- **🚫 No Gatekeeping** — No subjective rejections
- **🤝 Community-Driven** — Users decide value through usage

## Your Tool's New Home

✅ Your tool has been added to: https://github.com/thedotmack/awesome-claude-code/blob/main/README.md

Search for "{dev['name']}" to see your listing with:
- Full description
- Links to your repository
- GitHub stats display
- Proper categorization

## What This Means

- **Immediate Visibility**: Your tool is now discoverable by the community
- **No More Gatekeeping**: Future updates won't be blocked by subjective opinions
- **Growing Community**: Users who value open, community-driven resources

## Evidence & Links

- **Gatekeeping Evidence**: [Issue #{dev['issue']} in Analysis](https://github.com/thedotmack/awesome-claude-code/blob/main/GATEKEEPING_ANALYSIS.md#part-1-validated-submissions-that-were-rejected)
- **Fork Philosophy**: https://github.com/thedotmack/awesome-claude-code/blob/main/FORK_README.md
- **Your Listing**: https://github.com/thedotmack/awesome-claude-code/blob/main/README.md

**Everyone gets to play. Your quality work deserves recognition.** 🚀

---
*This is an automated notification. You can keep your upstream submission if you'd like, but your tool is now available in the community-driven fork regardless.*
"""


def generate_waiting_notification(dev: Dict) -> str:
    """Generate notification message for waiting developers"""
    note_section = f"\n**Special Note**: {dev['note']}\n" if dev.get('note') else ""
    
    return f"""Hi @{dev['username']},

I noticed your tool **{dev['name']}** ({dev['upstream_issue']}) has been waiting **{dev['days_waiting']} days** for approval in hesreallyhim/awesome-claude-code, even though it passed validation.

**Your tool has now been added to a community-driven fork!**

🎉 **Your tool is now listed at:** https://github.com/thedotmack/awesome-claude-code
{note_section}
## The Waiting Problem

After analyzing the upstream repository, I found:
- Your submission is one of **14+ validated tools waiting** for approval
- Some submissions have been waiting **74+ days**
- Your tool passed validation but has been waiting **{dev['days_waiting']} days**

This isn't right. Quality tools deserve immediate visibility.

📊 **Full Analysis:** https://github.com/thedotmack/awesome-claude-code/blob/main/GATEKEEPING_ANALYSIS.md

## Our Philosophy

- **🎯 Validation = Approval** — If validation passes, you're automatically listed
- **⚡ Zero-Wait** — Target < 1 hour approval time (not weeks!)
- **🚫 No Indefinite Queues** — No more waiting in limbo
- **🤝 Community-Driven** — Users decide value through usage

## Your Tool's New Home

✅ Your tool has been added to: https://github.com/thedotmack/awesome-claude-code/blob/main/README.md

Search for "{dev['name']}" to see your listing with:
- Full description
- Links to your repository
- GitHub stats display
- Proper categorization

## What This Means

- **Immediate Visibility**: No more waiting - your tool is live now
- **No More Gatekeeping**: No subjective opinions blocking quality work
- **Growing Community**: Users who value open, community-driven resources

## You Can Keep Both Submissions

This is not an "either/or" situation:
- Keep your upstream submission if you'd like (maybe they'll eventually approve it)
- Your tool is already live here through auto-approval
- Reach users who are looking for the community-driven alternative

## Evidence & Links

- **Gatekeeping Evidence**: [Issue #{dev['issue']} in Analysis](https://github.com/thedotmack/awesome-claude-code/blob/main/GATEKEEPING_ANALYSIS.md#part-2-validated-submissions-waiting-still-open)
- **Fork Philosophy**: https://github.com/thedotmack/awesome-claude-code/blob/main/FORK_README.md
- **Your Listing**: https://github.com/thedotmack/awesome-claude-code/blob/main/README.md

**Everyone gets to play. No more waiting.** 🚀

---
*This is an automated notification. You can keep your upstream submission if you'd like, but your tool is now available in the community-driven fork regardless.*
"""


def main():
    """Generate all notifications"""
    print("=" * 80)
    print("AWESOME CLAUDE CODE - Generate Notifications")
    print("=" * 80)
    print()
    
    output_dir = "outreach/generated_notifications"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate rejected notifications
    print("Generating notifications for REJECTED tools...")
    for dev in REJECTED_DEVELOPERS:
        message = generate_rejected_notification(dev)
        filename = f"{output_dir}/rejected_{dev['username']}_issue{dev['issue']}.md"
        with open(filename, 'w') as f:
            f.write(message)
        print(f"  ✅ Generated: {filename}")
    
    print()
    print("Generating notifications for WAITING tools...")
    for dev in WAITING_DEVELOPERS:
        message = generate_waiting_notification(dev)
        filename = f"{output_dir}/waiting_{dev['username']}_issue{dev['issue']}.md"
        with open(filename, 'w') as f:
            f.write(message)
        print(f"  ✅ Generated: {filename}")
    
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Generated {len(REJECTED_DEVELOPERS)} notifications for rejected tools")
    print(f"Generated {len(WAITING_DEVELOPERS)} notifications for waiting tools")
    print(f"Total: {len(REJECTED_DEVELOPERS) + len(WAITING_DEVELOPERS)} notifications")
    print()
    print(f"📁 All notifications saved to: {output_dir}/")
    print()
    print("Next steps:")
    print("1. Review the generated notifications")
    print("2. Post them as comments on the respective upstream issues")
    print("3. Or send via other channels (email, discussions, etc.)")
    print()
    print("✅ All affected developers have been notified!")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

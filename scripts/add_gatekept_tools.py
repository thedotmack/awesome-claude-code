#!/usr/bin/env python3
"""
Script to extract gatekept tools from GATEKEEPING_ANALYSIS.md and add them to THE_RESOURCES_TABLE.csv
This script automates the process of adding all validated-but-rejected/waiting tools to the repository.
"""

import csv
import os
import sys
import re
from datetime import datetime
from typing import Dict, List

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from resource_id import generate_resource_id
except ImportError:
    from scripts.resource_id import generate_resource_id

# Map of categories from gatekeeping analysis to our category system
CATEGORY_MAP = {
    "Tooling: Orchestrators": "Tooling",
    "Tooling: IDE Integrations": "Tooling",
    "Tooling: General": "Tooling",
    "Tooling: Usage Monitors": "Tooling",
    "Tooling": "Tooling",
    "Workflows & Knowledge Guides": "Workflows & Knowledge Guides",
    "CLAUDE.md Files": "CLAUDE.md Files",
    "CLAUDE.md Files: Project Scaffolding & MCP": "CLAUDE.md Files",
    "Hooks": "Hooks",
    "Agent Skills": "Agent Skills",
    "Slash-Commands: Project & Task Management": "Slash-Commands",
    "Output Styles": "Output Styles",
}

# All gatekept tools extracted from GATEKEEPING_ANALYSIS.md
GATEKEPT_TOOLS = [
    # REJECTED TOOLS (7)
    {
        "issue": 228,
        "name": "Claude Control Terminal",
        "author": "schlunsen",
        "author_link": "https://github.com/schlunsen",
        "category": "Tooling: General",
        "repository": "https://github.com/schlunsen/claude-control-terminal",
        "license": "MIT",
        "description": "High-performance Go port of claude-code-templates providing component installation (600+ agents, 200+ commands, MCPs), Docker containerization, real-time analytics dashboard with WebSocket monitoring, and cross-platform deployment. Features 10-50x faster startup and 3-5x lower memory usage compared to Node.js alternatives.",
        "status": "rejected",
        "validation": "unknown",
    },
    {
        "issue": 205,
        "name": "Schaltwerk",
        "author": "Marius Wichtner",
        "author_link": "https://github.com/2mawi2",
        "category": "Tooling: Orchestrators",
        "repository": "https://github.com/2mawi2/schaltwerk",
        "license": "MIT",
        "description": "Schaltwerk is a macOS Tauri desktop app that runs multiple terminal agents (Claude, Codex, OpenCode, Gemini-CLI) in parallel. Each session is isolated in its own git worktree/branch and includes a driving spec plus multiple terminals for running and testing. The keyboard-first, spec-driven workflow and local diff review keep humans in control.",
        "status": "rejected",
        "validation": "passed",
    },
    {
        "issue": 175,
        "name": "Claude Code Sub agents Starter Kit",
        "author": "shinpr",
        "author_link": "https://github.com/shinpr",
        "category": "CLAUDE.md Files",
        "repository": "https://github.com/shinpr/ai-coding-project-boilerplate",
        "secondary": "https://dev.to/shinpr/zero-context-exhaustion-building-production-ready-ai-coding-teams-with-claude-code-sub-agents-31b",
        "license": "MIT",
        "description": "Comprehensive Claude Code configuration featuring 11 specialized Sub agents with independent contexts and rule-based development system - maintains production-grade TypeScript quality across 770K+ token sessions without context exhaustion.",
        "status": "rejected",
        "validation": "passed",
    },
    {
        "issue": 166,
        "name": "Claude Code Web Shell",
        "author": "vaderyang",
        "author_link": "https://github.com/vaderyang",
        "category": "Tooling: Orchestrators",
        "repository": "https://github.com/vaderyang/claudecode_web_shell",
        "license": "MIT",
        "description": "A web-based terminal interface for Claude Code that allows you to interact with Claude Code through your browser.",
        "status": "rejected",
        "validation": "passed",
    },
    {
        "issue": 165,
        "name": "Claude Code Cheat Sheet",
        "author": "aeulker",
        "author_link": "https://github.com/aeulker",
        "category": "Workflows & Knowledge Guides",
        "repository": "https://github.com/aeulker/Claude-Code-Cheat-Sheet",
        "license": "MIT",
        "description": "Claude Code Cheat Sheet - A comprehensive reference guide for Claude Code workflows and best practices.",
        "status": "rejected",
        "validation": "passed",
    },
    {
        "issue": 108,
        "name": "Codanna",
        "author": "bartolli",
        "author_link": "https://github.com/bartolli",
        "category": "Tooling: IDE Integrations",
        "repository": "https://github.com/bartolli/codanna",
        "license": "Apache-2.0",
        "description": "Semantic code search and relationship tracking via MCP and Unix CLI. Features 91,318 symbols/sec parsing, Tree-sitter AST parsing for Rust and Python, 384-dimensional vectors, Tantivy full-text search, <10ms lookups, ~300ms MCP response time. FNV-1a hashed lookups with memory-mapped storage and specialized caches.",
        "status": "rejected",
        "validation": "passed",
    },
    {
        "issue": 104,
        "name": "AI Coding Project Boilerplate",
        "author": "shinpr",
        "author_link": "https://github.com/shinpr",
        "category": "CLAUDE.md Files: Project Scaffolding & MCP",
        "repository": "https://github.com/shinpr/ai-coding-project-boilerplate",
        "license": "MIT",
        "description": "TypeScript boilerplate designed for AI-driven development with 10+ specialized sub-agents, preventive control mechanisms, and automated quality gates that enable Claude Code to work autonomously while maintaining production standards.",
        "status": "rejected",
        "validation": "passed",
    },
    # WAITING TOOLS (14)
    {
        "issue": 122,
        "name": "claude-code-guardian",
        "author": "jfpedroza",
        "author_link": "https://github.com/jfpedroza",
        "category": "Hooks",
        "repository": "https://github.com/jfpedroza/claude-code-guardian",
        "license": "MIT",
        "description": "Validation and permission system for Claude Code focused on controlling what Claude Code can execute, read or write. Allows users to define a set of rules to evaluate. E.g., allow `git push` but not `git push --force`.",
        "status": "waiting",
        "validation": "passed",
    },
    {
        "issue": 148,
        "name": "Claudable",
        "author": "Ethan Park",
        "author_link": "https://github.com/Atipico1",
        "category": "Tooling",
        "repository": "https://github.com/opactorai/Claudable",
        "license": "MIT",
        "description": "Claudable is an open-source web builder that leverages local CLI agents, such as Claude Code and Cursor Agent, to build and deploy products effortlessly. OpenSource Lovable that runs locally.",
        "status": "waiting",
        "validation": "passed",
    },
    {
        "issue": 169,
        "name": "Claude Agent Toolkit",
        "author": "Cheolwan Park",
        "author_link": "https://github.com/cheolwanpark",
        "category": "Tooling: Orchestrators",
        "repository": "https://github.com/cheolwanpark/claude-agent-toolkit",
        "secondary": "https://pypi.org/project/claude-agent-toolkit/",
        "license": "MIT",
        "description": "A Python framework that wraps claude-code-sdk to provide better developer experience through decorator-based tools, runtime isolation, and simplified agent development. Built for production safety with Docker containers. Features simple class-based definition with @tool decorator, built-in parallel execution, and FileSystemTool with permission control.",
        "status": "waiting",
        "validation": "passed",
    },
    {
        "issue": 178,
        "name": "Claude Code Hook Comms (HCOM)",
        "author": "aannoo",
        "author_link": "https://github.com/aannoo",
        "category": "Hooks",
        "repository": "https://github.com/aannoo/claude-hook-comms",
        "secondary": "https://pypi.org/project/hcom",
        "license": "MIT",
        "description": "Lightweight CLI tool for real-time communication between Claude Code sub agents using hooks. Enables multi-agent collaboration with @-mention targeting, live dashboard monitoring, and zero-dependency implementation.",
        "status": "waiting",
        "validation": "passed",
    },
    {
        "issue": 183,
        "name": "Omnara",
        "author": "Ishaan Sehgal",
        "author_link": "https://github.com/ishaansehgal99",
        "category": "Tooling",
        "repository": "https://github.com/omnara-ai/omnara",
        "secondary": "https://omnara.com",
        "license": "Apache-2.0",
        "description": "A command center for AI agents that syncs Claude Code sessions across terminal, web, and mobile. Allows for remote monitoring, human-in-the-loop interaction, and team collaboration. Recently open-sourced web and mobile applications.",
        "status": "waiting",
        "validation": "passed",
    },
    {
        "issue": 233,
        "name": "Session Driven Development",
        "author": "Ankush Dixit",
        "author_link": "https://github.com/ankushdixit",
        "category": "Slash-Commands: Project & Task Management",
        "repository": "https://github.com/ankushdixit/sdd",
        "license": "MIT",
        "description": "SDD implements Session-Driven Development, a comprehensive methodology that enables AI coding assistants to work on software projects across multiple sessions with perfect context continuity, enforced quality standards, and accumulated institutional knowledge.",
        "status": "waiting",
        "validation": "passed",
    },
    {
        "issue": 238,
        "name": "Claude Code Handbook",
        "author": "nikiforovall",
        "author_link": "https://github.com/NikiforovAll",
        "category": "Workflows & Knowledge Guides",
        "repository": "https://nikiforovall.blog/claude-code-rules/",
        "license": "MIT",
        "description": "Collection of best practices, tips, and techniques for Claude Code development workflows, enhanced with distributable plugins. Covers practical technique guides for beginners and advanced users.",
        "status": "waiting",
        "validation": "passed",
    },
    {
        "issue": 242,
        "name": "Claude X",
        "author": "Kunwar Shah",
        "author_link": "https://github.com/kunwar-shah",
        "category": "Output Styles",
        "repository": "https://github.com/kunwar-shah/claudex",
        "secondary": "https://kunwar-shah.github.io/claudex/#/",
        "license": "MIT",
        "description": "Claudex - A friendly viewer, Browse and explore your Claude conversations. Features auto project discovery (scans ~/.claude/projects), SQLite FTS5-powered full-text search, session analytics, and export options (JSON, HTML, TXT).",
        "status": "waiting",
        "validation": "passed",
    },
    {
        "issue": 243,
        "name": "conduit8",
        "author": "Alexander Zuev",
        "author_link": "https://github.com/alexander-zuev",
        "category": "Tooling",
        "repository": "https://github.com/conduit8/conduit8",
        "secondary": "https://conduit8.dev",
        "license": "AGPL-3.0",
        "description": "CLI registry for discovering, installing, and managing Claude Code skills. Search 20+ curated skills by keyword or category, install directly to ~/.claude/skills/ with one command. Like context7 for Claude Code skills. Available via npx - no global installation required.",
        "status": "waiting",
        "validation": "passed",
    },
    {
        "issue": 244,
        "name": "Web Assets Generator",
        "author": "Alon Wolenitz",
        "author_link": "https://github.com/alonw0",
        "category": "Agent Skills",
        "repository": "https://github.com/alonw0/web-asset-generator",
        "license": "MIT",
        "description": "Easily generate web assets from Claude Code including favicons, app icons (PWA), and social media meta images (Open Graph) for Facebook, Twitter, WhatsApp, and LinkedIn. Handles image resizing, text-to-image generation, emojis, and provides proper HTML meta tags.",
        "status": "waiting",
        "validation": "passed",
    },
    {
        "issue": 252,
        "name": "Claw Code",
        "author": "James Rochabrun",
        "author_link": "https://github.com/jamesrochabrun",
        "category": "Tooling: IDE Integrations",
        "repository": "https://github.com/jamesrochabrun/Claw",
        "license": "MIT",
        "description": "A friendly macOS app for Claude Code. Uses Claude Code SDK to bring most of the well known features from Claude Code to a macOS app. In addition uses accessibility API to inspect Xcode workspaces making it a great tool for iOS engineers.",
        "status": "waiting",
        "validation": "passed",
    },
    {
        "issue": 253,
        "name": "Claude Codex Api",
        "author": "4xian",
        "author_link": "https://github.com/4xian",
        "category": "Tooling",
        "repository": "https://github.com/4xian/claude-codex-api",
        "secondary": "https://github.com/4xian/claude-codex-api/blob/master/README_EN.md",
        "license": "MIT",
        "description": "A CLI tool for managing Claude Code and Codex configurations, allowing one-click switching between multiple transit station API configurations; One-click switching of system environment variables, one-click testing of API latency/validity, automatic optimal route switching with internationalization support.",
        "status": "waiting",
        "validation": "passed",
    },
    {
        "issue": 259,
        "name": "DevRag",
        "author": "Tomohiro Owada",
        "author_link": "https://github.com/tomohiro-owada",
        "category": "Tooling: General",
        "repository": "https://github.com/tomohiro-owada/devrag",
        "license": "MIT",
        "description": "Lightweight local RAG system for Claude Code that uses vector search to retrieve only relevant document chunks, reducing token usage by 40x and search time by 15x compared to reading entire files.",
        "status": "waiting",
        "validation": "passed",
    },
    {
        "issue": 264,
        "name": "Claude Code Agent SDK Pretty Printer",
        "author": "PepijnSenders",
        "author_link": "https://github.com/PepijnSenders",
        "category": "Tooling: General",
        "repository": "https://github.com/PepijnSenders/claude-pretty-printer",
        "license": "MIT",
        "description": "A lightweight utility that transforms raw Claude Agent SDK JSON messages into beautiful, readable CLI output with color-coded boxes and professional formatting.",
        "status": "waiting",
        "validation": "passed",
    },
]


def get_csv_path():
    """Get the path to THE_RESOURCES_TABLE.csv"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    return os.path.join(repo_root, "THE_RESOURCES_TABLE.csv")


def read_existing_resources():
    """Read existing resources from CSV to avoid duplicates"""
    csv_path = get_csv_path()
    existing = set()
    
    if not os.path.exists(csv_path):
        return existing
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Store repository URL to check for duplicates
            existing.add(row['Primary Link'].strip().lower())
    
    return existing


def add_tool_to_csv(tool: Dict) -> bool:
    """Add a single tool to THE_RESOURCES_TABLE.csv"""
    csv_path = get_csv_path()
    
    # Map category
    category = CATEGORY_MAP.get(tool['category'], 'Tooling')
    
    # Generate resource ID
    resource_id = generate_resource_id(tool['name'], tool['repository'], category)
    
    # Prepare row data
    now = datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
    row = {
        'ID': resource_id,
        'Display Name': tool['name'],
        'Category': category,
        'Sub-Category': 'General',
        'Primary Link': tool['repository'],
        'Secondary Link': tool.get('secondary', ''),
        'Author Name': tool['author'],
        'Author Link': tool['author_link'],
        'Active': 'TRUE',
        'Date Added': now,
        'Last Modified': '',
        'Last Checked': now,
        'License': tool['license'],
        'Description': tool['description'],
        'Removed From Origin': 'FALSE',
    }
    
    # Append to CSV
    with open(csv_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        writer.writerow(row)
    
    return True


def main():
    """Main function to add all gatekept tools"""
    print("=" * 80)
    print("AWESOME CLAUDE CODE - Add Gatekept Tools")
    print("=" * 80)
    print()
    print(f"This script will add {len(GATEKEPT_TOOLS)} gatekept tools to the repository.")
    print()
    
    # Read existing resources
    print("Reading existing resources...")
    existing = read_existing_resources()
    print(f"Found {len(existing)} existing resources")
    print()
    
    # Track additions
    added = []
    skipped = []
    
    # Add each tool
    for tool in GATEKEPT_TOOLS:
        repo_url = tool['repository'].strip().lower()
        
        if repo_url in existing:
            print(f"⏭️  SKIPPED: {tool['name']} (already exists)")
            skipped.append(tool)
        else:
            try:
                add_tool_to_csv(tool)
                print(f"✅ ADDED: {tool['name']} (Issue #{tool['issue']})")
                added.append(tool)
            except Exception as e:
                print(f"❌ ERROR adding {tool['name']}: {e}")
    
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total tools processed: {len(GATEKEPT_TOOLS)}")
    print(f"Added: {len(added)}")
    print(f"Skipped (already exists): {len(skipped)}")
    print()
    
    if added:
        print("✅ Successfully added gatekept tools to THE_RESOURCES_TABLE.csv")
        print()
        print("Next steps:")
        print("1. Run generate_readme.py to regenerate the README")
        print("2. Review the changes")
        print("3. Commit and push")
    else:
        print("⚠️  No new tools were added (all already exist)")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

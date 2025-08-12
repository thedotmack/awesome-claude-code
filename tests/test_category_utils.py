#!/usr/bin/env python3
"""
Unit tests for the CategoryManager class.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.category_utils import category_manager


def test_get_all_categories():
    """Test getting all category names."""
    categories = category_manager.get_all_categories()

    # Check we have the expected categories
    assert "Workflows & Knowledge Guides" in categories
    assert "Tooling" in categories
    assert "Statusline" in categories
    assert "Hooks" in categories
    assert "Slash-Commands" in categories
    assert "CLAUDE.md Files" in categories
    assert "Official Documentation" in categories

    # Check count
    assert len(categories) == 7


def test_get_category_prefixes():
    """Test getting category ID prefixes."""
    prefixes = category_manager.get_category_prefixes()

    # Check specific mappings
    assert prefixes["Workflows & Knowledge Guides"] == "wf"
    assert prefixes["Tooling"] == "tool"
    assert prefixes["Statusline"] == "status"
    assert prefixes["Hooks"] == "hook"
    assert prefixes["Slash-Commands"] == "cmd"
    assert prefixes["CLAUDE.md Files"] == "claude"
    assert prefixes["Official Documentation"] == "doc"


def test_get_category_by_name():
    """Test retrieving category by name."""
    # Test existing category
    statusline = category_manager.get_category_by_name("Statusline")
    assert statusline is not None
    assert statusline["id"] == "statusline"
    assert statusline["prefix"] == "status"
    assert statusline["icon"] == "📊"

    # Test non-existent category
    nonexistent = category_manager.get_category_by_name("NonExistent")
    assert nonexistent is None


def test_get_category_by_id():
    """Test retrieving category by ID."""
    # Test existing category
    tooling = category_manager.get_category_by_id("tooling")
    assert tooling is not None
    assert tooling["name"] == "Tooling"
    assert tooling["prefix"] == "tool"

    # Test non-existent category
    nonexistent = category_manager.get_category_by_id("nonexistent")
    assert nonexistent is None


def test_get_all_subcategories():
    """Test getting all subcategories with parent info."""
    subcategories = category_manager.get_all_subcategories()

    # Check we have subcategories
    assert len(subcategories) > 0

    # Check specific subcategory
    ide_integration = next((s for s in subcategories if s["name"] == "IDE Integrations"), None)
    assert ide_integration is not None
    assert ide_integration["parent"] == "Tooling"
    assert ide_integration["full_name"] == "Tooling: IDE Integrations"


def test_get_subcategories_for_category():
    """Test getting subcategories for a specific category."""
    # Category with subcategories
    slash_cmd_subs = category_manager.get_subcategories_for_category("Slash-Commands")
    assert "Version Control & Git" in slash_cmd_subs
    assert "Code Analysis & Testing" in slash_cmd_subs
    assert len(slash_cmd_subs) == 7

    # Category without subcategories
    statusline_subs = category_manager.get_subcategories_for_category("Statusline")
    assert statusline_subs == []


def test_validate_category_subcategory():
    """Test validation of category-subcategory relationships."""
    # Valid combinations
    assert category_manager.validate_category_subcategory("Tooling", "IDE Integrations") is True
    assert category_manager.validate_category_subcategory("Slash-Commands", "Version Control & Git") is True

    # No subcategory (always valid)
    assert category_manager.validate_category_subcategory("Statusline", "") is True
    assert category_manager.validate_category_subcategory("Statusline", None) is True

    # Invalid combinations
    assert category_manager.validate_category_subcategory("Tooling", "Version Control & Git") is False
    assert category_manager.validate_category_subcategory("NonExistent", "Something") is False


def test_get_categories_for_readme():
    """Test getting categories ordered for README generation."""
    categories = category_manager.get_categories_for_readme()

    # Check ordering by verifying first few
    assert categories[0]["id"] == "workflows"  # order: 1
    assert categories[1]["id"] == "tooling"  # order: 2
    assert categories[2]["id"] == "statusline"  # order: 3

    # All categories should be present
    assert len(categories) == 7


def test_get_toc_config():
    """Test getting table of contents configuration."""
    toc_config = category_manager.get_toc_config()

    # Check expected TOC settings
    assert toc_config["style"] == "custom"
    assert toc_config["symbol"] == "▪"
    assert toc_config["subsymbol"] == "▫"
    assert "indent" in toc_config
    assert "subindent" in toc_config


def test_singleton_behavior():
    """Test that CategoryManager behaves as a singleton."""
    from scripts.category_utils import CategoryManager

    # Create new instances
    instance1 = CategoryManager()
    instance2 = CategoryManager()

    # They should be the same object
    assert instance1 is instance2
    assert instance1 is category_manager


if __name__ == "__main__":
    # Run all tests
    test_functions = [
        test_get_all_categories,
        test_get_category_prefixes,
        test_get_category_by_name,
        test_get_category_by_id,
        test_get_all_subcategories,
        test_get_subcategories_for_category,
        test_validate_category_subcategory,
        test_get_categories_for_readme,
        test_get_toc_config,
        test_singleton_behavior,
    ]

    passed = 0
    failed = 0

    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ {test_func.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"✗ {test_func.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__}: Unexpected error: {e}")
            failed += 1

    print(f"\nTests: {passed} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)

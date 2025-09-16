#!/usr/bin/env python3
"""Tests for README generation functions."""

import os
import sys
import tempfile
import unittest
from datetime import datetime

import yaml

# Add the scripts directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

try:
    from generate_readme import (  # type: ignore
        generate_toc_from_categories,
        get_anchor_suffix_for_icon,
        load_announcements,
        parse_resource_date,
    )
except ImportError:
    from scripts.generate_readme import (
        generate_toc_from_categories,
        get_anchor_suffix_for_icon,
        load_announcements,
        parse_resource_date,
    )


class TestParseResourceDate(unittest.TestCase):
    """Test cases for the parse_resource_date function."""

    def test_parse_date_only_format(self):
        """Test parsing YYYY-MM-DD format."""
        result = parse_resource_date("2025-08-07")
        expected = datetime(2025, 8, 7)
        self.assertEqual(result, expected)

    def test_parse_date_with_timestamp_format(self):
        """Test parsing YYYY-MM-DD:HH-MM-SS format."""
        result = parse_resource_date("2025-08-07:18-26-57")
        expected = datetime(2025, 8, 7, 18, 26, 57)
        self.assertEqual(result, expected)

    def test_parse_with_whitespace(self):
        """Test parsing with leading/trailing whitespace."""
        result = parse_resource_date("  2025-08-07  ")
        expected = datetime(2025, 8, 7)
        self.assertEqual(result, expected)

    def test_parse_empty_string(self):
        """Test parsing empty string returns None."""
        result = parse_resource_date("")
        self.assertIsNone(result)

    def test_parse_none(self):
        """Test parsing None returns None."""
        result = parse_resource_date(None)
        self.assertIsNone(result)

    def test_parse_invalid_format(self):
        """Test parsing invalid date format returns None."""
        invalid_formats = [
            "2025/08/07",  # Wrong separator
            "07-08-2025",  # Wrong order
            "2025-13-01",  # Invalid month
            "2025-08-32",  # Invalid day
            "not-a-date",  # Complete nonsense
            "2025-08-07 18:26:57",  # Space instead of colon
        ]

        for invalid_date in invalid_formats:
            with self.subTest(invalid_date=invalid_date):
                result = parse_resource_date(invalid_date)
                self.assertIsNone(result, f"Expected None for invalid date: {invalid_date}")

    def test_parse_various_timestamps(self):
        """Test parsing various valid timestamp formats."""
        test_cases = [
            ("2025-08-05:11-48-39", datetime(2025, 8, 5, 11, 48, 39)),
            ("2025-07-29:18-37-05", datetime(2025, 7, 29, 18, 37, 5)),
            ("2025-08-07:00-00-00", datetime(2025, 8, 7, 0, 0, 0)),
            ("2025-12-31:23-59-59", datetime(2025, 12, 31, 23, 59, 59)),
        ]

        for date_string, expected in test_cases:
            with self.subTest(date_string=date_string):
                result = parse_resource_date(date_string)
                self.assertEqual(result, expected, f"Failed to parse: {date_string}")

    def test_date_comparison(self):
        """Test that parsed dates can be compared correctly."""
        date1 = parse_resource_date("2025-08-07")
        date2 = parse_resource_date("2025-08-05")
        date3 = parse_resource_date("2025-08-07:18-26-57")

        if date1 and date2 and date3:
            self.assertTrue(date1 > date2)
            self.assertTrue(date3 > date1)  # Same date but with time
            self.assertFalse(date2 > date1)


class TestGetAnchorSuffix(unittest.TestCase):
    """Test cases for the get_anchor_suffix_for_icon function."""

    def test_no_icon(self):
        """Test empty icon returns empty string."""
        self.assertEqual(get_anchor_suffix_for_icon(""), "")
        self.assertEqual(get_anchor_suffix_for_icon(None), "")

    def test_simple_emoji(self):
        """Test simple emoji returns dash."""
        self.assertEqual(get_anchor_suffix_for_icon("🎯"), "-")
        self.assertEqual(get_anchor_suffix_for_icon("💡"), "-")
        self.assertEqual(get_anchor_suffix_for_icon("🔧"), "-")

    def test_emoji_with_variation_selector(self):
        """Test emoji with VS-16 returns URL-encoded suffix."""
        # Classical Building emoji with VS-16
        self.assertEqual(get_anchor_suffix_for_icon("🏛️"), "-%EF%B8%8F")


class TestGenerateTOC(unittest.TestCase):
    """Test cases for the generate_toc_from_categories function."""

    def setUp(self):
        """Set up test fixtures."""
        # Mock the category_manager import
        self.original_modules = {}
        if "category_utils" in sys.modules:
            self.original_modules["category_utils"] = sys.modules["category_utils"]

    def tearDown(self):
        """Clean up test fixtures."""
        # Restore original modules
        for module_name, module in self.original_modules.items():
            sys.modules[module_name] = module

    def _mock_category_manager(self, categories):
        """Create a mock category_manager module."""
        from unittest.mock import MagicMock

        mock_manager = MagicMock()
        mock_manager.get_categories_for_readme.return_value = categories

        mock_module = MagicMock()
        mock_module.category_manager = mock_manager

        sys.modules["category_utils"] = mock_module
        return mock_manager

    def test_empty_categories(self):
        """Test TOC generation with no categories."""
        self._mock_category_manager([])

        result = generate_toc_from_categories()

        # Check for main structure
        self.assertIn("<details>", result)
        self.assertIn("<summary>Table of Contents</summary>", result)
        self.assertIn("</details>", result)

    def test_simple_categories(self):
        """Test TOC generation with simple categories (no subcategories)."""
        categories = [
            {"name": "Getting Started", "icon": "🚀"},
            {"name": "Resources", "icon": "📚"},
            {"name": "Tools", "icon": "🔧"},
        ]
        self._mock_category_manager(categories)

        result = generate_toc_from_categories()

        # Check for main structure
        self.assertIn("<summary>Table of Contents</summary>", result)

        # Check for simple links
        self.assertIn("- [Getting Started](#getting-started-)", result)
        self.assertIn("- [Resources](#resources-)", result)
        self.assertIn("- [Tools](#tools-)", result)

    def test_categories_with_subcategories(self):
        """Test TOC generation with categories containing subcategories."""
        categories = [
            {
                "name": "Configuration",
                "icon": "⚙️",
                "subcategories": [
                    {"name": "Basic Setup"},
                    {"name": "Advanced Options"},
                ],
            },
            {"name": "Simple Category"},  # No subcategories
        ]
        self._mock_category_manager(categories)

        result = generate_toc_from_categories()

        # Check for collapsible category with subcategories
        self.assertIn("- <details>", result)
        # The gear emoji has a variation selector, so it gets URL-encoded
        self.assertIn('  <summary><a href="#configuration-%EF%B8%8F">Configuration</a>', result)

        # Check for subcategories
        self.assertIn("  - [Basic Setup](#basic-setup)", result)
        self.assertIn("  - [Advanced Options](#advanced-options)", result)

        # Check for simple category
        self.assertIn("- [Simple Category](#simple-category)", result)

    def test_special_characters_in_names(self):
        """Test TOC generation with special characters in category names."""
        categories = [
            {"name": "Tips & Tricks"},
            {"name": "CI/CD Tools"},
            {"name": "Node.js Resources"},
        ]
        self._mock_category_manager(categories)

        result = generate_toc_from_categories()

        # Check that special characters are properly handled in anchors
        self.assertIn("[Tips & Tricks](#tips--tricks)", result)
        self.assertIn("[CI/CD Tools](#cicd-tools)", result)
        self.assertIn("[Node.js Resources](#nodejs-resources)", result)

    def test_mixed_categories(self):
        """Test TOC with a mix of simple and nested categories."""
        categories = [
            {"name": "Overview"},
            {
                "name": "Documentation",
                "icon": "📖",
                "subcategories": [
                    {"name": "API Reference"},
                    {"name": "Tutorials"},
                ],
            },
            {"name": "Community", "icon": "👥"},
            {
                "name": "Development",
                "subcategories": [{"name": "Contributing"}],
            },
        ]
        self._mock_category_manager(categories)

        result = generate_toc_from_categories()

        # Check structure
        lines = result.split("\n")

        # Should have main details wrapper
        self.assertEqual(lines[0], "<details>")
        self.assertEqual(lines[1], "<summary>Table of Contents</summary>")

        # Check for simple categories
        self.assertIn("- [Overview](#overview)", result)
        self.assertIn("- [Community](#community-)", result)

        # Check for nested categories
        self.assertIn('  <summary><a href="#documentation-">Documentation</a>', result)
        self.assertIn("  - [API Reference](#api-reference)", result)
        self.assertIn("  - [Tutorials](#tutorials)", result)

        # Count details blocks (main + 2 categories with subcategories)
        self.assertEqual(result.count("<details>"), 3)
        self.assertEqual(result.count("</details>"), 3)


class TestLoadAnnouncements(unittest.TestCase):
    """Test cases for the load_announcements function."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir)

    def test_empty_announcements(self):
        """Test loading empty announcements."""
        # Create empty YAML file
        yaml_path = os.path.join(self.temp_dir, "announcements.yaml")
        with open(yaml_path, "w") as f:
            f.write("")

        result = load_announcements(self.temp_dir)
        self.assertEqual(result, "")

    def test_simple_string_announcement(self):
        """Test announcements with simple string items."""
        announcements_data = [
            {
                "date": "2025-09-12",
                "title": "Test Announcements",
                "items": ["First announcement", "Second announcement"],
            }
        ]

        yaml_path = os.path.join(self.temp_dir, "announcements.yaml")
        with open(yaml_path, "w") as f:
            yaml.dump(announcements_data, f)

        result = load_announcements(self.temp_dir)

        # Check for main structure
        self.assertIn("<details>", result)
        self.assertIn("<summary>View Announcements</summary>", result)

        # Check for date group
        self.assertIn("- <details>", result)
        self.assertIn("<summary>2025-09-12 - Test Announcements</summary>", result)

        # Check for items
        self.assertIn("  - First announcement", result)
        self.assertIn("  - Second announcement", result)

    def test_collapsible_announcement_items(self):
        """Test announcements with collapsible summary/text items."""
        announcements_data = [
            {
                "date": "2025-09-12",
                "title": "Feature Updates",
                "items": [
                    {
                        "summary": "New feature added",
                        "text": "This is a detailed description of the new feature.",
                    },
                    {"summary": "Bug fix", "text": "Fixed a critical bug in the system."},
                ],
            }
        ]

        yaml_path = os.path.join(self.temp_dir, "announcements.yaml")
        with open(yaml_path, "w") as f:
            yaml.dump(announcements_data, f)

        result = load_announcements(self.temp_dir)

        # Check for nested collapsible items
        self.assertIn("  - <details>", result)
        self.assertIn("    <summary>New feature added</summary>", result)
        self.assertIn("    - This is a detailed description of the new feature.", result)
        self.assertIn("    <summary>Bug fix</summary>", result)
        self.assertIn("    - Fixed a critical bug in the system.", result)

    def test_multi_line_text_in_announcements(self):
        """Test announcements with multi-line text content."""
        announcements_data = [
            {
                "date": "2025-09-15",
                "title": "Important Notice",
                "items": [
                    {
                        "summary": "Multi-line announcement",
                        "text": "Line 1 of the announcement.\n\nLine 2 with a gap.\n\nLine 3 final.",
                    }
                ],
            }
        ]

        yaml_path = os.path.join(self.temp_dir, "announcements.yaml")
        with open(yaml_path, "w") as f:
            yaml.dump(announcements_data, f)

        result = load_announcements(self.temp_dir)

        # Check that multi-line text is properly formatted
        self.assertIn("    - Line 1 of the announcement.", result)
        self.assertIn("      Line 2 with a gap.", result)
        self.assertIn("      Line 3 final.", result)

    def test_mixed_announcement_types(self):
        """Test announcements with mixed item types."""
        announcements_data = [
            {
                "date": "2025-09-20",
                "items": [  # No title
                    "Simple string item",
                    {"summary": "Collapsible item", "text": "Detailed content here"},
                    {"summary": "Summary only item"},  # No text
                    {"text": "Text only item"},  # No summary
                ],
            }
        ]

        yaml_path = os.path.join(self.temp_dir, "announcements.yaml")
        with open(yaml_path, "w") as f:
            yaml.dump(announcements_data, f)

        result = load_announcements(self.temp_dir)

        # Check for date without title
        self.assertIn("<summary>2025-09-20</summary>", result)

        # Check for various item types
        self.assertIn("  - Simple string item", result)
        self.assertIn("    <summary>Collapsible item</summary>", result)
        self.assertIn("    - Detailed content here", result)
        self.assertIn("  - Summary only item", result)
        self.assertIn("  - Text only item", result)

    def test_multiple_date_groups(self):
        """Test announcements with multiple date groups."""
        announcements_data = [
            {
                "date": "2025-09-10",
                "title": "Week 1",
                "items": ["Announcement 1"],
            },
            {
                "date": "2025-09-17",
                "title": "Week 2",
                "items": ["Announcement 2"],
            },
        ]

        yaml_path = os.path.join(self.temp_dir, "announcements.yaml")
        with open(yaml_path, "w") as f:
            yaml.dump(announcements_data, f)

        result = load_announcements(self.temp_dir)

        # Check for both date groups
        self.assertIn("<summary>2025-09-10 - Week 1</summary>", result)
        self.assertIn("<summary>2025-09-17 - Week 2</summary>", result)

        # Verify proper nesting structure
        self.assertEqual(result.count("- <details>"), 2)  # Two date groups
        self.assertEqual(result.count("</details>"), 3)  # Main + 2 date groups

    def test_markdown_in_announcements(self):
        """Test that markdown formatting is preserved in announcements."""
        announcements_data = [
            {
                "date": "2025-09-12",
                "title": "Markdown Test",
                "items": [
                    {
                        "summary": "Test with markdown",
                        "text": "This has **bold** text and [a link](https://example.com).",
                    }
                ],
            }
        ]

        yaml_path = os.path.join(self.temp_dir, "announcements.yaml")
        with open(yaml_path, "w") as f:
            yaml.dump(announcements_data, f)

        result = load_announcements(self.temp_dir)

        # Check that markdown is preserved
        self.assertIn("**bold**", result)
        self.assertIn("[a link](https://example.com)", result)

    def test_fallback_to_markdown_file(self):
        """Test fallback to announcements.md if YAML doesn't exist."""
        # Create markdown file instead of YAML
        md_path = os.path.join(self.temp_dir, "announcements.md")
        with open(md_path, "w") as f:
            f.write("#### Legacy announcement format\n\nThis is from the old .md file.")

        result = load_announcements(self.temp_dir)

        self.assertIn("Legacy announcement format", result)
        self.assertIn("This is from the old .md file", result)

    def test_nonexistent_directory(self):
        """Test loading from a directory with no announcement files."""
        empty_dir = os.path.join(self.temp_dir, "empty")
        os.makedirs(empty_dir)

        result = load_announcements(empty_dir)
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()

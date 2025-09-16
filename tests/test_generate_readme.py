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
    from generate_readme import load_announcements, parse_resource_date  # type: ignore
except ImportError:
    from scripts.generate_readme import load_announcements, parse_resource_date


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

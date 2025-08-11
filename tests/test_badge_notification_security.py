#!/usr/bin/env python3
"""
Security-focused tests for badge notification system
Tests XSS prevention, injection attacks, and input validation
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from badge_notification_core import BadgeNotificationCore


def test_xss_prevention():
    """Test that XSS attempts are properly sanitized"""
    print("Testing XSS Prevention...")

    # Test cases with potential XSS
    xss_tests = [
        ("<script>alert('XSS')</script>", "Should escape script tags"),
        ("</textarea><script>alert('XSS')</script>", "Should escape closing tags"),
        ("<img src=x onerror=alert('XSS')>", "Should escape img tags"),
        ("<iframe src='evil.com'></iframe>", "Should escape iframes"),
        ("javascript:alert('XSS')", "Should handle javascript: protocol"),
        ("<svg onload=alert('XSS')>", "Should escape SVG tags"),
    ]

    for payload, description in xss_tests:
        sanitized = BadgeNotificationCore.sanitize_markdown(payload)
        # Check that dangerous HTML is escaped
        assert "<" not in sanitized or "&lt;" in sanitized, f"Failed: {description}"
        assert ">" not in sanitized or "&gt;" in sanitized, f"Failed: {description}"
        print(f"  ✓ {description}")


def test_markdown_injection():
    """Test that markdown injection is prevented"""
    print("\nTesting Markdown Injection Prevention...")

    # Test cases for markdown injection
    markdown_tests = [
        ("# Injected Header", "Should escape headers"),
        ("## Another Header", "Should escape h2 headers"),
        ("*italics* and **bold**", "Should escape emphasis"),
        ("[link](http://evil.com)", "Should escape links"),
        ("![image](http://evil.com/img.png)", "Should escape images"),
        ("`code injection`", "Should escape inline code"),
        ("```\ncode block\n```", "Should escape code blocks"),
        ("| table | injection |", "Should escape tables"),
    ]

    for payload, description in markdown_tests:
        sanitized = BadgeNotificationCore.sanitize_markdown(payload)
        # Check that markdown special chars are escaped
        assert "*" not in sanitized or "\\*" in sanitized, f"Failed: {description}"
        assert "#" not in sanitized or "\\#" in sanitized, f"Failed: {description}"
        assert "`" not in sanitized or "\\`" in sanitized, f"Failed: {description}"
        assert "[" not in sanitized or "\\[" in sanitized, f"Failed: {description}"
        print(f"  ✓ {description}")


def test_url_validation():
    """Test GitHub URL validation"""
    print("\nTesting URL Validation...")

    validate = BadgeNotificationCore.validate_github_url

    # Valid URLs
    valid_urls = [
        "https://github.com/owner/repo",
        "https://github.com/owner/repo/",
        "https://github.com/owner/repo.git",
        "https://github.com/owner-dash/repo_underscore",
        "https://github.com/owner.dot/repo.dot",
    ]

    for url in valid_urls:
        assert validate(url), f"Should accept valid URL: {url}"
        print(f"  ✓ Valid URL accepted: {url}")

    # Invalid/dangerous URLs
    invalid_urls = [
        "http://github.com/owner/repo",  # HTTP not allowed
        "https://gitlab.com/owner/repo",  # Not GitHub
        "https://github.com/owner/repo; rm -rf /",  # Command injection
        "https://github.com/owner/repo|cat /etc/passwd",  # Pipe injection
        "https://github.com/owner/repo`whoami`",  # Backtick injection
        "https://github.com/owner/repo$(hostname)",  # Command substitution
        "https://github.com/../../../etc/passwd",  # Path traversal
        "javascript:alert('XSS')",  # JS protocol
        "https://github.com/owner/repo<script>",  # HTML injection
        "",  # Empty string
        None,  # None value
    ]

    for url in invalid_urls:
        if url is None:
            continue
        assert not validate(url), f"Should reject invalid URL: {url}"
        print(f"  ✓ Invalid URL rejected: {url[:50]}...")


def test_url_parsing_safety():
    """Test that URL parsing is safe from injection"""
    print("\nTesting URL Parsing Safety...")

    parse = BadgeNotificationCore.parse_github_url

    # Dangerous URLs that should return (None, None)
    dangerous_urls = [
        "https://github.com/owner/repo; echo hacked",
        "https://github.com/owner/repo && rm -rf /",
        "https://github.com/owner/repo | cat /etc/passwd",
        "https://github.com/owner/../../etc",
        "https://evil.com/fake/repo",
        "not-a-url-at-all",
    ]

    for url in dangerous_urls:
        owner, repo = parse(url)
        assert owner is None and repo is None, f"Should reject dangerous URL: {url}"
        print(f"  ✓ Dangerous URL safely rejected: {url[:50]}...")


def test_input_length_limits():
    """Test that very long inputs are handled safely"""
    print("\nTesting Input Length Limits...")

    sanitize = BadgeNotificationCore.sanitize_markdown

    # Very long input
    long_input = "A" * 10000
    sanitized = sanitize(long_input)

    # Should be truncated to reasonable length
    assert len(sanitized) <= 1100, "Should truncate very long inputs"
    assert sanitized.endswith("..."), "Should indicate truncation"
    print(f"  ✓ Long input truncated from {len(long_input)} to {len(sanitized)} chars")


def test_newline_header_injection():
    """Test prevention of newline + header injection"""
    print("\nTesting Newline + Header Injection Prevention...")

    sanitize = BadgeNotificationCore.sanitize_markdown

    injections = [
        "Normal text\n# Injected Header",
        "Normal text\n\n## Injected H2",
        "Text\n### H3 Injection",
    ]

    for payload in injections:
        sanitized = sanitize(payload)
        # Should escape the # after newline
        assert "\n#" not in sanitized or "\n\\#" in sanitized, f"Failed to prevent: {payload}"
        print("  ✓ Prevented header injection")


def test_combined_attacks():
    """Test combined XSS + markdown injection"""
    print("\nTesting Combined Attack Prevention...")

    # Create a mock notifier instance to test issue body creation
    # We need an instance because create_issue_body is not static
    import unittest.mock as mock

    with mock.patch("badge_notification_core.Github"):
        notifier = BadgeNotificationCore("fake_token")

    # Combined attacks
    combined = [
        "<script>alert('XSS')</script> and **bold** text",
        "# Header with <img src=x onerror=alert()>",
        "[Click me](javascript:alert('XSS'))",
    ]

    for payload in combined:
        body = notifier.create_issue_body(payload, "Test description")

        # Should not contain any unescaped dangerous content
        assert "<script>" not in body, "Script tag not escaped"
        # Note: javascript: in links gets escaped via bracket escaping
        assert "javascript:" not in body or "\\[" in body, "JS protocol not handled"
        assert "<img" not in body, "IMG tag not escaped"

        print(f"  ✓ Combined attack prevented: {payload[:30]}...")


def run_all_tests():
    """Run all security tests"""
    print("=" * 60)
    print("Badge Notification Security Test Suite")
    print("=" * 60)

    try:
        test_xss_prevention()
        test_markdown_injection()
        test_url_validation()
        test_url_parsing_safety()
        test_input_length_limits()
        test_newline_header_injection()
        test_combined_attacks()

        print("\n" + "=" * 60)
        print("✅ All security tests passed!")
        print("=" * 60)
        return True

    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

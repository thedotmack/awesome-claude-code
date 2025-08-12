#!/usr/bin/env python3
"""
Unified category utilities for awesome-claude-code.
Provides a single source of truth for all category-related operations.
"""

import os
from functools import lru_cache

import yaml


@lru_cache(maxsize=1)
def load_categories():
    """Load category definitions from the unified YAML file."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    categories_path = os.path.join(script_dir, "..", "templates", "categories.yaml")

    with open(categories_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return data


def get_all_categories():
    """Get list of all category names."""
    data = load_categories()
    return [cat["name"] for cat in data["categories"]]


def get_category_prefixes():
    """Get mapping of category names to ID prefixes."""
    data = load_categories()
    return {cat["name"]: cat["prefix"] for cat in data["categories"]}


def get_category_by_name(name):
    """Get category configuration by name."""
    data = load_categories()
    for cat in data["categories"]:
        if cat["name"] == name:
            return cat
    return None


def get_category_by_id(cat_id):
    """Get category configuration by ID."""
    data = load_categories()
    for cat in data["categories"]:
        if cat["id"] == cat_id:
            return cat
    return None


def get_all_subcategories():
    """Get all subcategories with their parent category names."""
    data = load_categories()
    subcategories = []

    for cat in data["categories"]:
        if "subcategories" in cat:
            for subcat in cat["subcategories"]:
                subcategories.append(
                    {"parent": cat["name"], "name": subcat["name"], "full_name": f"{cat['name']}: {subcat['name']}"}
                )

    return subcategories


def get_subcategories_for_category(category_name):
    """Get subcategories for a specific category."""
    cat = get_category_by_name(category_name)
    if not cat or "subcategories" not in cat:
        return []

    return [subcat["name"] for subcat in cat["subcategories"]]


def validate_category_subcategory(category, subcategory):
    """Validate that a subcategory belongs to the given category."""
    if not subcategory:
        return True

    cat = get_category_by_name(category)
    if not cat:
        return False

    if "subcategories" not in cat:
        return False

    return any(subcat["name"] == subcategory for subcat in cat["subcategories"])


def get_categories_for_readme():
    """Get categories in order for README generation."""
    data = load_categories()
    categories = sorted(data["categories"], key=lambda x: x.get("order", 999))
    return categories


def get_toc_config():
    """Get table of contents configuration."""
    data = load_categories()
    return data.get("toc", {})

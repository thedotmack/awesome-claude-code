#!/usr/bin/env python3
"""Quick one-liner to generate a resource ID."""

import hashlib
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.category_utils import category_manager

if len(sys.argv) != 4:
    categories = category_manager.get_all_categories()
    print("Usage: python quick_id.py 'Display Name' 'https://link.com' 'Category'")
    print(f"Categories: {', '.join(categories)}")
    sys.exit(1)

display_name, link, category = sys.argv[1:4]
prefixes = category_manager.get_category_prefixes()
prefix = prefixes.get(category, "res")
hash_val = hashlib.sha256(f"{display_name}{link}".encode()).hexdigest()[:8]
print(f"{prefix}-{hash_val}")

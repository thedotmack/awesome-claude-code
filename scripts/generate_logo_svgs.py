#!/usr/bin/env python3
"""
Generate responsive SVG logos for the Awesome Claude Code repository.

This script creates:
- Desktop versions (light/dark) with full ASCII art
- Mobile versions (light/dark) with simplified design
"""

from pathlib import Path

# ASCII art for the desktop version
ASCII_ART = [
    " █████┐ ██┐    ██┐███████┐███████┐ ██████┐ ███┐   ███┐███████┐",
    "██┌──██┐██│    ██│██┌────┘██┌────┘██┌───██┐████┐ ████│██┌────┘",
    "███████│██│ █┐ ██│█████┐  ███████┐██│   ██│██┌████┌██│█████┐",
    "██┌──██│██│███┐██│██┌──┘  └────██│██│   ██│██│└██┌┘██│██┌──┘",
    "██│  ██│└███┌███┌┘███████┐███████│└██████┌┘██│ └─┘ ██│███████┐",
    "└─┘  └─┘ └──┘└──┘ └──────┘└──────┘ └─────┘ └─┘     └─┘└──────┘",
    "",
    "────────────────────────────────────────────────────────────────────────────────────",
    "",
    " ██████┐██┐      █████┐ ██┐   ██┐██████┐ ███████┐     ██████┐ ██████┐ ██████┐ ███████┐",
    "██┌────┘██│     ██┌──██┐██│   ██│██┌──██┐██┌────┘    ██┌────┘██┌───██┐██┌──██┐██┌────┘",
    "██│     ██│     ███████│██│   ██│██│  ██│█████┐      ██│     ██│   ██│██│  ██│█████┐",
    "██│     ██│     ██┌──██│██│   ██│██│  ██│██┌──┘      ██│     ██│   ██│██│  ██│██┌──┘",
    "└██████┐███████┐██│  ██│└██████┌┘██████┌┘███████┐    └██████┐└██████┌┘██████┌┘███████┐",
    " └─────┘└──────┘└─┘  └─┘ └─────┘ └─────┘ └──────┘     └─────┘ └─────┘ └─────┘ └──────┘",
]


def generate_desktop_svg(theme: str = "light") -> str:
    """Generate desktop SVG with full ASCII art."""
    fill_color = "#24292e" if theme == "light" else "#e1e4e8"

    svg_lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" preserveAspectRatio="xMidYMid meet">',
        "  <style>",
        "    text {",
        "      font-family: 'Courier New', Courier, monospace;",
        "      font-size: 14px;",
        f"      fill: {fill_color};",
        "      white-space: pre;",
        "    }",
        "  </style>",
    ]

    # Add each line of ASCII art as a text element
    y_position = 25
    for line in ASCII_ART:
        svg_lines.append(f'  <text x="10" y="{y_position}">{line}</text>')
        y_position += 20

    svg_lines.append("</svg>")
    return "\n".join(svg_lines)


def generate_mobile_svg(theme: str = "light") -> str:
    """Generate mobile SVG with simplified design."""
    if theme == "light":
        text_color = "#24292e"
        accent_color = "#0969da"
    else:
        text_color = "#e1e4e8"
        accent_color = "#58a6ff"

    opacity = "0.4" if theme == "light" else "0.6"
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200" preserveAspectRatio="xMidYMid meet">
  <style>
    .title {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
      font-weight: 900;
      fill: {text_color};
      text-anchor: middle;
    }}
    .line1 {{ font-size: 48px; }}
    .line2 {{ font-size: 44px; }}
    .line3 {{ font-size: 44px; }}
    .accent {{
      fill: none;
      stroke: {accent_color};
      stroke-width: 3;
    }}
  </style>

  <!-- Background decoration -->
  <rect x="20" y="20" width="360" height="160" rx="8" class="accent" opacity="0.1" fill="{accent_color}"/>

  <!-- Text content -->
  <text x="200" y="70" class="title line1">AWESOME</text>
  <text x="200" y="120" class="title line2">CLAUDE</text>
  <text x="200" y="165" class="title line3">CODE</text>

  <!-- Decorative elements -->
  <rect x="50" y="85" width="80" height="3" fill="{accent_color}" opacity="{opacity}"/>
  <rect x="270" y="85" width="80" height="3" fill="{accent_color}" opacity="{opacity}"/>
</svg>"""

    return svg_content


def main():
    """Generate all logo SVG files."""
    # Get the project root directory
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    assets_dir = project_root / "assets"

    # Create assets directory if it doesn't exist
    assets_dir.mkdir(exist_ok=True)

    # Generate desktop SVGs
    desktop_light = generate_desktop_svg("light")
    desktop_dark = generate_desktop_svg("dark")

    # Generate mobile SVGs
    mobile_light = generate_mobile_svg("light")
    mobile_dark = generate_mobile_svg("dark")

    # Write files
    files_to_write = {
        "logo-desktop-light.svg": desktop_light,
        "logo-desktop-dark.svg": desktop_dark,
        "logo-mobile-light.svg": mobile_light,
        "logo-mobile-dark.svg": mobile_dark,
    }

    for filename, content in files_to_write.items():
        filepath = assets_dir / filename
        filepath.write_text(content, encoding="utf-8")
        print(f"✅ Generated: {filepath}")

    print("\n🎨 All logo SVG files have been generated successfully!")
    print("📝 Run 'make generate' to update the README with the new logos.")


if __name__ == "__main__":
    main()

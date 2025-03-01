"""
Django Static Path Converter
-----------------------------
This script scans HTML files in a given directory and replaces hardcoded static file paths 
(e.g., "static/css/style.css") with Django's {% static %} template tag.

Usage:
    1. Place this script in your Django project root.
    2. Run: python convert_static.py
    3. It will update all .html files in the 'templates' directory.

Author: aminattaei
GitHub: https://github.com/aminattaei/
"""

import os
import re

# Directory where your HTML templates are located
TEMPLATES_DIR = "templates"

# Regex pattern to match static file paths (e.g., src="static/js/script.js")
STATIC_PATTERN = re.compile(r'(["\'])static/([^"\']+)(["\'])')

def convert_static_paths(file_path):
    """
    Reads an HTML file, replaces static file paths with Django's {% static %} tag, 
    and overwrites the file with updated content.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Replace static paths with Django's {% static %} tag
    new_content = STATIC_PATTERN.sub(r'\1{% static "\2" %}\3', content)

    # Write changes back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_content)

    print(f"✅ Processed: {file_path}")

def process_templates():
    """
    Loops through all HTML files in the 'templates' directory 
    and applies the static path conversion.
    """
    for root, _, files in os.walk(TEMPLATES_DIR):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                convert_static_paths(file_path)

if __name__ == "__main__":
    print("🔄 Starting static path conversion...")
    process_templates()
    print("🎉 Conversion completed!")

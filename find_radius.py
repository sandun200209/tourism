
import re

css_path = r'c:\xampp\htdocs\tourism\assets\css\style.css'

with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for product card image radius
# We want to find any block starting with .product-card that contains border-radius or clip-path
# This is tricky with regex for nested blocks.
# Let's just find all occurrences of .product-card and print the following 200 chars suitable for quick check.

matches = [m.start() for m in re.finditer(r'\.product-card', content)]

for start in matches:
    # grab context
    end = start + 500
    snippet = content[start:end]
    if "border-radius" in snippet or "clip-path" in snippet:
        print(f"--- Match at {start} ---")
        print(snippet.replace('\n', ' '))
        print("-" * 20)

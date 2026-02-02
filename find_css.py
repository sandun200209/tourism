
import re

css_path = r'c:\xampp\htdocs\tourism\assets\css\style.css'

with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

# simple regex to find .product-card block
matches = re.finditer(r'\.product-card\s*\{[^}]*\}', content)
for m in matches:
    print(f"Match at {m.start()}-{m.end()}:")
    print(m.group(0))

# Search for .product-card .image
matches_img = re.finditer(r'\.product-card\s+\.image\s*\{[^}]*\}', content)
for m in matches_img:
    print(f"Match Image at {m.start()}-{m.end()}:")
    print(m.group(0))
    
# Search for .product-card .image img
matches_img_tag = re.finditer(r'\.product-card\s+\.image\s+img\s*\{[^}]*\}', content)
for m in matches_img_tag:
    print(f"Match Image Tag at {m.start()}-{m.end()}:")
    print(m.group(0))

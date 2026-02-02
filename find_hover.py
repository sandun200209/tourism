
import re

css_path = r'c:\xampp\htdocs\tourism\assets\css\style.css'

with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

matches = [m.start() for m in re.finditer(r'\.hover-on-image', content)]

for start in matches:
    end = start + 300
    snippet = content[start:end]
    print(f"--- Match at {start} ---")
    print(snippet.replace('\n', ' '))
    print("-" * 20)

import json
from pathlib import Path


p = Path('innehåll.json')
text = p.read_text(encoding="Utf8")

data = json.loads(text)

for ele in data:
    if ele['rightalign'] == True:
        print(f"{ele['what']:>25}{ele['value']:12} {ele['unit']}")
    else:
        print(f"{ele['what']:<25}{ele['value']:12} {ele['unit']}")
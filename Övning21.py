import json
from pathlib import Path

p = Path('21_json').read_text(encoding="UTF8")  # Öppnar sökvägen till filen och .read gör läsbar
data = json.loads(p)                            #

total_lista = []                                # Skapar en lista för att hantera värde från item

for item in data['entries']:
    total_lista.append(item['total'])

print(sum(total_lista))








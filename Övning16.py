from pathlib import Path


def case():
    dokument = "system.log"
    important = []
    keep_phares = ["BEAR", "X-RAY"]
    lines = Path(dokument).read_text().splitlines()

    for line in lines:
        line = line.strip()
        for phrase in keep_phares:
            if phrase in line:
                important.append(line)
                break

    print('\n'.join(important))


if __name__ == '__main__':
    case()

# Olof lösning:
'''
from pathlib import Path

def run():
    for line in Path('system.log').read_text().splitlines():
        if 'BEAR' in line or 'X-RAY' in line:
            print(line)
            
if __name__ == '__main__':
    run()

'''
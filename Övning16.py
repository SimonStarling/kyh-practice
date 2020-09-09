from pathlib import Path  #  ger oss möjlighet att hämta/läsa filer


def case():
    dokument = "system.log"             #  Variabel som hanterar filen (system.log)
    important = []                      #  Lista för att hantera linjerna vi vill ha
    keep_phares = ["BEAR", "X-RAY"]     #  Orden som vi vill leta efter i Lines
    lines = Path(dokument).read_text().splitlines()     #  Variabel som hanterar öppning/läsning/stägning av filen system.log

    for line in lines:
        line = line.strip()             # tar bort Whitespace för varje line
        for phrase in keep_phares:      #  kommer stega igenom texten och för varje line som har BEAR eller X-RAY.
            if phrase in line:          #  så kommer listan important öka med varje linje text som matchar IF-statement
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
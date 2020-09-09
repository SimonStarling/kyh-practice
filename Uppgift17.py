from pathlib import Path

def main():
    alt = input(f'1. Lista TODO:\n2. Lägg till uppgift:\n3. Ta bort uddgift:\n4. Avbryt programmet:\nVälj alternativ: ')
    if alt == "4":
        print("Programmet avbryts")


if __name__ == '__main__':
    main()


def alt_1():
    for line in Path('TODO.txt').read_text(encoding="utf8").splitlines():
        print(line)


alt_1()
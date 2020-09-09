from pathlib import Path


def main():
    alt = input(f'1. Lista TODO:\n2. Lägg till uppgift:\n3. Ta bort uddgift:\n4. Avbryt programmet:\nVälj alternativ: ')
    if alt == "1":
        alt_1()
    if alt == "2":
        alt_2()


def alt_1():
    for line in Path('TODO.txt').read_text(encoding="utf8").splitlines(","):
        print(line)


def alt_2():
    todo = "TODO.txt"
    add = Path(todo).write_text(input("Lägg till aktivitet: "))

    print(add)


if __name__ == '__main__':
    main()

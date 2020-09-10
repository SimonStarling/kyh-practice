from pathlib import Path

p = Path("TODO.txt")

todo_list = []
todo_list.append(p.read_text())


def main():
    while True:
        alt = input(
            f'1. Lista TODO:\n2. Lägg till uppgift:\n3. Ta bort uddgift:\n4. Avbryt programmet:\nVälj alternativ: ')
        print("____________________________________")
        if alt == "1":
            alt_1()
        elif alt == "2":
            alt_2()
        elif alt == "3":
            alt_3()
        elif alt == "4":
            pass
        else:
            print("Välj ett alternativ mellan 1-4.")
        print("____________________________________")


def alt_1():
    for line in Path('TODO.txt').read_text(encoding="utf8").splitlines():
        print(line)


def alt_2():
    p.read_text()
    user_input2 = input("Lägg till: ")
    todo_list.append(user_input2)
    p.write_text(f"{todo_list}")


def alt_3():
    print(p.read_text())
    user_input3 = input("Vilken aktivitet vill du ta bort?: ")
    todo_list.remove(user_input3)
    p.write_text(f"{todo_list}")


def alt_4():
    pass


if __name__ == '__main__':
    print("EN GRYM TODO-App")
    print("________________")
    main()

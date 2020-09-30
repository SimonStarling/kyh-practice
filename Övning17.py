from pathlib import Path

p = Path('TODO.txt')
content = p.read_text(encoding="utf8")

def listTodo():
    print(content)


def addTodo():
    print("Placeholder")


def deleteEleTodo():
    print("Placeholder1")


def quitTodo():
    print("Placeholder2")


if __name__ == '__main__':
    print("TODO-list\n1. Visa TODO-lista\n2. Lägg till aktivitet\n3. Ta bort aktivitet\n4. Avsluta")
    user_input = input(">>>")
    while True:
        if user_input == "1":
            listTodo()
            
        if user_input == "2":
            addTodo()
            
        if user_input == "3":
            deleteEleTodo()
            
        if user_input == "4":
            quitTodo()
        break
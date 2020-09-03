import random


def game(number_of_questions, max_value):
    correct_answers = 0

    for i in range(number_of_questions):
        a = random.randint(1, max_value)
        b = random.randint(1, max_value)
        answer = input(f"{a} + {b}")
        try:
            number = int(answer)
        except ValueError:
            print("Du angav inte en siffra! Ditt svar blir 0")
            number = 0
        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a + b}")
            print("---")
        print(f"Du fick {correct_answers} av {number_of_questions} rätt.")


if __name__ == '__main__':
    try:
        number = int(input("Hur många frågor?"))
    except ValueError:
        print("Du skrev inte in ett tal. Antal frågor = 3")
        number = 3
    try:
        max_value = int(input("Största tal?"))
    except ValueError:
        print("Du angav inte ett heltal. Högsta tal är satt till 10")
        max_value = 10
    game(number, max_value)

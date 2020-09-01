# Program för att gissa ett slumpat nummer mellan 1 - 100.

import random

n = random.randint(1, 100)  # Kommer ge n ett värde slumpat mellan 1 till 100
print("Jag tänker på ett värde mellan 1 till 100. Kan du gissa vilket?")
guess_number = 0


def mainloop(guess_number):

    while True:
        text = input("Ditt svar: ")
        as_number = int(text)

        if as_number == n:
            print("Korrekt! Ditt antal gissningar var " + str(guess_number))
            guess_number += 1
            break

        if as_number < n:
            print("Fel, värdet är högre... Försök igen!")
            guess_number += 1
            print("Antal gissningar: " + str(guess_number))
        if as_number > n:
            print("Fel, värdet är mindre.. Försök igen!")
            guess_number += 1
            print("Antal gissningar: " + str(guess_number))

mainloop(guess_number)
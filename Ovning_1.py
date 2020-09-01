# Program för att gissa ett slumpat nummer mellan 1 - 100.

import random

n = random.randint(1, 100)  # Kommer ge n ett värde slumpat mellan 1 till 100
print("Jag tänker på ett värde mellan 1 till 100. Kan du gissa vilket?")
guess_number = 0


def ask_number():
    text = input("Ditt svar: ")
    tal = int(text)
    return tal


def mainloop(guess_number):
    while True:
        tal = ask_number()  # Kallar på funktioner ask_number
        if tal == n:

            guess_number += 1
            return guess_number
            break

        if tal < n:
            print("Fel, värdet är högre... Försök igen!")
            guess_number += 1

            print("Antal gissningar: " + str(guess_number))
        if tal > n:
            print("Fel, värdet är mindre.. Försök igen!")
            guess_number += 1

            print("Antal gissningar: " + str(guess_number))


guess_number = mainloop(guess_number)
print("Korrekt! Ditt antal gissningar var " + str(guess_number))

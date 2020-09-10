people = {"Fredrik": "0702778511", "Olof": "123456789", "Lisa": "99999999999", "Bodil": "555-666-897"}


def call():
    while True:
        vem = input("Vem vill du ringa?:")
        if vem not in people:
            print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
        else:
            number = people[vem]
            print(f"Numret till {vem} är {number}")


if __name__ == '__main__':
    print(len(people))
    call()

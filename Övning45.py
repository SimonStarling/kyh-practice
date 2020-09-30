# Kopia av kod från Övning 18

people = {"Fredrik": "0702778511",
          "Olof": "123456789",
          "Lisa": "99999999999",
          "Bodil": "555-666-897"
          }



def call():     # Funktionen call, inga parametrar.
    while True: # While loop som låter programmet snurra.
        val = input("1: Slå upp ett nummer:\n2: Redigera/Lägg till:\n Skriv: ")

        if val == "1":
            vem = input("Vem vill du ringa?: ")

            if vem not in people:
                print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
            else:
                number = people[vem]
                print(f"Numret till {vem} är {number}")
        if val == "2":
            name = input("Lägg till namn: ")
            number = input("Lägg till nummer: ")
            people[name] = number

if __name__ == '__main__':
    print(f"Det finns {len(people)} personer i denna listan")
    call()
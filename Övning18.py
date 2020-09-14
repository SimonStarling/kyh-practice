people = {"Fredrik": "0702778511",
          "Olof": "123456789",
          "Lisa": "99999999999",
          "Bodil": "555-666-897"
          } # Dictonary som håller key och value (name och number)


def call():     # Funktionen call, inga parametrar.
    while True: # While loop som låter programmet snurra.
        val = input("1: Slå upp ett nummer:\n2: Redigera/Lägg till:\n Skriv: ") # Printar de två valen som finns.

        if val == "1":      # Om användaren skriver 1 så kommer de behöva skriva in  Vem dem vill ringa.
            vem = input("Vem vill du ringa?: ") # ange namnet på personen vi vill ringa. Det blir värdet i vem.

            if vem not in people:   # Om värdet i variabel vem från inte finns med i people. Följande printas:
                print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
            else:                   # Om värdet i vem finns i people. kommer koppla namnet (key) till dess nummer (value)
                number = people[vem]
                print(f"Numret till {vem} är {number}") # prinar namn och tillhörande nummer.
        if val == "2":                      # Kommer att köra koden för att kunna lägga till/redigera.
            name = input("Lägg till namn: ")
            number = input("Lägg till nummer: ")
            people[name] = number

if __name__ == '__main__':
    print(f"Det finns {len(people)} personer i denna listan")
    call()

# Kopia av upg18 kod + moddifera med mer json
import json
from pathlib import Path

p = Path('phonenumbers.json')
content = p.read_text(encoding="utf8")
data = json.loads(content)


def main():
    while True:
        people = data
        print(f"Det finns {len(people)} nummer i telefonkatalogen.")

        svar = input("[S]lå upp eller [L]ägg till? ")
        svar = svar[0].upper()
        if svar == 'S':
            vem = input("Vem vill du ringa?")

            if vem not in people:
                # key fanns inte i dict
                print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
            else:
                # key fanns i dict; ta reda på value m.h.a indexering som göra med raka klamrar
                # (precis som med listor fast nycklar måste inte vara heltal!)
                number = people[vem]
                print(f"Numret till {vem} är {number}")

        elif svar == 'L':
            namn = input("Ange personens förnamn: ")
            tfn = input("Ange telefonnummer: ")
            people[namn] = tfn
            content = json.dumps(people, indent=2)
            p.write_text(content, encoding="utf8")

        else:
            print("Förstår inte, avbryter programmet.")
            # Avbryter while True och då tar main slut, d.v.s programmet avslutas
            # eftersom det inte står något mer i Pythonfilen på rad 69!
            break


if __name__ == '__main__':
    main()

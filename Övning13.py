"""
En app som kan laddas ned till mobiltelefonen ska varna finländare som kommit nära någon som smittats med coronaviruset.
– Jag tycker att ni i Sverige borde överväga att göra något liknande, säger Markku Tervahauta, generaldirektör för
Finska institutet för hälsa och välfärd, THL.
"""
import random # Importerar randomfunktionen till programmet.


def game():
    kanslor = ["lycka", "glädje", "ilska", "oro", "kärlek", "lust"]  # 1 Variabeln som innehåller elementen i listan
    kanslor_val = random.choice(kanslor)  # 2 variabel som gör så att ett slumpäsigt ord väljs från listan

    land = ["Sverige", "Island", "Tyskland", "USA"]  # se 1
    land_val = random.choice(land)  # se 2

    pryl = ["bilen", "kylskåpet", "tvättmaskinen", "huset", "grannens hund"] # se 1
    pryl_val = random.choice(pryl)  # se 2

    nationalitet = ["skojare", "pessemister", "skummisar", "kriminella", "rika"] # se 1
    nationalitet_val = random.choice(nationalitet)  # se 2

    namn = ["Göran Persson", "Zlatan", "Kurt Wallander", "Martin Beck", "Greta Thunberg"] # se 1
    namn_val = random.choice(namn)  # se 2

    jobb = ["vaktmästare", "polischef", "dungeonmaster", "ordförande", "badvakt"] # Har randintfuntkionen för slumpat val.
    # jobb_val = random.choice(jobb)  # se 2

    plats = ["skolmatsalen", "stranden", "lägenheten", "DND-gruppen", "guildet"]
    plats_val = random.choice(plats)  # se 2

    print(  # Kommer printa textetn och slumpäsigt välja ord från listorna i varje "f"sträng som kallar på en variabel.
        f"En app som kan laddas ned till {pryl_val} ska varna {nationalitet_val} som kommit nära någon som smittats med {kanslor_val}.")
    print(
        f"Jag tycker att ni i {land_val} borde överväga att göra något liknande, säger {namn_val}, {jobb[random.randint(0, 3)]} för")
    print(f"{plats_val}")


if __name__ == '__main__':
    game()

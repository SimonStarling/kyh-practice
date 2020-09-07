"""
En app som kan laddas ned till mobiltelefonen ska varna finländare som kommit nära någon som smittats med coronaviruset.
– Jag tycker att ni i Sverige borde överväga att göra något liknande, säger Markku Tervahauta, generaldirektör för
Finska institutet för hälsa och välfärd, THL.
"""
import random


def game():
    kanslor = ["lycka", "glädje", "ilska", "oro", "kärlek", "lust"]
    kanslor_val = random.choice(kanslor)

    land =["Sverige", "Island", "Tyskland", "USA"]
    land_val = random.choice(land)

    pryl = ["bilen", "kylskåpet", "tvättmaskinen", "huset", "grannens hund"]
    pryl_val = random.choice(pryl)

    nationalitet = ["skojare", "pessemister", "skummisar", "kriminella", "rika"]
    nationalitet_val = random.choice(nationalitet)

    namn =["Göran Persson", "Zlatan", "Kurt Wallander", "Martin Beck", "Greta Thunberg"]
    namn_val = random.choice(namn)

    jobb = ["vaktmästare", "polischef", "dungeonmaster", "ordförande", "badvakt"]
    jobb_val = random.choice(jobb)

    plats = ["skolmatsalen", "stranden", "lägenheten", "DND-gruppen", "guildet"]
    plats_val =random.choice(plats)
    print(
        f"En app som kan laddas ned till {pryl_val} ska varna {nationalitet_val} som kommit nära någon som smittats med {kanslor_val}.")
    print(
        f"Jag tycker att ni i {land_val} borde överväga att göra något liknande, säger {namn_val}, {jobb_val} för")
    print(f"{plats_val}")


if __name__ == '__main__':
    game()

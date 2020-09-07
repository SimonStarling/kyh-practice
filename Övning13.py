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

    print(
        f"En app som kan laddas ned till mobiltelefonen ska varna finländare som kommit nära någon som smittats med {kanslor_val}.")
    print(
        f"Jag tycker att ni i {land_val} borde överväga att göra något liknande, säger Markku Tervahauta, generaldirektör för")
    print(f"Finska institutet för hälsa och välfärd, THL")


if __name__ == '__main__':
    game()

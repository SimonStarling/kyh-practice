import webbrowser
from pathlib import Path

# POCO! Klar med 33 + 34.1-2

OUTPUT_PATH = Path("djur.html")
TEMPLATE_PATH = Path('djur_template.html')

# Definerar ny klass med namn Djur
class Djur:

    def __init__(self, name, carnivore, wiki_url): # init "konstruerar" en "instans" av klassen Djur.
        self.name = name
        self.carnivore = carnivore
        self.wiki_url = wiki_url

    def carnivore_or_vegetarian(self): # Funktion som kontrollerar om carnivore är True eller false.
                                        # Kommer att returnera det värde som matchar if-else
        # return "Köttätare" if self.carnivore else "Vegegarian" # Alternativ sätt att skriva return för denna.
        if self.carnivore:
            return "Köttätare"
        else:
            return "Vegegarian"

    def html_2(self, htmll):
        htmll += f'<tr><td><a href="{d.wiki_url}">{d.name}</td><td>{cell_2}</td></tr>\n'
        return htmll


if __name__ == '__main__':
    djur = []   # Lista för att hålla element
    # Skapar två instanser av "Djur" instans = objekt

    # Kallar på init i klass Djur och ger värde till dess parametrar( name, carnivore, wiki_url)
    zebra = Djur('Zebra', False, 'https://sv.wikipedia.org/wiki/Zebror')
    tiger = Djur('Tiger', True, 'https://sv.wikipedia.org/wiki/Tiger')
    elefant = Djur('Elefant', False, 'https://sv.wikipedia.org/wiki/Elefanter')
    varg = Djur('Varg', True, 'https://sv.wikipedia.org/wiki/Varg')
    kattbjorn = Djur('Kattbjörn', False, "https://sv.wikipedia.org/wiki/Kattbj%C3%B6rn")

    # Utökar listan djur[] med de objekt som har skapats i klassen Djur. Notera är att detta enbart lägger in dem som
    # Objekt, för att nå specifika attributt så behöver vi skriva "zebra.name" för att kunna se objektet zebras namn.
    djur.append(zebra)
    djur.append(tiger)
    djur.append(elefant)
    djur.append(varg)
    djur.append(kattbjorn)

    html = '<html><table>'

    for d in djur: # For loop som kallar på funktionen car/veg som finns i klass Djur
        cell_2 = d.carnivore_or_vegetarian()    # Kommer ta emot värdet från funktionen och ger return värdet till var.
        html = d.html_2(html)
    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')

    webbrowser.open(str(OUTPUT_PATH))

import webbrowser
from pathlib import Path

# POCO! Klar med 33 + 34.1-2

OUTPUT_PATH = Path("djur.html")
TEMPLATE_PATH = Path('djur_template.html')


class Djur:
    def __init__(self, name, carnivore, wiki_url):
        self.name = name
        self.carnivore = carnivore
        self.wiki_url = wiki_url

    def carnivore_or_vegetarian(self):
        if self.carnivore:
            return "Köttätare"
        else:
            return "Vetegarian"
    def html_2(self, html):
        html += f'<tr><td><a href="{d.wiki_url}">{d.name}</td><td>{cell_2}</td></tr>\n'
        return html
if __name__ == '__main__':
    djur = []
    zebra = Djur('Zebra', False, 'https://sv.wikipedia.org/wiki/Zebror')  # Kallar på init i klassen
    tiger = Djur('Tiger', True, 'https://sv.wikipedia.org/wiki/Tiger')
    elefant = Djur('Elefant', False, 'https://sv.wikipedia.org/wiki/Elefanter')
    varg = Djur('Varg', True, 'https://sv.wikipedia.org/wiki/Varg')
    kattbjörn = Djur('Kattbjörn', False, "https://sv.wikipedia.org/wiki/Kattbj%C3%B6rn")
    djur.append(zebra)
    djur.append(tiger)
    djur.append(elefant)
    djur.append(varg)
    djur.append(kattbjörn)

    html = '<html><table>'

    for d in djur:
        cell_2 = d.carnivore_or_vegetarian()
        html = d.html_2(html)
    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))

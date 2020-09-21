import webbrowser
import requests
from pathlib import Path


def get_advice():  # Funktionen som hämtar qoutes från webben.
    r = requests.get('https://api.adviceslip.com/advice')  # Get-metoden för hämta data från URL
    data = r.json()  # Läser in datan från URL som dic
    return data['slip']['advice']  # Returnerar datan med värder från keys, slip och advice


def write_goat_q():
    advice = get_advice()  # Variabel som har värdet/datan från funktionen get_advice
    template_html = Path('html_test.html').read_text()  # Koppling till till HTML fil.
    quote_replace = template_html.replace('QUOTE_TEXT', advice)  #
    new_html = Path('goat_q.html')
    new_html.write_text(quote_replace, encoding='utf8')


if __name__ == '__main__':
    write_goat_q()
    webbrowser.open('goat_q.html')

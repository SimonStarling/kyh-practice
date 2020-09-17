import requests
import json
from pprint import pprint

r = requests.get('http://www.omdbapi.com/', params={"t": "Alien", "apikey": "9f6d550c"})
text = r.text
data = json.loads(text)

def main():
    pprint(data)



if __name__ == '__main__':
    main()
    # titel = input("Skriv en titel: ")
    # main(titel_input=titel)

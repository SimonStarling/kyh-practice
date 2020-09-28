# Vi ska använda denna URL för att göra vårt GET-anrop för att hämta frågor för vårt Quiz!

import requests

ENDPOINT = 'https://mqif4s7obg.execute-api.eu-central-1.amazonaws.com/olofs_lambda'


class QuizzWebServiceAPI(object):

    def __init__(self):
        self.url = ENDPOINT

    def get_all_questions(self):
        r = requests.get(self.url)
        ls = r.json()['questions']
        return ls

    def add_question(self, prompt, answer, alternatives):
        data = {
            'prompt': prompt,
            'rightAnswer': answer,
            'wrongAnswers': alternatives
        }
        # Uppgift 35.2: fyll i ???
        r = requests.post(url=self.url, json= data)
        return True if r.status_code == 200 else False

if __name__ == '__main__':
   ''' frågor = QuizzWebServiceAPI()
    list = frågor.get_all_questions()
    lista = []
    for question in list:
        lista.append(question['prompt'])

while True:
   # print(f"Det finns {len(lista)} frågor i Quizz-db")
    print("1: Skapa en fråga.")
    print("2: Avsluta.")
    do = input(">>")

    if do == '1':
        prompt = input("Skriv din fråga:")
        answer = input("Skriv rätt svar:")
        altern = input("Skriv felaktigt alternativ, skilj vid komma.").split(',')

        frågor.add_question(prompt,answer,altern)

    else:
        print("----")
        print("Avslutar!")
        break
   '''
import Övning35

if __name__ == '__main__':

    api = Övning35.QuizzWebServiceAPI()
    print(f"Antal Frågor {len(api.get_all_questions())}")
    # print(f"Det finns {len(lista)} frågor i Quizz-db")
    print("1: Skapa en fråga.")
    print("2: Avsluta.")
    do = input(">>")
    while True:
        if do == '1':
            prompt = input("Skriv din fråga:")
            answer = input("Skriv rätt svar:")
            altern = input("Skriv felaktigt alternativ, skilj vid komma.").split(',')

            api.add_question(prompt, answer, altern)

        else:
            print("----")
            print("Avslutar!")
            break
# 1 Bygg ett program som låter användaren mata in ett reg.nr och skriv ut de två grupperna
# var för sig; använd slicing-syntax för att dela upp inputsträngen. Klar!

def reg():
    answer = input("Ange Regnummer: ")

    bokstäver = answer[0:3]
    siffror = answer[3:]

    print(f"Bokstävsgrupp: {bokstäver}\nSiffergrupp: {siffror}")

# 2
def heltal():
    nummerlist = input("Ange tal med , imellan: ")
    str_of_num = nummerlist.split(",")
    numbers = []
    for elem in str_of_num:
        numbers.append(int(elem))
    print(f"Första talet i listan:{nummerlist[0]}\n Sista talet i listan:{nummerlist[-1]}\nSumma av talen i listan: {sum(numbers)}")
    print(f"Listan baklänges:{nummerlist[::-1]}")





    # print(answer[0])
    #print(answer[-1])
if __name__ == '__main__':
    #reg()
    heltal()
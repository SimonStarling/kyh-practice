def main():

    #Uppgift 1 1-10
    print("uppgift 1")
    for i in range(1,11):
        print(i)

    # Uppgift 2 - 1-50 Ojämna
    print("Uppgift 2")
    for i in range(1, 50, 2):
        print(i)

    # Uppgift 3 - 1-10 i omvänd ordning
    print("Uppgift 3")
    for i in reversed(range(1, 11)):
        print(i)

    # Uppgift 4 - Addera summan av nästa tal
    print("Uppgift 4")
    sum = 0
    for i in range(7, 1000):
        sum += i
        print(sum)

    # Uppgift 5 - Produkten av talen 1 t.o.m 1000
    print("Uppgift 5")
    sum = 1
    for i in range(7, 1000):
        sum *= i
        print(sum)


if __name__ == '__main__':
    main()

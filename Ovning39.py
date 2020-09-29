# Repetion av Funktioner!

# 39.1
def count(a, b, c):  # a, b och c är våra parametrar som kommer hållde det värde som skickas in utifrån funktionen.

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > b and c > a:
        return c
    # Returnerar f och när vi sedan kallar på count, då kommer det som ske här vissas.
num1 = 1
num2 = 2
num3 = 3

print(count(num1, num2, num3))


# 39.2
def summa(t_list): # a = 5, b = 8 c = 10
    total = 0
    for i in t_list:
        total += i
    return total

print(summa([5,8,10,3,4,68,2,0]))
print(summa([22,2,9]))

# 39.3
def multi(myList):
    result = 1
    for i in myList:
        result = result * i
    return result

send_list = [5,3,7]
send_list1 = [10, 4, 2]
send_list2 = [120, 9, 0]
print(multi(send_list))
print(multi(send_list1))
print(multi(send_list2))





# Repetion av Funktioner!
# 39.1
'''
def count(a, b, c):  # a, b och c är våra parametrar som kommer hållde det värde som skickas in utifrån funktionen.

    if a > (b and c):
        return a
    elif b > (a and c):
        return b
    elif c > (b and a):
        return c
    # Returnerar f och när vi sedan kallar på count, då kommer det som ske här vissas.
num1 = input(">>>")
num2 = input(">>>")
num3 = input(">>>")

print(count(num1, num2, num3))
'''

# 39.2

def summa(a,b,c): # a = 5, b = 8 c = 10
    t_list = [a, b, c]
    total = 0
    for i in t_list:
        total += i
    return total

print(summa(5,8,10))
print(summa(22,2,9))
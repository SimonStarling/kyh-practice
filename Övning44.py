# 44.1 Namn och Ålder som string och int i en tuple.
'''
a = input("Namn: ")
b = int(input("Ålder:"))
t = (a, b)
print(type(a))
print(type(b))
print(t)
'''


# 44.2
'''
def switchT(t):
    (a, b) = t
    (a, b) = (b, a)
    t = (a, b)
    return t

t = (5, 6)
print(switchT(t))
'''
# 44.3
'''
def l_to_t(l):
    return tuple(l)
print(l_to_t([1, 2, 3]))
'''
# alt 44.3
'''
def convert(l):
    a = l[0]
    b = l[1]
    c = l[2]
    t = (a, b, c)
    return t
print(convert([1, 2, 3]))
'''

'''
# 40.1
def rev_text(text):

    res = ''
    for char in text:
        res = char + res
    return res
    y = []
    for i in text:
        y.append(i)
    # print(f"{y[4]}{y[3]}{y[2]}{y[1]}{y[0]}")


print(rev_text("ABCDEF"))
'''

# 40.2

def big_L(text):
    pass

# 41 - Tankeövning.
def fn(a):
    print(a)
    a = 2
    print(a)
    return  a

a = 1
print(a) # Kommer printa 1
fn(1)   # Kommer printa 1 sedan 2
b = a + fn(1) # Kör igenom fn igen och returnerar värdet från a. B får sedan värdet av a + return av fn(). Som blir 3.
print(b)
print(a)    # Kommer printa 1
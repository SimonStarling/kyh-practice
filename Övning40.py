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

print("40.1")
print(rev_text("12345"))
print("\n")

# 40.2

def big_L(text):
    upper = 0
    for c in range(len(text)):
        if text[c].isupper():
            upper += 1

    return upper

str = "AbCDefG"
print(big_L(str))

'''
def middle(value, min, max):
    if min < value > max:
  '''
'''
# 41 - Tankeövning.
def fn(a):
    print(a)
    a = 2
    print(a)
    return a

a = 1
print(a)  # Kommer printa 1
fn(1)  # Kommer printa 1 sedan 2
b = a + fn(1)  # Kör igenom fn igen och returnerar värdet från a. B får sedan värdet av a + return av fn(). Som blir 3.
print(b)
print(a)  # Kommer printa 1
'''
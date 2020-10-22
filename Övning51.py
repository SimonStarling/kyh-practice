# 51.1 Skriv om funktionen add_as_def som lambda, och lagra i en variabel
'''
add_as_lambda = lambda a,b:a+b
print(add_as_lambda(2,4))
'''

# 51.2 Skriv om obj som en funktion "upper"
'''
# Med lambda
obj = lambda s: s.upper()
print(obj("sträng"))

#Som funktion
def obj(s):
    s = s.upper()
    return s

x = "hej detta ska vara i upper"
z = obj(x)
print(z)
'''

# 51.3 Översätt denna lambda till en vanlig def funktion
'''
# Som lambda:
join_as_lambda = lambda strings, inbetween: inbetween.join(strings)
print(join_as_lambda("Hej", "Hej"))

print("Hej".join(["H", "e", "j"]))


def join_as_lambda(strings):

    ls = ["H", "e", "j"]
    print(strings.join(ls))

join_as_lambda("Hej")
'''
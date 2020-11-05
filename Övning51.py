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


#51.4 Vad kommer följande program att skriva ut? Läs och diskutera först.
# Testkör därefter, och förklara varför ni får det resultat ni får...
'''
anna = ("Anna", "Persson", 42)
lova = ("Lova", "Andersson", 35)
alex = ("Alex", "Börjesson", 10)
people = [anna, lova, alex]
on_surname = sorted(people, key=lambda p: p[1]) # värdet i p styr sorteringen av listan.
# 0 är förnamn, 1 efternamn och 2 är ålder
for (first, last, age) in on_surname:
    print(f"{first} {last} ({age} år)")
    '''

# 51.5 Skriv ett program som utgår ifrån ovanstående, men skriver ut personerna i åldersordning.
'''
anna = ("Anna", "Persson", 42)
lova = ("Lova", "Andersson", 35)
alex = ("Alex", "Börjesson", 10)
people = [anna, lova, alex]
on_surname = sorted(people, key=lambda p: p[2]) # värdet i p styr sorteringen av listan.
# 0 är förnamn, 1 efternamn och 2 är ålder
for (first, last, age) in on_surname:
    print(f"{first} {last} ({age} år)")
'''

# 51.6 Utgående ifrån förra programmet, ändra så att en "def age_sorter" funktion används istället med hjälp syntaxen key=age_sorter
# Vilket sätt tycker ni är tydligast?
'''
anna = ("Anna", "Persson", 42)
lova = ("Lova", "Andersson", 35)
alex = ("Alex", "Börjesson", 10)
people = [anna, lova, alex]

def age_sorter():
    ett =people[0][2]
    tva =people[1][2]
    tre =people[2][2]
    ls = [ett, tva, tre]
    print(sorted(ls))

age_sorter()
'''
# 51.7 Skriv om föregående program som använder sig av en class Person med attributen first, last och age
# istället för tuppler. Vilken form tycker är lättast att läsa enligt er?

class People:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def order_by():
        people = []
        people.append(People("Anna", "Persson", 42))
        people.append(People("Lova", "Andersson", 35))
        people.append(People("Alex", "Börjesson", 10))

        print(people)

    order_by()
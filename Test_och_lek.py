# Will print the welcome-text and my name
my_name = "Simon"
print("Hello and welcome " + my_name + "!\n")

#Printar frasen men kommer ändra Zinzino till Friday

phrase = "Zinzino is the best\n"
print(phrase.replace ("Zinzino", "Friday")) #Ersätter Zinzino med Friday

#Numbers
print("En test med siffror  och matte\n")
print(10)
print(5.7)
print(-420)
print(4+4)
print(5*3)

#Tillåter mig att printa nummer(int) i en string
my_num = 92
print(str(my_num) + " is my favorit\n")

#Functions
from math import * #Hämtar fler mattefuntktioner
#(math-modul) Lter mig göra mer mattefunktioner i koden.

my_num = -5
print(max(2, 3)) #ger mig högsta nummret av de två
print(pow(2, 3)) #ger  mig värdet av 2*2*2 (2 upphöjt med 2)
print(min(2, 3)) #ger mig lägsta siffran
print(round(6.6)) #avrundar till närmaste heltal
print("\n")

#Input/output
#name och age är mina variabler för att spara användarens input
#Kommer be användaren skriva sitt namn och ge dem möjlighet att skriva(ge input till programet)
#och returnera det användaren skrev + texten. Samma sak för ålder.
print("Denna biten hanterar input/output\n")
name = input("Enter your name: ")
age = input("Enter your age: ")
print ("Hello " + name +"! You are " + age + " years old!\n")

#Bygga en "miniräknare"
#num1 och num2 är mina variabler. Result kommer printa mina två variabler.
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + float(num2) #Utan int() så kommer Result bara printa num1 och num2 som strings
#och inte utföra någon form av beräkningar. Observera att int kan bara hantera heltal, ej decimal.
#för att hantera tal med decimal, använd datatyp float().
print(result)
print("\n")

#"Mad Libs Game", ber användaren skriva in "color, plural och celebrity.
#Returnerar i Print - Text + input från användaren(det som sparats i variabeln)
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are "+ color)
print(plural_noun +" are blue")
print ("I love "+ celebrity +"\n")

#Listor, hantera stora mängder data och organisera dessa. Listor i Python kan hantera olika datatyper i samma lista
#Exempel du kan blanda "Namn", 2, False. Använd variabelnamn med [] för att välja specifik indexplats.
family = ["Lena", "Urban", "Johan", "Elin", "Mormor", "Farfar"] #variabl och inehåll för listan
print(family) #printar hela listan
print (family[1]) #printar endast inedx nr 1 i listan
print(family[-1]) #printar den sista platsen i listan (böjar bakifrån)
print (family[2:]) #printar endast från plats 2 och fram (index 2 och framåt)
print(family[2:4:]) #tar endast de platser i inom vald index (i detta fall plats 2 och 3 men inte 4!)
print("\n")

#List-functions - Några funktioner för listor
cars = ["Volvo", "BMW", "KIA", "Renualt", "Ford", "Nissan"]
reg_number =[333, 444, 555, 666, 777, 888, 999, 111]

#cars.extend(reg_number) #Kombinera listor, i detta fall cars+reg_number
cars.append("Volkswagen") #Lägger till ett element i slutet av listan cars.
cars.insert(1,"Honda") #Kommer lägga till element "Honda" på indexplats 1 (resten av listan hoppar ett steg ned)
#cars.remove("Volvo") #kommer ta bort Element Volvo från listan
#cars.clear() #Kommer tömma listan på alla element
#cars.pop() #Tar bort det sista elementet i listan.
#cars.sort() #Sorterar listan i alfabetisk ordning(defult)

reg_number.reverse() #Kommer vända på ordningen i listan för nummer

print(cars) #kommer printa cars
print(reg_number) #Printar lstan reg_numbers
#print(cars.count("KIA")) #Kommer räkna och returnera hur många gånger "KIA" finns i listan
print("\n")

#Functions
# Ger oss möjlighet att kalla på en funktion som vi har skapat. Funktionen innehåller egenskaper som vi har tilldelat dem.
#Men kan ge funktioner ytterligare information genom Parametrar

#Funktion) (#Parameter)
def say_hi(name, age): #Funktionens namn och dessa Parametrar som styr vad den kommer utföra
    print("Hello " + name + ", you are " + age + " years old.")

say_hi("Simon", "28") #Information som kommer printas ut i funktionen say_hi med parametrarna name och age.
say_hi("Elin", "24")
print("\n")

#Return statments
#Använd Return för att få informationen från en Funktion. Obs, efter ett return-statment så avbryter den Funktioen, ingen kod efter Return kommer utföras.

def cube(num): #vår funktion och dess parametrar
    return num*num*num #kommer att använda värdet från variabel result för att ge (parameter) num värde 5 (som sedan blir 5*5*5)


result = cube(5) #Variable Result kommer skicka information till Function cub och ge värde till parameter num (=5)
print(result) #kommer printa informationen från variabel result, som hämtat information från cube
print("\n")

#IF-statment
# IF-statments hanterar saker som vi har satt ett Condition till, ex Om jag är hungrig (IF hungery) då äter jag mat (then eat food)
# Om vilkoret som är satt för ett IF så kommer koden som är kopplad till detta (true) utföras, om inte (false) så sker ingenting eller det som är kopplat till
# False-statment.

is_male = True #Sätter variable is_male till True
is_tall = True
if is_male or is_tall: #kontrollerar om is_male upplfyller kravet för True och printar texten som är kopplat till detta.
    print("You ara a male or tall or both")
else: #utför koden nedan om variabeln is_male inte var true och inte uppfyller kravet för ett true-statment - kommer printa texten nedan.
    print("You are netiher male nor tall")





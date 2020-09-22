'''
sträng = input("Skriv text: ")
ny_sträng = sträng.join('')
combo_sträng = ny_sträng[::-1]

print(len(sträng.replace(" ","")))

if combo_sträng.lower() == ny_sträng.lower():
    print(f"{sträng} är ett Palindrome")
else:
    print(f"{sträng} är inte ett palindrom")
'''

#Olof Kod:
text = input("Skriv text: ")
lowercase = ''.join([c for c in text.lower() if c != ' '])
lowercase_rev = lowercase[::-1]

print(len(text.replace(" ","")))

if lowercase == lowercase_rev:
    print(f"{text} är ett Palindrom!")
else:
    print(f"{text} är Ej palindrom!")
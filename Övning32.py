sträng = input("Skriv text: ")
ny_sträng = sträng.join('')
combo_sträng = ny_sträng[::-1]

print(len(sträng.replace(" ","")))

if combo_sträng.lower() == ny_sträng.lower():
    print(f"{sträng} är ett Palindrome")
else:
    print(f"{sträng} är inte ett palindrom")

'''
Olof Kod: 
    lowercase = sträng.lower()
    lowercase_rev = lowercase[::-1]
        if lowercase == lowercase_rev:
             print("Palindrom!)
        else:
            print(Ej palindrom!)    
'''
# 1 1. Bygg ett program som låter användaren mata in ett reg.nr och skriv ut de två grupperna
# var för sig; använd slicing-syntax för att dela upp inputsträngen. Klar!
answer = input("Ange Regnummer: ")

bokstäver = answer[0:3]
siffror = answer[3:]

print(f"Bokstävsgrupp: {bokstäver}\nSiffergrupp: {siffror}")

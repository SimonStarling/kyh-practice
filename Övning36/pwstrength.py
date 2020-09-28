def compute_strength(pw):
    points = 0

    if len(pw) >= 10:  # Kontrollerar längden på PW (antal char)
        points += 1

        if any(char.isdigit() for char in pw):  # Kontrollerar om PW innehåller Siffror

            if any(char.isalpha() for char in pw):  # Kontrollerar om PW innehåller Bokstäver
                points += 1

                special_char = "#%&+_-"  # Kontrollerar PW om den innehåller specialtecken
                if any(char in special_char for char in pw):
                    points += 1

    if not (len(pw) >= 10 or any(char.isdigit() for char in pw)
         or any(char.isalpha() for char in pw)
         or any(char in special_char for char in pw)):
         print("Ogiltligt lösenord!")
         points = 0
    return points

def compute_strength(pw):
    points = 0
    special_char = "#%&+_-"  # Kontrollerar PW om den innehåller specialtecken


    if len(pw) >= 10:  # Kontrollerar längden på PW (antal char)
        points += 1

    if any(char.isdigit() for char in pw):  # Kontrollerar om PW innehåller Siffror

        if any(char.isalpha() for char in pw):  # Kontrollerar om PW innehåller Bokstäver
            points += 1

    special_char = "#%&+_-"  # Kontrollerar PW om den innehåller specialtecken
    if any(char in special_char for char in pw):
        points += 1

    if any(not char.isalnum() and char not in special_char for char in pw):
        points = 0
        print("Ogiltligt")

    return points

from Övning36 import pwstrength

if __name__ == '__main__':
    password = input("Ange lösenord: ").strip() # Variabeln password håller värdet från input
    antal = pwstrength.compute_strength(password)
    print(antal)

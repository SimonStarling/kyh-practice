def is_it_too_long(name): # Kontrolerar längden på namnen som matas in
    return len(name) > 5


def main():
    students = input("Ange namn med kommatecken emellan: ").split(",") # Ber användaren skriva in namn och kommatecken

    for name in students:
        if is_it_too_long(name):
            print(f"{name} är för långt!")

if __name__ == '__main__':
    main()

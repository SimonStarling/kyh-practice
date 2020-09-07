def is_it_too_long(name):  # Kontrollerar längden på namnen som matas in
    return len(name) > 5


def main():
    students = input("Ange namn med kommatecken emellan: ").split(",")  # Ber användaren skriva in namn och kommatecken

    print(students)
    for name in students:

        if is_it_too_long(name):
            print(f"{name.title()} är för långt!")


if __name__ == '__main__':
    main()

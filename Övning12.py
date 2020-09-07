def is_it_too_long(name, max_length):  # Kontrollerar längden på namnen som matas in
    return len(name) > max_length


def main():
    try:
        max_length = int(input("Ange maxlängd på namn:"))
    except ValueError:
        max_length = 5

    students = input("Ange namn med kommatecken emellan: ").split(",")  # Ber användaren skriva in namn och kommatecken

    print(students)
    for name in students:

        if is_it_too_long(name):
            print(f"{name.title()} är för långt!")


if __name__ == '__main__':
    main()

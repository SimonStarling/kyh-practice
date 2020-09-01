# Basic IF-statment med fast boolean
is_male = False  # Hårdkodad vilkor.
is_tall = False

if is_male and is_tall:
    print("You are a  tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("Your a not a male but you are tall")
else:
    print("You are not a male nor tall")

print("\n")


# IF and Comparison
# Denna kod kommer att köra ett if-statment och jämföra variablerna med varandra.
# I detta fall så kommer num3 printas då den uppfyller IF-kravet.
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(30, 45, 90))
print("\n")

# Bättre Miniräknare med input och if-statements

num1 = float(input("Enter your first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter your second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid input")
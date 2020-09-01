# Basic IF-statment med fast boolean
is_male = False # Hårdkodad vilkor.
is_tall = False

if is_male and is_tall:
    print("You are a  tall male")
elif is_male and not (is_tall):
    print ("You are a short male")
elif not(is_male) and is_tall:
    print("Your a not a male but you are tall")
else:
    print("You are not a male nor tall")

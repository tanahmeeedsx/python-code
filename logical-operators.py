# Logical operators in python
# and , or , not
# and operator
not_married = True
age = 20
if not_married == True and age >= 18:
    print("Eligible for marriage")
else:
    print("Not eligible for marriage")

    # or operator
    is_student = False
    age = 22
    if is_student == True or age < 25:
        print("Eligible for student discount")
    else:
        print("Not eligible for student discount")

    # not operator
    is_adult = True
    if not is_adult:
        print("Not an adult")
    else:
        print("Is an adult")


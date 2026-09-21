def insert_user_in_database(name, age):
    print(f"User inserted in DB for {name}, {age}")


#A fuction haas to be called to execute it
insert_user_in_database("Alice", 30)

def insert_user_in_database(name, age):
    return f"User inserted in DB for {name}, {age}"

result = insert_user_in_database("Alice", 30)
print(result)


#Define the logic once and use it multiple times
def calculate_tax(amount, state):
    if state == "CA":
        return amount * 0.075
    elif state == "NY":
        return amount * 0.04
    else:
        return amount * 0.05
    return amount * tax_rate

# Reuse it 50 times with a single line of code
print(f"Customer 1 Tax: ${calculate_tax(100, 'CA')}")
print(f"Customer 2 Tax: ${calculate_tax(200, 'NY')}")
print(f"Customer 3 Tax: ${calculate_tax(300, 'TX')}")


#lambda or anonymous function
lambda arguments: expression

def double_number(num):
    return num * 2

print(double_number(5))  # Output: 10



# Using lambda function
double = lambda x: x * 2
print(double(5))  # Output: 10
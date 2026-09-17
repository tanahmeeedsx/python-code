#Comments
#Variables
#String (str)

name = "Tanjim Ahmed"
print(name)

status = 'Active'
print(status)

poem = '''Roses are red,
Violets are blue,
Sugar is sweet,
And so are you. '''

print(poem)
server_region = "us-west-2"
print(server_region)




#Integer (int)
page = 120 
coffee_price = 10.5     #decimal_float
print(page)
print(coffee_price)
print(type(page))
print(type(coffee_price))




#Boolean (bool)
is_class_running = True
print(is_class_running)
print(type(is_class_running))

num1 = 10
num2 = 20
print(num1 > num2)
print(type(num1 > num2))




#List
grocery_list = ["apples", "bananas", "milk", "bread", 12, 13.5, 125]
print(grocery_list)
print(type(grocery_list))



#Data_type_casting
coffee_price = 10.5
cup_cake_price = '200'
total_price = coffee_price + int(cup_cake_price)
print(total_price)
print(type(total_price))




#Casting and user_input
name = input("Enter your name:")
age = input("Enter your age:")
print(name)
print(age)
print(type(name))
print(type(age))



#string literal / string interpolation
print(f"My name is {name} and I am {age} years old.") #uses_in_industry
print("My name is {} and I am {} years old.".format(name, age))  #used_many_other_people
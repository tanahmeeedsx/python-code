# Multiplication of two numbers
# you buy 3 pizza for $10 each

pizza_price = 10
number_of_pizza = 3
total_cost = pizza_price * number_of_pizza
print("Total cost of pizza is: $", total_cost)

# Addition of two numbers
# you buy 3 pizza for $10 each and 2 burgers for $5 each
burger_price = 5
number_of_burger = 2
total_cost = (pizza_price * number_of_pizza) + (burger_price * number_of_burger)
print("Total cost of pizza and burger is: $", total_cost)

# Subtraction of two numbers
# you have $50 and you buy 3 pizza for $10 each and 2 burgers for $5 each
total_money = 50
remaining_money = total_money - total_cost
print("Remaining money after buying pizza and burger is: $", remaining_money)       

# Division of two numbers
# you have $50 and you buy 3 pizza for $10 each and 2 burgers for $5 each   
average_cost = total_cost / (number_of_pizza + number_of_burger)
print("Average cost per item is: $", average_cost)

# Modulus of two numbers
# you have $50 and you buy 3 pizza for $10 each and 2 burgers for $5 each   
remaining_money = total_money % total_cost
print("Remaining money after buying pizza and burger is: $", remaining_money)

# Exponentiation of two numbers
# you have $50 and you buy 3 pizza for $10 each and 2 burgers for $5 each   
total_cost = (pizza_price ** number_of_pizza) + (burger_price ** number_of_burger)
print("Total cost of pizza and burger is: $", total_cost)
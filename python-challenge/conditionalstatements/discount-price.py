#!/usr/bin/python3

def calculate_discount(price, discount_percentage):
	if discount_percentage < 1:
		return price * discount_percentage
	else:
		return price * (discount_percentage/100)


#take the user input

price =int(input('What is the price of your product? '))

print(f"discounted price = {calculate_discount(price,20)}")


print(f"total price = {price-calculate_discount(price,20)}")

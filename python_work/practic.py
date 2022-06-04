#age = 17
#if age >= 18:
#	print("You are old enough to vote!")
#	print("Have you registered to vote yet?")
#else:
#	print("Sorry, you are too young to vote.")
#	print("Please register to vote as soon as you turn 18!")
age = 3
if age < 4:
	cost = 0
elif age < 18:
	cost = 5
elif age >= 18:
	cost = 10
elif age > 65:
	cost = 5
print('Your cost is ' + str(cost))



requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings: 
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings: 
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings: 
	print("Adding extra cheese.")
print("\n\tFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	 if requested_topping == 'green peppers':
	 	print("Sorry, we are out of green peppers right now.")
	 else:
	    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings: 
		print("Adding " + requested_topping + ".") 
		print("\nFinished making your pizza!")
	else:
		print("Are you sure you want a plain pizza?")


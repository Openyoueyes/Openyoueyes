pizza = ['margorita', 'pepperoni', 'extracheese']
for i in pizza:
	print('I like ' + i + ' pizza')
print('I really love pizzza!')
pizza_frinds = pizza[:]
pizza.append('italiano')
print(pizza)
pizza_frinds.append('mushrooms')
print(pizza_frinds)
print ("My favorite:")
for i in pizza:
	print(i)
print("Friend favorite:")
for i in pizza_frinds:
	print(i)
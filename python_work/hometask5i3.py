#alien_color = 'green'
#if alien_color == 'green':
#	point = 5
#print("You earn = " + str(point) + " points")
alien_color = 'red'
if alien_color == 'green':
	point = 5
	print("You earn = " + str(point) + " points")
elif alien_color == 'yellow':
	point = 10
	print("You earn = " + str(point) + " points")
elif alien_color == 'red':
	point = 15
	print("You earn = " + str(point) + " points")

age = 78
if age < 2:
	age_category = 'infant'
elif age >= 2 and age < 4:
	age_category = 'baby'
elif age >= 4 and age < 13:
	age_category = 'kid'
elif age >= 13 and age < 20:
	age_category = 'young'
elif age >= 20 and age < 65:
	age_category = 'adult'
else: 
	age_category = 'old'
print(age_category)
fruit = ['apple', 'orange', 'pinapple', 'lemon', 'banana', 'pear']
if 'apple' in fruit:
      print('Yes')
favorite_fruits = ['banana', 'pinapple', 'pear']
if 'banana' in fruit:
	print('You really like banana!')
if 'pinapple' in fruit:
	print('You really like pinapple!')
if 'pear' in fruit:
	print('You really like pear!')



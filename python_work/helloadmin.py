names = ['Ilya','Diana','Svetlana',
		'Denis','Alexander','Michel','admin']
for names in names:
	if names == 'admin':
		print('Hello admin, would you like to see a status report?')
	elif names != 'admin':
		print('Hello ' + names + ', thank you for logging in again')
requested_toppings = []
if names:
	for i in names:
		print()		
else:
	print("We need to find some users")
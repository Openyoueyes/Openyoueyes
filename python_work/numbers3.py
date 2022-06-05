people_numbers = {'Ilya':[11,2,3], 'Diana':[7,3,1], 
				  'Oleg':[2,5,8], 'Dmitriy':[72,23,11], 'Andrey':[22,11,33]
				 }
for name,numbers in people_numbers.items():
	print(f'{name} favorite numbers:')
	for i in numbers:
		print(i)
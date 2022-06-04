famous_human = {'first_name': 'diana', 
				'last_name': 'hromova',
				'age': 27, 'city': 'homel'
				}
print(famous_human['first_name'].title(), 
	  famous_human['last_name'].title(),
	  str(famous_human['age']),
	  famous_human['city'].title())

people_numbers = {'Ilya':11, 'Diana':7, 
				  'Oleg':666, 'Dmitriy':72, 'Andrey':22
				 }
print('Ilya favorite numbers is: ' + str(people_numbers['Ilya']))

glossary = {'concatenatio': '- the operation of gluing objects of a linear structure',
			'lists': '- this is an abstract data type',
			'dairy': '- data structures designed to combine interrelated information',
			'tuples': '- values that cannot change are called immutable',
			'animal': 'cat,dog'
			}
for key,value in glossary.items(): 
	print('\nKey: ' + key)
	print('Value: ' + value)

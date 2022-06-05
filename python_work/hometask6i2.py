diana= {'first_name': 'diana', 
		'last_name': 'hromova',
		'age': 27, 'city': 'homel'
		}
ilya = {'first_name': 'ilya', 
		'last_name': 'glotov',
		'age': 28, 'city': 'senno'
		}
messi = {'first_name': 'messi', 
		'last_name': 'glotov',
		'age': 1, 'city': 'minsk'
		}
people = [diana, ilya, messi]
for people in people:
	print(people)

messi = {'cat':'ilya'}
destiny ={'dog':'diana'}
pets = [messi, destiny]
for pet in pets:
	for Name_pet,owner in pet.items():
	 print(f"{Name_pet} {owner.title()}")



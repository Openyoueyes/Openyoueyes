pets = []
murca = {'cat': 'alex'}
barbos = {'dog': 'vitalik'}
pirate = {'bird': 'kate'}
pets.append(murca)
pets.append(barbos)
pets.append(pirate)
for pet in pets:
	for kind, owner in pet.items():
	    print(f"{owner.title()}'s {kind}.")
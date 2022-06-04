input (user_name)
favorite_places = {'diana': ['minsk', 'homel', 'london'],
       'ilya': ['senno', 'orsha', 'mogilev'],
       'edward': ['moskov', 'brest'],
       'phil': ['vileika', 'stolbc'],
       }
for user_name,city in favorite_places.items():
	print(f"{user_name.title()} favorite place is:")
	for i in city:
		print(i.title())
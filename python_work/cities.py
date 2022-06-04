cities = {
	'minsk':{
		'country':'belarus',
		'population':1972643,
		'fact': 'Belarus lives'
		},
	'london':{
		'country':'uk',
		'population': 8982137,
		'fact':'very expensive city'
		},
	'senno':{
		'country': 'belarus',
		'population':  7027,
		'fact': 'the best city in Belarus'

	},
}
print(cities)
for city,city_info in cities.items():
		print(f'{city.title()}')
		country_info = city_info['country']
		population_info = city_info['population']
		fact_info = city_info['fact']
		print(f'\tcountry: {country_info.title()}')
		print(f'\tpopulation: {population_info}\n\tfact: {fact_info}')



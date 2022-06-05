lakes = {'nile':'egypt', 'dnepr':'belarus', 'amazonka': 'mexico'}
for lake,country in lakes.items():
	print('The ' + lake.title() + ' runs througt ' + country.title())
for lake in lakes.keys():
	print(lake.title())
print('\n')
for country in lakes.values():
	print('\t' + country.title())
favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
names = ['jen', 'sarah', 'edward', 'phil', 'ilya', 'diana']
for name in favorite_languages.keys():
	if name in names:
		print('Thank you for participating: ' + name.title())
	elif name not in names:
		print('Еake part: ' + name)
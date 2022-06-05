favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
names = ['jen', 'sarah', 'edward', 'phil', 'ilya', 'diana']
for name in names:
	if name in favorite_languages.keys():
		print('Thank you for participating: ' + name.title())
	elif name not in favorite_languages.keys():
		print('Еake part: ' + name.title())
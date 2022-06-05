car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
names = ['ilya','diana','messi']
name = 'david'
if name not in names:
   print(name.title() + '- this name is not included in the list')
print('alla' in names)
print('ilya' in names)
print(names[0] == 'lya')
numbers1 = 4
numbers2 = 3
print('\n')
print(numbers2 >= numbers1)
print(numbers1 == 3 or numbers2 == 3)
print((numbers1 == 4) and (numbers2 == 3))
print (numbers2 > 5)
if numbers1 != 2:
   print('Numbers1 not equals two')
fruit = ['orange', 'pinapple', 'lemon', 'apple', 'pear']
for i in fruit:
   if i == 'pinapple':
      print(i.title())
   else:
      print(i.upper())

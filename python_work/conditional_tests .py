numbers = list(range(1,10))
print(numbers)
if numbers[0] >= 2:
   print('True')
else:
   print('False')
fruit = ['orange', 'pinapple', 'lemon', 'apple', 'pear']
for i in fruit:
   if i == 'pinapple':
      print(i.title())
   else:
      print(i.upper())
for i in fruit:
   if i != "orange":
      print(i)
car = 'BMW'
print(car == 'Bmw')
print(car != 'Bmw')
print(car.lower() == 'BMW')
print(car.lower() == 'bmw')
numbers = list(range(1,12))
print(numbers[0] > 2)
print(numbers[0] < 2)
print(numbers[10] >= 5)
print(numbers[10] <= 5)
print(numbers)
print(numbers[10] <=2 and numbers[2] <= 2)
print(numbers[10] >=2 or numbers[9] >= 2)
print('\n')
if 10 in numbers:
   print('true')
else: 
   print('false')
if 10 not in numbers:
   print('true')
else:
   print('false')
one = 22
if one not in numbers:
   print("it is not")
else:
   for i in numbers:
      print(i)




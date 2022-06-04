motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
motorcycles[0] = 'ducati' 
print(motorcycles)
motorcycles.append('ducati') 
print(motorcycles)
#Метод append() упрощает динамическое построение списков. 
#Например, вы можете начать с пустого списка и добавлять в него элементы серией команд append(). В следующем примере в пустой список добавляются элементы 'honda', 'yamaha' и 'suzuki':
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(2, 'ducati') 
print(motorcycles)

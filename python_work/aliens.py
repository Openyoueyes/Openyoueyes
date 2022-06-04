# Создание пустого списка для хранения пришельцев.
aliens = {}
aliens['easy']= {'color': 'green', 'points': 5, 'speed': 'slow'}
aliens['medium']= {'color': 'yellow', 'points': 10, 'speed': 'average'}
aliens['hard']= {'color': 'black', 'points': 20, 'speed': 'fast'}
aliens['boss']= {'color': 'red', 'points': 50, 'speed': 'crazy'}
for alien,aliens_info in aliens.items():
    print(f'\nDifficulty level {alien}')
    alien_c = aliens_info['color']
    alien_p = aliens_info['points']
    alien_s = aliens_info['speed']
    print(f'color:{alien_c} points:{alien_p} speed:{alien_s}')
# Создание 30 зеленых пришельцев.
aliens_d =[]
for alien_number in range(30):
    new_alien = aliens['boss']
    aliens_d.append(new_alien)
#Вывод первых 5 пришельцев:
for alien in aliens_d[:5]:
   print(alien)
print("...")
# Вывод количества созданных пришельцев.
print("Total number of aliens: " + str(len(aliens_d)))
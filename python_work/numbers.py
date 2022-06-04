#squares = []                                                                  
#for value in range(1,11):
#  squares.append(value**2)
#print(squares)

squares = []
for value in range(1,11):
  sqare = value**2
  squares.append(sqare)
print(squares)
print(sum(squares))

squares = [value**2 for value in range(1,11)]
   print(squares)

Настройка Sublime Text для Python 3
Если для запуска терминального сеанса Python вместо python используется другая команда, вам придется настроить Sublime Text, чтобы программа знала, где найти правильную версию Python в вашей системе. Чтобы узнать полный путь к интер- претатору Python, введите следующую команду:
$ type -a python3
python3 is /usr/local/bin/python3
Теперь откройте Sublime Text и выберите команду ToolsBuild SystemNew Build System. Команда открывает новый конфигурационный файл. Удалите его текущее содержимое и введите следующий код:
   {
       "cmd": ["/usr/local/bin/python3", "-u", "$file"],
}
Этот код приказывает Sublime Text использовать команду python3 вашей си- стемы для запуска текущего открытого файла. Проследите за тем, чтобы в коде использовался путь, полученный при выполнении команды type -a python3 на предыдущем шаге. Сохраните файл с именем Python3 .sublime-build в каталоге по умолчанию, который Sublime Text открывает при выполнении команды Save.
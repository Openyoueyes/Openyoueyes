week = []
print(week)
#'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday'
week.insert(0,'Monday')
week.insert(1,'Tuesday')
print(week)
week.append('Wednesday')
print(week)
day3 = week.pop()
print(week)
print(day3)
week.insert(2,day3)
week.insert(3, 'Thursday')
print(week)
week.insert(4, 'Friday')
week.insert(5, 'Saturday')
day1 = week.pop(1)
print(week)
week.insert(1,day1)
print(week)
day5 = 'Friday'
week.remove('Friday')
print(week)
print('Day del ' + day5)
print(week)
print(sorted(week,reverse=True))
print(week)
week.sort(reverse=True)
print(week)
print(len(week))
del week[0:6]
print(week)



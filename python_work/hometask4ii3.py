#numbers = range(1,21)
#for i in numbers:
#	print(i)
#numbers = range(1,1000001)
#print(min(numbers),max(numbers), sum(numbers))
#numbers_odd = list(range(3,33,3))
#for numbers in numbers_odd:
#	print(numbers)
#numbers = [cube**3 for cube in range(1,10)]
#print(numbers)
numbers = []
for cube in range(1,10):
 numbers.append(cube**3)
print(numbers)
print("The first three items in the list are:")
for i in numbers[:3]:
	print(i)
print("Three items from the middle of the list are:")
for i in numbers[4:7]:
	print(i)
print(numbers)
print("The last three items in the list are:")
for i in numbers[-3:]:
	print(i)
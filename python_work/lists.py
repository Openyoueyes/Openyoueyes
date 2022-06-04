#bcycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(bicycles)
#-1 обрашение к последнему элементу в списке
#Индекс –2 возвращает второй эле- мент от конца списка, индекс –3 — третий элемент от конца и т. д.
bicycles = ['trek', 'cannONdale', 'redline', 'specialized']
print(bicycles[1].lower())
print(bicycles[2].upper())
print(bicycles[-1].title())
message = "My first bicycle was a " + bicycles[0].title() + "." 
print(message)

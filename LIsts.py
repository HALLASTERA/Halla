#           0        1        2        3        4
fruits = ['Yabloko','banan','Viwnya','Sliva','Persik'] #Массив фруктов

print(fruits)
print(len(fruits)) # "len" какой длины массив
print(fruits[4])
print(fruits[1].upper()) #.upper() делает большими буквами массив
print(fruits[-2]) # показывает второй элемент массива с конца
fruits[1] = 'qiwi' # заменяет элемент массива на другой
print(fruits)
fruits.append('4ernosliv') # dobavlyaet v konec massiva novui element
print(fruits)
fruits.append('Moloko')
print(fruits)
fruits.insert(0,'vinograd') # dobavlyaet na nomer massiva nujnui element insert dobavi't
fruits.insert(4,'morkov')
print(fruits)
print(fruits[0].upper())
print(fruits)

del fruits[2] # удаление элемента массива по номеру
print(fruits)
fruits.remove('Viwnya') # удаление элемента массива по названию
print(fruits)

deleted_fruits = fruits.pop(2) #deleted_nazvanie = nazanive_pop() udalenie  elementa i ego pokaz
print("deleted fruits is:" + deleted_fruits )
fruits.sort() # sortirovka po alfavitu
print(fruits)

fruits.sort(reverse=True) # sortirovka po drugomu randomno
print(fruits)
fruits.reverse() # sortirovka naoborot
print(fruits)

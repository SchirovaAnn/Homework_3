list_1 = input('Введите несколько цифр, разделенных запятой')
list_2 = input('Введите несколько цифр, разделенных запятой')

list_1 = list_1.split(',')
list_2 = list_2.split(',')

list_1 = set([int(x) for x in list_1])
list_2 = set([int(x) for x in list_2])

list_new = list(list_1 - list_2)

print(', '.join(str(el) for el in list_new))

len_list = int(input('Введите количество элементов списка: '))

my_list = []
for i in range(len_list):
    my_list.append(int(input(f'Введите {i} элемент: ')))

my_list.sort()
print(my_list)
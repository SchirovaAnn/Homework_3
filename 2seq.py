my_list = input('Введите несколько цифр, разделенных двоеточием, точкой с запятой или / ')

if ',' in my_list:
    my_list = my_list.split(',')
elif ';' in my_list:
    my_list = my_list.split(';')
else:
    my_list = my_list.split('/')


my_list_new = []
for el in my_list:
    my_list_new.append(int(el))

print(', '.join(str(el) for el in list(set(my_list_new))))
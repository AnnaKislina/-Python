from data_create import name_data,surname_data,phone_data,address_data

#--------------------внести контакт-------------------------------------------------
def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f'В каком формате записать данные?\n\n'
                    f'1 вариант:\n'
                    f'{name}\n{surname}\n{phone}\n{address}\n\n'
                    f'2 вариант: \n'
                    f'{name}; {surname}; {phone}; {address}\n\n'
                    f'Выберите вариант: '))
    
    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите число '))


    if var == 1:
        with open('data1.csv', 'a', encoding='utf-8') as f: 
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")       
    elif var == 2:
        with open('data2.csv', 'a', encoding='utf-8') as f:      
            f.write(f"{name}; {surname}; {phone}; {address}\n\n")
            
#------------------------найти контакт---------------------------------------------
""" def find_data():
    with open('data2.csv', 'r', encoding='utf8') as f:
        seach_param = (input('Введите параметр для поиска: ' ).title())
        for line in f:
            if seach_param in line:
                print(line) """
                
#-------------------------удалить контакт--------------------------------------------
""" def del_data():
    with open(f'data2.csv', 'r', encoding="utf-8") as f:
        X = input('Введите Имя или Фамилию для удаления: ')
        lines = f.readlines()
        with open('data2.csv', 'w', encoding="utf-8") as f:
            for line in lines:
                if X in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    f.write(line) """

#----------------------изменить контакт-----------------------------------------------
""" def change_data():
    first = 'data1.csv'
    second = 'data2.csv'
    file_name = input('Введите имя файла, в котором нужно изменить данные (data1.csv, data2.csv): ')
    if file_name == first:
        with open(first, 'r', encoding='utf-8') as f:
            data = f.readlines()
    elif file_name == second:
        with open(second, 'r', encoding='utf-8') as f:
            data = f.readlines()
    else:
        print('Неправильное имя файла')

    print('Текущие данные:')
    print(*data)

    index_to_modify = int(input('Введите номер строки для изменения: ')) - 1
    if 0 <= index_to_modify < len(data):
        new_data = input('Введите новые данные: ')
        data[index_to_modify] = f'{new_data}\n'
        if file_name == first:
            with open(first, 'w', encoding='utf-8') as f:
                f.writelines(data)
        elif file_name == second:
            with open(second, 'w', encoding='utf-8') as f:
                f.writelines(data)
        print('Данные успешно изменены!')
    else:
        print('Неверный номер строки.')
                 """
#----------------------печать всех контактов-----------------------------------------------
def print_data():
    print('Вывожу данные из 1 файла:  \n')
    with open('data1.csv','r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first)-1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))
    print('Вывожу данные из 2 файла:  \n')
    with open('data2.csv','r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)


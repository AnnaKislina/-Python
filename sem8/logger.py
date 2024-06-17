from data_create import name_data,surname_data,phone_data,address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name};{surname};{phone};{address}\n\n"
    f"2 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"Выберите вариант: "))
    while var  != 1 and var  != 2:
        print("Неправильно введена команда, повтори: ")
        var = int(input(f"В каком формате записать данные\n\n"
        f"1 Вариант: \n"
        f"{name}\n{surname}\n{phone}\n{address}\n\n"
        f"2 Вариант: \n"
        f"{name};{surname};{phone};{address}\n\n"
        f"Выберите вариант: "))

    if var == 1:
        with open('data1.csv','a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data2.csv','a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

#--------------------------------------------------------------
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
               


#---------------------------------------------------------------
def find_data():
    with open('data2.csv', 'r', encoding='utf8') as f:
        seach_param = (input('Введите имя или фамилию для поиска: ' ).title())
        for line in f:
            if seach_param in line:
                print(line)
                
"""     search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона', '4': 'Адрес'}
    found_contacts = []
    with open('data2.csv','r', encoding='utf-8') as f:
        contact_list = f.readlines()
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print() """

""" def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n2 - по имени')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    return search_field, search_value """

#-----------------------------------------------------------------
def change_data():
    pass
def del_data():
    pass

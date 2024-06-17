from data_create import name_data,surname_data,phone_data,address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n\n"
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
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n\n")
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
               


#----------------------поиск контакта-----------------------------------------
def find_data():
    seach_param = (input('Введите имя или фамилию для поиска: ' ).title()) 
    with open('data2.csv', 'w', encoding='utf8') as f:                # поиск во второй книге
        for line in f:
            if seach_param in line:
                print(line)
   
    search_field, search_value = search_parameters()          # поиск в первой книге
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона', '4': 'Адрес'}
    found_contacts = []
    with open('data1.csv','w', encoding='utf-8') as f:
        contact_list = f.readlines()
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print(found_contacts)

def search_parameters():
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
    return search_field, search_value

#------------------изменить контакт-----------------------------------------------
def change_data():
    with open('data2.csv', 'r', encoding='utf8') as f: 
            seach_param = (input('Введите параметр для поиска: ' ).title())
            with open ('data2.csv', 'w', encoding='utf8') as f:
                for line in seach_param:
                    if seach_param in line:
                        print(line)
                        add_f = (input('Введите Имя: ' ).title())
                        add_i = (input('Введите фамилию: ' ).title())
                        add_tel = (input('Введите телефон: ' ).title())
                        new_line = add_f +' '+add_i +' '+ add_tel + '\n'
                        line = line.replace(line, new_line)
                    f.writelines(line)


#----------------удалить контакт-------------------------------------------------
def del_data():
    with open('data2.csv', 'r', encoding='utf8') as f: 
        X = input('Введите Имя или Фамилию для удаления: ')
        lines = f.readlines()
        with open ('data2.csv', 'w', encoding='utf8') as f:
            for line in lines:
                if X in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    f.write(line)

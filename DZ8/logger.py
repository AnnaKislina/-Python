from data_create import name_data,surname_data,phone_data,address_data

#--------------------внести контакт-------------------------------------------------
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
            
#------------------------найти контакт---------------------------------------------
def find_data():
    with open('data2.csv', 'r', encoding='utf8') as f:
        seach_param = (input('Введите параметр для поиска: ' ).title())
        for line in f:
            if seach_param in line:
                print(line)
                
#-------------------------удалить контакт--------------------------------------------
def del_data():
    with open(f'data2.csv', 'r', encoding="utf-8") as f:
        X = input('Введите Имя или Фамилию для удаления: ')
        lines = f.readlines()
        with open('data2.csv', 'w', encoding="utf-8") as f:
            for line in lines:
                if X in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    f.write(line)

#----------------------изменить контакт-----------------------------------------------
def change_data():
    with open('data2.csv', 'r', encoding="utf-8") as f:
        seach_param = (input('Введите параметр для поиска: ' ).title())
        with open ('data2.csv', 'w', encoding='utf8') as of:
            for line in seach_param:
                if seach_param in line:
                    print(line)
                    add_f = (input('Введите фамилию: ' ).title())
                    add_i = (input('Введите Имя: ' ).title())
                    add_tel = (input('Введите телефон: ' ).title())
                    new_line = add_f +' '+add_i +' '+ add_tel + '\n'
                    line = line.replace(line, new_line)
                f.writelines(line)
                
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

"""     with open('data1.csv', 'r', encoding='utf8') as f:
        print()
        for line in f:
            print(line)  """ 
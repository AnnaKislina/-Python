from logger import input_data, print_data, find_data, change_data, del_data

def interface():
    print("Привет. Это бот телефонного справочника \nВыбери действие: \n 1- записать контакт \n 2- печать контактров \n 3- найти контакт\n 4- изменить конатакт\n 5- удалить конатакт")
    comand = int(input("Введите 1 или 2 : "))
    while comand != 1 and comand != 2 and comand != 3 and comand != 4 and comand != 5:
        print("Неправильно введена команда, повтори: ")
        comand = int(input("Введите 1,2,3,4,5 : "))
    
    if comand == 1:
        input_data()
    elif comand == 2:
        print_data()
    elif comand == 3:
        contact_list = list(input("Введите Имя или Фамилию для поиска контакта: "))
        find_data(contact_list)
    elif comand == 4:
        change_data()
    elif comand == 5:
        del_data()


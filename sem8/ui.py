from logger import input_data, print_data, find_data, change_data, del_data

def interface():
    print("Привет. Это бот телефонного справочника \nВыбери действие: \n 1- записать контакт \n 2- печать контактров \n  3- изменить конатакт\n 4- удалить конатакт")
    comand = int(input("Введите 1,2,3,4 : "))
    while comand != 1 and comand != 2 and comand != 3 and comand != 4 
        print("Неправильно введена команда, повтори: ")
        comand = int(input("Введите 1,2,3,4,5 : "))
    
    if comand == 1:      # записать контакт
        input_data()
    elif comand == 2:      # печать контактов
        print_data()
    elif comand == 3:      # изменить контакт
        find_data()
    elif comand == 4:      # удалить контакт
        change_data()



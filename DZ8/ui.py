from logger import input_data, print_data
from change_and_del import update_data, delete_data

def interface():
    print_menu()
    comand = int(input('Введите номер задачи от 1 до 5: '))
    if comand > 5: print('Неправильно введена команда, повтори: ')
    if comand == 5: print('Выход')
    else:
        match comand:
            case 1: # добавить контакт
                input_data()
                interface()   
            case 2: # вывести все контакты
                print_data()
                interface()
            case 3: # изменить контакт
                update_data()
                interface()
            case 4: # удалить контакт
                delete_data()
                interface() 

def print_menu():
    print("""
 ------------------------------- \n
 1 - добавить контакт
 2 - вывести все контакты
 3 - изменить данные контакта 
 4 - удалить контакт 
 5 - выход 
 ------------------------------- \n 
    """)
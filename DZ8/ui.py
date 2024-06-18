from logger import input_data, print_data, find_data, change_data, del_data

def interface():
    print_menu()
    comand = int(input('Введите номер задачи от 1 до 6: '))
    if comand > 6: print('Неправильно введена команда, повтори: ')
    if comand == 6: print('Выход')
    else:
        match comand:
            case 1: # добавить контакт
                input_data()
                interface()   
            case 2: # вывести все контакты
                print_data()
                interface()
            case 3: # поиск контактов
                find_data()
                interface()
            case 4: # изменить контакт
                change_data()
                interface()
            case 5: # удалить контакт
                del_data()
                interface() 

def print_menu():
    print("""
 ------------------------------- \n
 1 - добавить контакт
 2 - вывести все контакты
 3 - поиск контакта 
 4 - изменить данные контакта 
 5 - удалить контакт 
 6 - выход 
 ------------------------------- \n 
    """)
from logger import input_data, print_data

def interface():
    print("Привет. Это бот телефонного справочника \nВыбери действие: \n 1- записать данные \n 2- вывод данных ")
    comand = int(input("Введите 1 или 2 : "))
    while comand != 1 and comand != 2:
        print("Неправильно введена команда, повтори: ")
        comand = int(input("Введите 1 или 2 : "))
    
    if comand == 1:
        input_data()
    elif comand == 2:
        print_data()



#-------------------------считываем данные из файла(вход имя файла и разделитель) на выходе получаем список--------------------------------------------
def read_data(file_path, separator):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
    if separator == '\n':
        records = [record.split(separator) for record in content.split('\n\n') if record]
    else:
        records = [record.split('; ') for record in content.split('\n') if record]
    return records

#-------------------------записываем данные в файл(вход имя файла,новые данные и разделитель)--------------------------------------------
def write_data(file_path, data_list, separator):
    with open(file_path, 'w', encoding='utf-8') as f:
        for datal in data_list:
            if separator == '\n':
                f.write(separator.join(datal).strip() + '\n\n')
            else:
                f.write('; '.join(datal).strip() + '\n')
                
#-------------------------печать номер контакта и сам контакт--------------------------------------------
def display_records(data_list):
    for index, datal in enumerate(data_list):
        print(f"{index + 1}. {'; '.join(datal)}")
        
#-------------------------удалить контакт--------------------------------------------
def update_data():
    name_file = input("В каком файле вы хотите изменить данные?(data1.csv или data2.csv): ")
    if name_file == 'data1.csv':
        separator = '\n'
    else:
         separator = '; '

    data_list = read_data(name_file, separator)
    display_records(data_list)

    num = int(input('Введите номер записи для изменения: ')) - 1
    if 0 <= num < len(data_list):
        new_name = input('Введите новое имя: ')
        new_surname = input('Введите новую фамилию: ')
        new_phone = input('Введите новый телефон: ')
        new_address = input('Введите новый адрес: ')

        data_list[num] = [new_name, new_surname, new_phone, new_address]
        write_data(name_file, data_list, separator)
        print('Данные успешно обновлены.')
    else:
        raise IndexError
        
#-------------------------удалить контакт--------------------------------------------
def delete_data():
    name_file = input("В каком файле хотите удалить данные?(data1.csv или data2.csv): ")
    if name_file == 'data1.csv':
        separator = '\n'
    else:
         separator = '; '

    data_list = read_data(name_file, separator)
    display_records(data_list)

    num = int(input('Введите номер записи для удаления: ')) - 1
    if 0 <= num < len(data_list):
        del data_list[num]
        write_data(name_file, data_list, separator)
        print('Запись удалена.')
    else:
        raise IndexError
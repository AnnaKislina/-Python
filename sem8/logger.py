from data_create import name_data,surname_data,phone_data,address_data

#-----------------записать контакт---------------------------------------------
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
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n")
    elif var == 2:
        with open('data2.csv','a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

#---------------------печать всех контактов-----------------------------------------
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
               

#------------------изменить контакт-----------------------------------------------
def change_data():
    var=int(input('Выберите в каком файле будете производить изменения (1 или 2): '))
    while var  != 1 and var  != 2:
        print("Неправильно введена команда, повтори: ")
        var=int(input('Выберите в каком файле будете производить изменения (1 или 2): '))
    if var == 1 :
        change_dop_data()    
    elif var == 2:
        with open('data2.csv', 'r', encoding='utf8') as f: 
                seach_param = (input('Введите параметр для поиска: ' ).title())
                with open ('data2.csv', 'w', encoding='utf8') as f:
                    for line in seach_param:
                        if seach_param in line:
                            print(line)
                            fam = (input('Имя: ' ).title())
                            name = (input('Фамилия: ' ).title())
                            tel = (input('Телефон: ' ).title())
                            adr = (input('Телефон: ' ).title())
                            new_line = fam +';'+ name +';'+ tel +';'+ adr +'\n'
                            line = line.replace(line, new_line)
                        f.writelines(line)



def change_dop_data():      # функция замены контакта
     with open('data1.csv','r',encoding='utf-8') as f:
            data_first=f.readlines()  
            data_first_list=[]              
            j=0
            for i in range(1,len(data_first)):
                if data_first[i]=='\n':  
                    data_first_list.append(''.join(data_first[j:i])) 
                    j=i
                elif i==len(data_first)-1:
                    data_first_list.append(''.join(data_first[j:i+1]))   
        
        num = int(input(f'Всего записей {len(data_first_list)}. Введите номер записи, в которой бдут изменения: ')) 
        while num > len(data_first_list) or num < 1 :
            print('Неправильный ввод')
            num = int(input(f'Введите число от 1 до {len(data_first_list)}: '))
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        adress = adress_data()
        new_kontact = '\n' + name + '\n' + surname + '\n' + phone + '\n' + adress + '\n'
        data_first_list[num - 1] = new_kontact

        with open('data1.csv','w',encoding='utf-8') as f:
            f.write(''.join(data_first_list))

    
    

#----------------удалить контакт-------------------------------------------------
def del_data():
"""     with open('data2.csv', 'r', encoding='utf8') as f: 
        X = input('Введите Имя или Фамилию для удаления: ')
        lines = f.readlines()
        with open ('data2.csv', 'w', encoding='utf8') as f:
            for line in lines:
                if X in line:
                    print("Нет такой строки")
                else:
                    print(line)    
                    f.write(line) """
    var=int(input('Введите номер справочника, в которм нужно удалить запись: '))
    while var !=1 and var !=2:
        print('Неправильный ввод')
        var=int(input('Введите число 1 или 2: '))
    if var==1:
        with open('data_first_variant.csv','r',encoding='utf-8') as f:
            data_first=f.readlines()  
            data_first_list=[]              # каждую строку будем добавлять в список
            j=0
            for i in range(1,len(data_first)):
                if data_first[i]=='\n':  # i-тый элемент равен переходу на новую строку или i=последней записи
                    data_first_list.append(''.join(data_first[j:i])) # в список добавляем элемент. Преобразовываем список в строку с помощью функции join
                    j=i
                elif i==len(data_first)-1:
                    data_first_list.append(''.join(data_first[j:i+1]))
        #print(data_first_list)
        
        num_zap=int(input(f'Всего записей {len(data_first_list)}. Введите номер записи, которую нужно удалить: ')) 
        while num_zap>len(data_first_list) or num_zap<1:
            print('Неправильный ввод')
            num_zap=int(input(f'Введите число от 1 до {len(data_first_list)}: '))  
        data_first_list.pop(num_zap-1)
        #print(data_first_list)

        with open('data_first_variant.csv','w',encoding='utf-8') as f:
            f.write(''.join(data_first_list)) 
    if var==2:
        with open('data_second_variant.csv','r',encoding='utf-8') as f:
            data_second=f.readlines() 
            #print(data_second)
            data_second2=[i for i in data_second if i!='\n' ]
            #print(data_second2)
        num_zap=int(input(f'Всего записей {len(data_second2)}. Введите номер записи, которую нужно удалить: ')) 
        
        while num_zap>len(data_second2) or num_zap<1:
            print('Неправильный ввод')
            num_zap=int(input(f'Введите число от 1 до {len(data_second2)}: '))
        
        data_second2.pop(num_zap-1) 
        data_second2=[i+'\n' for i in data_second2]
        #print(data_second2)
        
        with open('data_second_variant.csv','w',encoding='utf-8') as f:
            f.write(''.join(data_second2))
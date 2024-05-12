line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

#работа со строками
text = "Привет как дела Еще и настроение"
print('Еще' in text) #проверка естьли фрагмент в тексте
print(len(text)) #длинна текста
print(text.lower()) #нижний регистр
print(text.upper()) #верхний регистр
print(text.replace('Еще','ещё')) #замена фрагмента на фрагмент
print(text[len(text)-1]) #последний элемент текста
print(text[:6]) #выводим с первого до шестого элеента
print(text[::6]) #выводим с первого элемента до последнего с шагом 6
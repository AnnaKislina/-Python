n = 1.89
print(type(n))
n = 'Hello\''
print(f"значение переменной n = {n}")


#ввод данных
print('введите переменную а')
a = input()
print(f"значение переменной а = {a}")
b = input('Введите переменную b: ')


#привидение типов
n1 = int(a)
n2 = int(b)
print(f"a + b = {a+b}")
print(f"a + b = {n1+n2}")


#округление переменных
a = 5.896544
b = 6.55478
print(round(a*b,3))

#логические переменные
a = 1 < 4 and b > 3
a = 1 != 2

#Пример 1
username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Марина':
    print('Ура, это же Марина!')
elif username == 'Ильнар':
    print('Ура, это же Ильнар!')
else:
    print('привет, ', username)


#Пример 2
n = 423
summa = 0
while n > 0 :
    x = n % 10
    summa = summa + x
    n = n // 10
print(summa)


#Пример 3
i = 0
while i < 5 :
    if i ==3:
        break
    i = i + 1
else:
    print('Пожалуй')
    print('хватит')
print(i)


#Пример 4 
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0:
        flag = False
        print(i)
    elif i > n //2:
        print(n)
        flag = False
    i += 1


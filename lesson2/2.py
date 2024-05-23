# создание списка
list1 = []
list1 = list()
list1 = [1,2,3]

print(list1[0])
print(list1[-1])
list1.append(8)  # добавить в конец списка
print(list1)

list2 = []
for i in range(5):
    list2.append(i)
print(list2)
#------------------------------------------
# Создание Кортеж
t = ()
t = (1,)
v = tuple(list1)

a,b,c,d = v      # 1 2 3 8 каждый элемиент присваиваеться в отдельную переменную
print (a,b,c,d)

for i in v:
    print(i)      #печать кортежа

for i in range(len(v)):
    print(v[i])   #печать кортежа

#------------------------------------------
# Создание словаря
d = {}
d = dict()

d['q'] = 'qwerty'
d['w'] = 'wsx'
print(d)

#------------------------------------------
# Создание множества
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

#------------------------------------------
# Создать список чисел от 1 до 100

list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]


# 2. Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]

# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]

# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]













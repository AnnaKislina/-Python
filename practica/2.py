def func(**kwargs):     #неограниченное кол-во именнованых аргументов
    return sum(kwargs.values())


s = func(a=100, b=200, c=600, d=700)
print(s)
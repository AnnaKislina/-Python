""" def sum_num (n, y = 'Hello'):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa

s = sum_num(5, 'Qwerty')
print(s) """

#------------------------------------------------------------
""" def sum_str (*args):     #неограниченное количество поступаюзщих аргументов
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('H','e','l','l','o','o')) """

#----------------------------------------------------
""" #Импортируем файл modul.py рассмотрим 4 варианта
import modul
print(modul.max1(5,9))

from modul import max1
print(max1(10,9))

from modul import *
print(max1(1,9))

import modul as m1
print(m1.max1(13,9)) """
#-------------------------------------------------------------

""" #Рекурсия числа Фибоначи
def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n-2)

list1 = []
for i in range(1,10):
    list1.append(fib(i))

print(list1) """

#----------------------------------------------------------

""" #Быстрая сортировка
def quick_sort(arr):
    if len(arr) <=1:
        return arr
    else:
        pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]        
    greater = [i for i in arr[1:] if i >= pivot] 
    return quick_sort(less)+ [pivot] + quick_sort(greater)

print(quick_sort([10,5,2])) """
#----------------------------------------------------------

def merge_sort (nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len (left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    

list2 =[5,9,14,3,8,7,1,17,2]
merge_sort(list2)
print(list2)
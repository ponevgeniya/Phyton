# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности в том же порядке.
# in 7 out [4, 5, 3, 3, 4, 1, 2]        [5, 1, 2]
# in -1 out Negative value of the number of numbers!     []
# in 10 out [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]     [6, 2, 3, 0, 9]

from random import randint
n=int(input("Введите число: "))

list=[randint(1,10) for i in range(n)]

if n < 1:
    print('Вы ввели отрицательное число, длина списка не может быть отрицательной ')
     
print(list)

def Poisk_element(x:int, lst:list):
    count = 0

    for i in range(len(lst)):
        if lst[i] == x:
            count += 1
    return count

 
res_list = []

for i in range(len(list)):
    if Poisk_element(list[i], list) == 1:
        res_list.append(list[i])
        
print(f'Список неповторяющихся эелементов:  {res_list} ')


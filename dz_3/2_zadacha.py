# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in 4 out [2, 5, 8, 10] [20, 40]
# in 5 out [2, 2, 4, 8, 8] [16, 16, 4]


from random import randint
n=int(input("Введите число (размер списка): "))

list=[randint(1,10) for i in range(n)]

print(list)

def Proizvedenie(list):
    rez=[]
    len_list = len (list)

    for i in range(len(list)//2):
        rez.append(list[i]*list([len(list)-i-1]))

    if len(list)%2:
        rez.append(list[list//2])   
    return rez

list = []
rez = []

Proizvedenie (list)
print(rez)
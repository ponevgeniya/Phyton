# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
#  значения которых больше предыдущего элемента. Use comprehension.
# in 9 out [15, 16, 2, 3, 1, 7, 5, 4, 10] [16, 3, 7, 10]
# in 10 out [28, 20, 10, 5, 1, 24, 7, 15, 23, 25] [24, 15, 23, 25]


from random import randint
num=int(input("Введите число: "))

list=[randint(1,10) for i in range(num)]

print(list)

new_list = []

for i in range(len(list)-1):
    n = [list[i]]
    j = i + 1
    m = [list[j]]
    if m > n:
        new_list.append(m)

print(new_list)



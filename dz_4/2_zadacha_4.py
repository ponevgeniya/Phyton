# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in 54 out [2, 3, 3, 3]
# in 9990 out [2, 3, 3, 3, 5, 37]
# in 650 out [2, 5, 5, 13]


def ProstMn(num:int):
    list = []
    i = 2
     
    while i <= num:
        while num % i != 0 and i < num:
            i += 1
      
        if i > 1:
            list.append(i)
    
        num = num // i           
       
    return list


num = int(input("Введите натуральное число: "))

print (f'Простые множители числа: {ProstMn(num)}')
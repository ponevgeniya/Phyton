# Задача 1. Напишите программу, которая на вход принимает цифру, обозначающую день недели, 
# и проверяет является ли этот день выходным.
# 6 - да, 7 - да, 1 - нет

number = int(input("Введите цифру, обозначающую день недели, от 1 до 7: "))

if number==6 or number==7:
    print ('Этот день выходной')
elif number<1 or number>7:
    print ('Это не день недели')
else:
    print('Это будний день')
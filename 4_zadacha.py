# Задача 4. Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0
# 8 -> нет такой четверти

numer = int (input('Введите номер четверти: '))

if numer == 1:
    print ('Точка с возможными координатами в первой четверти- x > 0 и y > 0')
elif numer == 2:
    print ('Точка с возможными координатами во второй четверти- x < 0 и y > 0')
elif numer == 3:
    print ('Точка с возможными координатами в третей четверти- x < 0 и y < 0')
elif numer == 4:
    print ('Точка с возможными координатами в четвертой четверти- x > 0 и y < 0')
else:
    print ('Неверно указано четверть, такой нет')

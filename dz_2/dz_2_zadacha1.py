# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

# in -> out
# 6782 -> 23
# 0.67 -> 13
# 198.45 -> 27

num = float (input("Введите число: "))
sum = float (0)
ostatok = float (0)

ostatok = num%1

while(ostatok != 0):
    num = num * 10
    ostatok = num%1

while (num>0):
    sum+=num%10
    num//=10
 
print (f"Сумма цифр в числе равна:  ", sum)

# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

# in 6 out [2.0, 2.25, 2.37, 2.441, 2.488, 2.522] 14.071

list = [ ]
n = float (input("Введите число n:  "))
end = int(n)
sum = 0


for i in range(1,end+1):
    rez = (round ((1+1/i)**i, 3))
    list.append(rez)
    sum=sum+rez

print(list)
print (round (sum, 3))

# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# 4 -> [1, 2, 6, 24]
# 6 -> [1, 2, 6, 24, 120, 720]

a=[]
n = int(input("Введите число n: "))
f = 1

for i in range(1,n+1):
    f*=i 
    a.append(f)
    
print(a)


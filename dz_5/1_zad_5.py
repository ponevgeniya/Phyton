# Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
# in Number of words: 10
# out авб абв бав абв вба бав вба абв абв абв
     # авб бав вба бав вба

# in Number of words: 6
# out ваб вба абв ваб бва абв
    # ваб вба ваб бва

# in Number of words: -1
# out The data is incorrect


from random import randint

num = int(input('Введите число:  '))
list = ['а', 'б', 'в']

if num < 1:
    print('Вы ввели отрицательное число, данные не верны')

res_list = ''

for i in range (num):
    for j in range(3):
        k = randint (0,2)
        res_list = res_list + list[k]
    
    res_list = res_list + ' '

print(res_list)

string_slova = res_list
new_res = ''

split_str = string_slova.split()
new_str = ' '.join(filter(lambda s: not "абв" in s, split_str))

print(*new_str)






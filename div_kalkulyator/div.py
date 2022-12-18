# Деление комплексных чисел

a = float (input("Введите действительную часть числа a: "))
b = float (input(" Введите мнимую часть числа b: "))
c = float (input("Введите действительную часть числа c: "))
d = float (input(" Введите мнимую часть числа d: "))

def div_complex_number(delimoe: complex, delitel: complex):
    rez = delimoe / delitel
    return rez

delimoe = complex(a, b) 
delitel = complex(c, d) 

rez = div_complex_number(delimoe,delitel)  

print(rez)

# Деление рациональных чисел

def div_rational_number(delimoe: float, delitel: float):
    
    if delitel == 0:
        print("Ошибка, на ноль делить нельзя")
        return 0

    else:
        return delimoe / delitel

delimoe = float(input("Введите делимое m: "))
delitel = float(input("Введите делитель n: "))

rez = div_rational_number(delimoe,delitel)    

print(rez)


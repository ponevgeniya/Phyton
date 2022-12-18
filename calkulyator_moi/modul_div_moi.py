# Создать калькулятор по работе с комплексными и рациональными числами.
# Деление.

  

delimoe = float(input("Введите делимое m: "))
delitel = float(input("Введите делитель n: "))

def div_rational_number(delimoe: float, delitel: float):
    
    if delitel == 0:
        print("Ошибка, на ноль делить нельзя")
        return 0

    else:
        return delimoe / delitel



rez = div_rational_number(delimoe,delitel)    

print(rez)








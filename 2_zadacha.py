# Задача 2. Напишите программу для проверки ложности утверждения:
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                print((w and z) or not y or (x == w))
                print(x,y,z,w)

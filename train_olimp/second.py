import numpy as np

numbers = int(input("Введите, сколько чисел Фибоначчи вы хотите увидеть: "))

Fibbo = np.ones((1, numbers), dtype = int)
Fibbo[0,0] = 0
Fibbo[0,1] = 1

for i in range(2, numbers):
    Fibbo[0,i] = Fibbo[0,i-1] + Fibbo[0,i-2]

print("Первые", numbers, "чисел последовательности Фибоначчи:")
for i in range(0, numbers):
    print(Fibbo[0,i])
def Fibbo(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    else:
        return Fibbo(num-1) + Fibbo(num-2)

num = int(input("Введите, сколько чисел Фибоначчи вы хотите увидеть: "))

for i in range(1, num+1):
    res = Fibbo(i)
    print(f"{i} число Фибоначчи равно {res}")
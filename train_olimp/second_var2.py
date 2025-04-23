def Fibbo(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    else:
        return Fibbo(num-1) + Fibbo(num-2)

num = int(input("Введите, какое число Фибоначчи вы хотите увидеть: "))

result = Fibbo(num)

print(f"{num} число Фибоначчи равно {result}")
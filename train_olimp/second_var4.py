num = int(input("Введите, сколько чисел Фибоначчи вы хотите увидеть: "))

F_prev, F_next = 0, 1

print(f"Первые {num} членов последовательности Фибоначчи равны")
for i in range(0, num):
    print(F_prev)
    F_prev, F_next = F_next, F_prev+F_next

import numpy as np

n = int(input("Введите размер массива: "))

arr = np.random.sample(n)

print(f"начальный массив: {arr}")

sup = arr[0]
for i in range(0, n-1):
    arr[i] = arr[i+1]
arr[-1] = sup

print(f"массив после сдвига: {arr}")
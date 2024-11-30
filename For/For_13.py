#Дано целое число N (> 0). Найти значение выражения 1.1 - 1.2 + 1.3 - ...
N = int(input("Введите число N: "))
m = 0
for i in range(1, N + 1):
    for j in range(0, 10):
        if j % 2 == 1:
            m = m + (i + (j / 10))
        else:
            m = m -(i + (j / 10))
print(m)

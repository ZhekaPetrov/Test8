#Дано целое число N (> 0). Найти квадрат данного числа, используя для его вычисления следующую формулу: 
# N ^ 2 = 1 + 3 + 5 + ... + (2 * N - 1)
N = int(input("Введите целое число N: "))
m = 0
for i in range(1, N + 1):
    m += 2 * i - 1
print(f'{N}^2 = {m}')
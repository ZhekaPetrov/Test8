#найти 10 натуральных чисел, дающих при делении на 2, 2, 4, 5, 6 соответственно остатки 1, 2, 3, 4, 5.
a = 0
b = 0
while True:
    if (a % 2 == 1) and (a % 3 == 2) and (a % 4 == 3) and (a % 5 == 4) and (a % 6 == 5):
        print(a)
        b += 1
    if b == 10:
        break
    a += 1
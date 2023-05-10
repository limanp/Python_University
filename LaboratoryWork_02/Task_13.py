
# Task_12 -----------------------------------------

import math

print("Введіть число a:")
a = int(input())

if 0 <= a <= 50:
    sum = 0
    i = a
    for i in range(a, 50 + 1):
        sum += math.pow(i, 2)
    print("Сума квадратів цілих чисел від", a, "до 50 =", sum)
else:
    print("Помилка!!! Число [а] має бути <= 50 або >= 0")
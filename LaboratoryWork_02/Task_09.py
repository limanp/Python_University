
# Task_09 -----------------------------------------
print("Введіть число a:")
a = int(input())
print("Введіть число b:")
b = int(input())

if a < b:
    sum = 0
    for i in range(a, b + 1):
        sum += i
    print("Сума цілих чисел від", a, "до", b, "=", sum)
else:
    print("Помилка!!! Число [а] має бути меншим за [b]")


# Task_11 -----------------------------------------

print("Введіть число a:")
a = int(input())
print("Введіть число b:")
b = int(input())

if a <= 200:
    if a < b:
        sum = 0
        for i in range(a, b + 1):
            sum += i
        print("Середнє арефметичне цілих чисел від", a, "до", b, "=", sum / b)
    else:
        print("Помилка!!! Число [а] має бути більшим за [b]")
else:
    print("Помилка!!! Число [а] має бути меньше або дорівнювати 200")
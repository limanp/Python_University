
# Task_05 -----------------------------------------

import math

print("Введіть три числа для знаходження сінуса максимального: ")
numbers = [float(input()), float(input()), float(input())]

max = math.sin(numbers[0])
number = numbers[0]

for x in numbers:
    if(math.sin(x) > max):
        max = math.sin(x)
        number = x

print("Сінус максимальний у числа", number, "=", max)

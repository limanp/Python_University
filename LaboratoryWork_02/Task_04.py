
# Task_04 -----------------------------------------

import math

print("Введіть чотири числа для знаходження мінімального косинуса: ")
numbers = [float(input()), float(input()), float(input()), float(input())]

min = math.cos(numbers[0])
number = numbers[0]

for x in numbers:
    if(math.cos(x) < min):
        min = math.cos(x)
        number = x

print("Мінімальний косинус у числа", number, "=", min)
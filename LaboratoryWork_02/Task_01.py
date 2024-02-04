
# Task_01 -----------------------------------------

print("Введіть три числа: ")
numbers = [int(input()), int(input()), int(input())]
i = 0
while i < 3:
    if 1 <= numbers[i] <= 3:
        print(numbers[i])
    i += 1

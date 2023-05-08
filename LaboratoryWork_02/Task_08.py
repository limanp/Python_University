
# Task_08 -----------------------------------------

print("Введіть три числа: ")
numbers = [int(input()), int(input()), int(input())]
count = 0

i = 0
while(i < len(numbers)):
    if(numbers[i] > 0):
        count += 1
    i += 1

print("Кількість позитивних чисел:", count)

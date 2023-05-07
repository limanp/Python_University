# Task_01 -----------------------------------------
import math

print("Введіть три числа: ")
numbers = [int(input()), int(input()), int(input())]
i = 0
while i < 3:
    if 1 <= numbers[i] <= 3:
        print(numbers[i])
    i += 1

# Task_02 -----------------------------------------
print("Введіть номер року: ")
YearNumber = int(input())

# Перевірка на дотатне число
if YearNumber >= 0:
    # Перевірка на кратність числа на 100
    if YearNumber % 100 == 0:
        # Якщо число кратне 400 то рік високосний інакше ні
        if YearNumber % 400 == 0:
            isLeapYear = True
        else:
            isLeapYear = False
    # Якщо рік кратний 4 то він то він високосний
    elif YearNumber % 4 == 0:
        isLeapYear = True
    else:
        isLeapYear = False

    if isLeapYear:
        print("Це високосний рік: 366 днів")
    else:
        print("Це не високосний рік: 365 днів")
else:
    print("Введіть дотатний номер року!!!")

# Task_03 -----------------------------------------
print("Введіть вартість покупки: ")
price = float(input())

# Перевіряємо яку потрібно знижку згідно вартості
if price >= 1000:
    discount = 5
elif price >= 500:
    discount = 3
else:
    discount = 0

# Обчислюємо якщо є знижка та виводимо дані
if discount == 0:
    print("Вартість покупки:")
else:
    print("Вартість покупки з урахуванням знижки", str(discount) + "%:")
print(price - (price / 100 * discount))

# Task_04 -----------------------------------------
print("Введіть чотири числа для знаходження мінімального косинуса: ")
numbers = [float(input()), float(input()), float(input()), float(input())]

min = math.cos(numbers[0])
number = numbers[0]

for x in numbers:
    if(math.cos(x) < min):
        min = math.cos(x)
        number = x

print("Мінімальний косинус у числа", number, "=", min)





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
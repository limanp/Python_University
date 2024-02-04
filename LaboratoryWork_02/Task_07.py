
# Task_07 -----------------------------------------

months = ["January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"]

print("Введіть число місяця для виводу назви на англійськом: ")
monthNumber = int(input())

if(monthNumber > 0 <= 12):
    print(months[monthNumber - 1])
else:
    print("Помилка!!! Такого місяця не має.")

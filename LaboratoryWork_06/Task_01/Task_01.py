import os

if os.path.exists('numbers.txt'):
    myFile = open('numbers.txt', 'r')
    sum = 0
    for number in myFile:
        try:
            sum += int(number)
        except:
            print("Помилка! У файлі є символи, що не являються числами")
    print(sum)
    myFile.close()
else:
    print("Помилка!!! Файлу не існує")



import os

if os.path.exists('numbers.txt'):
    myFile = open('numbers.txt', 'r')
    sum = 0
    for number in myFile:
        try:
            sum += int(number)
        except:
            print("Помилка! У файлі є символи, що не являються числами")
    myFile.close()
    print(sum)
    myFile = open('sum_numbers.txt', 'w')
    myFile.write(f"Сума чисел з файлу numbers.txt = {sum}")
    myFile.close()
else:
    print("Помилка!!! Файлу не існує")



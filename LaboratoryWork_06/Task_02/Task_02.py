
print("Введіть числа через пробіл: ")
numbers = list(map(int, input().split()))

myFile = open('result.txt', 'w+', encoding='UTF-8')

for i in numbers:
    if i % 2 == 0:
        myFile.write(f"Число {i} парне\n")
    else:
        myFile.write(f"число {i} не парне\n")
myFile.close()

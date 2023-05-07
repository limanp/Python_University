# Task_01 -----------------------------------------------------
a = int(input())
b = int(input())
c = float(input())
d = float(input())

# Task_02 -----------------------------------------------------
myList = [a + b, b - c, c / d, d * a, b % c, d // b, c ** a]

# Task_03 -----------------------------------------------------
sizeList = len(myList)

for i in range(sizeList):
   if(myList[i] % 2 == 0):
      print(myList[i])

# Task_04 -----------------------------------------------------
print(myList)
temp = myList[1]
myList[1] = myList[4]
myList[4] = temp
print(myList)

# Task_05 -----------------------------------------------------

name = input()
print("---> Виконав роботу", name,)
print("Висновок:\n"
      "В цій лабораторній роботі було ознайомлено з лінійним алгоритмом на мові Python.\n"
      "Також було розглянуто - Інтегроване середовище розробки (IDE).")






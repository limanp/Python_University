import os
MyFile = open('learning_python.txt', encoding='utf-8')

text = []
for line in MyFile:
    text.append(line.replace("\n", ""))

text = [i.replace("Python", "Swift") for i in text]

print(text)
MyFile.close()

try:
    os.mkdir("newdir")
except:
    print("Файл вже створений!!!")

MyFile = open('./newdir/changLang', 'w', encoding='utf-8')
for line in text:
    MyFile.write(line + "\n")
MyFile.close()

MyFile = open('./newdir/changLang', 'r', encoding='utf-8')

true = []
false = []
print("Фраза про мову є правдивою [так] [ні]: ")

for line in MyFile:
    print(line, end="")
    print("-->", end=" ")
    answer = input()
    if answer == "так":
        true.append(line.replace("\n", ""))
    elif answer == "ні":
        false.append(line.replace("\n", ""))
    else:
        print("Помилка!!! Введіть так або ні")
MyFile.close()

FileFalse = open('./newdir/falseOutput', 'w', encoding='utf-8')
FileTrue = open('./newdir/changLang', 'w', encoding='utf-8')

for line in true:
    FileTrue.write(line + "\n")

for line in false:
    FileFalse.write(line + "\n")

FileFalse.close()
FileTrue.close()


myFile = open('learning_python.txt', encoding='utf-8')
text = []
for line in myFile:
    text.append(line.replace("\n", ""))
    print(line.replace("\n", ""))

text.sort(key=len, reverse=True)
print('\nВідсортований список рядків від найбільшого до найменшого:')
print('--------------------------------------------------')
#print(text)
for line in text:
    print(line)
myFile.close()

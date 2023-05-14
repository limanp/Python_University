
myFile = open('learning_python.txt', encoding='utf-8')
text = []
for line in myFile:
    text.append(line.replace("\n", ""))
    print(line.replace("\n", ""))

text.sort(key=len, reverse=True)
print()
print(text)
myFile.close()

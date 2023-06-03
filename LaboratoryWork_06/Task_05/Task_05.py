from datetime import datetime
import os

def fileRead(path, time):
    with open(path, 'r', encoding='utf-8') as questBook:
        text = ""
        for line in questBook:
            if line[0] == '2':
                line = f"2. Час внесення останніх змін: {time} \n"
            text += line
        questBook.close()
    return text

def fileCreate(path, record, time):
    with open(path, 'w', encoding='utf-8') as questBook:
        questBook.write(f"1. Час створення файлу: {time} \n")
        questBook.write(f"2. Час внесення останніх змін: {time} \n\n")
        questBook.write(f"{record} | час добавлення: {time} \n")

def fileWrite(path, text, record, time):
    text += f"{record} | час добавлення: {time} \n"
    with open(path, 'w', encoding='utf-8') as questBook:
       questBook.write(text)

path = 'quest_book.txt'
print("Введіть їм'я: ")
name = input()
greeting = f"Доброго дня {name}"
print(greeting)

time = datetime.now()
if os.path.isfile(path):
    text = fileRead(path, time)
    fileWrite(path, text, greeting, time)
else:
    fileCreate(path, greeting, time)




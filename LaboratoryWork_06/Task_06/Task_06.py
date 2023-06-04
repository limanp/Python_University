from datetime import datetime
import time
with open('PublicationPython.txt', 'r', encoding='UTF-8') as pubPyFile:
    text = pubPyFile.read()
def strRefactor(word):
    symbols = ['.', ',', ';', '!', '?', '(', ')']
    for symbol in symbols:
        word = word.replace(symbol, '')
    return word.lower()

words = list(map(strRefactor, text.split()))

temp = []
for word in words:
    if word not in temp:
        temp.append(word)


with open('result.txt', 'w', encoding='UTF-8') as resultFile:
    timeCreate = datetime.now()
    start = time.time()
    for word in temp:
        countWord = words.count(word)
        resultFile.write(f"{word} - Кількість повторень: {countWord} | час зміни у файлі: {datetime.now().strftime('%H:%M:%S:%f')}\n")
        print(f"{word} - Кількість повторень: {countWord}")
    end = time.time() - start

    resultFile.write("-----------------------------------------------------------------------------\n")
    resultFile.write(f"Файл було створено: {timeCreate}\n")
    resultFile.write(f"Час на виконання пошуку: {end} секунд\n")
    resultFile.write("-----------------------------------------------------------------------------\n")

print(len(words))

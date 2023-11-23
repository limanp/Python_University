def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def checkRepeatGrade(gradeCheck, grades):
    count = 0
    for grade in grades:
        if float(gradeCheck) == float(grade):
            count = count + 1
    return count



with open('marks.lab6.csv', encoding='UTF-8') as fileMarks:
    studentsGrades = []
    countStudent = 0
    averageGrades = []
    statsStudentResult = []
    for entry in fileMarks:
        student = entry.split(',', 4)

        resultTest = student[4].replace('\",\"', " ").replace('\"', "").replace(',-', ' ').split()
        grade = resultTest[0].replace(',', '.')
        studentsGrades.append(grade)

        leadTime = student[3].replace(' хв ', '.').replace(' сек', '')

        # Розрахунок середньої оцінки с кроком 1 хвилина
        averageGrades.append(float(grade) / (len(resultTest) - 1))

        # Лічильник студентів
        countStudent += 1

        i = 1
        countCorrectAnswer = 0
        while i < len(resultTest):
            if resultTest[i] == "0,50":
                countCorrectAnswer = countCorrectAnswer + 1
            i = i + 1
        statsStudentResult.append(countCorrectAnswer)


print(f'Кількість студентів що проходили тестування: {countStudent}\n')
print(student)
print(statsStudentResult)

grade = 0
while(grade <= 10):
    print(f"Оцінку {grade} отримало = {checkRepeatGrade(grade, studentsGrades)} студ.")
    grade = grade + 0.50


for student in range(1, countStudent + 1):
    print(f'Середня оціка студента {student} с кроком 1 хв. = {averageGrades[student - 1]}')

#with open('result.txt', 'w') as result:
 #   result.write()





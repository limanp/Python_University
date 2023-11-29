NUMBER_QUESTIONS = 20


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def check_repeat_grade(grade_check, grades):
    count = 0
    for gradeSt in grades:
        if float(grade_check) == float(gradeSt):
            count = count + 1
    return count


def separation():
    return "========================================================================\n"


# def replace_min_number(arr, number):
#     index_min_num = arr.index(min(arr))
#     arr[index_min_num] = number


with open('marks.lab6.csv', encoding='UTF-8') as fileMarks:
    studentGrades = []
    countStudent = 0
    averageGrades = []
    statsStudentResult = [0] * NUMBER_QUESTIONS
    leadTimes = []
    for entry in fileMarks:
        student = entry.split(',', 4)

        resultTest = student[4].replace('\",\"', " ").replace('\"', "").replace(',-', ' ').split()
        grade = resultTest[0].replace(',', '.')
        resultTest.pop(0)
        studentGrades.append(grade)

        leadTimes.append(student[3].replace(' хв ', '.').replace(' сек', '').replace(' хв', ''))

        # Розрахунок середньої оцінки с кроком 1 хвилина
        averageGrades.append(float(grade) / (len(resultTest) - 1))

        # Лічильник студентів
        countStudent += 1

        i = 0
        while i < len(resultTest):
            if resultTest[i] == "0,50":
                statsStudentResult[i] = statsStudentResult[i] + 1
            i = i + 1

print(f'Кількість студентів що проходили тестування: {countStudent}\n')

grade = 0
while grade <= 10:
    print(f"Оцінку {grade} отримало = {check_repeat_grade(grade, studentGrades)} студ.")
    grade = grade + 0.50
print(separation())

for student in range(1, countStudent + 1):
    print(f'Середня оцінка студента {student} с кроком 1 хв. = {averageGrades[student - 1]:.2f}')
print(separation())

with open('result.txt', 'w', encoding='UTF-8') as resultFile:
    resultFile.write("Статистика правильних відповідей:\n")
    for question in range(NUMBER_QUESTIONS):
        result = statsStudentResult[question] / countStudent * 100
        resultFile.write(f"\tПитання {question + 1} = {result:.2f} %\n")

    resultFile.write(separation())

    resultFile.write("Статистика неправильних відповідей:\n")
    for question in range(NUMBER_QUESTIONS):
        result = 100 - statsStudentResult[question] / countStudent * 100
        resultFile.write(f"\tПитання {question + 1} = {result:.2f} %\n")

    fiveBestGrades = [8] * 5
    gradesRatioTimes = []
    i = 0
    while i < len(studentGrades):
        gradesRatioTimes.append(float(studentGrades[i]) / float(leadTimes[i]))
        i = i + 1

    resultFile.write(separation())
    resultFile.write("Найкращі 5 оцінок в співвідношенні оцінка/час:\n")
    i = 0
    while i < 5:
        student = gradesRatioTimes.index(max(gradesRatioTimes))
        resultFile.write(f"\tСтудент {student + 1} : Оцінка = {studentGrades[student]}: Час виконання = {leadTimes[student]}\n")
        del gradesRatioTimes[student]
        i = i + 1






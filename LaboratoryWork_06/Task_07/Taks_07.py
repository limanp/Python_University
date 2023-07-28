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

countStudent = 0
with open('marks.lab6.csv', encoding='UTF-8') as fileMarks:
    studentGrades = []
    for entry in fileMarks:
        student = entry.split(',', 4)

        # print(student[4].replace('\",\"', " ").replace('\"', "").replace(',-', ' ').split())
        grade = student[4].replace('\",\"', " ").replace('\"', "").replace(',-', ' ').split()[0].replace(',', '.')
        # print(grade)
        studentGrades.append(grade)

        countStudent += 1

print(f'Кількість студентів що проходили тестування: {countStudent}')

for grade in range(1, 11):
    print(f"Оцінку {grade} отримало = {checkRepeatGrade(grade, studentGrades)}")

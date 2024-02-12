import datetime
import math


# Лабораторна робота №7 Завдання 1.

class Person:
    def __init__(self, surname: str, first_name: str, birth_date: str, nickname=""):
        self._surname = surname
        self._first_name = first_name
        self._nickname = nickname
        self._birth_date = self._date_string_to_datetime(birth_date)

    @property
    def surname(self):
        return self._surname

    @property
    def first_name(self):
        return self._first_name

    @property
    def nickname(self):
        if self._nickname != "":
            return self._nickname
        else:
            print("This person does not have nickname!")

    @property
    def birth_date(self):
        return self._birth_date

    @staticmethod
    def _date_string_to_datetime(birth_date) -> datetime.date:
        date_split = birth_date.split('-')
        year = int(date_split[0])
        month = int(date_split[1])
        day = int(date_split[2])
        return datetime.date(year, month, day)

    def get_age(self) -> str:
        # Даний метод повертає вік користувача контакту

        to_day = datetime.date.today()
        age = (to_day - self._birth_date)
        return str(math.trunc(age.days / 365))

    def get_fullname(self) -> str:
        # Даний метод повертає повне ім'я користувача контакту

        return "{0} {1}".format(self._surname, self._first_name)


def modifier(filename):
    with open(filename, "r") as PersonFile:
        data = PersonFile.readlines()

        i = 0
        while i < len(data):
            data[i] = data[i].replace('\n', '')
            i += 1

        person = Person(data[0], data[1], data[2], data[3])

    with open(filename, "w") as PersonFile:
        PersonFile.write(person.surname + "\n")
        PersonFile.write(person.first_name + "\n")
        PersonFile.write(person.get_fullname() + "\n")
        PersonFile.write(person.nickname + "\n")
        PersonFile.write(str(person.birth_date) + "\n")
        PersonFile.write(person.get_age())


if __name__ == "__main__":
    modifier("PersonFile.txt")

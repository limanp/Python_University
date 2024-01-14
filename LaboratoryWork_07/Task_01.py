import datetime
import math


# Лабораторна робота №7 Завдання 1.

class Person:
    def __init__(self, surname: str, first_name: str, birth_date: str, nickname=""):
        self._surname = surname
        self._first_name = first_name
        self._nickname = nickname
        self._birth_date = self._date_string_to_datetime(birth_date)

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


if __name__ == "__main__":
    b_date = datetime.date(2002, 7, 14)
    person = Person("Liman", "Pavlo", "2002-07-14", "LiPa")
    print(person.get_age())
    print(person.get_fullname())

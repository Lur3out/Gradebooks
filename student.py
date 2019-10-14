from datetime import date


class Student:

    surname = ""
    name = ""
    lastname = ""
    birthDate = date.today()
    faculty = ""
    group = ""
    course = 0

    def __init__(
        self,
        surname,
        name,
        lastname,
        birthDate,
        faculty,
        group,
        course,
    ):
        self.surname = surname
        self.name = name
        self.lastname = lastname
        self.birthDate = birthDate
        self.faculty = faculty
        self.group = group
        self.course = course

    def __repr__(self):
        return F'''
            Фамилия: {self.surname}
            Имя: {self.name}
            Отчество: {self.lastname}
            Дата рождения: {self.birthDate}
            Факультет: {self.faculty}
            Группа: {self.group}
            Курс: {self.course}'''

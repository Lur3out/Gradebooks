from datetime import date
import gradebook


class Student:

    surname = ""
    name = ""
    lastname = ""
    birthDate = date.today()
    faculty = ""
    group = ""
    course = 0
    gradeBook = gradebook.Gradebook()

    def __init__(self):
        self.surname = ""
        self.name = ""
        self.lastname = ""
        self.birthDate = date.today()
        self.faculty = ""
        self.group = ""
        self.course = 0
        self.gradeBook = None

    def Fill(
        self,
        surname,
        name,
        lastname,
        birthDate,
        faculty,
        group,
        course,
        gradeBook
    ):
        self.surname = surname
        self.name = name
        self.lastname = lastname
        self.birthDate = birthDate
        self.faculty = faculty
        self.group = group
        self.course = course
        self.gradeBook = gradeBook

    def Show(self):
        msg = F"""
            Фамилия: {self.surname}
            Имя: {self.name}
            Отчество: {self.lastname}
            Дата рождения: {self.birthDate}
            Факультет: {self.faculty}
            Группа: {self.group}
            Курс: {self.course}
            Номер зачётной книжки: {self.gradeBook.number}
            """
        print(msg)

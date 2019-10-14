from datetime import date
from student import Student
from subject import Subject
from grades import Grades


class Gradebook:

    number = ""
    student = None
    grades = None
    courseWorks = None
    scienceWorks = None

    def __init__(self, number, student):
        self.number = number
        self.student = student
        self.grades = Grades()

    def __repr__(self):
        return F'''
        Зачётная книжка № {self.number}

        Информация о студенте:
        {self.student.__repr__() if (
            self.student is not None
            ) else "Не известно"}

        Данные об успеваемости:
        {self.grades.__repr__() if (
            self.grades is not None
            ) else "Не известно"}

        Курсовые работы:
        {self.courseWorks.__repr__() if (
            self.courseWorks is not None
            ) else "Не известно"}

        Научно-исследовательские работы:
        {self.scienceWorks.__repr__() if (
            self.scienceWorks is not None
            ) else "Не известно"}

        Средний балл:
        {self.grades.Average() if (
            self.grades is not None
            ) else "Не известно"}
        '''

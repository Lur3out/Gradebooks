# PEP8
from datetime import date
from gradebook import Gradebook
from grades import Grades
from student import Student
from subject import Subject
from pyDatalog import pyDatalog


def Show(Obj):
    print(repr(Obj))

if (__name__ == "__main__"):
    pyDatalog.create_terms('X,Y,book, Show, grades, hasGrades, hasKurs, passedSubject')
    s = Student(
        "Аюпов",
        "Александр",
        "Дамирович",
        date(1997, 6, 19),
        "Электротехнический",
        "АСУ2-19-1м",
        1
    )
    book = Gradebook("19-ЭТФ-1248", s)
    grades = book.grades
    kurs1 = dict()
    kurs2 = dict()
    kurs3 = dict()
    kurs4 = dict()
    subject1 = Subject("Философия", "Экзамен", 5)
    subject2 = Subject("Высшая математика", "Экзамен", 4)
    subject3 = Subject("Базы данных", "Экзамен", 5)
    subject4 = Subject("АСОИИУ", "Диф. зачёт", 5)
    kurs1.update({subject1.name: subject1})
    kurs2.update({subject2.name: subject2})
    kurs3.update({subject3.name: subject3})
    kurs4.update({subject4.name: subject4})
    grades.grades.update({1: kurs1})
    grades.grades.update({2: kurs2})
    grades.grades.update({3: kurs3})
    grades.grades.update({4: kurs4})

    + hasGrades(book, grades)

    + (passedSubject[subject1] == grades)
    + (passedSubject[subject2] == grades)
    + (passedSubject[subject3] == grades)
    + (passedSubject[subject4] == grades)

    print("PyDatalog:")
    print(hasGrades(X,Y))
    print("****************************************************************************")
    print(hasGrades(X,grades))
    print("****************************************************************************")
    print(X == passedSubject[Y])
    print("****************************************************************************")
    print(X == passedSubject[subject1])
else:
    print(str('It is a main file, so you cant import it to another module'))


    """card.update ({
        "фамилия" : "Швецов",
        "имя" : "Владислав",
        "отчество" : "Валерьевич",
        "дата рождения" : date(1997, 4, 29),
        "факультет" : "Электротехнический",
        "группа" : "АСУ2-19-1м",
        "курс" : 1 })
    gradebooks.update ({"19-ЭТФ-1257" : card.copy()})
    card.update ({
        "фамилия" : "Клеймёнова",
        "имя" : "Вероника",
        "отчество" : "Альбертовна",
        "дата рождения" : date(1997, 9, 2),
        "факультет" : "Электротехнический",
        "группа" : "АСУ2-19-1м",
        "курс" : 1 })
    gradebooks.update ({"19-ЭТФ-1253" : card.copy()})"""

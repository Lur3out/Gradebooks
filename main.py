# PEP8
from datetime import date
from gradebook import Gradebook
from student import Student
from subject import Subject
from pyDatalog import pyDatalog


def Show(Obj):
    print(repr(Obj))

if (__name__ == "__main__"):
    pyDatalog.create_terms('gradebookList, book, Show, grades')
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
    #book.grades.Add(1, Subject("Философия", "Экзамен", 5))
    + gradebookList(book)
    + hasGrades(gradebookList(book, "19-ЭТФ-1248"), grades)
    + passedSubject((grades == hasGrades(book == gradebookList(book, "19-ЭТФ-1248"))), (1, Subject("Философия", "Экзамен", 5)))
    + passedSubject((grades == hasGrades(book == gradebookList(book, "19-ЭТФ-1248"))), (2, Subject("Высшая математика", "Экзамен", 4)))
    + passedSubject((grades == hasGrades(book == gradebookList(book, "19-ЭТФ-1248"))), (3, Subject("Базы данных", "Экзамен", 5)))
    + passedSubject((grades == hasGrades(book == gradebookList(book, "19-ЭТФ-1248"))), (4, Subject("АСОИИУ", "Диф. зачёт", 5)))
    #book.grades.Add(2, Subject("Высшая математика", "Экзамен", 4))
    #book.grades.Add(3, Subject("Базы данных", "Экзамен", 5))
    #book.grades.Add(4, Subject("АСОИИУ", "Диф. зачёт", 5))

    #gradebookList.append(book)

    #for i in gradebookList:
        #Show(i)
    gradebookList.map(x => Show(x))
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

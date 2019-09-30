# PEP8
from datetime import date
from gradebook import Gradebook
from student import Student

if (__name__ == "__main__"):
    studentList = dict()
    card = dict()
    s = Student()

    s.Fill(
        "Аюпов",
        "Александр",
        "Дамирович",
        date(1997, 6, 19),
        "Электротехнический",
        "АСУ2-19-1м",
        1,
        Gradebook()
    )
    s.gradeBook.SetNumber("19-ЭТФ-1248")
    studentList.update({s.gradeBook.number: s})

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
    for num, st in studentList.items():
        st.Show()
else:
    print(str('It is a main file, so you cant import it to another module'))

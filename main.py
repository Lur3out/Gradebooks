# PEP8
from datetime import date
import gradebook

Gradebook book = new Gradebook()
card = dict()

# Constants
SURNAME = "фамилия"
NAME = "имя"
LASTNAME = "отчество"
BIRTHDATE = "дата рождения"
FACULTY = "факультет"
GROUP = "группа"
COURSE = "курс"

card.update({
    SURNAME: "Аюпов",
    NAME: "Александр",
    LASTNAME: "Дамирович",
    BIRTHDATE: date(1997, 6, 19),
    FACULTY: "Электротехнический",
    GROUP: "АСУ2-19-1м",
    COURSE: 1})

book.addItem("19-ЭТФ-1248", card.copy())

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

book.showList()

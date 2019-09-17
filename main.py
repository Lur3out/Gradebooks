from datetime import date
gradebooks = dict()
card = dict()
card.update ({
    "surname" : "Аюпов",
    "name" : "Александр",
    "lastname" : "Дамирович",
    "birthDate" : date(1997, 6, 19),
    "faculty" : "Электротехнический",
    "group" : "АСУ2-19-1м",
    "course" : 1 })

gradebooks.update ({"19-ЭТФ-1248" : card.copy()})

card.update ({
    "surname" : "Швецов",
    "name" : "Владислав",
    "lastname" : "Валерьевич",
    "birthDate" : date(1997, 4, 29),
    "faculty" : "Электротехнический",
    "group" : "АСУ2-19-1м",
    "course" : 1 })

gradebooks.update ({"19-ЭТФ-1257" : card.copy()})

card.update ({
    "surname" : "Клеймёнова",
    "name" : "Вероника",
    "lastname" : "Альбертовна",
    "birthDate" : date(1997, 9, 2),
    "faculty" : "Электротехнический",
    "group" : "АСУ2-19-1м",
    "course" : 1 })

gradebooks.update ({"19-ЭТФ-1253" : card.copy()})

for x, y in gradebooks.items():
    print(x, y)
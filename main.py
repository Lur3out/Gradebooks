from datetime import date
gradebooks = dict()
card = dict()
card.update ({
    "surname" : "Швецов",
    "name" : "Владислав",
    "lastname" : "Валерьевич",
    "birthDate" : date(1997, 4, 29),
    "faculty" : "Электротехнический",
    "group" : "АСУ2-19-1м",
    "course" : 1 })

gradebooks.update ({"19-ЭТФ-1257" : card})

print (gradebooks)

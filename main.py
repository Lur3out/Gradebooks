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

gradebooks.update ({"19-ЭТФ-1248" : card})

print (gradebooks)
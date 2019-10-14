from subject import Subject
import numpy


class Grades:

    grades = None

    def __init__(self):
        self.grades = {
            1: dict(),
            2: dict(),
            3: dict(),
            4: dict(),
            5: dict(),
            6: dict()
        }

    def Add(self, course, subject):
        if course > 0 and course < 7 and isinstance(course, int):
            self.grades[course].update({subject.name: subject})
        else:
            print("Неверно указан курс обучения")

    def __repr__(self):
        msg = ""
        for i, subs in self.grades.items():
            if (subs is not None):
                msg += F'''
            Курс № {i}:
                '''
                for j, s in subs.items():
                    msg += F'{s.name} ({s.type}): {s.grade}'
        return msg

    def Average(self):
        return numpy.mean(list(map(
            lambda v: numpy.mean(
                list(map(
                    lambda s: s.grade, v.values()
                ))),
            filter(lambda d: len(d) > 0, self.grades.values())
        )))

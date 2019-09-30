from datetime import date


class Gradebook:

    number = ""

    def __init__(self):
        self.number = "00-###-0000"

    def SetNumber(self, number):
        self.number = number

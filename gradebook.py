from datetime import date


class Gradebook:

    gradebooks

    def __init__(self):
        self.gradebooks = dict()

    def showList(self):
        for x, y in self.gradebooks.items():
            print(x, y)

    def addItem(self, key, item):
        self.gradebooks.update(key, item)

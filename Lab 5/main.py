import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def fileReader(file,limit):
    lim = 0
    while True:
        if lim >= limit:
            break
        data = file.readline()
        if not data:
            file.close()
            raise Exception("End of the file!")
            break       
        lim += 1
        yield data

_file = open('c:\\Users\\spies_000\Desktop\\Курушин\\Lab 5\\transactions.csv') 
  
class Application(QWidget):    
    def __init__(self):
        super().__init__()
        self.title = 'Transaction operations in network'
        self.left = 0
        self.top = 0
        self.width = 1450
        self.height = 400
        self.initUI()
        
    def initUI(self):
        # init
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)      
        self.createTable()

        # set layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
        
        # set button
        button = QPushButton('Next chunk', self)
        button.setToolTip('You can get more data if click :)')
        button.move(725,355)

        # binding click events
        button.clicked.connect(self.nextChunkClicked)
        self.tableWidget.doubleClicked.connect(self.cellClicked)

        self.show()

    def createTable(self):
       # creating widget
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setHorizontalHeaderLabels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'])

        # reading horizontal header titles from first row
        for elem in fileReader(_file, 1):            
                line = elem.split(",")
                for col in range(14):
                    self.tableWidget.horizontalHeaderItem(col).setText(line[col])    
        
        self.tableWidget.move(0,0)    
    
    @pyqtSlot()
    def nextChunkClicked(self):        
        try:
            row = 0
            for elem in fileReader(_file, 10):            
                line = elem.split(",")
                for col in range(14):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(line[col]))
                row += 1      
        except Exception as identifier:
            popup = QMessageBox.question(self, 
                                               'End of file', 
                                               "This is the end. Close this app?", 
                                               QMessageBox.Yes)
            if popup == QMessageBox.Yes:
                exit()
          
    def cellClicked(self):
        if self.tableWidget.currentItem():
            QMessageBox.information(self, 'Cell was picked', f'Value is {self.tableWidget.currentItem().text()}')


if __name__ == '__main__':
    application = QApplication(sys.argv)
    ex = Application()
    sys.exit(application.exec_())  
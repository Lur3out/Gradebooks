import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, \
    QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, \
    QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSlot
import os
import threading
import queue
from time import sleep
from PyQt5 import QtGui, uic


class Application(QMainWindow):

    _file = None
    _queue = queue.Queue()

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        QMainWindow.__init__(self)
        rootDirectory = os.path.dirname(os.path.abspath(__file__))

        self.ui = uic.loadUi(rootDirectory + '\\UI.ui', self)
        self.btnBrowse.clicked.connect(self.btnBrowseClicked)
        self.btnNextChunk.clicked.connect(self.btnNextChunkClicked)
        self.initUI()

    # Инициализация интерфейса
    def initUI(self):
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setHorizontalHeaderLabels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'])

    # Запись данных в очередь
    def fileReader(self):
        while True and not self._file.closed:
            data = self._file.readline()
            if not data:
                self._file.close()
                break
            self._queue.put(data)

    # Открытие файла
    def btnBrowseClicked(self):
        pathFile = QFileDialog.getOpenFileName(self, "Choose folder", './', 'CSV files(*.csv)')
        if pathFile[0] != '':
            self._file = open(pathFile[0])
        thread = threading.Thread(target=self.fileReader, name="Th ")
        thread.setDaemon(True)  # позволяет завершать основной поток, не дожидаясь порожденных
        thread.start()
        self.btnNextChunkClicked()

    # Получение следующей порции данных
    def btnNextChunkClicked(self):
        try:
            if self._file is None or self._queue.empty():
                raise Exception("End of file!\nClose this app?")
            # reading horizontal header titles from first row

            """"line = self._queue.get().split(",")
            for col in range(14):
                self.tableWidget.horizontalHeaderItem(col).setText(line[col]) """

            self.currentRow = 0
            for i in range(10):
                elem = self._queue.get()
                line = elem.split(",")
                for col in range(14):
                    self.tableWidget.setItem(i, col, QTableWidgetItem(line[col]))
        except Exception as identifier:
            buttonReply = QMessageBox.question(self,
                                               'Warning!',
                                               str(identifier),
                                               QMessageBox.Yes)
            if buttonReply == QMessageBox.Yes:
                exit()


def main():
    application = QApplication(sys.argv)
    window = Application()
    window.show()
    application.exec_()

if __name__ == '__main__':
    main()

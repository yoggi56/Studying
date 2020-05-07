import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import mainwindow
from shelvebase import PeopleBase
from person import Person

class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_mainwindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fetch_btn.clicked.connect(self.fetch)
        self.update_btn.clicked.connect(self.update)
        self.key = ''
        self.pers = Person()
        self.base = PeopleBase()

    def update(self):
        self.key = self.key_line.text()
        self.pers.name = self.name_line.text()
        self.pers.pay = self.pay_line.text()
        self.pers.job = self.job_line.text()
        self.pers.age = self.age_line.text()
        self.base.update_record(self.key, self.pers)

    def fetch(self):
        self.key = self.key_line.text()
        self.base.fetch_record(self.key)
        self.name_line.setText(self.base.record.name)
        self.age_line.setText(str(self.base.record.age))
        self.pay_line.setText(str(self.base.record.pay))
        self.job_line.setText(self.base.record.job)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

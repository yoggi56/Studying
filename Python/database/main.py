import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import mainwindow
from shelvebase import PeopleBase
from person import Person


class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_mainwindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.key = ''
        self.keylist = list()
        self.pers = Person()
        self.base = PeopleBase()
        self.init_datalist()

        self.fetch_btn.clicked.connect(self.find_record)
        self.update_btn.clicked.connect(self.update_record)
        self.delete_btn.clicked.connect(self.delete_record)
        self.clear_btn.clicked.connect(self.clear_base)

    def init_datalist(self):
        self.keylist = list(self.base.db.keys())
        self.keylist.sort()
        for key in self.keylist:
            self.list_widget.addItem(key)
        self.list_widget.itemClicked.connect(self.list_item_clicked)

    def refresh_list(self):
        self.list_widget.clear()
        self.init_datalist()

    def list_item_clicked(self, item):
        self.key = item.text()
        self.show_data(self.key)

    def update_record(self):
        if self.age_line.text().isalpha():
            QtWidgets.QMessageBox.information(self, "Information", "Field 'Age' has to be a number")
            return
        if int(self.age_line.text()) > 100 or int(self.age_line.text()) < 0 :
            QtWidgets.QMessageBox.information(self, "Information",
                                              """This person doesn't seem to be a human. 
                                              Please, change the age to a number from 0 to 100.""")
            return
        if self.pay_line.text().isalpha():
            QtWidgets.QMessageBox.information(self, "Information", "Field 'Pay' has to be a number")
            return
        if int(self.pay_line.text()) < 0:
            QtWidgets.QMessageBox.information(self, "Information",
                                              "You can't pay people negative salary.")
            return
        self.key = self.key_line.text()
        self.pers.name = self.name_line.text()
        self.pers.pay = self.pay_line.text()
        self.pers.job = self.job_line.text()
        self.pers.age = self.age_line.text()
        self.base.update_record(self.key, self.pers)
        self.refresh_list()

    def find_record(self):
        self.show_data(self.key_line.text())

    def delete_record(self):
        self.base.delete_record('bob')
        self.refresh_list()
        self.clear_textlines()

    def clear_base(self):
        self.base.clear_base()
        self.refresh_list()
        self.clear_textlines()

    def clear_textlines(self):
        self.name_line.setText('')
        self.age_line.setText('')
        self.pay_line.setText('')
        self.job_line.setText('')
        self.key_line.setText('')

    def show_data(self, key):
        self.base.fetch_record(key)
        self.name_line.setText(self.base.record.name)
        self.age_line.setText(str(self.base.record.age))
        self.pay_line.setText(str(self.base.record.pay))
        self.job_line.setText(self.base.record.job)
        self.key_line.setText(key)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

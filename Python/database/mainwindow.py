# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(475, 273)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.key_line = QtWidgets.QLineEdit(self.centralwidget)
        self.key_line.setObjectName("key_line")
        self.verticalLayout.addWidget(self.key_line)
        self.name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.name_line.setObjectName("name_line")
        self.verticalLayout.addWidget(self.name_line)
        self.age_line = QtWidgets.QLineEdit(self.centralwidget)
        self.age_line.setObjectName("age_line")
        self.verticalLayout.addWidget(self.age_line)
        self.job_line = QtWidgets.QLineEdit(self.centralwidget)
        self.job_line.setObjectName("job_line")
        self.verticalLayout.addWidget(self.job_line)
        self.pay_line = QtWidgets.QLineEdit(self.centralwidget)
        self.pay_line.setObjectName("pay_line")
        self.verticalLayout.addWidget(self.pay_line)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)
        self.list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget.setObjectName("list_widget")
        self.gridLayout_2.addWidget(self.list_widget, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fetch_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fetch_btn.setObjectName("fetch_btn")
        self.horizontalLayout_2.addWidget(self.fetch_btn)
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout_2.addWidget(self.update_btn)
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_2.addWidget(self.delete_btn)
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_2.addWidget(self.clear_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        mainwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "People Database"))
        self.label_7.setText(_translate("mainwindow", "Record Info:"))
        self.label.setText(_translate("mainwindow", "Key"))
        self.label_2.setText(_translate("mainwindow", "Name"))
        self.label_3.setText(_translate("mainwindow", "Age"))
        self.label_4.setText(_translate("mainwindow", "Job"))
        self.label_5.setText(_translate("mainwindow", "Pay"))
        self.label_6.setText(_translate("mainwindow", "Records List:"))
        self.fetch_btn.setText(_translate("mainwindow", "Find"))
        self.update_btn.setText(_translate("mainwindow", "Update"))
        self.delete_btn.setText(_translate("mainwindow", "Delete"))
        self.clear_btn.setText(_translate("mainwindow", "Clear"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(215, 206)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        self.horizontalLayout.addLayout(self.verticalLayout_2)
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
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fetch_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fetch_btn.setObjectName("fetch_btn")
        self.horizontalLayout_2.addWidget(self.fetch_btn)
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout_2.addWidget(self.update_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        mainwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "People Database"))
        self.label.setText(_translate("mainwindow", "Key"))
        self.label_2.setText(_translate("mainwindow", "Name"))
        self.label_3.setText(_translate("mainwindow", "Age"))
        self.label_4.setText(_translate("mainwindow", "Job"))
        self.label_5.setText(_translate("mainwindow", "Pay"))
        self.fetch_btn.setText(_translate("mainwindow", "Fetch"))
        self.update_btn.setText(_translate("mainwindow", "Update"))


# Copyright (C) 2019 Kyaw Kyaw Htike @ Ali Abdul Ghafur. All rights reserved.
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWin(object):
    def setupUi(self, MainWin):
        MainWin.setObjectName("MainWin")
        MainWin.resize(1030, 600)
        self.centralwidget = QtWidgets.QWidget(MainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 111, 16))
        self.label.setObjectName("label")
        self.lineEdit_pathToBat = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pathToBat.setGeometry(QtCore.QRect(180, 40, 641, 22))
        self.lineEdit_pathToBat.setObjectName("lineEdit_pathToBat")
        self.pushButton_browseBat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browseBat.setGeometry(QtCore.QRect(850, 40, 93, 28))
        self.pushButton_browseBat.setObjectName("pushButton_browseBat")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 121, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_pathToDirectoryToProcess = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pathToDirectoryToProcess.setGeometry(QtCore.QRect(170, 100, 651, 22))
        self.lineEdit_pathToDirectoryToProcess.setObjectName("lineEdit_pathToDirectoryToProcess")
        self.pushButton_browseDirProcess = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browseDirProcess.setGeometry(QtCore.QRect(850, 100, 93, 28))
        self.pushButton_browseDirProcess.setObjectName("pushButton_browseDirProcess")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 160, 101, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit_output = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_output.setGeometry(QtCore.QRect(40, 220, 951, 321))
        self.textEdit_output.setObjectName("textEdit_output")
        MainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 26))
        self.menubar.setObjectName("menubar")
        MainWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWin)
        self.statusbar.setObjectName("statusbar")
        MainWin.setStatusBar(self.statusbar)

        self.retranslateUi(MainWin)
        self.pushButton_browseDirProcess.clicked.connect(MainWin.browse_directory_to_process)
        self.pushButton_browseBat.clicked.connect(MainWin.browse_path_to_bat)
        self.pushButton_3.clicked.connect(MainWin.gen_code)
        QtCore.QMetaObject.connectSlotsByName(MainWin)

    def retranslateUi(self, MainWin):
        _translate = QtCore.QCoreApplication.translate
        MainWin.setWindowTitle(_translate("MainWin", "MainWindow"))
        self.label.setText(_translate("MainWin", "Path to pyuic5.bat "))
        self.pushButton_browseBat.setText(_translate("MainWin", "Browse"))
        self.label_2.setText(_translate("MainWin", "Directory to process:"))
        self.pushButton_browseDirProcess.setText(_translate("MainWin", "Browse"))
        self.pushButton_3.setText(_translate("MainWin", "Generate code"))


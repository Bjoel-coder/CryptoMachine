# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'App.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Main Screen
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(640, 386)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #background picture
        pixmap = QPixmap("Sources/Picture/background.png")
        label = QtWidgets.QLabel(self.centralwidget)
        label.setGeometry(QtCore.QRect(0, 0, 640, 386))
        label.setPixmap(pixmap)

        #Menubar
        menu = QtWidgets.QWidget(self.centralwidget)
        menu.setGeometry(QtCore.QRect(0, 0, 640, 40))
        menu.setObjectName("menubar")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crypto Machine"))

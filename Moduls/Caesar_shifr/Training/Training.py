# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'App.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from Sources.Gui.Gui_py import Ui_MainWindow
#os.chdir("Moduls")

class Training(Ui_MainWindow):
    def __init__(self):
        super(Training, self).__init__()
        self.setupUi(self)

    def setup(self):
        print(self.n)
        print('hi')

        #FIRST

        self.but = QtWidgets.QPushButton(self.centralwidget)
        self.but.setGeometry(QtCore.QRect(4, 4, 70, 36))
        '''
        self.firstScreen = QtWidgets.QWidget(test)
        self.firstScreen.setGeometry(QtCore.QRect(0, 0, 640, 386))

        self.firstPixmap = QPixmap("1.jpg")
        self.label = QtWidgets.QLabel(self.firstScreen)
        self.label.setGeometry(QtCore.QRect(0, 0, 640, 386))
        self.label.setPixmap(self.firstPixmap)
        '''
        #SECOND

        #HTIRD

        #FOURTH

        #FIFTH

    def show(self):
        self.setup()

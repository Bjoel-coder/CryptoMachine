# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from Sources.Gui import Ui_MainWindow
import sys
import time
import os
from os import remove
from random import choice

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)







app = QApplication([])
application = MainWindow()
qstyle = open("Sources/style.css", "r")
application.setStyleSheet(qstyle.read())
application.show()

sys.exit(app.exec())

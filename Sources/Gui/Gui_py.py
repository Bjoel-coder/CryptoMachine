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
        #############################################################
        #initial values and constants
        self.n = 172
        self.selected_shifr = "Шифр Цезаря"
        self.action = "Зашифровать"
        self.how_work_is = "Как работает " + self.selected_shifr

        #############################################################
        #main screen
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(640, 386)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #############################################################
        #BACKGROUND PICTURE

        self.pixmap = QPixmap("Sources/Picture/background.png")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 640, 386))
        self.label.setPixmap(self.pixmap)

        #############################################################
        #DARK BACKGROUND

        self.dark_background = QtWidgets.QPushButton(self.centralwidget)
        self.dark_background.setGeometry(QtCore.QRect(0, 0, 640, 386))
        self.dark_background.setObjectName("dark_background")
        self.dark_background.hide()

        #############################################################
        #MENUBAR

        #menu place
        self.menu = QtWidgets.QWidget(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(0, 0, 640, 44))
        self.menu.setObjectName("menubar")

        #history button
        self.but_history = QtWidgets.QPushButton(self.menu)
        self.but_history.setGeometry(QtCore.QRect(4, 4, 70, 36))

        #action encode
        self.but_act_encode = QtWidgets.QPushButton(self.menu)
        self.but_act_encode.setGeometry(QtCore.QRect(178, 4, 250, 36))

        #action decode
        self.but_act_decode = QtWidgets.QPushButton(self.menu)
        self.but_act_decode.setGeometry(QtCore.QRect(426, 4, 36, 36))

        #dropdown menu shifr
        self.select_shifr = QtWidgets.QComboBox(self.menu)
        self.select_shifr.setGeometry(QtCore.QRect(506, 4, 130, 36))
        self.select_shifr.addItem("Шифр Цезаря")
        self.select_shifr.addItem("Шифр Виженера")
        self.select_shifr.addItem("Шифр Энигмы")
        self.select_shifr.addItem("Настоящие кода")
        self.select_shifr.addItem("Публичный ключ")
        self.select_shifr.activated[str].connect(self.set_text_how_work_is)


        #############################################################
        #MAIN SCREEN

        #key input
        self.line_inp_key = QtWidgets.QLineEdit(self.centralwidget)
        self.line_inp_key.setGeometry(QtCore.QRect(60, 119, 520, 36))
        self.line_inp_key.setPlaceholderText("Введите ключ")

        #text input
        self.line_inp_text = QtWidgets.QTextEdit(self.centralwidget)
        self.line_inp_text.setGeometry(QtCore.QRect(60, 48, 520, 107))
        self.line_inp_text.setPlaceholderText("Введите текст")

        #button action
        self.but_act = QtWidgets.QPushButton(self.centralwidget)
        self.but_act.setGeometry(QtCore.QRect(60, 159, 520, 36))

        #text output
        self.line_out_text = QtWidgets.QTextEdit(self.centralwidget)
        self.line_out_text.setGeometry(QtCore.QRect(60, 386, 520, 107))

        #key output
        self.line_out_key = QtWidgets.QTextEdit(self.centralwidget)
        self.line_out_key.setGeometry(QtCore.QRect(60, 497, 520, 36))

        #button how
        self.but_how_work = QtWidgets.QPushButton(self.centralwidget)
        self.but_how_work.setGeometry(QtCore.QRect(60, 350, 520, 36))

        #############################################################
        #HISTORY

        #history place
        self.history = QtWidgets.QWidget(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(-320, 0, 320, 500))
        self.history.setObjectName("history")

        self.history_box = QtWidgets.QVBoxLayout(self.history)
        self.history_box.setGeometry(QtCore.QRect(0, 0, 316, 0))
        self.history_box.setContentsMargins(2, 2, 2, 2)
        self.history_box.setSpacing(8)

        self.but_close = QtWidgets.QPushButton(self.history)
        self.but_close.setGeometry(QtCore.QRect(2, 2, 70, 36))

        self.but_clear = QtWidgets.QPushButton(self.history)
        self.but_clear.setGeometry(QtCore.QRect(74, 2, 70, 36))


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def set_text_how_work_is(self, text_how_work_is):
        '''changes the name of the cipher for the bot_how_work button'''
        self.selected_shifr = self.select_shifr.currentText()
        self.how_work_is = "Как работает " + self.selected_shifr
        self.but_how_work.setText(self.how_work_is)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.but_act_encode.setText(_translate("MainWindow", "Зашифровать"))
        self.but_act_decode.setText(_translate("MainWindow", "Р"))
        self.but_act.setText(_translate("MainWindow", self.action))
        self.but_history.setText(_translate("MainWindow", "История"))
        self.but_how_work.setText(_translate("MainWindow", self.how_work_is))
        self.but_close.setText(_translate("MainWindow", "Закрыть"))
        self.but_clear.setText(_translate("MainWindow", "Очистить"))

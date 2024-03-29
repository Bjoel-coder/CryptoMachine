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
        self.action = "Шифрование"
        self.how_work_is = "Как работает " + self.selected_shifr

        #############################################################
        #main screen
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(640, 386)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #############################################################
        #BACKGROUND PICTURE

        self.pixmap = QPixmap("Sources/Picture/background2.png")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 640, 386))
        self.label.setPixmap(self.pixmap)

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
        self.but_act_encode.setToolTip('<b>Нажмите</b>, чтобы изменить действие')
        self.but_act_encode.setObjectName("but_act_encode")

        #action decode
        self.but_act_decode = QtWidgets.QPushButton(self.menu)
        self.but_act_decode.setGeometry(QtCore.QRect(426, 4, 36, 36))
        self.but_act_decode.setToolTip('<b>Нажмите</b>, чтобы изменить действие')
        self.but_act_decode.setObjectName("but_act_decode")

        #dropdown menu shifr
        self.select_shifr = QtWidgets.QComboBox(self.menu)
        self.select_shifr.setGeometry(QtCore.QRect(486, 4, 150, 36))
        self.select_shifr.addItem("Шифр Цезаря")
        self.select_shifr.addItem("Азбука Морзе")
        self.select_shifr.addItem("Шифр Виженера")
        self.select_shifr.addItem("Публичный ключ")
        self.select_shifr.addItem("Настоящие кода")
        #self.select_shifr.addItem("Публичный ключ")

        #############################################################
        #MAIN SCREEN

        #key input
        self.line_inp_key = QtWidgets.QLineEdit(self.centralwidget)
        self.line_inp_key.setGeometry(QtCore.QRect(60, 155, 520, 36))
        self.line_inp_key.setPlaceholderText("Введите ключ")
        self.line_inp_key.setObjectName("line_inp_key")

        #text input
        self.line_inp_text = QtWidgets.QTextEdit(self.centralwidget)
        self.line_inp_text.setGeometry(QtCore.QRect(60, 48, 520, 107))
        self.line_inp_text.setPlaceholderText("Введите текст")
        self.line_inp_text.setObjectName("line_inp_text")

        #button action
        self.but_act = QtWidgets.QPushButton(self.centralwidget)
        self.but_act.setGeometry(QtCore.QRect(60, 191, 520, 36))
        self.but_act.setObjectName("but_act")

        #text output
        self.line_out_text = QtWidgets.QTextEdit(self.centralwidget)
        self.line_out_text.setGeometry(QtCore.QRect(60, 386, 520, 107))
        self.line_out_text.setReadOnly(True)

        #key output
        self.line_out_key = QtWidgets.QTextEdit(self.centralwidget)
        self.line_out_key.setGeometry(QtCore.QRect(60, 497, 520, 36))
        self.line_out_key.setReadOnly(True)

        #button how
        self.but_how_work = QtWidgets.QPushButton(self.centralwidget)
        self.but_how_work.setGeometry(QtCore.QRect(60, 350, 520, 36))
        self.but_how_work.setObjectName("button_how_work")

        #############################################################
        #HOW WORK
        self.place_for_how_work = QtWidgets.QWidget(self.centralwidget)
        self.place_for_how_work.setGeometry(QtCore.QRect(0, 386, 640, 386))

        self.pixmap_for_how_work = QPixmap("Sources/Picture/0.jpg")
        self.bkg_for_how_work = QtWidgets.QLabel(self.place_for_how_work)
        self.bkg_for_how_work.setGeometry(QtCore.QRect(0, 0, 6400, 386))
        self.bkg_for_how_work.setPixmap(self.pixmap_for_how_work)

        self.hboxlayout = QtWidgets.QHBoxLayout(self.place_for_how_work)
        self.hboxlayout.setSpacing(0)

        self.but_close_how_work = QtWidgets.QPushButton(self.centralwidget)
        self.but_close_how_work.setGeometry(QtCore.QRect(611, 390, 24, 24))
        self.cross = QPixmap("Sources/Picture/cross_25.png")
        self.but_close_how_work.setIcon(QtGui.QIcon(self.cross))

        self.but_back_how_work = QtWidgets.QPushButton(self.centralwidget)
        self.but_back_how_work.setGeometry(QtCore.QRect(4, 732, 70, 36))
        self.but_back_how_work.setText("Назад")
        self.but_back_how_work.hide()

        self.but_onward_how_work = QtWidgets.QPushButton(self.centralwidget)
        self.but_onward_how_work.setGeometry(QtCore.QRect(566, 732, 70, 36))
        self.but_onward_how_work.setText("Дальше")

        #############################################################
        #DARK BACKGROUND

        self.dark_background = QtWidgets.QPushButton(self.centralwidget)
        self.dark_background.setGeometry(QtCore.QRect(0, 0, 640, 386))
        self.dark_background.setObjectName("dark_background")
        self.dark_background.hide()

        #############################################################
        #ERROR MESSAGE

        self.error_place = QtWidgets.QWidget(self.centralwidget)
        self.error_place.setGeometry(QtCore.QRect(170, 145, 300, 96))
        self.error_place.setObjectName("error_place")
        self.error_place.hide()

        self.textEdit_error_text = QtWidgets.QTextEdit(self.error_place)
        self.textEdit_error_text.setFixedSize(300, 60)
        #self.textEdit_error_text.setHtml("<center>Текст по центру</center>")
        #self.textEdit_error_text.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_error_text.setReadOnly(True)
        self.textEdit_error_text.setObjectName("textEdit_error_text")

        self.but_error_close = QtWidgets.QPushButton(self.error_place)
        self.but_error_close.setGeometry(QtCore.QRect(0, 60, 300, 36))
        self.but_error_close.setObjectName("but_error_close")

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
        self.but_close.setGeometry(QtCore.QRect(4, 4, 70, 36))

        self.but_clear = QtWidgets.QPushButton(self.history)
        self.but_clear.setGeometry(QtCore.QRect(78, 4, 70, 36))

        #############################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crypto Machine"))
        self.but_act_encode.setText(_translate("MainWindow", "Шифрование"))
        self.but_act_decode.setText(_translate("MainWindow", "Р"))
        self.but_act.setText(_translate("MainWindow", "Зашифровать"))
        self.but_history.setText(_translate("MainWindow", "История"))
        self.but_how_work.setText(_translate("MainWindow", self.how_work_is))
        self.but_close.setText(_translate("MainWindow", "Закрыть"))
        self.but_clear.setText(_translate("MainWindow", "Очистить"))
        self.but_error_close.setText(_translate("MainWindow", "Закрыть"))

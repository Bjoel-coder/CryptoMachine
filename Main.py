# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication
from Sources.Gui.Gui_py import Ui_MainWindow
import sys
import time
import os
from os import remove
from random import choice

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.but_encode_press = False

        self.but_history.clicked.connect(self.btnHistory)
        self.but_close.clicked.connect(self.btnClose)
        self.dark_background.clicked.connect(self.btnClose)
        self.but_act_encode.clicked.connect(self.selectAction)
        self.but_act_decode.clicked.connect(self.selectAction)
        self.but_act.clicked.connect(self.encodeDecode)



    def selectAction(self):
        ###
        if self.action == "Зашифровать":
            self.action = "Расшифровать"

            #Animation for button action decode
            self.anim_but_act_decode = QPropertyAnimation(self.but_act_decode, b"geometry")
            self.anim_but_act_decode.setEndValue(QRect(212, 4, 250, 36))
            self.anim_but_act_decode.setDuration(200)

            #Animation for button action encode
            self.anim_but_act_encode = QPropertyAnimation(self.but_act_encode, b"geometry")
            self.anim_but_act_encode.setEndValue(QRect(178, 4, 36, 36))
            self.anim_but_act_encode.setDuration(200)

            #Animation for line input key
            self.anim_line_inp_key = QPropertyAnimation(self.line_inp_key, b"geometry")
            self.anim_line_inp_key.setEndValue(QRect(60, 159, 520, 36))
            self.anim_line_inp_key.setDuration(200)

            #Animation for button action
            self.anim_but_act = QPropertyAnimation(self.but_act, b"geometry")
            self.anim_but_act.setEndValue(QRect(60, 199, 520, 36))
            self.anim_but_act.setDuration(200)

            #starting animations
            self.anim_but_act_encode.start()
            self.anim_but_act_decode.start()
            self.anim_line_inp_key.start()
            self.anim_but_act.start()

            #moving line_out_key and line_out_text off the screen
            self.line_out_text.move(60, 386)
            self.line_out_key.move(60, 497)

            #set text
            self.but_act_decode.setText('Расшифровать')
            self.but_act_encode.setText('З')
            self.line_inp_text.setText('')
            self.line_out_text.setText('')
            self.line_inp_key.setText('')



        elif self.action == "Расшифровать":
            self.action = "Зашифровать"

            #Animation for button action decode
            self.anim_but_act_decode = QPropertyAnimation(self.but_act_decode, b"geometry")
            self.anim_but_act_decode.setEndValue(QRect(426, 4, 36, 36))
            self.anim_but_act_decode.setDuration(200)

            #Animation for button action encode
            self.anim_but_act_encode = QPropertyAnimation(self.but_act_encode, b"geometry")
            self.anim_but_act_encode.setEndValue(QRect(178, 4, 250, 36))
            self.anim_but_act_encode.setDuration(200)

            #Animation for line input key
            self.anim_line_inp_key = QPropertyAnimation(self.line_inp_key, b"geometry")
            self.anim_line_inp_key.setEndValue(QRect(60, 119, 520, 36))
            self.anim_line_inp_key.setDuration(200)

            #Animation for button action
            self.anim_but_act = QPropertyAnimation(self.but_act, b"geometry")
            self.anim_but_act.setEndValue(QRect(60, 159, 520, 36))
            self.anim_but_act.setDuration(200)

            #starting animations
            self.anim_but_act_encode.start()
            self.anim_but_act_decode.start()
            self.anim_line_inp_key.start()
            self.anim_but_act.start()

            #moving line_out_key and line_out_text off the screen
            self.line_out_text.move(60, 386)
            self.line_out_key.move(60, 497)

            #set text
            self.but_act_encode.setText('Зашифровать')
            self.but_act_decode.setText('Р')
            self.line_inp_text.setText('')
            self.line_out_text.setText('')
            self.line_inp_key.setText('')

    def btnHistory(self):
        self.but_history = QPropertyAnimation(self.history, b"geometry")
        self.but_history.setEndValue(QRect(0, 0, 320, 386))
        self.but_history.setDuration(200)

        self.dark_background.show()
        self.but_history.start()

    def btnClose(self):
        self.but_history = QPropertyAnimation(self.history, b"geometry")
        self.but_history.setEndValue(QRect(-320, 0, 320, 386))
        self.but_history.setDuration(200)

        self.dark_background.hide()
        self.but_history.start()

    def encodeDecode(self):
        if self.action == "Зашифровать":
            #Animation for text out line
            self.anim_line_out_text = QPropertyAnimation(self.line_out_text, b"geometry")
            self.anim_line_out_text.setEndValue(QRect(60, 199, 520, 107))
            self.anim_line_out_text.setDuration(200)

            #Animation for key out line
            self.anim_line_out_key = QPropertyAnimation(self.line_out_key, b"geometry")
            self.anim_line_out_key.setEndValue(QRect(60, 310, 520, 36))
            self.anim_line_out_key.setDuration(200)

            #starting animations
            self.anim_line_out_text.start()
            self.anim_line_out_key.start()

        if self.action == "Расшифровать":
            #Animation for text out line
            self.anim_line_out_text = QPropertyAnimation(self.line_out_text, b"geometry")
            self.anim_line_out_text.setEndValue(QRect(60, 239, 520, 107))
            self.anim_line_out_text.setDuration(200)

            #starting animations
            self.anim_line_out_text.start()






app = QApplication([])
application = MainWindow()
qstyle = open("Sources/CSS/style.css", "r")
application.setStyleSheet(qstyle.read())
application.show()

sys.exit(app.exec())

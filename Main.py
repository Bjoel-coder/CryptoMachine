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

moduls = []
titles = []
classes_shifr = []
main_class = "Caesar_shifr.Caesar()"

moduls_packages = [modul_package for modul_package in os.listdir("Moduls")]
#print(moduls_packages)

for i in range(len(moduls_packages)):
    perm_moduls = [perm_modul for perm_modul in os.listdir("Moduls/"+str(moduls_packages[i])) if perm_modul.endswith("head.txt")]
    moduls.append(perm_moduls[0])
#print(moduls)
for i in range(len(moduls_packages)):
    inspected_file = "Moduls/" + str(moduls_packages[i]) + "/" + str(moduls[i])
    with open(inspected_file, "r", encoding = "utf-8") as file:
        title = file.readline().replace("\n", "")
        comand = file.readline().replace("\n", "")
        class_shifr = file.readline().replace("\n", "")
    titles.append(title)
    classes_shifr.append(class_shifr)
    exec(comand)
    #print(comand)
#print(titles)
#print(classes_shifr)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        #############################################################
        #connection buttons to functions
        self.but_history.clicked.connect(self.btnHistory)
        self.but_close.clicked.connect(self.historyClose)
        self.but_act_encode.clicked.connect(self.selectAction)
        self.but_act_decode.clicked.connect(self.selectAction)
        self.but_act.clicked.connect(self.defineAction)
        self.select_shifr.activated[str].connect(self.set_text_how_work_is)

    def set_text_how_work_is(self, text_how_work_is):
        '''changes the name of the cipher for the bot_how_work button'''
        self.selected_shifr = self.select_shifr.currentText()
        self.how_work_is = "Как работает " + self.selected_shifr
        self.but_how_work.setText(self.how_work_is)
        self.index = titles.index(self.selected_shifr)
        #print(self.index)
        main_class = classes_shifr[self.index]
        #print(main_class)

    def selectAction(self):
        #changing action to decode
        if self.action == "Зашифровка":
            self.action = "Расшифровка"

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
            self.but_act_decode.setText('Расшифровка')
            self.but_act_encode.setText('З')
            self.but_act.setText('Расшифровать')
            self.line_inp_text.setText('')
            self.line_out_text.setText('')
            self.line_inp_key.setText('')

        #changing action to encode
        elif self.action == "Расшифровка":
            self.action = "Зашифровка"

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
            self.but_act_encode.setText('Зашифровка')
            self.but_act_decode.setText('Р')
            self.but_act.setText('Зашифровать')
            self.line_inp_text.setText('')
            self.line_out_text.setText('')
            self.line_inp_key.setText('')

    def btnHistory(self):
        #assignment dark_background to history
        self.dark_background.clicked.connect(self.historyClose)

        #init animation display history place
        self.but_history = QPropertyAnimation(self.history, b"geometry")
        self.but_history.setEndValue(QRect(0, 0, 320, 386))
        self.but_history.setDuration(200)

        #display dark_background
        self.dark_background.show()

        #start animation display history place
        self.but_history.start()

    def historyClose(self):
        #init animation hide history place
        self.but_history = QPropertyAnimation(self.history, b"geometry")
        self.but_history.setEndValue(QRect(-320, 0, 320, 386))
        self.but_history.setDuration(200)

        #hide dark_background
        self.dark_background.hide()

        #start animation hide history place
        self.but_history.start()

    def defineAction(self):
        #definition of action
        if self.action == "Зашифровка":
            self.callEncode()


        #definition of action
        if self.action == "Расшифровка":
            self.callDecode()


    def callEncode(self):
        #Animation for text out line
        self.anim_line_out_text = QPropertyAnimation(self.line_out_text, b"geometry")
        self.anim_line_out_text.setEndValue(QRect(60, 199, 520, 107))
        self.anim_line_out_text.setDuration(200)

        #Animation for key out line
        self.anim_line_out_key = QPropertyAnimation(self.line_out_key, b"geometry")
        self.anim_line_out_key.setEndValue(QRect(60, 310, 520, 36))
        self.anim_line_out_key.setDuration(200)

        #read text from line_inp_text
        text = self.line_inp_text.toPlainText()

        #create object of selected class
        exec("main = " + str(main_class))
        #call function with arguments text
        exec("textAndKey = main.encode(text)")
        text_output, key_output = eval("textAndKey")

        #set text in line_out_text and line_out_key
        self.line_out_text.setText(text_output)
        self.line_out_key.setText(key_output)

        #starting animations
        self.anim_line_out_text.start()
        self.anim_line_out_key.start()

    def callDecode(self):
        #Animation for text out line
        self.anim_line_out_text = QPropertyAnimation(self.line_out_text, b"geometry")
        self.anim_line_out_text.setEndValue(QRect(60, 239, 520, 107))
        self.anim_line_out_text.setDuration(200)

        #read text from line_inp_text
        text = self.line_inp_text.toPlainText()
        #read key from line_inp_key
        key = self.line_inp_key.text()

        #create object of selected class
        exec("main = " + str(main_class))
        #call function with arguments text and key
        exec("text_out = main.decode(text, key)")
        text_output = eval("text_out")

        #set text in line_out_text
        self.line_out_text.setText(text_output)

        #starting animations
        self.anim_line_out_text.start()




app = QApplication([])
application = MainWindow()
qstyle = open("Sources/CSS/style.css", "r")
application.setStyleSheet(qstyle.read())
qstyle.close()
application.show()

sys.exit(app.exec())

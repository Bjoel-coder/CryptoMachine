# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from Sources.Gui.Gui_py import Ui_MainWindow
import sys
import time
import os
from os import remove
from random import choice

moduls = []
titles = []
classes_shifr = []
params_encode_decode = []

class MainWindow(QMainWindow, Ui_MainWindow):
    main_class = "Caesar_shifr.Caesar()"
    index = 0
    begin_free_place = 231
    params_how_work = None
    slide_num = 0
    slide_pos = 0
    width_place_how_work = 640
    input_answer_lines = []
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.but_history.clicked.connect(self.btnHistory)
        self.but_close.clicked.connect(self.historyClose)
        self.but_act_encode.clicked.connect(self.selectAction)
        self.but_act_decode.clicked.connect(self.selectAction)
        self.but_act.clicked.connect(self.defineAction)
        self.select_shifr.activated[str].connect(self.selectShifr)
        self.but_how_work.clicked.connect(self.showHowWork)
        self.but_close_how_work.clicked.connect(self.closeHowWork)
        self.but_back_how_work.clicked.connect(lambda state, shift=-1: self.shiftHowWork(shift))
        self.but_onward_how_work.clicked.connect(lambda state, shift=1: self.shiftHowWork(shift))


    def showHowWork(self):
        self.but_onward_how_work.show()
        self.buildHowWork()

        self.anim_place_for_how_work = QPropertyAnimation(self.place_for_how_work, b"geometry")
        self.anim_place_for_how_work.setEndValue(QRect(0, 0, self.width_place_how_work, 386))
        self.anim_place_for_how_work.setDuration(200)

        self.anim_but_close_how_work = QPropertyAnimation(self.but_close_how_work, b"geometry")
        self.anim_but_close_how_work.setEndValue(QRect(611, 4, 24, 24))
        self.anim_but_close_how_work.setDuration(200)

        self.anim_but_back_how_work = QPropertyAnimation(self.but_back_how_work, b"geometry")
        self.anim_but_back_how_work.setEndValue(QRect(4, 346, 70, 36))
        self.anim_but_back_how_work.setDuration(200)

        self.anim_but_onward_how_work = QPropertyAnimation(self.but_onward_how_work, b"geometry")
        self.anim_but_onward_how_work.setEndValue(QRect(566, 346, 70, 36))
        self.anim_but_onward_how_work.setDuration(200)

        self.anim_place_for_how_work.start()
        self.anim_but_close_how_work.start()
        self.anim_but_back_how_work.start()
        self.anim_but_onward_how_work.start()

    def buildHowWork(self):
        while self.hboxlayout.count():
            item = self.hboxlayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        train_folder = "Moduls/"+str(moduls_packages[self.index])+"/Training"
        print(train_folder)
        train_head = "Moduls/"+str(moduls_packages[self.index])+"/Training/Head.txt"
        print(train_head)
        with open(train_head, "r", encoding="utf-8") as file:
            self.params_how_work = dict(eval(file.readline().replace("\n", "")))
        print(self.params_how_work)
        print(type(self.params_how_work))
        count_slides = int(self.params_how_work["slides"])
        count_theory = int(self.params_how_work["theory"])
        count_question = int(self.params_how_work["question"])
        self.width_place_how_work = 640*count_slides
        print(self.width_place_how_work)
        for i in range(count_slides):
            quest_num = count_question-count_slides+i
            self.lbl_place_how_work = QtWidgets.QLabel()
            bkg = train_folder + "/" + str(i+1) + ".jpg"
            print(bkg)
            self.pixmap_for_lbl = QPixmap(bkg)
            self.lbl_place_how_work.setPixmap(self.pixmap_for_lbl)
            if i < count_theory:
                self.hboxlayout.addWidget(self.lbl_place_how_work)
            else:# i < count_slides:
                self.line_input_answer = QtWidgets.QLineEdit()
                self.line_input_answer.setFixedSize(520, 36)
                self.line_input_answer.setPlaceholderText('Введите ответ')
                self.input_answer_lines.append(self.line_input_answer)

                self.hbl1 = QtWidgets.QHBoxLayout()
                self.hbl1.addWidget(self.line_input_answer)

                self.but_verify_answer = QtWidgets.QPushButton()
                self.but_verify_answer.setFixedSize(520, 36)
                self.but_verify_answer.setText("Проверить")
                self.but_verify_answer.clicked.connect(lambda state, numButton=quest_num: self.but_verify_answer_pushed(numButton))

                self.hbl2 = QtWidgets.QHBoxLayout()
                self.hbl2.addWidget(self.but_verify_answer)

                self.space = QtWidgets.QWidget()

                self.vboxlayout = QtWidgets.QVBoxLayout()
                self.vboxlayout.addWidget(self.lbl_place_how_work)
                self.vboxlayout.addLayout(self.hbl1)
                self.vboxlayout.addLayout(self.hbl2)
                self.vboxlayout.addWidget(self.space)
                self.vboxlayout.setSpacing(8)
                #self.vboxlayout.setContentsMargins(0, 0, 0, 220)

                self.hboxlayout.addLayout(self.vboxlayout)

    def but_verify_answer_pushed(self, numButton):
        train_head = "Moduls/"+str(moduls_packages[self.index])+"/Training/Head.txt"
        with open(train_head, "r", encoding="utf-8") as file:
            file.readline()
            training_datas = dict(eval(file.readline().replace("\n", "")))
        answer = str(training_datas[numButton])
        input_answer = str(self.input_answer_lines[numButton].text())
        if input_answer == answer:
            self.alert("Верный ответ!", "#$/SUCCESS/$#")
        else:
            self.alert("Неверный ответ!", "#$/ERROR/$#")

    def shiftHowWork(self, shift):
        self.slide_num += shift
        shift = self.slide_pos - 640 * shift
        self.slide_pos = shift
        print("slide_num:", self.slide_num)
        print("slide_pos:", self.slide_pos)
        if self.slide_num != 0:
            self.but_back_how_work.show()
        else:
            self.but_back_how_work.hide()

        if self.slide_num != (self.params_how_work["slides"]-1):
            self.but_onward_how_work.show()
        else:
            self.but_onward_how_work.hide()


        self.anim_shift_how_work = QPropertyAnimation(self.place_for_how_work, b"geometry")
        self.anim_place_for_how_work.setEndValue(QRect(shift, 0, self.width_place_how_work, 386))
        self.anim_place_for_how_work.setDuration(200)

        self.anim_place_for_how_work.start()

    def closeHowWork(self):
        self.anim_place_for_how_work = QPropertyAnimation(self.place_for_how_work, b"geometry")
        self.anim_place_for_how_work.setEndValue(QRect(0, 386, 640, 386))
        self.anim_place_for_how_work.setDuration(200)

        self.anim_but_close_how_work = QPropertyAnimation(self.but_close_how_work, b"geometry")
        self.anim_but_close_how_work.setEndValue(QRect(611, 390, 25, 25))
        self.anim_but_close_how_work.setDuration(200)

        self.anim_but_back_how_work = QPropertyAnimation(self.but_back_how_work, b"geometry")
        self.anim_but_back_how_work.setEndValue(QRect(4, 732, 70, 36))
        self.anim_but_back_how_work.setDuration(200)

        self.anim_but_onward_how_work = QPropertyAnimation(self.but_onward_how_work, b"geometry")
        self.anim_but_onward_how_work.setEndValue(QRect(566, 732, 70, 36))
        self.anim_but_onward_how_work.setDuration(200)

        self.anim_place_for_how_work.start()
        self.anim_but_close_how_work.start()
        self.anim_but_back_how_work.start()
        self.anim_but_onward_how_work.start()

        self.but_back_how_work.hide()
        self.slide_num = 0
        self.slide_pos = 0
        self.input_answer_lines = []

    def alert(self, message, type_alert):
        self.dark_background.clicked.connect(self.alertClose)
        self.but_error_close.clicked.connect(self.alertClose)
        self.label_error_text.setText(message)
        if type_alert == "#$/ERROR/$#":
            self.label_error_text.setStyleSheet("color: #ff0000;")
        elif type_alert == "#$/SUCCESS/$#":
            self.label_error_text.setStyleSheet("color: #28a745;")
        self.dark_background.show()
        self.error_place.show()

    def alertClose(self):
        self.error_place.hide()
        self.dark_background.hide()

    def selectShifr(self, text_how_work_is):
        #changes the name of the cipher for the bot_how_work button
        self.selected_shifr = self.select_shifr.currentText()
        self.how_work_is = "Как работает " + self.selected_shifr
        self.but_how_work.setText(self.how_work_is)
        self.index = titles.index(self.selected_shifr)

        #init main_class
        self.main_class = classes_shifr[self.index]

        if (self.action == "Зашифровка") and (params_encode_decode[self.index]["encode"]["encode"] == False):
            self.selectAction()
            self.alert(self.selected_shifr + " нельзя зашифровать!", "#$/ERROR/$#")
        elif (self.action == "Расшифровка") and (params_encode_decode[self.index]["decode"]["decode"] == False):
            self.selectAction()
            self.alert(self.selected_shifr + " нельзя расшифровать!", "#$/ERROR/$#")
        elif (self.action == "Зашифровка") and (params_encode_decode[self.index]["encode"]["encode"] == True):
            if params_encode_decode[self.index]["decode"]["line_inp_key"] == True:
                move_inp_key = 155
                move_but = 191
                self.begin_free_place = 231
            elif params_encode_decode[self.index]["decode"]["line_inp_key"] == False:
                move_inp_key = 119
                move_but = 155
                self.begin_free_place = 195

            #Animation for line input key
            self.anim_line_inp_key = QPropertyAnimation(self.line_inp_key, b"geometry")
            self.anim_line_inp_key.setEndValue(QRect(60, move_inp_key, 520, 36))
            self.anim_line_inp_key.setDuration(200)

            #Animation for button action
            self.anim_but_act = QPropertyAnimation(self.but_act, b"geometry")
            self.anim_but_act.setEndValue(QRect(60, move_but, 520, 36))
            self.anim_but_act.setDuration(200)

            self.anim_line_inp_key.start()
            self.anim_but_act.start()

        elif (self.action == "Расшифровка") and (params_encode_decode[self.index]["decode"]["decode"] == True):
            if params_encode_decode[self.index]["decode"]["line_inp_key"] == True:
                move_inp_key = 155
                move_but = 191
                self.begin_free_place = 231
            elif params_encode_decode[self.index]["decode"]["line_inp_key"] == False:
                move_inp_key = 119
                move_but = 155
                self.begin_free_place = 195

            #Animation for line input key
            self.anim_line_inp_key = QPropertyAnimation(self.line_inp_key, b"geometry")
            self.anim_line_inp_key.setEndValue(QRect(60, move_inp_key, 520, 36))
            self.anim_line_inp_key.setDuration(200)

            #Animation for button action
            self.anim_but_act = QPropertyAnimation(self.but_act, b"geometry")
            self.anim_but_act.setEndValue(QRect(60, move_but, 520, 36))
            self.anim_but_act.setDuration(200)

            self.anim_line_inp_key.start()
            self.anim_but_act.start()

        #clear text
        self.line_inp_text.setText("")
        self.line_inp_key.setText("")
        self.line_out_text.move(60, 386)
        self.line_out_text.setText("")
        self.line_out_key.move(60, 497)
        self.line_out_key.setText("")

    def selectAction(self):
        #changing action to decode
        if self.action == "Зашифровка":
            if params_encode_decode[self.index]["decode"]["decode"] == True:
                self.action = "Расшифровка"
                if params_encode_decode[self.index]["decode"]["line_inp_key"] == True:
                    move_inp_key = 155
                    move_but = 191
                    self.begin_free_place = 231
                elif params_encode_decode[self.index]["decode"]["line_inp_key"] == False:
                    move_inp_key = 119
                    move_but = 155
                    self.begin_free_place = 195

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
                self.anim_line_inp_key.setEndValue(QRect(60, move_inp_key, 520, 36))
                self.anim_line_inp_key.setDuration(200)

                #Animation for button action
                self.anim_but_act = QPropertyAnimation(self.but_act, b"geometry")
                self.anim_but_act.setEndValue(QRect(60, move_but, 520, 36))
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
            elif params_encode_decode[self.index]["decode"]["decode"] == False:
                self.alert(self.selected_shifr + " нельзя расшифровать!", "#$/ERROR/$#")

        #changing action to encode
        elif self.action == "Расшифровка":
            if params_encode_decode[self.index]["encode"]["encode"] == True:
                self.action = "Зашифровка"
                if params_encode_decode[self.index]["encode"]["line_inp_key"] == True:
                    move_inp_key = 155
                    move_but = 191
                    self.begin_free_place = 231
                elif params_encode_decode[self.index]["encode"]["line_inp_key"] == False:
                    move_inp_key = 119
                    move_but = 155
                    self.begin_free_place = 195

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
                self.anim_line_inp_key.setEndValue(QRect(60, move_inp_key, 520, 36))
                self.anim_line_inp_key.setDuration(200)

                #Animation for button action
                self.anim_but_act = QPropertyAnimation(self.but_act, b"geometry")
                self.anim_but_act.setEndValue(QRect(60, move_but, 520, 36))
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
            elif params_encode_decode[self.index]["encode"]["encode"] == False:
                self.alert(self.selected_shifr + " нельзя зашифровать!", "#$/ERROR/$#")

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
        if params_encode_decode[self.index]["encode"]["line_out_text"] == True:
            move_out_text = self.begin_free_place
        else:
            move_out_text = 386
        if params_encode_decode[self.index]["encode"]["line_out_key"] == True:
            move_out_key = move_out_text + 4 + 107
        else:
            move_out_key = 497
        #Animation for text out line
        self.anim_line_out_text = QPropertyAnimation(self.line_out_text, b"geometry")
        self.anim_line_out_text.setEndValue(QRect(60, move_out_text, 520, 107))
        self.anim_line_out_text.setDuration(200)

        #Animation for key out line
        self.anim_line_out_key = QPropertyAnimation(self.line_out_key, b"geometry")
        self.anim_line_out_key.setEndValue(QRect(60, move_out_key, 520, 36))
        self.anim_line_out_key.setDuration(200)

        #read text from line_inp_text
        text = self.line_inp_text.toPlainText()
        #create object of selected class
        exec("main = " + str(self.main_class))

        if params_encode_decode[self.index]["encode"]["line_inp_key"] == True:
            key = self.line_inp_key.text()
            #call function with arguments text
            exec("func = main.encode(text, key)")
            text_output, key_output, alert_type = eval("func")
        else:
            #call function with arguments text
            exec("func = main.encode(text)")
            text_output, key_output, alert_type = eval("func")

        if alert_type == "":
            #set text in line_out_text and line_out_key
            self.line_out_text.setText(text_output)
            self.line_out_key.setText(key_output)

            #starting animations
            self.anim_line_out_text.start()
            self.anim_line_out_key.start()

        else:
            message = text_output
            print(alert_type)
            self.alert(message, alert_type)

    def callDecode(self):
        if params_encode_decode[self.index]["decode"]["line_out_text"] == True:
            move_out_text = self.begin_free_place
        else:
            move_out_text = 386
        if params_encode_decode[self.index]["decode"]["line_out_key"] == True:
            move_out_key = move_out_text + 4 + 107
        else:
            move_out_key = 497
        #Animation for text out line
        self.anim_line_out_text = QPropertyAnimation(self.line_out_text, b"geometry")
        self.anim_line_out_text.setEndValue(QRect(60, move_out_text, 520, 107))
        self.anim_line_out_text.setDuration(200)

        #Animation for key out line
        self.anim_line_out_key = QPropertyAnimation(self.line_out_key, b"geometry")
        self.anim_line_out_key.setEndValue(QRect(60, move_out_key, 520, 36))
        self.anim_line_out_key.setDuration(200)

        #read text from line_inp_text
        text = self.line_inp_text.toPlainText()
        #create object of selected class
        exec("main = " + str(self.main_class))

        if params_encode_decode[self.index]["decode"]["line_inp_key"] == True:
            #read key from line_inp_key
            key = self.line_inp_key.text()
            #call function with arguments text and key
            exec("func = main.decode(text, key)")
        else:
            #call function with arguments text
            exec("func = main.decode(text)")
        text_output, key_output, alert_type = eval("func")

        if alert_type == "":
            #set text in line_out_text
            self.line_out_text.setText(text_output)
            self.line_out_key.setText(key_output)

            #starting animations
            self.anim_line_out_key.start()
            self.anim_line_out_text.start()
        else:
            message = text_output
            self.alert(message, alert_type)

#INIT moduls, classes, titles, params_encode_decode
moduls_packages = [modul_package for modul_package in os.listdir("Moduls")]
print(moduls_packages)

for i in range(len(moduls_packages)):
    perm_moduls = [perm_modul for perm_modul in os.listdir("Moduls/"+str(moduls_packages[i])) if perm_modul.endswith("head.txt")]
    moduls.append(perm_moduls[0])
for i in range(len(moduls_packages)):
    inspected_file = "Moduls/" + str(moduls_packages[i]) + "/" + str(moduls[i])
    with open(inspected_file, "r", encoding = "utf-8") as file:
        titles.append(file.readline().replace("\n", ""))
        comand = file.readline().replace("\n", "")
        classes_shifr.append(file.readline().replace("\n", ""))
        params_encode_decode.append(dict(eval(file.readline().replace("\n", ""))))
    exec(comand)

class Alert(MainWindow):
    def alert(self, message, type_alert):
        self.dark_background.clicked.connect(self.alertClose)
        self.but_error_close.clicked.connect(self.alertClose)
        self.label_error_text.setText(message)
        if type_alert == "#$/ERROR/$#":
            print("ку")
        elif type_alert == "#$/SUCCESS/$#":
            pass
        self.dark_background.show()
        self.error_place.show()

    def alertClose(self):
        self.error_place.hide()
        self.dark_background.hide()



#APPLICATION
app = QApplication([])
application = MainWindow()
qstyle = open("Sources/CSS/style.css", "r")
application.setStyleSheet(qstyle.read())
qstyle.close()
application.show()

sys.exit(app.exec())

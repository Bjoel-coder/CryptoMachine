from kivy.app import App

from kivy.config import Config

from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.animation import Animation

from os import remove
from random import choice

import Value_for_keys
from Pmodul import coder
from Pmodul import decoder

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '386')



class TestApp(App):
    def uncode(self, test):
        file = open("test.txt", "w")
        lib_lib=["Libraries/Lib2_1.txt", "Libraries/Lib2_2.txt", \
        "Libraries/Lib2_3.txt", "Libraries/Lib3_1.txt", "Libraries/Lib3_2.txt", \
        "Libraries/Lib3_3.txt", "Libraries/Lib4_1.txt", "Libraries/Lib4_2.txt", \
        "Libraries/Lib4_3.txt", "Libraries/Lib5_1.txt", "Libraries/Lib5_2.txt", \
        "Libraries/Lib5_3.txt"]

        keys_21=[]
        Value_for_keys.k21(keys_21)

        keys_22=[]
        Value_for_keys.k22(keys_22)

        keys_23=[]
        Value_for_keys.k23(keys_23)

        keys_31=[]
        Value_for_keys.k31(keys_31)

        keys_32=[]
        Value_for_keys.k32(keys_32)

        keys_33=[]
        Value_for_keys.k33(keys_33)

        keys_41=[]
        Value_for_keys.k41(keys_41)

        keys_42=[]
        Value_for_keys.k42(keys_42)

        keys_43=[]
        Value_for_keys.k43(keys_43)

        keys_51=[]
        Value_for_keys.k51(keys_51)

        keys_52=[]
        Value_for_keys.k52(keys_52)

        keys_53=[]
        Value_for_keys.k53(keys_53)

        text_input = self.text_shifr.text
        text_key = self.text_key.text
        if self.text_key.text in keys_21 or self.text_key.text in keys_22 \
        or self.text_key.text in keys_23 or self.text_key.text in keys_31 \
        or self.text_key.text in keys_32 or self.text_key.text in keys_33 \
        or self.text_key.text in keys_41 or self.text_key.text in keys_42 \
        or self.text_key.text in keys_43 or self.text_key.text in keys_51 \
        or self.text_key.text in keys_52 or self.text_key.text in keys_53:
            if text_key in keys_21:
                library=lib_lib[0]
                k=2
            elif text_key in keys_22:
                library=lib_lib[1]
                k=2
            elif text_key in keys_23:
                library=lib_lib[2]
                k=2
            elif text_key in keys_31:
                library=lib_lib[3]
                k=3
            elif text_key in keys_32:
                library=lib_lib[4]
                k=3
            elif text_key in keys_33:
                library=lib_lib[5]
                k=3
            elif text_key in keys_41:
                library=lib_lib[6]
                k=4
            elif text_key in keys_42:
                library=lib_lib[7]
                k=4
            elif text_key in keys_43:
                library=lib_lib[8]
                k=4
            elif text_key in keys_51:
                library=lib_lib[9]
                k=5
            elif text_key in keys_52:
                library=lib_lib[10]
                k=5
            elif text_key in keys_53:
                library=lib_lib[11]
                k=5

            n_key=len(text_key)
            text= self.text_shifr.text
            n_text=len(text)  # считает колво символов в шифре
            n = int(n_text / k)
            word_2 = []
            file.write(text)
            file.close()

            file = open("test.txt", "r")
            for i in range(n):
                decoder(library, k, word_2, file) # Декодирует шифр
            file.close()

            file = open("test.txt", "w")
            n = int(n_text / k)
            for i in range(n):
                file.write(word_2[i])
            file.close()
            file = open("test.txt", "r")
            text_output=file.read()
            self.text_uncode.text= "Результат расшифровки:\n{0}".format(text_output)
            file.close()
            remove("test.txt")
        else:
            self.text_uncode.text= "Неверный ключ"
    def code(self, test):
        lib_lib=["Libraries/Lib2_1.txt", "Libraries/Lib2_2.txt", \
        "Libraries/Lib2_3.txt", "Libraries/Lib3_1.txt", "Libraries/Lib3_2.txt", \
        "Libraries/Lib3_3.txt", "Libraries/Lib4_1.txt", "Libraries/Lib4_2.txt", \
        "Libraries/Lib4_3.txt", "Libraries/Lib5_1.txt", "Libraries/Lib5_2.txt", \
        "Libraries/Lib5_3.txt"]
        text_input= self.text_input.text

        keys_21=[]
        Value_for_keys.k21(keys_21)

        keys_22=[]
        Value_for_keys.k22(keys_22)

        keys_23=[]
        Value_for_keys.k23(keys_23)

        keys_31=[]
        Value_for_keys.k31(keys_31)

        keys_32=[]
        Value_for_keys.k32(keys_32)

        keys_33=[]
        Value_for_keys.k33(keys_33)

        keys_41=[]
        Value_for_keys.k41(keys_41)

        keys_42=[]
        Value_for_keys.k42(keys_42)

        keys_43=[]
        Value_for_keys.k43(keys_43)

        keys_51=[]
        Value_for_keys.k51(keys_51)

        keys_52=[]
        Value_for_keys.k52(keys_52)

        keys_53=[]
        Value_for_keys.k53(keys_53)

        file = open("test.txt", "w")

        library=choice(lib_lib)
        if library in lib_lib[0]:
            key=choice(keys_21)
        elif library in lib_lib[1]:
            key=choice(keys_22)
        elif library in lib_lib[2]:
            key=choice(keys_23)
        elif library in lib_lib[3]:
            key=choice(keys_31)
        elif library in lib_lib[4]:  # Подбирает ключ для библиотеки
            key=choice(keys_32)
        elif library in lib_lib[5]:
            key=choice(keys_33)
        elif library in lib_lib[6]:
            key=choice(keys_41)
        elif library in lib_lib[7]:
            key=choice(keys_42)
        elif library in lib_lib[8]:
            key=choice(keys_43)
        elif library in lib_lib[9]:
            key=choice(keys_51)
        elif library in lib_lib[10]:
            key=choice(keys_52)
        elif library in lib_lib[11]:
            key=choice(keys_53)

        n = len(str(text_input))
        for i in range(n):
            a = text_input[i]
            coder(library, a, file)
        file.close()


        file = open("test.txt", "r")
        text_output = file.read()
        file.close()

        self.text_code.text = "Результат кодировки:\n{}".format(text_output)
        self.text_key_for_code.text = "Ключ для расшифровки:\n{}".format(key)

        remove("test.txt")

    def slip_1(self, instance):
        self.anim.start(self.bl)
        self.anim_2.start(self.bl_2)
        self.anim_4.start(self.but_back_1)

    def slip_2(self, instance):
        self.anim.start(self.bl)
        self.anim_2.start(self.bl_4)
        self.anim_4.start(self.but_back_2)

    def back_1(self, instance):
        self.anim_2.start(self.bl)
        self.anim_3.start(self.bl_2)
        self.anim_5.start(self.but_back_1)

    def back_2(self, instance):
        self.anim_2.start(self.bl)
        self.anim_3.start(self.bl_4)
        self.anim_5.start(self.but_back_2)

    def build(self):
        self.anim = Animation(x=-640+96)
        self.anim_2 = Animation(x=96)
        self.anim_3 = Animation(x=640+96)
        self.anim_4 = Animation(x=0)
        self.anim_5 = Animation(x=640)
        screen = Widget(size_hint = (1, 3))
        al = AnchorLayout(anchor_x = 'center', anchor_y = 'center')
        lbl = Label(text='Выберите действие', color = [0, 0, 0, 1])
        self.bl = BoxLayout(orientation='vertical', size = (448, 232), spacing=10, pos = (96, 77))
        self.bl_2 = BoxLayout(orientation='vertical', size = (448, 232), spacing=10, pos = (640+96, 77))
        bl_3 = BoxLayout(orientation='horizontal', spacing=10)
        self.bl_4 = BoxLayout(orientation='vertical', size = (448, 232), spacing=10, pos = (640+96, 77))
        bl_5 = BoxLayout(orientation='horizontal', spacing=10)
        but_1= Button(text="Расшифровать", on_press = self.slip_1)
        but_2= Button(text="Зашифровать", on_press = self.slip_2)
        but_3= Button(text="расшифровать", size_hint = (.5, 1), on_press = self.uncode)
        but_4= Button(text="Зашифровать", size_hint = (.5, 1), on_press = self.code)
        self.but_back_1= Button(text="Назад", size = (96, 39), on_press = self.back_1, pos = (640, 0))
        self.but_back_2= Button(text="Назад", size = (96, 39), on_press = self.back_2, pos = (640, 0))
        img = Image(source='background.png', size=(640, 386))
        widg = Widget()
        self.text_key = TextInput(text='Введите ключ')
        self.text_shifr = TextInput(text='Введите текст')
        self.text_uncode = TextInput(text='Результат расшифровки:')
        self.text_input = TextInput(text='Введите текст')
        self.text_code = TextInput(text='Результат кодировки:')
        self.text_key_for_code = TextInput(text='Ключ для расшифровки:')

        widg.add_widget(img)
        screen.add_widget( widg )
        al.add_widget( screen )
        self.bl.add_widget( lbl )
        self.bl.add_widget( but_1 )
        self.bl.add_widget( but_2 )
        screen.add_widget( self.bl )
        self.bl_2.add_widget( self.text_shifr )
        bl_3.add_widget( self.text_key )
        bl_3.add_widget (but_3)
        self.bl_2.add_widget( bl_3 )
        self.bl_2.add_widget( self.text_uncode )
        screen.add_widget( self.bl_2 )
        bl_5.add_widget( self.text_input )
        bl_5.add_widget( but_4 )
        self.bl_4.add_widget( bl_5 )
        self.bl_4.add_widget( self.text_code )
        self.bl_4.add_widget( self.text_key_for_code )
        screen.add_widget( self.bl_4 )
        screen.add_widget( self.but_back_1 )
        screen.add_widget( self.but_back_2 )

        return al

if __name__ == "__main__":
    TestApp().run()

# -*- coding: utf-8 -*-
class Vigenere:
    #RUS
    symbolsRus = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я")

    #ENG
    symbolsEng = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

    #NUMBERS
    numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

    lib = (symbolsRus, symbolsEng, numbers)

    def encode(self, text_input, key_input):
        return self.shifr("encode", text_input, key_input)

    def decode(self, text_input, key_input):
        return self.shifr("decode", text_input, key_input)

    def shifr(self, action, text_input, key_input):
        l = 0
        text_input = text_input.strip().lower()
        if text_input == "":
            return "Введите текст!", "", "#$/ERROR/$#"
        if key_input == "":
            return "Введите ключ!", "", "#$/ERROR/$#"
        key = key_input
        for i in range(len(key)):
            if (key[i] not in self.symbolsRus) and (key[i] not in self.symbolsEng) and (key[i] not in self.numbers):
                return "Ключ должен быть только буквой или цифрой!", "", "#$/ERROR/$#"
        text = list(text_input)
        count = len(text)
        for i in range(count):
            alphabet_text = None
            alphabet_key = None
            for j in range(3):
                if text[i] in self.lib[j]:
                    alphabet_text = self.lib[j]
                    len_alphabet_text = len(alphabet_text)
                if key[l] in self.lib[j]:
                    alphabet_key = self.lib[j]
                    len_alphabet_key = len(alphabet_key)
            if (alphabet_text != None):
                if action == "encode":
                    ind = alphabet_text.index(text[i]) + alphabet_key.index(key[l]) + 1
                    ind = ind%len_alphabet_text
                    text[i] = alphabet_text[ind]
                    print(text[i])
                    if l == len(key)-1:
                        l = 0
                    else:
                        l += 1
                else:
                    key_index = alphabet_key.index(key[l])%len_alphabet_text
                    ind = alphabet_text.index(text[i]) - key_index - 1
                    if ind<0:
                        ind = len_alphabet_text+ind
                        text[i] = alphabet_text[ind]
                    else:
                        text[i] = alphabet_text[ind]
                    if l == len(key)-1:
                        l = 0
                    else:
                        l += 1
            else:
                l += 1

        text = "".join(text)
        text_output = str(text)
        key_output = str(key)
        return text_output, "", ""

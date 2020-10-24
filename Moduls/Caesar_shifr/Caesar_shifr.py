class Caesar:
    #RUS
    symbolsRus = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я")

    #ENG
    symbolsEng = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

    #NUMBERS
    numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

    lib = (symbolsRus, symbolsEng, numbers)

    def encode(self, text_input, key_input):
        if text_input != "":
            try:
                key  = int(key_input)
                if (key >= 0) and (key <= 100):
                    text = list(text_input)
                    count = len(text)
                    for i in range(count):
                        alphabet = None
                        for j in range(3):
                            if text[i] in self.lib[j]:
                                alphabet = self.lib[j]
                                len_alphabet = len(alphabet)
                                break
                        if alphabet != None:
                            ind = alphabet.index(text[i]) + key
                            ind = ind%len_alphabet
                            text[i] = alphabet[ind]
                        else:
                            pass

                    text = "".join(text)
                    text_output = str(text)
                    key_output = str(key)
                    return text_output, "", None
                else:
                    return "Ключ должен быть числом >=0 и <=100!", "", "#$/ERROR/$#"
            except:
                return "Ключ должен быть числом >=0 и <=100!", "", "#$/ERROR/$#"
        else:
            return "Введите текст!", "", "#$/ERROR/$#"


    def decode(self, text_input, key_input):
        if text_input != "":
            text = list(text_input)
            try:
                key = int(key_input)
                if (key >= 0) and (key <= 100):
                    count = len(text)
                    for i in range(count):
                        alphabet = None
                        for j in range(3):
                            if text[i] in self.lib[j]:
                                alphabet = self.lib[j]
                                len_alphabet = len(alphabet)
                                break
                        if alphabet != None:
                            key = key%len_alphabet
                            ind = alphabet.index(text[i]) - key
                            if ind<0:
                                ind = len_alphabet+ind
                                text[i] = alphabet[ind]
                            else:
                                text[i] = alphabet[ind]
                        else:
                            pass
                    text = "".join(text)
                    text_output = str(text)
                    return text_output, "", None
                else:
                    return "Ключ должен быть числом >=0 и <=100!", "", "#$/ERROR/$#"
            except:
                if key_input == "":
                    return "Введите ключ!", None, "#$/ERROR/$#"
                else:
                    return "Ключ должен быть числом >=0 и <=100!", None, "#$/ERROR/$#"
        else:
            return "Введите текст!", "", "#$/ERROR/$#"
